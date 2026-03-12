# Underfoot Depths [Raid]

**Expansion:** Sentinel's Fate (Exp 06)

This zone has 8 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Regulas and Regulus](#regulas-and-regulus) | Twin detection, AE-based jousting, teleport handling |
| [Haephaus](#haephaus) | Weapon ready timer with counter |
| [Horraastaas](#horraastaas) | Dot-based positioning, group rotation, AE phase |
| [Taehric Construct](#taehric-construct) | Class-specific group cures, blue phase timing, crystal activation |
| [Xaalax / Yaalax / Zaalax](#xaalax--yaalax--zaalax) | Group-based positioning, fissure avoidance |
| [Vaclaz Released](#vaclaz-released) | Role-based positioning, add management, dual AE timers |
| [Aereon](#aereon) | Vortex avoidance with device-safe positioning |
| [Syfak](#syfak) | Curse self-targeting |

---

## Regulas and Regulus

Setup is automatic when engaged.

### Overview

A twin boss fight with side-specific AE jousting and a teleport transition phase.

### What the Module Does

**Twin Detection:**

- Automatically detects which twin is active and adjusts camp positions accordingly
- When one twin despawns mid-combat, transitions camp to a center position then to the remaining twin

**AE-Based Jousting:**

- Tracks multiple AE types per twin (Pressure Wave, Whirlpool for Regulas; Thunderous Tremor, Rockslide for Regulus)
- Jousts in on the 2nd hit of each AE cycle
- Arcane Vexing (both twins) — resets counter and jousts out after 10 seconds, back in after 32

**Teleport Handling:**

- When teleported to the open area, resets AE counter and moves to the far camp spot

### Player Notes

- AE jousting triggers on the 2nd hit, not the 1st

---

## Haephaus

Setup is automatic when engaged.

### Overview

A fight with a weapon ready countdown timer.

### What the Module Does

**Weapon Ready Timer:**

- When Haephaus announces "Weapon ready in 60 seconds", starts a 63-second HUD countdown
- Tracks weapon count with a persistent counter display

### Player Notes

- Timer and counter display only

---

## Horraastaas

Setup command: `Set up for Horraas`

### Overview

A dot-swapping encounter where groups rotate between "get the dot" and "no dot" positions.

### What the Module Does

**Dot-Based Positioning:**

- When the Horraastaas dot is detected with more than 5 seconds remaining, moves to the safe (no-dot) position
- When not dotted, targets self and jousts out to receive the dot

**Group Rotation:**

- Chat commands `g2 and g3 get the dot` or `g1 and g4 get the dot` send the specified groups to the dot-acquisition position

**AE Phase:**

- On `AE coming` chat command, moves everyone to the no-dot position with a 60-second HUD timer

### Player Notes

- Group rotation is triggered by raid leader chat commands

---

## Taehric Construct

Setup command: `Set up for Construct`

### Overview

A fight with class-specific group cures, a blue phase energy cycle, and crystal activation.

### What the Module Does

**Class-Specific Group Cures:**

- Clerics with the first AE debuff cast their primary group cure
- Shamans with the second AE debuff cast their primary group cure
- Anyone with the third AE debuff casts their secondary group cure

**Blue Phase Timing:**

- When auxiliary energy activates (blue phase starts), starts a 26-second "Blue ends in" HUD timer
- When energy depletes (blue phase ends), starts a 63-second "Blue hits in" HUD timer
- On construct spawn, starts a 90-second initial timer

**Crystal Activation:**

- During blue phase, Mages within 13 meters of a shackling crystal automatically activate it

**Positioning:**

- Priests in groups 1 or 3 get a separate position; everyone else at the raid spot
- During blue phase, everyone moves to the raid spot

### Player Notes

- Uses configured group cure abilities from the Cast Stack

---

## Xaalax / Yaalax / Zaalax

Setup command: `Set up for XYZ`

### Overview

A multi-boss fight with group-based positioning and fissure avoidance.

### What the Module Does

**Group-Based Positioning:**

- Groups are assigned to different positions based on which boss is active (Xaalax, Yaalax, or Zaalax)
- Group 1 gets a dedicated position regardless of which boss is up

**Fissure Avoidance:**

- When fissures form near a player within 25 meters, jousts out to the safe position
- Returns to camp after 12 seconds
- If the fissure target is more than 25 meters away, no movement needed

### Player Notes

- Positions adjust based on which of the three bosses is currently active

---

## Vaclaz Released

Setup command: `Set up for Vaclaz`

### Overview

A fight with role-based positioning, add management via debuff detection, and dual AE timers.

### What the Module Does

**Role-Based Positioning:**

- Priests go to the tank group position
- Mages get a separate position
- Everyone else at the main raid spot

**Add Management:**

- When the Vaclaz add detriment is detected and an untargeted roekillik energymaster exists, moves to the add's location
- Enables AutoTarget with a 20-meter scan radius focused on the energymaster
- Clears targeting when the detriment drops or the add is killed

**Dual AE Timers:**

- Poisonous Wave — 40-second HUD countdown
- Caustic Cloud — 40-second HUD countdown (tracked independently)

### Player Notes

- Add targeting is automatic based on detriment detection

---

## Aereon

Setup is automatic when engaged.

### Overview

A fight with vortex avoidance positioning using the Taaskat Device as a safe zone reference.

### What the Module Does

**Vortex Avoidance:**

- When an Archaic Energy Vortex spawns within 10 meters and no Taaskat Device is nearby, repositions the raid
- Groups 1-4 choose between two positions near the boss, picking whichever is farther from the vortex
- Group 5+ chooses between two positions near the adds
- Triggers on both vortex spawn and device despawn events

### Player Notes

- Stay away from the vortex; the device creates a safe zone

---

## Syfak

Setup is automatic when engaged.

### Overview

A fight with a curse mechanic that requires stopping all actions.

### What the Module Does

**Curse Self-Targeting:**

- While cursed, stops the bot from taking further actions

### Player Notes

- Full action pause during curse duration
