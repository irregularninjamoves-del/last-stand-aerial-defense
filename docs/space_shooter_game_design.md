# SPACE SHOOTER - GAME DESIGN DOCUMENT
## "LAST STAND: Aerial Defense"

---

## CORE CONCEPT
A procedurally-generated side-scrolling space shooter (SHMUP) roguelike where players pilot an upgraded jet fighter against an alien invasion. Emphasis on skill-based combat, strategic talent tree progression, and weapon/stat customization. Dark, atmospheric aesthetic reflecting Earth's final stand.

---

## GAME OVERVIEW

### Setting
- **Time**: Present day alien invasion
- **Location**: Earth's atmosphere (skies, clouds, storms)
- **Tone**: Apocalyptic, desperate, but hopeful—humanity's last defense

### Story Hook
Aliens have invaded Earth. All military and civilian forces are mobilized. You are one of the last pilots. Your mission: hold the line and protect what remains. That's all you need to know. Go.

---

## CORE MECHANICS

### 1. FLIGHT & COMBAT
- **Player Control**: Side-scrolling jet (horizontal movement, vertical positioning)
- **Default Weapons**: Two assault rifles (left and right wing mounts)
- **Shooting**: Automatic fire with togglable manual aim
- **Movement**: Smooth acceleration/deceleration with inertia
- **Collision**: Physical collisions with terrain/obstacles (wind effects push the jet)

### 2. PROGRESSION SYSTEM

#### XP & Leveling
- **Slower XP Curve**: Players level every 2-5 minutes of gameplay
- **Level Reward**: 3 points per level to allocate to base stats
- **Max Levels**: 30+ (runs can reach this with good play)
- **No Hard Caps**: Players can redistribute points between runs

#### THREE STAT TREES

**ASSAULT (Red)**
- Base Stat: Weapon Damage, Fire Rate, Ammo Efficiency
- Abilities Include:
  - Rapid Fire (increase weapon fire rate)
  - Multi-Shot (bullets spread slightly)
  - Piercing Rounds (bullets go through enemies)
  - Artillery Mastery (unlock grenade launcher, rail gun, beam cannon)
  - Critical Strike (small chance for 2x damage)
  - Explosive Rounds (bullets create small AoE explosions)
  - Weapon Swap Speed

**REPAIR (Blue)**
- Base Stat: Self-heal rate, shield generation, cooldown reduction
- Abilities Include:
  - Auto-Repair (passively regenerate hull HP over time)
  - Shield Generator (absorb one hit, recharge after combat pause)
  - Emergency Weld (instantly heal 20% HP, long cooldown)
  - Enhanced Recovery (healing effects are 30% stronger)
  - Ablative Plating (reduce damage taken by percentage)
  - Drone Repair (summon a repair drone that follows for 10 seconds)
  - Cooldown Mastery (all ability cooldowns reduced)

**DURABILITY (Green)**
- Base Stat: Max HP, Damage Reduction, Armor
- Abilities Include:
  - Reinforced Hull (increase max HP by 25%)
  - Evasive Maneuvers (brief invulnerability dash, short cooldown)
  - Damage Threshold (ignore first 10 damage from each hit)
  - Heavy Plating (reduce all damage by 15%)
  - Momentum Shield (speed increases defense temporarily)
  - Armor Mastery (equip external armor modules)
  - Reactive Barriers (automatically block attacks that would be lethal)

#### Talent Tree Rules
- **3-5 Tiers** per tree
- **Branching Paths**: Multiple routes, not every ability available per run
- **Synergies**: Some abilities combo (e.g., Piercing Rounds + Explosive Rounds)
- **Respec Allowed**: Between runs only
- **Balanced**: No tree is strictly superior; all viable

### 3. WEAPONS & UPGRADES

#### Weapon Progression
- **Assault Rifles** (Start): Moderate damage, fast fire rate, no spread
- **Laser Cannons** (Mid): Higher damage, smaller magazine, more precision
- **Grenade Launcher** (Mid-Late): AoE damage, slower fire, arcing trajectory
- **Rail Gun** (Late): High damage, pierce through multiple enemies, slow fire
- **Beam Cannon** (Late): Continuous beam, high DPS but power-hungry
- **Plasma Rifles** (Late): Homing-style fire with mild tracking

#### Upgrade Mechanics
- **Per-Run Upgrades**: Found by defeating enemy squadrons or destroying enviro-hazards
- **Upgrade Types**:
  - Damage +15%
  - Fire Rate +20%
  - Magazine Size +10 rounds
  - Accuracy +30%
  - Reload Speed +25%
  - Unlock new weapon tier
  - Dual-Wield capability (add second weapon type)

