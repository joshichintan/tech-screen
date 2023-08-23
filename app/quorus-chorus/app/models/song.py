from app.db.base_class import Base

from sqlalchemy import Integer, String, Numeric
from sqlalchemy.orm import Mapped, mapped_column
from decimal import Decimal


class Song(Base):
    __tablename__ = "songs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    isrc: Mapped[str] = mapped_column(String)
    album: Mapped[str] = mapped_column(String)
    artist: Mapped[str] = mapped_column(String)
    payout_per_play: Mapped[Decimal] = mapped_column(Numeric(precision=7, scale=8))
    licensing_group: Mapped[str] = mapped_column(String)
