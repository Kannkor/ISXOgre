# Karuupa Jungle: The Fading Light [Raid]

**Expansion:** Visions of Vetrovia (Exp 18)

This zone has 4 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Quilliclaw](#quilliclaw) | Subtle Strikes aggro management, Scatterstorm curse jousting with raid ordering, portal add handling |
| [Glaur Xrzin](#glaur-xrzin) | Hex cure via movement to named, side script for pre-teleport jousting |
| [The Vetrovian Mantrap](#the-vetrovian-mantrap) | Venomized Decay cure via inventory item |
| [Guabancek](#guabancek) | Front/behind jousting, rested shockwave joust, regeneration timer |

---

## Quilliclaw

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A complex fight with aggro management, curse-based jousting with raid-wide ordering, and archetype-specific portal add encounters.

### What the Module Does

**Subtle Strikes Aggro Management:**

- When the boss burns a target's face into memory, the targeted character casts Subtle Strikes (and Recapture for Guardians) to shed aggro
- Non-targeted characters cancel Subtle Strikes

**Scatterstorm Curse Jousting:**

- When the Scatterstorm curse appears, each cursed character determines their position among all cursed raid members
- Each player moves to a unique relative camp spot to avoid spreading the curse
- Challenge Mode adds timing logic -- waits 3-7 seconds before jousting
- Positions reset when the curse clears

**Ghastly Detriment:**

- Triggers cure requests via cross-session and IRC commands

**Archetype Portal Add Handling:**

- At specific phases, archetype-specific portals spawn (Scout, Fighter, Priest, Mage)
- The matching archetype enters the portal, disables buffs/heals, targets and kills the archetype-specific add, then resets
- Fighters drop aggro with Rescue and Cry of the Warrior before entering

### Player Notes

- Scatterstorm assigns each cursed player to a unique position automatically
- Portal encounters are handled per archetype with auto-targeting
- Fighters drop aggro before entering portals

---

## Glaur Xrzin

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a hex mechanic that requires moving close to the boss for curing.

### What the Module Does

**Sharpshot Technique Hex:**

- When the hex detriment is detected, the character moves toward the named via relative camp spot
- Once within 5 meters, requests a cure curse from all sessions
- Position clears once cured

**Side Script:**

- Launches a side script for jousting before the boss teleports

### Player Notes

- Movement toward the boss for hex curing is automatic
- A side script handles pre-teleport jousting

---

## The Vetrovian Mantrap

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with an uncurable noxious detriment that must be removed using an inventory item.

### What the Module Does

**Venomized Decay:**

- Monitors for the uncurable noxious detriment
- When detected, checks inventory for "An 'Acquired' Witchdoctor's Potion Bag" and uses it to cure the decay
- Reports failure via cross-session and IRC if the item is missing

### Player Notes

- Ensure you have the Witchdoctor's Potion Bag in your inventory
- The module reports missing items so you know to restock

---

## Guabancek

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with front/behind jousting mechanics, a rested shockwave, and a DPS check timer.

### What the Module Does

**Front/Behind Jousting:**

- Frontal breath attack positions tanks in front and everyone else behind
- Tail backlash moves everyone in front of the boss
- Positions reset after a configurable delay

**Rested Shockwave:**

- When the boss is now rested, everyone jousts away from the named

**Regeneration Timer:**

- When the boss begins regenerating plumes, a 65-second on-screen countdown timer is displayed for the DPS check window

### Player Notes

- Front/behind positioning is automated based on the boss's attack type
- Watch the 65-second regeneration timer for the DPS check deadline
