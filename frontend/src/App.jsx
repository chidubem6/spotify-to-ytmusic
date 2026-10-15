import { useEffect, useState } from "react";
import "./App.css";

const BATCH_SIZE = 65;

function Tile ({label, count}) {
  return (
    <div className="tile">
      <p>{count}</p>
      <p>{label}</p>
    </div>
  )
}

function App() {
  const [songs, setSongs] = useState(null);

  useEffect(() => {
    fetch("/api/songs")
      .then((response) => response.json())
      .then((data) => setSongs(data));
  }, []);

  if (songs === null) {
    return <p>Loading songs…</p>;
  }

  const pending = songs.filter((song) => song.status === "pending");
  const matched = songs.filter((song) => song.status === "matched");
  const unsure = songs.filter((song) => song.status === "unsure");
  const notFound = songs.filter((song) => song.status === "not_found");

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
      <div className="tiles">
        <Tile label="Matched" count={matched.length} />
        <Tile label="Not liked yet" count={unsure.length} />
        <Tile label="Not Found" count={notFound.length} />
        <Tile label="Remaining" count={pending.length} />
      </div>

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
