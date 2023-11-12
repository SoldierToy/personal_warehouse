from pydantic import BaseModel


class StatusesSchema(BaseModel):
    id: int
    name: str
