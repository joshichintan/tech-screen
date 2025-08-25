from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

# Existing schemas
class PayoutBase(BaseModel):
    isrc: str
    artist: str
    album: str
    payout_per_play: float
    licensing_group: str

class PayoutCreate(PayoutBase):
    pass

class Payout(PayoutBase):
    id: int

    class Config:
        from_attributes = True

# New simplified schema for payout calculation
class PayoutRequest(BaseModel):
    isrc: str = Field(..., description="Song ISRC identifier")
    start_date: Optional[date] = Field(None, description="Start date for payout calculation")
    end_date: Optional[date] = Field(None, description="End date for payout calculation")

class PayoutResult(BaseModel):
    isrc: str
    artist: str
    total_payout: float
    total_plays: int
    payout_per_play: float
    date_range: Optional[str] = None
