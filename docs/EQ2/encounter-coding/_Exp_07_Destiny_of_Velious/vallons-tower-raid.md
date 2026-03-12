# Vallon's Tower [Raid]

**Expansion:** Destiny of Velious (Exp 07)

This zone has 5 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Lichlord (Maalus Reborn)](#lichlord-maalus-reborn) | Noxious timebomb joust + cancel, buff strip item use, curse handling |
| [Gindan Commander Angler](#gindan-commander-angler) | Boss-distance-based positioning |
| [Ambassador Grindstone](#ambassador-grindstone) | Red text timer |
| [Hand of Vallon](#hand-of-vallon) | Group-based positioning, colour change self-targeting |
| [Kulaxis Da'Kraal (Vallon)](#kulaxis-dakraal-vallon) | Dome assignment, curse handling, add management, multi-timer |

---

## Lichlord (Maalus Reborn)

Setup command: `Set up for Lichlord`

### Overview

A fight with a noxious timebomb mechanic, buff strip recovery, and curse handling.

### What the Module Does

**Noxious Timebomb:**

- When hit with noxious timebomb, moves to the joust spot away from the raid
- Waits until in position, then cancels the timebomb effect
- Announces to the raid that the player has the timebomb
- Returns to camp after cancellation

**Buff Strip Recovery:**

- When the Lichlord strips buffs, shows a 10-second HUD timer

**Taunt Immunity:**

- When fighter taunts become immune, targets the boss and uses the "Crystallized Shard of Hate" inventory item

**Curse Handling:**

- Greater Curse of Devastation — detects the cursed player and triggers cure curse

**Positioning:**

- Scouts get a separate position; everyone else at the raid spot

### Player Notes

- Requires "Crystallized Shard of Hate" inventory item

---

## Gindan Commander Angler

Setup command: `Set up for GCA`

### Overview

A fight with boss-distance-based positioning.

### What the Module Does

**Dynamic Positioning:**

- On rage announcement, calculates which of two position sets is farther from the boss
- Moves the camp to the farther set (separate fighter/non-fighter spots)

### Player Notes

- Positions adjust based on boss location

---

## Ambassador Grindstone

Setup is automatic when engaged.

### Overview

A fight with a red text timer.

### What the Module Does

**Red Text Timer:**

- When Kanogan stomps, starts an 80-second HUD countdown

### Player Notes

- Timer-only module

---

## Hand of Vallon

Setup command: `Set up for Hand`

### Overview

A fight with group-based positioning and a colour change self-targeting mechanic.

### What the Module Does

**Group-Based Positioning:**

- Groups 1/2 share one position; groups 3/4 share another

**Colour Change Mechanic:**

- When the golems begin to change colors, fighters target themselves to drop targeting during the transition

### Player Notes

- Fighters must drop target during colour changes

---

## Kulaxis Da'Kraal (Vallon)

Setup command: `Set up for Vallon`

### Overview

The final boss with dome assignments, curse handling, group 3 add management, and multiple timers.

### What the Module Does

**Dome Assignment:**

- Players are assigned to Red or Blue domes via announcements
- When your dome spawns, automatically moves into it
- When the dome despawns, returns to the raid spot
- 150-second dome respawn timer tracked on HUD

**Curse Handling:**

- If cursed while inside a dome, stays at the raid spot
- If cursed without a dome, moves to the curse spot and requests cure
- Returns to dome or raid spot when cured

**Group 3 Add Management:**

- Group 3 handles suppression field generator and vallonite volley commander spawns
- Calculates the closest position (far, close, or middle) and camps there

**Multi-Timer System:**

- 150-second dome respawn timer
- 60-second add respawn timer
- 54-second Warlord's Siphon AE timer with 9-second damage sub-timer

### Player Notes

- Dome assignment determines positioning throughout the fight
