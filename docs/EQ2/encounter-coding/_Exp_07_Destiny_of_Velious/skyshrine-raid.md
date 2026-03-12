# Skyshrine [Raid]

**Expansion:** Destiny of Velious (Exp 07)

This zone has 8 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Dagarn](#dagarn) | Red text joust (toxic spores) |
| [Ikatiar](#ikatiar) | Stare joust, three-spot goo avoidance |
| [Dozekar](#dozekar) | Red text joust, assassin alert |
| [Malteor](#malteor) | Red text joust, time-phased elemental add targeting |
| [Sevalor](#sevalor) | Role-aware red text joust (tank/off-tank/raid) |
| [Balor the Primeval](#balor-the-primeval) | Red text joust, Soulsand Crystal item use |
| [Tel'koran](#telkoran) | Targeted death mechanic with feign death |
| [Blazeclaw](#blazeclaw) | Curse self-targeting |

---

## Dagarn

Setup command: `Set up for Dagarn`

### Overview

A fight with a red text joust on toxic spore emissions.

### What the Module Does

**Red Text Joust:**

- On toxic spores announcement, toggles camp spot between raid and joust positions

### Player Notes

- Standard two-position toggle joust

---

## Ikatiar

Setup command: `Set up for Ikatiar`

### Overview

A fight with a stare joust and intelligent goo avoidance using three positions.

### What the Module Does

**Stare Joust:**

- When Ikatiar stares at the raid, jousts out and announces to the group

**Goo Avoidance:**

- Three camp positions available
- When a goo spawns, calculates which position is farthest from both the new goo and the previous goo
- Moves the raid to the safest position
- Tracks previous goo location for hard mode three-spot avoidance

### Player Notes

- Positions rotate based on goo spawn locations

---

## Dozekar

Setup command: `Set up for Dozekar`

### Overview

A fight with a red text joust and assassin alert.

### What the Module Does

**Red Text Joust:**

- On inner rage glow announcement, toggles between raid and joust spots

**Assassin Alert:**

- When an infernal assassin moves toward the player, jousts out and announces to the group

### Player Notes

- Standard joust with assassin awareness

---

## Malteor

Setup command: `Set up for Malteor`

### Overview

A fight with red text jousting and time-phased elemental add management.

### What the Module Does

**Red Text Joust:**

- On immolation announcement, toggles between raid and joust spots

**Time-Phased Elemental Add Targeting:**

- When the infernal conundrum detriment is detected and a time-phased elemental exists, forces targeting of the elemental
- Disables defensive abilities and ignores assist during the add phase
- If no elemental exists, cancels the effect

### Player Notes

- Add targeting is automatic when the detriment is active

---

## Sevalor

Setup command: `Set up for Sevalor`

### Overview

A fight with role-aware red text jousting.

### What the Module Does

**Role-Aware Joust:**

- On toxic force thrashing announcement, each role jousts to a different position:
    - Group 1 fighters go to the tank joust spot
    - Other fighters go to the off-tank joust spot
    - Everyone else goes to the raid joust spot

### Player Notes

- Three separate joust destinations based on role

---

## Balor the Primeval

Setup command: `Set up for Balor`

### Overview

A fight with red text jousting and automated item use.

### What the Module Does

**Red Text Joust:**

- On destructive power glow announcement, toggles between raid and joust spots

**Soulsand Crystal:**

- When Balor gains strength from his Soul Barrier, all characters use the "Soulsand Crystal" inventory item

### Player Notes

- Requires "Soulsand Crystal" inventory item

---

## Tel'koran

Setup is automatic when engaged.

### Overview

A fight with a targeted death mechanic.

### What the Module Does

**Death Mechanic:**

- When Tel'koran targets a specific player for death, that player casts Recapture and Feign Death
- Disables offensive abilities for 12 seconds, then stands back up

### Player Notes

- Only the targeted player feigns death

---

## Blazeclaw

Setup is automatic when engaged.

### Overview

A fight with a dangerous curse that requires self-targeting.

### What the Module Does

**Curse Self-Targeting:**

- While cursed, stops all actions and targets self to prevent harmful curse effects

### Player Notes

- Full action stop during curse duration
