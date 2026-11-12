# Matching — requirements (section 5)

## Problem
The user's liked songs are saved from Spotify, but none of them is linked to a song on YouTube Music yet. Searching YouTube for a song returns covers, live versions, remixes and parodies that share its title, and tools like SongShift picked the wrong one or dropped songs entirely. The user only finds out when they hit play and hear a parody they thought was the real song, and the only way to find every wrong one is to listen to all ~9600 songs. If each song showed what it was matched to, and the uncertain ones were flagged, the user would only need to check the flagged songs instead of the whole library, and would see exactly which songs weren't found instead of losing them silently.

## User stories
1. As a user, I want to see each matched song next to its Spotify song, so that I can catch a wrong match without listening to it.

2. As a user, I want to see which songs were not found, so that I can search for them and add them to my YouTube Music library myself.

3. As a user, I want to see which songs the app wasn't sure about, next to their Spotify songs, so that I only check those instead of my whole library.

4. As a user, I want each song searched only once, so that every day's quota goes to new songs and my transfer finishes sooner.

## Acceptance criteria
1. **Every song gets a verdict (stories 1–3).** Given 20 pending songs from my real library, when matching runs on them, then those 20 leave Pending and appear under Matched, Unsure and Not found (the three counts add up to 20), and every Matched and Unsure row shows the Spotify title beside the YouTube title, the Spotify artist beside the YouTube channel, and a link.

2. **No wrong matches (story 1).** Given that run, when I open every link under Matched, then 0 of them are the wrong song (a cover, live version, remix or parody counts as wrong).

3. **Unsure stays small (story 3).** Given that run, then at most 5 of the 20 are Unsure.

4. **Not found means not found (story 2).** Given that run, when I search YouTube Music by hand for each Not found song, then none of them turns up as the real song in the first results.

5. **Searched only once (story 4).** Given those 20 songs have verdicts, when I log in again and run matching again, then the first 20 keep the same verdicts and links, and the run takes 20 different pending songs.

## Out of scope
- Liking songs on YouTube Music, daily batches, and picking the start date: section 6 (decision 20).
- Approving or skipping Unsure songs in the app: section 7.
- Asking Google for more quota: section 8 (decision 20).
