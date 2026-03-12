# The Fabled Nizara, City of the Nayad [Heroic]

**Expansion:** Terrors of Thalumbra (Exp 12)

This zone has 3 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [K'huthas](#khuthas) | Freeze joust, auto-target smallest copy |
| [Sshi'vaez the Studious](#sshivaez-the-studious) | Archetype book auto-clicking for curse cure |
| [Dutheris, the Dying Dark](#dutheris-the-dying-dark) | Auto defensive abilities on AE |

---

## K'huthas

Setup command: `Set up for Khuthas`

Additional options:

- `Set up for Khuthas Auto` -- full auto with movement
- `Set up for Khuthas targeting` -- targeting only, no movement

### Overview

A fight where K'huthas splits into multiple copies and the group must target the smallest one, while handling freeze mechanics.

### What the Module Does

**Auto-Target Smallest Copy:**

- When K'huthas actors spawn, fighters automatically target the copy with the smallest collision scale (the correct target)

**Freeze Joust (Fighters):**

- When a fighter gets the Freezing Storm detriment, they are moved to the group spot (away from tank spot)
- After 11 seconds, they return to the tank spot

**Setup Actions:**

- Enables assist mode and disables auto-targeting for all characters
- On kill, cancels Singular Focus and re-enables PBAoE and encounter nukes

### Player Notes

- The "targeting" setup variant disables movement (useful if you want to handle positioning manually)

---

## Sshi'vaez the Studious

Setup is automatic when engaged.

### Overview

A fight where a curse can only be removed by clicking the correct archetype-specific book.

### What the Module Does

**Book Cure:**

- When the curse fires, automatically determines which book to click based on your archetype:
    - Fighters: Book of Sun
    - Priests: Book of Spirit
    - Mages: Book of Mind
    - Scouts: Book of Moon
- If the matching book is within 10 meters, automatically double-clicks it

### Player Notes

- If you are not close enough to the book, move near it and press `Special_ZoneSpecific` in MCP to trigger the click manually

---

## Dutheris, the Dying Dark

Setup is automatic when engaged.

### Overview

A fight with a dangerous AE attack that requires defensive abilities.

### What the Module Does

**AE Avoidance:**

- When the AE warning fires, Bards automatically cast Bladedance and Druids automatically cast Tortoise Shell

### Player Notes

- Only Bards and Druids have automated defensive responses for this mechanic
