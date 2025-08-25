from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.schemas.payout import PayoutRequest, PayoutResult

router = APIRouter()

@router.post("/", response_model=PayoutResult)
def payout(
    *,
    db: Session = Depends(deps.get_db),
    request: PayoutRequest,
) -> Any:
    """
    Calculate and store payout for a song based on the dates provided.
    
    This endpoint automatically detects the calculation type based on which dates are provided:
    
    1. **Lifetime**: No dates provided - Calculate total payout for all time
    2. **From Start**: Only start_date provided - Calculate from start_date to current date
    3. **To End**: Only end_date provided - Calculate from beginning to end_date
    4. **Date Range**: Both dates provided - Calculate between start_date and end_date
    
    The calculated payout is automatically stored in the database.
    """
    try:
        result = crud.crud_payout.payout.create(db, request=request)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error calculating payout: {str(e)}")
