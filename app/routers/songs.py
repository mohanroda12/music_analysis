from fastapi import APIRouter, Depends
from app.services.music_service import MusicService

router = APIRouter(
    prefix="/songs",
    tags=["songs"],
)

music_service = MusicService()

def get_music_service() -> MusicService:
    return music_service

@router.get("/")
def get_songs():
    return {"songs": "All songs list"}

@router.get("/search")
def search_song(artist: str, title: str, service: MusicService = Depends(get_music_service)):
    songs = service.song_search(title, artist)
    return {"songs": songs}

@router.get("/{id}")
def get_song(id: int, service: MusicService = Depends(get_music_service)):
    song = service.get_by_id(id)
    return song

