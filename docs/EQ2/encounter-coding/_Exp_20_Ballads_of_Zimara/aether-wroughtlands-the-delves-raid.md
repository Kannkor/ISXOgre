# Aether Wroughtlands: The Delves [Raid]

**Expansion:** Ballads of Zimara (Exp 20)

This raid zone contains 3 boss encounters.

## Available Setups

| Boss | Description |
|------|-------------|
| [Feri'tal the Immeasurable](#ferital-the-immeasurable) | Curse-based cluster movement |
| [Mezkhuur](#mezkhuur) | Auto cure arcane |
| [Tuer'el of the Delves](#tuerel-of-the-delves) | Add management |

---

## Feri'tal the Immeasurable

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight centered around the Liquidmetal Supplication curse variants (Gold, Silver, and Iron) that require moving to specific Radiating Cluster locations.

### What the Module Does

**Liquidmetal Supplication:**

- Detects which variant of Liquidmetal Supplication the player has (Gold, Silver, or Iron)
- Automatically moves the player to the matching Radiating Cluster
- Handles cluster repositioning as cluster locations change during the fight

**Cure Management:**

- Priest cure curse is disabled during the fight to prevent premature curing of the Liquidmetal Supplication

### Player Notes

- The curse requires moving to the correct colored cluster -- this is handled automatically
- Do not manually cure the Liquidmetal Supplication curse

---

## Mezkhuur

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with automated cure arcane requests, but requiring player awareness to avoid getting stuck.

### What the Module Does

**Cure Arcane:**

- Automatically requests cure arcane when needed

### Player Notes

- **YOU** need to make sure no one gets stuck during the encounter
- The cure is automated but positioning awareness is required

---

## Tuer'el of the Delves

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with add management for Drifting Delver spawns.

### What the Module Does

**Add Management:**

- Handles Drifting Delver add spawns and despawns during the fight

### Player Notes

- Adds are managed automatically as they spawn and despawn
