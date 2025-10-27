
from observability_setup import setup_observability
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict, Field
from typing import List, Dict
import joblib, json, time
from pathlib import Path
import numpy as np


APP_VERSION = "0.1.0"
ARTIFACTS_DIR = Path("artifacts")
MODEL_PATH = ARTIFACTS_DIR / "model.joblib"
COLUMNS_PATH = ARTIFACTS_DIR / "feature_columns.json"
META_PATH = ARTIFACTS_DIR / "metadata.json"

app = FastAPI(title="ML API", version=APP_VERSION)

setup_observability(app)
# Variables globales que se cargarán al inicio
model = None
columns = []
meta = {}
label_map = {0: "Setosa", 1: "Versicolor", 2: "Virginica"} #traduce la etiqueta en predicciones


# TODO: Define tus modelos Pydantic aquí

class Sample(BaseModel):
    model_config = ConfigDict(extra="forbid")
    # ---- COMPLETA CON TUS CAMPOS SEGÚN feature_columns.json ----

    sepal_length_cm: float = Field(..., ge=3.0, le=8.5, description="Longitud del sépalo en cm")
    sepal_width_cm: float = Field(..., ge=1.5, le=5.0, description="Ancho del sépalo en cm")
    petal_length_cm: float = Field(..., ge=0.5, le=7.5, description="Longitud del pétalo en cm")
    petal_width_cm: float = Field(..., ge=0.0, le=3.0, description="Ancho del pétalo en cm")


class PredictionOut(BaseModel):
    # ---- COMPLETA: qué devuelves? label / score / probs / latencia ----

    label_id: int = Field(..., description="ID de la categoria predicha")
    label_name: str = Field(..., description="Nombre de la categoria predicha.")
    score: float = Field(..., ge=0.0, le=1.0, description="confianza de la predicción.")
    latency_ms: float = Field(..., gr=0, description="Tiempo de procesamiento de la predicción en milisegundos.")
    pass

@app.on_event("startup")
def load_artifacts():
    global model, columns, meta
    if not MODEL_PATH.exists():
        raise RuntimeError("Modelo no encontrado. Entrena y exporta primero.")
    model = joblib.load(MODEL_PATH)
    columns = json.loads(COLUMNS_PATH.read_text())["feature_columns"]
    meta = json.loads(META_PATH.read_text()) if META_PATH.exists() else {}


def prepare_data_for_model(data_samples: List[Sample], columns: List[str]) -> np.ndarray:
    # Convertir cada Sample a un diccionario
    data_dicts = [sample.model_dump() for sample in data_samples]

    # Crear la matriz NumPy en el orden correcto
    X_input = []
    for d in data_dicts:
        # Asegura que los valores se extraigan en el orden de 'columns'
        row = [d[col] for col in columns]
        X_input.append(row)

    return np.array(X_input)

#ENDPOINTS 

@app.get("/health")
def health():
    return {
        "status": "ok",
        "version": APP_VERSION,
        "metrics": meta.get("metrics"),
        "n_features": len(columns),
        "model_pipeline_steps": [name for name, _ in model.steps] if model else "N/A" #estructura interna del modelo
        }

@app.post("/predict")
def predict(sample: Sample):
    try:
        start = time.perf_counter()
        # TODO: transforma 'sample' a lista en el orden de 'columns'
        # y haz model.predict / predict_proba
        # ---- TU CÓDIGO AQUÍ ----

        X_input = prepare_data_for_model([sample], columns)
        #   predicciones
        prediction_id = model.predict(X_input)[0]
        prediction_proba = model.predict_proba(X_input)[0]

        # Calcular la confianza 
        score = np.max(prediction_proba)

        # latencia y formatear salida
        latency_ms = (time.perf_counter() - start) * 1000

        # con el mapa se obtiene el nombre de la etiqueta
        label_name = label_map.get(prediction_id, "Desconocida")

        return PredictionOut(
            label_id=int(prediction_id),
            label_name=label_name,
            score=round(score, 4),
            latency_ms=round(latency_ms, 3)
        )

    except Exception as e:
        print(f"Error en /predict: {e}")
        raise HTTPException(status_code=400, detail=f"Error en el procesamiento de la predicción: {str(e)}")


@app.post("/predict-batch")
def predict_batch(samples: List[Sample]):
    try:
        # TODO: similar a /predict pero para lista
        # ---- TU CÓDIGO AQUÍ ----

        start = time.perf_counter()
        X_input = prepare_data_for_model(samples, columns)

        #  predicciones
        prediction_ids = model.predict(X_input)
        prediction_probas = model.predict_proba(X_input)

        results = []
        for id_pred, probas in zip(prediction_ids, prediction_probas):
            score = np.max(probas)
            label_name = label_map.get(id_pred, "Desconocida")

            results.append(PredictionOut(
                label_id=int(id_pred),
                label_name=label_name,
                score=round(score, 4),
                latency_ms=0.0 
            ))

        # Reemplaza latency_ms individual con el tiempo total del batch
        total_latency_ms = (time.perf_counter() - start) * 1000

        # Para el batch, se actualiza el primer elemento 
        if results:
            results[0].latency_ms = round(total_latency_ms, 3)

        return results

    except Exception as e:
        print(f"Error en /predict-batch: {e}")
        raise HTTPException(status_code=400, detail=f"Error en el procesamiento del lote: {str(e)}")

