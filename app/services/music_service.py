from app.models.song import Song
from app.services.soundcharts import search_by_id as soundcharts_id_search
from app.services.deezer import search_by_id as deezer_id_search

class MusicService:

    async def get_song_details(self, isrc: str) -> Song:

        song = await deezer_id_search(isrc)
        song_data = await soundcharts_id_search(isrc)

        song_data.song = song

        return song_data


