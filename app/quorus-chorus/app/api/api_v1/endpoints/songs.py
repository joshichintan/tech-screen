from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api import deps

router = APIRouter()


@router.get("/{isrc}")
def get_song_by_isrc(isrc: str, db: Session = Depends(deps.get_db)):
    ...