#### Missile System (Limited Ordnance)
- **Count**: 2 missiles per level (resets each level; upgradeable to 4)
- **Behavior**: Fires straight forward, explodes on impact with AoE blast (60 radius, 100 base damage)
- **Asset**: Uses the provided missile sprite (silver/blue body, orange flame exhaust, transparent PNG)
- **Elemental Specs** (choose one, changeable between runs):
  - **FIRE (Orange/Red)**: Ignites enemies in the blast — 4 damage per second DoT for 6 seconds
  - **ICE (Cyan/White-Blue)**: Chills enemies — movement speed AND attack speed reduced 50% for 5 seconds
  - **RADIATION (Toxic Acid-Green)**: Irradiates enemies — defense resistance reduced 50% for 8 seconds, and it's CONTAGIOUS: spreads to any clean enemy that comes within 50px of an infected one, chaining through formations. Infected ships pulse with a green glow.
- **Missile Upgrades**: Blast radius, damage, extra missile count, travel speed, self-damage immunity

#### Plane Customization
- **Hull Types** (visual/stat differences): Fighter (balanced), Interceptor (speed), Gunship (armor)
- **Wing Modifications**: Narrow wings (speed), Wide wings (stability), Swept wings (maneuverability)
- **Engine Upgrades**: Afterburner, Quick-turn, Hover-mode (limited)
- **Cockpit Modules**: Targeting computer, radar jammer, prediction sight

---

## ENEMY AI & PATTERNS

### AI Behavior (Learnable Patterns)
- **Patrol Formation**: Enemies move in predictable geometric patterns (sine waves, circles)
- **Attack Rotation**: 3-phase attack cycle (player can memorize and avoid)
- **Telegraphed Moves**: Red flash indicates upcoming attack
- **Adaptation**: Enemy doesn't adapt to player tactics; it follows scripted cycles
- **Vulnerability Windows**: Brief moments where enemy is exposed (reward for patience)

### Enemy Types
- **Fighter Drone**: Fast, low damage, swarm tactics
- **Bomber**: Slow, high damage, predictable patterns, drops mines
- **Interceptor**: Medium speed, medium damage, tries to flank
- **Cannon Ship**: Stationary or slow, fires heavy artillery
- **Mothership**: Mini-boss, large health pool, multi-phase attack pattern
- **Hive Swarm**: Many small enemies with coordinated attacks

---

## LEVEL GENERATION & PROGRESSION

### Procedural Generation
- **Chunk-Based**: Levels built from pre-designed encounter tiles
- **Difficulty Scaling**: More enemies, stronger variants, complex patterns as player progresses
- **Environmental Variety**: Each sector has themed obstacles
- **Guaranteed Boss Nodes**: Every 3-5 encounters, player faces a boss

### Environmental Systems

#### Parallax Scrolling
- **3-4 Depth Layers**: Foreground terrain, mid-ground objects, background sky, distant mountains
- **Smooth Scrolling**: No screen-locking; camera follows player with slight lag
- **Visual Depth**: Parallax speed increases with depth

#### Weather System
- **Clear Skies**: Normal gameplay (10%)
- **Cloudy**: Slight visual obstruction, improved atmosphere (30%)
- **Rain**: Reduced visibility, environmental particles, audio ambiance (25%)
- **Storm**: Lightning flashes, heavy rain, wind gusts push player jet (20%)
- **Fog**: Heavy visual obstruction, reliance on UI radar (10%)
- **Sandstorm** (desert zones): Sand particles reduce visibility, wind mechanics (5%)

#### Environmental Effects
- **Wind**: Directional force affecting player trajectory; can help or hinder
- **Lightning Strikes**: Rare environmental hazard, telegraphed by flash
- **Updrafts/Downdrafts**: Temporary zones that affect vertical movement
- **Clouds**: Pass-through obstacles that reduce visibility
- **Falling Debris**: Wreckage from destroyed buildings/aircraft
- **Burning Areas**: Zones with fire particles; minor damage if touched

#### Animated Living Backgrounds
All parallax layers contain animated elements — nothing is a static painting:
- **Smoke Plumes**: Particle emitters at fire sources — dark particles rise, sway, grow, and fade; wind bends the columns
- **Fires**: Flickering flame sprites with pulsing orange glow on nearby terrain
- **Birds**: Flocks in V-formation with wing-flap animation, crossing every 20-40 seconds
- **Doomed Helicopters**: Cross the far background occasionally, some trailing smoke
- **Distant Explosions**: Random sky flashes + slow-rising smoke puffs + delayed rumble (every 15-45s)
- **Searchlights**: Slow rotating light cones sweeping the clouds
- **Dying City Lights**: Horizon light clusters that randomly blink out during the level — the world going dark in real time
- **Water Shimmer**: Animated waves with fire reflections dancing near burning structures (coastal levels)
- **Performance**: ~200 ambient particle cap, object pooling, auto-reduce density under 50 FPS

