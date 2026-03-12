# Tallon's Stronghold [Raid]

**Expansion:** Destiny of Velious (Exp 07)

This zone has 5 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [General Zevitus / Aakita](#general-zevitus--aakita) | Offensive toggle, dynamic curse avoidance, dual AE timers |
| [Mystikus](#mystikus) | Positioning only |
| [Lieutenant Klaatuus](#lieutenant-klaatuus) | Cure/don't-cure logic, totem moving (bards) |
| [Tyrax Terrolus](#tyrax-terrolus) | Offensive toggle, cure curse, banner joust |
| [Tallon](#tallon) | Positioning only |

---

## General Zevitus / Aakita

Setup command: `Set up for General`

### Overview

A fight with offensive toggling, dynamic curse avoidance across three positions, and dual AE timers.

### What the Module Does

**Offensive Toggle:**

- When the Zevitus detriment is detected, disables offensive abilities
- Re-enables when the detriment clears

**Dynamic Curse Avoidance:**

- Three camp positions arranged in a triangle
- Scans all raid members for curses and determines which positions have cursed players nearby
- If your current position is unsafe, automatically moves to a safe position
- Group 4 and cursed players are excluded from movement

**Dual AE Timers:**

- Inferno of War — 30-second HUD countdown
- Deluge of War — 30-second HUD countdown

### Player Notes

- Positions shift dynamically based on where cursed players are standing

---

## Mystikus

Setup command: `Set up for Mystikus`

### Overview

Positioning setup only.

### What the Module Does

**Positioning:**

- Sets camp position for the encounter

### Player Notes

- No automated mechanics beyond positioning

---

## Lieutenant Klaatuus

Setup is automatic when engaged.

### Overview

A fight with intelligent cure/don't-cure logic and an automated totem-moving mechanic for bards.

### What the Module Does

**Cure Logic:**

- Tactical Malaise — detects the cursed player and triggers cure curse
- Tactical Subversion — detects the afflicted player and displays a "Do NOT Cure" warning

**Totem Moving (Bards):**

- When a mysterious totem spawns, bards in groups 1/2 physically move the totem
- Automated camera zoom, movement, double-click pickup, carry to destination, and placement

### Player Notes

- Pay attention to the "Do NOT Cure" warnings — some curses must not be removed

---

## Tyrax Terrolus

Setup command: `Set up for Tyrax`

### Overview

A fight with offensive toggling, cure curses, and banner-based jousting.

### What the Module Does

**Offensive Toggle:**

- When the Tyrax detriment is detected, disables offensive abilities

**Cure Curses:**

- Touch of Tyrax — 60-second HUD timer, triggers cure curse
- Scent of Defeat — 10-second HUD, triggers cure curse with cleric priority

**Banner Joust:**

- When the Banner of Martial Warding despawns, non-priests joust to the joust spot
- When the Banner of Arcane Warding despawns, non-priests return to the raid spot

### Player Notes

- Jousting is triggered by banner despawns, not red text

---

## Tallon

Setup command: `Set up for Tallon`

### Overview

Positioning setup only.

### What the Module Does

**Positioning:**

- Sets camp position for the encounter

### Player Notes

- No automated mechanics beyond positioning
