from app.models.plays import Play
from app.schemas.play import PlayCreate, PlayUpdate, PlayCreateResponse
from app.crud.base import CRUDBase
from sqlalchemy.orm import Session

class CRUDPlay(CRUDBase[Play, PlayCreate, PlayUpdate]):
    def create_play(self, db: Session, *, obj_in: PlayCreate) -> Play:
        db_obj = Play(
            isrc=obj_in.isrc,
            date=obj_in.date,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        count = self.get_play_count(db, isrc=obj_in.isrc)
        return PlayCreateResponse(isrc=obj_in.isrc, count=count)
    
    def get_play_count(self, db: Session, *, isrc: str) -> int:
        return db.query(Play).filter(Play.isrc == isrc).count()

play = CRUDPlay(PlayCreate)