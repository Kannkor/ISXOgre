# The Nexus Core [Heroic]

**Expansion:** Tears of Veeshan (Exp 10)

This zone has 4 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Luminox / Core Guardian](#luminox--core-guardian) | Missile volley joust, dual positioning |
| [Amalgam of Energy](#amalgam-of-energy) | Positioning with auto-target list |
| [Blaster Module / Energy Delivery Module](#blaster-module--energy-delivery-module) | Blast joust behind module |
| [Luminox Prime](#luminox-prime) | Blast joust, 60% HP pre-positioning |

---

## Luminox / Core Guardian

Setup command: `Set up for Luminox`

### Overview

A fight with missile volley jousting between two sides of the room.

### What the Module Does

**Missile Volley Joust:**

- When the Core Guardian prepares to fire short-range missiles, determines which side the boss is closer to and moves the raid to the opposite position
- Also triggers on Luminox Prime's light/dark rend attack

**60% Pre-Positioning:**

- When Luminox Prime is near 60% HP, automatically moves the group toward the center of the room

### Player Notes

- Ping-pong joust between two sides based on boss position

---

## Amalgam of Energy

Setup command: `Set up for Amalgam`

### Overview

A positioning setup with auto-target list.

### What the Module Does

**Positioning:**

- Fighters at tank spot with auto-target list "AmalgamOfEnergy" loaded

### Player Notes

- Positioning with automatic target list configuration

---

## Blaster Module / Energy Delivery Module

Setup command: `Set up for Modules`

### Overview

A fight where the group must joust behind the Energy Delivery Module during blast charges.

### What the Module Does

**Blast Joust:**

- When the Blaster Module charges up a massive blast, calculates a point behind the Energy Delivery Module
- Jousts out, moves behind the module, then returns after 8 seconds

### Player Notes

- Auto-target list "Modules" is loaded for fighters

---

## Luminox Prime

Setup is automatic when engaged.

### Overview

The final boss with a blast joust mechanic.

### What the Module Does

**Blast Joust:**

- When Luminox Prime charges up a massive blast, calculates a point behind it
- Jousts out, moves behind the boss, then resets to a fixed position after 7 seconds

### Player Notes

- Connected to the Luminox module for the light/dark mechanic
