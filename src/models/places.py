from .base import BaseORM
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import ForeignKey
from .products import ProductsORM


class PlacesORM(BaseORM):
    __tablename__ = "places"

    product: Mapped["ProductsORM"] = relationship(
        back_populates="place_purchase",
        uselist=False)

