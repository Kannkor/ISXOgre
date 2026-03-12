# Shard of Hate: Utter Contempt [Heroic]

**Expansion:** Planes of Prophecy (Exp 14)

This zone has 3 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Morg and Horb](#morg-and-horb) | Auto meat destruction on Spite Plague curse |
| [Morghorb](#morghorb) | Circle positioning, Primal Hatred cure handling, frontal/rear jousting |
| [Estir the Spiteful](#estir-the-spiteful) | Archetype-based targeted curing |

---

## Morg and Horb

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where the Spite Plague curse is removed by clicking rotting meat.

### What the Module Does

**Auto Meat Destruction:**

- When cursed with Spite Plague, automatically double-clicks rotting meat to remove the curse

### Player Notes

- The meat clicking is automatic when the curse is detected

---

## Morghorb

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with circle positioning and multiple jousting mechanics.

### What the Module Does

**Circle Positioning:**

- Each group member is assigned to one of 6 circle positions and crouches

**Primal Hatred Handling:**

- When cursed with Primal Hatred, jumps out of the circle, moves to the boss, and has a priest cure the curse
- Returns to the assigned circle after being cured

**Frontal/Rear Assault Jousting:**

- On frontal assault, jumps and moves behind the NPC
- On rear assault, jumps and moves in front of the NPC
- Returns to circle position after 5 seconds

### Player Notes

- Auto get into circles on setup

---

## Estir the Spiteful

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where the boss calls out an archetype to destroy, requiring targeted curing.

### What the Module Does

**Archetype-Based Targeted Curing:**

- When the boss announces which archetype to destroy (Mage, Priest, Scout, Fighter), priests identify matching group members
- Priests cure themselves first if they match, then cure all affected group members

### Player Notes

- Make sure you disable cures first (Disable CS_Cure) -- the module manages curing
