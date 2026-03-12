# Tomb of the Mad Crusader [Raid]

**Expansion:** The Shadow Odyssey (Exp 05)

This zone has 3 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Thet-em-aua](#thet-em-aua) | Selective curse curing |
| [Xebnok the Wretched](#xebnok-the-wretched) | Raid-wide item-based arcane curing |
| [Gynok Moltor](#gynok-moltor) | Purple vision joust to named with self-targeting |

---

## Thet-em-aua

Setup command: `Set up for Thet-em-aua`

### Overview

A fight with two different curses where only one should be cured.

### What the Module Does

**Selective Curse Curing:**

- When "Curse of the Thet" is detected, sends a cross-session command requesting all healers cure this character
- Does NOT cure "Mark of the Serpent" (a different curse that should be left alone)

### Player Notes

- Unlike similar mechanics in other zones, offensive abilities are NOT paused during the curse

---

## Xebnok the Wretched

Setup command: `Set up for Xebnok the Wretched`

### Overview

A fight where raid members get uncurable arcane debuffs that must be cleared using an item.

### What the Module Does

**Raid-Wide Item Curing:**

- Scans all 24 raid members for uncurable arcane debuffs
- If a debuffed member is found and the character has "pungent salts" ready, targets that member and uses the item on them

### Player Notes

- Requires "pungent salts" inventory item
- Any class with the item can perform the cure

---

## Gynok Moltor

Setup command: `Set up for Gynok Moltor`

### Overview

A fight with a purple vision curse that requires running to the named mob before it expires.

### What the Module Does

**Purple Vision Joust:**

- When the "Mark of the Gnollslayer" curse has less than 7 seconds remaining, jousts out and repositions to Gynok Moltor's location
- Disables offensive abilities and forces self-targeting to avoid reflect damage
- Re-enables offensive and clears positioning when the curse expires

### Player Notes

- Joust triggers near the end of the curse duration, not on application
