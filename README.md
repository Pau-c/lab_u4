# Presentación
<img width="1024" height="682" alt="unidad4" src="https://github.com/user-attachments/assets/0d98dc07-d621-4542-81a6-e3aa352ea932" />




---

## Integrantes

- Ariel Omar Leche
- Diego Ariel Gutierrez 
- José Alberto Rubio
- Maria Paula Cobas
- Mauro Ruben De Natale

> [!TIP]
>[Repo en Github](https://github.com/Pau-c/lab_u4)

## Descripción

## Instrucciones 

### 🛠️ Requisitos e Instalación

<!-- PROJECT SHIELDS -->
[![datadogBadge][datadog-shield]][datadog-url]
[![dockerBadge][docker-shield]][docker-url]
[![fastapiBadge][fastapi-shield]][fastapi-url]
[![jupyterBadge][jupyter-shield]][jupyter-url]
[![joblibBadge][joblib-shield]][joblib-url]
[![loguruBadge][loguru-shield]][loguru-url]
[![pandasBadge][pandas-shield]][pandas-url]
[![pydanticBadge][pydantic-shield]][pydantic-url]
[![pythonBadge][python-shield]][python-url]
[![scikitlearnBadge][scikitlearn-shield]][scikitlearn-url]
[![uvBadge][uv-shield]][uv-url]
[![uvicornBadge][uvicorn-shield]][uvicorn-url]

<!-- PROJECT SHIELDS -->
*****************************************************************************************************************
PASOS PARA USAR CON DOCKER
****************************************************************************************************************

### - Instalar `Docker` desktop
### - Hacer una cuenta en `Datadog` -> install agents-> Docker -> elegir region.
### - Copiar `Api key` y dirección(ej: us3.datadoghq.com)  
### - Tener el servicio de Docker corriendo
### - Clonar repo:
```
git clone https://github.com/Pau-c/lab_u4.git
```
### - Abrir el proyecto en ide
### - Crear un archivo en la raíz del proyecto llamado `.env`
### - Dentro pegar la api key de Datadog que se copio antes siguiendo este formato (sin espacios ni comillas): `DD_API_KEY=`
### - En archivo `compose.yaml` pegar la direccion copiada en `DD_SITE=` (sin espacios ni comillas)
### -  Ir a carpeta de proyecto en terminal:
```
docker compose up --build
```
### - Para volver a correr el proyecto dentro del contenedor si no hubo cambios:
```
docker compose up 
```

### - Abrir proyecto en un browser:
```
http://127.0.0.1:8000/docs
```



***************************************************************************************************************
PASOS PARA USAR en IDE SIN DOCKER con UV y COMENZAR DESARROLLO
****************************************************************************************************************

### - Instalar uv en la pc si es necesario (en terminal de Windows):

   Abrir un prompt CMD en win  o terminal ID, ver el prompt con PS:>    y ejecutar
```
 powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
### - Instalar uv en la pc si es necesario (linux)

### Instalar curl si no lo tienes
```
sudo apt update
```
```
sudo apt install curl
```
### Descargar e instalar uv
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```
### Recargar el profile 
```
source ~/.bashrc  # Para Bash
```
source ~/.zshrc   # Para Zsh

### - Clonar repo:
```
git clone https://github.com/Pau-c/lab_u4.git
```

### - Abrir proyecto en un IDE

### - Crear entorno virtual:
Si todavía no se instaló uv en el sistema como en el primer paso, en terminal: `pip install uv` y luego  ejecutar:
```
uv venv
```

### - Sincronizar entorno virtual al instalar el proyecto y luego de cada cambio en el .toml
```
uv sync
```

### -Elegir kernel
>Para que el código del notebook funcione,  indicarle a VS Code que utilice el Python >que está dentro del nuevo entorno. Esto se hace dentro de la interfaz del notebook:

> [!IMPORTANT]
> Abrir el archivo `.ipynb` en VS Code.
> 1. Hacer clic en el selector del kernel (la esquina superior derecha).
> 2. Seleccionar otro kernel.
> 3. Elegir el kernel que tenga el nombre del proyecto.


#### Asegurarse estar en el etorno correcto y activado: De ser necesario correr en terminal: `.venv\Scripts\activate`
#### En linux: `source .venv/bin/activate`

### - Correr en 04_3_Taller_FastAPI.ipynb hasta la celda 4

### - Antes de correr la celda 5 con las pruebas, ejecutar el proyecto localmente en terminal con:
```
uvicorn app:app --reload --port 8000
```

### - Abrir proyecto en browser para ver los endpoints:
```
http://127.0.0.1:8000/docs
```


<!-- PROJECT SHIELDS VARIABLES-->
[datadog-shield]:https://img.shields.io/badge/Observability-Datadog-black?style=flat&labelColor=%23808080k&color=81493b&logo=datadog&logoColor=white
[datadog-url]: https://www.datadoghq.com/
[deepnote-shield]:https://img.shields.io/badge/Live-Deepnote-black?style=flat&labelColor=%23808080k&color=d65e40&logo=deepnote&logoColor=white
[deepnote-url]: https://deepnote.com/
[docker-shield]:https://img.shields.io/badge/Container-Docker-black?style=flat&labelColor=%23808080k&color=f7b387&logo=docker&logoColor=white
[docker-url]: https://www.docker.com
[dotenv-shield]:https://img.shields.io/badge/Env-Dotenv-black?style=flat&labelColor=%23808080k&color=f3edb9&logo=dotenv&logoColor=white
[dotenv-url]:https://pypi.org/project/python-dotenv/
[fastapi-shield]:https://img.shields.io/badge/Framework-Fastapi-black?style=flat&labelColor=%23808080k&color=b0c69a&logo=fastapi&logoColor=white
[fastapi-url]: https://fastapi.tiangolo.com/
[joblib-shield]:https://img.shields.io/badge/Serializer-Joblib-black?style=flat&labelColor=%23808080k&color=70b29c&logo=joblib&logoColor=white
[joblib-url]:https://joblib.readthedocs.io/en/stable/
[jupyter-shield]:https://img.shields.io/badge/Notebook-Jupyter-black?style=flat&labelColor=%23808080k&color=2a9ca0&logo=Jupyter&logoColor=white
[jupyter-url]: https://jupyter.org/
[loguru-shield]:https://img.shields.io/badge/Logger-Loguru-black?style=flat&labelColor=%23808080k&color=2a6478&logo=loguru
[loguru-url]:https://pandas.pydata.org/
[pandas-shield]:https://img.shields.io/badge/Data_analysis-Pandas-black?style=flat&labelColor=%23808080k&color=4c4e77&logo=pandas
[pandas-url]:https://pandas.pydata.org/
[plotly-shield]:https://img.shields.io/badge/Data_Viz-Plotly-black?style=flat&labelColor=%23808080k&color=133337&logo=plotly&logoColor=white
[plotly-url]: https://plotly.com/python/
[pydantic-shield]:https://img.shields.io/badge/Validation-Pydantic-black?style=flat&labelColor=%23808080k&color=81493b&logo=pydantic&logoColor=white
[pydantic-url]: https://docs.pydantic.dev/latest/
[python-shield]:https://img.shields.io/badge/Language-Python-black?style=flat&labelColor=%23808080k&color=d65e40&logo=python&logoColor=white
[python-url]: https://www.python.org/
[scikitlearn-shield]:https://img.shields.io/badge/ML-Scikitlearn-black?style=flat&labelColor=%23808080k&color=f7b387&logo=scikitlearn&logoColor=white
[scikitlearn-url]: https://scikit-learn.org/
[supabase-shield]:https://img.shields.io/badge/DB-Supabase-black?style=flat&labelColor=%23808080k&color=166866&logo=supabase&logoColor=white
[supabase-url]: https://supabase.com/
[uv-shield]:https://img.shields.io/badge/Dependencies-UV-black?style=flat&labelColor=%23808080k&color=2a0944&logo=uv&logoColor=white
[uv-url]: https://github.com/astral-sh/uv
[uvicorn-shield]:https://img.shields.io/badge/Server-Uvicorn-black?style=flat&labelColor=%23808080k&color=166866&logo=uvicorn&logoColor=white
[uvicorn-url]: https://uvicorn.dev/

---
## 📘 Bitácora de Decisiones

**Dataset y objetivo:** se utilizó el dataset *Iris* de `sklearn.datasets` para clasificar la especie de una flor (*Setosa*, *Versicolor* o *Virginica*) a partir de las medidas de sépalos y pétalos (problema de clasificación multiclase).

**Selección de features/target:** se emplearon las cuatro variables numéricas `sepal_length_cm`, `sepal_width_cm`, `petal_length_cm` y `petal_width_cm` como entrada, y la columna `target` como salida.

**Modelo y preprocesamiento:** Dado que el dataset de Iris no tiene datos faltantes, las características son numéricas y están en una escala similar, las necesidades de preprocesamiento son mínimas.Se entrenó un **K-Nearest Neighbors (KNN)** con 5 vecinos (`KNeighborsClassifier`) dentro de un `Pipeline` junto a un `StandardScaler` para escalar los datos.Este asume una distribución normal y centra los datos alrededor dedesviacion de 0 a 1, lo cual es crucial para modelos basados en distancia como KNN. El conjunto se dividió en 80 % entrenamiento y 20 % prueba con **estratificación**.  El modelo y las columnas se guardaron con `joblib` para su reutilización.

**Métrica principal y resultados:** se utilizó **accuracy** como métrica principal, obteniendo una precisión de alrededor del **93 %** en el conjunto de prueba. Dado que el modelo KNN depende fuertemente de la elección de hiperparámetros (especialmente el número de vecinos), en futuras iteraciones se podría aplicar **GridSearchCV** u otras técnicas de búsqueda de hiperparámetros para evaluar si es posible mejorar el desempeño del modelo.

**Decisiones de contrato:** la API expone los endpoints dados `/health`, `/predict` y `/predict-batch`. Se definieron esquemas **Pydantic** que validan tipos y rangos de las features, y las respuestas se devuelven en formato **JSON** con campos como `label_id`, `label_name`, `score` y `latency_ms`, además del manejo  de errores HTTP.

**Observabilidad y pruebas:** se implementó **logging con Loguru** y se realizaron pruebas desde el notebook utilizando `requests`, abarcando casos válidos e inválidos (faltan campos, tipo incorrecto, campo extra) y midiendo **latencia**. El entorno es completamente reproducible mediante **Docker** y `uv`.

**Lecciones aprendidas:** el uso de **FastAPI** y **Pydantic** simplifica la validación y documentación de la API; el **Pipeline** de scikit-learn con **KNN** garantiza reproducibilidad, y las pruebas junto con el **logging** en **Datadog** son escenciales al monitoreo en tiempo real y fortalecen la confiabilidad del servicio.

**Análisis del Dataset**

**Basado en la salida de la celda de "Carga y exploración":**

**Dataset Utilizado:** sklearn.datasets.load_iris.

**Cantidad de Registros:** 150 (según el count en df.describe()).

**Cantidad de Columnas:** 5 (4 features y 1 target).

**Valores Nulos:** 0. La salida de df.isnull().sum() muestra 0 para todas las columnas.

**Valores Duplicados:** El notebook no incluye un paso específico para verificar registros duplicados (ej. df.duplicated().sum()).

**Métricas Descriptivas (Estadísticas):**

**sepal length (cm):** Media 5.84; Min 4.3; Max 7.9

**sepal width (cm):** Media 3.05; Min 2.0; Max 4.4

**petal length (cm):** Media 3.75; Min 1.0; Max 6.9

**petal width (cm):** Media 1.19; Min 0.1; Max 2.5

**Target:** 3 clases (0, 1, 2).

**Análisis de Métricas Descriptivas:** Las medidas del sépalo (largo y ancho) siguen una distribución simétrica (media $\approx$ mediana). En cambio, las medidas del pétalo son la clave: sus medias y medianas son muy diferentes, revelando una distribución bimodal.Esto indica que los datos se agrupan naturalmente en dos grupos separados (flores de pétalo corto vs. flores de pétalo largo), facilitando la clasificación.


### Datadog:
![datadog](https://github.com/user-attachments/assets/e15b746e-c96a-4d20-97d5-208f3910a402)

### Docker:
![docker](https://github.com/user-attachments/assets/d56bf4bb-1e80-43f8-9fed-25c413e75923)

### API:
![api](https://github.com/user-attachments/assets/07d76a71-d7d1-4c34-b002-7d246eb70ccb)

### HEALTH:
![health](https://github.com/user-attachments/assets/3d03dc6c-97a5-4325-ad45-fe4e2219d147)

### PREDICT:
![post predict](https://github.com/user-attachments/assets/57ad1179-db5e-49e3-8190-042fb32838b7)

### PREDICT BATCH:
![predictbatch](https://github.com/user-attachments/assets/9052449a-e983-4d73-ab0c-fc70fd977e94)

### Test Output:
![test_output_hasta3](https://github.com/user-attachments/assets/cde7325e-8e02-442d-976c-8a5ef46b8443)

![test_output_4](https://github.com/user-attachments/assets/3e427350-d1fb-473f-a3e6-fead9fb2b59b)

![test_output_5](https://github.com/user-attachments/assets/96d14ed7-0052-439f-8d34-7af130cd663c)

![test_output_6](https://github.com/user-attachments/assets/dee8d76f-c013-4465-8766-13177955e055)

![test_output_7y8](https://github.com/user-attachments/assets/92c35fae-6809-4ff7-8c27-4ce6df81c16a)

