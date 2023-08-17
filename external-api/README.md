# Quorus Tech Screen "3rd Party API"

A small HTTP API with runs at http://localhost:5050 with a single endpoint - `GET /api/songs/:ISRC` - that returns a JSON object with the following structure:

```json
{
  "iswc": "T-34.989.316-0",
  "title": "Yellow",
  "artist": "Coldplay",
  "spotifyUrl": "https://open.spotify.com/track/3AJwUDP919kvQ9QcozQPxg",
  "albumArtUrl": "https://i.scdn.co/image/ab67616d0000b273e4b4e6a2b8c7b3b0b3b0b3b0"
}
```

Written using [Deno](https://deno.land/). Just to try it out.
