# Eryslai: The Midnight Aerie [Heroic]

**Expansion:** Chaos Descending (Exp 15)

This zone has 3 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Xochntula](#xochntula) | Frontal jousting (spray magic) |
| [Prosperon the Tempest](#prosperon-the-tempest) | Auto light buff acquisition, priest exclusion |
| [Sterek Swiftwind](#sterek-swiftwind) | Egg clicking/waypoint when boss has Egged On debuff |

---

## Xochntula

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with frontal jousting mechanics.

### What the Module Does

**Frontal Jousting:**

- When the boss sprays magic in front, all characters move behind the boss
- Positions reset automatically after 10 seconds
- Camp spot is set dynamically relative to the boss (fighters in front, non-fighters behind)

### Player Notes

- Fighters are automatically positioned in front of the boss, non-fighters behind

---

## Prosperon the Tempest

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where characters must acquire the Light of Aerieyal buff by moving to light sources.

### What the Module Does

**Auto Light Buff Acquisition:**

- Continuously checks if the character needs the Light of Aerieyal buff
- Each group member is assigned to a unique light source based on their group position
- Automatically moves to the assigned light and jumps to activate it
- Returns to normal position after acquiring the buff

### Player Notes

- Priests do not move for the light buff mechanic
- Each character is assigned a different light source to prevent conflicts

---

## Sterek Swiftwind

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with an egg clicking mechanic triggered by a debuff on the boss.

### What the Module Does

**Egg Clicking (Marked/Bard Toons):**

- Monitors for the Egged On debuff on the boss
- When detected, finds the correct shaking egg by its visual animation
- Marked characters or bards automatically walk to the egg, click it, and return

**Egg Waypoint (Other Toons):**

- Non-marked characters receive a waypoint to the egg's location for manual clicking

### Player Notes

- Mark a character (or the bard handles it automatically) for auto-clicking
- Other characters get a waypoint indicator to the egg