---

## XP & LEVELING DETAILS

### Experience Gain
- **Enemy Kill**: 10-50 XP (scales with enemy tier)
- **Objective Completion**: 100 XP per sector cleared
- **Environmental Destruction**: 5-20 XP per destructible
- **Boss Defeat**: 200-500 XP

### Level Scaling
- **Slow Curve**: First level at 100 XP, increases by 50 XP per level
- **Level 1-5**: ~100-300 XP each
- **Level 6-15**: ~350-600 XP each
- **Level 16+**: ~700+ XP each
- **Typical Run**: Player reaches level 10-15 before final boss

### Stat Point Allocation
- **Per Level**: 3 points to distribute
- **No Minimum**: Can dump all into one stat if desired
- **Respec Between Runs**: Full reset allowed after each run ends

---

## PROGRESSION: ACHIEVEMENTS & TOKEN SYSTEM

### Achievements (40+ total)
- **Difficulty Milestones**: Reach level 10, 20, survive 20 min run
- **Combat**: 100 enemies defeated, 10 bosses defeated, 5-kill streak
- **Skill-Based**: Beat level without taking damage, reach sector 5, perfect run
- **Exploration**: Destroy all environmental hazards in one level, find hidden area
- **Collection**: Unlock all weapons, unlock all abilities, complete all talent trees
- **Challenge**: Kill 3 bosses without repair ability, beat game on hard mode

### Token System
- **Earn**: 10-50 tokens per run (based on score/performance)
- **Token Shop**:
  - **Skins**: Fighter jet paint jobs, historical aircraft skins, exotic skins (50-200 tokens)
  - **XP Boosts**: +10% XP gain for next 10 runs (50 tokens), +25% for next 5 runs (100 tokens)
  - **Cosmetics**: Weapon trails, engine effects, cockpit sounds (25-100 tokens)
  - **Quality of Life**: Inventory expansion (one-time, 200 tokens)

---

## LEVEL DESIGN: FIRST LEVEL DARK AESTHETIC

### Theme: "Coastal Defense"
- **Time**: Twilight/dusk (dark, moody)
- **Location**: Abandoned coastal military base under attack
- **Atmosphere**: Desperate last stand, previous defenders already overwhelmed

### Visual Design
- **Palette**: Desaturated blues, grays, dark purples; warm orange fire accents
- **Sky**: Overcast, darkening toward the horizon; distant city lights flickering and going out
- **Terrain**: Crumbling concrete fortifications, damaged buildings, burning oil tanks
- **Lighting**: Harsh searchlights sweeping, emergency red beacon lights, fire reflections on water

### Layout
```
[START] → Patrol Squadron → Debris Field → Convoy Ambush 
   ↓
Reinforcements Arrive → Bunker Defense → BOSS: Invasion Carrier
```

### Encounters

**Wave 1: Patrol Squadron**
- 4 Fighter Drones in V-formation
- Predictable sine-wave movement pattern
- Telegraphed machine gun fire (red muzzle flashes)
- Reward: First weapon upgrade token (+damage)

**Wave 2: Debris Field**
- Navigational hazard section mixed with 2 Bomber ships
- Falling wreckage moves in predictable arcs
- Bombers follow perimeter, drop mines on intervals
- Tutorial moment for environment interaction
- Reward: Repair upgrade token or XP bonus

**Wave 3: Convoy Ambush**
- 3 Cannon Ships positioned along a coastal road
- Fire vertically at player; pattern is wait → 3-shot burst → pause → repeat
- Civilian trucks (non-hostile) moving across screen; destruction triggers story beat
- Reward: Multiple upgrade tokens, level up

**Wave 4: Reinforcements Arrive (Mini-Boss)**
- 2 Interceptor ships + 1 Bomber
- Interceptors flank in coordinated strike; learnable timing
- Brief lull for repair/recalibration
- Reward: Significant XP, talent point earned

**Wave 5: Bunker Defense (Scenario)**
- Stationary turret emplacements (3 total)
- Turrets have predictable 180-degree sweep patterns with safe spots
- Player must navigate through kill zones
- Optional: Destroy turrets for bonus XP
- Reward: Optional equipment

**Wave 6: BOSS - Invasion Carrier**
- **Appearance**: Large capital ship, multiple weapon mounts, shields
- **Attack Pattern** (4-phase cycle):
  1. Missile Barrage (telegraphed by red warning, salvo of projectiles, learnable dodge)
  2. Beam Sweep (slow-moving laser, player can outrun or dodge)
  3. Drone Launch (5 fighter drones spawn, similar to Wave 1)
  4. Pause/Reload (brief vulnerability window where player can deal heavy damage)
