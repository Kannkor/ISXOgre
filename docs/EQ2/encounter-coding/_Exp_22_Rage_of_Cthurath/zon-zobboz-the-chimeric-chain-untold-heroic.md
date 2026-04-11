# Zon Zobboz: The Chimeric Chain [Untold Heroic]

**Expansion:** Rage of Cthurath (Exp 22)

This zone has 5 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Setup Name | Description |
|------|-----------|-------------|
| [Lord Shomp](#lord-shomp) | Shomp | T21+: add targeting, Timmmberrr, Despotic Decree, Foothold |
| [Kur'Granox](#kurgranox) | KurGranox | Full auto |
| [Vadrak the Vile](#vadrak-the-vile) | Vadrak | Full auto |
| [Xigothid](#xigothid) | Xigothid | Auto face-away, mage-only curing, black hole avoidance |
| [Mozal](#mozal) | Mozal | Mage omni focus clicking, fighter auto-target |

---

## Lord Shomp

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter where the boss becomes immune during a flight phase and stormclouds must be dispersed by group members. At T21+, additional mechanics include add targeting, Timmmberrr cure management, Despotic Decree tracking, and Foothold auto-curing.

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

**T21+ Mechanics:**

- **Add Targeting:** Auto-targets "a nullite foot soldier" at two configurable HP thresholds (default 50% and 20%), with the boss as fallback. Thresholds can be changed via `oc !c -Set_Variable` commands (announced in OC on setup)
- **Timmmberrr:** When "TIMMMBERRR" is detected, disables ALL cures for the group immediately (group curing during Timmmberrr wipes the group). After 4 seconds, checks self for the detriment and announces if present. Re-enables cures after 10 seconds
- **Fallen:** When "You have fallen to the ground" is detected, requests an autocure and announces in OC
- **Despotic Decree:** Monitors for the Despotic Decree detriment on self, announces in OC when gained or removed
- **Foothold:** Auto-cures Foothold using both an autocure request and a cure potion. Skips curing if Timmmberrr is currently active
- **Lord Shomp Faces:** When "Lord Shomp faces" a player, that player announces it in OC

### Player Notes

- Uses the @Healer1 alias to determine which healer stays behind.
- All other group members automatically disperse to handle stormclouds during the flight phase.
- T21+ add HP thresholds are configurable -- OC messages explain how to change them on setup.
- On kill, cures are re-enabled and auto-target is cleared.

---

## Kur'Granox

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter where the boss gains a defensive buff that must be countered by fighters, and non-tank players must position between active vat beams and the boss.

### Requirements

- **Fighter** (casts Bulwark of Order)

### What the Module Does

**Bulwark of Order:**

- When the boss has "Aegis of Bloodshed" active (reduces damage by 50%), fighters automatically cast Bulwark of Order
- 7-second cooldown between casts

**Vat Beam Positioning:**

- Each non-tank player is assigned an order number at setup
- Every 3 seconds, each player scans for their matching vat cube actor with an active yellow beam
- If found, the player repositions 70% of the way from the vat cube toward the boss (standing in the beam)

### Player Notes

- Only fighters take special action for Aegis of Bloodshed. All non-tank players automatically reposition for vat beams.

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

An encounter where the boss casts Tentacle Lash that can only be cured by mages, players must face away during the cast, and black holes spawn that require the group to reposition to safe spots.

### Requirements

- **Mage** (only class that can cure Tentacle Lash)
- **Fighter** (handles black hole repositioning)

### What the Module Does

**Mage-Only Curing:**

- All curing is disabled for non-mages -- only mages can cure Tentacle Lash
- When a player gets Tentacle Lash, a cure request is sent specifically to mages

**Face Away Mechanic:**

- NPC Cast Monitoring detects when the boss begins casting Tentacle Lash
- All players auto-target themselves (to stop targeting the boss)
- The module repeatedly turns each character to face away from the boss for the duration of the cast
- When the cast ends, targeting is restored

**Black Hole Avoidance:**

- When a "boss_03_black_hole" spawns near the group's current camp spot, the fighter finds the next safe joust spot from a list of 25 predefined positions
- A spot is considered safe if it is more than 5 meters from all existing black holes
- The entire group is repositioned to the new safe spot

### Player Notes

- Automated face-away mechanic prevents Tentacle Lash application.
- All curing for non-mages is re-enabled when the boss dies.
- Black hole repositioning is fully automatic.

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
