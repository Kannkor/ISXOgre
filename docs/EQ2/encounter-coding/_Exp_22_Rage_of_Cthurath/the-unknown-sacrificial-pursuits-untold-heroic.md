# The Unknown: Sacrificial Pursuits [Untold Heroic]

**Expansion:** Rage of Cthurath (Exp 22)

This zone has 5 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Setup Name | Description |
|------|-----------|-------------|
| [Fungoid Alpha](#fungoid-alpha) | FungoidAlpha | AutoTarget for adds |
| [Death Spark](#death-spark) | DeathSpark | Full-Auto. Not perfect |
| [Goligok](#goligok) | Goligok | AutoTarget for adds |
| [Molderbeard](#molderbeard) | Molderbeard | AutoTarget for adds |
| [Derlak](#derlak) | Derlak | WIP |

---

## Fungoid Alpha

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A simple add-targeting setup for this encounter.

### Requirements

- **Fighter** (auto-targets adds)

### What the Module Does

**Auto-Target:**

- Fighters auto-target "a fungal harbinger" and "a fungoid dasher" adds before the boss

### Player Notes

- Add-targeting setup only. Other fight mechanics must be handled manually.

---

## Death Spark

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

> **:memo: Not Perfect**
>
> This automation is functional but may not handle all edge cases perfectly.

### Overview

A complex encounter with colored circle mechanics and a lethal Soul Tug curse. Players must move to specific colored circles when they receive matching detriments, and Soul Tug requires precise proximity to a partner before curing.

### Requirements

- All classes participate in circle mechanics

### What the Module Does

**Colored Circle Detriments:**

When a player gets one of four detriments, they are automatically moved to the matching colored circle:

| Detriment | Circle Color | Add to Kill |
|-----------|-------------|-------------|
| Ire Radiation | Yellow | Luminous soul spark |
| Null Vacuum | Blue | Esoteric soul spark |
| Disarming Brand | Red | Emblazoned soul spark |
| Umbral Veil | Black | Fading soul spark |

- Auto-target is dynamically updated to include the matching soul spark add
- When the detriment clears, the add is removed from auto-target
- Circle positions update every second to track moving actors

**Soul Tug Handling:**

- A 15-second lethal curse that requires the cursed player to be alone with their "soul ally" (within 2 meters)
- The module detects the chat message identifying who the soul partner is
- Moves the cursed player to a hug spot
- Only requests a curse cure when exactly 1 other player is within 3 meters
- Coordinates between the two affected players across sessions
- If Soul Tug is active, all other detriment handling is paused

**Dispelling Disabled:**

- Dispelling is turned off because dispelling the boss's buff resets the #1 hate target

**Curse Cures Disabled for Priests:**

- Soul Tug requires precise positioning before curing

### Player Notes

- Messages to chat announce which detriment the player has.
- Soul Tug coordinates between two players automatically.
- Soul Tug takes priority over all other mechanics when active.

---

## Goligok

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A simple add-targeting setup for this encounter.

### Requirements

- **Fighter** (auto-targets adds)

### What the Module Does

**Auto-Target:**

- Fighters auto-target "a digestive sucker" before the boss

### Player Notes

- Add-targeting setup only.

---

## Molderbeard

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter with archetype-specific cap adds and a frontal attack that requires repositioning.

### Requirements

- All classes (auto-target enabled for everyone, not just fighters)

### What the Module Does

**Auto-Target (All Players):**

- All players (not just fighters) have auto-target enabled, targeting all four Cap add types before the boss:
    - Sporepox Cap (scouts)
    - Sporecrux Cap (priests)
    - Sporerage Cap (fighters)
    - Sporespawn Cap (mages)

**Front/Behind Jousting:**

- When the boss "sucks in air" (frontal attack), the module moves everyone behind the mob
- After 10 seconds, fighters reposition in front and non-fighters behind (normal formation)

### Player Notes

- Auto-target is enabled for everyone, not just fighters. It is turned off for non-fighters when the boss dies.
- The group automatically repositions when the frontal attack is announced.

---

## Derlak

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

> **:warning: Work In Progress**
>
> This encounter's automation is still under development.

### Overview

An encounter where the group rotates through dais positions on a timer, dispelling the boss at each new position.

### Requirements

- **Fighter** (drives the encounter, manages formation, auto-targets adds)

### What the Module Does

**Rotating Dais Positions:**

- The group cycles through 5 pre-defined positions using a spread formation at 7 meters
- A new position is selected every 30 seconds
- The tank has a separate spot at each dais position

**Dispelling:**

- Dispels are disabled by default to prevent accidentally resetting the boss
- After moving to a new position and waiting for everyone to arrive, a dispel is enabled
- Once the boss's Steleslag Link is dispelled (confirmed via chat), dispels are re-disabled

**Auto-Target:**

- Fighters auto-target Frostwrought Titan, Flamewrought Titan, and "a shadow-venom umbrith" adds before the boss

### Player Notes

- The group rotates positions automatically on a 30-second timer.
- Do not manually dispel -- the module manages dispel timing carefully.
