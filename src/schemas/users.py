from pydantic import BaseModel


class UsersSchema(BaseModel):
    tg_id: int
    name: str
