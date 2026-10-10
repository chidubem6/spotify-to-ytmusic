# Report page — requirements

## Problem
<!-- TODO(you, task 5): one or two sentences — what does the user not know without this page? -->

## User stories
1. As a user, I want to see how many songs were matched, unsure, and not found, so that I can see the remaining songs left to port, the amount of songs matched, unsured and not foound.

2. As a user, I want each matched song to show its Spotify title and artist beside the YouTube video it was liked as, with a link, so that I can verify that songs were correctly matched.

3. As a user, I want unsure songs listed separately and clearly marked as not liked yet, so that I can approve or skip songs manually 

4. As a user, I want to see exactly which songs were not found, so that I can manully search and add songs to my YT music.

5. As a user, I want to see every liked song still waiting to be transferred, with the next batch marked, so that I know which songs are getting transferred next and which will be transferred eventually.


## Acceptance criteria

### Tiles (top of the page)
- Matched, unsure, not found and remaining are displayed as tiles at the top of the screen.
- The matched, unsure, and not found tiles each show the same number as the count of songs listed in that section of the page.
- Remaining = the number of pending songs (the same as total liked songs − matched − unsure − not found, e.g. 1000 − 150 − 30 − 15 = 805).

### Sections (all lists)
- Matched, unsure ("Not liked yet"), not found, and pending songs are each listed under their own heading.
- Matched, unsure, and not-found songs are ordered by when the app checked them (`checkedAt`), newest at the top, oldest at the bottom.

### Matched
- A matched song displays its YouTube Music title and channel, with the Spotify title and artist beside it as a subtitle.
- The YouTube Music title is a link that opens the actual song in YouTube Music.

### Not liked yet (unsure)
- Unsure songs are listed under a "Not liked yet" heading.

### Not found
- A not-found song displays its Spotify title and artist. Display only — no buttons or actions yet.

### Still to transfer (pending)
- All pending songs are listed, oldest liked to newest liked (`addedAt`), the same order the batches work through them.
- The first 65 sit under a "Next batch" heading; the rest sit under a "Later" heading.
- Each pending song shows its Spotify title and artist. Display only — no buttons.

## Not on this page (built elsewhere)
- Approve / Skip for unsure songs — `review-page.md` (section 7).
- Removing a pending song from the batch — `review-page.md` (section 7).
- Logging in to Spotify and Google — `login.md` (sections 4 and 6).

## Later on this page
- Live updates while a batch runs — once real batches exist (section 6); polling (fetch every few seconds) is enough, no WebSockets.
