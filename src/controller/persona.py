from bson import ObjectId

from src.models.persona import Persona, persona_collection


def obtener_persona(id: str) -> Persona | None:
    result = persona_collection.find_one({"_id": ObjectId(id)})
    persona = Persona(**result) if result else None
    return persona


def listar_personas() -> list[Persona]:
    return [Persona(**p) for p in persona_collection.find()]
