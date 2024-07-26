from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection

client: MongoClient = MongoClient("mongodb://root:pass@db:27017")  # type: ignore

database: Database[dict[str, Database]] = client["portafolio"]  # type: ignore

personas: Collection = database["personas"]  # type: ignore
experiencias: Collection = database["experiencias"]  # type: ignore
educacion: Collection = database["educacion"]  # type: ignore
certificados: Collection = database["certificados"]  # type: ignore
info_extra: Collection = database["info_extra"]  # type: ignore
