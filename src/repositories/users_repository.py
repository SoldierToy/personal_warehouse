from src.models import UsersORM
from src.repositories.base_repository import SQLAlchemyRepository


class UsersRepository(SQLAlchemyRepository):
    model = UsersORM
