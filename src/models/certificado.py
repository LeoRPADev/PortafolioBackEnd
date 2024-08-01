from datetime import datetime
from typing import Any

from pymongo.collection import Collection

from src.models.mongo_config import database
from src.models.base import DBModel, PydanticOID


class Certificado(DBModel):
    persona_id: PydanticOID
    nombre: str
    fecha_certificacion: datetime
    fecha_expiracion: datetime


certificado_collection: Collection[dict[str, Any]] = database["certificados"]
