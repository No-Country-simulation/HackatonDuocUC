from fastapi import APIRouter
from src.gpt_client import ask_openai

router = APIRouter()

@router.post("/coach")
async def coach(prompt: str) -> dict:
    """
    Devuelve un plan textual basado en la base de conocimiento /kb.
    """
    plan = ask_openai(f"Genera un plan de coaching para: {prompt}")
    return {"plan": plan, "source": "/kb"}
