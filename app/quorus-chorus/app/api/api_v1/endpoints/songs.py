from sqlalchemy import sql
import sqlalchemy
from app.api import deps
from fastapi import APIRouter, Depends, HTTPException, UploadFile
from sqlalchemy.orm import Session
from datetime import datetime, timezone
from app import crud, schemas, services

router = APIRouter()


@router.get("/{isrc}", response_model=schemas.Song)
def get_song_by_isrc(isrc: str, db: Session = Depends(deps.get_db)) -> schemas.Song:
    song = crud.song.get_by_isrc(db, isrc=isrc)

    if not song:
        raise HTTPException(status_code=404, detail="Song not found")

    return schemas.Song.from_orm(song)

@router.get("/play/{isrc}", response_model=schemas.PlayCreateResponse)
def play_song(isrc: str, db: Session = Depends(deps.get_db)) -> schemas.PlayCreateResponse:
    play = crud.play.create_play(db, obj_in=schemas.PlayCreate(isrc=isrc, date=datetime.now(timezone.utc)))

    return play

@router.post("/upload", status_code=201)
def upload_songs_file(file: UploadFile, db: Session = Depends(deps.get_db)) -> None:
    songs = services.SongLoaderService.load_from_file(file.file)

    for song in songs:
        crud.song.create(db, obj_in=song)

    return {"message": "Songs uploaded successfully"}
