# Temple of Veeshan: Vulak's Dominion [Heroic]

**Expansion:** Tears of Veeshan (Exp 10)

This zone has 4 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Aegragis](#aegragis) | Invisible cube AoE joust |
| [Getiar Razorwing](#getiar-razorwing) | Positioning |
| [Dagrin the Defiler](#dagrin-the-defiler) | Dynamic boss-relative positioning, bard add targeting |
| [Ahrmatal the Scorcher](#ahrmatal-the-scorcher) | Fire avoidance repositioning |

---

## Aegragis

Setup command: `Set up for Aegragis`

### Overview

A fight with AoE avoidance jousting.

### What the Module Does

**AoE Joust:**

- When invisible cube AoEs spawn during combat, determines which position is closer and moves the raid to the opposite side

### Player Notes

- Ping-pong joust between two positions based on AoE spawn location

---

## Getiar Razorwing

Setup command: `Set up for Getiar`

### Overview

A positioning-only setup.

### What the Module Does

**Positioning:**

- Fighters at tank spot, others at raid spot

### Player Notes

- Positioning only, no mechanic automation

---

## Dagrin the Defiler

Setup command: `Set up for Dagrin`

### Overview

A fight with dynamic positioning relative to the boss and a bard add-killing mechanic.

### What the Module Does

**Dynamic Positioning:**

- Fighters are positioned behind the boss, non-fighters in front
- Positions update dynamically as the boss moves

**Bard Add Targeting:**

- When a Magmatic Malformation add spawns, bards automatically target it, move to its location, and kill it
- When the add despawns, bards return to their normal position

### Player Notes

- The raid follows the boss as it moves through the room

---

## Ahrmatal the Scorcher

Setup command: `Set up for Scorcher` (also accepts `Set up for Ahrmatal`)

### Overview

A fight with an automated fire avoidance system.

### What the Module Does

**Fire Avoidance:**

- When fire patches spawn near the current campspot, automatically searches for a fire-free location
- Tests multiple movement vectors and distances, checking each candidate spot for nearby fire
- Moves to the first safe position found, preferring movement toward the center of the room

### Player Notes

- The fire avoidance repositioning is fully automated
