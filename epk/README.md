# Gaming EPK / Portfolio

Public-facing artist landing page that doubles as the outreach EPK for streamers and game devs.

Single-page, vanilla HTML + CSS — no framework, no build step.

## Preview locally

```powershell
# Just open in a browser:
start epk\index.html
```

For a slightly better local experience (so relative paths and `fetch()` work properly later):

```powershell
# From repo root, with Python on PATH:
python -m http.server 8000 --directory epk
# Then open http://localhost:8000
```

## Layout

```
epk/
├── index.html       Main page (hero, about, tracks, gallery, licensing, contact)
├── styles.css       Cozy Gamer Sanctuary palette + responsive layout
├── assets/          Cover art, hero images go here (gitignored except dropped files)
└── README.md        This file
```

## What's filled / what's pending

| Section | Status | Needs |
|---|---|---|
| Hero — artist name | ✅ Mad Bunni | Placeholder stage name (artist's Spotify display is "Jahna."). Final stage name TBD by artist. |
| Hero — tagline | ✅ Filled | "Lo-fi for cozy games you haven't played yet." Tweak if it doesn't sit right. |
| Hero — Spotify CTA | ✅ Live | Wired to her Spotify artist URL |
| About | 🟡 Two drafts inline | Draft A (first-person, confessional) is active; Draft B (third-person) is commented out. Pick one, delete the other. Both anchor to her real Spotify bio line. |
| Featured tracks | 🟡 Placeholder | JR picks headliner + 2 suggestions in the chat. Then I wire all 3 Spotify embeds. |
| Cover gallery | 🟡 Placeholder | Real covers as AI/JR/Artist covers come online from the Asset Library |
| Licensing | ✅ Live | Credit line now uses "Mad Bunni". Refine wording when artist reviews. |
| Contact | 🟡 Placeholder | JR to register a dedicated alias (suggestions in HTML comment). Paste address into placeholder. |

## Discovered catalog (for reference when picking featured tracks)

Pulled from Spotify on 2026-05-17. IDs below are **album/EP** IDs (Spotify embed works for both tracks and albums).

| Release | Type | Year | Spotify ID |
|---|---|---|---|
| Selected Works for Imaginary Video Games | Album | 2026 | `3GM7KYuMlY94b93mpdmUvQ` ← on-brand for the pitch |
| Just another DnB. | Single | 2026 | `1eAj6up63imTZAFp4NUiy4` |
| Just another DnB Part 2. | Single | 2026 | `0DmC2jhIfjNJ117kPGmhBF` |
| Painting Hue Study No. 1 | Single | 2026 | `3NN5QUYThg9xuLmsgDUrrG` |
| β-catenin Bumps | Album | 2025 | `21S6fFYeSvjvdBYRoANZwu` |
| GOTW (Extended Play) | EP | 2025 | `3GzlTOH6pQCWysIQEaXVkF` |
| Ride With Us | Single | 2025 | `0XMDkYlaLetdSD0j1fxOLF` |
| Cheese | Single | 2025 | `78dXDgby5zJTE7GpPdbn8V` |
| LOOPSCOOPS (Instrumental) | EP | 2025 | `0oYHlwk3YIaP5iFZyGxXm3` |
| i think not─ nah | Single | 2024 | `4iCTSY2Pm4uYMOGWojS23z` |

Embed URL format: `https://open.spotify.com/embed/album/{ID}?utm_source=generator`

Placeholders render visibly on the page (italic with dashed amber underline) so unfilled slots are obvious.

## Deployment

Not yet deployed. Options when content is ready:

- **GitHub Pages** — simplest. Enable Pages on the repo with source = `main` branch + `/epk` folder. Free, lives at `https://dazed-shadow.github.io/LOFI_SANCTUARY/`.
- **Vercel / Netlify** — connect repo, custom domain, more bells.
- **Custom domain** — point a domain at GitHub Pages or Vercel.

Decision deferred until the page is filled in and JR confirms the artist is comfortable being publicly attributed (per `CLAUDE.md`, she stays anonymous unless she opts in).
