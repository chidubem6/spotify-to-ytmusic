import { fakeSongs } from "./fakeSongs";
import "./App.css";

const BATCH_SIZE = 65;

function App() {
  const pending = fakeSongs.filter((song) => song.status === "pending");
  const matched = fakeSongs.filter((song) => song.status === "matched");
  const unsure = fakeSongs.filter((song) => song.status === "unsure");
  const notFound = fakeSongs.filter((song) => song.status === "not_found");

  const sortedMatched = [...matched].sort((a, b) =>
    b.checkedAt.localeCompare(a.checkedAt),
  );

  const sortedUnsure = [...unsure].sort((a, b) =>
    b.checkedAt.localeCompare(a.checkedAt),
  );

  const sortedNotFound = [...notFound].sort((a, b) =>
    b.checkedAt.localeCompare(a.checkedAt),
  );

  const sortedPending = [...pending].sort((a, b) =>
    a.addedAt.localeCompare(b.addedAt),
  );

  const nextBatch = sortedPending.slice(0, BATCH_SIZE);
  const later = sortedPending.slice(BATCH_SIZE);

  return (
    <>
      <p>Matched: {matched.length}</p>
      <p>Not liked yet: {unsure.length}</p>
      <p>Not found: {notFound.length}</p>
      <p>Remaining: {pending.length}</p>

      <h2>Matched</h2>
      {sortedMatched.map((song) => (
        <div key={song.id}>
          <a href={song.ytUrl}>{song.ytTitle}</a>
          <p>{song.ytChannel}</p>
          <small>
            {song.spotifyTitle} by {song.spotifyArtist}
          </small>
        </div>
      ))}

      <h2>Not liked yet (Unsure)</h2>
      {sortedUnsure.map((song) => (
        <div key={song.id}>
          <a href={song.ytUrl}>{song.ytTitle}</a>
          <p>{song.ytChannel}</p>
          <small>
            {song.spotifyTitle} by {song.spotifyArtist}
          </small>
        </div>
      ))}

      <h2>Not Found</h2>
      {sortedNotFound.map((song) => (
        <div key={song.id}>
          <small>
            {song.spotifyTitle} by {song.spotifyArtist}
          </small>
        </div>
      ))}

      <h2>Next batch</h2>
      {nextBatch.map((song) => (
        <div key={song.id}>
          <small>
            {song.spotifyTitle} by {song.spotifyArtist}
          </small>
        </div>
      ))}

      {later.length > 0 && (
        <>
          <h2>Later</h2>

          {later.map((song) => (
            <div key={song.id}>
              <small>
                {song.spotifyTitle} by {song.spotifyArtist}
              </small>
            </div>
          ))}
        </>
      )}
    </>
  );
}

export default App;
