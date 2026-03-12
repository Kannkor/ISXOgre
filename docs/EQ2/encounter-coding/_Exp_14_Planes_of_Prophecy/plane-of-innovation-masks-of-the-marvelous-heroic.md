# Plane of Innovation: Masks of the Marvelous [Heroic]

**Expansion:** Planes of Prophecy (Exp 14)

This zone has 5 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Ancient Clockwork Prototype](#ancient-clockwork-prototype) | Auto-targeting the vulnerable prototype |
| [Clockwork Scrounger XVII](#clockwork-scrounger-xvii) | Spread positioning across 5 spots |
| [The Glitched Guardian 10101](#the-glitched-guardian-10101) | Overheat jousting (camp spot swap) |
| [Glitched Cell Keeper](#glitched-cell-keeper) | Red circle dodge jousting |
| [Gearclaw the Collector](#gearclaw-the-collector) | Auto Turn Key verb, auto-dispelling |

---

## Ancient Clockwork Prototype

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with three prototypes where only one is vulnerable at a time.

### What the Module Does

**Auto-Targeting Vulnerable Mob:**

- Tracks which two prototypes are protected and determines which one is NOT immune
- Displays the kill target on HUD and automatically targets the vulnerable prototype

### Player Notes

- Two prototypes are always immune -- the module identifies and targets the correct one

---

## Clockwork Scrounger XVII

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight requiring the group to spread out.

### What the Module Does

**Spread Positioning:**

- Non-fighters are spread across 5 positions based on their group order
- Fighters go to the tank spot

### Player Notes

- Positions are assigned automatically based on sorted group position

---

## The Glitched Guardian 10101

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with jousting triggered by overheating.

### What the Module Does

**Overheat Jousting:**

- When the boss begins to overheat, jousts to the opposite camp spot (whichever is farther)
- Fighters and non-fighters have separate position sets

### Player Notes

- Camp spots swap between two positions on each overheat

---

## Glitched Cell Keeper

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with red circle avoidance.

### What the Module Does

**Red Circle Dodge:**

- When a red circle spawns near the group, jousts to the opposite camp spot

### Player Notes

- Camp spots swap between two positions on each red circle

---

## Gearclaw the Collector

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a key-turning mechanic and dispellable buffs.

### What the Module Does

**Auto Turn Key:**

- When Gearclaw runs out of power, automatically uses the "Turn Key" verb on the boss

**Auto-Dispelling:**

- Mages and druids automatically dispel the boss's buffs when detected

### Player Notes

- Both the key turning and dispelling are handled automatically
