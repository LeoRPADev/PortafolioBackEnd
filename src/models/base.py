from typing import Annotated

from bson import ObjectId
from pydantic import AliasChoices, BaseModel, ConfigDict, Field, PlainSerializer


PydanticOID = Annotated[
    ObjectId | str,
    PlainSerializer(lambda x: str(x), return_type=str, when_used="json"),
]


class DBModel(BaseModel):
    id: PydanticOID = Field(validation_alias=AliasChoices("_id", "id"))

    model_config = ConfigDict(arbitrary_types_allowed=True)
