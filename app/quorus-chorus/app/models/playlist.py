from app.db.base_class import Base
from sqlalchemy.orm import Mapped, mapped_column


class Playlist(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    ...
