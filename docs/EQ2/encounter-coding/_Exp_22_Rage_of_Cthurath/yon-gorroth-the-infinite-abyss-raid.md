# Yon Gorroth: The Infinite Abyss [Raid]

**Expansion:** Rage of Cthurath (Exp 22)

This zone has 1 boss encounter with an OgreBot automation module.

## Available Setups

| Boss | Setup Name | Description |
|------|-----------|-------------|
| [Dondari, Darou Archmage](#dondari-darou-archmage) | Dondari, Darou Archmage | Handles curse and aggro |

---

## Dondari, Darou Archmage

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A raid encounter with timed curse curing, aggro management, and proximity-based jousting. The module handles all three major mechanics automatically.

### Requirements

- **Fighter** in raid groups 1 or 2 (designated tank, placed at tank spot)
- **Priest** (curse cure for Forced Procrastination)

### What the Module Does

**Forced Procrastination Curse:**

- A 60-second curse that wounds health/power
- The module waits until the curse has 1-10 seconds remaining, then requests a curse cure
- Curing early heals the boss more (the heal is based on remaining duration), so delayed curing is critical
- Priest curse cures are disabled to prevent premature curing

**Spotted Weakness Aggro Management:**

- When a player gets Spotted Weakness, the module immediately:
    - Stops all offensive actions
    - Casts Subtle Strikes (stealth)
    - Adds the player to the fighter threat ignore list
- When the detriment clears, offensive actions resume and the ignore list is cleared
- Being targeted again while already having Spotted Weakness kills the group
- Announcements are posted to IRC

**Repair Robes Jousting:**

- NPC cast monitoring detects when the boss casts Maelstrom of Ice
- A 50-second on-screen countdown timer is displayed for the next Repair Robes
- 5 seconds before Repair Robes is expected, non-fighters move to a joust spot (Repair Robes deals more damage the closer you are)
- Once the detriment clears, the group returns to normal positions

**Add-Based Repositioning:**

- When "Archmage's Chosen" (the add) spawns, fighters position in front and non-fighters behind
- When the add despawns, the group repositions relative to the boss

**Tank Setup:**

- Fighters in raid groups 1 or 2 are flagged as tanks and given a separate tank camp spot

### Player Notes

- On-screen timer shows countdown to next Repair Robes cast.
- IRC announcements are posted for Spotted Weakness and curse cure requests.
- Non-fighters automatically joust away before Repair Robes hits and return after it clears.
- The module respects raid group assignment to determine which fighters are designated tanks.
