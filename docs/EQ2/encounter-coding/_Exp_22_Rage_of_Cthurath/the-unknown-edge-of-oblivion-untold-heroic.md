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

- When a player gets Sap Claret, the module shifts their camp spot away from the boss
- Once at the new position, it requests a cure on a short cooldown
- After the detriment clears, the player returns to their normal camp spot

**Anticoagulant Curing:**

- When the player has Anticoagulant (mage-only cure), the module requests a mage-specific cure with a 5-second cooldown
- Anticoagulant curing is suppressed while Sap Claret is active -- the repositioning takes priority

**Cure and AE Management:**

- All cures are disabled at setup (Sap Claret kills if cured too close to the boss)
- PBAoE abilities are disabled to prevent issues while repositioning

### Player Notes

- Players are moved away from the boss before any cure is attempted.
- AEs and cures are re-enabled when the boss dies.

---

## Do'Guen

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter where the boss summons void auras and crystals spawn marking dangerous ground areas. The module handles group repositioning to avoid both.

### Requirements

- **Fighter** (auto-targets darkened slashers as priority adds)

### What the Module Does

**Void Aura Jousting:**

- When the boss summons a Void-Bound Aura, the module resets the spot index and moves the group to the first available pre-defined position along a ring of 10 safe spots
- Bad spot locations are cleared at the start of each Void Aura event

**Crystal Dodge System:**

- When a crystal spawns marking a dangerous ground area, the module records its location
- After a 2-second delay (allowing all crystals in a batch to register), it checks whether the current camp spot is within 5 meters of any crystal
- If too close, it scans forward through the pre-defined spots (starting from the current index) and moves the group to the first safe spot found
- When crystals despawn, their locations are removed from the bad-spot list

**Return to Center:**

- When the Void-Bound Aura detriment clears from the boss (with a minimum 10-second hold to avoid early return), the group's ranged camp spot is cleared and they return to normal positioning

**Auto-Target:**

- Fighters auto-target "a darkened slasher" as priority, then the boss

### Player Notes

- The group repositions dynamically, avoiding crystal spawn locations and cycling through safe spots around the room.

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
- When stacks drop to 3 or below, the module moves to a random rose of the correct type within 30 meters and clicks it
- Stops gathering when stacks reach 10
- After clicking, the player returns to the normal camp spot; a randomized cooldown (2--4 seconds for non-priests, 4--8 seconds for priests) prevents clicking too quickly

**Broken Heart Avoidance:**

- If the player has the "Broken Heart" detriment, rose gathering is suspended (prevents seeing roses and causes knockback)
- The click is also skipped mid-gather if Broken Heart appears before the rose can be clicked

**Heart Bomb Avoidance:**

- When a heart actor spawns (Shriveled Heart, Alluring Heart, Heart of Repulsion), the module moves the group to whichever of two pre-defined positions is farther from the heart

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
- **Fighter** (auto-targets phantasm adds; manages aggro at T21+)

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
- Fighters auto-target both the named and phantasm adds (with keep-engaged on both)
- All other players auto-target the named directly
- If the named is below 95% HP and not targeting a fighter, the tank moves to an aggro-grab position
- Non-fighters alert the tank to reposition if the named gets within 7 meters of them; the tank then temporarily moves to a reposition spot and returns to tank spot after 5 seconds

### Player Notes

- Mages handle dispelling automatically. Curse cure settings are restored when the boss dies.
- At T21+, the tank manages aggro with repositioning. AoEs are disabled for everyone.
- Auto-target is enabled for all players; non-fighter auto-target is turned off when the boss dies.

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

- All players have auto-target enabled, targeting these adds before the boss (in priority order):
    - an Ebonlithe Enthraller
    - seeping seduction
    - an Ebonlithe Compulsor
    - an Ebonlithe Dazzler (stops targeting below configurable HP%)
    - an Ebonlithe Beguiler (stops targeting below configurable HP%)
    - an Ebonlithe lamia (stops targeting below configurable HP%)
    - Infernal Tyrant Dennigrah

- Fighters have force-target overrides disabled so they can freely switch to manage adds

**Cthurath's Will Tracking:**

- Each player broadcasts their current Cthurath's Will stack count to the group every 10 seconds
- Priests find the group member with the lowest stacks who is also currently cursed and cast Cure Curse on them
- Curing is suppressed when Consumer's Caress on the named reaches 6 or more stacks
- When an Enthraller is alive, the cure threshold drops to 1 stack (only cure at 1 stack)
- Otherwise, the threshold is configurable via `Tyrant_CureCurseStacks` (default: 2)
- Cure Curse has a 10-second cooldown between attempts

**Curse Cures Disabled:**

- Priest auto-cure curses are disabled (the module handles cure curse timing directly)

**Eternal Pain / Intercept:**

- Non-fighters with Eternal Pain announce in chat and broadcast an intercept request
- Fighters automatically cast Intercept on the affected player
- Intercept setup is configured automatically at setup time and reset on kill

**Enthralling Escapade Kiting:**

- Players with Enthralling Escapade are assigned their Ebonlithe Enthraller add
- The module immediately moves the player to the pre-defined kiting spot farthest from the add
- As the add closes in, when it gets within 14 meters of the player's camp spot, the module advances to the next kiting spot
- The kiting loop uses 6 pre-defined positions plus either the tank spot (fighters) or raid spot (non-fighters) as the final position
- When the detriment clears, kiting stops and the player's camp spot is cleared
- Players stun nearby Enthrallers when within 12 meters and a stun ability is available (3-second cooldown)

**Testament to the Consumer Jousting:**

- When a non-fighter is targeted by Testament to the Consumer, they joust to a safe spot for 6 seconds then return
- Fighters stay in place when targeted
- Players currently kiting an Enthraller handle Testament differently -- if on the last kiting position (raid/tank spot), they cycle to spot 1 instead of using the testament joust spot

**Seeping Seductions Phase:**

- When "Destroy the seeping seductions" appears, a 65-second seeping window begins
- When the countdown reaches 5 during the seeping window, the group moves to a designated safe position; if camp spots are enabled, the group also jumps
- After "They're coming down! Watch out!", the module re-runs full setup after a 4-second delay

**Configurable Variables:**

| Variable | Default | Description |
|----------|---------|-------------|
| `Tyrant_DisableCureCurse` | FALSE | Set to TRUE to disable priest auto-cure curse entirely |
| `Tyrant_CureCurseStacks` | 2 | Cure curse when player stacks are at or below this value |
| `Tyrant_KillAddsToHP` | 50 | HP% threshold for Dazzler/Beguiler/lamia auto-targeting |

To change a variable: `oc !c -Set_Variable igw:YOURNAME Tyrant_VariableName VALUE`

The group leader announces current settings in chat at setup time.

### Player Notes

- Auto-target is enabled for all players; non-fighter auto-target is turned off when the boss dies.
- Cure Curse is managed automatically by priests based on tracked stacks across the group.
- Enthralling Escapade kiting is fully automatic -- the module moves you through safe spots and advances when the add gets too close.
- The module announces configurable settings at setup time in chat.
