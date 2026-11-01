from fastapi import FastAPI
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
            
