# Accursed Sanctum [Raid]

**Expansion:** Tears of Veeshan (Exp 10)

This zone has 10 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Accursed Custodian](#accursed-custodian) | Rift spawn positioning |
| [Adherent Custodian](#adherent-custodian) | Rune glow timers, architect add tracking |
| [Subsistent Custodian](#subsistent-custodian) | Rune storm / pitfall avoidance positioning |
| [Kaasssrelik the Afflicted](#kaasssrelik-the-afflicted) | Volatile slitherer explosion timer |
| [A Protective Custodian](#a-protective-custodian) | Add management by guild tag, verse stack positioning |
| [Toxin Sisters](#toxin-sisters) | Tank swap mechanic by class request |
| [Legionnaire D'rin](#legionnaire-drin) | Positioning |
| [Sacrificer Buran](#sacrificer-buran) | Positioning |
| [Matri Marn](#matri-marn) | Noxious sludge avoidance, healing totem targeting |
| [The Crumbling Emperor](#the-crumbling-emperor) | Room-on-fire mechanic, knockback timer |

---

## Accursed Custodian

Setup command: `Set up for Accursed`

### Overview

A fight where accursed rifts spawn and the raid must move to the opposite side.

### What the Module Does

**Rift Positioning:**

- When an accursed rift spawns, determines which side it is closest to and moves the raid to the opposite position

### Player Notes

- Two position sets are used for the back-and-forth movement

---

## Adherent Custodian

Setup is automatic when engaged.

### Overview

A fight with rune glow mechanics and architect add spawns.

### What the Module Does

**HUD Timers:**

- Rune glow intensity countdown (62-second timer)
- Custodial architect add spawn countdown (120-second timer)

### Player Notes

- Timer-only tracking with no positioning automation

---

## Subsistent Custodian

Setup command: `Set up for Subsistent`

### Overview

A fight where the raid must avoid Visceral Rune Storms and unstable pitfalls.

### What the Module Does

**Hazard Avoidance:**

- Maintains two campspot positions
- When a rune storm or pitfall spawns/despawns, dynamically moves the raid to whichever position is farther from the hazard

### Player Notes

- The module automatically repositions when hazards appear within 10 meters

---

## Kaasssrelik the Afflicted

Setup is automatic when engaged.

### Overview

A fight with volatile slitherer adds that explode.

### What the Module Does

**Explosion Timer:**

- When volatile slitherers spawn, displays a 38-second countdown HUD until they explode

### Player Notes

- Timer-only tracking

---

## A Protective Custodian

Setup command: `Set up for Protector`

### Overview

A fight with add management based on the add's guild tag and verse detriment stacking.

### What the Module Does

**Add Management:**

- Projecting Servant: kill near the boss (HUD notification)
- Perpetual Servant: kill far from the boss

**Verse Stack Positioning:**

- Monitors Red Destructive Verses and Blue Waning Verses detriment stacks
- At 3+ Red stacks, moves to the far (Blue) spot
- At 3+ Blue stacks, moves to the close (Red) spot
- GetClose detriment forces return to the close spot

### Player Notes

- Positioning is automatic based on detriment stack counts

---

## Toxin Sisters

Setup command: `Set up for Sisters`

### Overview

A tank swap fight where the sisters demand specific class tanks.

### What the Module Does

**Tank Swap Mechanic:**

- Listens for the sisters requesting a specific class to tank
- If your class matches the request, you target that sister and enable offensive actions
- If your class does not match, you stop attacking
- All fighters cast Recapture during swaps
- HUD tracks which sister wants which class and a 38-second swap timer

### Player Notes

- Fighters automatically manage offensive actions based on the class request

---

## Legionnaire D'rin

Setup command: `Set up for Legionnaire`

### Overview

A fight with curse mechanics and circle avoidance.

### What the Module Does

**Positioning:**

- Sets a single campspot for the raid

### Player Notes

- Avoid circles on red text
- Three different curse types have corresponding positions (documented in the module comments)

---

## Sacrificer Buran

Setup command: `Set up for Buran`

### Overview

A positioning-only setup.

### What the Module Does

**Positioning:**

- Sets a single campspot for the raid

### Player Notes

- Positioning only, no mechanic automation

---

## Matri Marn

Setup command: `Set up for Matri`

### Overview

A fight with noxious sludge avoidance and healing totem interaction.

### What the Module Does

**Sludge Avoidance:**

- Maintains 4 campspot positions
- When Noxious Sludge spawns, scans all sludge locations, marks positions within 12 meters as unsafe, and moves the raid to the first clean position

**Healing Totem:**

- When a Healing Totem spawns, players without trauma temporarily disable defensive actions and auto-target the totem

### Player Notes

- The module automatically finds safe positions as sludge pools appear

---

## The Crumbling Emperor

Setup command: `Set up for Emperor`

### Overview

A complex fight with a room-on-fire mechanic and knockback timing.

### What the Module Does

**Room-on-Fire Mechanic:**

- Four pairs of inner/outer campspot positions indexed by raid group number
- Detects whether the outer rooms or center room catches fire
- After a timed delay (25 seconds for outer fire, 10 seconds for center fire), swaps between inner and outer positions

**Knockback Timer:**

- HUD shows Torrent of the Ancients countdown (41-second timer)

**Special Click:**

- Mages, scouts, and fighters can click invisible cubes during the fight

### Player Notes

- Cast while moving is enabled for this fight
- Raid group positioning is automatic based on your group number
