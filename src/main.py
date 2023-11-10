from fastapi import FastAPI
from src.api_v1 import router as auth_router

app = FastAPI(title="Personal warehouse")

app.include_router(router=auth_router, tags=['auth'], prefix='/api/v1')