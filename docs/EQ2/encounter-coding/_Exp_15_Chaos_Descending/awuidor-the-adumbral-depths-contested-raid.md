# Awuidor: The Adumbral Depths [Contested Raid]

**Expansion:** Chaos Descending (Exp 15)

This zone has 3 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [A Deepwater Kraken](#a-deepwater-kraken) | Conch shell item usage, auto-clicking constrict objects, curse monitoring |
| [Servant of Krziik](#servant-of-krziik) | Two-tier breath jousting (behind NPC or full joust) |
| [Krziik the Mighty](#krziik-the-mighty) | Two-tier breath jousting (behind NPC or full joust) |

---

## A Deepwater Kraken

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a constrict mechanic requiring item usage and object clicking.

### What the Module Does

**Constrict Handling (Marked Toon):**

- When the constrict mechanic fires, a marked character handles the full sequence:
- First attempts to use a Conch Shell item from inventory
- Then pauses casting, walks to the clickable object, double-clicks it, and returns
- Retries automatically if the first attempt fails or no conch shells remain

**Tank Aggro Snap:**

- Guardians automatically cast a snap ability when the boss takes notice of them

**Curse Monitoring (Priests):**

- Priests monitor for the Furious Folly curse and request cure when detected

### Player Notes

- Mark ONE character (such as a bard) to handle the conch mechanic
- These encounters are only available on Drunder

---

## Servant of Krziik

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a two-tier breath jousting system.

### What the Module Does

**Deep Breath (Short Joust):**

- When the servant takes a deep breath, all characters move behind the NPC
- Positions reset after 10 seconds

**Deeper Breath (Full Joust):**

- When the servant takes an even deeper breath, all characters move to the far joust spot
- Positions reset after 10 seconds

### Player Notes

- The regular breath only requires moving behind the boss
- The deeper breath requires getting much farther away

---

## Krziik the Mighty

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with the same two-tier breath jousting as Servant of Krziik.

### What the Module Does

**Deep Breath (Short Joust):**

- When Krziik takes a deep breath, all characters move behind the NPC
- Positions reset after 10 seconds

**Deeper Breath (Full Joust):**

- When Krziik takes an even deeper breath, all characters move to the far joust spot
- Positions reset after 10 seconds

### Player Notes

- Same breath mechanics as Servant of Krziik
- Fighters are positioned in front, non-fighters behind during normal combat
