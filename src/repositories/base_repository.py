from src.db.connections import get_async_session, async_session_maker
from src.repositories.abstract_repository import AbstractRepository
from sqlalchemy import insert, delete, update, select


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, data: dict):
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            await session.execute(stmt)
            await session.commit()

    async def find_all(self):
        async with async_session_maker() as session:
            stmt = select(self.model)
            res = await session.execute(stmt)
            res = res.scalars().all()
            return res

    async def find_one(self, obj_id):
        async with async_session_maker() as session:
            stmt = select(self.model).filter_by(id=obj_id)
            res = await session.execute(stmt)
            return res.scalar_one()

    async def del_one(self, obj_id: int):
        async with async_session_maker() as session:
            stmt = delete(self.model).filter_by(id=obj_id)
            await session.execute(stmt)
            await session.commit()

    async def update_one(self, obj_id: int, data):
        async with async_session_maker() as session:
            stmt = update(self.model).filter_by(id=obj_id).values(**data)
            await session.execute(stmt)
            await session.commit()
