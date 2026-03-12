# Echo Caverns: Quarry Quandary [Heroic]

**Expansion:** Reign of Shadows (Exp 17)

This zone has 3 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [The Needlite Queen](#the-needlite-queen) | Stops offensive when Blood Donor is active, coordinates bloodsac item usage |
| [Scyphodon](#scyphodon) | Auto-cancels Magic Sugar, picks up and uses colossal canes |
| [Killmodo](#killmodo) | Jousts non-fighters away from Harsh Conditions target |

---

## The Needlite Queen

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a damage-reflection mechanic and a stacking boss buff that must be removed with items.

### What the Module Does

**Blood Donor:**

- When a player receives the Blood Donor detriment, all offensive abilities are disabled to prevent healing the boss
- When the detriment clears, offensive abilities are re-enabled

**Bloodthirst Stacks:**

- Monitors the boss for Bloodthirst stacks
- When the boss reaches 3 or more stacks, all characters use the "a needlite bloodsac" item (if available and ready) to remove stacks

### Player Notes

- Do not attack while Blood Donor is active -- the module handles toggling offensives automatically
- Ensure you have needlite bloodsac items available for the Bloodthirst mechanic

---

## Scyphodon

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight requiring coordinated item interaction with colossal canes and timed buff cancellation.

### What the Module Does

**Magic Sugar Cancellation:**

- When the boss announces it is ready to devour sugary treats, all characters cancel the Magic Sugar maintained spell to avoid being devoured

**Colossal Cane Auto-Pickup:**

- On each pulse, if the character has no Magic Sugar buff and has a free concentration slot, the module:
    - Moves to a nearby colossal cane interactable object
    - Double-clicks it to pick it up
    - Uses the cane to reapply the Magic Sugar buff
- A cooldown timer prevents re-acquisition too quickly after cancellation

**Camp Spot Setup:**

- Fighters are positioned at a tank spot, everyone else at the raid spot

### Player Notes

- The module handles the sugar/cane cycle automatically
- Ensure you stay near the fight area so the module can find canes

---

## Killmodo

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a targeted joust mechanic.

### What the Module Does

**Harsh Conditions:**

- When a player is targeted by Killmodo's Harsh Conditions, non-fighter characters joust 14 meters away
- After 7 seconds, the character automatically returns to their camp spot
- Fighters are excluded from jousting to maintain aggro

### Player Notes

- Non-fighters are automatically moved away when targeted and returned after the effect resolves
- Fighters stay in place during the mechanic
