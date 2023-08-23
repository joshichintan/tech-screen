from app.crud.base import CRUDBase
from app.models.payout import Payout
from app.schemas.payout import PayoutCreate, PayoutUpdate


class CRUDPayout(CRUDBase[Payout, PayoutCreate, PayoutUpdate]):
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
    ...


payout = CRUDPayout(Payout)
