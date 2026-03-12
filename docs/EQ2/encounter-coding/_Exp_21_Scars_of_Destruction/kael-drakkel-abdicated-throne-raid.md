# Kael Drakkel: Abdicated Throne [Raid]

**Expansion:** Scars of Destruction (Exp 21)

> **:warning: Work In Progress**
>
> This zone's automation is still under development. Some mechanics may not be fully automated yet.

This raid zone contains 1 boss encounter.

## Available Setups

| Boss | Description |
|------|-------------|
| [Frostking Jund'Erin](#frostking-junderin) | Crystal clicking coordination (WIP) |

---

## Frostking Jund'Erin

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight centered around Crystallizing Compression curses that require clicking specific crystals to remove. The module coordinates crystal assignment across the raid. This encounter also appears in Western Wastes: Exploration Determination [Raid] with the same mechanics.

### What the Module Does

**Crystallizing Compression:**

- Detects the Crystallizing Compression curse on the player
- Coordinates crystal assignment across the raid using a button system
- Each player is assigned a crystal index based on a sorted list
- Players move to their assigned crystal and click it to remove the curse
- A random crystal fallback is used if the indexed assignment fails

**Crystal Button:**

- Use `Obj_OgreMCP:PasteButton[OgreConsoleCommand,Jund,-ExecuteEvent_AP,auto,Jund_AtCrystal]` to signal you are at your crystal

**Protection Phase:**

- When the boss "prepares to protect himself," the module stops all offensive actions for a configurable duration (default 15 seconds)
- DPS is automatically resumed after the protection phase ends

**Ability Management:**

- Defiler's Defile ability is disabled during the fight
- Fighter dethreat is managed during Crystallizing Compression

### Player Notes

- Crystal assignment is coordinated automatically -- follow the module's positioning
- Stop DPS during the protection phase (automated)
- The crystal button can be used to signal you are at your assigned crystal for coordination
