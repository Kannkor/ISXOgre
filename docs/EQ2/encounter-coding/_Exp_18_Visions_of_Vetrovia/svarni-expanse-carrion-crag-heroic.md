# Svarni Expanse: Carrion Crag [Heroic]

**Expansion:** Visions of Vetrovia (Exp 18)

This zone has 1 boss encounter with an OgreBot automation module.

## Available Setups

| Boss | Description |
|------|-------------|
| [High Shikari Olyxa](#high-shikari-olyxa) | Positional jousting based on attack direction (WIP) |

---

## High Shikari Olyxa

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

!!! warning "Work in Progress"
    This encounter's automation is still under development.

### Overview

A fight where the boss hides in darkness and attacks from different directions, requiring the group to reposition to the correct safe spot.

### What the Module Does

**Directional Jousting:**

- When Olyxa takes cover in the darkness, the group moves to the centre of the bridge
- When she attacks from a specific direction (bridge, east, or west side), the group relocates to the corresponding safe spot
- Three hardcoded positions are used for east, centre, and west

**Shield Actor Tracking:**

- When an unnamed actor spawns with a shield visual overlay, the group camp spot is moved to that actor's location, indicating where Olyxa has revealed herself

### Player Notes

- Movement is automated based on the boss's attack direction
- Three positions on the bridge are used depending on where Olyxa attacks from
