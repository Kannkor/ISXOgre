# Dragon Necropolis: Ancient Tombs [Raid]

**Expansion:** Scars of Destruction (Exp 21)

> **:warning: Work In Progress**
>
> Some encounters in this zone are still under development.

This raid zone contains 5 boss encounters.

## Available Setups

| Boss | Description |
|------|-------------|
| [Churaggus](#churaggus) | Curse handling and tank swap (WIP) |
| [Rexxil the Gilded Spirit](#rexxil-the-gilded-spirit) | Item usage and timed cure curse |
| [Sabelraze the Rotting](#sabelraze-the-rotting) | Noxbomb totem clicking and jousting |
| [Nerafiun of the Burning Bones](#nerafiun-of-the-burning-bones) | Joust-then-cure and weapon clicking |
| [Amalgus the Many](#amalgus-the-many) | Joust-then-cure and totem clicking |

---

## Churaggus

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a curse that requires moving to a bonestorm add to remove protection, plus a tank swap mechanic.

### What the Module Does

**Scratched by Churaggus:**

- Detects the Scratched by Churaggus curse on the player
- Finds the nearest chaotic bonestorm add
- Moves the player to the bonestorm add
- Clicks "Remove Protection of Churaggus" on the add to clear the curse

**Fated Gaze (Tank Swap):**

- Detects Fated Gaze on the tank
- Activates Subtle Strikes and fighter dethreat to manage aggro transfer

**Ability Management:**

- Disables Guardian's Recapture ability for the fight

**Add Targeting:**

- Auto-targets chaotic bonestorm and snarling hunter adds

### Player Notes

- This encounter is still a work in progress
- The bonestorm add must be alive and in range for the curse removal to work

---

## Rexxil the Gilded Spirit

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where a special item (Drakebreath Focuser) must be used when healing is detected on the named, plus a timed cure curse mechanic.

### What the Module Does

**Drakebreath Focuser:**

- Monitors for healing-related casts by the named
- Automatically uses the Drakebreath Focuser item when healing is detected

**Entrancing Glimmer (Timed Cure Curse):**

- Detects the Entrancing Glimmer curse on the player
- Waits until the curse has approximately 15 seconds remaining before curing
- Timed curing prevents the curse from being removed too early

**Cure Management:**

- Priest cure curse is disabled during the fight to prevent premature curing of Entrancing Glimmer

### Player Notes

- The Drakebreath Focuser item must be in your inventory
- The timed cure mechanic is important -- curing too early will cause problems

---

## Sabelraze the Rotting

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A complex fight with a noxbomb curse requiring totem interaction, a druid-specific cleanse mechanic, and timed jousting.

### What the Module Does

**Festering Noxbomb:**

- Detects the Festering Noxbomb curse on the player
- Activates sprint and moves the player to the nearest totem
- Clicks the totem to clear the curse
- Applies fighter dethreat (Subtle Strikes, threat ignore list) during the noxbomb run to prevent aggro issues

**Corrosive Blast:**

- Detects Corrosive Blast on the player
- Druids automatically use Natural Cleanse to handle this mechanic

**Confrontation Joust:**

- 45-second timed joust mechanic that runs throughout the fight

**Ability Management:**

- Disables Balanced Synergy
- Disables ability collision checks
- Scouts have an optional positioning configuration to stand with tanks

### Player Notes

- The totem must be reachable for the Festering Noxbomb mechanic to work
- Druids need Natural Cleanse available for Corrosive Blast

---

## Nerafiun of the Burning Bones

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a joust-then-cure mechanic, a weapon clicking mechanic to damage the named, and add management.

### What the Module Does

**Incendiary Release (Joust-Then-Cure):**

- Detects Incendiary Release detriment on the player
- Jousts away from the named to a safe position
- Requests a cure once at the safe position

**Weapon Clicking:**

- Detects special weapon actors that spawn during the fight
- Automatically clicks these weapons to deal damage to the named

**Add Management:**

- Fighters auto-target cinder guardian adds
- Cinder guardians spawn on a 60-second timer

### Player Notes

- Weapons must be clicked to damage the named during certain phases
- Fighters should focus on cinder guardian adds when they spawn

---

## Amalgus the Many

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a joust-then-cure mechanic, a curse requiring totem interaction in the middle of the room, and archetype-specific add management.

### What the Module Does

**Draconic Release (Joust-Then-Cure):**

- Detects Draconic Release detriment on the player
- Jousts away from the named to a safe position
- Requests a cure once at the safe position

**Bone Chilling Curse:**

- Detects the Bone Chilling Curse on the player
- Automatically moves the player to the heat totem in the center of the room
- Clicks the totem to clear the curse

**Heat of Battle:**

- Monitors Heat of Battle stacks on the player
- When stacks exceed 8, clicks the heat totem in the middle to reset

**Add Management:**

- Different add types are targeted by different archetypes:
    - All classes target draconic emberdrakes
    - Mages and priests target draconic gliders
    - Fighters and scouts target draconic toughskins

### Player Notes

- The heat totem in the center of the room is critical for both the curse and Heat of Battle mechanics
- Keep an eye on Heat of Battle stacks -- the module clicks the totem automatically at 8+ stacks
