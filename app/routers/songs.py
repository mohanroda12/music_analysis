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

@router.get("/{id}")
def get_song(id: int, service: MusicService = Depends(get_music_service)):
    print("Test")
    song = service.get_by_id(id)
    return song

@router.get("/search/{search_term}")
def search_song(search_term: str):
    return {"search_term": search_term}