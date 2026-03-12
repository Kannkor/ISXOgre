# Kralet Penumbra: The Hive Mind [Raid]

**Expansion:** Terrors of Thalumbra (Exp 12)

This zone has 7 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Karith'Ta](#karithta) | Paralyze detection, coercer auto-charm, fighter orb positioning |
| [General Area](#general-area) | Auto curse calling for cross-session curing |
| [The Psionist](#the-psionist) | Well of Power water rotation for bards/enchanters |
| [Sath'Oprusk](#sathoprousk) | Bends joust, vulnerability/immunity cycling, staff usage |
| [The Polliwog](#the-polliwog) | Pox/plague curse joust with auto-cure calling |
| [Ynonngozzz'Koolbh](#ynonngozzzkoolbh) | Complex group positioning, cloud of vile crouch |
| [Kraletus](#kraletus) | Charm rotation, mental breach cure rotation, immunity tracking |

---

## Karith'Ta

Setup command: `Set up for KarithTa`

### Overview

A fight with paralyze detection, coercer auto-charm on adds, and fighter repositioning based on invisible orbs.

### What the Module Does

**Paralyze Detection:**

- When the Paralyze detriment is detected, disables offensive combat and campspot, announces via IRC
- When Paralyze fades, re-enables everything

**Coercer Auto-Charm:**

- When Telekinetic Stasis spawns, coercers automatically target and charm it

**Orb-Based Fighter Positioning:**

- When invisible orbs spawn, fighters reposition their camp spot near the orb

### Player Notes

- All classes share the same raid spot (no separate tank positioning)

---

## General Area

Setup is automatic.

### Overview

Auto curse detection for the Charrid the Mindwarper area.

### What the Module Does

**Auto Curse Calling:**

- Monitors for the Enslave Adversary curse
- When detected, broadcasts a cross-session auto-cure request
- Clears targeting if the cursed character is targeting a PC when the curse fades

### Player Notes

- The IRC relay system must be active for cross-session curing

---

## The Psionist

Setup command: `Set up for Psionist`

### Overview

A fight with a Well of Power water mechanic handled by bards and enchanters.

### What the Module Does

**Well of Power Water Rotation:**

- Bards activate immediately when the Well spawns; enchanters have a 45-second delay
- Characters with too many Tunnel Visioned stacks (over 15) stop participating
- Participation is staggered by raid group number based on the Well's stack count
- Characters automatically take water from the Well and dump it at a Wall Drain

**Behemoth HUD:**

- When any Behemoth add spawns, a 45-second countdown timer is displayed

### Player Notes

- You may want to turn raid options off unless you are in a bot raid

---

## Sath'Oprusk

Setup command: `Set up for Sath`

Additional options:

- `Set up for auto Sath` -- full auto mode with defensive cycling
- `Set up for guardian Sath` -- guardian auto mode (raid leader only)

### Overview

A fight with alternating vulnerability and immunity phases, requiring jousting and timed item/ability usage.

### What the Module Does

**The Bends Joust:**

- When the Bends detriment is detected, moves to the joust spot
- Returns to camp when it fades

**Vulnerability Phase:**

- Re-enables cast stack abilities, casts Temporal Mimicry
- Displays a 20-second HUD countdown until immunity returns

**Immunity Phase:**

- Disables cast stack abilities
- In auto modes, schedules defensive ability cycling and staff usage after the immunity timer

### Player Notes

- Characters with "a Penumbra Captivator's Staff" in inventory are placed at the joust spot
- Setup disables named CA cast stack, force named CA tab, and Temporal Mimicry initially

---

## The Polliwog

Setup command: `Set up for Polliwog`

### Overview

A fight with a curse that requires jousting away from the group.

### What the Module Does

**Curse Joust:**

- When hit by Bring About a Pox/Plague/Affliction, the character jousts to the designated spot
- Fighters additionally send cross-session auto-cure requests
- When curses clear, returns to normal camp position

**Indisposition HUD:**

- Displays countdown timers for the next Indisposition mechanic (13-second and 28-second timers)

### Player Notes

- Fighters have a separate position with an 8-second anti-spam timer on cure requests

---

## Ynonngozzz'Koolbh

Setup command: `Set up for Koolbh` (also accepts `Set up for Ynonngozzz`)

### Overview

A fight with precise per-player positioning by raid group and archetype, plus a crouch mechanic.

### What the Module Does

**Complex Positioning:**

- Each player is assigned a specific camp spot based on their raid group and class archetype
- Groups 1 and 4 (tank groups) have 5 slots; Groups 2 and 3 have 6 slots
- Bards, shamans, druids/clerics, enchanters, and mages each have designated slot positions

**Cloud of Vile:**

- When a noxious gas cloud surrounds your head, the module broadcasts a cross-session alert
- All characters automatically crouch, then jump back up 2 seconds later

**Mindslurper HUD:**

- When a Mindslurper spawns, a 45-second countdown timer is displayed

### Player Notes

- Groups 1(MT) and 4(OT) have 5 slots, Groups 2 and 3 have 6 slots
- Players are spaced 7 meters apart on the X axis

---

## Kraletus

!!! warning "Work in Progress"
    This encounter module is still under development. If you raid for real, turn OFF raid options.

Setup command: `Set up for Kraletus`

### Overview

A complex fight with a charm rotation system, mental breach cure rotation, and immunity phase tracking.

### What the Module Does

**Charm Rotation:**

- Builds a rotation of charm-capable classes (Coercer, Troubador, Warden/Fury, Necromancer)
- As Coerced Gnemlins and Dhalgars spawn, charmers take turns targeting and charming them
- Odd-numbered charmers handle Gnemlins, even-numbered handle Dhalgars

**Mental Breach Cure Rotation:**

- Monitors for the Mental Breach detriment
- When the duration drops below 15 seconds, jousts to the joust spot
- Below 10 seconds, broadcasts a cure request to the next curer in rotation
- The cure rotation system handles failover -- if a curer can't cure, it passes to the next one

**Immunity Tracking:**

- Tracks when Kraletus goes immune and non-immune
- Displays status changes to the group

**Chanter Spawn Waypoints:**

- When Penumbran Chanters spawn, sets waypoints for the raid

### Player Notes

- Setup casts Singular Focus and dismisses non-released coercer pets
- The charm rotation requires multiple charm-capable classes in the raid
