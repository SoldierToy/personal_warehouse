from .base import BaseORM
from sqlalchemy.orm import Mapped, relationship


class StatusesORM(BaseORM):
    __tablename__ = "statuses"

    product: Mapped["ProductsORM"] = relationship(
        back_populates="status",
        uselist=False)

