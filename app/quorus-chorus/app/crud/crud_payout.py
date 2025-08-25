from app.crud.base import CRUDBase
from app.models.payout import Payout
from app.schemas.payout import PayoutCreate
from datetime import datetime, timezone
from sqlalchemy.orm import Session
from typing import List, Optional
from sqlalchemy import func, and_
from datetime import date, datetime, timezone
from app.models.song import Song
from app.models.plays import Play
from app.schemas.payout import (
    PayoutRequest, PayoutResult
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

    def create(self, db: Session, request: PayoutRequest) -> PayoutResult:
        """
        Main function to calculate payouts based on the request type.
        Automatically detects the case based on which dates are provided.
        Converts incoming dates to UTC for consistent processing.
        """
        # Convert request dates to UTC for consistent processing
        utc_start_date = None
        utc_end_date = None
        
        if request.start_date:
            # Convert to UTC midnight (00:00:00)
            utc_start_date = datetime.combine(request.start_date, datetime.min.time())
            utc_start_date = utc_start_date.replace(tzinfo=timezone.utc)
        
        if request.end_date:
            # Convert to UTC end of day (23:59:59)
            utc_end_date = datetime.combine(request.end_date, datetime.max.time())
            utc_end_date = utc_end_date.replace(tzinfo=timezone.utc)
        
        # Auto-detect case based on UTC dates
        if utc_start_date is None and utc_end_date is None:
            # Case 1: Lifetime (no dates)
            return self._calculate_lifetime_payout(db, request.isrc)
        elif utc_start_date is not None and utc_end_date is None:
            # Case 2: From start date to current date
            return self._calculate_from_start_payout(db, request.isrc, utc_start_date)
        elif utc_start_date is None and utc_end_date is not None:
            # Case 3: From beginning to end date
            return self._calculate_to_end_payout(db, request.isrc, utc_end_date)
        elif utc_start_date is not None and utc_end_date is not None:
            # Case 4: Date range
            return self._calculate_date_range_payout(db, request.isrc, utc_start_date, utc_end_date)
        else:
            raise ValueError("Invalid date combination")

    def _calculate_lifetime_payout(self, db: Session, isrc: str) -> PayoutResult:
        """Case 1: Calculate lifetime payouts for a song (no date filtering)"""
        return self._calculate_payout_base(db, isrc, None, None, "lifetime")

    def _calculate_from_start_payout(self, db: Session, isrc: str, start_date: date) -> PayoutResult:
        """Case 2: Calculate payouts from start date to current date"""
        return self._calculate_payout_base(db, isrc, start_date, None, "from_start")

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

        # Get current UTC date for storage
        current_utc_date = datetime.now(timezone.utc).date()


        # Store the calculated payout in the database
        payout_record = Payout(
            isrc=isrc,
            amount=Decimal(str(total_payout)),
            period_start=start_date,
            period_end=end_date,
            total_plays=total_plays,
            payout_per_play=Decimal(str(song.payout_per_play)),
            calculation_type=calculation_type,
            created_at=current_utc_date
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
            current_utc_date = datetime.now(timezone.utc).date()
            return f"From {start_date} to {current_utc_date}"
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
