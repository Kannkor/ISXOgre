# Plane of Innovation: Gears in the Machine [Heroic]

**Expansion:** Planes of Prophecy (Exp 14)

This zone has 2 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Powered Mechanization](#powered-mechanization) | Beam jousting (camp spot swap) |
| [Toa The Shiny](#toa-the-shiny) | Curse-based target management (stop DPS at 3+ curses) |

---

## Powered Mechanization

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a beam jousting mechanic.

### What the Module Does

**Beam Jousting:**

- When the boss begins to cast a powerful beam, moves the group to whichever of two positions is farther from the boss

### Player Notes

- The joust alternates between two positions based on boss proximity

---

## Toa The Shiny

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where DPS must stop when too many curses are active.

### What the Module Does

**Curse-Based Target Management:**

- When 3 or more curses exist in the group, non-assist characters target themselves to stop DPS
- When curses drop below 3, characters retarget the boss

### Player Notes

- DPS automatically stops when curse count gets too high, allowing healers to catch up
