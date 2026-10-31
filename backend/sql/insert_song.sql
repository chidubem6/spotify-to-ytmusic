-- Put one song into the table: song 1 from fake_songs.py (Essence, pending).
INSERT INTO songs (status, checked_at, added_at, spotify_title, spotify_artist,
                   yt_title, yt_channel, yt_url)
VALUES (
    'pending',
    NULL,
    '2024-02-11T09:30:00Z',
    'Essence',
    'Wizkid',
    NULL,
    NULL,
    NULL
);
