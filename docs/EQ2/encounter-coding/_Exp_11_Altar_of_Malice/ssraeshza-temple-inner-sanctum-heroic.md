# Ssraeshza Temple: Inner Sanctum [Heroic]

**Expansion:** Altar of Malice (Exp 11)

This zone has 4 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Pov Xin'Kaas](#pov-xinkaas) | Port-and-click mechanic, low HP joust |
| [Stonefang](#stonefang) | Dust joust, hide line-of-sight mechanic |
| [Kesa'Tra Xon'Xiu](#kesatra-xonxiu) | Vision impairment, illusion clicking |
| [Arch Lich Rhag'Zadune](#arch-lich-rhagzadune) | Pool of disease dodging, add tracking, cure curse |

---

## Pov Xin'Kaas

Setup command: `Set up for Pov`

### Overview

A fight with a teleport mechanic and a low HP joust phase.

### What the Module Does

**Port-and-Click:**

- Monitors vertical position to detect when teleported up
- When returned down, automatically clicks all listless body actors to free raid members (up to 12 clicks)

**Low HP Joust:**

- When Pov drops below 30% HP, non-fighters move to a joust position

### Player Notes

- Tank and group have separate campspot positions

---

## Stonefang

Setup command: `Set up for Stonefang`

### Overview

A fight with two distinct avoidance mechanics -- a dust joust and a stoney scales hide phase.

### What the Module Does

**Stoney Scales (Hide):**

- Moves to joust spot, then after 3 seconds to a line-of-sight hide spot, then 9 seconds back to joust spot, then returns to campspot

**Poisonous Dust (Joust):**

- Moves to joust spot, returns to campspot after 5 seconds

### Player Notes

- Two different movement patterns depending on the boss's ability

---

## Kesa'Tra Xon'Xiu

Setup command: `Set up for Kessatras`

### Overview

A fight where vision impairment targets must relay their location so bards and enchanters can click the correct illusion.

### What the Module Does

**Illusion Clicking:**

- When "Your vision is impaired!" fires, the affected player relays their location to all sessions
- Bards and Enchanters receive the relay, navigate to the correct illusion location, click it, then return to their position
- North/south positioning is determined by location in the room

### Player Notes

- Bards and Enchanters handle the illusion clicking automatically
- Multiple illusion spawn locations are tracked throughout the room

---

## Arch Lich Rhag'Zadune

Setup command: `Set up for Lich` (also accepts `Set up for Arch`)

### Overview

A fight with add tracking, pool of disease dodging, and curse management.

### What the Module Does

**Add Tracking:**

- Tracks which adds are alive (warrior and summoner) and automatically updates campspot to the correct side as adds die

**Pool of Disease Dodging:**

- When a pool of disease spawns within 7 meters, auto-moves to the farther of two available campspot positions

**Cure Curse Management:**

- Monitors Death Shackles curse
- Calls out via group say for cure curse twice -- once at 15 seconds remaining, again at 8 seconds

### Player Notes

- Campspot shifts dynamically as adds are killed
