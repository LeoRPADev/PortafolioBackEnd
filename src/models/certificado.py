from datetime import datetime
from pymongo.collection import Collection

from src.models.mongo_config import database
from src.models.base import DBModel, PydanticOID

class CertificadoBase(DBModel):
    persona_id: PydanticOID
    nombre: str
    fecha_certificacion: datetime
    fecha_expiracion: datetime

class Certificado(CertificadoBase):
    def get_collection() -> Collection[CertificadoBase]:
        return database["certificados"]