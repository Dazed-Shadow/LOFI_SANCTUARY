# LOFI_SANCTUARY — Project Context

Creative campaign to drive visibility and licensing deals for an original lo-fi music library, aimed at the cozy gaming subculture, mid-tier Twitch variety streamers, and indie game developers on Itch.io.

This is a creative/marketing project, not a deployed application. There is no backend service — the artifacts here are strategy, prompts, templates, assets, and automation glue.

## Stack

| Layer | Tech |
|---|---|
| Strategy doc | Markdown (this repo + Notion) |
| AI video pipeline (Tier A) | Freebeat / Kaiber → Kling 2.6 or Veo 3.1 |
| AI video pipeline (Tier B) | Pika / CapCut → WAN 2.6 or Google Flow |
| AI video pipeline (Tier C) | Neural Frames (audio-reactive) |
| Static image gen | Midjourney / DALL-E 3 / OpenArt |
| Audio | Original WAV/MP3 library (gitignored — too large) |
| Workspace | Notion (`MR_C · LOFI_SANCTUARY`) — relational DBs |
| Outreach channels | Email, Reddit, Itch.io, Twitch DMs |

## Repo layout

```
docs/
  blueprint.md           # The master strategy (source of truth for direction)
  design-system.md       # Cozy Gamer Sanctuary — palette, motifs, anti-patterns
prompts/
  README.md              # Index of all AI prompts
  tier-a-longform.md     # 1-hour YouTube ambient loops
  tier-b-shortform.md    # 15-30s TikTok/Shorts (fake cozy dev log hooks)
  tier-c-visualizer.md   # Audio-reactive abstract visualizers
outreach/
  README.md              # Playbook index + status conventions
  cozy-streamer-pack.md  # Pitch for mid-tier Twitch/VTuber
  itch-io-game-jam.md    # Pitch for indie game devs / jam packs
assets/                  # Small refs only (palettes, mood boards)
scripts/
  notion_setup.py        # One-time Notion workspace bootstrap
  notion_client.py       # Reusable Notion API helper
.github/                 # Workflows (placeholder)
BACKLOG.md               # User-owned running log — single source of truth
CLAUDE.md                # This file
README.md                # Public repo landing
```

## Critical creative constraints

- **No "pro-gamer" aesthetic.** Aggressive neon/RGB themes are an instant-fail for this audience. Stick to warm/organic — sage greens, cream tones, earth browns, pastel pinks, warm amber light.
- **Pixel-art or low-poly only** for visuals. Photoreal AI imagery breaks the nostalgia hook.
- **Visual motifs are non-negotiable:** lived-in desks, mechanical keyboards, steaming mugs, houseplants (pothos/monsteras), sleeping pets, rain/snow outside a window.
- **Seamless loops, no tearing.** Tier A pipeline is two-step: generate static foundation, then animate only micro-movements (rising steam, falling rain) — never let the AI animate the whole canvas.
- **Stream-safe / Game-safe by default.** All tracks offered to streamers and devs must be pre-cleared for broadcast and in-game use. Track this in the Notion Asset Library.

## Key conventions

- **Track every asset in Notion first, then push files to the repo.** The Notion Asset Library is the source of truth for which track is approved for which use case.
- **Outreach status lives in Notion CRM, not in markdown.** `outreach/` holds the *templates*; the *targets and status* belong in the Outreach CRM DB.
- **Caption style for short-form: confessional / world-building.** Example: *"Designing a cozy farming RPG that doesn't exist yet, just so I have an excuse to listen to this track. Should I actually build the game?"* — narrative hooks outperform straight track promotion.
- **Audio files are gitignored.** Repo stays lean; raw WAV/MP3s live in the user's local library and are referenced by name from the Asset Library DB.

## Agent workflow — Opus + Sonnet + Notion

Same two-tier pattern as HORIZON_SEARCH:

| Agent | Role |
|---|---|
| **Opus** | Orchestrator — creative direction, campaign strategy, outreach prioritization |
| **Sonnet** | Implementer — writes prompts, drafts outreach copy, formats Notion entries |
| **Notion** | Shared memory — Asset Library, Content Pipeline, Outreach CRM are the live state |

