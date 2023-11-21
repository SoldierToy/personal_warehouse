from src.db.connections import async_session_maker
from src.models import ProductsORM
from src.repositories.base_repository import SQLAlchemyRepository
from sqlalchemy import insert


class ProductsRepository(SQLAlchemyRepository):
    model = ProductsORM

