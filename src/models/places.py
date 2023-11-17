from .base import BaseORM
from sqlalchemy.orm import Mapped, relationship
from .products import ProductsORM


class PlacesORM(BaseORM):
    __tablename__ = "places"

    product: Mapped["ProductsORM"] = relationship(
        back_populates="place",
        uselist=False)

