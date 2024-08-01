from typing import Any
from pymongo.collection import Collection

from src.models.base import DBModel, PydanticOID
from src.models.mongo_config import database


class InformacionExtra(DBModel):
    persona_id: PydanticOID
    titulo: str
    contenido: str


informacion_extra_collection: Collection[dict[str, Any]] = database["extras"]
