# Vaashkaani, Alcazar of Zimara: Chromatic Chamber [Raid]

**Expansion:** Ballads of Zimara (Exp 20)

> **:warning: Work In Progress**
>
> Some encounters in this zone are still under development.

This raid zone contains 3 boss encounters.

## Available Setups

| Boss | Description |
|------|-------------|
| [Aurous the Judged](#aurous-the-judged) | Dual-mob tank positioning (WIP) |
| [Chromon, Titan of Colors](#chromon-titan-of-colors) | Curse curing and increment jousting |
| [Krayte, Titan of Colors](#krayte-titan-of-colors) | Curse curing and increment jousting |

---

## Aurous the Judged

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A dual-mob fight controller that manages the positioning for both Chromon and Krayte. Tank positioning is split between three tanks.

### What the Module Does

**Tank Positioning:**

- Tank 1 is positioned at the raid spot
- Tank 2 is positioned at the Chromon spot
- Tank 3 is positioned at the Krayte spot

**Cure Management:**

- Priest cure curse is disabled during the fight

### Player Notes

- This encounter is a work in progress
- The module manages tank positioning for the dual-mob phase
- Additional mechanics are still being developed

---

## Chromon, Titan of Colors

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with curse tracking and increment-based jousting behind an idol.

### What the Module Does

**Curse of Restraint:**

- Detects the curable variant of Curse of Restraint on the player
- Automatically requests a cure

**Emissary's Mental Instability:**

- Detects this detriment on the player
- Automatically requests a cure

**Increment Jousting:**

- Monitors increment stacks on the player
- When stacks reach the threshold, moves the player behind the Idol of Enlightenment
- Returns the player to their position once stacks drop

### Player Notes

- Cures are handled automatically for both curse mechanics
- Follow the automated movement during increment jousting phases

---

## Krayte, Titan of Colors

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with curse tracking and increment-based jousting behind an idol.

### What the Module Does

**Curse of Restraint:**

- Detects the curable variant of Curse of Restraint on the player
- Automatically requests a cure

**Emissary's Mental Instability:**

- Detects this detriment on the player
- Automatically requests a cure

**Increment Jousting:**

- Monitors increment stacks on the player
- When stacks reach the threshold, moves the player behind the Idol of the Long Dark
- Returns the player to their position once stacks drop

### Player Notes

- Cures are handled automatically for both curse mechanics
- Follow the automated movement during increment jousting phases
- This fight uses a different idol position than Chromon
