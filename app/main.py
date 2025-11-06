from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes_predict import router as predict_router
from api.routes_coach import router as coach_router

app = FastAPI(
    title="HackatonDuocUC API",
    description="API RES  con FastAPI + OpenAI",
    version="1.0.5"
)

# Configuración CORS
origins = [
    "http://localhost:4200",   # React local
    "http://127.0.0.1:4200",   # Alternativa local
    "https://tu-dominio.com",  # Producción (opcional)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # Dominios permitidos
    allow_credentials=True,          # Permitir cookies/autenticación
    allow_methods=["*"],             # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],             # Permitir todos los headers (Authorization, Content-Type, etc.)
)

# Rutas
app.include_router(predict_router, prefix="/api")
app.include_router(coach_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Bienvenido a la API de HackatonDuocUC 2025"}