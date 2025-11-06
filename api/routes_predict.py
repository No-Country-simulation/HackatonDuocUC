from fastapi import APIRouter
from src.gpt_client import ask_openai

router = APIRouter()

@router.post("/predict")
async def predict(prompt: str) -> dict:
    """
    Devuelve {"score": float, "drivers": [top_features]} o una respuesta del modelo.
    """
    response = ask_openai(prompt)
    # Simulamos estructura esperada (ajústala según tu lógica)
    return {"score": 0.85, "drivers": [response]}
