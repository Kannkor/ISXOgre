# Ossuary: Resonance of Malice [Heroic]

**Expansion:** Altar of Malice (Exp 11)

This zone has 2 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Praetor Pheris](#praetor-pheris) | Bone wall jousting, curse warning |
| [Elder Senistus Verish](#elder-senistus-verish) | Spread positioning |

---

## Praetor Pheris

Setup command: `Set up for Praetor` (also accepts `Set up for Pheris`)

### Overview

A fight with bone walls that require the group to joust to the opposite side of the room.

### What the Module Does

**Bone Wall Jousting:**

- When a bone wall spawns, automatically moves the group to the opposite side of the room
- Uses staged movement with timed waypoints: halfway, far side, back to halfway, back to center

**Curse Warning:**

- Monitors the Cursed Resonation debuff duration
- When duration drops to 10 seconds or less, announces that the curse is expiring

### Player Notes

- Positioned in the middle of the room by default

---

## Elder Senistus Verish

Setup command: `Set up for Elder` (also accepts `Set up for Senistus`)

### Overview

A fight requiring spread positioning for all group members.

### What the Module Does

**Spread Positioning:**

- Assigns all 6 group members to individual spread spots
- Positions are assigned based on sort order with the fighter/tank getting a separate spot

### Player Notes

- Each group member gets a unique position to prevent stacking
