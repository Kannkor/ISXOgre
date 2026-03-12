# Solusek Ro's Tower: Monolith of Fire [Heroic]

**Expansion:** Planes of Prophecy (Exp 14)

This zone has 5 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [West Wing / East Wing](#west-wing--east-wing) | Split group positioning to wings |
| [Jiva](#jiva) | Platform jumping with OgreNav navigation |
| [So'Valiz](#sovaliz) | Claw puzzle automation (collision detection, pillar clicking) |
| [Solusek Ro](#solusek-ro) | Platform jumping, Ro Nova and Avatar Nova jousting |
| [Xuzl](#xuzl) | Fissure vent riding, shard targeting, flame sign clicking |

---

## West Wing / East Wing

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A pre-boss mechanic where the group splits to different wings.

### What the Module Does

**Split Group Positioning:**

- Each non-fighter is assigned to one of 3 wing positions based on their group order
- Uses extended camp spot range to handle the large distances

### Player Notes

- Be near the middle button and set up for -- will run a toon to each wing

---

## Jiva

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where characters must jump onto elevated platforms.

### What the Module Does

**Platform Jumping:**

- Each non-fighter is assigned to one of 5 platforms based on group order
- Navigates to the prep spot, then jumps at the designated point to land on the platform
- After the boss dies, navigates everyone to a regrouping point

### Player Notes

- Will move non-tanks around the middle area and jump them onto the platforms

---

## So'Valiz

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fully automated claw puzzle encounter using collision detection.

### What the Module Does

**Claw Puzzle Automation:**

- When the North/South claw mirroring phase begins, reads which claws are "down" on the source pillar using collision detection
- Bards or marked characters navigate to and click the corresponding claws on the target pillar
- Other characters relay claw status information via cross-session commands
- Handles first-round special coordinates separately

### Player Notes

- Completely automated!

---

## Solusek Ro

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with platform jumping to start and nova jousting during combat.

### What the Module Does

**Platform Jumping:**

- Navigates characters from the start area to the middle platform via designated jump spots

**Nova Jousting:**

- On Ro Nova (flesh to ash), moves everyone behind Solusek Ro, returns after 10 seconds
- On Avatar Nova (die mortals), moves everyone behind the Avatar of the Sun, returns after 10 seconds

### Player Notes

- Will get everyone onto the main platform, then auto-joust behind Ro and Avatar

---

## Xuzl

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with fissure vent riding and shard targeting.

### What the Module Does

**Fissure Vent Riding:**

- Navigates to a fissure vent with an active fire blast and rides it to the top
- Targets the Obsidian Shard when airborne

**Flame Sign Clicking (Solo):**

- When no shards exist, finds and clicks Flame Sword Sign objects

### Player Notes

- The module handles the vertical navigation automatically
