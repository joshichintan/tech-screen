from app.db.base_class import Base

from sqlalchemy import Column, Integer


class Payout(Base):
    id = Column(Integer, primary_key=True)
    ...
