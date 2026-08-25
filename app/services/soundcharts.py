from dotenv import load_dotenv
import os
import httpx
from app.models.song_details import SongDetails
from app.models.audio_stats import AudioStats

# This API will strictly be used to get song metadata

load_dotenv()

CLIENT_ID = os.getenv("SOUNDCHARTS_CLIENT_ID")
CLIENT_SECRET = os.getenv("SOUNDCHARTS_CLIENT_SECRET")
BASE_URL = os.getenv("SOUNDCHARTS_BASE_URL")

async def __get_access_token():

    async with httpx.AsyncClient() as client:
        # Send POST request to get client access token
        response = await client.post(
            "https://account.soundcharts.com/oauth/token",
            auth=(CLIENT_ID, CLIENT_SECRET),
            data={
                "grant_type": "client_credentials"
            }
        )
        # Check if response is successful
        response.raise_for_status()
        # Return only the access token as JSON
        return response.json()["access_token"]


async def search_by_id(isrc: str):

        uuid = await __get_song_uuid(isrc)
        song_json = await __get_song_metadata(uuid)

        song = soundcharts_track_to_song(song_json["object"])
        return song

async def __get_song_uuid(isrc: str) -> str:
    token = await __get_access_token()

    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{BASE_URL}/api/v2/song/by-isrc/{isrc}",
            headers={
                "Authorization": f"Bearer {token}"
            }
        )

        response.raise_for_status()
        return response.json()["object"]["uuid"]


async def __get_song_metadata(uuid: str) -> dict:
    token = await __get_access_token()

    async with httpx.AsyncClient() as client:

        response = await client.get(
            f"{BASE_URL}/api/v2.25/song/{uuid}",
            headers={
                "Authorization": f"Bearer {token}"
            }
        )
        response.raise_for_status()
        return response.json()

def soundcharts_track_to_song(song_data: dict) -> SongDetails:
    audio_stats = song_data["audio"]
    return SongDetails(song=None,
                       uuid=song_data["uuid"],
                       duration=song_data["duration"],
                       genres=None,

                       audio_stats=AudioStats(
                           acousticness=audio_stats["acousticness"],
                           danceability=audio_stats["danceability"],
                           energy=audio_stats["energy"],
                           instrumentalness=audio_stats["instrumentalness"],
                           key=audio_stats["key"],
                           liveness=audio_stats["liveness"],
                           loudness=audio_stats["loudness"],
                           mode=audio_stats["mode"],
                           speechiness=audio_stats["speechiness"],
                           tempo=audio_stats["tempo"],
                           time_signature=audio_stats["timeSignature"],
                           valence=audio_stats["valence"]
                       ),

                       language=song_data["languageCode"]

                )






