from app.models.song import Song

class MusicService:

    def __init__(self):
        self.songs = [
            Song(id=1, title="Billie Jean", artist="Michael Jackson", album="Thriller", genre="Pop"),
                      Song(id=2, title="Soon as I get home", artist="2pac", album="Pac", genre="Rap"),
                      Song(id=3, title="Runaway", artist="kanye", album="kanye", genre="Rap")
        ]

    def get_all_songs(self) -> list[Song]:
        return self.songs

    def song_search(self, title_input: str | None, artist_input: str | None) -> list[Song]:
        # Create a count for each song when searched
        songs_by_title = list()
        songs_by_artist = list()

        if title_input:
            songs_by_title = self.__title_search(search_term=title_input)

        if artist_input:
            songs_by_artist = self.__artist_search(search_term=artist_input)

        # Combine lists
        found_songs = set(songs_by_title + songs_by_artist)
        return list(found_songs)

    def __title_search(self, search_term: str) -> list[Song]:
        search_term = search_term.strip()
        found_songs = list()

        if search_term == "":
            return found_songs

        for song in self.songs:

            if search_term.lower() in song.title.lower():
                found_songs.append(song)

        return found_songs

    def __artist_search(self, search_term: str) -> list[Song]:
        search_term = search_term.strip()
        found_songs = list()

        if search_term == "":
            return found_songs

        for song in self.songs:
            if search_term.lower() in song.artist.lower():
                found_songs.append(song)

        return found_songs

    def get_by_id(self, id: int) -> Song | None:
        for song in self.songs:
            if song.id == id:
                return song
        return None
