# Presentación


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
### - Bajar dataset
>[Dataset original](https://www.kaggle.com/datasets/ludmin/billboard?resource=download)

## PROCESO ETL 



## 🛠️ Requisitos e Instalación

<!-- PROJECT SHIELDS -->
[![scikitlearnBadge][scikitlearn-shield]][scikitlearn-url]
[![pythonBadge][python-shield]][python-url]
[![pandasBadge][pandas-shield]][pandas-url]
[![pydanticBadge][pydantic-shield]][pydantic-url]
[![uvBadge][uv-shield]][uv-url]
[![uvicornBadge][uvicorn-shield]][uvicorn-url]
[![jupyterBadge][jupyter-shield]][jupyter-url]
[![joblibBadge][joblib-shield]][joblib-url]
[![fastapiBadge][fastapi-shield]][fastapi-url]
<!-- PROJECT SHIELDS -->


***************************************************************************************************************
PASOS PARA USAR IDE con UV y COMENZAR DESARROLLO
****************************************************************************************************************

### - Instalar uv en la pc si es necesario (en terminal de Windows):

   Abrir un prompt CMD en win  o terminal ID, ver el prompt con PS:>    y ejecutar
```
 powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
### - Instalar uv en la pc si es necesario (linux)

# Instalar curl si no lo tienes
```
sudo apt update
```
```
sudo apt install curl
```
# Descargar e instalar uv
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```
# Recargar el profile 
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


#### asegurarse estar en el etorno correcto y activado: De ser necesario correr en terminal: `.venv\Scripts\activate`
### En linux: `source.venv/bin/activate`


## correr archivo en terminal con:
```
uvicorn app:app --reload --port 8000
```

## Abrir proyecto en browser:
```
http://127.0.0.1:8000/docs
```


<!-- PROJECT SHIELDS VARIABLES-->
[deepnote-shield]:https://img.shields.io/badge/Live-Deepnote-black?style=flat&labelColor=%23808080k&color=de6d40&logo=deepnote&logoColor=white
[deepnote-url]: https://deepnote.com/
[dotenv-shield]:https://img.shields.io/badge/env-dotenv-black?style=flat&labelColor=%23808080k&color=fec260&logo=dotenv&logoColor=white
[dotenv-url]:https://pypi.org/project/python-dotenv/
[fastapi-shield]:https://img.shields.io/badge/framework-fastapi-black?style=flat&labelColor=%23808080k&color=de6d40&logo=fastapi&logoColor=white
[fastapi-url]: https://fastapi.tiangolo.com/
[joblib-shield]:https://img.shields.io/badge/serializer-joblib-black?style=flat&labelColor=%23808080k&color=fec260&logo=joblib&logoColor=white
[joblib-url]:https://joblib.readthedocs.io/en/stable/
[jupyter-shield]:https://img.shields.io/badge/Notebook-jupyter-black?style=flat&labelColor=%23808080k&color=fec260&logo=Jupyter&logoColor=white
[jupyter-url]: https://jupyter.org/
[pandas-shield]:https://img.shields.io/badge/Data_analysis-Pandas-black?style=flat&labelColor=%23808080k&color=453076&logo=pandas
[pandas-url]:https://pandas.pydata.org/
[plotly-shield]:https://img.shields.io/badge/Data_Viz-Plotly-black?style=flat&labelColor=%23808080k&color=9ABF80&logo=plotly&logoColor=white
[plotly-url]: https://plotly.com/python/
[pydantic-shield]:https://img.shields.io/badge/validation-pydantic-black?style=flat&labelColor=%23808080k&color=9ABF80&logo=pydantic&logoColor=white
[pydantic-url]: https://docs.pydantic.dev/latest/
[python-shield]:https://img.shields.io/badge/Language-Python-black?style=flat&labelColor=%23808080k&color=2a0944&logo=python&logoColor=white
[python-url]: https://www.python.org/
[scikitlearn-shield]:https://img.shields.io/badge/ML-scikitlearn-black?style=flat&labelColor=%23808080k&color=de6d40&logo=scikitlearn&logoColor=white
[scikitlearn-url]: https://scikit-learn.org/
[supabase-shield]:https://img.shields.io/badge/DB-supabase-black?style=flat&labelColor=%23808080k&color=166866&logo=supabase&logoColor=white
[supabase-url]: https://supabase.com/
[uv-shield]:https://img.shields.io/badge/Dependencias-UV-black?style=flat&labelColor=%23808080k&color=2a0944&logo=uv&logoColor=white
[uv-url]: https://github.com/astral-sh/uv
[uvicorn-shield]:https://img.shields.io/badge/server-uvicorn-black?style=flat&labelColor=%23808080k&color=166866&logo=uvicorn&logoColor=white
[uvicorn-url]: https://uvicorn.dev/
