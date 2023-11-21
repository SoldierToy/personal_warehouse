from fastapi import APIRouter

router = APIRouter(prefix="/products_types", tags=['products_types'])


@router.post('/')
async def create_product_type():
    ...


@router.get('/{product_type_id}')
async def get_one_product_type(product_type_id):
    ...


@router.get('/')
async def get_all_product_types():
    ...


@router.delete('/{product_type_id}')
async def del_one_product_type(product_type_id):
    ...


@router.patch('/{product_type_id}')
async def update_one_product_type(product_type_id):
    ...
