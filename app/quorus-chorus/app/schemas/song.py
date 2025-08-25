from decimal import Decimal
from pydantic import BaseModel

class ExternalSongResponse(BaseModel):
    isrc: str
    iswc: str
    title: str
    artist: str
    album: str
    payout_per_play: float
    licensing_group: str



class SongBase(BaseModel):
    isrc: str
    artist: str
    album: str
    payout_per_play: float
    licensing_group: str


class SongCreate(SongBase):
    ...


class SongUpdate(SongBase):
    isrc: str | None = None
    artist: str | None = None
    album: str | None = None
    payout_per_play: float | None = None
    licensing_group: str | None = None


class SongInDbBase(SongBase):
    id: int

    class Config:
        from_attributes = True


class Song(SongInDbBase):
    ...
