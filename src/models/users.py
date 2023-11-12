from .base import BaseORM
from sqlalchemy.orm import Mapped, relationship


class UsersORM(BaseORM):
    __tablename__ = "users"

    tg_id: Mapped[int]

    product: Mapped["ProductsORM"] = relationship(
        back_populates="user_id",
        uselist=False)
