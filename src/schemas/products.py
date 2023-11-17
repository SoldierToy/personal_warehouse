import datetime
from typing import Optional

from pydantic import BaseModel


class ProductsSchema(BaseModel):
    id: int
    name: str
    user_id: int
    product_type: str
    price: Optional[int]
    selling_price: Optional[int]
    repair_price:Optional[int]
    profit: Optional[int]
    receipt_date: Optional[datetime.date]
    sale_date: Optional[datetime.date]
    comment: Optional[str]
    place: Optional[str]
    status: Optional[str]
    product_location: Optional[str]