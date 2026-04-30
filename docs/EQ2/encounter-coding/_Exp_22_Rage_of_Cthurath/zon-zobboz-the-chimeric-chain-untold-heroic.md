# Zon Zobboz: The Chimeric Chain [Untold Heroic]

**Expansion:** Rage of Cthurath (Exp 22)

This zone has 5 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Setup Name | Description |
|------|-----------|-------------|
| [Lord Shomp](#lord-shomp) | Shomp | Stormcloud dispelling, T21+: add targeting, Timmmberrr, Despotic Decree, Foothold |
| [Kur'Granox](#kurgranox) | KurGranox | Fighter Bulwark of Order, vat beam positioning |
| [Vadrak the Vile](#vadrak-the-vile) | Vadrak | Frontal assault dodging, gamma blast positioning |
| [Xigothid](#xigothid) | Xigothid | NPC-cast-triggered face-away, mage-only curing, black hole avoidance |
| [Mozal](#mozal) | Mozal | Mage omni focus clicking, fighter auto-target |

---

## Lord Shomp

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter where the boss becomes immune during a flight phase and stormclouds must be dispersed by group members. At T21+, additional mechanics include add targeting, Timmmberrr cure management, Despotic Decree tracking, and Foothold auto-curing.

### Requirements

- Uses the @Healer1 alias to exempt one healer from stormcloud duty

### What the Module Does

**Flight Phase / Stormcloud Dispelling:**

- When the boss gains its flight immunity buff ("Flight of the Nullite"), each group member (except @Healer1) is assigned a specific stormcloud location via the flag system
- Each member travels to their assigned stormcloud dispell position and uses dispel abilities on it until the cloud is gone or the flight phase ends
- If the assigned cloud is not present at the expected location, the player moves to a secondary scan location; if the cloud still cannot be found there, a random available cloud is selected to help with instead

**Role Assignment:**

- The @Healer1 alias holder stays behind and does not participate in stormcloud dispelling
- All other group members are assigned numbered positions corresponding to one of up to 5 stormcloud locations

**T21+ Mechanics:**

- **Add Targeting:** Auto-targets "a nullite foot soldier" at two configurable HP thresholds (default 50% and 20%), with the boss as fallback. Thresholds can be changed via `oc !c -Set_Variable` commands (announced in OC on setup). After changing thresholds, run setup again to apply them.
- **Timmmberrr:** When "TIMMMBERRR" is detected in chat, disables ALL cures for the group immediately (group curing during Timmmberrr wipes the group). After 4 seconds, checks self for the detriment and announces in OC if present. Re-enables cures after 10 seconds.
- **Fallen:** When "You have fallen to the ground." is detected, requests an autocure for that player and announces in OC.
- **Despotic Decree:** Monitors for the Despotic Decree detriment on self each pulse, and announces in OC when it is gained or removed.
- **Foothold:** Auto-cures Foothold using both an autocure request and a cure potion. Skips curing entirely if Timmmberrr is currently active (curing is unsafe during that window).
- **Lord Shomp Faces:** When "Lord Shomp faces" a player is detected in chat, that player announces it in OC.

### Player Notes

- Uses the @Healer1 alias to determine which healer stays behind during the flight phase.
- All other group members automatically disperse to handle stormclouds.
- T21+ add HP thresholds are configurable -- OC messages explain how to change them on setup. Re-run setup after changing values.
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
- If found, the player repositions 70% of the way from the vat cube toward the boss (standing in the beam path)
- If the Camp Spot Pulse (CSP) setting is enabled, a jump is triggered after repositioning

### Player Notes

- Only fighters take special action for Aegis of Bloodshed. All non-tank players automatically reposition for vat beams.

---

## Vadrak the Vile

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter with frontal assault dodging and gamma blast positioning mechanics.

### Requirements

- **Guardian** (casts Focused Offensive)
- **Fighter** (handles gamma blast joust)

### What the Module Does

**Setup:**

- Casts Focused Offensive (guardian only) and Singular Focus (all players) targeting Vadrak the Vile on setup
- Enables dynamic ignore of PBAoE for all group members

**Frontal Assault Avoidance:**

- When Vadrak announces an irradiated frontal assault, there is a 2-second delay and then fighters move behind the boss at distance 5 and non-fighters move behind the boss at distance 2
- After 5 seconds, everyone returns to their normal setup positions

**Gamma Blast Positioning:**

- When Vadrak announces which position can absorb the blast, fighters immediately move to a tank joust spot
- Non-fighter group members are sorted by their distance from the tank; any player at or beyond the required position number moves to a far raid joust spot
- When the correct position is confirmed (the "correct position to absorb" message fires), all joust overrides are cleared and players return to their normal positions

### Player Notes

- Focused Offensive and Singular Focus are canceled and dynamic PBAoE ignore is disabled when the boss dies.
- Frontal assault dodging and gamma blast positioning are fully automated.

---

## Xigothid

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter where the boss casts Tentacle Lash that can only be cured by mages, players must face away from the boss during the cast to avoid it, and black holes spawn that require the group to reposition to safe spots.

### Requirements

- **Mage** (only class that can cure Tentacle Lash)
- **Fighter** (handles black hole repositioning)

### What the Module Does

**Mage-Only Curing:**

- Curing is disabled for all non-mages on setup -- only mages can cure Tentacle Lash
- Each pulse, if any group member has the Tentacle Lash detriment, a cure request is sent specifically to mages (5-second cooldown between requests)

**Face Away Mechanic:**

- NPC Cast Monitoring detects when the boss begins casting Tentacle Lash (ability ID: 3359949986, cast time: ~3 seconds)
- All players auto-target themselves (to stop targeting the boss)
- The module repeatedly turns each character to face away from the boss for the duration of the cast, refreshing the facing every 2 seconds
- When the cast ends (or after 7 seconds as a fallback), targeting is restored to the boss

**Black Hole Avoidance:**

- When a "boss_03_black_hole" spawns within 5 meters of the group's current camp spot, the fighter finds the next safe joust spot from a list of 25 predefined positions
- A spot is considered safe if it is more than 5 meters from all existing black holes and the newly spawned one
- The entire group is repositioned to the new safe spot via cross-session camp spot change

### Player Notes

- The face-away is driven by NPC cast monitoring, not the "Xigothid lashes out at everyone!" chat line.
- All curing for non-mages is re-enabled when the boss dies.
- Black hole repositioning is fully automatic and handled by the fighter's session on behalf of the whole group.

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

- Mages automatically move to the omni focus object's location and double-click it three times
- After interacting, they return to their camp spot
- A 3-second cooldown between interactions prevents spamming

**Auto-Target:**

- Fighters auto-target "eyes without a face" (adds) and the boss as a fallback

### Player Notes

- Mages automatically travel to and interact with the omni focus object during the fight.
- Fighters handle add targeting automatically.
