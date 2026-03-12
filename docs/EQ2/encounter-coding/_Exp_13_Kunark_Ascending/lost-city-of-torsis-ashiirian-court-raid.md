# Lost City of Torsis: Ashiirian Court [Raid]

**Expansion:** Kunark Ascending (Exp 13)

This zone has 3 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [A Black Reaver](#a-black-reaver) | Uncurable debuff joust |
| [A Gyrating Green Slime](#a-gyrating-green-slime) | Spray gunk distance-based joust |
| [Lord Rak'Ashiir](#lord-rakashiir) | Tank swap, auto-run to music boxes |

---

## A Black Reaver

Setup command: `Set up for Reaver`

### Overview

A fight with an uncurable debuff that requires jousting away from the boss.

### What the Module Does

**Black Heart Joust:**

- Monitors for the uncurable "Black Heart" debuff
- When detected, moves the character to the joust spot (away from the Reaver)
- When the debuff drops, returns to the raid position
- Automatically detects which of the two Reaver spawn locations is active and uses the correct raid/joust spots

### Player Notes

- The Reaver spawns at two different locations in the zone -- the module auto-detects which one based on proximity

---

## A Gyrating Green Slime

Setup command: `Set up for Gyrating`

### Overview

A fight where the group jousts between two positions to avoid the slime's spray gunk attack.

### What the Module Does

**Spray Gunk Joust:**

- When the slime prepares to spray gunk, compares the distances between the two camp positions and the slime's current location
- Moves the entire group to whichever position is farther from the slime
- Fighters have separate tank spots at each position

### Player Notes

- Fighters and non-fighters each have their own positions at both camp locations

---

## Lord Rak'Ashiir

Setup command: `Set up for Lord`

Additional options:

- `Set up for Lord all` -- makes ALL groups (including tank groups) run to music boxes
- `Set up for Lord dps` -- only non-tank groups run to music boxes (default behavior)

### Overview

A complex fight with a death touch tank swap mechanic and music box adds that the raid must run to.

### What the Module Does

**Tank Swap (Death Touch):**

- When Lord Rak'Ashiir targets a player for his death touch, a 60-second HUD countdown is displayed
- If your character is the target: stops all offensive actions, casts threat-shedding abilities, then resumes attacking after 60 seconds
- If your character is not the target: shows a message to get aggro

**Music Box Auto-Run:**

- When a Torsis Music Box spawns, the module determines which of the 4 known positions it appeared at
- By default, only non-tank groups move to the music box location
- With the `all` option, all groups including tanks move to the music box
- A waypoint is set on screen for the music box location
- Shows a HUD timer for the next expected music box spawn (45 seconds)
- When the music box despawns, everyone returns to the raid position

### Player Notes

- Use `Set up for Lord all` if you want tank groups to also run to music boxes
- The default behavior keeps tank groups stationary while DPS/healer groups move
