# Forlorn Gist: Akashic Incursion [Raid]

**Expansion:** Visions of Vetrovia (Exp 18)

This zone has 10 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Flora Maldehyde](#flora-maldehyde) | Timing-based Pox/Oozing cure coordination |
| [Odelia Wretch](#odelia-wretch) | Fear belt adorn equip |
| [Husk of Gorefus](#husk-of-gorefus) | Fighter aggro transfer and joust on curse |
| [Husk of Memnotum](#husk-of-memnotum) | Priest positional spread and self-cure on curse |
| [Husk of Psyclis](#husk-of-psyclis) | Mage self-target on curse |
| [Husk of Vermidicus](#husk-of-vermidicus) | Scout stealth on curse |
| [The Cloaked Necromancer](#the-cloaked-necromancer) | Composite -- runs all four Husk mechanics simultaneously |
| [Auntie Grimm / Sister Belladonna](#auntie-grimm--sister-belladonna) | Hex area jousting, curse-based jumping to colored pools, raid group positioning |
| [Grandmother Deliria](#grandmother-deliria) | Hex bubble jousting, The Mother's Will item usage, class-based positioning |
| [Mother Ballentree](#mother-ballentree) | Dynamic multi-point rotating joust based on gift/igniter tracking |

---

## Flora Maldehyde

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with two simultaneous detriments that must be cured in the correct order.

### What the Module Does

**Pox/Oozing Cure Timing:**

- Pox Paradox and Oozing Wound land simultaneously
- Antiseptic Splash removes Pox first
- The module waits until Pox is gone but Oozing remains, then triggers cures from priests and requests trauma cures from non-priests
- If both detriments are still present, the module waits for the Antiseptic to resolve first

### Player Notes

- All cures are disabled on setup -- the module manages cure timing manually
- Cure order matters: Pox must be removed before Oozing is cured

---

## Odelia Wretch

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A minimal setup encounter.

### What the Module Does

**Fear Belt Adorn:**

- Equips the fear belt adorn on setup

### Player Notes

- No active fight mechanics -- setup only

---

## Husk of Gorefus

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

Fighter-specific mechanic for the Husk fights.

### What the Module Does

**Distracting Aggression (Fighter):**

- When the curse is detected, calls for Rescue and Cry of the Warrior from other fighters to shed aggro
- Waits in a loop until the boss is no longer targeting this fighter
- Once aggro is fully transferred, jousts 50+ meters away
- Returns when the curse clears

### Player Notes

- Fighters must fully transfer aggro before jousting -- the module handles this coordination
- Rescue and Cry of the Warrior are disabled from cast stacks to prevent unwanted use

---

## Husk of Memnotum

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

Priest-specific mechanic for the Husk fights.

### What the Module Does

**Distracting Admission (Priest):**

- When the curse is detected, sets relative camp spot to a predefined position away from other priests
- Self-cures, then returns when the curse is removed

### Player Notes

- Priests spread out automatically to avoid overlapping curse effects

---

## Husk of Psyclis

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

Mage-specific mechanic for the Husk fights.

### What the Module Does

**Distracting Self-Target (Mage):**

- When the curse is detected, continuously targets self until the curse clears

### Player Notes

- Mages stop attacking automatically by self-targeting during the curse

---

## Husk of Vermidicus

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

Scout-specific mechanic for the Husk fights.

### What the Module Does

**Distracting Stealth (Scout):**

- When the curse is detected, uses class-specific stealth abilities (Dirge Shroud, Ranger Stealth, or Swashbuckler Sneak)
- While invisible, continuously targets self until the curse clears

### Player Notes

- Scouts go invisible and stop attacking automatically during the curse

---

## The Cloaked Necromancer

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A composite boss fight that runs all four Husk archetype mechanics simultaneously.

### What the Module Does

**Combined Husk Mechanics:**

- Every tick, the module calls the ZonePulse for all four Husks (Gorefus, Memnotum, Psyclis, Vermidicus)
- Each archetype handles its Distracting detriment in its unique way (fighter jousts, priest spreads, mage self-targets, scout stealths)

### Player Notes

- All four archetype-specific mechanics run at the same time
- Each class responds to the curse differently -- all handled automatically

---

## Auntie Grimm / Sister Belladonna

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A twin-named fight with hex area jousting, curse-based jumping to specific locations, and raid group-based positioning.

### What the Module Does

**Hex Area Jousting:**

- When Blanket of Aggression (Auntie) or Blanket of Arcana (Sister) hex areas spawn near the group, the module moves everyone to the corresponding joust spot
- Returns to fight position when the hex area despawns

**Curse-Based Jumping:**

- Four different curses each require jumping to a specific 3D location:
    - Curse of Ill Intent, Curse of Lost Voices, Curse of the Spoken Word, Curse of the Wanderer
- The module identifies which curse is active, moves to the matching location, jumps to clear it, then returns

**Raid Group Positioning:**

- Groups 1/3 fight Auntie Grimm, Groups 2/4 fight Sister Belladonna
- Each group has its own fighter and raid positioning

### Player Notes

- Curse-to-location matching is fully automated
- Your raid group assignment determines which named you fight

---

## Grandmother Deliria

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with hex bubble jousting, an item-based arcane cure mechanic, and class-based positioning.

### What the Module Does

**Hex Bubble Jousting:**

- When a Vitrifying Hex bubble spawns within 18m, everyone moves to a joust spot
- Fighters reposition forward for a configurable duration after the bubble despawns

**The Mother's Will Item:**

- The item holder scans all 24 raid members for anyone with an uncurable arcane debuff
- Uses the item to teleport the cursed person to the item holder's location, making the arcane curable

**Class-Based Positioning:**

- Fighters, priests/enchanters, bards, and DPS each get assigned to specific camp spots

### Player Notes

- The Mother's Will item usage is automated for arcane debuff handling
- Class-based positioning is set up on engagement

---

## Mother Ballentree

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a dynamic rotating joust system that cycles through multiple positions.

### What the Module Does

**Dynamic Multi-Point Jousting:**

- Maintains 5 joust positions in a rotating index
- Every pulse, checks for "gift" actors within 30m or "skulking spirit igniter" near the boss
- If either is detected, advances to the next joust position (wrapping from 5 back to 1)
- The entire raid wing moves to the new position
- A 10-second cooldown prevents double-jousting

### Player Notes

- The group cycles through 5 positions as explosives spawn
- Jousting is automatic and raid-wide
