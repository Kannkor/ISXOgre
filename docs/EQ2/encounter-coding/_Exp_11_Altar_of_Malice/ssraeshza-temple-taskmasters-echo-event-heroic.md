# Ssraeshza Temple: Taskmaster's Echo [Event Heroic]

**Expansion:** Altar of Malice (Exp 11)

This zone has 2 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Echo of Mikazha](#echo-of-mikazha) | Portal tube mechanics, moonbeam targeting |
| [Revenant Sha'Kaz](#revenant-shakaz) | Archetype spread positioning, explosion joust for scouts |

---

## Echo of Mikazha

Setup command: `Set up for Echo` (also accepts `Set up for Mikazha`)

### Overview

A fight with portal tube mechanics and moonbeam targeting.

### What the Module Does

**Moonbeam Targeting:**

- When targeted by the taskmaster, non-fighters move to an assigned portal position (one of 6 positions based on group ordering)
- Once the portal disperses the moon's energy and the Reprimand detriment clears, returns to normal position
- Retries return every second if the detriment hasn't cleared yet

**Add Portal Mechanic:**

- When Mikazha sends adds through portals, non-fighters move into tube positions for 16 seconds, then return

### Player Notes

- Each group member gets a unique portal position based on their sort order

---

## Revenant Sha'Kaz

Setup command: `Set up for ShaKaz` (also accepts `Set up for Sha'Kaz` or `Set up for Revenant`)

### Overview

A fight with archetype-based spread positioning and an explosion curse that scouts must joust away from.

### What the Module Does

**Spread Positioning:**

- Assigns 6 positions based on archetype (Tank, Scout x2, Mage, Priest x2)

**Explosion Joust:**

- Monitors the Countdown to Explosion curse
- When duration drops below 4 seconds, scouts automatically joust out
- When the curse clears, scouts joust back in

### Player Notes

- Only scouts need to joust for the explosion mechanic
