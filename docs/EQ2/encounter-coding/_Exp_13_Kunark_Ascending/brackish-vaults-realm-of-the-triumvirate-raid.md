# Brackish Vaults: Realm of the Triumvirate [Raid]

**Expansion:** Kunark Ascending (Exp 13)

!!! warning "Work in Progress"
    This module is still under development. Some encounters may have partial or missing automation.

This zone has 1 boss encounter with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Eurold, Harbinger of Povar](#eurold-harbinger-of-povar) | Curse detection with distributed priest curing |

---

## Eurold, Harbinger of Povar

Setup command: `Set up for Eurold curse`

### Overview

A fight with a curable curse that is detected and distributed among priests for curing.

### What the Module Does

**Curse Detection:**

- Monitors for the curable "Through the Mist" debuff
- When detected, broadcasts a raid-wide setup command to all sessions via IRC

**Distributed Priest Curing:**

- When the cure command fires, each priest is assigned a cursed raid member based on their position in the priest sort order
- The Nth priest cures the Nth cursed person, distributing the cure load evenly
- Priests who are cursed themselves cure themselves first
- Has a 20-second cooldown to prevent command spam

### Player Notes

- The IRC relay system must be active for the cross-session cure broadcast to work
- Only priests perform the actual curing
