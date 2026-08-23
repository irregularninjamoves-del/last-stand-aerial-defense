# CLAUDE FABLE GAME BUILD PROMPT
## Space Shooter: Last Stand - Aerial Defense

---

## PROMPT FOR CLAUDE FABLE

```
You are an expert game developer. Build a procedurally-generated side-scrolling space shooter 
roguelike game called "LAST STAND: Aerial Defense" with the following specifications:

## CORE GAMEPLAY
- Side-scrolling 2D jet fighter that fires automatically with smooth parallax scrolling
- Player starts with two assault rifles (left/right mounts) and can unlock 5+ weapon types
- Procedurally-generated levels with themed encounters and a boss at the end
- Skill-based combat where enemy patterns are learnable and telegraphed (red flashes, etc.)
- Players must navigate environmental hazards (debris, wind, weather effects)

## PROGRESSION SYSTEM

### XP & Leveling (CRITICAL)
- Slower XP curve: players level every 2-5 minutes of gameplay
- Enemies grant 10-50 XP, bosses grant 200-500 XP, objectives grant 100 XP
- 3 stat points awarded per level to allocate to ASSAULT, REPAIR, or DURABILITY
- No hard caps; players can redistribute between runs
- Typical run: player reaches level 10-15 before final boss

### Three Talent Trees (Players can't unlock all abilities per run)

**ASSAULT TREE (Red - Weapon/Damage)**
- Rapid Fire: increase weapon fire rate by 30%
- Multi-Shot: bullets spread slightly (cone fire)
- Piercing Rounds: bullets go through multiple enemies
- Artillery Mastery: unlock grenade launcher, rail gun, beam cannon in this run
- Critical Strike: 15% chance for 2x damage on hits
- Explosive Rounds: bullets create small AoE explosions (10 radius)
- Weapon Swap Speed: switch between weapons 40% faster

**REPAIR TREE (Blue - Healing/Defense Buffs)**
- Auto-Repair: passively regenerate 1% max HP per second when not taking damage
- Shield Generator: absorb one hit (30s cooldown), recharge after 5s of non-combat
- Emergency Weld: instantly heal 25% HP (60s cooldown)
- Enhanced Recovery: healing effects are 30% stronger
- Ablative Plating: reduce damage taken by 15%
- Drone Repair: summon a repair drone that follows for 10 seconds (45s cooldown)
- Cooldown Mastery: all ability cooldowns reduced by 20%

**DURABILITY TREE (Green - HP/Armor)**
- Reinforced Hull: increase max HP by 25%
- Evasive Maneuvers: brief invulnerability dash (0.5s) with 8s cooldown
- Damage Threshold: ignore first 10 damage from each hit
- Heavy Plating: reduce all damage by 15% (stacks with Ablative Plating)
- Momentum Shield: speed increases defense (move at 2x speed = +10% defense)
- Armor Mastery: equip external armor modules (+30% max HP, -10% speed)
- Reactive Barriers: automatically block attacks that would be lethal (5 min cooldown)

## WEAPON PROGRESSION
- **Assault Rifles** (Start): Moderate damage (20), fast fire rate (0.1s), no spread
- **Laser Cannons** (Unlock at Wave 2): Higher damage (35), smaller magazine (20 rounds), more precision
- **Grenade Launcher** (Mid): AoE damage (50 damage in 40 radius), slower fire (0.8s), arcing trajectory
- **Rail Gun** (Late): High damage (80), pierces through enemies, slow fire (0.6s), high ammo cost
- **Beam Cannon** (Late): Continuous beam, 30 DPS, consumes ammo rapidly but high precision
- **Plasma Rifles** (Late): Homing projectiles (mild tracking), 40 damage, medium fire rate

## MISSILE SYSTEM (Limited Ordnance)

### Core Rules
- Player carries **2 missiles per level** (resets each level; not stockpiled between levels)
- Fired with a dedicated key/button (e.g., Shift on desktop, dedicated button on mobile)
- Missiles **explode on impact** with an AoE blast (60 radius, 100 base damage)
- Missile travels straight forward with a smooth exhaust flame trail
- Use the provided missile sprite asset (missile_asset.png — silver/blue missile with orange flame exhaust, transparent background). Scale it down to roughly 48-64px wide in-game and flip/rotate as needed for fire direction
- HUD shows missile count as 2 small missile icons near the weapon indicator; icons gray out when spent

### Missile Upgrades (Found During Runs)
- Blast Radius +25%
- Missile Damage +30%
- Extra Missile (+1 per level, max 4 total)
- Faster Missile Travel Speed +40%
- Reduced Self-Damage (immune to your own blast)

### Elemental Missile Specs (Player chooses ONE spec; tied to talent trees)
Each spec changes the missile's exhaust flame, trail particles, and explosion color so the player instantly knows what's loaded:

**FIRE SPEC (Orange/Red)** — Damage over time
- Explosion ignites all enemies in the blast
- Burning enemies take **4 damage per second** DoT for 6 seconds
- Visuals: orange-red exhaust flame, ember particle trail, fireball explosion, burning enemies flicker with small flame particles

**ICE SPEC (Cyan/White-Blue)** — Slowing debuff
- Explosion freezes/chills all enemies in the blast
- Chilled enemies have **movement speed AND attack speed reduced by 50%** for 5 seconds
- Visuals: pale cyan exhaust flame, frost mist trail, crystalline shatter explosion, chilled enemies get a frosty blue tint and slowed animations

**RADIATION SPEC (Toxic Acid-Green)** — Contagious armor shred
- Explosion irradiates all enemies in the blast
- Irradiated enemies have **defense/damage resistance reduced by 50%** for 8 seconds (they take way more damage from all sources)
- **CONTAGIOUS**: if an irradiated enemy comes within 50 pixels of a clean enemy, the radiation spreads to that ship too (spread enemies get the full debuff and can spread it further — chain reactions through tight formations)
- Visuals: sickly neon acid-green exhaust flame, dripping green particle trail, green mushroom-puff explosion, irradiated enemies pulse with a green glow and emit small trailing radiation particles (this glow is also the "I'm contagious" indicator)

### Spec Selection
- Player picks their missile spec at the start of a run (or via talent tree nodes: Fire under ASSAULT, Ice as a hybrid utility node, Radiation as a late-tier ASSAULT node)
- Spec can be changed between runs, not mid-run
- Unspecced missiles (before player unlocks any spec) are plain explosive with a standard orange blast

## ENVIRONMENTAL SYSTEMS

### Parallax Scrolling
- Implement 3-4 depth layers with different scroll speeds to create visual depth
- Foreground (fastest), mid-ground, background sky, distant mountains (slowest)
- Smooth camera following player position with slight lag for depth effect

### Weather System (Randomly selected per level)
- **Clear Skies** (10% chance): Normal gameplay, good visibility
- **Cloudy** (30%): Slight visual obstruction via semi-transparent cloud layer
- **Rain** (25%): Water particles falling, reduced visibility by 20%, audio ambiance
- **Storm** (20%): Heavy rain, lightning flashes (damage 50 HP if struck), wind gusts push player ±50 pixels horizontally every 3 seconds
- **Fog** (10%): Heavy visual obstruction (gray overlay), player radar becomes more important
- **Sandstorm** (5%): Sand particles reduce visibility, constant wind pushing player

### Environmental Hazards
- **Wind Gusts**: Directional force affecting player trajectory (varies 30-100 pixels per second)
- **Lightning Strikes**: Telegraphed by bright white flash 1 second before strike; deals 50 damage in 40 radius
- **Updrafts/Downdrafts**: Temporary zones (visible as shimmering air) that accelerate player up/down
- **Clouds**: Pass-through obstacles that obscure visibility; reduce sight radius by 50%
- **Falling Debris**: Wreckage from destroyed buildings; moves in predictable arcs, deals 15 damage on contact
- **Burning Areas**: Fire particle effects; deal 5 damage per second if player remains in zone

### ANIMATED LIVING BACKGROUNDS (High Priority)
The backgrounds must NOT be static images. Every parallax layer should have animated elements so the world feels alive and under active invasion. Implement these as looping particle systems and animated sprites baked into the parallax layers:

**Smoke (animate this specifically):**
- Smoke plumes rising from burning cities/wreckage in the background layers
- Use particle emitters: dark gray/black particles that spawn at the fire source, drift upward with slight horizontal sway, grow larger and fade to transparent as they rise
- 3-5 smoke columns visible per screen in damaged zones, each animating independently at slightly different speeds
- Wind direction affects smoke drift (storm weather bends smoke plumes sideways)

**Fires:**
- Flickering flame sprites on burning buildings/oil tanks (2-4 frame animation loop or procedural flicker via scale/opacity jitter)
- Warm orange glow pulsing on nearby terrain (animated light radius)

**Sky Life & Traffic:**
- Bird flocks flying across mid-background in V-formations with wing-flap animation (purely aesthetic, spawn every 20-40 seconds)
- Doomed military helicopters crossing the far background occasionally, some trailing smoke
- Falling debris/wreckage tumbling down in the distance with rotation

**Invasion Atmosphere:**
- Distant explosions: random background flashes that briefly light the sky, followed by a slow-rising smoke puff and faint delayed rumble sound (every 15-45 seconds)
- Searchlights sweeping across clouds in slow arcs (rotating light-cone sprites)
- Flickering, dying city lights on the horizon — small light clusters that randomly blink out over the course of the level (subtle storytelling: the world is going dark)
- Emergency beacon lights blinking red on base structures

**Weather Layer Animation:**
- Drifting cloud layers that move independently of parallax scroll speed
- Rain streaks angled by wind, with tiny splash particles on terrain surfaces
- Lightning: full-screen brightness flash + jagged bolt sprite, 1-frame afterglow
- Fog banks that slowly roll across the mid-ground

**Water (coastal level):**
- Animated wave shimmer on the ocean surface
- Fire reflections dancing on the water near burning structures

**Performance note:** Cap total ambient particles (~200 on screen) and use object pooling. Background animations should be cheap: sprite-frame loops and simple particle emitters, not physics simulations. Reduce ambient density automatically if FPS drops below 50.

## AI & ENEMY PATTERNS (Learnable, Not Adaptive)

### Enemy Types
1. **Fighter Drone**: Fast (speed 150), 20 HP, fires 3-shot bursts every 2 seconds, moves in predictable sine waves
2. **Bomber**: Slow (speed 80), 50 HP, drops mines every 3 seconds (mines explode on contact with player), stationary patterns
3. **Interceptor**: Medium (speed 120), 35 HP, tries to flank player, follows scripted circular patterns
4. **Cannon Ship**: Stationary or slow (speed 40), 80 HP, fires heavy salvos (5 projectiles in arc), pause between attacks
5. **Hive Swarm**: Small (5 HP each), 12+ enemies, coordinated but predictable swarm behavior
6. **Mothership Boss**: 300+ HP, multi-phase, see Boss Details section below

### AI Behavior (All patterns are scripted and learnable)
- Enemies move in predictable geometric patterns (sine waves, circles, spirals)
- Attack patterns are telegraphed: red muzzle flashes, audible wind-up sounds, projectiles have colored trails
- Each enemy has a 3-4 phase attack cycle that repeats
- Vulnerability windows exist during reload animations (brief pause where enemy can't fire)
- Enemies do NOT adapt to player tactics; they follow pre-determined scripts
- Pattern indicators: visual effects (red glow) before major attacks, consistent timing between attacks

## LEVEL STRUCTURE & PROCEDURAL GENERATION

### Chunk-Based Generation
- Levels built from pre-designed encounter tiles (no randomized geometry)
- Difficulty scaling: more enemies, stronger variants, complex patterns as player progresses
- Each level has 5-6 major encounter waves followed by a boss
- Encounters are mixed: combat waves, environmental navigation, mini-bosses, resource collection

### Level Progression (Example: Level 1 - Coastal Defense)
```
[START] → Wave 1: Patrol Squadron (4 Fighter Drones)
         → Wave 2: Debris Field (2 Bombers + falling wreckage)
         → Wave 3: Convoy Ambush (3 Cannon Ships + vehicles)
         → Wave 4: Reinforcements (2 Interceptors + 1 Bomber)
         → Wave 5: Bunker Defense (3 Turret Emplacements)
         → BOSS: Invasion Carrier (capital ship, multi-phase)
