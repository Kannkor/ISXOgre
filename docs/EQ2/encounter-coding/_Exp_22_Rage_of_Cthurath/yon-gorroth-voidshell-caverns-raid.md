# Yon Gorroth: Voidshell Caverns [Raid]

**Expansion:** Rage of Cthurath (Exp 22)

> **:warning: Work In Progress**
>
> This zone's automation is still under development.

## Available Setups

| Boss | Setup Name | Description |
|------|-----------|-------------|
| [Kantankerus Voidshell](#kantankerus-voidshell) | Kantankerus Voidshell | WIP |

---

## Kantankerus Voidshell

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A raid encounter where Spotted Weakness must be carefully managed to prevent group wipes.

### Requirements

- **Fighter** (force-targets disabled during the fight)

### What the Module Does

**Setup:**

- Disables fighter force-targets
- Jousts all toons out

**Spotted Weakness Handling:**

- When a player gets Spotted Weakness, the module immediately:
    - Announces it via IRC
    - Activates Subtle Strikes to reduce threat
    - Stops all offensive actions
    - Tells fighters in the raid to ignore the affected player on the threat list
- When the detriment clears:
    - Subtle Strikes is canceled
    - Offensive actions resume
    - The threat ignore list is cleared
    - An IRC announcement confirms the detriment has dropped

**Cleanup on Kill:**

- Subtle Strikes is canceled
- Offensive actions resume
- Fighter threat ignore list is cleared
- Fighter force-targets are re-enabled

### Player Notes

- This module is a work in progress -- additional mechanics may not yet be automated.
- The boss will kill anyone's group who already has Spotted Weakness if targeted again, making this mechanic critical.