**When to invoke Opus:**
- New campaign phase / new platform (e.g. adding YouTube Shorts strategy)
- Brand voice or design system decisions
- Pricing / licensing structure for placements
- Pitch strategy for a new tier of partner

**How to invoke Opus in Claude Code:** Agent tool with `subagent_type: "claude"` and `model: "opus"`. Pass the question with full creative context. Opus writes recommendation; Sonnet drafts and logs to Notion.

## Notion workspace — `MR_C · LOFI_SANCTUARY`

Workspace: separate top-level Notion workspace (`LOFI Sanctuary`), auth'd via the `plugin:engineering:notion` OAuth flow. Does NOT share an integration with the HZ workspace — isolated by design.

**Landing page:** [MR_C-LOFI_SANCTUARY](https://www.notion.so/MR_C-LOFI_SANCTUARY-363c30e1314880319921dcf0a2f7770b) — HZ-style command center with embedded DB views, current focus, agent workflow.

| Page / DB | URL | Role |
|---|---|---|
| Command Center (landing) | https://www.notion.so/MR_C-LOFI_SANCTUARY-363c30e1314880319921dcf0a2f7770b | Dashboard, links to everything |
| 📋 Master Strategy Blueprint | https://www.notion.so/363c30e13148810699afe593526ac2ef | Strategy summary (canonical lives in `docs/blueprint.md`) |
| 🎨 Design System | https://www.notion.so/363c30e131488159aff3fbd6981d3e7d | Cozy Gamer Sanctuary spec (canonical in `docs/design-system.md`) |
| 🧭 Quick Reference | https://www.notion.so/363c30e131488164b084d2d65ccf6df7 | Status conventions, caption voice, session checklist |
| 📌 **Backlog** | https://www.notion.so/9d0a30fd4fef43c4ad788770f8fcaaa5 | **Source of truth** for items. `BACKLOG.md` in the repo is a regenerated snapshot. |
| 🧠 **Decisions** | https://www.notion.so/209730e36c5245fdac808ab602a1ed6d | **Source of truth** for design/architecture/creative-direction calls with rationale + alternatives. Distinct from Backlog (items) and Session Log (activity). |
| 🎵 Asset Library | https://www.notion.so/cdf82b386d3b4bd28ea250ea0d4fbb05 | Every track + clearance status. Includes `Artist/JR/AI Cover Art`, `Cover Selected` (multi-select for blend optionality), `JR Alt Title`, `Video Link`, `Available On`, `Spotify Link`, `Track Docs`. |
| 🎬 Content Pipeline | https://www.notion.so/019118f7c515411ab4fe38b8e2cd1b45 | Kanban — ideation to published |
| 📨 Outreach CRM | https://www.notion.so/5338e679565a4caf85fdcae8dfa39f4d | Streamer/dev contacts + pitch status |
| ✍️ Prompt Library | https://www.notion.so/d41b2e5f8481479e93e12d3d209ec4ec | Proven AI video/image prompts by tier |
| 📓 Session Log | https://www.notion.so/7e81ea6e91fc4d4aad6d24620eda593a | Per-session state for resume-ability (Opus + Sonnet activity) |
| 📔 **Owner Log** | https://www.notion.so/8e7af2a7f62d41b5a67bf530472bc1be | Jonathan's personal log — ideas, reactions, decisions. Notion-only; paired with local gitignored `journal/` directory. Distinct from agent Session Log. |
| 🔗 **References** | https://www.notion.so/7ae8adbd39b04bbba01187c5801312c5 | External tools/sites/communities by category (AI gen, indie communities, streaming platforms, etc.) |

## Session start ritual (do this every session, in order)

1. Read the most recent **📓 Session Log** entry's `Next session` field — picks up where the prior session left off.
2. Skim **📌 Backlog** for items Jonathan added between sessions. Filter `Status = Open`, sort by `Date` desc. **Jonathan's direct-add rows are safe** — Claude only edits specific page IDs, never `replace_content` on the DB itself.
3. Check **🧠 Decisions** for any `Pending` items needing review or ratification.
4. Glance **🎬 Content Pipeline** at `Rendering` or `Scheduled` stages — has anything stalled?
5. Glance **📨 Outreach CRM** for `Follow Up` dates due today.

## Per-track design pipeline

For each track in the Asset Library, the path from row to rendered output:

```
Row created (min: Track Title + Spotify Link)
  → BPM extracted via `python scripts/extract_bpm.py <audio_folder>`
       outputs Filename + BPM + half/double sanity + duration
       JR pastes BPM + duration into the Asset Library row
  → JR fills Mood tags (+ JR Alt Title if the official title is generic)
  → AI Cover Art generated (Midjourney/OpenArt) — prompt derived from:
       BPM (high = lean energetic/joy/techno; low = lean cozy)
       Mood (drives palette weighting per docs/design-system.md "Per-track variance")
       Design system universals (hand-crafted, no photoreal/neon/RGB)
  → JR review → keep AI cover, paint a JR Cover, or fall back to Artist Cover
  → Cover Selected (multi-select) marks which cover(s) feed downstream — blends allowed
  → Tier A loop | Tier B narrative short | Tier C visualizer
       Tier A: Midjourney static → Kling micro-animation, 1hr YouTube
       Tier B: Pika/WAN game-engine camera, 15-30s short-form
       Tier C: Neural Frames audio-reactive (SECONDARY vehicle, cozy-constrained prompts)
  → Video Link populated → Content Pipeline entry created tying track + prompt + render
```

**On cover-gen variance (Decisions DB):** The cozy aesthetic is the catalog umbrella, not a straitjacket. A high-BPM track can lean energetic/techno/joyful; a melancholy track leans cozy/rainy. The design system's universals still hold (hand-crafted, no photoreal/neon) but palette weighting and motif density vary per track. See `docs/design-system.md` → "Per-track variance".

**On Tier C (Neural Frames):** Per the Decisions DB, Tier C is a *secondary* vehicle — useful for audio-only contexts (YouTube auto-visualizers, sleep/focus playlists) where motion is expected, but it fundamentally fights the cozy gaming aesthetic. Prompts must aggressively constrain output toward sage/cream/amber palette with soft particle drift, NOT default-Neural-Frames psychedelia.

**On BPM extraction (Decisions DB):** `scripts/extract_bpm.py` (librosa-based) extracts BPM + duration from local audio files. Spotify Web API audio-features was considered and rejected (deprecated for new apps Nov 2024). The script prints half/double sanity values because librosa can octave-error on lo-fi rhythm patterns.

## Safeguard & backups

**Rule: no structural Notion change without a snapshot first.**

- **Pre-change snapshot.** Before any DB schema change, Claude writes a `scripts/backups/session_YYYY-MM-DD_*.json` capturing the schema + row counts of all DBs. Read-only — written via MCP fetch tools, never touches Notion.
- **Scripted full backup.** `python scripts/notion_backup.py` snapshots every page in every DB to `scripts/backups/backup_*.json`. Keeps the 10 most recent. Setup steps in `scripts/notion_client.py`.
- **ADD-only philosophy.** `ADD COLUMN` is fine. `DROP COLUMN` on a populated field is forbidden without (a) a fresh backup, (b) a Session Log entry explaining why.
- **Restore.** Backup JSON contains every page object. Recreate the DB via the Notion API and replay the pages from the most recent backup.

`scripts/backups/` is gitignored — backups stay local, never commit them.

**Session start checklist:**
1. Read BACKLOG.md for open items
2. Check Notion Session Log for the most recent session's "Next session" notes
3. Check Notion Content Pipeline for anything in `Rendering` or `Scheduled` that may have moved
4. Review Outreach CRM for follow-up dates due today

## Notion setup (one-time)

Run from the repo root after adding `NOTION_API_KEY` and `NOTION_ROOT_PAGE_ID` to a local `.env`:

```
python scripts/notion_setup.py
```

Requires the Claude/MR_C Notion integration to be connected to the root page in the Notion UI first (page ••• → Connections → add the integration).

## Owner preferences

- **Vibe over volume.** A handful of high-craft assets beats a flood of low-effort ones.
- **The relative behind the music is family** — protect her name and image; she stays anonymous unless she explicitly opts in to any given asset or pitch.
- **Outreach is warm, never cold-spam.** Personal note per recipient. Mass DMs are an instant-fail.
- **BACKLOG.md lives in the repo** — edit it there, not in a separate local copy.
- **Commit messages: concise, explain WHY not what.**
