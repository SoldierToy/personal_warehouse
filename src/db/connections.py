from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
)
from src.settings import settings

engine = create_async_engine(
    url=settings.get_db_url(),
    echo=True
)

async_session_maker = async_sessionmaker(
    engine,
    expire_on_commit=False
)


async def get_async_session():
    async with async_session_maker() as session:
        yield session
        await session.close()
