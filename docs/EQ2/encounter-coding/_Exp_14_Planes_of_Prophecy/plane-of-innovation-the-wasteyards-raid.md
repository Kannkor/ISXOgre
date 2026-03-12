# Plane of Innovation: The Wasteyards [Raid]

**Expansion:** Planes of Prophecy (Exp 14)

This zone has 8 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Karnah of the Source](#karnah-of-the-source) | Staged Destruction positioning, marked toon callout handling |
| [Junk Beast](#junk-beast) | Auto wrench looting, distribution, and usage |
| [Construct Automaton](#construct-automaton) | Exothermic Combustion jousting |
| [Meldrath the Mechanized](#meldrath-the-mechanized) | Direct Tinkering stack management (stop offensive at 15+) |
| [Meldrath the Malignant](#meldrath-the-malignant) | Deadly Pustules jousting, assassin spawn HUD timer |
| [Operator Figl](#operator-figl) | Targeted Repulsion jousting |
| [Junkyard Mawg](#junkyard-mawg) | Deadly Pustules jousting (east direction) |
| [The Manaetic Behemoth](#the-manaetic-behemoth) | Device response (move to boss on warning) |

---

## Karnah of the Source

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with Staged Destruction positioning and optional marked toon management.

### What the Module Does

**Staged Destruction Handling:**

- When a player is called out for Staged Destruction, they move close to the boss
- When the detriment clears, they return to their original position

**Marked Toon Callout:**

- If a toon is marked before setup, they are positioned far behind the boss to always be the one called out

### Player Notes

- Mark a toon prior to setup to make them the designated callout target

---

## Junk Beast

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with automated wrench looting and usage.

### What the Module Does

**Auto Wrench Handling:**

- When a discarded wrench spawns, the marked toon automatically opens the chest
- Distributes the wrench to the correct player via Leader Only Looting
- After looting, automatically uses the wrench item on the boss repeatedly until consumed

### Player Notes

- You MUST be using Leader Only Looting for wrench distribution

---

## Construct Automaton

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with jousting on Exothermic Combustion.

### What the Module Does

**Exothermic Combustion Jousting:**

- When the boss begins to cast Exothermic Combustion, everyone moves to the joust spot
- Returns after 8 seconds

### Player Notes

- General placement and automatic jousting for the raid

---

## Meldrath the Mechanized

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where DPS must stop when Direct Tinkering stacks get too high.

### What the Module Does

**Stack Management:**

- When Direct Tinkering stacks exceed 14, stops all offensive actions
- When stacks drop below 5, re-enables offensive actions

### Player Notes

- If your stacks get to 15 or above, the bot will not do anything offensive until they drop

---

## Meldrath the Malignant

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with Deadly Pustules jousting and add spawn tracking.

### What the Module Does

**Deadly Pustules Jousting:**

- When cursed with Deadly Pustules, automatically moves away from the raid
- Returns to position when the curse clears

**Assassin Spawn Timer:**

- HUD displays a 60-second countdown when a clockwork assassin spawns

### Player Notes

- Auto jousting for Deadly Pustules

---

## Operator Figl

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with Targeted Repulsion jousting.

### What the Module Does

**Targeted Repulsion Jousting:**

- When targeted with Targeted Repulsion, moves to the joust spot
- Returns after 7 seconds

### Player Notes

- Set up for in the hallway -- auto-jousts anyone who gets the message

---

## Junkyard Mawg

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with Deadly Pustules jousting to the east.

### What the Module Does

**Deadly Pustules Jousting:**

- When cursed with Deadly Pustules, moves to the east (away from the group)
- Returns to position when the curse clears

### Player Notes

- Auto jousting for Deadly Pustules to the east

---

## The Manaetic Behemoth

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a device disable response.

### What the Module Does

**Device Response:**

- When the room must be disabled, characters far from the boss automatically move to the boss

### Player Notes

- Make sure characters respond quickly to the disable warning
