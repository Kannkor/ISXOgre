# Vaedenmoor, Heart of Nightmares [Raid]

**Expansion:** Chaos Descending (Exp 15)

This zone has 3 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Territus, the Deathbringer](#territus-the-deathbringer) | Add phase jousting, buff-based positioning (Residual Nightmares), auto-target switching |
| [Baliath, Harbinger of Nightmares](#baliath-harbinger-of-nightmares) | Tank stack (Concussed) monitoring with threshold alerts |
| [The Summoned Ones](#the-summoned-ones) | Color-based portal assignment, curse stop-casting, HUD timers |

---

## Territus, the Deathbringer

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A complex fight with add phases, buff-based positioning, and group-specific behavior.

### What the Module Does

**Add Phase Handling:**

- When adds spawn ("howl in the distance"), non-group-1 members joust to group-specific add kill spots
- Auto-target switches to Kaniz Frightfeeder adds
- Named combat art cast stack is disabled during the add phase

**Buff-Based Positioning (Residual Nightmares):**

- Characters WITH the Residual Nightmares buff are positioned in front of the boss
- Characters WITHOUT the buff are positioned behind the boss
- Buff is checked repeatedly after frontal AE and add despawn events

**Auto-Target Switching:**

- Automatically switches between add targeting and boss targeting based on fight phase
- Group 2 has special handling during certain buff/frontal combinations

### Player Notes

- Group 1 stays on the boss at all times (tank group)
- Groups 2-4 joust to kill adds then return based on buff status
- HUD shows next event countdown timer

---

## Baliath, Harbinger of Nightmares

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where tank stacks (Concussed debuff) must be managed carefully.

### What the Module Does

**Tank Stack Monitoring:**

- Continuously monitors Concussed debuff stack count
- Announces stack thresholds to the raid at 5, 8, 10, 11, and 12 stacks
- Alert sounds trigger at 8+ stacks
- Announces when stacks fully fade to 0

### Player Notes

- Stack management is up to the raid -- the module reports stacks but does not automate tank swaps
- At 12 stacks, the debuff goes raid-wide

---

## The Summoned Ones

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A combined Saryrn/Terris-Thule encounter with color-coded portal phases and multiple timed mechanics.

### What the Module Does

**Color-Based Portal Assignment:**

- When the lock-down warning fires, the module reads each character's recognition buff color (Blue, Red, or Yellow)
- Automatically moves to the matching colored portal position
- Characters without a color buff move to the center raid spot

**Curse Stop-Casting (Planar Magic):**

- Identical to the Realm of Despair mechanic -- cancels all casting and targets self until cured

**HUD Timers:**

- Portal confinement countdown (12 seconds to get in, 30 seconds confined)
- Hemorrhage AE incoming timer
- Waking Dream/Nightmare add spawn timer
- Frontal notification for fighters (Saryrn phase)

### Player Notes

- Portal assignment is fully automated based on buff colors
- The encounter flows between Saryrn and Terris-Thule phases
- Fighters get a special frontal alert during the Saryrn phase
