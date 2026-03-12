# Ossuary: Sanguine Fountains [Heroic]

**Expansion:** Altar of Malice (Exp 11)

This zone has 4 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [The Sanguine Fiend](#the-sanguine-fiend) | Mage auto-dispel, red text joust |
| [D'Nari the Bone Sculptor](#dnari-the-bone-sculptor) | Add spawn joust |
| [Ritualist K'Deru](#ritualist-kderu) | Center positioning, skull tag |
| [The Embodiment of Gore](#the-embodiment-of-gore) | Mage auto-dispel |

---

## The Sanguine Fiend

Setup is automatic when engaged.

### Overview

A fight with a bone hardening buff that must be dispelled and red text jousting mechanics.

### What the Module Does

**Mage Auto-Dispel:**

- Mages automatically dispel the Harden Bones buff from The Sanguine Fiend when detected

**Red Text Joust:**

- On any splinter announcement (close, front, far, or behind), automatically jousts the group out

### Player Notes

- Absorb Magic is automatically disabled from cast stack when entering the zone so dispels are only used by the auto-dispel logic

---

## D'Nari the Bone Sculptor

Setup command: `Set up for DNari` (also accepts `Set up for D'Nari`)

### Overview

A fight with adds that require the group to move to the opposite side of the room.

### What the Module Does

**Add Spawn Joust:**

- When The Touch of Death add spawns, jousts the group out and moves to the opposite side based on the add's proximity to the current position
- Separate tank and group spots are maintained on each side

### Player Notes

- Two position sets are used for the left/right movement

---

## Ritualist K'Deru

Setup command: `Set up for KDeru` (also accepts `Set up for K'Deru` or `Set up for Ritualist`)

### Overview

A fight where the group positions in the center of the room.

### What the Module Does

**Center Positioning:**

- Moves everyone to the center of the room
- Fighters tag the target with a skull marker

### Player Notes

- Mages with interrupts enabled should be able to stun from the center position

---

## The Embodiment of Gore

Setup is automatic when engaged.

### Overview

A fight with an enriched blood buff that must be dispelled.

### What the Module Does

**Mage Auto-Dispel:**

- Mages automatically dispel the Enriched Blood buff from The Embodiment of Gore when detected

### Player Notes

- Same auto-dispel pattern as The Sanguine Fiend
