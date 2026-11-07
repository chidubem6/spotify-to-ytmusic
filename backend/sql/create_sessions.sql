-- The sessions table: one row per logged-in browser.
-- The browser holds only the id (in a cookie); the token never leaves the backend.
CREATE TABLE sessions (
    id           text PRIMARY KEY,
    access_token text NOT NULL,
    expires_at   timestamptz NOT NULL
);
