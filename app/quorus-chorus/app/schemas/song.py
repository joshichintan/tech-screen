from pydantic import BaseModel


class SongBase(BaseModel):
    ...


class SongCreate(SongBase):
    ...


class SongUpdate(SongBase):
    ...
