from fastapi import FastAPI, Request, Response
from loguru import logger
import time

# --- Logger con loguru, persiste logs por 1 semana o hasta 10mb ---


async def loguru_middleware(request: Request, call_next):

    # mide tiempo de procesamiento 

    start_time = time.perf_counter()

    response: Response = await call_next(request)

    end_time = time.perf_counter()
    process_time_ms = (end_time - start_time) * 1000
# agrega header X-Process-Time-ms a la respuesta
    response.headers["X-Process-Time-ms"] = f"{process_time_ms:.3f}"

    # estructura de Log
    logger.info(
        "Request processed",
        time_ms=process_time_ms,
        method=request.method,
        url=request.url.path,
        status_code=response.status_code,
        client_ip=request.client.host if request.client else "N/A",
    )

    return response


# --- manejo de warnings de input  ---


def check_input_ranges(sample):

    # chequea si los valores de entrada están fuera del rango o cerca del límite

    warnings_list = []

    RANGES = {
        "sepal_length_cm": (3.0, 8.5),
        "petal_length_cm": (0.5, 7.5),
    }

    for field, (min_val, max_val) in RANGES.items():
        value = getattr(sample, field)

        if value > max_val * 0.9 and value <= max_val:
            warnings_list.append(
                f"ADVERTENCIA: '{field}' ({value:.2f}) se acerca al límite superior ({max_val:.2f})."
            )

        if value < min_val or value > max_val:
            warnings_list.append(
                f"CRÍTICO: '{field}' ({value:.2f}) está fuera del rango de entrenamiento ({min_val:.2f}-{max_val:.2f})."
            )

    if warnings_list:
        sample_dict = sample.model_dump()
        sample_id = str(hash(tuple(sample_dict.values())))
        logger.warning(
            "Input con valores atípicos o cercanos al límite.",
            warnings=warnings_list,
            sample_id=sample_id,
        )


# --- Función de Setup que aplica la lógica ---


def setup_observability(app: FastAPI):
    # Aplica el middleware de logging y latencia a la instancia de FastAPI app
    app.middleware("http")(loguru_middleware)

    # elimina la salida a la consola estándar y lo guarda en archivo log
    logger.remove()  # Opcional

    # Configuración del sink para guardar en un archivo local:
    # rotation="10 MB": Rotar el archivo de log cuando llega a 10 MB
    # compression="zip": Comprimir los archivos de log antiguos
    # serialize=True: Guarda el log en  JSON
    logger.add(
        "api_logs/api_logs_{time:YYYY-MM-DD}.json",
        rotation="1 week",
        retention="4 weeks",
        compression="zip",
        level="INFO",
        serialize=True,
    )

    logger.info(
        "Logs guardados en api_logs/"
    )
