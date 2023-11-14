from fastapi import APIRouter

router = APIRouter(prefix="/products_types",  tags=['products_types'])


@router.get('/')
async def get_products_types():
    print("products_types")
