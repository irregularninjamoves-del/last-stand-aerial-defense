# LAST STAND: Aerial Defense — Sprite Specification & Generation Prompts

This document lists every sprite the game needs to replace its procedural vector art, with exact sizes derived from the game's collision radii and draw code, plus copy-paste prompts for ChatGPT / DALL·E (or any image model).

---

## 1. Global rules (read first)

| Rule | Value | Why |
|---|---|---|
| Canvas | 1280 × 720 logical px | fixed internal resolution, scaled to screen |
| Asset scale | **Author at 2× the listed size** (so a 60×44 sprite is delivered at 120×88) | crisp on high-DPI phones and laptops; game downsamples |
| Format | PNG, transparent background (or flat **#FF00FF magenta** background if the tool can't do transparency — it will be keyed out) | |
| Facing | Player and player projectiles face **RIGHT**. Enemies, enemy projectiles face **LEFT**. Pickups/hazards are symmetric | side-scroller flying right |
| Camera | Pure **side view** (profile), no perspective/3-D tilt, no cast shadows | matches parallax layers |
| Origin | Centered on the sprite's collision circle (given per asset as `r`) | game positions by center |
| Style | Clean flat-shaded vector look with 2–3 tone cel shading, thin dark outline (1–2 px at 2×), slight rim-light on top edges, saturated palette, readable silhouettes at 50% size | must read at phone size in a horde of 80 |
| Palette | Player: steel blue-grey #c9d3e6 / #8fa2c4 with cyan canopy #4fd0ff and orange engine glow. Enemies each keep their **signature color** (below) so type is readable at a glance. Bosses: dark hull #3a1a10 with orange #ff6b3d panels (final variant magenta #ff4d8d) | color = enemy type in this game |
| Animation | Keep frame counts low; motion is mostly done in code (banking tilt, exhaust particles, hit-flash, telegraph glow). Where frames are listed, deliver as a **horizontal strip**, equal cells, 4 px padding, left→right | AI image tools are bad at multi-frame consistency |
| Sheet layout | One PNG per asset (strip if animated). File names as listed. Optional: a `sheet.json` with cell sizes | simple loader |
| Empty margin | Leave 4–8 px transparent margin around every sprite | glow/flash effects drawn around it |

---

## 2. Player

| File | Size (1×) | r | Frames | Notes |
|---|---|---|---|---|
| `player.png` | 64 × 48 | 14 | 1 (+ optional 3-frame bank strip: level / up / down) | Twin-engine jet fighter, delta wings, cyan bubble canopy, **two under-wing gun mounts** at ±9 px from centerline (visible barrels). Engine nozzle at rear center (exhaust is procedural). Faces right. |
| `player_shield.png` | 72 × 72 | — | 1 | Circular translucent blue energy shell (#5da8ff), 30 px radius, thin bright rim. |
| `player_dash.png` | 80 × 48 | — | 1 | Optional afterimage/motion streak, cyan, transparent. |
| `repair_drone.png` | 20 × 20 | — | 2 (rotor spin) | Small blue quad-drone with white cross (medic). |
| `armor_module.png` | 40 × 26 | — | 1 | Green (#6bff8f) external plating overlay drawn on top of player when Armor Mastery is taken. |

## 3. Enemies (all face LEFT)

| File | Size (1×) | r | Signature color | Frames | Notes |
|---|---|---|---|---|---|
| `drone.png` | 32 × 26 | 14 | orange-red #ff7a5c | 1 | Small fast fighter drone, diamond/dart hull, single engine, red sensor eye. |
| `bomber.png` | 54 × 34 | 22 | tan/brass #c9a25c | 2 (bay doors closed / open) | Slow fat twin-boom bomber; **bomb bay under belly** that glows red when open (telegraph). |
| `interceptor.png` | 36 × 26 | 16 | magenta #ff5db8 | 1 | Sleek swept-wing fighter, forked tail. |
| `cannon.png` | 58 × 58 | 26 | violet #a08cff | 2 (idle / barrel recoiled) | Round hover-platform with a **big forward cannon barrel** on its left side, glowing core in center (turns red on telegraph). |
| `swarm.png` | 18 × 12 | 8 | acid green #8fff5c | 2 (wing flap) | Tiny insectoid dart, dozens on screen — silhouette must read at 18 px. |
| `elite_ring.png` | 80 × 80 | — | gold #ffd36b | 1 | Gold rune-ring overlay drawn around any elite (mini-boss) variant; transparent center. |
| `mine.png` | 26 × 26 | 12 | brass + red LED | 2 (LED off/on) | Spiked sea-mine style, 6 spikes. |
| `debris_a.png` `debris_b.png` `debris_c.png` | 48 × 32 each | 12–24 | grey #5c5f68 with orange ember | 1 each | Wreckage chunks (fuselage slab, wing shard, engine block), one hot glowing spot. |
| `crate_supply.png` | 32 × 28 (+ parachute 32×24 above) | — | brass + green ring | 1 | Objective supply crate with a small parachute canopy above it. |

## 4. Bosses (all face LEFT)

| File | Size (1×) | r | Frames | Notes |
|---|---|---|---|---|
| `boss_mothership.png` | 280 × 140 | 70 | 3 (idle / turrets glowing red / damaged) | Massive elongated hull, dark plating with orange panel lines, **five turrets down the left/front side** (they glow red on telegraph), central glowing core window (cyan → red in final phase), 3 engine nozzles at rear. Drawn dark enough that bullets read on top of it. |
| `boss_prime.png` | 280 × 140 | 70 | 3 | Same silhouette, magenta/black "Hive Prime" reskin, extra spines. Used every 5th level. |
| `boss_laser.png` | 64 × 32 (tileable horizontally) | — | 1 | Horizontal red laser beam segment with white-hot core (tiled from 0 to boss). |

## 5. Projectiles & weapons

| File | Size (1×) | Frames | Notes |
|---|---|---|---|
| `bullet_assault.png` | 12 × 4 | 1 | Yellow tracer #ffd36b, bright center. |
| `bullet_laser.png` | 18 × 4 | 1 | Cyan #7df9ff needle. |
| `bullet_plasma.png` | 12 × 12 | 2 (pulse) | Blue-white orb #6bd1ff, soft glow. |
| `grenade.png` | 12 × 12 | 1 | Dark green sphere with light green (#9dff6b) ring. |
| `beam_segment.png` | 64 × 16 (tileable) | 1 | Pink #ff8adf beam with white core. |
| `rail_muzzle.png` | 48 × 48 | 1 | Violet #d19bff radial flash. |
| `ebullet_orange.png` | 10 × 10 | 1 | Enemy shot, orange #ff9955 with white center (drone/boss). |
| `ebullet_pink.png` | 10 × 10 | 1 | Interceptor shot #ff5db8. |
| `ebullet_violet.png` | 14 × 14 | 1 | Cannon heavy shell #c9b3ff. |
| `ebullet_red.png` | 12 × 12 | 1 | Boss ring bullet #ff5d5d. |
| `muzzle_flash.png` | 16 × 16 | 2 | Small yellow-white star burst (player mounts). |

## 6. Pickups (symmetric, 32 × 22 capsule)

| File | Notes |
|---|---|
| `pickup_health.png` | Green #6bff8f square with dark cross. 20×20. |
| `pickup_weapon_L.png` `_P` `_G` `_R` `_B` | Black rounded capsule 32×22 with colored border + big letter (L cyan, P blue, G green, R violet, B pink). Glow is procedural. |

## 7. Environment (per biome — 5 biomes: Coastal, Urban Ruins, Mountain Pass, Desert Wastes, Orbital)

Each biome needs the following **tileable horizontally** strips. Widths are tile widths; the game repeats them. Heights are the visible band.

| File | Size (1×) | Layer | Notes |
|---|---|---|---|
| `bg_<biome>_sky.png` | 1280 × 720 | 0 (static) | Gradient sky with sun/moon glow — or skip and keep procedural gradient. |
| `bg_<biome>_far.png` | 2400 × 300 | 1 (0.06×) | Distant mountains / skyline / dunes / stars. Silhouette, low contrast, atmospheric. |
| `bg_<biome>_mid.png` | 2400 × 400 | 2 (0.18×) | City / cliffs / rock spires with **destroyed buildings, fires** (fire glow can be procedural: leave dark windows/holes). |
| `bg_<biome>_near.png` | 2400 × 200 | 3 (0.4×) | Low hills / rooftops / clouds / water surface. |
| `bg_<biome>_ground.png` | 2400 × 60 | 3 | Bottom edge band (water for coastal, sand for desert, void for orbital). |
| `fg_wisps.png` | 256 × 8 ×4 variants | 4 (1.5×) | Fast foreground cloud/dust streaks, mostly transparent white. |
| `wreck_airliner.png` | 120 × 40 | bg | Falling/derelict civilian aircraft silhouette (2 variants). |
| `bird.png` | 12 × 8 | bg | 2 frames (flap), dark silhouette. |
| `cloud_soft.png` | 400 × 240 | zone | Big soft white cloud (pass-through obstacle). |
| `fire_zone.png` | 64 × 64 | zone | 4-frame flame loop tile, transparent. |
| `updraft_arrow.png` | 16 × 24 | zone | Faint white chevron for updraft/downdraft shimmer. |
| `lightning.png` | 64 × 720 | weather | Vertical bolt, white/blue, transparent (2 variants). |
| `rain_drop.png` `sand_grain.png` | 4 × 16 / 4 × 2 | weather | Optional; currently procedural. |

## 8. UI

| File | Size (1×) | Notes |
|---|---|---|
| `icon_talent_<id>.png` × 28 | 32 × 32 | One icon per talent (assault red, repair blue, durability green, radar amber). Flat glyph style, transparent. |
| `icon_ability_dash/weld/drone/strike/nuke/shield/react.png` | 40 × 40 | Ability chip icons. |
| `icon_hangar_<id>.png` × 10 | 32 × 32 | Hangar upgrade icons. |
| `logo.png` | 800 × 260 | "LAST STAND / AERIAL DEFENSE" title treatment, gold #ffd36b + white, retro-arcade chrome. |
| `icon_app.png` | 512 × 512 | App/store icon: the jet on dark navy #0b1230. |
| `btn_touch_ring.png` | 80 × 80 | Mobile ability button ring (transparent center). |
| `stick_base.png` `stick_knob.png` | 128 × 128 / 52 × 52 | Virtual joystick. |

## 9. FX (optional — most are procedural already)

| File | Notes |
|---|---|
| `explosion_small.png` | 8-frame strip, 48 × 48 cells, orange→smoke. |
| `explosion_big.png` | 10-frame strip, 128 × 128 cells (boss/nuke satellites). |
| `shockwave_ring.png` | 256 × 256 white ring, soft edges (nuke/level-up). |
| `smoke_puff.png` | 64 × 64 grey puff, 4 variants (plumes/debris trails). |

---

## 10. Priority order (what to make first)

1. `player.png`, the 5 enemies, `boss_mothership.png` — this alone transforms the game.
2. Projectiles + pickups.
3. One full biome background set (Coastal) to prove the pipeline, then the other four.
4. UI icons, logo, app icon.
5. FX (only if the procedural ones feel weak after 1–3).

---

## 11. Prompts for ChatGPT (image generation)

Paste the **STYLE BLOCK** at the top of every request so all assets match. Generate **one asset per image** for consistency; ask for a magenta background if transparency isn't supported.

### STYLE BLOCK (paste first, every time)

```
Create a 2D game sprite for a side-scrolling arcade shooter called "LAST STAND: Aerial Defense".
STYLE: clean flat-shaded vector art with 2–3 tone cel shading, thin dark outline, subtle rim light on
top edges, saturated colors, strong readable silhouette. Pure SIDE VIEW (profile), no perspective, no
3D tilt, no ground shadow, no background scenery. Centered on a solid #FF00FF magenta background
(or transparent PNG if supported), with a small empty margin around the sprite. No text, no watermark.
Output as a square/rectangular PNG suitable for a sprite sheet.
```

### Player jet
```
[STYLE BLOCK]
SUBJECT: the player's jet fighter, FACING RIGHT. Twin-engine delta-wing fighter, steel blue-grey hull
(#c9d3e6 body, #8fa2c4 wings), cyan bubble canopy (#4fd0ff), two visible under-wing gun barrels,
single rear engine nozzle glowing orange. Sleek, heroic, slightly retro-futuristic. Aspect ratio 4:3
(about 640×480 render; the game will scale to 128×96). Also acceptable: a horizontal strip of 3 poses —
level flight, banking up, banking down — with identical size and spacing.
```

### Fighter drone (enemy)
```
[STYLE BLOCK]
SUBJECT: a small fast enemy fighter drone, FACING LEFT. Dart/diamond-shaped hull, orange-red (#ff7a5c)
with dark grey underside, single glowing red sensor eye at the front, one small engine. Aggressive but
simple — must read at 32×26 pixels among dozens of others. Aspect ~5:4.
```

### Bomber (enemy)
```
[STYLE BLOCK]
SUBJECT: a slow heavy enemy bomber, FACING LEFT. Fat fuselage with twin tail booms and stubby wings,
tan/brass hull (#c9a25c) with dark panel lines, an obvious bomb bay on the belly. Provide TWO versions
side by side, same size and position: (1) bay doors closed, (2) bay doors open with a red glow inside.
Aspect ~8:5.
```

### Interceptor (enemy)
```
[STYLE BLOCK]
SUBJECT: a sleek enemy interceptor fighter, FACING LEFT. Swept-back wings, forked twin tail, needle
nose, magenta/hot-pink hull (#ff5db8) with dark accents and a small dark cockpit. Fast and elegant.
Aspect ~7:5.
```

### Cannon ship (enemy)
```
[STYLE BLOCK]
SUBJECT: an enemy hover gun-platform, FACING LEFT. Round/disc-shaped armored body in violet (#a08cff)
with dark grey plating, a large heavy cannon barrel protruding to the LEFT, a glowing core in the
center. Provide TWO versions side by side: (1) idle with a dim grey core, (2) firing with the core
glowing bright red and the barrel recoiled. Square aspect.
```

### Swarm unit (enemy)
```
[STYLE BLOCK]
SUBJECT: a tiny insectoid enemy swarm drone, FACING LEFT. Acid-green (#8fff5c) dart-shaped body with
two small wings and a dark tip. Extremely simple — this is drawn at only 18×12 pixels with 30–60 on
screen. Provide two frames side by side: wings up, wings down. Aspect 3:2.
```

### Mothership boss
```
[STYLE BLOCK]
SUBJECT: a massive enemy mothership boss, FACING LEFT. Long elongated hull (aspect 2:1), dark
plating (#3a1a10) with orange (#ff6b3d) panel lines and lights, FIVE turrets along the front/left
edge, a large glowing cyan core window near the front, three big engine nozzles at the rear.
Menacing, industrial, heavy. Provide THREE versions stacked vertically, identical size and position:
(1) idle, (2) all five turrets glowing bright red, (3) battle-damaged with cracks, smoke holes and
the core glowing red.
```

### Hive Mothership Prime (boss reskin)
```
[STYLE BLOCK]
SUBJECT: the same mothership silhouette as before (long 2:1 hull, five front turrets, big core
window, three rear engines), FACING LEFT, but re-skinned as "Hive Prime": black-purple hull with
magenta (#ff4d8d) glowing veins and lights, organic spines and ribbed plating. Three versions
stacked: idle / turrets glowing / damaged.
```

### Projectiles (one prompt, one sheet)
```
[STYLE BLOCK]
SUBJECT: a sprite sheet of small projectiles laid out in a single row with equal spacing, all
horizontal, all glowing with a bright white core:
1) yellow tracer bullet (#ffd36b) 3:1 elongated
2) cyan laser needle (#7df9ff) 4:1 elongated
3) blue-white plasma orb (#6bd1ff) round
4) dark green grenade sphere with a light green ring (#9dff6b)
5) orange enemy energy shot (#ff9955) round
6) pink enemy shot (#ff5db8) round
7) violet heavy shell (#c9b3ff) round, slightly larger
8) red boss ring bullet (#ff5d5d) round
```

### Pickups
```
[STYLE BLOCK]
SUBJECT: a row of game pickup icons, equal spacing: (1) a green health square (#6bff8f) with a dark
cross; then five black rounded capsules with a thin colored border and a large bold letter centered:
"L" cyan (#7df9ff), "P" blue (#6bd1ff), "G" green (#9dff6b), "R" violet (#d19bff), "B" pink (#ff8adf).
Slight glossy highlight on each capsule.
```

### Mine, debris, supply crate
```
[STYLE BLOCK]
SUBJECT: three hazard sprites in a row: (1) a spiked spherical mine, brass with six dark spikes and a
red LED (provide LED off and LED on variants); (2) three chunks of aircraft wreckage — a fuselage
slab, a wing shard, an engine block — grey (#5c5f68) metal with one glowing orange ember spot each;
(3) a brass supply crate with a green glowing ring and a small white parachute canopy above it.
```

### Backgrounds (one per biome; example: Coastal Defense)
```
Create seamless horizontally-tileable 2D parallax background layers for a side-scrolling shooter,
biome "COASTAL DEFENSE — harbor city under siege at dusk". Same flat vector cel-shaded style as the
sprites, no characters, no text. Deliver as separate images, each tileable left↔right:
LAYER FAR (2400×300): distant mountain range silhouette in muted blue (#2b3f66), low contrast, hazy.
LAYER MID (2400×400): coastal city skyline in dark navy (#141d30) with several buildings damaged and
burning (leave fire as bright orange glow spots), harbor cranes, smoke columns rising.
LAYER NEAR (2400×200): low sea cliffs / rooftops in #22345a, and a strip of dark ocean water at the
bottom with subtle wave lines.
Sky palette: deep navy top (#1a2b57) through steel blue (#5b7fb5) to warm gold at the horizon (#c8a26a).
```
Repeat with these biome briefs:
- **URBAN RUINS** — "the capital burns": dense skyscrapers, collapsed towers, smoke, ember-orange sky (#2b1c2c → #7a4a3c → #d09a5a), mid layer #1d1518, near #33232a.
- **MOUNTAIN PASS** — snow-capped peaks (#5c6f88 with white caps), pine ridges, cold blue sky (#0f1c30 → #3d5f8a → #b8d3e8), mid #2a3546, near #3d4c60.
- **DESERT WASTES** — dunes and mesas, wrecked convoys, hot orange sky (#3a1e0e → #b0603a → #f0c070), far #7a4a2a, mid #3d2614, near #5c3a1c.
- **ORBITAL ASCENT** — upper atmosphere/near space, starfield, curved planet horizon glow, aurora bands (green/violet), dark navy (#02030a → #0a1030 → #2a2050), silhouettes of orbital platforms.

### Talent / ability icons
```
Create a set of 32×32-style flat glyph icons for a sci-fi arcade shooter's talent tree, white/light
glyph on transparent (or magenta) background, bold and readable at small size, consistent 2px stroke,
no text. One icon per line:
Rapid Fire (three motion-blurred bullets), Multi-Shot (three diverging bullets), Piercing Rounds
(bullet through two rings), Artillery Mastery (shell + crosshair), Critical Strike (starburst with
lightning), Explosive Rounds (bullet with blast ring), Nuclear Stockpile (radiation trefoil),
Auto-Repair (wrench with circular arrows), Shield Generator (hex shield), Emergency Weld (welding
torch spark), Enhanced Recovery (heart with plus), Ablative Plating (layered plates), Drone Repair
(small drone with cross), Cooldown Mastery (clock with fast arrow), Reinforced Hull (thick hull
outline), Evasive Maneuvers (jet with speed lines), Damage Threshold (shield with "10" chip),
Heavy Plating (armor plate with rivets), Momentum Shield (arrow inside shield), Armor Mastery
(exo-armor frame), Reactive Barriers (shield with lightning bolt), Extended Range (radar sweep),
Threat Analysis (eye in target ring), Target Lock (crosshair locking), Weak-Point Scanner (magnifier
on crack), Salvage Beacon (magnet with sparkles), Predictive Tracking (dotted trajectory), Orbital
Uplink (satellite beam), Dash (chevrons), Nuke (mushroom cloud), Orbital Strike (beam column).
```

### Logo & app icon
```
Design a retro-arcade video game logo for "LAST STAND" with the subtitle "AERIAL DEFENSE".
Bold condensed uppercase, gold-yellow (#ffd36b) beveled chrome letters with a thin dark outline,
subtitle in white below, subtle jet silhouette streaking through the letters, slight 90s arcade
cabinet vibe. Transparent or dark navy (#0b1230) background, no other text.
---
Design a square app icon: the same steel-blue jet fighter (facing right, slight upward angle) centered
on a dark navy (#0b1230) rounded square with a faint radial glow behind it. Flat vector style, no text.
```

---

## 12. Tips for getting usable output

- Ask for **one subject per image**; sheets of many small objects lose consistency.
- If a result is close but the pose is off, reply: *"Same design, same colors, but strictly side profile facing LEFT, no perspective."*
- Always request the magenta background if you can't get transparency; remove it in any editor with a color-key/magic-wand at ~10% tolerance.
- Downscale in a real editor (Photoshop/GIMP/Aseprite) with bilinear filtering to the 2× target size, then check readability at 1× — that's the phone case.
- Keep the source renders; you'll want them for the store page.
