# Copy the 10 fake songs into the songs table.
# Run from backend/ with the venv active:  python load_fake_songs.py
from datetime import datetime

from sqlalchemy.orm import Session

from database import engine
from fake_songs import fake_songs
from models import Song


def to_time(text):
    # "2024-02-11T09:30:00Z" (text) -> a real datetime; None stays None.
    return datetime.fromisoformat(text) if text else None


with Session(engine) as session:
    for fake in fake_songs:
        song = Song(
            status=fake["status"],
            checked_at=to_time(fake["checkedAt"]),
            added_at=to_time(fake["addedAt"]),
            spotify_title=fake["spotifyTitle"],
            spotify_artist=fake["spotifyArtist"],
            yt_title=fake["ytTitle"],
            yt_channel=fake["ytChannel"],
            yt_url=fake["ytUrl"],
        )
        session.add(song)
    session.commit()
