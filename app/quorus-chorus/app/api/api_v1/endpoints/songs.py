from fastapi import APIRouter, Depends, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.api import deps
from app import schemas, crud

router = APIRouter()


@router.get("/{isrc}", response_model=schemas.Song)
def get_song_by_isrc(isrc: str, db: Session = Depends(deps.get_db)) -> schemas.Song:
    song = crud.song.get_by_isrc(db, isrc=isrc)

    if not song:
        raise HTTPException(status_code=404, detail="Song not found")

    return schemas.Song.from_orm(song)


@router.post("/upload", status_code=201)
def upload_songs_file(file: UploadFile, db: Session = Depends(deps.get_db)) -> None:
    ...
