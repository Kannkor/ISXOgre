# Vegarlson: Ruins of Rathe [Heroic]

**Expansion:** Chaos Descending (Exp 15)

This zone has 2 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Slurpgaloop](#slurpgaloop) | Fully automated frontal/rear poison jousting, knockback recovery |
| [Koni Ferus and Pete Bog](#koni-ferus-and-pete-bog) | Fully automated tree spawn jousting |

---

## Slurpgaloop

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fully automated fight with directional poison jousting and knockback recovery.

### What the Module Does

**Frontal Poison Jousting:**

- When the boss prepares to spit poison in front, all characters move behind the boss
- Positions reset automatically after 7 seconds

**Rear Poison Jousting:**

- When the boss prepares to spray poison behind, all characters move in front of the boss
- Positions reset automatically after 7 seconds

**Knockback Recovery:**

- When the boss's legs bulge (knockback incoming), camp spot movement is temporarily disabled
- After the knockback, camp spot is recalculated based on the boss's new position and movement re-enabled

### Player Notes

- Camp spot is set dynamically relative to the boss's facing direction
- The fight is completely automated -- set up and engage

---

## Koni Ferus and Pete Bog

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fully automated fight with tree spawn jousting.

### What the Module Does

**Tree Spawn Jousting:**

- When the forest grows or healing is requested, the module determines which named is active
- Calculates which of two positions is farther from the boss and moves the group there
- Fighters and non-fighters have separate position sets

### Player Notes

- The fight is completely automated -- set up and engage
- The joust alternates between two positions based on boss proximity

---

## Zone Mechanic: Knockdown Recovery

When you fall to the ground in this zone, the module automatically stands you back up after a brief delay.
