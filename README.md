# LAST STAND: Aerial Defense

Arcade horde side-scrolling shooter roguelike. Single self-contained `index.html` — no build step, no dependencies.

- 1000 procedurally generated levels, each harder than the last
- 6 weapons, 4 talent trees (Assault / Repair / Durability / Radar), 1 stat point every 3 levels
- Learnable, telegraphed enemy patterns; multi-phase mothership bosses
- Weather, hazards, parallax, procedural jungle/techno soundtrack
- Keyboard + mouse on desktop, touch controls on mobile (play in landscape)

## Run locally

Open `index.html` in a browser, or serve the folder:

```bash
python -m http.server 8733
```

## Deploy

Static site — point Vercel / Netlify / GitHub Pages at the repo root.

## Optional music

Drop MP3s at `music/title.mp3`, `music/boss.mp3`, `music/level1.mp3`, `music/level2.mp3`, `music/level3.mp3` to override the built-in synth soundtrack.
