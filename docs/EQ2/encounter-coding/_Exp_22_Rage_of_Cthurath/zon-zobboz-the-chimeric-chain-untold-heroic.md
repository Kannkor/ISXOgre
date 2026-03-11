# Zon Zobboz: The Chimeric Chain [Untold Heroic]

**Expansion:** Rage of Cthurath (Exp 22)

This zone has 5 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Setup Name | Description |
|------|-----------|-------------|
| [Lord Shomp](#lord-shomp) | Lord Shomp | Stormcloud dispelling during flight phase |
| [Kur'Granox](#kurgranox) | Kur'Granox | Full auto |
| [Vadrak the Vile](#vadrak-the-vile) | Vadrak | Full auto |
| [Xigothid](#xigothid) | Xigothid | Auto face-away, mage-only curing |
| [Mozal](#mozal) | Mozal | Mage omni focus clicking, fighter auto-target |

---

## Lord Shomp

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter where the boss becomes immune during a flight phase and stormclouds must be dispersed by group members.

### Requirements

- Uses the @Healer1 alias to exempt one healer from cloud duty

### What the Module Does

**Flight Phase / Stormcloud Dispelling:**

- When the boss gains its flight immunity buff, each group member (except @Healer1) is assigned a specific stormcloud location via the flag system
- Each member travels to their assigned stormcloud and uses dispel abilities on it
- If the assigned cloud is not present, the player moves to a secondary location to scan, and if still not found, picks a random cloud to help with

**Role Assignment:**

- The @Healer1 alias holder stays behind and does not participate in stormcloud dispelling
- All other group members are assigned numbered positions

### Player Notes

- Uses the @Healer1 alias to determine which healer stays behind.
- All other group members automatically disperse to handle stormclouds during the flight phase.

---

## Kur'Granox

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter where the boss gains a defensive buff that must be countered by fighters.

### Requirements

- **Fighter** (casts Bulwark of Order)

### What the Module Does

**Bulwark of Order:**

- When the boss has "Aegis of Bloodshed" active (reduces damage by 50%), fighters automatically cast Bulwark of Order
- 7-second cooldown between casts

### Player Notes

- Only fighters take special action. The rest of the group fights normally.

---

## Vadrak the Vile

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter with frontal assault dodging and gamma blast positioning mechanics.

### Requirements

- **Guardian**, **Fighter**

### What the Module Does

**Frontal Assault Avoidance:**

- When the boss announces an irradiated frontal assault, fighters move behind the boss at distance 5 and non-fighters behind at distance 2
- Everyone returns to normal positions after the assault completes

**Gamma Blast Positioning:**

- When the boss announces which position can absorb the blast, the module:
    - Moves fighters to a tank joust spot
    - Determines group order based on position from the tank
    - Players at or beyond the required position move to a far joust spot

**Setup:**

- Casts Focused Offensive (guardian) and Singular Focus (all) targeting the boss
- Enables dynamic ignore of PBAoE for all

### Player Notes

- Fully automated frontal assault dodging and gamma blast position handling.
- Focused Offensive and Singular Focus are canceled when the boss dies.

---

## Xigothid

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter where the boss casts Tentacle Lash that can only be cured by mages, and players must face away during the cast.

### Requirements

- **Mage** (only class that can cure Tentacle Lash)

### What the Module Does

**Mage-Only Curing:**

- Priest curing is disabled for everyone -- only mages can cure Tentacle Lash
- When a player gets Tentacle Lash, a cure request is sent specifically to mages

**Face Away Mechanic:**

- NPC Cast Monitoring detects when the boss begins casting Tentacle Lash
- All players auto-target themselves (to stop targeting the boss)
- The module repeatedly turns each character to face away from the boss for the duration of the cast
- When the cast ends, targeting is restored

### Player Notes

- Automated face-away mechanic prevents Tentacle Lash application.
- Priest curing is re-enabled when the boss dies.

---

## Mozal

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter where mages must interact with an omni focus object during the fight while fighters handle adds.

### Requirements

- **Mage** (clicks omni focus object)
- **Fighter** (auto-targets adds)

### What the Module Does

**Omni Focus Clicking:**

- Mages are automatically moved to the omni focus object and click it repeatedly
- After clicking, they return to their camp spot
- Done on a timer to avoid spamming

**Auto-Target:**

- Fighters auto-target "eyes without a face" (adds) and the boss

### Player Notes

- Mages automatically interact with the omni focus object during the fight.
