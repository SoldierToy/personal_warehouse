from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from src.api_v1 import router as v1_router
from src.db.db import engine
from src.models.base import BaseORM


@asynccontextmanager
async def lifespan(app: FastAPI):
    print(BaseORM.metadata.info)
    async with engine.begin() as conn:
        await conn.run_sync(BaseORM.metadata.create_all)

    yield


app = FastAPI(title="Personal warehouse", lifespan=lifespan)

app.include_router(router=v1_router, tags=['auth'], prefix='/api/v1')

if __name__ == '__main__':
    uvicorn.run("src.main:app", reload=True)
