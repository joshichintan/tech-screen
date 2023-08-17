from app.crud.base import CRUDBase
from app.models.payout import Payout
from app.schemas.payout import PayoutCreate, PayoutUpdate


class CRUDPayout(CRUDBase[Payout, PayoutCreate, PayoutUpdate]):
    ...


payout = CRUDPayout(Payout)
