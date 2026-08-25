from pydantic import BaseModel

class Song(BaseModel):
    isrc: str
    title: str
    artist: str
    album: str
    album_cover_url: str

    def __hash__(self):
        return hash(self.isrc)


