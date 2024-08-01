from typing import Any
from pymongo.collection import Collection

from src.models.base import DBModel, PydanticOID
from src.models.mongo_config import database


class Educacion(DBModel):
    persona_id: PydanticOID
    institucion: str
    fecha_ingreso: str
    fecha_egreso: str


educacion_collection: Collection[dict[str, Any]] = database["educacion"]
