# Plane of Disease: Virulent Insurrection [Raid]

**Expansion:** Planes of Prophecy (Exp 14)

This zone has 2 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Grummus](#grummus) | Auto cure-curse relay (Gut Check), fighter Marked detriment management, HUD timer (WIP) |
| [Skal'sli the Wretched](#skalsli-the-wretched) | Vomit jousting, intelligent cure distribution across priests, self-cure (WIP) |

---

## Grummus

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

!!! warning "Work in Progress"
    This encounter's automation is still under development.

### Overview

A fight with auto curse-cure relay and fighter-specific detriment management.

### What the Module Does

**Auto Cure-Curse Relay (Gut Check):**

- When the Gut Check curse duration drops below 17 seconds, automatically broadcasts a cure relay to the group

**Fighter Marked Detriment:**

- Fighters monitor the Marked detriment and cast subtle strikes when stacks are high
- When duration drops, cancels subtle strikes and casts Provocation to regain aggro

**HUD Timer:**

- Brutal Disease countdown (37 seconds)

### Player Notes

- Fighters automatically manage their aggro during the Marked mechanic

---

## Skal'sli the Wretched

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

!!! warning "Work in Progress"
    This encounter's automation is still under development.

### Overview

A fight with vomit jousting and intelligent distributed curse curing.

### What the Module Does

**Vomit Jousting:**

- When the boss prepares to vomit, moves the group to the opposite camp spot

**Intelligent Cure Distribution:**

- Each priest determines their ordinal position among all priests in the raid
- Each priest cures a specific cursed player based on their position, distributing cures evenly
- Separate handling for caster, tracker, warlord, and healer curse variants

**Priest Self-Cure:**

- Priests automatically cure themselves when hit with the Healer's Holistic Hampering curse

### Player Notes

- Cure duties are distributed automatically across all priests in the raid
