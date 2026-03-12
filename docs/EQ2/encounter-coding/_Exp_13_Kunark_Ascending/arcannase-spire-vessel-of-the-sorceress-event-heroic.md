# Arcanna'se Spire: Vessel of the Sorceress [Event Heroic]

**Expansion:** Kunark Ascending (Exp 13)

This zone has 2 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Sorceress Gwen'vae](#sorceress-gwenvae) | Enchanter auto-dispelling |
| [The Gooblin King](#the-gooblin-king) | Bomb rotation item usage |

---

## Sorceress Gwen'vae

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where Enchanters automatically dispel a buff from the boss.

### What the Module Does

**Auto Dispell:**

- Enchanters automatically dispel a defensive buff from Sorceress Gwen'vae when detected

### Player Notes

- Only Enchanters perform the dispelling

---

## The Gooblin King

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a bomb rotation item usage mechanic.

### What the Module Does

**Bomb Rotation:**

- Each group member is assigned a slot in the rotation order (1 through 6)
- When it is their turn and the boss has the Amorphous Defense buff, they automatically use a Soothsayer's Bomb Dispenser from inventory on The Gooblin King
- After using the bomb, the rotation advances to the next player

### Player Notes

- The rotation starts when the message about Kly assistants bringing in goblins appears
- Takes about 15 seconds to start -- be patient
- Press `Special_ZoneSpecific` in MCP if the rotation does not start (this resets and displays the rotation order)
