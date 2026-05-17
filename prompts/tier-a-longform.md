# Tier A — Long-form ambient loops (1-hour YouTube)

**Pipeline:** Static foundation (Midjourney / DALL-E 3 / OpenArt) → micro-animation only (Kling 2.6 or Freebeat).

**Discipline:** Animate ONLY isolated micro-elements (rising steam, falling rain/snow, flickering lamp). Never let the model re-render the canvas — that's how seams appear in the loop.

---

## Step 1 — Static foundation prompt template

```
A cozy [TIME_OF_DAY] scene rendered in [STYLE: 2D pixel art / 3D low-poly],
viewed through a [CAMERA_ANGLE: slight high-angle window-side / over-the-shoulder desk view].

Foreground: a lived-in desk with [MOTIFS: e.g. a steaming mug, mechanical keyboard, open notebook, sleeping cat].
Midground: a [HOUSEPLANT: pothos / monstera] in a clay pot, [BOOKSHELF / window pane].
Background: [WINDOW_VIEW: e.g. rain tracking down glass / soft snow falling / dusk sky over rooftops].

Lighting: single warm key light from [LAMP / MONITOR / WINDOW], soft shadows, slight rim from cooler ambient.
Palette: warm and organic — sage greens, cream, earth brown, pastel rose, amber.
Mood: [MOOD — e.g. quiet, focused, melancholic-but-safe].

NO neon, NO RGB, NO sci-fi, NO photoreal, NO modern minimalism.
Hand-crafted feel, slightly imperfect, lived-in.
```

---

## Step 2 — Micro-animation prompt template

```
Animate ONLY the following elements; leave EVERY other pixel completely still:

- [STEAM]: gentle rising wisps from the mug, looping every 4 seconds.
- [WEATHER]: [rain droplets tracking down the window / slow snowflakes drifting past].
- [LAMP]: subtle warm flicker every 6-8 seconds.
- [PET]: occasional slow breathing rise/fall of the sleeping cat's side.

Do NOT zoom, pan, or re-render any background detail.
Do NOT introduce new objects.
Camera is locked.
Loop must be seamless — first frame and last frame must match exactly.
```

---

## Proven prompts

*(Log here when a prompt produces a winning render. One-liner on what worked.)*

- *(none yet)*

---

## Common failure modes

- **Canvas drift** — model tries to re-render. Fix: hard-emphasize "camera locked, animate only X". Drop animated elements to 1-2 if needed.
- **Seam at loop boundary** — pick an even cycle length (4s, 6s, 8s) so all animated elements complete cleanly.
- **Palette creep** — model warms or cools the whole frame. Re-state the palette tokens explicitly.
- **New objects appear** — happens when prompt is too short. Always include "Do NOT introduce new objects."
