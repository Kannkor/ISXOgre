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
| [Infernal Tyrant Dennigrah](#infernal-tyrant-dennigrah) | Infernal Tyrant Dennigrah | Full auto with add management and curse control |

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

**Heart Bomb Avoidance:**

- When heart actors spawn (Shriveled Heart, Alluring Heart, Heart of Repulsion), the group automatically moves to whichever of two positions is farther from the heart

**Absorb Magic Disabled:**

- Absorb Magic is disabled for mages during this encounter

### Player Notes

- Fully automatic rose maintenance -- players never need to manually gather roses.
- The module handles all four archetypes independently with the correct rose type.
- The group repositions away from heart bombs when they spawn.

---

## Carnagor

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter where the boss stacks Infernal Carnage (a Flurry buff) that must be dispelled by mages. Fractured phantasm adds also spawn. Behavior changes at Untold Tier 21+.

### Requirements

- **Mage** (dispels Infernal Carnage off the boss)
- **Fighter** (auto-targets phantasm adds, manages aggro at T21+)

### What the Module Does

**Infernal Carnage Dispelling:**

- Mages automatically dispel "Infernal Carnage" off the boss when detected
- 8-second cooldown between dispel attempts

**Curse Cures Disabled:**

- Priest curse cures are disabled during this fight

**Auto-Target (T1-20):**

- All players auto-target "a fractured phantasm" adds before the boss

**T21+ Changes:**

- All AoEs are disabled for all players
- Fighters auto-target both the named and phantasm adds (with keep-engaged)
- All other players auto-target the named directly
- If the named is below 95% HP and not targeting a fighter, the tank moves to an aggro-grab position
- Non-fighters alert the tank to reposition if the named gets within 7 meters of them

### Player Notes

- Mages handle dispelling automatically. Curse cure settings are restored when the boss dies.
- At T21+, the tank manages aggro with repositioning. AoEs are disabled for everyone.
- Auto-target is enabled for all players and is turned off for non-fighters when the boss dies.

---

## Infernal Tyrant Dennigrah

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A complex encounter with multiple add types, a lethal curse tracking mechanic (Cthurath's Will), Enthralling Escapade kiting, Testament jousting, and a seeping seductions phase.

### Requirements

- **All classes** (auto-target is enabled for everyone)
- **Priest** (manages Cure Curse based on Cthurath's Will stacks)
- **Fighter** (intercepts Eternal Pain, manages adds)

### What the Module Does

**Auto-Target (All Players):**

- All players have auto-target enabled, targeting these adds before the boss:
    - an Ebonlithe Enthraller
    - seeping seduction
    - an Ebonlithe Compulsor
    - an Ebonlithe Dazzler (stops targeting below configurable HP%)
    - an Ebonlithe Beguiler (stops targeting below configurable HP%)
    - an Ebonlithe lamia (stops targeting below configurable HP%)

**Cthurath's Will Tracking:**

- Tracks Cthurath's Will stacks across all players via cross-session events
- Priests auto-cast Cure Curse on the player with the lowest stacks
- Curing is suppressed when Consumer's Caress on the named reaches 6+ stacks
- When an Enthraller is alive, the cure threshold drops to 1 stack
- Cure curse has a 10-second cooldown between attempts

**Curse Cures Disabled:**

- Priest cure curses are disabled (the module handles cure curse timing directly)

**Eternal Pain / Intercept:**

- Non-fighters with Eternal Pain broadcast a request for Intercept
- Fighters automatically cast Intercept on the affected player
- Intercept setup is configured automatically

**Enthralling Escapade Kiting:**

- Players with Enthralling Escapade are assigned an Ebonlithe Enthraller add
- The player kites the add through a set of 6 pre-defined spots, moving to the farthest spot from the add
- When the add gets within 14 meters of the player's camp spot, they cycle to the next spot
- Players stun nearby Enthrallers when possible

**Testament to the Consumer Jousting:**

- When a non-fighter is targeted by Testament, they joust to a safe spot for 6 seconds then return
- Fighters stay in place when targeted

**Seeping Seductions Phase:**

- When the seeping seductions phase begins, seeping seduction adds are included in auto-target
- After the countdown reaches 5 during the seeping window, the group moves to a safe position
- After "They're coming down!", the module re-runs setup after 4 seconds

**Configurable Variables:**

| Variable | Default | Description |
|----------|---------|-------------|
| `Tyrant_DisableCureCurse` | FALSE | Set to TRUE to disable priest auto-cure curse entirely |
| `Tyrant_CureCurseStacks` | 2 | Cure curse when player stacks are at or below this value |
| `Tyrant_KillAddsToHP` | 50 | HP% threshold for Dazzler/Beguiler/lamia auto-targeting |

To change a variable: `oc !c -Set_Variable igw:YOURNAME Tyrant_VariableName VALUE`

### Player Notes

- Auto-target is enabled for all players and is turned off for non-fighters when the boss dies.
- Cure Curse is managed automatically by priests based on tracked stacks across the group.
- Enthralling Escapade kiting is fully automatic -- the module moves you through safe spots.
- The module announces configurable settings at setup time in chat.
