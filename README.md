# HackatonDuocUC

---

Este proyecto implementa una API con **FastAPI** para conectarse a **OpenAI GPT-5**, estructurada de forma profesional, además de dar una solución a el tema de 'Smart Cities' entregada en la hackaton AI Aplicada por Duoc UC 2025.


## Resumen rápido

- Lenguaje: Python
- Framework web: FastAPI
- Cliente OpenAI: `src/gpt_client.py` (usa `python-dotenv` para cargar `.env`)
- Entrypoint de desarrollo: `run.py` (usa `uvicorn`)

## Estructura del proyecto

``` bash
HackatonDuocUC/
├── app/                  # Aplicación FastAPI (punto de entrada)
│   └── main.py
├── api/                  # Rutas / endpoints
│   ├── routes_predict.py
│   └── routes_coach.py
├── src/                  # Código auxiliar / clientes
│   └── gpt_client.py
├── .env                  # Variables de entorno (no versionar)
├── requirements.txt
├── run.py                # Script para arrancar con uvicorn
└── README.md
```

## Endpoints principales

- GET `/` → Mensaje de bienvenida (definido en `app/main.py`).
- POST `/api/predict` → endpoint definido en `api/routes_predict.py` (usa `src.gpt_client.ask_openai`).
- POST `/api/coach` → endpoint definido en `api/routes_coach.py` (genera un plan de coaching usando `ask_openai`).

## Requisitos

- Python 3.10+ recomendado.
- `OPENAI_API_KEY` si vas a usar los endpoints que llaman a OpenAI.

## Instalación y ejecución (Linux / zsh)

1. Sitúate en la carpeta del proyecto:

```bash
cd /home/jarod/Documents/web/tracks/CITT/HACKATON
```

2. Crear y activar un entorno virtual (recomendado):

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Crear archivo `.env` en la raíz con tu API key (si corresponde):

```env
OPENAI_API_KEY=sk-...   # reemplaza con tu clave real
```

5. Ejecutar la aplicación (desarrollo):

```bash
python run.py
```

Esto lanza Uvicorn con el app importado desde `app.main`. Alternativamente puedes ejecutar directamente:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Probar endpoints (ejemplos)

```bash
# Root
curl http://127.0.0.1:8000/

```