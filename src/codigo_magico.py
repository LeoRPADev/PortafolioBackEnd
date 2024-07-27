from pydantic import BaseModel, field_serializer, field_validator, ConfigDict, Field
from bson.objectid import ObjectId


class Persona(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    id: str | ObjectId = Field(alias="_id")

    Nombre: str

    Introduccion: str

    Titulo: str

    Edad: str

    @field_validator("id")
    @classmethod
    def metodo(cls, id: str | ObjectId) -> str:
        return str(id)


class Experiencia(BaseModel):
    NombreCargo: str

