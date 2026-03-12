# Sleeper's Tomb [Raid]

**Expansion:** Destiny of Velious (Exp 07)

This zone has 13 boss encounters with OgreBot automation modules across two sub-zones.

## Available Setups

**Temporal Leap:**

| Boss | Description |
|------|-------------|
| [Master of the Guard](#master-of-the-guard) | Red text joust |
| [Eudoxxus](#eudoxxus) | Ritual damage type response |
| [Paldar](#paldar) | Red text joust with off-tank pattern, curse handling |
| [Ingolf](#ingolf) | Class-based add management |
| [Milas](#milas) | AE timer, red text joust, chronorift add management |

**Unearthed:**

| Boss | Description |
|------|-------------|
| [Gloust](#gloust) | Charm/curse call-out |
| [Drels Ma'Gor](#drels-magor) | Charm/curse call-out, class-based add targeting |
| [Sorrn](#sorrn) | Detriment-based joust |
| [Mazarine](#mazarine) | Positioning with extended range |
| [Silis On'Va](#silis-onva) | Help free mechanic |
| [Ancient Sentinel](#ancient-sentinel) | Smashing machine repositioning, AE timer |
| [Eidolon](#eidolon) | Front/rear positional toggling |
| [Amalgamon](#amalgamon) | Class-based add splitting (mages/scouts) |

---

## Master of the Guard

Setup command: `Set up for Master` (also accepts `Set up for MOTG`)

### Overview

A fight with red text jousting.

### What the Module Does

**Red Text Joust:**

- On ominous crystal announcement, toggles between raid and joust spots

### Player Notes

- Standard two-position toggle joust

---

## Eudoxxus

Setup is automatic when engaged.

### Overview

A fight where the raid must counter specific damage type rituals.

### What the Module Does

**Ritual Response:**

- When Eudoxxus begins the ritual of stone, cancels maintained spells and targets self
- Responds to damage type announcements (Elemental, Noxious, Physical, Arcane) by casting matching class abilities
- HUD displays the required damage type for 10 seconds
- Fighters retarget the boss when the ritual is blocked

### Player Notes

- Correct damage type ability is cast automatically

---

## Paldar

Setup command: `Set up for Paldar`

### Overview

A fight with group-specific jousting and curse handling.

### What the Module Does

**Red Text Joust:**

- On enkindled sentry glow, 56-second HUD timer
- Off-tank fighters (group 2) have a complex two-position alternating joust pattern
- Other groups do a standard joust

**Curse Handling:**

- When cursed, non-off-tank players move to the joust spot and call for cure curse
- Off-tank fighters stay in place and request cure
- Returns to role-appropriate camp spot when cured

**Positioning:**

- Separate spots for tank (group 1), off-tank (group 2 fighter), and raid

### Player Notes

- Off-tank has unique joust pattern separate from the rest of the raid

---

## Ingolf

Setup is automatic when engaged.

### Overview

A fight with class-based add management.

### What the Module Does

**Class-Based Add Targeting:**

- Physical phantasm adds — scouts target and set temp assist
- Arcane phantasm adds — mages and priests target and set temp assist
- Clears targeting when adds despawn

### Player Notes

- Scouts and mages/priests handle different add types

---

## Milas

Setup command: `Set up for Milas`

### Overview

A fight with AE timing, red text jousting, and chronorift add management.

### What the Module Does

**AE Timer:**

- Fiery Breath — 32-second HUD countdown

**Red Text Joust:**

- On explosive force announcement, 65-second HUD timer
- Group 1 fighters alternate between tank and tank joust spots with repositioning waypoints

**Chronorift Add Management:**

- When a Chronorift Entity spawns matching the player's name, that player targets it and disables named combat arts
- Group 2 fighters also target the add
- Clears settings when all adds despawn

### Player Notes

- Tank (group 1) has a separate joust pattern

---

## Gloust

Setup is automatic when engaged.

### Overview

A fight with charm/curse handling.

### What the Module Does

**Charm/Curse Call-Out:**

- When the Gloust charm detriment is detected, calls out for cure curse in raid chat

### Player Notes

- Call-out only, no positioning

---

## Drels Ma'Gor

Setup is automatic when engaged.

### Overview

A fight with charm/curse handling and class-based add targeting.

### What the Module Does

**Charm/Curse Call-Out:**

- When the Drels Ma'Gor charm detriment is detected, calls out for cure curse

**Class-Based Add Targeting:**

- Scouts target abyssal assassin adds
- Mages target dark sorcerer adds

### Player Notes

- Different classes handle different add types

---

## Sorrn

Setup command: `Set up for Sorrn`

### Overview

A fight with detriment-based jousting.

### What the Module Does

**Detriment Joust:**

- When the Sorrn detriment is detected, jousts out and moves to the joust spot
- Fighters disable auto-attack during the joust
- Returns to raid spot when the detriment clears

### Player Notes

- Fighters stop auto-attacking during the detriment phase

---

## Mazarine

Setup command: `Set up for Mazarine`

### Overview

Positioning setup with extended follow range.

### What the Module Does

**Positioning:**

- Sets camp position with extended follow distance (250)

### Player Notes

- Extended leash distance for large arena

---

## Silis On'Va

Setup is automatic when engaged.

### Overview

A fight with an automated help mechanic.

### What the Module Does

**Help Free Mechanic:**

- When a raid member is being crushed by Silis' foot, automatically applies "Help free raidmember" on the boss after a 5-second delay

### Player Notes

- Rescue interaction is fully automated

---

## Ancient Sentinel

Setup is automatic when engaged.

### Overview

A fight with smashing machine repositioning and an AE timer.

### What the Module Does

**Smashing Machine Repositioning:**

- When the machine spawns, calculates which side is closer and moves the camp there
- 55.5-second HUD timer tracks machine spawn cycles

**AE Timer:**

- Velium Blast — 22-second HUD countdown

### Player Notes

- Positions shift based on machine spawn location

---

## Eidolon

Setup is automatic when engaged.

### Overview

A fight with front/rear positional toggling.

### What the Module Does

**Positional Toggling:**

- On tail swipe rear assault, non-fighters move in front of the boss
- On frontal assault, non-fighters move behind the boss
- Toggles are reset on a timer

### Player Notes

- Non-fighters automatically adjust position based on the boss's attack direction

---

## Amalgamon

Setup command: `Set up for Amalgamon`

### Overview

A fight with class-based add splitting for mages and scouts.

### What the Module Does

**Add Management:**

- Air add spawns — mages are split by even/odd ID sorting to two separate positions, target the add, and set temp assist
- Earth add spawns — scouts are split similarly with jousting
- 41-second "Add explodes in" HUD timer
- Clears all settings when adds despawn

**Positioning:**

- Off-tank fighters (not group 1) get a separate position
- Everyone else at the raid spot

### Player Notes

- Mages and scouts are automatically split between add positions
