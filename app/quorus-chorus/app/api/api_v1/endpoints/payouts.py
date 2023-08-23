from app.api import deps
from fastapi import APIRouter, Depends, HTTPException

from datetime import datetime

from app import crud, models, schemas
from sqlalchemy.orm import Session


router = APIRouter()


@router.get("/{isrc}")
def get_payout_for_song(
    isrc: str,
    start_date: datetime | None = None,
    end_date: datetime | None = None,
    db: Session = Depends(deps.get_db),
) -> float:
    ...
