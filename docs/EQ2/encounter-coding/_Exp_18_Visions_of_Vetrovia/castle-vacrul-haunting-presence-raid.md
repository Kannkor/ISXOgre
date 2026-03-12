# Castle Vacrul: Haunting Presence [Raid]

**Expansion:** Visions of Vetrovia (Exp 18)

This zone has 4 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Lord Mayong Mistmoore](#lord-mayong-mistmoore) | Blood joust with role-based positioning, blanket dodge, multi-detriment handling, add tracking |
| [Lenya Thex](#lenya-thex) | Dark Tidings proximity hex rescue, sculpture clicking |
| [Zarrakon](#zarrakon) | Color-coded bloodcurse pool matching, Mark of Darkness add targeting |
| [Poppet the Thrasher](#poppet-the-thrasher) | Organized Chaos jousting |

---

## Lord Mayong Mistmoore

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

The most complex encounter in this zone with many overlapping mechanics: role-based blood jousting, blanket dodging, multiple detriment responses, and add tracking with timers.

### What the Module Does

**Blood Joust:**

- On the joust trigger, different roles go to different spots: main tank stays, off-tank goes to one spot, other tanks to another, and all non-fighters to the raid joust spot
- When the bite trigger fires, positions reset and flagged characters re-target the boss

**Blanket of Eternal Damnation:**

- Continuously scans for blanket actors within 10m of the current camp spot
- If one spawns nearby, calculates the farthest safe spot between two options and moves there
- Positions reset when the actor despawns

**Seeing Red:**

- Non-fighters with this detriment request cures via IRC every 10 seconds

**Vampiric Emblement:**

- Moves the character to a far-away spot when detected, returns when it expires

**Call of Blood:**

- Moves the character within 10m of Mayong when detected, returns when it expires

**Juxtaposed Hex:**

- Reads the hex description to determine whether to cancel it or let it expire naturally

**Royal Guard Add Tracking:**

- When royal guard adds spawn, a 120-second HUD timer is displayed
- Flagged characters auto-target the adds, then retarget the boss when adds die

### Player Notes

- Multiple mechanics run simultaneously -- the module coordinates all positioning
- Role assignments determine joust positions during the blood phase
- The blanket dodge is automatic based on proximity scanning

---

## Lenya Thex

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a proximity hex that requires a specific player to rescue the afflicted character, and a sculpture clicking mechanic.

### What the Module Does

**Dark Tidings Proximity Hex:**

- When a player gets the hex, the module reads the effect text to extract which specific character must cure it
- A cross-session event is fired to that character, who uses the "Rescue from the Hex!" verb on the afflicted player

**Sculpture Clicking:**

- When Lenya activates a sculpture (finality, loyalty, Time, or Wonder), the module maps it to the correct in-game actor
- A flagged character moves to the sculpture and clicks it, then returns
- If the character has the Thexen Hex (preventing further clicks), the flag passes to the next person

### Player Notes

- The hex rescue is coordinated automatically across sessions
- Sculpture clicking is handled by a flagged character with automatic flag passing

---

## Zarrakon

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with color-coded curses that require running to matching colored pools, and an add-targeting phase.

### What the Module Does

**Bloodcurse Pool Matching:**

- Three different curses (Spiteful, Obscure, Chilling) each require running to a corresponding colored pool (Crimson, Golden, Azure)
- The module detects which curse is active, moves to the matching pool's location, and jumps to clear it

**Mark of Darkness Add Targeting:**

- When the Darkness mark is detected, auto-target switches from Zarrakon to the "Oblivion Coagulation" add
- When the mark clears, targeting reverts to Zarrakon

### Player Notes

- Curse-to-pool matching is fully automated
- Auto-target switches between the boss and add based on the mark detriment

---

## Poppet the Thrasher

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a jousting mechanic triggered by the Organized Chaos detriment.

### What the Module Does

**Organized Chaos Joust:**

- When the detriment is detected, waits 2 seconds to confirm, then jousts 28m away from the boss
- When the detriment clears, fighters go to the tank spot and everyone else repositions to the boss

### Player Notes

- The joust has a brief confirmation delay before movement
- Fighters and non-fighters return to different positions after the joust
