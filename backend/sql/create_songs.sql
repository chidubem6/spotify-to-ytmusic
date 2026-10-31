-- The songs table: one row per Spotify liked song.
CREATE TABLE songs (
    id             integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    status   text NOT NULL,
    checked_at     timestamptz,
    added_at       timestamptz NOT NULL,
    spotify_title  text NOT NULL,
    spotify_artist text NOT NULL,

    yt_title       text,
    yt_channel     text,
    yt_url text
);
