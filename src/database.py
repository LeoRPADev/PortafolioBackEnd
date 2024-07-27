import pymongo
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection


client = MongoClient("mongodb://root:pass@db/")# type: ignore
database = client["portafolio"]

persona = database["persona"]
experiencia = database["experiencia"]
info_extra = database["info_extra"]
educacion = database["educacion"]
certificado = database["certificado"]