from fastapi import APIRouter

router = APIRouter(prefix="/products_locations", tags=['products_locations'])


@router.post('/')
async def create_products_location():
    ...


@router.get('/{product_location_id}')
async def get_one_product_location(product_location_id):
    ...


@router.get('/')
async def get_all_products_locations():
    ...


@router.delete('/{product_location_id}')
async def del_one_product_location(product_location_id):
    ...


@router.patch('/{products_location_id}')
async def update_one_product_location(product_location_id):
    ...
