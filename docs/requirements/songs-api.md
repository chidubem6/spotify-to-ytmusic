# Songs API — requirements

## Problem
Right now the React page can only show songs hardcoded in `fakeSongs.js`. It has no way to get songs from anywhere else, so it can never show real liked songs. This section gives the frontend an API endpoint to fetch songs from, so that in section 4 the backend can fill it with real Spotify songs.


## User stories
1. As a developer, I want the frontend to call an endpoint that returns all the user's liked songs, so that the songs come from the backend (and later from Spotify) rather than being hardcoded in React.

2. As a developer, I want to test the endpoint on its own (on FastAPI's `/docs` page) before connecting the frontend, so that I know it works, and if the page breaks later I can tell whether the bug is in the backend or the frontend.

## Acceptance criteria

### The page gets its songs from the API (story 1)
- `frontend/src/fakeSongs.js` is deleted, and the report page still shows the same 10 songs, with the same tile counts and the same sections, as before the change.

### The endpoint works on its own (story 2)
- On FastAPI's `/docs` page, calling `GET /api/songs` returns all 10 songs as JSON.
- Every song has the same fields as `fakeSongs.js`: `id`, `status`, `checkedAt`, `addedAt`, `spotifyTitle`, `spotifyArtist`, `ytTitle`, `ytChannel`, `ytUrl`, with the same values.

## Not in this section (built elsewhere)
- Real Spotify songs and logging in: section 4 (`login.md`).
- Storing songs in a database, so they survive a restart: section 3. In this section the songs are still a fixed list, just written in Python.
