import os
from urllib.parse import urlencode

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import engine
from models import Song

app = FastAPI()


def song_to_json(song):
    # Left: the names App.jsx expects. Right: the column names in models.py.
    return {
        "id": song.id,
        "status": song.status,
        "checkedAt": song.checked_at,
        "addedAt": song.added_at,
        "spotifyTitle": song.spotify_title,
        "spotifyArtist": song.spotify_artist,
        "ytTitle": song.yt_title,
        "ytChannel": song.yt_channel,
        "ytUrl": song.yt_url,
    }


@app.get("/api/songs")
def get_songs():
    with Session(engine) as session:
        songs = session.scalars(select(Song)).all()
        json_songs = []
        for song in songs:
            json_songs.append(song_to_json(song))
        return json_songs


@app.get("/api/login")
def login():
    # Everything Spotify needs to show the consent page, as key: value pairs.
    params = {
        "client_id": os.getenv("SPOTIFY_CLIENT_ID"),
        "response_type": "code",
        "redirect_uri": os.getenv("SPOTIFY_REDIRECT_URI"),
        "scope": "user-library-read",
    }
    url = "https://accounts.spotify.com/authorize?" + urlencode(params)
    return RedirectResponse(url)


@app.get("/api/callback")
def callback(code: str):
    return {"code": code}