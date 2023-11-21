from src.repositories.products_repository import ProductsRepository
from src.services.products_service import ProductsService


def products_service_depend():
    return ProductsService(ProductsRepository)
