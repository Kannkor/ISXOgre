# Arcanna'se Spire: Order and Chaos [Raid]

**Expansion:** Kunark Ascending (Exp 13)

This zone has 4 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Shanaira the Powermonger](#shanaira-the-powermonger) | Venom archetype joust, blazing winds joust |
| [Shanaira the Prestigious](#shanaira-the-prestigious) | Ascension combo counter system by raid group |
| [Botanist Heridal](#botanist-heridal) | Mushroom waypoints and add timer display |
| [Guardian of Arcanna'se](#guardian-of-arcannas) | Statue color detection HUD |

---

## Shanaira the Powermonger

Setup command: `Set up for Shanaira` (only when Shanaira the Powermonger is present)

### Overview

A fight with two jousting mechanics -- archetype-targeted venom and blazing winds ring placement.

### What the Module Does

**Venom Joust:**

- When Shanaira targets an archetype to spread her venom, the affected archetype moves to the joust position
- The archetype to avoid is parsed from the boss emote

**Blazing Winds Joust:**

- When a ring of blazing winds is placed around a specific player, everyone EXCEPT that player moves to the joust position
- After 10 seconds, everyone returns to their normal positions

### Player Notes

- You will need to re-setup after each joust out when appropriate
- Fighters, mages, and other archetypes have separate camp positions

---

## Shanaira the Prestigious

Setup command: `Set up for Shanaira` (only when Shanaira the Prestigious is present)

### Overview

A complex fight centered around countering the boss's magical channels with specific ascension abilities, coordinated across raid groups.

### What the Module Does

**Ascension Combo Counter (Two-Type):**

- When two magic types are channeled, two raid groups are assigned to counter them based on the boss's current health percentage
- At 80% or 40%: Groups 1 and 2 respond
- At 60% or 20%: Groups 3 and 4 respond
- Each group automatically casts a specific pair of ascension abilities matching the magic types being channeled

**Four-Type Counter:**

- When all four magic types are channeled simultaneously, all four raid groups cast their assigned ascension abilities in staggered order
- Each group has a different casting sequence to distribute the countering across all four ascension class ability sets

**Setup:**

- Disables auto-complete ascension combos to prevent interference with the manual combo system

### Player Notes

- Ascension auto-combos are explicitly disabled during this fight
- The combo assignments are coordinated across raid groups -- each group has specific abilities to cast

---

## Botanist Heridal

Setup is automatic when engaged.

### Overview

A fight with mushroom spawns and timed add waves. The module provides informational displays.

### What the Module Does

**Mushroom Waypoint:**

- When a Magic Mushroom spawns, an in-game waypoint is set to its location

**Add Timer:**

- When plants sprout, a 45-second HUD countdown is displayed showing when the next adds will spawn

### Player Notes

- The module provides information only -- players must manually handle mushroom and plant kill timing
- Kill mushrooms when the named is NOT close, kill plants when the named IS close

---

## Guardian of Arcanna'se

Setup is automatic when engaged.

### Overview

A fight where the Guardian attunes to colored statues. The module detects and displays the statue color.

### What the Module Does

**Statue Color Detection:**

- When the Guardian becomes attuned to a statue, reads the actor's tint to determine the color (Blue or Green)
- Displays the statue color and the Guardian's health percentage on the HUD
- Shows the predicted health percentage for the next color change

### Player Notes

- The module provides information only -- players must manually handle killing the correct statue
- Color detection requires being close enough to the Guardian to see the tint change
