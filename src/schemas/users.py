from pydantic import BaseModel


class UsersSchema(BaseModel):
    id: int
    tg_id: int
    name: str
