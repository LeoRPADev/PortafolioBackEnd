from pymongo.collection import Collection

from src.models.base import DBModel, PydanticOID
from src.models.mongo_config import database

class EducacionBase(DBModel):
    persona_id: PydanticOID
    institucion: str
    fecha_ingreso: str
    fecha_egreso: str

class Educacion(EducacionBase):
    def get_collection() -> Collection[EducacionBase]:
        return database["educacion"]