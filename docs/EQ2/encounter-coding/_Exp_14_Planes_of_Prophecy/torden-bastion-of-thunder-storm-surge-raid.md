# Torden, Bastion of Thunder: Storm Surge [Raid]

**Expansion:** Planes of Prophecy (Exp 14)

This zone has 3 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Valbrand and Thangbrand](#valbrand-and-thangbrand) | Auto-dispelling |
| [Emmerik Skyfury](#emmerik-skyfury) | Detriment cancellation, NPC protection tracking HUD |
| [Eindride Icestorm](#eindride-icestorm) | Add spawn timer HUD |

---

## Valbrand and Thangbrand

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a dispellable buff on the bosses.

### What the Module Does

**Auto-Dispelling:**

- Enchanters automatically dispel both Valbrand and Thangbrand when the appropriate buff is detected

### Player Notes

- Dispelling is handled automatically

---

## Emmerik Skyfury

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with charge detrimentals and boss protection tracking.

### What the Module Does

**Detriment Cancellation:**

- On setup, all characters cancel Electrical Charge and Atmospheric Charge detrimentals

**NPC Protection Tracking:**

- HUD displays which protection (Electrical or Atmospheric) each boss currently has, updated every 5 seconds

### Player Notes

- Use "set up for" to have all characters cancel their charge detrimentals

---

## Eindride Icestorm

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with add spawn tracking.

### What the Module Does

**Add Spawn Timer:**

- HUD displays a 35-second countdown when a Vann militis add spawns, showing when the next add will appear

### Player Notes

- The HUD timer helps coordinate add management
