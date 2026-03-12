# Crypt of Dalnir: Wizard's Den [Event Heroic]

**Expansion:** Kunark Ascending (Exp 13)

This zone has 1 boss encounter with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [The Gooblin King](#the-gooblin-king) | Bomb rotation item usage |

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
