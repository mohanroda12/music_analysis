from pydantic import BaseModel

class Song(BaseModel):
    id: int
    title: str
    artist: str
    album: str
    genre: str

    def __hash__(self):
        return hash(self.id)


