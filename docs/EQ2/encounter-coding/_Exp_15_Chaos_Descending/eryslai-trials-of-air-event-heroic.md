# Eryslai: Trials of Air [Event Heroic]

**Expansion:** Chaos Descending (Exp 15)

This zone has 3 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Cyclono](#cyclono) | Auto duck (jump + crouch), distance-based jousting |
| [Quarez](#quarez) | Auto duck (jump + crouch), red text jousting |
| [Kamara Zar](#kamara-zar) | Air Pocket buff auto-movement to Xegony, formation spread |

---

## Cyclono

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with an auto-duck mechanic and distance-based jousting.

### What the Module Does

**Auto Duck:**

- When the boss says to duck, automatically jumps then crouches to avoid the attack

**Distance-Based Jousting:**

- When the boss dispenses with pleas, calculates which of two positions is farther from the boss and moves there

### Player Notes

- Camp spot is set automatically when Cyclono spawns

---

## Quarez

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with jousting triggered by red text announcements.

### What the Module Does

**Auto Duck:**

- Same jump + crouch mechanic as Cyclono

**Red Text Jousting:**

- When the winds blow toward Quarez (red text announcement), moves to the position farther from the boss

### Player Notes

- The joust is triggered by on-screen red text announcements about wind

---

## Kamara Zar

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with an Air Pocket buff mechanic that requires moving to a specific location.

### What the Module Does

**Air Pocket Buff Movement:**

- When a character receives the Air Pocket buff, automatically moves to the Xegony location
- Jumps at the destination to activate the mechanic
- Returns to normal position when the buff fades

**Formation Spread:**

- On setup, spreads all group members in a circle formation around the group leader

### Player Notes

- Priests do not move for the Air Pocket mechanic
- The formation spread uses a 10-meter radius centered on the group leader
