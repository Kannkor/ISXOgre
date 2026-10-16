# Wracklands: Diaku Corral [Solo]

**Expansion:** Blood of Luclin (Exp 16)

This solo zone contains 3 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Elga Upo](#elga-upo) | Animal identification from dialogue clues |
| [Morna Joro](#morna-joro) | Auto-clicking Mech Bull |
| [Vleecan Fele](#vleecan-fele) | Add identification from dialogue clues |

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

### Player Notes

- Watch the HUD to see which animal to kill.
- Use the HUD information to find and kill the correct animal.

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

### Player Notes

- Watch the HUD to see which add to kill.
- Use the HUD information to find and kill the correct add.
