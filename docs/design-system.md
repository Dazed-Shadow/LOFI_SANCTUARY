# Design System — Cozy Gamer Sanctuary

Every visual asset for LOFI_SANCTUARY must read at a glance as *cozy, lived-in, nostalgic*. The audience reflexively rejects anything that looks like "pro-gamer" content.

## Anti-patterns (instant-fail)

- Aggressive neon / RGB lighting
- Photoreal AI portraits
- Sci-fi or cyberpunk environments
- High-contrast hero compositions
- Bombastic motion / fast cuts
- Modern minimalist "tech bro" desk setups

## Art styles (pick one per asset)

1. **2D Retro Pixel Art** — Stardew Valley / Coffee Talk lineage. Soft anti-aliased pixels, limited palette per scene.
2. **3D Low-Poly** — A Short Hike / Lil Gator Game lineage. Flat-shaded, soft ambient occlusion, slight stylized exaggeration.

Both styles must feel hand-made, not procedurally generated.

## Color palette

Warm and organic only. Reference swatches:

| Token | Hex | Use |
|---|---|---|
| `sage-fog` | `#A8B89A` | Houseplant leaves, distant hills |
| `cream-paper` | `#F4ECD8` | Page backgrounds, mug ceramic |
| `earth-cocoa` | `#6B4F3F` | Wood desks, picture frames |
| `pastel-rose` | `#E8B4B8` | Sky at dusk, blush accents |
| `amber-lamp` | `#E8A857` | Warm light sources, lamp glow |
| `rain-slate` | `#5C6B73` | Window glass, rainy sky |
| `cocoa-night` | `#2B1F1A` | Nighttime backgrounds |

Avoid pure black, pure white, pure saturated primaries.

## Visual motifs (use 2-3 per composition)

- Lived-in desk setup (papers, pencil, half-finished project)
- Mechanical keyboard with warm-toned keycaps
- Steaming mug (coffee, tea, hot chocolate)
- Houseplant — pothos or monstera, slightly overgrown
- Sleeping pet (cat curled, dog on a rug)
- Rain or snow tracking past a window pane
- Bookshelf with mismatched paperbacks
- String lights or a single warm lamp
- Headphones resting on the desk
- An open notebook with a pen across it

## Light direction

Single warm key light (lamp, monitor glow, sunset through window). Soft shadows. Subtle rim light from a cooler ambient source (overcast window light) is fine for contrast.

## Per-track variance (cover gen)

The Cozy Gamer Sanctuary aesthetic is the **catalog-level umbrella** — landing page, masthead, brand voice, hero compositions. It is not a straitjacket that flattens every cover into the same look.

Individual track covers should reflect what the **track** actually does:

| Track mood / energy | Cover lean | Palette weighting |
|---|---|---|
| Rainy afternoon / midnight study | Classic cozy | sage-fog, rain-slate, cocoa-night, amber-lamp |
| Morning coffee / sunday lazy | Bright cozy | cream-paper, amber-lamp, pastel-rose, sage-fog |
| Autumn walk | Outdoor cozy | earth-cocoa, amber-lamp, sage-fog (muted) |
| Focused work / driving beat | Energetic / joy-leaning | brighter palette, slightly more saturation, possibly geometric motifs |
| High-BPM techno-leaning | Pull away from cozy | bolder color blocking, abstract shapes, but still **hand-crafted** and **no photoreal / no neon RGB** |

**What stays universal regardless of mood:**

- Hand-crafted feel (pixel art or low-poly, slight imperfection)
- No photoreal, no neon, no RGB, no sci-fi/cyberpunk
- No pure black, pure white, or pure saturated primaries
- Soft lighting, no harsh contrast

**What varies per track:** palette weighting, motif choice, energy level of composition, density of detail. A techno-leaning cover can be MORE abstract and bolder than a midnight-study cover — but both still feel made by a human, not extruded from a stock generator.

The cozy umbrella keeps the catalog readable as one body of work; the variance keeps each track's cover honest to the music.

## Loop discipline (Tier A pipeline)

Tier A 1-hour YouTube tracks demand **seamless loops** with zero tearing or canvas-drift. Two-step rule:

1. **Static foundation** — Midjourney / DALL-E 3 / OpenArt generates a pristine, finished background.
2. **Micro-animation only** — Kling / Freebeat animates *only* small isolated elements: rising steam, falling rain/snow, flickering lamp, blinking cat ear. Never let the AI re-render the canvas.

If the model can't be constrained to micro-movement, ship the asset as a static image with audio instead of a flawed loop.

## Caption / copy voice

Confessional and narrative — like a journal entry from someone designing a game that doesn't exist. First-person, soft, never salesy. Hooks should make the viewer wonder if the world is real.
