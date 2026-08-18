from fastapi import FastAPI
from app.routers import songs

app = FastAPI()

app.include_router(songs.router)

