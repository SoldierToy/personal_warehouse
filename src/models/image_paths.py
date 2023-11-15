from .base import BaseORM
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy import ForeignKey
from .products import ProductsORM


class ImagePaths(BaseORM):
    __tablename__ = "image_paths"

    product: Mapped["ProductsORM"] = relationship(
        back_populates="image_paths",
        uselist=False)

    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'), nullable=True)
