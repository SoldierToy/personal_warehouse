from pydantic import BaseModel


class PlacesSchema(BaseModel):
    id: int
    name: str
