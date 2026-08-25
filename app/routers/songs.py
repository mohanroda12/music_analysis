from fastapi import APIRouter, Depends
from app.services.music_service import MusicService
from typing import Optional
from app.services.soundcharts import search_song as external_song_search

router = APIRouter(
    prefix="/songs",
    tags=["songs"],
)

music_service = MusicService()

def get_music_service() -> MusicService:
    return music_service
@router.get("/")
async def search_song(artist: Optional[str] = None,
                title: Optional[str] = None,
                service: MusicService = Depends(get_music_service)
                ):
    if artist or title:
        #songs = service.song_search(title, artist)
        songs = await external_song_search(title)
    else:
        songs = service.get_all_songs()

    return {"songs": songs}

@router.get("/{id}")
def get_song(id: int, service: MusicService = Depends(get_music_service)):
    song = service.get_by_id(id)
    return song

