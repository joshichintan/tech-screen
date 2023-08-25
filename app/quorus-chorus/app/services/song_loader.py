from typing import BinaryIO

from app.schemas import SongCreate


class SongLoaderService:
    @staticmethod
    def load_from_file(songs_file: BinaryIO) -> list[SongCreate]:
        songs: list[SongCreate] = []

        return songs