```

### Boss: Invasion Carrier (Level 1 Final Boss)
**Appearance**: Large capital ship with multiple weapon mounts and shield effects
**Health**: 300 HP
**Attack Pattern Cycle** (repeats, learnable):
  1. **Missile Barrage** (15 seconds): Red warning flash, launches 10 missiles in arc patterns, 3-second wind-up
  2. **Beam Sweep** (12 seconds): Slow-moving laser beam rotates 180 degrees, takes 8 seconds to sweep (player can outrun or dodge)
  3. **Drone Launch** (10 seconds): Spawns 5 fighter drones (same behavior as Wave 1), 30-second engagement window
  4. **Reload/Vulnerable** (8 seconds): Boss glows yellow, cannot fire; player can deal 2x damage

**Visuals**: Hull cracks spread across surface as player deals damage; final explosion is spectacular with debris flying
**Reward**: 500 XP, guaranteed level up, rare weapon upgrade token

## LEVEL 1: COASTAL DEFENSE (Dark Aesthetic)

### Visual Theme
- **Time**: Twilight/dusk, darkening toward night
- **Setting**: Abandoned coastal military base under alien attack
- **Color Palette**: Desaturated blues, grays, dark purples; warm orange fire accents
- **Sky**: Overcast, darkening horizon; distant city lights flickering and dying
- **Terrain**: Crumbling concrete fortifications, damaged buildings, burning oil tanks
- **Lighting**: Harsh searchlights sweeping, red emergency beacon lights, fire reflections on water

### Story Text (Minimal)
- **Opening Brief**: "Alien forces have breached our defenses. The coastal base is overrun. Your mission: survive and push back. Command will monitor your progress."
- **Before Boss**: "Carrier class vessel detected. This is their supply line. Take it down. All of humanity depends on your success."
- **Upon Victory**: "Excellent work, pilot. Proceed to next sector. We're counting on you."
- **Background Radio**: Static-filled chatter, distress calls, garbled orders (atmospheric only)

### Environmental Events During Level
- **Lightning Strikes** (30-40% chance): Random location warned by flash 1 second before impact
- **Wind Gusts**: Every 30 seconds, directional push (±60 pixels horizontally)
- **Smoke Waves**: Reduce visibility for 5-8 seconds periodically
- **Sky Events**: Distant explosion lights sky, helicopters pass overhead (doomed, adds atmosphere), searchlights sweep clouds

### Pacing & Difficulty
- **Waves 1-3** (Early): Teach mechanics, introduce learnable patterns, moderate difficulty
- **Waves 4-5** (Mid): Increase complexity, multi-enemy scenarios, environmental navigation
- **Wave 6 - Boss** (Late): Boss-specific mechanics, high intensity, reward for mastery
- **Target Duration**: 4-6 minutes completion time
- **Designed For**: Level 1-8 players (new to mid-game)

## UI REQUIREMENTS

### Heads-Up Display (HUD)
- **Health Bar** (top-left): Player hull integrity with visual damage effects, show HP numbers (e.g., 80/100)
- **Ammo Counter** (top-right): Current magazine / reserves (e.g., "32/128")
- **XP Bar** (bottom-center): Progress to next level with percentage, clear visual feedback
- **Radar** (bottom-left): Mini-map showing enemies (red dots), terrain (gray), player (green dot)
- **Weapon Indicator** (bottom): Currently equipped weapon name + available upgrades this level
- **Score** (top-center): Running total score (for leaderboards)

### Menus
- **Main Menu**: "Start Run", "Achievements", "Token Shop", "Settings"
- **Level-Up Screen**: Visual talent tree with branches, node hover-over shows ability description, click to allocate point
- **Pause Menu**: "Resume", "Settings", "Quit to Menu"
- **End-of-Run Screen**: Final score, XP earned, tokens earned, achievements unlocked, next level preview

### Audio UI
- **Level-Up Sound**: Distinctive ascending chime (high reward signal)
- **Enemy Death**: Satisfying explosion/spark sound + brief rumble
- **Low Health**: Warning beep that intensifies as HP decreases
- **Boss Appear**: Dramatic music shift + deep rumble effect
- **Music**: Dark, tense orchestral theme during gameplay; increases tempo during boss fight

## SAVES & PERSISTENCE

### Between-Run Data
- Total tokens earned (persists across runs)
- Achievements unlocked (persists)
- Unlocked skins (persists)
- High score leaderboard (local or cloud sync)

### During-Run Data
- Current level/wave
- Player position and state
- Ammo and weapon status
- HP and shield status
- Current XP and talent tree allocation
- Enemy positions (for pause/resume)

## TOKEN SYSTEM & SHOP

### Token Earnings
- Earn 10-50 tokens per completed run (based on final score and level reached)
- Bonus tokens for achievements
- Token multiplier for consecutive wins

### Token Shop Items
- **Skins** (50-200 tokens each): Fighter jet paint jobs, historical aircraft skins, exotic sci-fi designs
- **XP Boosts** (50-100 tokens): "+10% XP for next 10 runs" or "+25% XP for next 5 runs"
- **Cosmetics** (25-100 tokens): Weapon trails, engine effects, cockpit sounds, particle effects
- **Quality of Life** (200 tokens one-time): Inventory expansion, quick-restart button

## ACHIEVEMENTS (40+ Total)

### Difficulty/Progression
- "Survivor": Reach level 5
- "Veteran": Reach level 15
- "Master": Reach level 25
- "Sector Clear": Defeat a boss
- "Ten Bosses": Defeat 10 bosses total
- "Endurance": Survive 20 minutes in one run

### Combat
- "Century": Defeat 100 enemies in one run
- "Streak": Get 5+ consecutive kills without taking damage
- "Marksman": Deal 1000 damage to bosses in one run
- "Overkill": Kill an enemy with 50+ damage in one hit

### Skill-Based
- "Untouchable": Complete a level without taking damage
- "Arsenal Master": Unlock all 6 weapon types in one run
- "Full Tree": Unlock all talents from one tree
- "Speedrun": Complete level 1 boss in under 3 minutes

### Exploration/Collection
- "Scrapheap": Destroy 50 environmental hazards total
- "Skin Collector": Unlock 10 different skins
- "Token Millionaire": Earn 10,000 total tokens

## TECHNICAL SPECS

### Performance
- Target 60 FPS on mid-range devices
- Smooth parallax scrolling without lag
- Procedural generation should complete in <500ms
- Asset streaming for next encounter preload

### Browser/Mobile Compatibility
- Responsive controls (mouse for desktop, touch for mobile)
- Optimized graphics for web (webGL recommended)
- Keyboard controls: Arrow keys or WASD for movement, Spacebar to fire
- Mobile: Touch-drag for movement, tap to fire

## BUILD PRIORITIZATION (Start with Core)
1. **Foundation**: Player movement, 2 assault rifles, basic shooting mechanics
2. **First Enemy**: Fighter Drone with learnable sine-wave pattern
3. **Health & UI**: Health bar, XP bar, basic HUD
4. **First Boss**: Invasion Carrier with 4-phase pattern
5. **Talent Trees**: Basic allocation system for 3 stat trees
6. **Missile System**: 2-per-level missiles with explode-on-impact AoE, then the three elemental specs (Fire/Ice/Radiation)
7. **Procedural Gen**: Encounter chunk system
8. **Weather System**: Rain, storm, fog effects
9. **Animated Backgrounds**: Smoke plumes, fires, distant explosions, searchlights, birds, dying city lights
10. **Additional Weapons**: Grenade launcher, rail gun, beam cannon
11. **More Enemies**: Add bomber, interceptor, cannon ship, swarm
12. **Polish**: Particles, sounds, leaderboards, token shop

## NO ADS / NO MONETIZATION (For This Build)
- Do NOT include any ads, ad prompts, ad-reward buttons, or purchase flows in this version
- This build is for playtesting and demoing to others — keep it clean
- Tokens are earned purely through gameplay
- All shop items are purchasable with earned tokens only

## KEY DESIGN PRINCIPLES
- Enemies should NEVER feel unfair; all attacks are telegraphed
- Player skill matters: mastering patterns rewards the player
- No pay-to-win mechanics; tokens are cosmetic only
- Progression feels good: every level-up feels earned
- The world should feel like it's actively under invasion
- Dark tone, but not depressing; humanity has a fighting chance

## DO NOT INCLUDE
- Ads of any kind (no banners, no rewarded ads, no interstitials — this is a clean playtest build)
- Static, lifeless backgrounds (every layer needs animated elements per the Animated Living Backgrounds section)
- Random powerups falling from enemies (all upgrades are level-based)
- Guaranteed healing items (players must build for repair ability)
- Difficulty options (scaling is automatic via procedural difficulty)
- Tutorial overlays after level 1 (teach through gameplay)
- Bright, cartoonish colors (maintain dark, serious aesthetic)

Good luck, developer. Humanity's last stand begins now.
```

---

## NOTES FOR YOUR BUILD

1. **Start Small**: Begin with just the player jet, basic assault rifles, and one enemy type
2. **Playtesting Early**: Get the "feel" right before adding complexity
3. **Audio Matters**: Sound design will make this game feel impactful (explosions, weapon feedback)
4. **Talent Trees**: Consider using a node-based UI so players can see connections between abilities
5. **Boss Design**: Make sure the Invasion Carrier is challenging but fair; telegraph everything
6. **Parallax**: This is what makes a side-scroller feel alive; prioritize it early
7. **Story Through Action**: Minimal text; let the gameplay and visuals tell the story
8. **Replayability**: Once procedural generation is solid, each run should feel fresh

---

## POST-BUILD FEATURES (If you want to expand)
- Co-op multiplayer (2 players, screen split or shared)
- Daily challenges with unique modifiers (e.g., "No repair abilities")
- Narrative campaign mode (linear story progression)
- Leaderboard with timestamps and replay system
- Custom difficulty modifiers (hardcore mode, challenge runs)
