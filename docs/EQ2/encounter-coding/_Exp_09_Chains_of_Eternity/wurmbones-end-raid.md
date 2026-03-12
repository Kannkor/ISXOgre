# Wurmbone's End [Raid]

**Expansion:** Chains of Eternity (Exp 09)

This zone has 3 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Kradon the Drake Lord](#kradon-the-drake-lord) | Curse-based joust, elemental AE timer |
| [Zazun](#zazun) | Hand of the Devourer pause, curse handling |
| [Necromunger](#necromunger) | Curse call-out |

---

## Kradon the Drake Lord

Setup command: `Set up for Kradon`

### Overview

A fight with curse-based jousting and an elemental knockback AE timer.

### What the Module Does

**Curse-Based Joust:**

- When cursed, non-fighters joust out and move to the joust spot
- Fighters remain at their position (no curse movement)
- Returns to raid spot when the curse clears

**Elemental AE Timer (Seething Zephyr):**

- When Kradon's Seething Zephyr fires, starts a 42-second HUD countdown for the next elemental knockback AE

**Positioning:**

- Fighters at tank spot, everyone else at raid spot

### Player Notes

- Only non-fighters move on curse

---

## Zazun

Setup command: `Set up for Zazun`

### Overview

A fight with a "stop everything" mechanic and curse handling.

### What the Module Does

**Hand of the Great Devourer:**

- When the hand of the Great Devourer looms, the bot targets self, cancels all casting, and pauses OgreBot for 10 seconds

**Curse Handling:**

- When cursed, stops the bot from casting

**Positioning:**

- Fighters at tank spot, everyone else at raid spot

### Player Notes

- Full 10-second pause during the Devourer hand mechanic

---

## Necromunger

Setup is automatic when engaged.

### Overview

A fight with curse call-out mechanics.

### What the Module Does

**Curse Call-Out:**

- Monitors for two specific detriments (main curse and de-level curse)
- When either is detected, calls out "Need a cure curse!" in raid chat
- Resets when both detriments clear

### Player Notes

- Call-out only, no positioning or movement
