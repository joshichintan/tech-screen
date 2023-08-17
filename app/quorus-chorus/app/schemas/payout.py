from pydantic import BaseModel


class PayoutBase(BaseModel):
    ...


class PayoutCreate(PayoutBase):
    pass


class PayoutUpdate(PayoutBase):
    pass
