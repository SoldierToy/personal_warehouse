from .base import BaseORM
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import ForeignKey
from .products import ProductsORM


class ProductTypesORM(BaseORM):
    __tablename__ = "product_types"

    product: Mapped["ProductsORM"] = relationship(
        back_populates="product_type_id",
        uselist=False)

