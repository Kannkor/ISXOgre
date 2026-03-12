# Blackhook Spiral: Spiritual Terror [Raid]

**Expansion:** Scars of Destruction (Exp 21)

> **:warning: Work In Progress**
>
> This zone's automation is still under development. Some mechanics may not be fully automated yet.

This raid zone contains 2 boss encounters.

## Available Setups

| Boss | Description |
|------|-------------|
| [Xychintus the Voidcaller](#xychintus-the-voidcaller) | Complex curse and jousting management (WIP) |
| [Vul Lord Tarinax](#vul-lord-tarinax) | Joust-then-cure for Endless Suffering |

---

## Xychintus the Voidcaller

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A complex encounter with archetype-specific curse variants, jousting mechanics, and coordinated cure management between scouts and priests.

### What the Module Does

**Curse Management:**

- Detects three different curse variants depending on archetype (Coercer, Scout/Fighter, and Priest each get a different version)
- Handles cure coordination between scouts and priests -- scouts report that they need a cure, and priests with cure curse available respond

**Jousting:**

- Crushing Darkness: 30-second timed joust mechanic
- Void Banishment: 60-second timed joust mechanic
- Scouts have a dedicated safe spot and a close spot for jousting

**Ability Management:**

- Disables Hadooken ability
- Disables vampiric items
- Enables MaxHealing tag for healing optimization
- Disables cure curse for priests (handled via the coordination system)
- Disables various offensive abilities during curse phases

**Add Targeting:**

- Auto-targets Void-Soaked Entity adds

### Player Notes

- This module is a work in progress and described as challenging
- Cure coordination is complex -- scouts request cures, and priests respond based on availability
- Multiple jousting timers run simultaneously

---

## Vul Lord Tarinax

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with Endless Suffering that requires a joust-then-cure pattern. The module handles the joust and cure automatically.

### What the Module Does

**Endless Suffering (Joust-Then-Cure):**

- Detects Endless Suffering detriment on the player
- Automatically jousts away from the named to a safe position
- Once at a safe distance, requests a cure
- Uses a 22-second timeout for the mechanic

**Positioning:**

- Places the group at designated tank and raid spots

### Player Notes

- Deteriorate Armor (tank swap) is noted in the code but not yet automated
- The joust-then-cure mechanic requires staying at the safe position until cured
