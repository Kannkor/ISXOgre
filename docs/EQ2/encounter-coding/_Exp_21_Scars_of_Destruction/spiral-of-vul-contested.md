# Spiral of Vul [Contested]

**Expansion:** Scars of Destruction (Exp 21)

> **:warning: Contested Zone**
>
> This is a CONTESTED zone. These setups are coded for players who are massively overgeared and can burn each named in under a minute.

This contested zone contains 7 boss encounters with simplified automation designed for quick burns.

## Available Setups

| Boss | Description |
|------|-------------|
| [Vyrakaz](#vyrakaz) | Enchanter will automatically dispell |
| [Tembrusk](#tembrusk) | Disables cures and curses |
| [Pruug the Pitiless](#pruug-the-pitiless) | Disables interrupts then re-enables them after |
| [Oggorn Leg-shorn](#oggorn-leg-shorn) | Enables dispells then disables them after |
| [Greshlokk the Gluttonous](#greshlokk-the-gluttonous) | Disables cures and curses. Must have high DPS to ignore the script |
| [Crabicus Crunch](#crabicus-crunch) | Disables cures and curses. Must have high DPS to ignore the script |
| [The Runic Ruins](#the-runic-ruins) | Disables combat arts and runs external script |

---

## Vyrakaz

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where the enchanter handles dispelling the named. The module positions the group and manages the enchanter's dispell movement.

### What the Module Does

- Places the group at the raid position
- Disables dispells for non-enchanters
- Enchanter automatically moves to the dispell position, dispells the named, and returns
- Enchanter jumps if needed to reach the dispell target

### Player Notes

- Requires an enchanter in the group for the dispell mechanic
- Burn the named quickly

---

## Tembrusk

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A simple fight where cures and curses need to be disabled to avoid triggering harmful mechanics.

### What the Module Does

- Disables priest cure curse
- Disables all cure abilities
- Re-enables both after the named is killed

### Player Notes

- Must have high DPS to burn the named before the script mechanics become problematic

---

## Pruug the Pitiless

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where interrupts need to be disabled to avoid triggering harmful mechanics.

### What the Module Does

- Disables all interrupts for the fight
- Re-enables interrupts after the named is killed

### Player Notes

- Burn the named quickly while interrupts are disabled

---

## Oggorn Leg-shorn

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where dispells need to be enabled to handle the named's buffs.

### What the Module Does

- Enables dispells for the fight
- Sets up dispell configuration
- Disables dispells after the named is killed

### Player Notes

- Burn the named quickly while dispells handle the buffs

---

## Greshlokk the Gluttonous

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where cures and curses need to be disabled to avoid triggering harmful mechanics.

### What the Module Does

- Disables priest cure curse
- Disables all cure abilities
- Re-enables both after the named is killed

### Player Notes

- Must have high DPS to ignore the script mechanics and burn the named down quickly

---

## Crabicus Crunch

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where cures and curses need to be disabled to avoid triggering harmful mechanics.

### What the Module Does

- Disables priest cure curse
- Disables all cure abilities
- Re-enables both after the named is killed

### Player Notes

- Must have high DPS to ignore the script mechanics and burn the named down quickly

---

## The Runic Ruins

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight that uses an external script for heroic opportunity management and disables combat arts.

### What the Module Does

- Disables combat arts and named combat arts
- Runs an external heroic opportunity script for the fight
- Re-enables combat arts, heroic opportunity abilities, pre-cast, and post-cast after the named is killed

### Player Notes

- Combat arts are disabled during this fight -- the external script handles ability usage
- All disabled settings are restored after the named dies
