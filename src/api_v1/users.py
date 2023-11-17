from typing import Annotated

from fastapi import APIRouter, Depends
from src.schemas.users import UsersSchema
from src.services.users_service import UsersService

from src.dependencies.depends_users_service import users_service

router = APIRouter(prefix="/users", tags=['users'])


@router.get('/')
async def get_users():
    print("get_users")


@router.post('/')
async def create_user(
        user: UsersSchema,
        user_service: Annotated[UsersService, Depends(users_service)]
):
    print(user)
    print(user_service)
    user_id = await user_service.add_user(user)
    print(user_id)
