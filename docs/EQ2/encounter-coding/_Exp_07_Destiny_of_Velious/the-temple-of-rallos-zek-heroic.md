# The Temple of Rallos Zek [Heroic]

**Expansion:** Destiny of Velious (Exp 07)

This zone has 2 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Rallos Zek Prime](#rallos-zek-prime) | Dot-duration-based joust timing |
| [Idol of Rallos Zek](#idol-of-rallos-zek) | Role-based positioning with rubble avoidance |

---

## Rallos Zek Prime

Setup command: `Set up for Prime`

### Overview

A fight where the joust timing is calculated from the Mark of Discontinuance dot duration.

### What the Module Does

**Mark of Discontinuance Joust:**

- When the mark is applied to the player, calculates a delay based on the dot's remaining duration
- Moves to the joust spot before the dot expires
- Returns to camp 3 seconds after the dot ends

### Player Notes

- Joust timing is dynamically calculated from the detriment duration

---

## Idol of Rallos Zek

Setup command: `Set up for Idol`

### Overview

A fight with role-based positioning and dynamic rubble avoidance.

### What the Module Does

**Role-Based Positioning:**

- Separate positions for tanks, priests (sorted by priority), mages, and melee
- Each role has two possible spots

**Rubble Avoidance:**

- When Crushing Rubble spawns within 13 meters of the current camp spot, moves to the alternate spot for that role
- Determines which of the two spots is farther from the rubble

### Player Notes

- Positions shift automatically when rubble spawns nearby
