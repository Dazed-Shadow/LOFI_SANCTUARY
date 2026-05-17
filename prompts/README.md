# Prompt Library

AI video and image prompts, organized by pipeline tier. Each prompt file is a template — substitute the bracketed `[VARIABLES]` per track.

| File | Tier | Use |
|---|---|---|
| [`tier-a-longform.md`](./tier-a-longform.md) | A | 1-hour YouTube ambient loops — seamless, micro-animation only |
| [`tier-b-shortform.md`](./tier-b-shortform.md) | B | 15-30s TikTok/Shorts with game-engine camera moves |
| [`tier-c-visualizer.md`](./tier-c-visualizer.md) | C | Audio-reactive abstract visualizers (Neural Frames) |

## How to use

1. Pick the track from the **Asset Library** in Notion. Note its mood tag (e.g. *rainy afternoon*).
2. Open the matching tier file. Copy the prompt block.
3. Substitute the `[MOOD]`, `[TIME_OF_DAY]`, `[KEY_MOTIFS]` etc. tokens.
4. Generate. Log the result in the **Content Pipeline** Notion DB at the `Prompting` stage.
5. When a prompt produces a winner, copy it back into the corresponding tier file under "Proven prompts" with a one-line note on what worked.

## Don't

- Don't paste a tier-B "camera tracking shot" prompt into a tier-A pipeline. Tier A wants stillness; tier B wants motion.
- Don't drop the "no neon / no RGB / no photoreal" guardrails when shortening prompts — they're load-bearing.
- Don't fork the prompt files per-track. Keep templates lean; per-track variations live in Notion.
