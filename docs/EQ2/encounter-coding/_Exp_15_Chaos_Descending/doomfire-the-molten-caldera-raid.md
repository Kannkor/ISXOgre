# Doomfire: The Molten Caldera [Raid]

**Expansion:** Chaos Descending (Exp 15)

This zone has 5 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Arch Mage Yozanni](#arch-mage-yozanni) | Auto-cure with magma gem items, add positioning, HUD timers |
| [Magmaton](#magmaton) | 7-position tank rotation on firewall drops |
| [Pyronis](#pyronis) | Auto jousting on rapid expansion |
| [Jopal the Thief](#jopal-the-thief) | Sniper detection/avoidance via animation checking |
| [Chancellor Traxom / Chancellor Kirtra](#chancellor-traxom--chancellor-kirtra) | Aura-based movement (Crystal/Fiery), periodic center jousting |

---

## Arch Mage Yozanni

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with item-based curing and add positioning.

### What the Module Does

**Auto-Cure with Magma Gem:**

- If the character has a brittle magma gem in inventory, scans all raid members for curse
- Automatically targets and uses the gem on cursed raid members

**Add Positioning (Ro Flamecaster):**

- When a Flamecaster add spawns, fighters position in front and non-fighters behind it
- When the add despawns, positions return to the boss

**HUD Timers:**

- Next Barrage countdown (118 seconds)
- Next Ro Flamecaster spawn countdown (45 seconds)

### Player Notes

- Keep magma gems in inventory for automatic curse removal

---

## Magmaton

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where the tank must rotate through 7 positions when firewalls drop.

### What the Module Does

**Tank Rotation on Firewall:**

- When the boss drops a firewall at its feet, fighters cycle to the next tank position in a rotation of 7 spots
- Non-fighters stay at a fixed raid spot

### Player Notes

- This setup starts in aggro range -- be prepared to engage immediately

---

## Pyronis

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with jousting when the boss expands rapidly.

### What the Module Does

**Auto Jousting:**

- When Pyronis begins to expand rapidly, calculates which of two positions is farther and moves the raid there
- Fighters go to tank spots, others to raid spots

### Player Notes

- The joust alternates between two positions based on boss proximity

---

## Jopal the Thief

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a sniper mechanic where targeted characters must move to safety.

### What the Module Does

**Sniper Detection:**

- When a warning zone actor spawns near the boss, the module checks the character's current animation
- Characters being targeted (sniped) move to a joust spot
- Characters not being sniped move to a safe spot
- Animation checks happen repeatedly over 4 seconds

### Player Notes

- Particle priority is set to 1 on setup for visual clarity

---

## Chancellor Traxom / Chancellor Kirtra

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A dual-boss fight with aura-based movement between the two Chancellors and periodic jousting.

### What the Module Does

**Aura-Based Movement:**

- Characters with Crystal Aura automatically move to Chancellor Kirtra
- Characters with Fiery Aura automatically move to Chancellor Traxom
- The module handles pathing, jumping to clear curses, and returning to position

**Periodic Center Jousting:**

- A recurring 25-second timer sends all characters to a center joust point when tick damage is about to hit
- Coordinated via cross-session commands

### Player Notes

- Camp spots are arranged by raid group with separate positions for tanks, bards, and raid
