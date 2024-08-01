from fastapi import APIRouter, HTTPException

from src.models.persona import PersonaBase, PersonaBasico
from src.controller.persona import listar_personas, obtener_persona

router = APIRouter(tags=["persona"])


@router.get("/persona/{id}")
def obtener(id: str) -> PersonaBase:
    persona = obtener_persona(id)
    return persona or HTTPException(404, "Not Found")

@router.get("/persona")
def listar() -> list[PersonaBasico]:
    return listar_personas()