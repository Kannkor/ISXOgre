# Precipice of Power [Raid]

**Expansion:** Altar of Malice (Exp 11)

This zone has 3 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Dread Armoloch of Corruption](#dread-armoloch-of-corruption) | AE timer with dual countdown |
| [The Tribunal](#the-tribunal) | Guilty/innocent auto-positioning, silent executioner targeting |
| [Karana](#karana) | Storm tracking, ball lightning timers, charge detection |

---

## Dread Armoloch of Corruption

Setup is automatic when engaged.

### Overview

A fight with a timed AE ability that requires defensive tracking.

### What the Module Does

**AE Timer:**

- Dual HUD timers showing next AE countdown (35/52 seconds) and "if skipped" timing (70/104 seconds)
- Auto-cancels Tortoise Shell on druids when the AE fires

### Player Notes

- HUD timers help coordinate defensive abilities

---

## The Tribunal

Setup is automatic when engaged.

### Overview

A fight with guilty/innocent verdict mechanics and a silent executioner add.

### What the Module Does

**Verdict Positioning:**

- Monitors for Guilty and Innocent detriments
- Guilty: auto-moves to the East/Red area
- Innocent: auto-moves to the West/Blue area
- HUD shows verdict status with a 30-second countdown

**Silent Executioner:**

- When "You feel something is watching you!" triggers, the affected player jousts out
- Once the Executioner spawns within range, automatically targets it

### Player Notes

- After entering your plea, the module moves you back to the raid spot

---

## Karana

Setup is automatic when engaged.

### Overview

A fight with storm direction tracking, ball lightning adds, and positive/negative charge mechanics.

### What the Module Does

**Storm Direction Tracking:**

- Monitors storm announcements (away from boss vs near boss)
- HUD timer (55 seconds) shows current storm direction and when it changes

**Ball Lightning:**

- On spawn, shows 28-second explosion timer and 110-second respawn timer

**Charge Detection:**

- While adds are alive, scans Karana's effects for charge type
- Positive charge: displayed as INSIDE the triangle
- Negative charge: displayed as OUTSIDE the triangle
- Shows charge status on HUD

### Player Notes

- The triangle position (inside vs outside) is determined by the charge type on the boss
