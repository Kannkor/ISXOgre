# Fabled Kael Drakkel [Contested]

**Expansion:** Chaos Descending (Exp 15)

This zone has 1 boss encounter with an OgreBot automation module.

## Available Setups

| Boss | Description |
|------|-------------|
| [Soren the Vindicator](#soren-the-vindicator) | Forces of Zek jousting (WIP) |

---

## Soren the Vindicator

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

!!! warning "Work in Progress"
    This encounter's automation is still under development.

### Overview

A fight with jousting triggered by Forces of Zek spawning.

### What the Module Does

**Forces of Zek Jousting:**

- When a Forces of Zek actor spawns, the module calculates which of two camp spots is farther from the spawn
- Moves the group to the farther position
- Fighters get tank spots, non-fighters get raid spots

### Player Notes

- Auto-detection is based on proximity (500 range) to the boss
