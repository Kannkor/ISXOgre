# Castle Highhold: No Quarter [Raid]

**Expansion:** Altar of Malice (Exp 11)

This zone has 3 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Grevog the Punisher](#grevog-the-punisher) | Berserk handling, elemental joust, fighter FD management |
| [Zebrun the Torso](#zebrun-the-torso) | Stack monitoring, 8-stack joust |
| [Grethah the Frenzied](#grethah-the-frenzied) | Cocoon joust, AE toggling, add management timers |

---

## Grevog the Punisher

Setup command: `Set up for Grevog`

### Overview

A fight with berserk phases and an elemental pool joust mechanic.

### What the Module Does

**Berserk Handling:**

- When Grevog goes berserk, fighters use Subtle Strikes to stop generating hate (or disable offensive actions if unavailable)
- Enchanters cast Sever Hate on the current tank target
- When berserk ends, fighters stand up and resume offensive actions

**Elemental Joust:**

- When elemental resistance drops, triggers a callout and moves to a joust spot
- Automatically jumps into the pool at a specific waypoint, then jumps back out and returns to position

### Player Notes

- Tank spot is included in the setup
- Sever Hate is automatically disabled from cast stack during setup

---

## Zebrun the Torso

Setup command: `Set up for Torso` (also accepts `Set up for Zebrun`)

### Overview

A fight where the raid must joust when the boss reaches 8 stacks of a buff.

### What the Module Does

**Stack Monitoring:**

- Continuously scans the boss for buff stacks
- When stacks reach 8, automatically moves everyone to the opposite position (100 meters away)
- Bards auto-cast Quick Tempo during the move
- Two position sets are used for the back-and-forth joust

### Player Notes

- Tank spot is included in the setup
- An alternate "no move" burn strategy is available

---

## Grethah the Frenzied

Setup command: `Set up for Grethah`

### Overview

A fight with swarmling adds, cocoon jousting, and dynamic AE ability toggling.

### What the Module Does

**AE Toggle System:**

- Dynamically enables/disables AE abilities, encounter nukes, named combat arts, and Temporal Mimicry based on whether swarmling adds are alive
- When adds spawn, enables AE abilities; when all adds die, disables them again

**Add Timer:**

- HUD shows a 35-second countdown for how long adds must be killed within

**Cocoon Joust:**

- When a cocoon spawns, shows a 37-second HUD countdown
- Automatically swaps between two position sets, moving to whichever is farther from the current location

### Player Notes

- AEs, encounter nukes, named combat arts, and Temporal Mimicry are all disabled during initial setup
