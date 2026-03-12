# F.S. Distillery: Stowaways [Event Heroic]

**Expansion:** Altar of Malice (Exp 11)

This zone has 3 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Oofgoof Doof](#oofgoof-doof) | Targeted joust on Bulk Breaker |
| [Sir Wharfie](#sir-wharfie) | Archetype positioning, frontal attack handling, package delivery |
| [Zaxfalump](#zaxfalump) | AE warning joust, bard box running |

---

## Oofgoof Doof

Setup command: `Set up for Oofgoof` (also accepts `Set up for Doof`)

### Overview

A fight with a targeted attack that requires jousting away.

### What the Module Does

**Targeted Joust:**

- When a player is targeted by Oofgoof, fighters receive a warning message
- All players automatically move 14 meters away and return after 20 seconds

### Player Notes

- Positioned near zone-in

---

## Sir Wharfie

Setup command: `Set up for Sir` (also accepts `Set up for Wharfie`)

### Overview

A fight with archetype-based positioning, frontal attack avoidance, and add management phases.

### What the Module Does

**Archetype-Based Positioning:**

- Assigns separate positions for tank, scouts, priests, mages, and overflow based on class

**Frontal Attack Handling:**

- When Wharfie stops to attack everyone in front, fighters automatically reposition behind

**Package Delivery Phase:**

- On "Package Delivered!" fighters target self and PBAoE abilities are disabled
- When the kill phase begins ("uh oh!"), AE abilities are re-enabled and fighters target Wharfie

### Player Notes

- Player still handles boxes and barrels manually

---

## Zaxfalump

Setup command: `Set up for Zaxfalump`

### Overview

A fight with AE warning circles and a summoning circle phase where a bard runs boxes.

### What the Module Does

**AE Warning Joust:**

- When AE Warning Areas spawn, automatically moves to whichever of two positions is farther away

**Bard Box Running:**

- During the summoning circle phase, a bard is automated to:
    - Navigate to 4 box locations, pick up crates
    - Carry each crate to the corresponding summoning circle
    - Place the crate via mouse interaction
- Fighter campspots are removed during the summoning circle phase

### Player Notes

- A bard is required for the automated box running mechanic
- Two position sets are used for jousting between AE circles
