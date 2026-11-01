# Database — requirements

## Problem
Songs and their status live as a python list in fake_songs.py, rebuilt every time FastAPI starts.

A restart on the application causes a wipe of memory, including the batch of songs that were processed. A restart would mean processing already processed songs which would mean that the daily limit is reached on the same subset of songs meaning that max only 65 songs can be processed. Remembering the songs and their status means that the process can work on the next batch of songs instead of starting completely again.

## User stories
As a user, I want the app to remember the songs and their statuses so that the transfer does not start over and redo the same songs

As a developer, I want songs and their status to survive a restart so that I can deploy new code at any time without the transfer starting over.

## Acceptance criteria

### A change survives a restart (stories 1 and 2)
- Given the 10 fake songs are in the database, when I change one song's status in the database from `pending` to `matched` and provide its realistic YouTube fields (`checked_at`, `yt_title`, `yt_channel`, `yt_url`) and restart FastAPI, then the report page shows that song under Matched, the Matched tile goes up by 1, and the Remaining tile goes down by 1.

### The songs come from the database
- Given the 10 fake songs are loaded into the database, when I delete `backend/fake_songs.py` and restart FastAPI, then the report page shows the same 10 songs with the same tile counts. (The deleted file stays in git history.)
