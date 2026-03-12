# Palace of the Ancient One [Raid]

**Expansion:** The Shadow Odyssey (Exp 05)

This zone has 3 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Anashti Sul](#anashti-sul) | Selective curse curing with combat suppression |
| [Switchmaster Zaxlyz](#switchmaster-zaxlyz) | Uncurable arcane portal repositioning |
| [Mynzak](#mynzak) | Debuff-triggered lamp clicking, ice block rescue |

---

## Anashti Sul

Setup is automatic when engaged.

### Overview

A fight with a selective curse curing mechanic that requires distinguishing between two different curses.

### What the Module Does

**Selective Curse Curing:**

- When "The Ancient's Curse" is detected, sends a cross-session command requesting all healers cure this character
- While cursed, suppresses all offensive and defensive abilities
- Re-enables combat when the curse clears
- Does NOT cure "Void Interdiction" (a different curse that should be left alone)

### Player Notes

- Combat is fully paused while cursed

---

## Switchmaster Zaxlyz

Setup command: `Set up for Switchmaster`

### Overview

A fight with an uncurable arcane debuff that must be cleared by running to a portal.

### What the Module Does

**Portal Repositioning:**

- When "Chaotic Infusion" (uncurable arcane) is detected, jousts out and repositions to the cure portal location via campspot
- Announces to the raid that the character is heading to the portal
- Clears the campspot and returns to position when the debuff drops

### Player Notes

- Movement to the portal is automatic

---

## Mynzak

Setup command: `Set up for Mynzak`

### Overview

A fight with debuff-triggered lamp clicking and an ice block rescue mechanic.

### What the Module Does

**Lamp Clicking:**

- When the Mynzak debuff is detected, jousts out and moves toward the void lamp via campspot
- Once within 13 meters, double-clicks the lamp to clear the debuff

**Ice Block Rescue:**

- When "is encased in a block of solid ice" is announced, applies "Drag into the Void Flame" on the frozen group member

### Player Notes

- Lamp interaction is fully automated
- Ice block rescue only targets group members
