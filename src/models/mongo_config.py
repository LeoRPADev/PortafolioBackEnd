from pymongo import MongoClient
from pymongo.database import Database
from src.settings import settings

client: MongoClient = MongoClient(settings.DB_URI)

database: Database = client["portafolio"]