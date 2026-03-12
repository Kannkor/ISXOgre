# Doomfire: The Broken Throne [Raid]

**Expansion:** Chaos Descending (Exp 15)

This zone has 1 boss encounter with an OgreBot automation module.

## Available Setups

| Boss | Description |
|------|-------------|
| [Fennin Ro](#fennin-ro) | Fully automated 3-stage fire grid positioning (Gust/Fan/Pull) |

---

## Fennin Ro

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight on a fire grid where the raid must continuously reposition based on environmental stage detection.

### What the Module Does

**3-Stage Fire Grid Positioning:**

The module continuously monitors invisible environmental actors (walls, claws, fans) on the fire grid to determine the current stage:

- **GUST Stage:** Moves all characters to the safe center location
- **FAN Stage:** Detects which quadrant (NE/SE/SW/NW) Xegony is closest to and moves the raid to that kill spot
- **PULL Stage:** Detects which wall is down and moves the raid to the corresponding quadrant's kill spot

**Environmental Actor Tracking:**

- Queries wall, claw, and fan objects at known positions and reads their Y-axis to determine stage state
- Actor IDs are cached and refreshed automatically if validation fails

### Player Notes

- Get everyone onto the grid, then on ONE person type: `ogre cd_fenninro`
- The module uses cross-session commands to move the entire raid
- Positioning updates only fire when movement of more than 1 meter is needed
