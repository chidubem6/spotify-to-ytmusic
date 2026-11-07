from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


# Every table class inherits from Base, so SQLAlchemy keeps a list of them.
class Base(DeclarativeBase):
    pass


# One Song object = one row in the songs table (see sql/create_songs.sql).
class Song(Base):
    __tablename__ = "songs"

    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[str]
    checked_at: Mapped[datetime | None]
    added_at: Mapped[datetime]
    spotify_title: Mapped[str]
    spotify_artist: Mapped[str]
    yt_title: Mapped[str | None]
    yt_channel: Mapped[str | None]
    yt_url: Mapped[str | None]


# One LoginSession object = one logged-in browser (see sql/create_sessions.sql).
# Not called "Session": that name is already SQLAlchemy's database workspace.
class LoginSession(Base):
    __tablename__ = "sessions"

    id: Mapped[str] = mapped_column(primary_key=True)
    access_token: Mapped[str]
    expires_at: Mapped[datetime]
