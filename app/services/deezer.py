from dotenv import load_dotenv
import os
import httpx
from app.models.song import Song

# This API will strictly be used to get song metadata

load_dotenv()
BASE_URL = os.getenv("DEEZER_BASE_URL")

async def search_song(search_term: str | None) -> list[Song]:

    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{BASE_URL}/search",
            params={
                "q": search_term,
                "limit": 8
            }
        )
        response.raise_for_status()

        songs = []

        for song in response.json()["data"]:
            songs.append(deezer_track_to_song(song))

        return songs

async def search_by_id(isrc: str) -> Song:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{BASE_URL}/track/isrc:{isrc}"
        )
        response.raise_for_status()
        return deezer_track_to_song(response.json())


def deezer_track_to_song(song_data: dict) -> Song:
    return Song(isrc=song_data["isrc"],
                title=song_data["title"],
                artist=song_data["artist"]["name"],
                album=song_data["album"]["title"],
                album_cover_url=song_data["album"]["cover_medium"]
                )




