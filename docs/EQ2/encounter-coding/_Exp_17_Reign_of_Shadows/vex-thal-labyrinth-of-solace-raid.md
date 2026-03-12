# Vex Thal: Labyrinth of Solace [Raid]

**Expansion:** Reign of Shadows (Exp 17)

This zone has 1 boss encounter with an OgreBot automation module.

## Available Setups

| Boss | Description |
|------|-------------|
| [Va Dyn Khar](#va-dyn-khar) | Timed joust on deafening roar, add repositioning |

---

## Va Dyn Khar

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a timed retreat-and-return joust mechanic and add positioning.

### What the Module Does

**Deafening Roar Joust:**

- When the boss lets out a deafening roar, the module waits 4 seconds then moves the group to the zone-in spot
- After 6 seconds at the zone-in spot, the group returns to their normal positions
- This is a timed retreat-and-return joust pattern

**Pulsating Renovator Positioning:**

- When a "pulsating renovator" add spawns, the module automatically positions the group near it so the raid can kill it

### Player Notes

- The joust has a brief delay before movement to account for timing
- The boss does not always stay rooted, so joust timing can vary slightly
