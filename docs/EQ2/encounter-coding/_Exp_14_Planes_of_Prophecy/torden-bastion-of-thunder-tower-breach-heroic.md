# Torden, Bastion of Thunder: Tower Breach [Heroic]

**Expansion:** Planes of Prophecy (Exp 14)

This zone has 1 boss encounter with an OgreBot automation module.

## Available Setups

| Boss | Description |
|------|-------------|
| [Auliffe Chaoswind](#auliffe-chaoswind) | Fire ring jousting (white/red ring detection) |

---

## Auliffe Chaoswind

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with jousting triggered by fire ring spawns.

### What the Module Does

**Fire Ring Jousting:**

- When a white ring spawns, moves the group to position 1
- When a red ring spawns while the boss is in combat, moves the group to position 2
- Alternates between safe positions based on which ring appears

### Player Notes

- You will need to control your DPS manually
