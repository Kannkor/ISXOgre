# Brokenskull Bay: Fury of the Cursed [Raid]

**Expansion:** Altar of Malice (Exp 11)

This zone has 2 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Captain Krasnok the Immortal](#captain-krasnok-the-immortal) | Greenmist curse timers, bubble sorting, spirit add tracking |
| [Jessip Daggerheart](#jessip-daggerheart) | Sneak attack auto-movement |

---

## Captain Krasnok the Immortal

Setup command: `Set up for Captain`

### Overview

A complex fight with greenmist curse mechanics, bubble sorting, and spirit add tracking.

### What the Module Does

**Greenmist Curse Tracking:**

- Tracks boss health to calculate and display the next greenmist threshold percentage via HUD timer (95/80/65/50/35/20/5%)

**Bubble Sorting:**

- When 8 greenmist pustules spawn, they are sorted by distance and each raid sub-group is assigned a specific bubble
- Players are staggered with timed delays before moving to their assigned bubble

**Spirit Add Timer:**

- HUD timer shows when the next spirit add spawns (90-second countdown)
- HUD timer shows when new green blobs respawn (45-second countdown)

### Player Notes

- Requires controlling at least 2 characters in the raid for full automation

---

## Jessip Daggerheart

Setup is automatic when engaged.

### Overview

A fight where Jessip targets random players with sneak attacks that require evasive movement.

### What the Module Does

**Sneak Attack Avoidance:**

- Detects when Jessip is sneaking up on a player
- The targeted player (and all campspotted characters) automatically move 30 meters away
- After 9 seconds, everyone returns to their original position
- Fighters receive a warning message when targeted

### Player Notes

- Requires controlling at least 2 characters in the raid
