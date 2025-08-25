import os
import requests
from app.schemas.song import ExternalSongResponse

# Use container name for Docker network communication, with environment variable override
BASE_URL = os.getenv("EXTERNAL_API_URL", "http://external-api:4001")

class ExternalAPIService:
    @staticmethod
    def get_song_by_isrc(song_id: str) -> ExternalSongResponse:
        response = requests.get(f"{BASE_URL}/api/songs/{song_id}")
        return ExternalSongResponse.model_validate_json(response.text)