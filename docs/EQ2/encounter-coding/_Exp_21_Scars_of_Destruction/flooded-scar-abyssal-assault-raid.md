# Flooded Scar: Abyssal Assault [Raid]

**Expansion:** Scars of Destruction (Exp 21)

> **:warning: Work In Progress**
>
> This zone's automation is still under development. Some mechanics may not be fully automated yet.

This raid zone contains 1 boss encounter.

## Available Setups

| Boss | Description |
|------|-------------|
| [Zeraloth the Unfathomable](#zeraloth-the-unfathomable) | Complex curse management and archetype-specific interrupts (WIP) |

---

## Zeraloth the Unfathomable

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A complex encounter with multiple interacting curse mechanics that require careful cure management, plus archetype-specific interrupt assignments on arm adds.

### What the Module Does

**Curse of Cure Curse:**

- Detects the "Curse of Cure Curse" detriment on the player
- This curse disables the player's cure curse ability
- The module waits until the curse timer reaches approximately 10 seconds remaining before allowing cure
- If the player also has Venomous Arm, cure is allowed immediately instead of waiting

**Venomous Arm:**

- Detects Venomous Arm on the player
- This curse should be cured as soon as possible
- The module enables cure curse immediately when this detriment is detected

**Perils of Pruul:**

- Detects Perils of Pruul on the player
- This curse should only be cured if the player is the only cursed person in their group
- The module checks all other group members for "Curse of Cure Curse" before allowing the cure
- If other group members have Curse of Cure Curse, the cure is held until they are clear

**Ravenous Hunger (Archetype Interrupts):**

- When Ravenous Hunger activates, archetype-specific arms spawn that need to be interrupted:
    - Scouts target Arm of Senzu
    - Priests target Arm of Pruul
    - Mages target Arm of Mozal
    - Fighters target Arm of Fydoon
- Each archetype auto-targets their assigned arm for interrupts

**Setup:**

- Interrupts are disabled during the initial setup phase (re-enabled after)

### Player Notes

- The curse interaction system is complex -- Curse of Cure Curse, Venomous Arm, and Perils of Pruul all interact with each other
- Make sure you know which arm your archetype is assigned to for interrupts
- The module handles the timing of cures automatically, but understanding the mechanics helps if something goes wrong
