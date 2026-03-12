# Lost City of Torsis: The Spectral Market [Heroic]

**Expansion:** Kunark Ascending (Exp 13)

This zone has 2 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [The Torsis Champion](#the-torsis-champion) | Progressive kiting through waypoints on red text |
| [Ongnissim the Unseen](#ongnissim-the-unseen) | Two-position crashing fist joust |

---

## The Torsis Champion

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with progressive kiting through multiple waypoints, including tanks.

### What the Module Does

**Progressive Kiting:**

- When the Champion "eyes" a player (at HP thresholds), the entire group moves through a series of waypoints
- Each trigger advances the group through 3 positions with staggered timing (immediate, then 4 seconds, then 10 seconds)
- The kiting path runs incrementally down a hallway through multiple rooms
- Movement applies to everyone including tanks

### Player Notes

- All players including tanks share the same movement positions

---

## Ongnissim the Unseen

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with jousting between two positions when the boss prepares a crashing fist attack.

### What the Module Does

**Crashing Fist Joust:**

- When the boss prepares to unleash a crashing fist, determines which of two positions the boss is closer to
- Moves the entire group to the opposite position (away from the boss)
- Fighters have separate tank spots corresponding to each position

### Player Notes

- Fighters and non-fighters have separate camp spots at each position
