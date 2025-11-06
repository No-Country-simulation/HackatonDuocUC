# HackatonDuocUC

---

Proyecto de ejemplo que contiene una pequeña API FastAPI (`app.py`) y un script de prueba (`main.py`) que utiliza un cliente para comunicarse con la API de OpenAI (`gpt_client.py`).

## Estructura principal

- `app.py` - Aplicación FastAPI con endpoints de ejemplo.
- `main.py` - Script que usa `gpt_client.ask_openai` para solicitar una respuesta al modelo.
- `gpt_client.py` - Cliente que encapsula llamadas a la API de OpenAI (carga variables desde `.env`).
- `requirements.txt` - Dependencias del proyecto.

## Requisitos

- Python 3.10+ (recomendado). Si usas otra versión, valida compatibilidad con las dependencias en `requirements.txt`.
- Una clave de OpenAI si quieres ejecutar `main.py` (variable `OPENAI_API_KEY`).

## Instalación rápida (Linux / zsh)

1. Clona el repositorio y sitúate en la carpeta del proyecto:

```bash
cd /ruta/al/proyecto/HackatonDuocUC
```

2. Crea y activa un entorno virtual (recomendado):

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instala dependencias:

```bash
pip install -r requirements.txt
```

4. Crea un archivo `.env` en la raíz del proyecto con tu clave de OpenAI (si vas a usar `main.py`):

```
OPENAI_API_KEY=sk-....
```