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
> Last regenerated: **2026-05-17** (after audio-file constraint + EPK scaffold)

---

## Open

### 🔴 High — Build Gaming EPK / Portfolio HTML site
**Type:** Feature · **Status:** In Progress · **Tags:** `design` `outreach`

Public-facing artist landing page that doubles as the outreach EPK for streamers and (eventually) game devs. Scaffold shipped at `epk/` — single-page vanilla HTML + CSS, cozy aesthetic, placeholder copy clearly marked. Sections live: hero, about, featured tracks (Spotify embed slots), cover gallery, licensing (stream-safe + game-safe + custom commissions), contact, footer. Pending: artist public name, bio (3-4 sentences), 3 featured track Spotify IDs, contact channel. Deployment via GitHub Pages from `/epk` folder when filled in.

### 🔴 High — Source raw audio files from the artist (target: end of 2026-05-24 weekend)
**Type:** Asset · **Tags:** `asset` `licensing`

Audio files only exist on Spotify currently — blocks BPM extraction script, Tier A loop generation, and Tier C visualizer rendering. JR is asking the artist for raw MP3/WAV masters. Once received: drop into local audio library (gitignored), run `scripts/extract_bpm.py` to backfill BPM, unblock Tier A/C. Half the pipeline gates on this.

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

### ✅ BPM extraction tooling + cover-gen variance decision — 2026-05-17
**Type:** Enhancement · **Tags:** `tooling` `aesthetic` `pipeline`

Round-5 enhancements:
- **`scripts/extract_bpm.py`** (librosa-based) — extracts BPM + duration from local audio files. Prints half/double sanity columns because lo-fi rhythm patterns can fool simple beat trackers. Includes `scripts/requirements.txt`.
- **Decision: Cover-gen aesthetic variance** logged in 🧠 Decisions DB — cozy is the catalog umbrella, but per-track mood drives style (techno/joy-leaning when track calls for it). `docs/design-system.md` updated with the "Per-track variance" section spelling out palette weighting by mood.
- **Decision: BPM via librosa, not Spotify Web API** logged in 🧠 Decisions DB — Spotify audio-features endpoint was deprecated for new apps Nov 2024; local-first is more durable.
- **CLAUDE.md per-track pipeline** updated: BPM extraction is now step 1 (not manual entry).

### ✅ Decisions DB + Asset Library cover-art schema + per-track design pipeline — 2026-05-17
**Type:** Enhancement · **Tags:** `notion` `asset` `pipeline` `workflow`

Round-4 enhancements:
- **🧠 Decisions DB** added (HZ pattern) — captures architectural / creative-direction calls with rationale and alternatives. Distinct from Backlog (items) and Session Log (activity). Seeded with 4 foundational decisions: Hybrid Notion architecture, Separate Notion workspace, Safeguard rule + ADD-only philosophy, Tier C as secondary vehicle with Neural Frames + cozy-constraints.
- **Asset Library schema extended** (6 ADD-only columns): `Artist Cover Art` (FILES), `JR Cover Art` (FILES), `AI Cover Art` (FILES), `JR Alt Title` (RICH_TEXT), `Video Link` (URL), `Cover Selected` (multi-select Artist/JR/AI — blend optionality).
- **Per-track design pipeline** documented in CLAUDE.md: row → BPM/Mood → AI Cover gen → JR review → Cover Selected (allows blends) → Tier A/B/C render → Video Link populated.
- **Session-start ritual** documented in both landing page and CLAUDE.md so backlog items Jonathan adds directly are picked up at the start of every session.
- **9 total DBs** now backed up by `notion_backup.py`.

Pre-change snapshot: `scripts/backups/session_2026-05-17_pre-decisions-db-and-cover-art.json`.

### ✅ Owner Log + References DBs + 2-column landing layout — 2026-05-17
**Type:** Enhancement · **Tags:** `notion`

Round-3 enhancements:
- **📔 Owner Log DB** (Notion-only) — personal log distinct from agent Session Log. Schema: Entry Title, Date, Energy (High/Medium/Low/Drained), Tags (idea/reaction/decision/concern/win/observation/family/craft/business), Linked Track relation, Entry rich text.
- **🔗 References DB** — external tools/sites/communities by Category (AI Image/Video/Audio/Visualizer Gen, Indie Game Community, Game Jam, Streaming Platform, Outreach Tool, Licensing, Reading, Other) + Status + Tags. Seeded with 8 starters: Kling AI, Pika, Neural Frames, Midjourney, OpenArt, Itch.io, Twitch, Reddit r/IndieDev.
- **2-column landing layout** — metadata table left, References preview right. Fixed misplaced Safeguard heading from previous round.
- **`journal/` directory** — local gitignored markdown companion to Owner Log DB. README explains conventions.
- **`notion_backup.py` + `.env.example`** updated for the 2 new DBs (8 total now).

All schema additions, no destructive changes. Pre-change snapshot in `scripts/backups/session_2026-05-17_pre-owner-log-and-references.json`.

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
