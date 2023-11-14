from fastapi import APIRouter

router = APIRouter(prefix="/products",  tags=['products'])


@router.get('/')
async def get_products():
    print("get_products")
