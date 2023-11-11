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
    product_type_fk: Mapped[int] = mapped_column(ForeignKey('product_types.id'))

    price: Mapped[int]
    selling_price: Mapped[int]
    repair_price: Mapped[int]
    profit: Mapped[int]
    receipt_date: Mapped[datetime.date]
    sale_date: Mapped[datetime.date]
    comment: Mapped[str]

    place: Mapped["PlacesORM"] = relationship(
        back_populates="product",
        uselist=False)
    place_fk: Mapped[int] = mapped_column(ForeignKey('places.id'))

    status: Mapped["StatusesORM"] = relationship(
        back_populates="product",
        uselist=False)
    status_fk: Mapped[int] = mapped_column(ForeignKey('statuses.id'))

    product_location: Mapped["ProductLocationsORM"] = relationship(
        back_populates="products",
        uselist=False)
    product_location_fk: Mapped[int] = mapped_column(ForeignKey('product_locations.id'))
