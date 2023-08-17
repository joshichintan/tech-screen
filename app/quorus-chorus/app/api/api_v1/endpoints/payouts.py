from app.api import deps
from fastapi import APIRouter, Depends, HTTPException

from app import crud, models, schemas
from sqlalchemy.orm import Session


router = APIRouter()


@router.get("/{isrc}")
def get_payout_for_song(isrc: str, db: Session = Depends(deps.get_db)):
    ...
