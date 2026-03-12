# Vasty Deep: Toil and Trouble [Heroic II]

**Expansion:** Reign of Shadows (Exp 17)

This zone has 3 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Palovina Vodlak](#palovina-vodlak) | Auto-identifies transmogrify creature and moves to matching test tube |
| [Nogrovska Vodlak](#nogrovska-vodlak) | Cross-session curse tracking with ordinal-based coordinated curing |
| [The Abandoned Labomination](#the-abandoned-labomination) | Limb Breaker movement, damage type add spawning, math curse puzzle, HO management |

---

## Palovina Vodlak

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where players are transformed into different creatures and must move to the correct test tube to cure the transformation.

### What the Module Does

**Transmogrify Cure:**

- When a character gets the Transmogrify detriment, the module identifies what creature the player has been transformed into by checking the character's visual model
- 8 creature types are supported (satyr, ratman, human variants, hooluk owl, displacer beast, cockatrice, fungusman), each mapped to a specific test tube location
- The character is automatically moved to the matching test tube location
- Once there, the character jumps to trigger the cure
- When the detriment clears, the character returns to their camp spot

**Auto-Target:**

- Fighters get an auto-target list prioritizing "a Dreadfell lycan" adds, with the boss as fallback

### Player Notes

- The transmogrify identification and cure movement is fully automated
- Each creature type has a specific test tube -- the module handles the mapping
- Camp spots are set up with separate positions for tank, DPS, and two healers

---

## Nogrovska Vodlak

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a sophisticated curse-tracking system that coordinates precise curing across the group based on stack counts and boss callouts.

### What the Module Does

**Grave Reminder Tracking:**

- When Nogrovska curses the group, each character reports their Grave Reminder stack count across all sessions using cross-session variables
- This builds a shared data table mapping increment counts to player names

**Coordinated Cure Curse:**

- When the boss announces "I choose the [ordinal] to nurse with your Cure Curse" (first through sixth), priests parse the ordinal to look up which player has that increment count from the shared variable table
- After a 2-second delay, the module cures the specific player
- When a Grave Reminder is successfully cured, all tracking variables are cleared

**Setup:**

- Both standard cure and cure-curse are disabled in cast stacks since the module handles curing manually with precise timing

### Player Notes

- Cure curse timing is fully coordinated by the module -- do not cure manually
- The system maps stack counts across the entire group to determine cure targets
- Standard curing is disabled during this fight

---

## The Abandoned Labomination

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

The most complex encounter in this zone, handling at least 6 distinct mechanics: limb breaker movement, damage type diffusing, a math-based curse puzzle, NPC dispelling, interrupt phases, and heroic opportunity management.

### What the Module Does

**Limb Breaker:**

- When a character gets Limb Breaker, they announce it, cancel Maelstrom of Sound, non-fighters target themselves, and move through 3 waypoints to reach the Center of Pain (crouching at the final point)
- Once there, they wait for the elemental detriment to become cureable, then request cures and use Shadowscream Cure Elemental items
- Includes a safety abort if the detriment duration drops too low
- After curing, the character jumps out and returns to camp

**Damage Type Diffusing (Bard):**

- When the boss announces it is diffusing all damage except a specific type (heat, poison, mental, or slashing), the bard moves to the corresponding panel in the room
- The bard interacts with the panel to release a Crawler Queen add, engages it, and returns to camp when the add dies

**Wrath of the Math (Curse Puzzle):**

- Each character reports their Wrath of the Math increment count across sessions
- The fighter scans all group members to find two players whose increment values sum to equal the NPC's increment count
- Healers are assigned to simultaneously cure the matching pair

**Mortal Test Coil II Dispel:**

- Every 4 seconds, checks if the boss has the Mortal Test Coil II detriment and dispels it if ready

**Disenchant Actor (Mage):**

- Mages scan for "Enchanted" actors and cast Absorb Magic on them with a per-mob cooldown

**Interrupt Mode:**

- When triggered, enables interrupt-tagged abilities in the cast stack for 12 seconds, then automatically disables them

**HO Management (Fighter):**

- Fighter starts Heroic Opportunities when the boss needs a buff removed via HO
- After completion, auto-target resets to add priority

**Thought Experiment:**

- When detected, announces urgently, requests group cures, and uses Shadowscream Cure Arcane items within a 3.5-second window

### Player Notes

- This fight has many simultaneous mechanics -- the module coordinates all of them automatically
- Bards handle panel interaction and add spawning for damage type phases
- The math puzzle is solved automatically by scanning increment values across the group
- Interrupt abilities are toggled on and off as needed
- Mages should have Absorb Magic available for the disenchant mechanic
