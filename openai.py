import os
from dotenv import load_dotenv
from openai import OpenAI

# Carga variables desde .env (por defecto busca en el directorio actual)
load_dotenv()

# Obtén variables (recomendado: usar os.getenv para valores opcionales)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


if not OPENAI_API_KEY:
    raise RuntimeError("Falta OPENAI_API_KEY en las variables de entorno")

# Crea el cliente con tu API key
client = OpenAI(api_key="OPENAI_API_KEY")

# Envía una solicitud de chat
response = client.chat.completions.create(
    model="gpt-5",  # o "gpt-4o" según el modelo disponible en tu cuenta
    messages=[
        {"role": "system", "content": "Eres un asistente útil."},
        {"role": "user", "content": "Dame una broma corta sobre programadores."}
    ]
)

# Imprime la respuesta del modelo
print(response.choices[0].message.content)
