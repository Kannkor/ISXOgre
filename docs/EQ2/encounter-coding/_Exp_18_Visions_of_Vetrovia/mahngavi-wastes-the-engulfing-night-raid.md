# Mahngavi Wastes: The Engulfing Night [Raid]

**Expansion:** Visions of Vetrovia (Exp 18)

This zone has 3 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Persepherator](#persepherator) | Enables cures and Absorb Magic for coordinated curse curing |
| [Cewtie Irewater](#cewtie-irewater) | Cascading damage jousting with timed repositioning |
| [Cewtie?](#cewtie) | Cascading damage jousting with archetype-based return positions |

---

## Persepherator

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with 4 curses going out at HP thresholds (95/65/40/15%), requiring fast coordinated curing.

### What the Module Does

**Cure Setup:**

- Enables cure and cure curse cast stacks
- Turns on Absorb Magic for the fight

### Player Notes

- Curses go out at specific HP thresholds and must be cured quickly
- The module sets up the curing framework; players handle the execution

---

## Cewtie Irewater

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a cascading damage mechanic that requires timed two-phase movement.

### What the Module Does

**Cascading Damage Joust:**

- When cascading damage begins, the module executes a two-phase timed movement:
    - Phase 1 (3 seconds): Moves everyone to an intermediate safe spot
    - Phase 2 (8 seconds): Moves back to fight positions with fighters at the tank spot and non-fighters at the raid spot

### Player Notes

- The two-phase joust is fully automated with timed transitions

---

## Cewtie?

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A variant of the Cewtie fight with archetype-based return positioning after the cascading damage joust.

### What the Module Does

**Cascading Damage Joust:**

- Same two-phase timed movement as Cewtie Irewater
- On the return phase, mages and non-mages go to different positions instead of the standard fighter/non-fighter split

### Player Notes

- The return positioning differs from Cewtie Irewater based on archetype (mage vs non-mage)
