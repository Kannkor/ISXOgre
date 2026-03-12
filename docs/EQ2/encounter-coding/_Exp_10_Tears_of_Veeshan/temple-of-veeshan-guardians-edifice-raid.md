# Temple of Veeshan: Guardian's Edifice [Raid]

**Expansion:** Tears of Veeshan (Exp 10)

This zone has 12 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Sontalak](#sontalak) | AE timer, idol of fire add tracking |
| [Rarthek the Swiftclaw](#rarthek-the-swiftclaw) | Spread positioning, armor crack/chomp detection, raptor egg tracking |
| [Jalkhir](#jalkhir) | Fireball warning joust |
| [Caden](#caden) | Attention draw fighter warning |
| [Tavekalem](#tavekalem) | Detriment orb-clicking automation, AE timer |
| [Derig Cinderaxe](#derig-cinderaxe) | Executioner add timer, trial interrupt |
| [Grendish](#grendish) | Multi-floor positioning, juggernaut health tracking |
| [Merig](#merig) | Four-group positioning, aerakyn add timer |
| [Andreis the Culler](#andreis-the-culler) | Sacrifice add timer, bone rot AE timer |
| [Klandicar](#klandicar) | Group-specific positioning, chaos ability timers, Tortoise Shell automation |
| [Zlandicar](#zlandicar) | Eating phase target management, bone spirit timer |

---

## Sontalak

Setup is automatic when engaged.

### Overview

A fight with AE timing and idol of fire add tracking.

### What the Module Does

**HUD Timers:**

- AE timer (45/71 seconds)
- Idol of fire add spawn countdown (55 seconds)

### Player Notes

- Timer-only tracking

---

## Rarthek the Swiftclaw

Setup command: `Set up for Rarthek`

### Overview

A complex fight with spread positioning, detriment detection, and raptor egg tracking.

### What the Module Does

**Spread Positioning:**

- Calculates 7 positions per raid group (6 spread + rogue swiping position)
- Priests are prioritized to specific positions
- Positions are dynamically calculated based on raid group number

**Armor Crack/Chomp Detection:**

- Monitors Armor Crack and Empowered Chomp detriments on fighters
- When detected, disables offensive actions and announces

**Raptor Egg Tracking:**

- HUD tracks raptor egg spawns and despawns

### Player Notes

- Starts the `ogre tov_rarthek` helper script on setup

---

## Jalkhir

Setup command: `Set up for Jalkhir`

### Overview

A fight with fireball warning jousting between two positions.

### What the Module Does

**Fireball Joust:**

- When a fireball warning spawns, jousts the raid out and moves to whichever of two positions is farther from the current location

### Player Notes

- Ping-pong joust between two spots

---

## Caden

Setup is automatic when engaged.

### Overview

A fight with an attention draw mechanic for fighters.

### What the Module Does

**Attention Draw Warning:**

- When a fighter draws attention, displays HUD with who drew it
- If you are the one who drew attention, targets self and plays a voice announcement

### Player Notes

- Fighter-specific warning mechanic

---

## Tavekalem

Setup command: `Set up for Tavekalem`

### Overview

A highly automated fight where players must click specific orbs to cure detriments.

### What the Module Does

**Orb-Clicking Automation:**

- Monitors 4 detriments: Wandering Mind, Slime Spray, Deteriorating Funk, Burning Skin
- Each detriment has a corresponding cure orb at a specific location (Arcanum, Curing, Ailment, or Aquatic Orb)
- When a detriment is detected, the player moves to the correct orb, HUD shows distance, and once in range auto-clicks it
- Returns to camp after the detriment is cured

**AE Timer:**

- Draconic Torrent timer (30/45 seconds)

### Player Notes

- The orb clicking is fully automated once the detriment is detected

---

## Derig Cinderaxe

Setup is automatic when engaged.

### Overview

A fight with executioner add spawns and a trial interrupt mechanic.

### What the Module Does

**Add Timer:**

- Executioner of Elements add spawn countdown (60-second timer)

**Trial Interrupt:**

- When Derig calls "Get over here and stand trial!", all characters apply the "Interrupt the trial!" verb

### Player Notes

- The trial interrupt is automated via uplink

---

## Grendish

Setup command: `Set up for Grendish`

### Overview

A complex multi-floor encounter with juggernaut add tracking.

### What the Module Does

**Multi-Floor Positioning:**

- Different campspots for the bottom floor (G2) with separate positions for sorcerers/rangers vs. others
- Fighter/non-fighter split positioning

**Juggernaut Tracking:**

- Tracks winter juggernaut spawns at 4 locations (Main, Bottom, North, South)
- Health-tracking HUDs for each juggernaut

### Player Notes

- Multiple floors require different positioning strategies

---

## Merig

Setup command: `Set up for Merig`

### Overview

A fight with four-group positioning and aerakyn add tracking.

### What the Module Does

**Four-Group Positioning:**

- Each raid group (1-4) has separate tank and group campspot positions

**Add Timer:**

- Aerakyn add spawn countdown (60-second timer) for disruptors, provokers, and devastators

### Player Notes

- Positioning is automatic based on raid group number

---

## Andreis the Culler

Setup is automatic when engaged.

### Overview

A fight with sacrifice add tracking and bone rot AE timing.

### What the Module Does

**HUD Timers:**

- Sacrifice of bone add spawn countdown (48 seconds)
- Bone Rot AE dual timer (60 seconds until end / 100 seconds until next)

### Player Notes

- Timer-only tracking

---

## Klandicar

Setup command: `Set up for Klandicar`

### Overview

A fight with group-specific positioning, chaos ability timers, and automated Tortoise Shell casting.

### What the Module Does

**Group-Specific Positioning:**

- Group 1 gets sub-positions for priests, rogues, and others

**Chaos Ability Timers:**

- Chaos Bolt I timer (60/90 seconds)
- Chaos Storm II timer (60/90 seconds) -- auto-casts Tortoise Shell 85 seconds later
- Chaos Storm III timer (60/90 seconds) -- auto-cancels Tortoise Shell on druids

**Curse Timer:**

- 60-second countdown on chaos creation

### Player Notes

- Tortoise Shell is automatically cast and canceled based on chaos storm timing

---

## Zlandicar

Setup is automatic when engaged.

### Overview

A fight with an eating phase where the boss must not be attacked.

### What the Module Does

**Eating Phase:**

- When Zlandicar starts eating bones, all characters target self (stop attacking)
- HUD shows 60-second countdown until eating is done
- When done eating, re-targets Zlandicar

**Bone Spirit Timer:**

- Add spawn countdown (70-second timer)

### Player Notes

- Attacking during the eating phase must be avoided
