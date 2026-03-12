# Crypt of Dalnir: Ritual Chamber [Heroic]

**Expansion:** Kunark Ascending (Exp 13)

This zone has 3 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Rector Droz'Kzar](#rector-drozkzar) | Totem spawn jousting between two positions |
| [Izzak Sira](#izzak-sira) | Circle positioning by room, death orb color order display |
| [The Kly](#the-kly) | Orb color detection, bard/enchanter auto-clicking |

---

## Rector Droz'Kzar

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with totem jousting between two positions.

### What the Module Does

**Totem Jousting:**

- When a totem spawns within 35 meters, determines which of two group spots it is closest to
- Moves the group to the opposite spot (away from the totem)

### Player Notes

- Distant totems (beyond 35 meters) are ignored

---

## Izzak Sira

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with room-based circle positioning and death orb color order detection.

### What the Module Does

**Circle Positioning:**

- Each player is assigned to one of 6 circle positions in the nearest room
- The script detects which room the group is closest to and assigns circles based on player sort order
- Players move to their assigned circles with staggered timing

**Death Orb Color Order:**

- When Izzak Sira dies, the script reads the colors of rune actors at specific locations
- Displays the orb clicking order to the group

### Player Notes

- The circle assignment is based on which room the group is nearest to when setup runs

---

## The Kly

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with power orb color detection and automated orb clicking.

### What the Module Does

**Orb Color Detection:**

- When the boss draws power from orbs, reads the overlay of the power source actors to determine the West and East orb colors
- Polls up to 10 times (1 second apart) until colors resolve
- Displays both orb colors on the HUD

**Automated Orb Clicking:**

- The Bard automatically handles the West orb: navigates through waypoints to the matching colored orb, clicks the Power Switch, and returns
- The Enchanter automatically handles the East orb using the same approach

### Player Notes

- Make sure your EQ2 rendering distance is set to 410 or higher (required to see orb actors at distance)
- Bards handle the West orb, Enchanters handle the East orb
