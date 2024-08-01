from typing import Any
from pymongo.collection import Collection

from src.models.base import DBModel
from src.models.mongo_config import database


class Persona(DBModel):
    nombre: str
    introduccion: str
    titulo: str
    edad: int | None = None


class PersonaBasic(DBModel):
    nombre: str


persona_collection: Collection[dict[str, Any]] = database["personas"]
