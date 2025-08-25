from pydantic import BaseModel
from datetime import datetime
class PlayBase(BaseModel):
    isrc: str

class PlayCreate(PlayBase):
    isrc: str
    date: datetime

class PlayCreateResponse(BaseModel):
    isrc: str
    count: int

class PlayUpdate(PlayBase):
    ...

class PlayInDBBase(PlayBase):
    id: int
    date: datetime
    class Config:
        orm_mode = True

class Play(PlayInDBBase):
    ...