# Dragon Necropolis: Chetari Warrens [Heroic II]

**Expansion:** Scars of Destruction (Exp 21)

> **:warning: Work In Progress**
>
> This zone's automation is still under development. Some mechanics may not be fully automated yet.

This Heroic II zone contains 1 boss encounter with a unique dragon transformation mechanic.

## Available Setups

| Boss | Description |
|------|-------------|
| [Jaled Dar](#jaled-dar) | Dragon transformation with auto-ability usage (WIP) |

---

## Jaled Dar

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A unique encounter where players receive "Possess Bones" and are transformed into First Brood dragons. Each dragon type has its own set of abilities that the module casts automatically. The module also monitors for critical abilities that require immediate response.

### What the Module Does

**Dragon Transformation:**

- Detects when the player receives "Possess Bones" and becomes a First Brood dragon
- Automatically identifies which type of dragon the player has become:
    - First Brood Warder
    - First Brood Protector
    - First Brood Vanguard
    - First Brood Sentry
    - First Brood Custodian
    - First Brood Servitor
- Each dragon type has a priority-ordered list of abilities that the module cycles through automatically

**Difficulty-Specific Abilities:**

- The module supports different ability sets for Heroic II, Heroic I, and Solo difficulties

**Critical Ability Monitoring:**

- Monitors for "Deathblaze" being cast
- When Deathblaze is detected, the Sentry dragon type automatically uses "Rebuke Death" to counter it
- The Servitor dragon type uses "Sever Curse" when group members are cursed

**NPC Cast Monitoring:**

- Enables NPC cast monitoring to detect important boss abilities

### Player Notes

- Your abilities change based on which dragon you become -- the module handles casting the correct abilities automatically
- Sentry players are especially important for countering Deathblaze with Rebuke Death
- Servitor players handle curse removal via Sever Curse
