from app.db.base_class import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Numeric, Date, Integer, ForeignKey
from decimal import Decimal
from datetime import date

class Payout(Base):
    __tablename__ = "payouts"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True)
    isrc: Mapped[str] = mapped_column(String(16), ForeignKey("songs.isrc"), index=True)
    amount: Mapped[Decimal] = mapped_column(Numeric(precision=10, scale=2))
    period_start: Mapped[date] = mapped_column(Date, nullable=True)  # Null for lifetime payouts
    period_end: Mapped[date] = mapped_column(Date, nullable=True)    # Null for lifetime payouts
    total_plays: Mapped[int] = mapped_column(Integer)
    payout_per_play: Mapped[Decimal] = mapped_column(Numeric(precision=9, scale=8))
    calculation_type: Mapped[str] = mapped_column(String(50))  # "lifetime", "from_start", "to_end", "date_range"
    created_at: Mapped[date] = mapped_column(Date, default=date.today)
