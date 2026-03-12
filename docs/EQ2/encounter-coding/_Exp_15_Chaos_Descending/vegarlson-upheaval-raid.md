# Vegarlson: Upheaval [Raid]

**Expansion:** Chaos Descending (Exp 15)

This zone has 3 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Sergie the Blade](#sergie-the-blade) | Multi-area auto jousting, curse clearing via named copy, HUD timer |
| [Tantisala Jaggedtooth](#tantisala-jaggedtooth) | Auto free raid members (Save groupmate) |
| [Warlord Gintolaken](#warlord-gintolaken) | Auto-use Distract from Tactic ability on class call |

---

## Sergie the Blade

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A roaming boss fight with location-aware jousting and curse clearing mechanics.

### What the Module Does

**Multi-Area Auto Jousting:**

- When the boss charges up, calculates which of two positions is farther and moves the raid there
- Supports 7 different area locations as the boss roams through the zone
- Camp spots are set based on which area the boss is currently in

**Curse Clearing (ZonePulse):**

- When cursed, automatically moves to the farther copy of the named, jumps to clear the curse, then returns

**HUD Timer:**

- Displays a 51-second joust countdown timer

### Player Notes

- The module automatically detects which area of the zone the boss is in and adjusts positions
- Fighters get tank spots, everyone else gets raid spots

---

## Tantisala Jaggedtooth

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where the boss stares at a player who must be freed by the raid.

### What the Module Does

**Auto Free Raid Members:**

- When the boss stares at a player, the module automatically has the raid use "Save groupmate!" on the boss
- Supports both normal and Mythic zone difficulty variants

### Player Notes

- The save mechanic is handled automatically via right-click verb on the boss

---

## Warlord Gintolaken

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where the boss calls out a class and the matching player must use a special ability.

### What the Module Does

**Auto Distract from Tactic:**

- When the boss calls out a specific class, the module checks if the character matches
- Only the lowest-ID member of the called class in the raid responds (prevents duplicates)
- Automatically uses the Distract from Tactic ability

### Player Notes

- Only one character per class responds to the call-out automatically
