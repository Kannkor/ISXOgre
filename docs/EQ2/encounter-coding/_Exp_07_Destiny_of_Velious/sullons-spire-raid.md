# Sullon's Spire [Raid]

**Expansion:** Destiny of Velious (Exp 07)

This zone has 5 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Ragebourne Gregor Haldane](#ragebourne-gregor-haldane) | Memwipe timer, veteran debuff mechanic |
| [Hragdold](#hragdold) | Add spawn timer |
| [Mrogr](#mrogr) | Totem of silence avoidance, disease cure item use |
| [Aaranae](#aaranae) | Positioning only |
| [Sullon Zek](#sullon-zek) | AE timer, priest-specific positioning |

---

## Ragebourne Gregor Haldane

Setup command: `Set up for Ragebourne`

### Overview

A fight with a memwipe timer and a veteran debuff mechanic.

### What the Module Does

**Memwipe Timer:**

- When Ragebourne says "My rage is without limits!", starts a 52-second HUD countdown

**Veteran Debuff Mechanic:**

- Scans for multiple copies of Ragebourne and assigns targets based on raid group
- Groups 1/3 target the lower-ID copy; groups 2/4 target the higher-ID copy
- Alternates between shamans and clerics for the debuff application

**Positioning:**

- Scouts get a separate position; everyone else at the raid spot

### Player Notes

- Multi-copy targeting is handled automatically by raid group

---

## Hragdold

Setup command: `Set up for Hragdold`

### Overview

A fight with add spawn tracking.

### What the Module Does

**Add Spawn Timer:**

- When an ironclaw priest add spawns, starts a 120-second HUD countdown for the next wave

### Player Notes

- Timer-only module with positioning

---

## Mrogr

Setup command: `Set up for Mrogr`

### Overview

A fight with totem avoidance and disease curing via inventory item.

### What the Module Does

**Totem of Silence Avoidance:**

- When a totem of silence spawns, compares distances and moves the camp to whichever spot is farther from the totem

**Disease Cure Item Use:**

- When the Mrogr disease detriment is detected, automatically uses the "diseased pox shard" inventory item to cure it

### Player Notes

- Requires "diseased pox shard" inventory item

---

## Aaranae

Setup command: `Set up for Aaranae`

### Overview

Positioning setup only.

### What the Module Does

**Positioning:**

- Sets camp position for the encounter

### Player Notes

- No automated mechanics beyond positioning

---

## Sullon Zek

Setup command: `Set up for Sullon`

### Overview

A fight with an AE timer and priest-specific positioning.

### What the Module Does

**AE Timer:**

- Rageslam — 45-second HUD countdown

**Positioning:**

- Priests in groups 1/2/3 go to a separate priest position
- Everyone else at the raid spot

### Player Notes

- Priests are positioned separately from the rest of the raid
