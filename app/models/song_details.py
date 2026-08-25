from pydantic import BaseModel
from app.models.audio_stats import AudioStats
from app.models.song import Song

class SongDetails(BaseModel):
    song: Song
    uuid: str
    duration: int
    genres: dict | None
    audio_stats: AudioStats
    language: str

    def __hash__(self):
        return hash(self.uuid)


