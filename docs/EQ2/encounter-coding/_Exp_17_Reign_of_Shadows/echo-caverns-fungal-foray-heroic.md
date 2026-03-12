# Echo Caverns: Fungal Foray [Heroic]

**Expansion:** Reign of Shadows (Exp 17)

This zone has 2 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Fungus King Cremini](#fungus-king-cremini) | Jousts to mushroom cover during acid rain |
| [Shadowphage](#shadowphage) | Dynamically repositions away from fresh guano spawns |

---

## Fungus King Cremini

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with an acid rain mechanic that requires taking cover under mushrooms.

### What the Module Does

**Acid Rain Jousting:**

- When the boss announces acid rain ("Find cover before the acid kills you!"), all characters joust to a designated mushroom cover spot
- When the text indicates it is safe to move out from under the mushroom, characters return to the main raid spot

### Player Notes

- Movement to and from mushroom cover is fully automated
- Stay near the fight area so the module can position you correctly

---

## Shadowphage

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with dynamic repositioning based on add spawn locations.

### What the Module Does

**Fresh Guano Avoidance:**

- When a "fresh guano" actor spawns during combat, the module calculates which of two predefined raid spots is farther from the guano spawn location
- The group is automatically moved to the safer position

### Player Notes

- The module dynamically chooses the best position based on where the guano spawns
- Two possible raid positions are used depending on guano placement
