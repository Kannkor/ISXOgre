# The Unknown: Edge of Oblivion [Untold Heroic]

**Expansion:** Rage of Cthurath (Exp 22)

This zone has 5 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Setup Name | Description |
|------|-----------|-------------|
| [Sinferzall](#sinferzall) | Sinferzall | Full auto |
| [Do'Guen](#doguen) | Do'Guen | Jousts void auras, kills darkened slashers |
| [Scaladia Yen](#scaladia-yen) | Scaladia Yen | Auto-gathers roses, avoids Broken Heart |
| [Carnagor](#carnagor) | Carnagor | Dispels Infernal Carnage, kills phantasms |
| [Infernal Tyrant Dennigrah](#infernal-tyrant-dennigrah) | Infernal Tyrant Dennigrah | Kills adds, monkey formation |

---

## Sinferzall

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter where the boss places Sap Claret on players, which kills on expiration or if cured within 10 meters of the boss. The module handles safe repositioning before curing.

### Requirements

- **Mage** (cures Anticoagulant, which can only be cured by mages)

### What the Module Does

**Sap Claret Handling:**

- When a player gets Sap Claret, the module moves them away from the boss
- Once at a safe distance, it requests a cure
- After the detriment clears, the player returns to their camp spot

**Anticoagulant Curing:**

- When the player has Anticoagulant (mage-only cure), the module requests a mage-specific cure
- Sap Claret takes priority -- Anticoagulant cures are paused while Sap Claret is active

**Cure and AE Management:**

- All cures are disabled (Sap Claret kills if cured too close to the boss)
- PBAoE abilities are disabled to prevent issues while repositioning

### Player Notes

- Players are moved away from the boss before any cure is attempted.
- AEs and cures are re-enabled when the boss dies.

---

## Do'Guen

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter where the boss summons void auras and spawns crystals on the ground that mark dangerous areas. The module handles group repositioning to avoid both.

### Requirements

- **Fighter** (auto-targets darkened slashers as priority adds)

### What the Module Does

**Void Aura Jousting:**

- When the boss summons a Void-Bound Aura, the group moves to a safe camp spot from a list of pre-defined positions

**Crystal Dodge System:**

- When crystals spawn marking dangerous ground, the module records their locations
- Checks if the current camp spot is within 5 meters of any crystal
- If too close, finds and moves the group to the nearest safe spot

**Return to Center:**

- When the Void-Bound Aura detriment clears from the boss, the group returns to normal positioning

**Auto-Target:**

- Fighters auto-target "a darkened slasher" as priority, then the boss

### Player Notes

- The group repositions dynamically, avoiding crystal spawn locations and cycling through safe spots.

---

## Scaladia Yen

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter where each archetype must gather a specific type of rose to maintain a buff. The module handles rose gathering automatically for all four archetypes.

### Requirements

- Each archetype gathers a different rose type automatically -- no specific class required.

### What the Module Does

**Rose Gathering by Archetype:**

| Archetype | Rose Type | Buff Name |
|-----------|-----------|-----------|
| Scout | Ebon (black) | Lover's Gambit |
| Mage | Violet (purple) | Lovestruck |
| Fighter | Scarlet (red) | Love-Hate Relationship |
| Priest | Gilded (yellow) | Labor of Love |

- Monitors the player's rose buff stacks
- When stacks drop to 3 or below, automatically moves to a nearby rose and clicks it
- Stops gathering when stacks reach 10
- Picks a random rose from all roses of the correct type within 30 meters

**Broken Heart Avoidance:**

- If the player has the "Broken Heart" detriment, rose gathering is suspended (prevents seeing roses and causes knockback)

### Player Notes

- Fully automatic rose maintenance -- players never need to manually gather roses.
- The module handles all four archetypes independently with the correct rose type.

---

## Carnagor

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter where the boss stacks Infernal Carnage (a Flurry buff) that must be dispelled by mages. Fractured phantasm adds also spawn.

### Requirements

- **Mage** (dispels Infernal Carnage off the boss)
- **Fighter** (auto-targets phantasm adds)

### What the Module Does

**Infernal Carnage Dispelling:**

- Mages automatically dispel "Infernal Carnage" off the boss when detected
- 8-second cooldown between dispel attempts

**Curse Cures Disabled:**

- Priest curse cures are disabled during this fight

**Auto-Target:**

- Fighters auto-target "a fractured phantasm" adds before the boss

### Player Notes

- Mages handle dispelling automatically. Curse cure settings are restored when the boss dies.

---

## Infernal Tyrant Dennigrah

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter with multiple add types where the group uses a spread formation around the boss.

### Requirements

- **Fighter** (auto-targets multiple add types)

### What the Module Does

**Monkey In Middle Formation:**

- Sets up a spread formation at 15 meters around the tank spot so the group stays distributed around the boss

**Auto-Target:**

- Fighters auto-target five different add types before the boss:
    - Ebonlithe Enthraller
    - Ebonlithe Dazzler
    - Ebonlithe Beguiler
    - Ebonlithe Compulsor
    - Ebonlithe lamia

**Curse Cures Disabled:**

- Priest curse cures are disabled during this fight

### Player Notes

- The group automatically spreads into a circle formation and prioritizes killing adds.
- Curse cure settings are restored when the boss dies.
