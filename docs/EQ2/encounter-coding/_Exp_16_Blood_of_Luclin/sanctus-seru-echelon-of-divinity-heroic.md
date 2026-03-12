# Sanctus Seru: Echelon of Divinity [Heroic]

**Expansion:** Blood of Luclin (Exp 16)

This heroic zone contains 1 boss encounter with an OgreBot automation module.

## Available Setups

| Boss | Description |
|------|-------------|
| [Unhilynd](#unhilynd) | Auto-handles multi-stage jousting to avoid AE damage |

---

## Unhilynd

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A jousting encounter where the boss launches skyward and deals massive AE damage. The group must reposition through several stages to avoid the damage, then return to the original positions after the mechanic completes.

### What the Module Does

**Multi-Stage Joust:**

- When the message "Unhilynd launches skyward!" appears, the module begins the joust sequence
- The entire group is repositioned incrementally through several positions over time to avoid the AE damage
- Each stage moves the group further from the danger zone
- After the mechanic completes, the group is automatically returned to their original positions

### Player Notes

- The joust happens in multiple stages -- do not manually move during the sequence.
- Let the module handle all repositioning. Moving manually can put you out of position for the next stage.
- The group will automatically return to the original camp spots once the AE mechanic is over.
