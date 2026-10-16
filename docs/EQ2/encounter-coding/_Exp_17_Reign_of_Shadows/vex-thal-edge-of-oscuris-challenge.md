# Vex Thal: Edge of Oscuris [Challenge]

**Expansion:** Reign of Shadows (Exp 17)

This zone has 4 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Atramonox](#atramonox) | Auto-HOs near adds, auto face away on Tentacular Twirl |
| [The Bagagoogaz](#the-bagagoogaz) | Gaze tracking, HO cure rotation |
| [Hunaga](#hunaga) | Static field HO system, archetype-based positioning, lasher add management |
| [Aten Ha Ra](#aten-ha-ra) | Word of Moonlight HOs, Maiden's Eye dome tracking, Silence broadcast |

---

## Atramonox

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with face-away mechanics, HO management near adds, and ink-based detriments. Players handle their own movement.

### What the Module Does

**Tentacular Twirl:**

- Detected via text trigger -- the module handles the face-away mechanic automatically

**Heroic Opportunities:**

- Auto-HOs are managed when the player is near adds
- Monitors for Spell Dismantle HO completion

**Ink Mechanics:**

- Tracks Inky Curse and Drown in Ink text triggers
- Monitors spawns of summoned adds (summons of Oscuris, inkling blotters, shaded latchers)

### Player Notes

- You handle all movement yourself -- the module manages HOs and face-away
- Stay close to adds when HOs need to be completed

---

## The Bagagoogaz

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A complex fight centered around managing 4 different gaze detriments, coordinated Heroic Opportunities for gaze curing, and a spawning add sequence with a countdown timer.

### What the Module Does

**Gaze System:**

- The boss applies 4 different gazes (Astonishing, Admonishing, Banishing, Shrouded) to players
- Accumulating 3 different gazes kills the player
- The module tracks gaze counts per player across all sessions and prioritizes curing players with the most gazes

**Mask of Unraveling HO:**

- Completing this HO cures gazes on the finishing archetype
- The fighter orchestrates the HO sequence: disables all cast stacks, has non-finishing archetypes complete their slots first, then the finishing archetype completes last to receive the cure
- Cast stacks are re-enabled per archetype as they finish

**Auto-Target (Fighter):**

- Dynamically swaps auto-target priority to focus on spawned adds, returning to the boss when adds are dead

### Player Notes

- The HO system coordinates gaze curing across the group -- follow the cast stack toggling
- Watch for cast stack enable/disable during HO execution
- The countdown timer is managed by killing adds in the correct order

---

## Hunaga

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight built around a static field system where each archetype must create and stand in color-coded fields through Heroic Opportunities.

### What the Module Does

**Static Field System:**

- The boss gains Static buffs (Amber/Azure/Jade/Vermillion) every 5% HP, each tied to an archetype:
    - Amber (yellow) = Priest
    - Azure (blue) = Mage
    - Jade (green) = Scout
    - Vermillion (red) = Fighter
- Each Static buff also casts a matching Lash detriment on players unless the corresponding archetype stands in the matching field

**Static Field HO:**

- Completing the Static Field HO with the correct archetype as the finisher creates a static field of that color
- The module detects which Static detriment the boss has and sets the finishing archetype accordingly
- After field creation, the group is repositioned to the field's group camp spot and the matching archetype gets a separate position inside the field

**Lasher Add Management (Fighter):**

- When a color-coded lasher add spawns (amber, azure, jade, or vermillion lasher), the fighter's auto-target updates to prioritize it
- When the lasher dies, auto-target resets to the boss and the group repositions

**HO Orchestration:**

- Same multi-archetype HO execution as the Bagagoogaz fight: disables cast stacks, has non-finishers go first, finishing archetype completes last

### Player Notes

- Each archetype has specific positioning responsibilities inside their static field
- The HO system is fully automated -- follow the cast stack toggling
- Lasher adds are auto-targeted and killed as they spawn

---

## Aten Ha Ra

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

The final boss of the zone with multiple interconnected mechanics: Word buff removal via HOs, a growing dome (Maiden's Eye) that must be compressed, Ebon add weapon matching, and Xakra disruption.

### What the Module Does

**Word of Moonlight HO:**

- The boss gains one of four Word buffs, each tied to an archetype:
    - Word of Command = Fighter
    - Word of Survival = Priest
    - Word of Power = Mage
    - Word of Subterfuge = Scout
- While active, the Word gives the boss massive potency and 25% ability reflection against the associated archetype
- The module detects which Word is active and sets the matching archetype as the HO finisher
- The HO execution follows the standard multi-archetype pattern

**Maiden's Eye (Growing Dome):**

- At 90% HP, Akelha'Ra spawns with a growing blue dome
- The module monitors dome size (1-5) by checking sword statue actor overlays and displays the size on a HUD element

**Silence from the Shadows:**

- When a player receives Silence from the Shadows, their ID is broadcast across sessions

**Avarice of Darkness:**

- The module monitors the linked curse between the player and boss
- Only requests a cure when the boss's version has been removed (to avoid killing the player)
- Cure curse is disabled globally during the fight to prevent accidental curing

### Player Notes

- Multiple mechanics run simultaneously -- the module coordinates all of them
- Cure curse is disabled to prevent accidental Avarice deaths
- Maiden's Eye size is displayed on the HUD
