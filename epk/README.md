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
| Hero — artist name | 🟡 Placeholder | Artist's public name + one-line tagline |
| Hero — Spotify CTA | ✅ Live | Wired to her Spotify artist URL |
| About | 🟡 Placeholder | 3–4 sentence bio |
| Featured tracks | 🟡 Placeholder | 3 Spotify track IDs (Spotify → Share → Copy link → grab `/track/{ID}` portion) |
| Cover gallery | 🟡 Placeholder | Real covers as AI/JR/Artist covers come online from the Asset Library |
| Licensing | ✅ Draft copy | Replace `[Artist Name]` in the credit line; refine wording with her once she reviews |
| Contact | 🟡 Placeholder | Pick a channel — dedicated email alias recommended |

Placeholders render visibly on the page (italic with dashed amber underline) so unfilled slots are obvious.

## Deployment

Not yet deployed. Options when content is ready:

- **GitHub Pages** — simplest. Enable Pages on the repo with source = `main` branch + `/epk` folder. Free, lives at `https://dazed-shadow.github.io/LOFI_SANCTUARY/`.
- **Vercel / Netlify** — connect repo, custom domain, more bells.
- **Custom domain** — point a domain at GitHub Pages or Vercel.

Decision deferred until the page is filled in and JR confirms the artist is comfortable being publicly attributed (per `CLAUDE.md`, she stays anonymous unless she opts in).
