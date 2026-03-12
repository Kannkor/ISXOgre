# Wracklands: Diaku Corral [Solo]

**Expansion:** Blood of Luclin (Exp 16)

This solo zone contains 5 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Brutto Ucot](#brutto-ucot) | Crate lid pickup and drop mechanic |
| [The Invisible Swordsman](#the-invisible-swordsman) | 100% AFK circle-chasing mechanic |
| [Elga Upo](#elga-upo) | Animal identification from dialogue clues |
| [Morna Joro](#morna-joro) | Auto-clicking Mech Bull |
| [Vleecan Fele](#vleecan-fele) | Add identification from dialogue clues |

---

## Brutto Ucot

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A crate lid mechanic where a movable crate lid must be picked up, carried to an open crate, and dropped in. The module uses first-person view and mouse automation to handle the interaction.

### What the Module Does

**Crate Lid Mechanic (if marked):**

- Picks up the movable crate lid
- Carries it to the open crate
- Drops the lid into the crate using first-person view and mouse automation

### Player Notes

- This mechanic only activates if the character is **marked** for it.
- The module switches to first-person view to handle the mouse-driven pickup and drop.

---

## The Invisible Swordsman

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fully automated encounter where circles spawn on the ground and the group must find the invisible swordsman by moving to circle locations and rotating through angles. This fight can be completed 100% AFK.

### What the Module Does

**Circle Detection and Positioning:**

- Detects when circles spawn on the ground
- Automatically positions the group at the nearest circle location
- Rotates through different angles at each circle to find the invisible swordsman
- Continuously repositions as circles move to new locations

### Player Notes

- This fight is **100% AFK**. No manual input is needed.
- The module handles all movement and targeting automatically.

---

## Elga Upo

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A puzzle encounter where dialogue clues indicate which animal pinata to kill. The module identifies the correct animal from the clues and displays a HUD message.

### What the Module Does

**Animal Identification:**

- Reads dialogue clues during the encounter and identifies the correct animal:

| Clue | Animal |
|------|--------|
| "Ever see one fly?" | Pegasus |
| "ain't got no wings" | Lion |
| "beat no hare in a race" | Turtle |
| "Hungry like a..." | Wolf |
| "give me the creeps" | Spider |
| "Quit yer badgerin'" | Badger |
| "comin' up through the sand" | Crab |
| "Hop to it!" | Rabbit |
| "Hey Honey!" | Bear |

- Displays a HUD showing which animal to kill

**Auto-Targeting (if marked):**

- If the character is marked, automatically ports to and targets the correct animal pinata

### Player Notes

- Watch the HUD to see which animal to kill.
- If marked, the module handles movement and targeting automatically.
- If not marked, use the HUD information to manually find and kill the correct animal.

---

## Morna Joro

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A Mech Bull encounter where bull icons and clickable objects spawn during the fight. The module automatically clicks on the closed mech bull clickies.

### What the Module Does

**Mech Bull Auto-Clicking:**

- Detects when mech bull icons and clickable objects spawn
- Automatically clicks on the closed mech bull clickies

### Player Notes

- The clicking is handled automatically, but you still need to **manually get ON the bull**.
- The module only handles clicking the closed bull clickies, not mounting.

---

## Vleecan Fele

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A puzzle encounter where dialogue clues indicate which add type to kill. The module identifies the correct add from the clues and displays a HUD message.

### What the Module Does

**Add Identification:**

- Reads dialogue clues during the encounter and identifies the correct add to kill:

| Clue | Add to Kill |
|------|------------|
| "more 'an heal" | a Diakaroo sawbones |
| "you backstabbers" | a Diakaroo desperado |
| "fire and ice" | a Diakaroo regulator |
| "Hit me!" | a Diakaroo bulldozer |

- Displays a HUD showing which add to kill

**Auto-Targeting (if marked):**

- If the character is marked, automatically moves to and targets the correct add
- When the add dies, the module returns to the named

### Player Notes

- Watch the HUD to see which add to kill.
- If marked, the module handles movement and targeting automatically, then returns to the named when the add is dead.
- If not marked, use the HUD information to manually find and kill the correct add.
