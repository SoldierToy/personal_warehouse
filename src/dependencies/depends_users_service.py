from src.repositories.users_repository import UsersRepository
from src.services.users_service import UsersService


def users_service_depend():
    return UsersService(UsersRepository)

