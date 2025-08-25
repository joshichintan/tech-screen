from app.crud.base import CRUDBase
from app.models.payout import Payout
from app.schemas.payout import PayoutCreate
from datetime import datetime
from sqlalchemy.orm import Session
from typing import List, Optional
from sqlalchemy import func, and_
from datetime import date, datetime
from app.models.song import Song
from app.models.plays import Play
from app.schemas.payout import (
    PayoutRequest, PayoutResult,
    LifetimePayoutRequest, FromStartPayoutRequest, 
    ToEndPayoutRequest, DateRangePayoutRequest
)
from decimal import Decimal

class CRUDPayout:
    # Now that we have the song information in the database,
    # we'd like to know how much we have to pay each artist
    # for the number of plays.
    #
    # This payout function should take in an ISRC, an optional start date
    # and an optional end date.
    #
    # There are 4 cases to handle:
    #   1. ISRC - Given just the ISRC, calculate the lifetime
    #      payouts for this song

    #   2. ISRC + Start date - Given ISRC and start date, calculate
    #      payouts from the start date to the current date

    #   3. ISRC + End Date - Given ISRC and end date, calculate payouts
    #      from the initial create date to the end date

    #   4. ISRC + start and end date - Given ISRC, start, and end date,
    #      calculate payout between the two dates

    def calculate_payout(self, db: Session, request: PayoutRequest) -> PayoutResult:
        """
        Main function to calculate payouts based on the request type.
        Handles all 4 cases using Pydantic schemas for validation.
        """
        if isinstance(request, LifetimePayoutRequest):
            return self._calculate_lifetime_payout(db, request.isrc)
        elif isinstance(request, FromStartPayoutRequest):
            return self._calculate_from_start_payout(db, request.isrc, request.start_date)
        elif isinstance(request, ToEndPayoutRequest):
            return self._calculate_to_end_payout(db, request.isrc, request.end_date)
        elif isinstance(request, DateRangePayoutRequest):
            return self._calculate_date_range_payout(db, request.isrc, request.start_date, request.end_date)
        else:
            raise ValueError(f"Unknown payout request type: {type(request)}")

    def _calculate_lifetime_payout(self, db: Session, isrc: str) -> PayoutResult:
        """Case 1: Calculate lifetime payouts for a song (no date filtering)"""
        return self._calculate_payout_base(db, isrc, None, None, "lifetime")

    def _calculate_from_start_payout(self, db: Session, isrc: str, start_date: date) -> PayoutResult:
        """Case 2: Calculate payouts from start date to current date"""
        current_date = datetime.now().date()
        return self._calculate_payout_base(db, isrc, start_date, current_date, "from_start")

    def _calculate_to_end_payout(self, db: Session, isrc: str, end_date: date) -> PayoutResult:
        """Case 3: Calculate payouts from earliest play to end date"""
        return self._calculate_payout_base(db, isrc, None, end_date, "to_end")

    def _calculate_date_range_payout(self, db: Session, isrc: str, start_date: date, end_date: date) -> PayoutResult:
        """Case 4: Calculate payouts between two specific dates"""
        if start_date > end_date:
            raise ValueError("Start date cannot be after end date")
        return self._calculate_payout_base(db, isrc, start_date, end_date, "date_range")

    def _calculate_payout_base(self, db: Session, isrc: str, start_date: Optional[date], 
                              end_date: Optional[date], calculation_type: str) -> PayoutResult:
        """
        Base calculation function that handles the core logic for all cases.
        """
        # Get song information
        song = db.query(Song).filter(Song.isrc == isrc).first()
        if not song:
            raise ValueError(f"Song with ISRC {isrc} not found")

        # Build query for plays
        query = db.query(Play).filter(Play.isrc == isrc)
        
        # Apply date filtering based on case
        if start_date:
            query = query.filter(Play.date >= start_date)
        if end_date:
            query = query.filter(Play.date <= end_date)
        
        # Get total plays count
        total_plays = query.count()
        
        # Calculate total payout
        total_payout = total_plays * song.payout_per_play

        # Store the calculated payout in the database
        payout_record = Payout(
            isrc=isrc,
            amount=Decimal(str(total_payout)),
            period_start=start_date,
            period_end=end_date,
            total_plays=total_plays,
            payout_per_play=Decimal(str(song.payout_per_play)),
            calculation_type=calculation_type,
            created_at=datetime.now().date()
        )
        
        db.add(payout_record)
        db.commit()
        db.refresh(payout_record)

        return PayoutResult(
            isrc=song.isrc,
            artist=song.artist,
            total_payout=total_payout,
            total_plays=total_plays,
            payout_per_play=song.payout_per_play,
            date_range=self._format_date_range(start_date, end_date, calculation_type)
        )

    def _format_date_range(self, start_date: Optional[date], end_date: Optional[date], calculation_type: str) -> str:
        """Format the date range description for display"""
        if calculation_type == "lifetime":
            return "Lifetime"
        elif calculation_type == "from_start" and start_date:
            return f"From {start_date} to {datetime.now().date()}"
        elif calculation_type == "to_end" and end_date:
            return f"Until {end_date}"
        elif calculation_type == "date_range" and start_date and end_date:
            return f"From {start_date} to {end_date}"
        else:
            return "Unknown period"

    def get_stored_payouts(self, db: Session, isrc: str, skip: int = 0, limit: int = 100) -> list[Payout]:
        """Get stored payout records for a specific ISRC"""
        return db.query(Payout).filter(Payout.isrc == isrc).offset(skip).limit(limit).all()

    def get_latest_payout(self, db: Session, isrc: str, calculation_type: str = None) -> Optional[Payout]:
        """Get the most recent payout record for a specific ISRC and calculation type"""
        query = db.query(Payout).filter(Payout.isrc == isrc)
        if calculation_type:
            query = query.filter(Payout.calculation_type == calculation_type)
        return query.order_by(Payout.created_at.desc()).first()

payout = CRUDPayout()
