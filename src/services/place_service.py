

class ProductsService:
    def __init__(self, users_repo: Type[ProductsRepository]):
        self.products_repo: ProductsRepository = users_repo()

    async def add_product(self, product: ProductsCreateSchema):
        product_dict = product.model_dump()
        product_id = await self.products_repo.add_one(product_dict)
        return product_id

    async def get_one_product(self, product: ProductsCreateSchema):
        product_dict = product
        product_info = await self.products_repo.find_one(product_dict)
        return product_info

    async def get_all_products(self):
        products = await self.products_repo.find_all()
        return products

    async def del_product(self, obj_id):
        product = await self.products_repo.del_one(obj_id)
        return product

    async def update_product(self, obj_id: int, data: ProductsCreateSchema):
        data = data.model_dump()
        product = await self.products_repo.update_one(obj_id=obj_id, data=data)
        return product
