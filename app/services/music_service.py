from app.models.song import Song

class MusicService:

    def __init__(self):
        self.songs = [
            Song(id=1, title="Billie Jean", artist="Michael Jackson", album="Thriller", genre="Pop"),
                      Song(id=2, title="Soon as I get home", artist="2pac", album="Pac", genre="Rap")
        ]

    def song_search(self, search_term: str) -> list[Song]:
        pass

    def artist_search(self, search_term: str) -> list[Song]:
        pass

    def get_by_id(self, id: int) -> Song | None:
        for song in self.songs:
            if song.id == id:
                return song
        return None
