from pymongo.collection import Collection

from src.models.base import DBModel, PydanticOID
from src.models.mongo_config import database

class ExperienciaBase(DBModel):
    persona_id: PydanticOID
    cargo: str
    empleador: str
    inicio: str
    termino: str
    descripcion: str

class Experiencia(ExperienciaBase):
    def get_collection() -> Collection[ExperienciaBase]:
        return database["experiencias"]