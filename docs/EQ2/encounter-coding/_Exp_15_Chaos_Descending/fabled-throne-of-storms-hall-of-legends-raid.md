# Fabled Throne of Storms: Hall of Legends [Raid]

**Expansion:** Chaos Descending (Exp 15)

This zone has 4 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Legatus Prime Mikill](#legatus-prime-mikill) | Auto wiggle movement below 50% HP, HUD timers |
| [Arch-Magistor Modrfrost](#arch-magistor-modrfrost) | Item-based arcane/elemental cures, shaman/non-shaman curse cure split |
| [Imperator Kolskeggr](#imperator-kolskeggr) | HUD timers for add and static spawns |
| [King Tormax](#king-tormax) | Red text jousting, HUD timer |

---

## Legatus Prime Mikill

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where the raid must continuously move below 50% boss HP to avoid a mechanic.

### What the Module Does

**Auto Wiggle Movement (Below 50% HP):**

- Once the boss drops below 50% health, the module moves the raid camp spot in a square pattern every 8 seconds
- Cycles through 4 positions to prevent a mechanic from landing

**HUD Timers:**

- Giant Swipe countdown (45 seconds)
- Flurry of Punches countdown (35 seconds)

### Player Notes

- The wiggle movement is fully automated below 50% HP

---

## Arch-Magistor Modrfrost

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A complex fight with multiple cure types requiring specific items and cure assignments.

### What the Module Does

**Arcane Cure (Ghastly Pallor):**

- Tracks affected players and displays HUD with target names
- If the character has an Echo Fragment item in inventory, automatically targets and cures the affected player

**Elemental Cure (Everlasting Fire):**

- Same pattern as arcane -- tracks targets and auto-cures with Elemental Shard of Frost item

**Curse Cure Split (Lethal Proximity / Magistor's Scourge):**

- Displays curse targets on HUD
- Shamans handle the first curse, non-shamans handle the second curse

**Knockback Timer:**

- HUD displays a 27-second countdown for Cyclonic Freeze

### Player Notes

- Keep Echo Fragments and Elemental Shards of Frost in inventory for automatic curing
- Curse curing is split between shamans and non-shamans

---

## Imperator Kolskeggr

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight tracked by HUD timers for add and elemental spawns.

### What the Module Does

**HUD Timers:**

- Adds (kromzek stormtrooper) spawn countdown (78 seconds)
- Static storm elemental spawn countdown (78 seconds)

### Player Notes

- The HUD timers help coordinate the raid around add spawn patterns

---

## King Tormax

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with red text jousting and camp spot alternation.

### What the Module Does

**Red Text Jousting:**

- When an energy vortex forms, the group jousts out and camp spots swap between two positions

**HUD Timer:**

- Ghostly Siphon countdown (45 seconds)

### Player Notes

- Group 3 priests have a separate camp spot for the dragon mechanic
- Camp spots alternate between two positions after each joust
