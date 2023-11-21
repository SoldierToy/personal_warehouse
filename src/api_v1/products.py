from fastapi import APIRouter, Depends, status
from src.schemas.products import ProductsCreateSchema, ProductDeleteSchema, ProductsReadOneSchema, \
    ProductCreateResponse
from src.dependencies.depends_products_service import products_service_depend

router = APIRouter(prefix="/products", tags=['products'])


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_products(
        products: ProductsCreateSchema,
        products_service=Depends(products_service_depend)
):
    res = await products_service.add_product(products)
    return res


@router.get('/{product_id}', response_model=ProductsReadOneSchema, status_code=status.HTTP_200_OK)
async def get_product(product_id: int, products_service=Depends(products_service_depend)):
    res = await products_service.get_one_product(product_id)
    return res


@router.get('/', status_code=status.HTTP_200_OK)
async def get_all_products(products_service=Depends(products_service_depend)):
    res = await products_service.get_all_products()
    return res


@router.patch('/{product_id}')
async def update_products(product_id: int, product: ProductsCreateSchema,
                          products_service=Depends(products_service_depend)):
    res = await products_service.update_product(obj_id=product_id, data=product)
    return res


@router.delete('/{product_id}', status_code=status.HTTP_202_ACCEPTED)
async def delete_products(product_id: int, products_service=Depends(products_service_depend)):
    res = await products_service.del_product(product_id)
    return res
