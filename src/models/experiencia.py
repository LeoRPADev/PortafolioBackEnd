from typing import Any
from pymongo.collection import Collection

from src.models.base import DBModel, PydanticOID
from src.models.mongo_config import database


class Experiencia(DBModel):
    persona_id: PydanticOID
    cargo: str
    empleador: str
    inicio: str
    termino: str
    descripcion: str


experiencia_collection: Collection[dict[str, Any]] = database["experiencias"]
