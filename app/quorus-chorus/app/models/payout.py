from app.db.base_class import Base
from sqlalchemy.orm import Mapped, mapped_column


class Payout(Base):
    __tablename__ = "payouts"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True)
    ...
