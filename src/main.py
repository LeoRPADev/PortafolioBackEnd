from fastapi import FastAPI
from src.database import persona
from src.database import experiencia
from src.database import info_extra
from src.database import educacion
from src.database import certificado
from typing import Any
from bson.objectid import ObjectId
from src.codigo_magico import Persona


app = FastAPI()


@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}


@app.get("/ingreso")
def ingreso_prueba() -> dict[str, str]:
    data = {
        "Nombre": "Jhon",
        "Introduccion": "Soy un mantenido por mi familia",
        "Titulo": "Flojo certificado",
        "Edad": "29",
    }
    persona.insert_one(data)
    data["_id"] = str(data["_id"])
    return data


@app.get("/obtencion")
def obtener(id: str) -> Persona:
    intancia_objeto = ObjectId(id)
    x = persona.find_one({"_id": intancia_objeto})
    return x # type: ignore


@app.get("/listar")
def listar() -> list[Persona]:
    x = persona.find()
    return list(x)
