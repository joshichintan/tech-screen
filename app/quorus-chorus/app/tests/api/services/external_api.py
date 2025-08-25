from app.services.external_api import MockExternalAPIService


class TestExternalAPI:
    def test_get_song_by_isrc(self):
        external_api = MockExternalAPIService()
        song = external_api.get_song_by_isrc("US-1234567890")
        assert song.isrc == "US-1234567890"