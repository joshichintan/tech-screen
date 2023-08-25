from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.song import Song
from app.schemas.song import SongCreate, SongUpdate

from app.crud.base import CRUDBase


class CRUDSong(CRUDBase[Song, SongCreate, SongUpdate]):
    # In our DB, songs are created from multiple data sources.
    #
    # Song payout information comes in via flat files which, unfortunately
    # for us, are stored in a bizarre and non-standard format created by
    # the data provider (The reason for which is lost to the mire of corporate
    # bureaucracy).
    #
    # The internal identifier code (Called the IRA code) is in the form:
    # IRA-{Licensing Group}-{Last 5 ISRC}-{Len. song title as 3 digit number}
    #
    # EG: A song with:
    #   ISRC: US-XJD-23-83229,
    #   Title: Value Million,
    #   Licensor: The Orchard
    #
    # would produce the IRA code: IRA-The_Orchard-83229-013
    # (Song title len = 13) -> 013
    #
    # Other song information must be pulled from an external API
    # and merged with our pricing data.
    #
    # External API URL: GET http://localhost:4001/api/songs/{ISRC}

    def get_by_isrc(self, db: Session, *, isrc: str) -> Song | None:
        return db.scalar(select(Song).where(Song.isrc == isrc))


song = CRUDSong(Song)
