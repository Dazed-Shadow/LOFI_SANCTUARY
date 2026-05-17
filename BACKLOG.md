# LOFI_SANCTUARY · Backlog (snapshot)

> ⚠️ **This file is a regenerated snapshot, not the source of truth.**
>
> The canonical Backlog lives in Notion:
> 📌 **[LOFI_SANCTUARY Backlog DB](https://www.notion.so/9d0a30fd4fef43c4ad788770f8fcaaa5)**
>
> Add, edit, or close items there. Regenerate this file from Notion when you
> want a static checked-in copy (e.g. before tagging a release or sharing
> the repo for review).
>
> Last regenerated: **2026-05-17** (after Spotify artist URL wired in)

---

## Open

### 🔴 High — Catalog her actual song library
**Type:** Asset · **Tags:** `asset` `notion`

Cataloging starts at the artist's actual existing artwork. For each released track on her Spotify (URL TBD — user to provide): add to Asset Library with Track Title, BPM, Duration, Mood tags, Available On (Spotify + any other DSPs), Spotify Link, current Status (likely Released), and any creative briefs/lyric sheets/references attached via Track Docs. Free-form notes (mastering history, inspiration, related tracks) go in the row body.

### 🔴 High — First-batch content seed
**Type:** Feature · **Tags:** `asset` `prompt` `outreach` `notion`

Populate the framework with the first real batch:
1. Log 5–10 tracks in Asset Library with BPM, duration, mood tags, current clearance status, and Available On platforms + Spotify Link.
2. Copy the 3 tier-template prompts from `prompts/` into Prompt Library and run each against one track.
3. Research 10 outreach targets (5 Twitch variety, 5 Itch.io cozy devs) and add to Outreach CRM with `Personal Hook` filled in for every one.
4. Write the first Session Log entry.

---

## Done

### ✅ Wire her Spotify artist page into the workspace — 2026-05-17
**Type:** Enhancement · **Tags:** `notion` `asset`

Spotify artist URL `https://open.spotify.com/artist/3AjmrMM0t7YekEDKnk5Tai` wired into: landing page metadata table + bookmark block, Master Strategy Blueprint Notion page (new "Artist" section), and repo `README.md` quick links. Per-track Spotify URLs go into each Asset Library track row's `Spotify Link` column as catalog progresses.

### ✅ Schema enhancements + Backlog DB + backup safeguard — 2026-05-17
**Type:** Enhancement · **Tags:** `notion` `asset`

Round-2 enhancements:
- Added Backlog DB to Notion as source-of-truth (HZ pattern).
- Extended Asset Library with `Available On` (multi-select platforms), `Spotify Link` (URL), and `Track Docs` (FILES).
- Built `scripts/notion_backup.py` + `scripts/notion_client.py` for scripted backups.
- Established the pre-change snapshot rule.

### ✅ Bootstrap LOFI_SANCTUARY project — 2026-05-17
**Type:** Feature · **Tags:** `asset` `design` `prompt` `outreach` `notion`

Initial scaffolding: public GitHub repo, Notion workspace with command-center landing + 5 DBs + 3 reference pages, local repo skeleton, master strategy blueprint mirrored into `docs/`, first-pass design system, stub prompt files, stub outreach templates.

Repo: https://github.com/Dazed-Shadow/LOFI_SANCTUARY (commits 072cb60 + 9f71939)
