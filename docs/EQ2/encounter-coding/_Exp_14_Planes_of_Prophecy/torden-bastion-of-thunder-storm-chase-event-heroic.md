# Torden, Bastion of Thunder: Storm Chase [Event Heroic]

**Expansion:** Planes of Prophecy (Exp 14)

This zone has 4 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Pre-Arkose Circles](#pre-arkose-circles) | Class-based circle positioning |
| [Arkose](#arkose) | 45-second patrol monitoring, automated pillar clicking sequence |
| [Frostward](#frostward) | Wind direction jousting, auto brazier clicking |
| [Oveld Stormwaker](#oveld-stormwaker) | Storm type add targeting, tornado following |

---

## Pre-Arkose Circles

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A pre-boss puzzle where the group must stand in specific circles.

### What the Module Does

**Class-Based Circle Positioning:**

- Assigns each group member to the correct circle based on their class role (bard, enchanter, priest, DPS)
- Handles the "odd man out" (second priest or second DPS) with a unique position

### Player Notes

- Set up for will get everyone into circles automatically

---

## Arkose

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight requiring 45-60 seconds of patrol monitoring before engagement, followed by automated pillar clicking.

### What the Module Does

**Patrol Monitoring:**

- The character with the arcane quartz rod monitors Arkose's patrol path for 45-60 seconds
- Records which 4 pillar locations Arkose visits and in what order

**Pillar Clicking Sequence:**

- When the boss heats up, jousts to the correct pillar in the monitored order
- Moves to the pillar, double-clicks it, and returns to the raid

### Player Notes

- The character with the arcane quartz rod initiates the monitoring sequence
- Make sure everyone has camp spot on

---

## Frostward

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with wind direction jousting and brazier clicking.

### What the Module Does

**Wind Direction Jousting:**

- When a cold wind blows from the southwest, moves to the southeast
- When a cold wind blows from the southeast, moves to the southwest

**Auto Brazier Clicking:**

- If the character has a spark of frost in inventory and is near an Ice Brazier, automatically clicks it

### Player Notes

- Keep sparks of frost in inventory for the brazier mechanic

---

## Oveld Stormwaker

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fully automated fight with storm type tracking, add targeting, and tornado following.

### What the Module Does

**Storm Type Add Targeting:**

- Parses the current storm type (firestorm, snowstorm, sandstorm, maelstrom)
- Automatically targets the correct counter-add for each storm type

**Tornado Following:**

- Once the correct tornado spawns, continuously updates the tank's camp spot to push the boss through the tornado

### Player Notes

- Completely automated -- make sure everyone has camp spot on
