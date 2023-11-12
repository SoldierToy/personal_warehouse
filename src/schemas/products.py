import datetime

from pydantic import BaseModel


class ProductsSchema(BaseModel):
    id: int
    name: str | None
    user_fk: int
    product_type_fk: int
    price: int | None
    selling_price: int | None
    repair_price: int | None
    profit: int | None
    receipt_date: datetime.date | None
    sale_date: datetime.date | None
    comment: str | None
    place_fk: int | None
    status_fk: int | None
    product_location_fk: int | None
