from typing import BinaryIO

from app.schemas import SongCreate
from app.utils import parse_ira
from app.services.external_api import ExternalAPIService

class SongLoaderService:
    @staticmethod
    def load_from_file(songs_file: BinaryIO) -> list[SongCreate]:
        songs: list[SongCreate] = []
        parsed_iras = parse_ira(songs_file)

        for ira in parsed_iras:
            try:
                external_song = ExternalAPIService.get_song_by_isrc(ira.last5_isrc)
            except Exception as e:
                print(f"Error getting song by ISRC: {e}")
                continue

            if external_song and not all([external_song.isrc.split('-')[-1] == ira.last5_isrc, 
                            external_song.licensing_group == ira.licensing_group.replace('_', ' '),
                            str(external_song.payout_per_play) == str(ira.payout_per_play)]):
                print(f"ISRC mismatch: {external_song.isrc} != {ira.last5_isrc}")
                continue
            
            songs.append(SongCreate(
                isrc=external_song.isrc,
                artist=external_song.artist,
                album=external_song.album,
                payout_per_play=ira.payout_per_play,
                licensing_group=ira.licensing_group,
            ))
        return songs
