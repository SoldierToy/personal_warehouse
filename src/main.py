import uvicorn
from fastapi import FastAPI
from src.api_v1 import router as v1_router

app = FastAPI(title="Personal warehouse")

app.include_router(router=v1_router, tags=['auth'], prefix='/api/v1')

if __name__ == '__main__':
    uvicorn.run("src.main:app", reload=True)
