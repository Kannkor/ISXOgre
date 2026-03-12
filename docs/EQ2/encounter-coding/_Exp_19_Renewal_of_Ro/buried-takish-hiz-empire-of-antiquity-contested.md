# Buried Takish'Hiz: Empire of Antiquity [Contested]

**Expansion:** Renewal of Ro (Exp 19)

This contested zone contains 3 boss encounters.

## Available Setups

| Boss | Description |
|------|-------------|
| [Gribbick](#gribbick) | Auto-target adds, auto-jump on detriment |
| [The Magmalgam](#the-magmalgam) | Cure management, auto-cure, dispell, weapon swap |
| [Melted Malachiel](#melted-malachiel) | Cure management |

---

## Gribbick

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with add management and a detriment that requires jumping to clear.

### What the Module Does

**Auto-Target:**

- Automatically targets mini mossphibian adds

**Hop to It:**

- Detects the Hop to It detriment on your character
- Automatically jumps to clear the detriment

### Player Notes

- Adds are targeted automatically
- The jump mechanic is handled automatically when the detriment is detected

---

## The Magmalgam

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with multiple detriment mechanics including auto-cure, auto-dispell on the boss, and a weapon swap mechanic.

### What the Module Does

**Cure Management:**

- Disables all cures except cure curse at the start of the fight
- Re-enables cures when the boss is killed

**Elemental Extrusion:**

- Detects the Elemental Extrusion detriment
- Automatically requests a cure curse

**Blazing Hilt:**

- Detects the Blazing Hilt detriment on the boss
- Automatically requests a dispell on the named

**Weapon Swap:**

- Detects the burn text trigger
- Automatically unequips and re-equips primary weapon

### Player Notes

- Only cure curse works during this fight — other cures are disabled
- The weapon swap mechanic is handled automatically
- Cures are restored after the boss is defeated

---

## Melted Malachiel

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A straightforward fight where cures are managed.

### What the Module Does

**Cure Management:**

- Disables cures at the start of the fight
- Re-enables cures when the boss is killed

### Player Notes

- Cures are disabled during the fight and automatically restored after the boss is defeated
