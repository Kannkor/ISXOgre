# Eryslai: The Aether Vale [Raid]

**Expansion:** Chaos Descending (Exp 15)

This zone has 1 boss encounter with an OgreBot automation module.

## Available Setups

| Boss | Description |
|------|-------------|
| [Xegony](#xegony) | Fully automated 3-phase positioning (Gust/Fan/Pull) via environmental detection |

---

## Xegony

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fully automated fight where positioning is determined by reading environmental objects in real time.

### What the Module Does

**3-Phase Environmental Detection:**

The module continuously monitors walls, claws, and fans by their Y-axis positions to determine the current phase:

- **GUST Phase:** Raid stays in the center at the safe location
- **FAN Phase:** Detects which quadrant (NE/SE/SW/NW) Xegony is closest to and moves the raid to that kill spot
- **PULL Phase:** Detects which wall is down and moves the raid to the corresponding quadrant

**Smart Position Updates:**

- Only changes camp spot when the destination differs by more than 1 meter from current position
- Prevents unnecessary movement commands during phase transitions

### Player Notes

- The fight is completely automated -- positioning adjusts continuously based on the environment
- Supports both Raid and Mythic Raid variants
