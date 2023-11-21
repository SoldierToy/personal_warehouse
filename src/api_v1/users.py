from typing import Annotated

from fastapi import APIRouter, Depends
from src.schemas.users import UsersSchema
from src.dependencies.depends_users_service import users_service_depend
router = APIRouter(prefix="/users", tags=['users'])


@router.get('/')
async def get_users():
    print("get_users")


@router.post('/')
async def create_user(user: UsersSchema, user_service=Depends(users_service_depend)):
    user_id = await user_service.add_user(user)

