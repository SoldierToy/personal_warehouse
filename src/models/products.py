import datetime
from .base import BaseORM
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import ForeignKey


class ProductsORM(BaseORM):
    __tablename__ = "products"

    user_id: Mapped["UsersORM"] = relationship(
        back_populates="product")
    user_fk: Mapped[int] = mapped_column(ForeignKey('users.id'))

    product_type_id: Mapped["ProductTypesORM"] = relationship(
        back_populates="product",
        uselist=False)
    product_type_fk: Mapped[int] = mapped_column(ForeignKey('product_types.id'), nullable=True)

    price: Mapped[int] = mapped_column(nullable=True)
    selling_price: Mapped[int] = mapped_column(nullable=True)
    repair_price: Mapped[int] = mapped_column(nullable=True)
    profit: Mapped[int] = mapped_column(nullable=True)
    receipt_date: Mapped[datetime.date] = mapped_column(nullable=True)
    sale_date: Mapped[datetime.date] = mapped_column(nullable=True)
    comment: Mapped[str] = mapped_column(nullable=True)

    place: Mapped["PlacesORM"] = relationship(
        back_populates="product",
        uselist=False)
    place_fk: Mapped[int] = mapped_column(ForeignKey('places.id'), nullable=True)

    status: Mapped["StatusesORM"] = relationship(
        back_populates="product",
        uselist=False)
    status_fk: Mapped[int] = mapped_column(ForeignKey('statuses.id'), nullable=True)

    product_location: Mapped["ProductLocationsORM"] = relationship(
        back_populates="product",
        uselist=False)
    product_location_fk: Mapped[int] = mapped_column(ForeignKey('product_locations.id'), nullable=True)

    image_paths: Mapped["ImagePaths"] = relationship(
        back_populates='product')
