# Temple of Rallos Zek [Raid]

**Expansion:** Destiny of Velious (Exp 07)

This zone has 5 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Prime-Cornicen Munderrad](#prime-cornicen-munderrad) | AE timer, cure curse |
| [Prime-Curator Undr](#prime-curator-undr) | AE timer, group-based positioning |
| [Proto-Exarch Finnrdag](#proto-exarch-finnrdag) | Red text joust with dual position sets |
| [Supreme Imperium Valdemar](#supreme-imperium-valdemar) | Reflect mechanic |
| [Statue of Rallos Zek](#statue-of-rallos-zek) | Curse handling, dual AE timers, red text move-to-player, add targeting |

---

## Prime-Cornicen Munderrad

Setup command: `Set up for Munderrad`

### Overview

A fight with an AE timer and curse curing.

### What the Module Does

**AE Timer:**

- Toxic Tornado — 30-second HUD countdown

**Cure Curse:**

- Toxic Implosion — detects the cursed player, shows HUD, and triggers cure curse with auto-removal from the queue after 3 seconds

### Player Notes

- Curse cure has a short auto-expire to prevent stale queue entries

---

## Prime-Curator Undr

Setup command: `Set up for Undr`

### Overview

A fight with an AE timer and group-based positioning.

### What the Module Does

**AE Timer:**

- Cyclonic Freeze (knockback) — 40-second HUD countdown

**Group-Based Positioning:**

- Group 1 gets a forward position
- All other groups are positioned further back with significant separation

### Player Notes

- Groups are widely separated

---

## Proto-Exarch Finnrdag

Setup command: `Set up for Proto`

### Overview

A fight with red text jousting between two sets of positions.

### What the Module Does

**Red Text Joust:**

- Two position sets available (normal and easy mode)
- Setup automatically selects the closer set based on player location
- On warhammer announcement, toggles between raid and joust spots within the selected set
- 60-second HUD timer

### Player Notes

- Position set is automatically determined on setup

---

## Supreme Imperium Valdemar

Setup command: `Set up for SIV`

### Overview

A fight with a reflect mechanic.

### What the Module Does

**Reflect Mechanic:**

- When Valdemar says "Your attacks become mine!", shows a 15-second HUD timer
- If currently targeting Valdemar, cancels the spellcast and targets self

**Positioning:**

- Group 1 priests get a separate position; everyone else at the raid spot

### Player Notes

- Stop attacking during the reflect phase

---

## Statue of Rallos Zek

Setup is automatic when engaged.

### Overview

A fight with curse handling, dual AE timers, a red text move-to-player mechanic, and add targeting.

### What the Module Does

**Curse Handling:**

- When the statue curse detriment is detected, calls for cure curse once in raid chat

**Dual AE Timers:**

- Titanic Swipe (trauma) — 30-second HUD countdown
- Poisonous Fog (noxious) — 30-second HUD countdown

**Red Text (Devastating Blow):**

- On announcement, moves all players to the position player's location
- 60-second HUD timer

**Add Targeting:**

- When a greater warboar spawns, non-group-1 fighters target it

### Player Notes

- Multiple simultaneous mechanics with timers and add management
