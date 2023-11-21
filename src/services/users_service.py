from typing import Type

from src.repositories.users_repository import UsersRepository
from src.schemas.users import UsersSchema


class UsersService:
    def __init__(self, users_repo: Type[UsersRepository]):
        self.users_repo: UsersRepository = users_repo()

    async def add_user(self, user: UsersSchema):
        user_dict = user.model_dump()
        user_id = await self.users_repo.add_one(user_dict)
        return user_id
