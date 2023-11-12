from pydantic import BaseModel


class ProductsTypesSchema(BaseModel):
    id: int
    name: str
