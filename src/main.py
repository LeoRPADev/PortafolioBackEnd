from fastapi import FastAPI

from src.database import personas

app = FastAPI()


@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}


@app.post("/persona")
def crear_persona() -> dict[str, str]:
    result = personas.insert_one(
        {
            "nombre": "Juanito Perez",
            "introduccion": "Hola me llamo Juanito Perez",
            "titulo": "Zopenco",
        }
    )
    return {"id": result.inserted_id}


@app.get("/persona")
def obtener_persona() -> dict[str, str]:
    result: dict[str, str] | None = personas.find_one()
    if result is not None:
        return {"nombre": result["nombre"], "titulo": result["titulo"]}
    return {}
