from dotenv import load_dotenv
import os
import httpx

# This API will strictly be used to get song metadata

load_dotenv()

CLIENT_ID = os.getenv("SOUNDCHARTS_CLIENT_ID")
CLIENT_SECRET = os.getenv("SOUNDCHARTS_CLIENT_SECRET")
BASE_URL = os.getenv("SOUNDCHARTS_BASE_URL")

async def get_access_token():

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


async def search_song(search_term: str | None):
    token = await get_access_token()

    async with httpx.AsyncClient() as client:

        response = await client.get(
            f"{BASE_URL}/api/v2/song/search/{search_term}",
            headers={
                "Authorization": f"Bearer {token}"
            }
        )

        response.raise_for_status()

        return response.json()





