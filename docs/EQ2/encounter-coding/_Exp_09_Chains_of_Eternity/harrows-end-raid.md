# Harrow's End [Raid]

**Expansion:** Chains of Eternity (Exp 09)

This zone has 6 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Caerina the Lost / Melanie Everling](#caerina-the-lost--melanie-everling) | NPC dispel, fighter/non-fighter positioning |
| [The Construct of Souls](#the-construct-of-souls) | Three-position ping-pong on red text |
| [Bastion the Immovable](#bastion-the-immovable) | Three-position system, colour change timer, memwipe with defiler logic |
| [Fitzpitzle](#fitzpitzle) | Multi-room curse repositioning |
| [Oligar of the Dead](#oligar-of-the-dead) | Targeted joust with hard mode detection |
| [Drinal](#drinal) | Noxious/elemental handling, add targeting, aggro management, dynamic tank positioning |

---

## Caerina the Lost / Melanie Everling

Setup command: `Set up for Melanie`

### Overview

A fight where the boss must be dispelled when weeping.

### What the Module Does

**NPC Dispel:**

- When Caerina or Melanie "begins to weep...", automatically dispels the NPC

**Positioning:**

- Fighters go to the tank spot, everyone else to the raid spot

### Player Notes

- Two-position fighter/non-fighter split

---

## The Construct of Souls

Setup command: `Set up for Construct`

### Overview

A fight with soul and spirit drain mechanics requiring positional shifts.

### What the Module Does

**Soul/Spirit Repositioning:**

- On "drain the soul!" red text, moves the raid from position 1 to position 2
- On "drain the spirit!" red text, toggles between position 1 and position 3
- Implements a ping-pong dodge pattern between three camp spots

### Player Notes

- Three positions used in alternating pattern based on drain type

---

## Bastion the Immovable

Setup command: `Set up for Bastion` (also accepts `Set up for Bastion Blue` or `Set up for Bastion Red`)

### Overview

A fight with colour-based energy mechanics, trauma AEs, and memory shuffle phases.

### What the Module Does

**Three-Position System:**

- Mid, Blue, and Red camp spots allow manual assignment via setup commands
- `Set up for Bastion` puts you at mid, `Blue` and `Red` variants for the other positions

**Colour Change Timer:**

- When Bastion draws energy from the closest source, starts a 30-second HUD countdown

**Trauma AE Timer:**

- When Bastion's Pummeling fires, starts a 26-second HUD countdown

**Memwipe with Defiler Logic:**

- On memory shuffle, starts a memshuffle timer (30s if Bastion is up, 60s if not)
- Defilers alternate Malicious Spirits casts between groups 1/2 and groups 3/4 on each memwipe, then cancel their maintained Malicious Spirits 10 seconds later

### Player Notes

- Use the Blue/Red setup variants to assign groups to specific positions

---

## Fitzpitzle

Setup command: `Set up for Fitzpitzle`

### Overview

A multi-room fight with curse-based repositioning.

### What the Module Does

**Multi-Room Detection:**

- Determines which of 4 rooms the player is in by comparing distances to room centers

**Curse Repositioning:**

- When cursed, moves to a safe position closer to the room center
- When not cursed, stays at the outer position for that room
- Jousts out on curse detection and returns when curse clears

### Player Notes

- Positions are automatic based on which room you are in

---

## Oligar of the Dead

Setup command: `Set up for Oligar`

### Overview

A fight with a targeted joust mechanic and hard mode support.

### What the Module Does

**Targeted Joust:**

- When Oligar "cackles in the direction of" a player, that player jousts to the safe spot
- Hard Mode detection: checks if Oligar has the "Empowered Guardian" guild tag
- Hard Mode uses a 6-second return timer, normal mode uses 10 seconds

**Positioning:**

- Fighters at tank spot, everyone else at raid spot

### Player Notes

- Hard Mode is detected automatically and adjusts joust timing

---

## Drinal

Setup command: `Set up for Drinal`

### Overview

The final boss with multiple detriment-handling mechanics, add management, and dynamic tank positioning.

### What the Module Does

**Noxious Detriment Handling:**

- When noxious is detected, determines if you are the 1st or 2nd person with nox in the raid
- Each player moves to a separate nox-safe position
- Returns to camp when noxious clears

**Encasing Drinal's Light (Add Targeting):**

- When a player has the Transfiguration detriment and the light actor exists, forces targeting of it
- Disables defensive abilities and ignores normal assist until the add is handled

**Curse Call-Out:**

- If cursed and the power-over-death buff is running low, calls out for a cure curse

The following features require Elite 2:

**Elemental Detriment Handling:**

- Fighters disable offensive, cast Recapture, and move to a separate tank elemental spot
- Non-fighters move to the elemental safe spot

**Red Text Joust (Fighters):**

- On massive smite channel, fighters joust out, move behind at 3 seconds, then back in front at 7.5 seconds

**Aggro Management:**

- When the bot needs to gain Drinal's attention, uses Sneering Assault, Rescue, or Cry of the Warrior in priority order
- When another player needs aggro, fighters disable offensive for 9 seconds

**NPC Dispel:**

- Enchanters dispel Drinal directly

**Dynamic Tank Positioning:**

- Tank positions are calculated relative to Drinal's actual location (in front and behind)

### Player Notes

- Basic noxious handling and add targeting work for all users
- Elite 2 adds elemental handling, red text joust, aggro management, NPC dispel, and dynamic tank positioning
