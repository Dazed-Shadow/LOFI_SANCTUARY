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

## Loop discipline (Tier A pipeline)

Tier A 1-hour YouTube tracks demand **seamless loops** with zero tearing or canvas-drift. Two-step rule:

1. **Static foundation** — Midjourney / DALL-E 3 / OpenArt generates a pristine, finished background.
2. **Micro-animation only** — Kling / Freebeat animates *only* small isolated elements: rising steam, falling rain/snow, flickering lamp, blinking cat ear. Never let the AI re-render the canvas.

If the model can't be constrained to micro-movement, ship the asset as a static image with audio instead of a flawed loop.

## Caption / copy voice

Confessional and narrative — like a journal entry from someone designing a game that doesn't exist. First-person, soft, never salesy. Hooks should make the viewer wonder if the world is real.
