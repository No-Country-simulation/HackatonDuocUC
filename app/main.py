from fastapi import FastAPI
from api.routes_predict import router as predict_router
from api.routes_coach import router as coach_router

app = FastAPI(
    title="HackatonDuocUC API",
    description="API mínima con FastAPI + OpenAI",
    version="1.0.0"
)

# Rutas
app.include_router(predict_router, prefix="/api")
app.include_router(coach_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Bienvenido a la API de HackatonDuocUC 2025"}