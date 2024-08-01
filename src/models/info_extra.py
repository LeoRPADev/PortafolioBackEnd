from pydantic import BaseModel
from pymongo.collection import Collection

from src.models.base import PydanticOID
from src.models.mongo_config import database

class InformacionExtraBase(BaseModel):
    persona_id: PydanticOID
    titulo: str
    contenido: str


class InformacionExtra(InformacionExtraBase):
    def get_collection() -> Collection[InformacionExtraBase]:
        return database["extras"]