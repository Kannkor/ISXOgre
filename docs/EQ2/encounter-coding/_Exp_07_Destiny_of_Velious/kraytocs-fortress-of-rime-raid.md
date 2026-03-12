# Kraytoc's Fortress of Rime [Raid]

**Expansion:** Destiny of Velious (Exp 07)

This zone has 5 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Eirreen](#eirreen) | Red text timer |
| [Taaltak the Mighty](#taaltak-the-mighty) | Red text joust with group-based positioning |
| [Tert Turganpuncher](#tert-turganpuncher) | Dynamic boss-tracking, water phase, dual AE timers |
| [Brendegor Bitelimb](#brendegor-bitelimb) | AE timer, red text joust with distance check |
| [Kraytoc](#kraytoc) | Positioning only |

---

## Eirreen

Setup command: `Set up for Eirreen`

### Overview

A fight with a red text timer.

### What the Module Does

**Red Text Timer:**

- When the frigid aura quenches the pulsing flames, starts a 45-second HUD countdown

### Player Notes

- Timer-only module with positioning

---

## Taaltak the Mighty

Setup command: `Set up for Taaltak`

### Overview

A fight with red text jousting and group-based positioning.

### What the Module Does

**Red Text Joust:**

- On ancestral spirits or rage announcements, jousts everyone to the back position
- Returns to the forward position after 10 seconds
- 60-second HUD timer tracks the cycle

**Group-Based Positioning:**

- Group 1 gets a closer position to the boss
- All other groups are positioned further back

### Player Notes

- Two positions based on raid group

---

## Tert Turganpuncher

Setup command: `Set up for Tert`

### Overview

A fight with dynamic boss-tracking, a water phase transition, and dual AE timers.

### What the Module Does

**Dynamic Boss-Tracking:**

- Continuously monitors Tert's distance to two group positions
- When the boss moves closer to the opposite side, jousts the raid to follow

**Water Phase:**

- When Tert retreats, moves the camp spot into the water area

**Dual AE Timers:**

- Deafening Slam (elemental AE) — 30-second HUD countdown
- Wave of Beatings (trauma AE) — 30-second HUD countdown

### Player Notes

- Raid follows the boss automatically between two positions

---

## Brendegor Bitelimb

Setup command: `Set up for Brendegor`

### Overview

A fight with an AE timer and red text jousting with a distance check.

### What the Module Does

**AE Timer:**

- Crushing Boot AE — 43-second HUD countdown

**Red Text Joust:**

- On ritual of rage or icy vortex announcements, jousts to the safe spot
- For the icy vortex, skips jousting if the player is already far enough away (26+ meters)
- Returns after 11 seconds

**Positioning:**

- Fighters stay in place; group 1 priests/bards get a closer spot; everyone else at the back

### Player Notes

- Distance check prevents unnecessary movement on the vortex mechanic

---

## Kraytoc

Setup command: `Set up for Kraytoc`

### Overview

Positioning setup only.

### What the Module Does

**Positioning:**

- Sets camp position for the encounter

### Player Notes

- Requires full raid access to activate
