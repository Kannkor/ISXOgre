# Altar of Abhorrence [Raid]

**Expansion:** Chains of Eternity (Exp 09)

This zone has 4 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Sarinich the Wretched](#sarinich-the-wretched) | NPC dispel on feast |
| [Pharinich the Forlorn](#pharinich-the-forlorn) | Red text joust with alternating positions, curse separation |
| [Baroddas](#baroddas) | Uncurable curse with add targeting |
| [Baelon of Thule](#baelon-of-thule) | Positioning only |

---

## Sarinich the Wretched

Setup is automatic when engaged.

### Overview

A fight where the NPC must be dispelled during its feast mechanic.

### What the Module Does

**NPC Dispel:**

- When Sarinich "begins to feast on your power!", automatically dispels the NPC to remove its buff

### Player Notes

- Automated dispel only, no positioning

---

## Pharinich the Forlorn

Setup command: `Set up for Pharinich`

### Overview

A fight with alternating camp positions on red text and curse-based player separation.

### What the Module Does

**Red Text Joust (Devastating Ritual):**

- When Pharinich chants a devastating ritual, jousts the raid out
- Alternates the camp position between two spots each time the red text fires (ping-pong pattern)
- 65-second HUD timer tracks the next red text

**Curse Separation:**

- When cursed, determines if you are the 1st or 2nd cursed player in the raid
- First cursed player moves to one safe spot, second moves to a different safe spot
- Returns to the current camp position when the curse clears

### Player Notes

- Camp alternates between two positions each red text cycle

---

## Baroddas

Setup command: `Set up for Baroddas`

### Overview

A fight with an uncurable curse that requires killing a specific add.

### What the Module Does

**Uncurable Curse (Fear-Touched Grasping Vines):**

- When the curse is detected, disables defensive abilities and movement
- Forces targeting of the "Fear-Touched Grasping Vines" add that must be killed to remove the curse
- Announces curse status to the raid
- Restores all systems when the curse clears

### Player Notes

- Extended leash distance (250) is set on setup

---

## Baelon of Thule

Setup command: `Set up for Baelon`

### Overview

Positioning setup only.

### What the Module Does

**Positioning:**

- Sets camp position for the encounter

### Player Notes

- Extended leash distance (250) is set on setup
