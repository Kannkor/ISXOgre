# Plane of War [Raid]

**Expansion:** Destiny of Velious (Exp 07)

This zone has 8 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [The Enraged War Boar](#the-enraged-war-boar) | Red text joust, AE timer, add tracking |
| [Berik Bloodfist](#berik-bloodfist) | Tainted/Toxic blood chase mechanic, memwipe timer, AE timers |
| [Eriak](#eriak) | Red text AE joust, spectral blast curse handling |
| [Tagrin Maldric](#tagrin-maldric) | Red text joust, death touch timer, shadow/spirit targeting, curse monitoring |
| [Glokus Windhelm](#glokus-windhelm) | Red text joust, shaman clicking, music box targeting, add management |
| [Commander Goreslaughter](#commander-goreslaughter) | Rotating 7-position camp system, crystal placement, curse handling |
| [Commander Corpsemaul](#commander-corpsemaul) | AE timer, curse handling |
| [General Teku](#general-teku) | Red text joust, AE timers, add tracking |

---

## The Enraged War Boar

Setup is automatic (detected by proximity).

### Overview

A fight with red text jousting and add tracking.

### What the Module Does

**Red Text Joust:**

- On rampage, calculates which of two positions is farther from the boar and moves the raid there
- 60-second HUD timer

**AE Timer:**

- Noxious Stench — 30-second HUD countdown

**Add Tracking:**

- Beast of war add spawns tracked with a 60-second HUD timer

### Player Notes

- Boss position determines which side the raid moves to

---

## Berik Bloodfist

Setup is automatic (detected by proximity).

### Overview

A complex fight with a blood curse chase mechanic where cursed players must run to each other.

### What the Module Does

**Tainted Blood Chase:**

- When you receive the Tainted Blood curse, stops offensive actions and jousts out
- Enters a coroutine that continuously moves toward the player with the Toxic Blood debuff
- Jumps when close to trigger proximity cure
- Resumes normal operation when the bloodcurse is removed
- Group 1 fighters cast Sever Hate on the tainted player

**Timers:**

- Memwipe (Bloodfist) — 45-second HUD countdown
- Bloodfist's Fury AE — 30-second HUD countdown
- Fallen warrior add spawns — 60-second HUD timer

### Player Notes

- The bot physically chases the Toxic Blood carrier to cure the Tainted Blood

---

## Eriak

Setup is automatic (detected by proximity).

### Overview

A fight with a red text AE joust and spectral blast curse handling.

### What the Module Does

**Red Text AE Joust:**

- On Demonic Blast charge-up, jousts the raid away
- 50-second HUD timer

**Spectral Blast Curse:**

- When cursed, moves to a separate position, cancels the curse effect, then returns

**Positioning:**

- Fighters offset from the main raid position

### Player Notes

- Curse is self-cancelled after repositioning

---

## Tagrin Maldric

Setup is automatic (detected by proximity).

### Overview

A fight with jousting, death touch timer, shadow figure targeting, and curse monitoring.

### What the Module Does

**Red Text AE Joust:**

- On mighty attack preparation, toggles between two position sets (separate tank/raid spots)
- 50-second HUD timer

**Timers:**

- Touch of the Deceptor (death touch) — 45-second HUD countdown
- Cloud of Deceit AE — 26-second HUD countdown
- Shadowy brigands — 60-second HUD timer

**Shadow/Spirit Targeting:**

- When a shadowy figure enters the fray, sets a 10-second targeting window
- Spirit assassins and spirit slayers that spawn during this window are force-targeted

**Curse Monitoring:**

- Monitors the Tagrin curse detriment and waits for it to fade

### Player Notes

- Spirit adds must be killed quickly during the shadow window

---

## Glokus Windhelm

Setup is automatic (detected by proximity).

### Overview

A complex fight with jousting, aviak shaman interactions, music box targeting, and multi-phase add management.

### What the Module Does

**Red Text AE Joust:**

- On wind force gathering, group 1 toggles between two position sets
- Separate fighter/non-fighter positioning within group 1

**Knockback Timer:**

- Windhelm's Fury — 26-second HUD countdown

**Aviak Shaman Clicking:**

- When a shaman spawns, repeatedly applies barrier-removal verbs (Martial/Divine/Elemental/Toxic) at timed intervals
- 60-second HUD timer with pre-joust at 55 seconds

**Music Box Targeting:**

- Non-group-1 scouts move to position-specific spots around the music box based on its spawn location
- Non-fighters in other groups force-target the music box
- Clears on despawn

**Elite Add Management:**

- Elite guardian spawns tracked with 60-second HUD timer

### Player Notes

- Multiple simultaneous add types require different group assignments

---

## Commander Goreslaughter

Setup is automatic (detected by proximity).

### Overview

A complex fight with a rotating 7-position camp system, crystal placement mechanics, and curse handling.

### What the Module Does

**Rotating Camp Positions:**

- 7 positions cycle on each red text event
- Each red text advances the camp to the next position in the rotation
- Group 1 fighters have separate tank spots with timed joust patterns at each position

**Red Text AE Joust:**

- On massive attack preparation, jousts out and advances to the next position
- 30-second Slaughtering Cloud AE timer

**Crystal Placement:**

- When the Commander calls for Aura of Destruction (blue crystal) or Aura of Death (red crystal), designated players pick up and carry the matching crystal to the boss
- Automated crystal movement using first-person camera, apply verb, and mouse clicks

**Curse Handling:**

- Non-fighters joust to the curse spot for their current rotation position
- Priests self-cure; others call for cure curse
- Returns to camp when curse clears

### Player Notes

- Crystal mechanic can be toggled with `no crystals` / `do crystals` chat commands

---

## Commander Corpsemaul

Setup is automatic (detected by proximity).

### Overview

A fight with an AE timer and curse handling (shares the room with Commander Goreslaughter).

### What the Module Does

**AE Timer:**

- Mauler's Touch — 45-second HUD countdown

**Curse Handling:**

- Non-fighters move to the curse spot, call for cure, and return when cured

### Player Notes

- Simpler mechanics than Commander Goreslaughter

---

## General Teku

Setup is automatic (detected by proximity).

### Overview

A fight with red text jousting, AE timers, and add tracking.

### What the Module Does

**Red Text AE Joust:**

- On draconian assault preparation, toggles between two position sets
- Separate tank/raid/mage spots at each position
- 60-second HUD timer

**Timers:**

- Fist of Rallos AE — 30-second HUD countdown
- Elite diaku war rider add spawns — 90-second HUD timer

**Add Counter:**

- Tracks cumulative warrior add count on a persistent HUD

### Player Notes

- Mage spot used when a Troubador is present or no fighters in group
