# Blackhook Spiral: Frenzied Breach [Raid]

**Expansion:** Scars of Destruction (Exp 21)

This raid zone contains 3 boss encounters.

## Available Setups

| Boss | Description |
|------|-------------|
| [Orgain the Frenzied](#orgain-the-frenzied) | Auto jousting |
| [Overseer Decarun](#overseer-decarun) | Auto jousting |
| [Foulgore the Rotten](#foulgore-the-rotten) | Curse jousting and archetype-targeted mechanics |

---

## Orgain the Frenzied

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where a poison AoE spawns under the named that requires jousting away. The module handles the joust automatically.

### What the Module Does

**Jousting:**

- Monitors for a poison area overlay spawning under the named
- When detected, jousts the group away from the named
- Pulls pets back during the joust and re-enables them after

### Player Notes

- Pets are automatically managed during jousts

---

## Overseer Decarun

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with Decarun's Decree requiring a joust-then-cure, a tank swap mechanic via Fated Overwatch, and add management.

### What the Module Does

**Decarun's Decree (Joust-Then-Cure):**

- Detects Decarun's Decree detriment on the player
- Automatically jousts away from the named to a safe distance
- Once at the safe position, requests a cure

**Fated Overwatch (Tank Swap):**

- Detects Fated Overwatch on the tank
- Disables threat increases and force targets
- Activates Subtle Strikes to shed aggro
- Adds the affected fighter to the threat ignore list
- Resets all threat settings once the detriment fades

**Dispells:**

- Enables dispell setup for the fight

**Add Management:**

- Mages are set to auto-target Blackhook Lackey adds

### Player Notes

- Tank swap is handled automatically through threat management
- Make sure dispells are configured before the fight

---

## Foulgore the Rotten

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a curse that requires running to a pillar away from the named, plus archetype-targeted preparation mechanics.

### What the Module Does

**Curse of Foulgore:**

- Detects the Curse of Foulgore on the player
- Finds the nearest purple lightning pillar that is NOT near the named
- Automatically moves the player to that pillar for the curse to be handled

**Preparation Mechanic:**

- When the named prepares an archetype-targeted attack, the module jousts the affected archetype away to a safe position
- Uses a short delay before jousting to allow proper timing

### Player Notes

- The curse mechanic requires pillars to be available and away from the named
- Different archetypes will be pulled during different preparation phases
