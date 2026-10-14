from fastapi import FastAPI

from fake_songs import fake_songs

app = FastAPI()


@app.get("/api/songs")
def get_songs():
    return fake_songs
