import { Song } from "./models.ts";

const songsDb = await import("../data/songs-db.json", {
  assert: { type: "json" },
});

export function getSong(ISRC: string): Song | null {
  if (!songsDb.default[ISRC as keyof typeof songsDb.default]) {
    return null;
  }
  return songsDb.default[ISRC as keyof typeof songsDb.default];
}
