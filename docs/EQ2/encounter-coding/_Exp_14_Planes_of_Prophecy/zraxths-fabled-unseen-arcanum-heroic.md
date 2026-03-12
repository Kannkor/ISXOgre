# Zraxth's Fabled Unseen Arcanum [Heroic]

**Expansion:** Planes of Prophecy (Exp 14)

This zone has 2 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Treskar Throatpuncher](#treskar-throatpuncher) | Jousting with tank/raid split |
| [Anathraxxis Fetidspine](#anathraxxis-fetidspine) | 6-position rotation based on add spawn locations |

---

## Treskar Throatpuncher

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with jousting.

### What the Module Does

**Jousting:**

- When the boss plants himself to destroy, moves the group to whichever of two positions is farther from the boss
- Fighters and non-fighters have separate camp spots

### Player Notes

- At least 1 person MUST speak Ykeshan

---

## Anathraxxis Fetidspine

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with rotational positioning based on add spawn locations.

### What the Module Does

**6-Position Rotation:**

- 6 camp spot positions are arranged in a circular pattern
- When a spewing corpuscle add spawns, determines which position it's closest to
- Moves the entire group to the NEXT position in the rotation (away from the add)

### Player Notes

- The group rotates around 6 positions as adds spawn
