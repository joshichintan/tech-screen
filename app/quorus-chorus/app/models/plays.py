from app.db.base_class import Base
from datetime import datetime
from sqlalchemy import String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, foreign, mapped_column

class Play(Base):
    __tablename__ = "plays"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True)
    isrc: Mapped[str] = mapped_column(String(16), ForeignKey("songs.isrc"),unique=False, index=True)
    date: Mapped[datetime] = mapped_column(DateTime(), unique=False, index=True)
