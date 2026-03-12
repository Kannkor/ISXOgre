# Echo Caverns: Expedition Precarious [Raidventure]

**Expansion:** Reign of Shadows (Exp 17)

This zone has 1 boss encounter with an OgreBot automation module.

## Available Setups

| Boss | Description |
|------|-------------|
| [Lhurzz the Nibbler](#lhurzz-the-nibbler) | Distance-based jousting to minimize boss healing |

---

## Lhurzz the Nibbler

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where the boss drains blood at regular HP intervals, healing more the closer players are.

### What the Module Does

**Blood Drain Jousting:**

- Triggered at approximately 85/65/45/25/10% HP when the boss announces draining blood
- The module calculates which of two predefined raid spots is farther from the boss and moves the group there
- Being closer to the boss during this mechanic causes the boss to heal more, so maximizing distance is critical

### Player Notes

- The module automatically selects the optimal joust position based on distance from the boss
- Jousting happens multiple times throughout the fight at HP thresholds
