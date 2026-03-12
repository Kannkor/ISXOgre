# Throne of Storms [Raid]

**Expansion:** Destiny of Velious (Exp 07)

This zone has 4 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Legatus Prime Mikill](#legatus-prime-mikill) | Dual AE timers |
| [Tormax](#tormax) | Red text joust, AE timer |
| [Imperator](#imperator) | Positioning only |
| [Arch-Magistor Modrfrost](#arch-magistor-modrfrost) | AE timer, item-based arcane/elemental cures, dual curse tracking |

---

## Legatus Prime Mikill

Setup command: `Set up for Legatus`

### Overview

A fight with dual AE timers.

### What the Module Does

**Dual AE Timers:**

- Giant Swipe — 45-second HUD countdown
- Flurry of Punches — 35-second HUD countdown

### Player Notes

- Timer-only module with positioning

---

## Tormax

Setup command: `Set up for Tormax`

### Overview

A fight with red text jousting and an AE timer.

### What the Module Does

**Red Text Joust:**

- On energy vortex announcement, toggles between two camp positions
- 10-second cooldown prevents rapid toggling

**AE Timer:**

- Ghostly Siphon — 45-second HUD countdown

**Positioning:**

- Group 3 priests have separate dragon-side positions when a phantasmal remnant exists

### Player Notes

- Standard two-position toggle joust

---

## Imperator

Setup command: `Set up for Imperator`

### Overview

Positioning setup only.

### What the Module Does

**Positioning:**

- Sets camp position for the encounter

### Player Notes

- No automated mechanics beyond positioning

---

## Arch-Magistor Modrfrost

Setup command: `Set up for ArchMagistor`

### Overview

A complex fight with an AE timer, item-based cures for arcane and elemental detriments, and dual curse tracking.

### What the Module Does

**AE Timer:**

- Cyclonic Freeze (knockback) — 27-second HUD countdown

**Arcane Cure (Ghastly Pallor):**

- Detects the afflicted player and targets them
- Automatically uses the "Echo Fragment" inventory item to cure the arcane detriment
- Dual HUD tracking for up to two simultaneous afflictions

**Elemental Cure (Everlasting Fire):**

- Detects the afflicted player and targets them
- Automatically uses the "Elemental Shard of Frost" inventory item to cure the elemental detriment
- Dual HUD tracking for up to two simultaneous afflictions

**Dual Curse Tracking:**

- Lethal Proximity — triggers cure curse with cleric priority
- Magistor's Scourge — triggers cure curse with cleric priority
- Each curse has dual HUD tracking (up to two cursed players each)

### Player Notes

- Requires "Echo Fragment" and "Elemental Shard of Frost" inventory items
- Uses 9 simultaneous HUD timer slots
