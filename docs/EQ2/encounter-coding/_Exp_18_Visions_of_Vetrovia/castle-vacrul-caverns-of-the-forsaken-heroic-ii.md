# Castle Vacrul: Caverns of the Forsaken [Heroic II]

**Expansion:** Visions of Vetrovia (Exp 18)

This zone has 1 boss encounter with an OgreBot automation module.

## Available Setups

| Boss | Description |
|------|-------------|
| [Sypheria the Shackled](#sypheria-the-shackled) | Coordinated Balanced Synergy dispel with trauma checking (WIP) |

---

## Sypheria the Shackled

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

!!! warning "Work in Progress"
    This encounter's automation is still under development.

### Overview

A fight centered around coordinated dispelling using Balanced Synergy, with precise timing windows.

### What the Module Does

**Bloodlinked Chains Dispel:**

- Balanced Synergy and Absorb Magic are disabled on setup to prevent premature firing
- Fighters monitor the boss for Bloodlinked Chains and queue Balanced Synergy casting at specific HP thresholds (26-35% and 11-20%)
- The module tracks how many group members have Balanced Synergy active
- Once all members have it up, a timed dispel window is calculated and characters use their dispel abilities on the boss
- Trauma is checked before dispelling -- if any group member has trauma, dispelling is skipped

### Player Notes

- Balanced Synergy timing is fully coordinated across the group
- The module calculates safe dispel windows automatically
- Trauma prevents dispelling -- the module checks this before acting
