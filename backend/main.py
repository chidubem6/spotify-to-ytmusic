import os
import secrets
from datetime import datetime, timedelta, timezone
from urllib.parse import urlencode

import httpx
from fastapi import Cookie, FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import engine
from models import LoginSession, Song

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
    # Trade the one-time code for a token. Python asks Spotify directly,
    # so the browser never sees this request or its reply.
    response = httpx.post(
        "https://accounts.spotify.com/api/token",
        data={
            "grant_type": "authorization_code",
            "code": code,
            # Must match the one /api/login sent: the code's "delivery address".
            "redirect_uri": os.getenv("SPOTIFY_REDIRECT_URI")
        },
        # The app's ID card: client ID + secret (httpx sends them as a header).
        auth=(os.getenv("SPOTIFY_CLIENT_ID"), os.getenv("SPOTIFY_CLIENT_SECRET"))
    )
    token_data = response.json()

    # Spotify said no (like your typo): stop with an error instead of saving nothing.
    if "access_token" not in token_data:
        raise HTTPException(status_code=400, detail=token_data.get("error_description"))

    # Make up an unguessable session ID, and work out when the token dies.
    session_id = secrets.token_urlsafe(32)
    expires_at = datetime.now(timezone.utc) + timedelta(seconds=token_data["expires_in"])

    with Session(engine) as session:
        session.add(LoginSession(id=session_id, access_token=token_data["access_token"], expires_at=expires_at))
        session.commit()

    # Send the browser home, carrying its claim ticket in a cookie.
    redirect = RedirectResponse("/")
    redirect.set_cookie("session_id", session_id, httponly=True, samesite="lax")
    return redirect


@app.get("/api/me")
def me(session_id: str | None = Cookie(default=None)):
    # The cookie is the lookup key. No cookie, no row, or a dead token = not logged in.
    if session_id is None:
        raise HTTPException(status_code=401, detail="Not logged in")
    with Session(engine) as session:
        login = session.get(LoginSession, session_id)
    if login is None or login.expires_at < datetime.now(timezone.utc):
        raise HTTPException(status_code=401, detail="Not logged in")

    # Use the token: ask Spotify who this is.
    response = httpx.get(
        "https://api.spotify.com/v1/me",
        # The token travels in a header: "Bearer", a space, then the token.
        headers={"Authorization": "Bearer " + login.access_token}
    )
    return {"name": response.json()["display_name"]}