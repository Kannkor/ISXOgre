# Savage Weald: Backwoods Brawl [Challenge]

**Expansion:** Reign of Shadows (Exp 17)

This zone has 2 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [The Grimling Zero](#the-grimling-zero) | Auto-targeting with TintFlag-based add kill order |
| [Herbwitch Eepkie](#herbwitch-eepkie) | Interrupt casting on herb balm search |

---

## The Grimling Zero

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where the boss equips different weapons, determining which of three spawning adds must be killed last.

### What the Module Does

**Add Kill Order:**

- Three "wealdling merc" adds spawn during the fight, identified by their visual appearance (TintFlags)
- The module determines which add type to kill last based on what the boss equips:
    - When the boss equips a sword and shield, dual-wield adds are killed first and the sword-and-shield add is killed last
    - When the boss equips dual swords, sword-and-shield adds are killed first and the dual-wield add is killed last
- The "odd one out" among the three adds becomes the last kill target

**Auto-Targeting:**

- The fighter controlling assist automatically iterates through the kill order, targeting the first living add
- When all adds are dead, targeting returns to the named boss
- Camp spots assign specific positions for healers, enchanter, DPS, and bard

### Player Notes

- Add kill order is determined automatically based on the boss's weapon -- follow the auto-targeting
- The module tracks add spawns and death to maintain the correct kill sequence

---

## Herbwitch Eepkie

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with an interrupt mechanic.

### What the Module Does

**Herb Balm Interrupt:**

- When the boss searches for herb balm, the module immediately casts interrupt abilities (Spellblade's Counter and Hemorrhage) to interrupt the cast

### Player Notes

- The interrupt is handled automatically -- ensure interrupt abilities are available
