from fastapi import APIRouter

router = APIRouter(prefix="/products_locations", tags=['products_locations'])


@router.get('/')
async def get_products():
    print("products_locations")
