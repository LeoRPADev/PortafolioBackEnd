from fastapi import APIRouter, HTTPException

from src.models.persona import Persona, PersonaBasic
from src.controller.persona import listar_personas, obtener_persona

router = APIRouter(tags=["persona"])


@router.get("/persona/{id}")
def obtener(id: str) -> Persona:
    persona = obtener_persona(id)
    if not persona:
        raise HTTPException(404, "Not Found")
    return persona


@router.get("/persona")
def listar() -> list[PersonaBasic]:
    return listar_personas()  # type: ignore
