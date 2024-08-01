from bson import ObjectId

from src.models.persona import Persona

def obtener_persona(id: str) -> Persona:
    return Persona.get_collection().find_one({"_id": ObjectId(id)})

def listar_personas() -> list[Persona]:
    return Persona.get_collection().find()