from pydantic import BaseModel, Field
from typing import Literal, Union, Optional
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

# New schemas for payout calculation
class LifetimePayoutRequest(BaseModel):
    isrc: str = Field(..., description="Song ISRC identifier")
    case: Literal["lifetime"] = "lifetime"

class FromStartPayoutRequest(BaseModel):
    isrc: str = Field(..., description="Song ISRC identifier")
    case: Literal["from_start"] = "from_start"
    start_date: date = Field(..., description="Start date for payout calculation")

class ToEndPayoutRequest(BaseModel):
    isrc: str = Field(..., description="Song ISRC identifier")
    case: Literal["to_end"] = "to_end"
    end_date: date = Field(..., description="End date for payout calculation")

class DateRangePayoutRequest(BaseModel):
    isrc: str = Field(..., description="Song ISRC identifier")
    case: Literal["date_range"] = "date_range"
    start_date: date = Field(..., description="Start date for payout calculation")
    end_date: date = Field(..., description="End date for payout calculation")

# Union type for all possible requests
PayoutRequest = Union[LifetimePayoutRequest, FromStartPayoutRequest, ToEndPayoutRequest, DateRangePayoutRequest]

class PayoutResult(BaseModel):
    isrc: str
    artist: str
    total_payout: float
    total_plays: int
    payout_per_play: float
    date_range: Optional[str] = None
