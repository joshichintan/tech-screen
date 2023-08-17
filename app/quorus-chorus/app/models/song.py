from app.db.base_class import Base

from sqlalchemy import Column, Integer, String, Numeric


class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, index=True)
    isrc = Column(String)
    album = Column(String)
    artist = Column(String)
    payout_per_play = Column(Numeric(precision=7, scale=8))
    licensing_group = Column(String)
