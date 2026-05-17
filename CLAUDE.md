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

Hybrid layout: HZ-style command-center landing page + the blueprint's 3 campaign databases + a Prompt Library section.

- **Command Center** (page) — dashboard with links to all DBs, current sprint focus, KPI summary
- **Asset Library** (DB) — every track: title, BPM, duration, mood, approved style refs, license status
- **Content Pipeline** (DB) — Kanban: Ideation → Prompting → Rendering → Scheduled → Published, with engagement metrics
- **Outreach CRM** (DB) — every streamer/dev target: contact info, pitch status, tracks offered, follow-up dates
- **Prompt Library** (page/DB) — every AI video/image prompt, organized by Tier A/B/C and tagged by mood
- **Session Log** (DB) — lightweight per-session record of what was done and what's next

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
