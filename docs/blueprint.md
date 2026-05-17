# LOFI_SANCTUARY — Master Strategy Blueprint

> Snapshot of the strategy doc that seeded this project. Source-of-truth lives at:
> `C:\Users\theri\OneDrive\Terminal\MR_C\GIT COWORK REFS\PWC\MASTER STRATEGY BLUEPRINT.md`
>
> Update this file when the source changes — don't edit it in isolation.

---

## Overview

**Role for Claude:** Creative Director, Copywriter, and Campaign Manager.

**Objective:** Weaponize a library of original lo-fi tracks to drive visibility, build a highly engaged social audience, and secure soundtrack placements or licensing agreements with indie game developers and streamers.

**Target audience:** The "Cozy Gaming" subculture (Stardew Valley, Animal Crossing, Coffee Talk, Unpacking), variety Twitch streamers, and indie game developers on Itch.io.

---

## Design System: Cozy Gamer Sanctuary

See [design-system.md](./design-system.md) for the full spec.

Anchors:
- 2D retro pixel art **or** 3D low-poly only
- Warm/organic palette (sage, cream, earth brown, pastel pink, amber)
- Visual motifs: desks, mechanical keyboards, mugs, houseplants, pets, rain/snow at a window
- No neon / RGB / sci-fi / photoreal

---

## Video production tiers

### Tier A — Long-form ambient loops (1-hour YouTube)
- **Platforms:** Freebeat or Kaiber, with Kling 2.6 or Google Veo 3.1
- **Pipeline:** Two-step — static foundation in Midjourney/DALL-E/OpenArt, then micro-animation only in Kling/Freebeat

### Tier B — Short-form socials & fake gameplay (15-30s)
- **Platforms:** CapCut or Pika, with Alibaba WAN 2.6 or Google Flow
- **Aesthetic:** Game-engine camera moves ("2D side-scrolling platformer camera tracking left-to-right")

### Tier C — Abstract audio-reactive visualizers
- **Platform:** Neural Frames (Stable Diffusion)
- **Mapping:** Geometric forms / color waves mapped to bass and treble bands

Prompt library lives in [`prompts/`](../prompts/README.md).

---

## Notion architecture

Three relational databases under the `MR_C · LOFI_SANCTUARY` Notion workspace:

1. **Asset Library** — raw audio files, duration, exact BPM, mood (e.g. "rainy afternoon," "morning coffee"), approved style reference images.
2. **Content Pipeline** — Kanban: *Ideation → Prompting → Rendering → Scheduled → Published* + engagement metrics.
3. **Outreach CRM** — indie devs (Reddit, Itch.io) + mid-tier Twitch streamers. Fields: Contact Info, Pitch Status (Not Contacted, Pitched, Followed Up, Partnered), Tracks Offered.

Bootstrap with `scripts/notion_setup.py` after auth (see [CLAUDE.md](../CLAUDE.md) for setup steps).

---

## Outreach playbooks

See [`outreach/`](../outreach/README.md) for templates.

- **Cozy Streamer Pack** — free, copyright-safe pack of pre-cleared tracks + loopable transition overlays for mid-tier Twitch/VTuber audiences.
- **Fake Cozy Dev Log Hook** — short-form videos of a character in a fictional cozy world synced to a track. Caption hooks the audience into a non-existent game.
- **Game Jam Funnel** — bundle tracks as free-to-use assets for Itch.io cozy game jam participants. Exchange: in-game credits + EPK link.

---

## Execution prompts

The original blueprint defines three reusable prompts for Claude:

- **A. Activate Notion Blueprint** — generate exact Notion DB columns/properties (now superseded by `scripts/notion_setup.py`)
- **B. Generate Video AI Prompts** — supply a song mood, get 3 shot-by-shot Kling/WAN prompts (use the templates in `prompts/`)
- **C. Indie Dev Outreach Script** — low-friction, warm outreach email (template in `outreach/itch-io-game-jam.md`)
