from .base import BaseORM
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import ForeignKey
from .products import ProductsORM


class ProductLocationsORM(BaseORM):
    __tablename__ = "product_locations"

    product: Mapped["ProductsORM"] = relationship(
        back_populates="product_location",
        uselist=False)
