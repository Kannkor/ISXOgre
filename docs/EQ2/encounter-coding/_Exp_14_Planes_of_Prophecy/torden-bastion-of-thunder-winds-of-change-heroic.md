# Torden, Bastion of Thunder: Winds of Change [Heroic]

**Expansion:** Planes of Prophecy (Exp 14)

This zone has 3 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Laef Windfall](#laef-windfall) | Wind barrage dodge, auto-cancel Caught in the Storm |
| [Torstien Stoneskin / Hreidar Lynhillig](#torstien-stoneskin--hreidar-lynhillig) | Protection spell target swap, health balance monitoring |
| [Elif Whitewind](#elif-whitewind) | Auto-dispelling |

---

## Laef Windfall

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a wind barrage dodge and a debuff that must be cancelled.

### What the Module Does

**Wind Barrage Dodge:**

- When the boss prepares a frontal wind barrage, all characters move behind the boss
- Positions reset after the barrage ends

**Auto-Cancel Caught in the Storm:**

- Automatically cancels the Caught in the Storm maintained effect whenever it appears

### Player Notes

- Tanks are positioned in front, everyone else behind during normal combat

---

## Torstien Stoneskin / Hreidar Lynhillig

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A linked pair fight where the unprotected boss must be targeted.

### What the Module Does

**Protection Spell Target Swap:**

- When one boss casts a protection spell, fighters and the group leader automatically target the other boss

**Health Balance Monitoring:**

- Monitors both bosses' health and switches targets if either drops to 1%, preventing premature kills

### Player Notes

- The module coordinates target swapping to keep both bosses balanced

---

## Elif Whitewind

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a dispellable buff.

### What the Module Does

**Auto-Dispelling:**

- Mages and druids automatically dispel the boss's buff when detected

### Player Notes

- Dispelling is handled passively -- no setup required
