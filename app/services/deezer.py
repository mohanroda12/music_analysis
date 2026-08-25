from dotenv import load_dotenv
import os
import httpx

# This API will strictly be used to get song metadata

load_dotenv()
BASE_URL = os.getenv("DEEZER_BASE_URL")

async def search_song(search_term: str | None):

    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{BASE_URL}/search",
            params={
                "q": search_term
            }
        )
        response.raise_for_status()
        return response.json()





