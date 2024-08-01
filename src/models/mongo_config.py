from typing import Any

from pymongo import MongoClient
from pymongo.database import Database

from src.settings import settings

client: MongoClient[dict[str, Any]] = MongoClient(settings.DB_URI)

database: Database[dict[str, Any]] = client["portafolio"]
