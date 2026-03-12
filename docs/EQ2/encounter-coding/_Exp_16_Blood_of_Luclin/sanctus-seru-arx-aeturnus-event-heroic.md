# Sanctus Seru: Arx Aeturnus [Event Heroic]

**Expansion:** Blood of Luclin (Exp 16)

This event heroic zone contains 2 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Archon of Death](#archon-of-death) | Auto-handles pillar positioning based on Pole Position detriment |
| [Sanctus Eternus](#sanctus-eternus) | Role-based positioning |

---

## Archon of Death

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A positioning encounter involving pillars. The tank must alternate between sides of the boss based on the Pole Position detriment, while non-fighters maintain a fixed position.

### What the Module Does

**Pillar Positioning (Fighters):**

- Monitors for the **Pole Position** detriment on the named
- When the detriment is detected, the tank automatically moves to the opposite side of the boss
- Fighters alternate between two positions on either side of the named based on the detriment state

**Non-Fighter Positioning:**

- Non-fighters are placed at a fixed raid position and do not move during the pillar mechanic

### Player Notes

- The tank repositioning is fully automatic based on the Pole Position detriment.
- Non-fighters should stay at their assigned position and focus on DPS/healing.

---

## Sanctus Eternus

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A general placement encounter where fighters and non-fighters are positioned at separate locations.

### What the Module Does

**Role-Based Positioning:**

- Fighters are positioned at the front of the boss
- Non-fighters are positioned at a separate location behind or to the side of the boss

### Player Notes

- Positioning is handled automatically during setup. Stay at your assigned position.
