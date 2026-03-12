# Solusek Ro's Tower: The Obsidian Core [Heroic]

**Expansion:** Planes of Prophecy (Exp 14)

This zone has 2 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Balrezu](#balrezu) | Brazier clicking (bard/marked), add tracking with waypoints |
| [Verlixa](#verlixa) | Full navigation automation, brazier clicking sequence, add tracking |

---

## Balrezu

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with brazier clicking triggered by add spawn/despawn patterns.

### What the Module Does

**Brazier Clicking (Bard/Marked):**

- Tracks 6 brazier locations and which adds spawn near them
- When all adds are dead, the bard or marked character moves to the correct brazier and clicks it
- Fighters also receive a waypoint marker

### Player Notes

- The bard will automatically click the correct brazier

---

## Verlixa

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A complex multi-phase encounter with full navigation automation.

### What the Module Does

**Full Navigation Sequence (Tank/Marked):**

- Maps Shimmering Mirage adds to their room locations (Bottom, Top, Right, Left, Back) as they spawn
- When the tracking phase begins, the tank/marked character navigates to each brazier in order, clicks it, and targets the corresponding add
- After all rooms are cleared, navigates to the exit portal and clicks it
- Returns to Verlixa for the actual fight phase

### Player Notes

- Have everyone follow your tank -- they will move automatically and click the braziers
