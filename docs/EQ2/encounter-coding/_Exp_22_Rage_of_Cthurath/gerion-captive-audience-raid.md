# Gerion: Captive Audience [Raid]

**Expansion:** Rage of Cthurath (Exp 22)

> **:warning: Work In Progress**
>
> This zone's automation is still under development. Some mechanics may not be fully automated yet.

## Available Setups

| Boss | Setup Name | Description |
|------|-----------|-------------|
| [Benelith, Consumed Heart](#benelith-consumed-heart) | Benelith, Consumed Heart | Handles curse and aggro management (WIP) |

---

## Benelith, Consumed Heart

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A complex encounter where the boss places "Consume Will" curses on players, requiring them to travel to specific crystals (East, West, or Center) to remove the curse. The module handles curse detection, aggro management during the curse, and crystal clicking.

### Requirements

- **Guardian** recommended (uses Recapture to help shed aggro during curse phases)

### What the Module Does

**Consume Will Curse Handling:**

- Detects which variant of Consume Will the player has (East, West, or Center)
- Automatically moves the player to the correct crystal location
- Double-clicks the crystal to remove the curse
- Announces the direction to the group and IRC

**Aggro Management During Curse:**

- If the cursed player currently holds aggro on the boss, the module waits for aggro to drop before moving
- Enables Subtle Strikes to reduce threat
- Tells fighters to ignore the cursed player on the threat list
- Guardians cast Recapture to help shed aggro
- Auto-targeting is temporarily disabled while handling the curse

**On-Screen Timer:**

- Broadcasts a 90-second countdown timer for Consume Will across the group

### Player Notes

- The "Consume" effects (Minds, Spirits, Power) that require moving the boss into colored bubbles are not yet fully automated.
- This module is a work in progress.
