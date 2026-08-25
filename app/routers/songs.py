from fastapi import APIRouter, Depends
from app.services.music_service import MusicService
from typing import Optional
from app.services.deezer import search_song as external_song_search
from app.services.soundcharts import search_by_id as external_id_search

router = APIRouter(
    prefix="/songs",
    tags=["songs"],
)

def get_music_service() -> MusicService:
    return MusicService()

@router.get("/")
async def search_song(query: Optional[str] = None):
    if query:
        songs = await external_song_search(query)
    else:
        songs = []

    return {"songs": songs}

@router.get("/{isrc}")
async def get_song(isrc: str, service: MusicService = Depends(get_music_service)):
    song = await service.get_song_details(isrc)
    return song

