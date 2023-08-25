from pydantic import BaseModel


class SongBase(BaseModel):
    ...


class SongCreate(SongBase):
    ...


class SongUpdate(SongBase):
    ...


class SongInDbBase(SongBase):
    id: int

    class Config:
        from_attributes = True


class Song(SongInDbBase):
    pass
