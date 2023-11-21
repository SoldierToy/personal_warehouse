import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ProductsCreateSchema(BaseModel):
    name: str
    user_fk: int
    product_type_fk: int | None = None
    price: int | None = None
    selling_price: int | None = None
    repair_price: int | None = None
    profit: int | None = None
    receipt_date: Optional[datetime.date] = None
    sale_date: Optional[datetime.date] = None
    comment: Optional[str] = None
    place_fk: int | None = None
    status_fk: int | None = None
    product_location_fk: int | None = None


class ProductDeleteSchema(BaseModel):
    id: int


class ProductSchema(BaseModel):
    id: int


class ProductsReadOneSchema(ProductsCreateSchema):
    id: int


class ProductUpdate(BaseModel):
    id: int


class ProductCreateResponse(BaseModel):
    id: int
