from pymongo.collection import Collection

from src.models.base import DBModel
from src.models.mongo_config import database

class PersonaBase(DBModel):
    nombre: str
    introduccion: str
    titulo: str
    edad: int | None = None

class PersonaBasico(DBModel):
    nombre: str

class Persona(PersonaBase):
    def get_collection() -> Collection[PersonaBase]:
        return database["personas"]