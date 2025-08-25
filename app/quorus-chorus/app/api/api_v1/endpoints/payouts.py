from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.schemas.payout import (
    PayoutRequest, PayoutResult, LifetimePayoutRequest, 
    FromStartPayoutRequest, ToEndPayoutRequest, DateRangePayoutRequest
)

router = APIRouter()

@router.post("/", response_model=PayoutResult)
def payout(
    *,
    db: Session = Depends(deps.get_db),
    request: PayoutRequest,
) -> Any:
    """
    Calculate and store payout for a song based on the request type.
    
    This endpoint handles 4 different cases:
    1. Lifetime: Calculate total payout for a song (no dates)
    2. From Start: Calculate payout from start date to current date
    3. To End: Calculate payout from earliest play to end date
    4. Date Range: Calculate payout between two specific dates
    
    The calculated payout is automatically stored in the database.
    """
    try:
        result = crud.crud_payout.payout.calculate_payout(db, request=request)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error calculating payout: {str(e)}")
