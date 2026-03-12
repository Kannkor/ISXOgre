# Vaedenmoor, Realm of Despair [Raid]

**Expansion:** Chaos Descending (Exp 15)

This zone has 3 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Anaheed the Dreamkeeper](#anaheed-the-dreamkeeper) | Priest add targeting with cast stack management, dynamic campspot to Waking Dream adds |
| [Raenha, Sister of Remorse](#raenha-sister-of-remorse) | Add kill counter HUD display |
| [Terris Thule](#terris-thule) | AE timer HUD, auto-cancel casting on planar magic curse |

---

## Anaheed the Dreamkeeper

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where priests are distracted by Waking Dream adds and must kill them before returning to healing.

### What the Module Does

**Priest Distraction Handling:**

- When a priest is distracted by a Waking Dream add, the module automatically switches to offensive mode
- Disables heal, combat, and res cast stacks, enables auto-target on the Waking Dream
- When the priest returns to battle, all cast stacks are re-enabled and auto-target is disabled

**Dynamic Campspot to Adds:**

- Tracks spawning Waking Dream actors and sets camp spot to the nearest alive add
- When an add dies, camp spot moves to the next alive add
- HUD displays the current number of adds alive

### Player Notes

- Priests will release camp spot when distracted and only use offensive abilities -- you will still need to move them
- The module handles cast stack toggling automatically on distract/return

---

## Raenha, Sister of Remorse

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with an add kill tracking mechanic.

### What the Module Does

**Add Kill Counter:**

- Tracks despawning Reanimated Hobgoblin Fearfiend adds while Raenha is in combat
- HUD displays the running count of adds killed
- Counter resets when enough adds have been killed or when Raenha despawns

### Player Notes

- The HUD counter is informational only -- no automated positioning or targeting

---

## Terris Thule

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a recurring AE timer and a curse mechanic that requires stopping all casting.

### What the Module Does

**AE Timer:**

- Tracks Drain Life (100-50% HP) and Hemorrhage (50-0% HP) AEs with HUD countdown timers

**Planar Magic Curse:**

- When planar magic is detected, immediately cancels any current casting and targets self
- Waits in a loop until the curse is cured before resuming normal casting
- Announces casting status changes to the group

### Player Notes

- Casting is automatically stopped during the curse -- do not try to manually cast
- The module handles the full stop-and-wait sequence until the curse is removed

---

## Zone Mechanic: Portals

Campspot near the portal you want to enter (within 30m), then use the MCP button `Special_ZoneSpecific` to go through it.