- **Difficulty**: Moderate; teaches boss mechanics without overwhelming
- **Visual**: Explosions across hull as player damages it; final explosion is spectacular
- **Reward**: 500 XP, major upgrade token, level up guaranteed

### Environmental Events During Level
- **Lightning Strike** (50% chance): Random location warned by flash; adds tension
- **Wind Gusts**: Every 30 seconds, directional push to player (learning challenge)
- **Smoke Waves**: Reduce visibility temporarily; reliance on audio cues
- **Sky Events**: 
  - Distant city explosion lights up sky briefly
  - Military helicopters pass overhead (doomed, adds atmosphere)
  - Spotlights sweep across clouds

### Audio Landscape
- **Background**: Distant explosions, low atmospheric hum, wind
- **Weather**: Rain/storm sounds if weather active
- **Combat**: Machine gun fire, missile launches, explosions with spatial audio
- **Music**: Dark, tense orchestral theme; tempo increases during boss fight

### Story Elements (Minimal Dialogue)
- **Opening Briefing** (text overlay): "Alien forces have breached our defenses. The coastal base is overrun. Your mission: survive and push back. Command will monitor your progress."
- **During Level**: Static radio chatter, garbled distress calls in background
- **Upon Reaching Boss**: "Carrier class vessel detected. This is the invasion's supply line. Take it down."
- **Boss Defeated**: "Excellent work, pilot. Proceed to next sector. We're counting on you."

### Difficulty & Pacing
- **Early Encounters** (Waves 1-3): Teach mechanics, introduce patterns
- **Mid Encounters** (Wave 4): Increase complexity, multi-enemy scenarios
- **Late Encounters** (Waves 5-6): Boss-specific mechanics, high intensity
- **Designed For**: Level 1-8 player; completes in 4-6 minutes

---

## UI/UX ELEMENTS

### HUD
- **Health Bar** (top-left): Player hull integrity with visual damage effects
- **Ammo Counter** (top-right): Current magazine + reserves for equipped weapon
- **XP Bar** (bottom): Progress to next level, clear visual feedback
- **Radar** (bottom-left): Mini-map showing enemies, terrain, player position
- **Weapon Indicator** (bottom-center): Currently equipped weapon, upgrades available
- **Score** (top-center): Running total, leaderboard tracking

### Menus
- **Main Menu**: Start Run, View Achievements, Token Shop, Settings
- **Pause Menu** (mid-run): Resume, Quit to Menu, Settings
- **Talent Tree Screen** (level-up): Visual tree, click to allocate points, preview stat changes
- **End Screen**: Final score, XP earned, tokens earned, achievements unlocked, leaderboard position

### Audio UI
- **Level-Up Sound**: Distinctive chime, player knows immediately
- **Enemy Death**: Satisfying explosion/spark sound
- **Low Health**: Warning beep that intensifies
- **Boss Appear**: Dramatic music shift + rumble effect

---

## TECHNICAL ARCHITECTURE (HIGH-LEVEL)

### Engine Recommendation
- **HTML5/Canvas + JavaScript** (web), or **Godot/Unity** (native)
- **Physics**: Custom 2D physics for jet movement + environment
- **Procedural Generation**: Tile-based encounter system with pre-designed chunks
- **Networking** (Optional): Leaderboard sync, token system persistence

### Save Data
- **Between Runs**: Player stats, total tokens, achievements, unlocked skins
- **During Runs**: Current level, player position, ammo, HP, XP, talent tree allocation

### Performance Targets
- **60 FPS** on mid-range devices
- **Dynamic LOD**: Reduce visual effects (parallax layers, particle density) on weaker hardware
- **Asset Streaming**: Pre-load next encounter while current one plays

---

## MONETIZATION
**None for this build.** No ads, no purchases — this is a clean playtest/demo version. Tokens are earned only through gameplay. Monetization can be revisited later once the game is proven fun.

---

## FUTURE EXPANSIONS
- Additional weapon types (plasma, rail variants)
- New maps (desert, space, underground bunker)
- Multiplayer co-op (2-player campaign)
- Daily challenges with unique modifiers
- Narrative expansion (story-driven campaign mode)

---

## SUMMARY
A skill-based roguelike space shooter with deep progression systems, procedural challenge, and a dark atmospheric setting. Emphasis on learning enemy patterns, strategic upgrade choices, and rewarding player mastery. Designed to be accessible to new players while offering high skill ceiling for veterans.
