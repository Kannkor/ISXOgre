# Ykesha's Inner Stronghold [Raid]

**Expansion:** The Shadow Odyssey (Exp 05)

This zone has 3 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Ykesha](#ykesha) | Curse item usage, port detection alert |
| [Tyrannus the Dark](#tyrannus-the-dark) | Debuff-triggered add targeting |
| [Field General Uktap](#field-general-uktap) | Curse-triggered sapper targeting |

---

## Ykesha

Setup is automatic when engaged.

### Overview

A fight with a curse debuff requiring item usage and a teleport detection mechanic.

### What the Module Does

**Warbeads Usage:**

- When "Ykesha's Warcurse" is detected, automatically uses the "Ykeshan Warbeads" item

**Port Detection:**

- When teleported to the port area, announces to the raid
- Resets when the player returns to the main corridors

### Player Notes

- Requires "Ykeshan Warbeads" inventory item
- Port handling is alert-only (not automated)

---

## Tyrannus the Dark

Setup command: `Set up for Tyrannus the Dark`

### Overview

A fight where a debuff requires killing a specific add.

### What the Module Does

**Debuff-Triggered Add Targeting:**

- When "Purposeful Resolve" debuff is detected, forces targeting to "an unstable minion" if one exists within 30 meters
- Clears targeting when the debuff drops or the add is killed

### Player Notes

- Add targeting is automatic based on debuff detection

---

## Field General Uktap

Setup command: `Set up for Field General Uktap`

### Overview

A fight where a curse requires killing a sapper add.

### What the Module Does

**Curse-Triggered Sapper Targeting:**

- When the "Acute Vision" curse is detected, forces targeting to "a ykeshan sapper" if one exists
- Announces to the raid that the character is cursed and targeting the sapper
- Clears targeting when the curse drops

### Player Notes

- Sapper targeting is automatic based on curse detection
