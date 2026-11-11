# Login — requirements (Spotify: section 4, Google: section 6)

## Problem
The app currently shows fake songs stored in PostgreSQL. It cannot retrieve the user's real liked songs, because they are private: Spotify only shares them once the user grants the app permission. If the application used the user's password instead, it could affect data outside its purpose, such as changing the password or deleting playlists. Spotify's `user-library-read` limits the permission scope and allows the application to read the user's songs.

## Already decided
- Log in with Spotify to read your liked songs (section 4).
- Log in with Google for permission to like videos on your YouTube account (section 6).
- The app never sees your passwords; the backend holds the tokens, the browser never does.

## User stories
As a user, I want the app to only be able to read my liked songs, so that it can't change or delete anything else in my Spotify account.

As a user, I want songs from my Spotify liked songs to be retrieved, so that a transfer of my songs from Spotify to YouTube Music can commence

## Acceptance criteria
Given a user has never approved the app on their Spotify account (first login, or after removing it at spotify.com/account/apps), When a user is presented with the Spotify consent page, Then the page should display the application's need to view the user's Spotify data and their library but not have ability to change data

Given a user is not currently logged in and the database is currently populated with 10 fake songs, When a user logs in, Then the database song count must match the total field in Spotify's GET /v1/me/tracks reply.
