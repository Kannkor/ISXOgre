# Elements of War [Heroic]

**Expansion:** Destiny of Velious (Exp 07)

This zone has 2 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Bloodclaw](#bloodclaw) | Dynamic repositioning on wind crystal / steam rift spawns |
| [Bonewing](#bonewing) | Role-based positioning |

---

## Bloodclaw

Setup command: `Set up for Bloodclaw`

### Overview

A fight with dynamic repositioning based on hazard spawns.

### What the Module Does

**Dynamic Repositioning:**

- When wind crystals or steam rifts spawn, calculates a safe position relative to the hazard
- Adjusts camp spot based on which side of the room the player is on
- Moves players away from the spawned hazard with directional offsets

### Player Notes

- Positions adjust automatically based on hazard locations

---

## Bonewing

Setup command: `Set up for Bonewing`

### Overview

A fight with role-based positioning.

### What the Module Does

**Role-Based Positioning:**

- Fighters stay in place
- Priests are sorted and assigned to top or bottom spots
- Sorcerers, Predators, Rogues, and Summoners go to the top spot
- Everyone else goes to the middle spot

### Player Notes

- Positions differ by class role
