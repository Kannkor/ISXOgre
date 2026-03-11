# Zon Zobboz: Gaze of the Oglth [Raid]

**Expansion:** Rage of Cthurath (Exp 22)

This zone has 3 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Setup Name | Description |
|------|-----------|-------------|
| [Oglth](#oglth) | Oglth | Announce on when to joust |
| [Viniug the Horrific](#viniug-the-horrific) | Viniug | Supposed to be automated. May not be finished |
| [Pangionug](#pangionug) | Pangionug | G1/G4 tank one boss, G2/G3 tank the other. Auto-target lists |

---

## Oglth

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A three-named encounter (Glare Oglth, Gaze Oglth, Gawk Oglth) where the group must joust on a timer. The module provides on-screen countdown timers and handles class ability adjustments.

### Requirements

- **Enchanter**, **Guardian**, **Fighter** (specific abilities are toggled)

### What the Module Does

**Joust Timer:**

- When a "shocking glance" occurs, the module calculates how many of the three Oglth mobs are still alive
- If all 3 are alive: 150-second on-screen countdown timer
- If 1 or 2 remain: 75-second on-screen countdown timer
- Fighters receive a TTS "Joust" alert

**Warring Atrocities Cure:**

- When the Warring Atrocities detriment is detected (arcane, can only be cured by non-priest cures), the module automatically uses an arcane cure potion

**Class Ability Adjustments:**

- Disables Enchanter abilities: Channel, Manasoul
- Disables Guardian abilities: Recapture, Hold the Line, Champion's Interception
- Enables dynamic ignore of encounter nukes and PBAoE for fighters

**Post-Kill:**

- After all Oglth mobs die, broadcasts a message telling everyone to reload their bot

### Player Notes

- On-screen joust countdown timer is displayed to all players.
- TTS joust alert for fighters.
- You must manually joust -- the module announces timing but does not reposition.

---

## Viniug the Horrific

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

> **:memo: Possibly Unfinished**
>
> This automation may not be fully complete.

### Overview

An encounter with add phases and void rifts that require group repositioning.

### Requirements

- **Guardian**, **Fighter**, **Priest**

### What the Module Does

**Add Handling:**

- When "a Horrific Bonder" add spawns, the module repositions the group:
    - Non-priests move to a safe raid spot
    - Priests move to a separate priest spot
    - Fighters are eventually moved to drag the boss away from the raid

**Rift Handling:**

- When a Void Rift spawns, the module tracks it
- If an add is already up, the rift is deferred

**Post-Add Cleanup:**

- When the add despawns, everyone is reset to the center raid position

**Guardian Setup:**

- Disables Guardian "Recapture" on setup

### Player Notes

- Automatic repositioning during add phases.
- This module may not be fully finished.

---

## Pangionug

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A two-boss encounter (Fera Pangionug and Irid Pangionug) where the raid splits by raid group to tank each boss separately.

### Requirements

- **Guardian**, **Fighter**

### What the Module Does

**Raid Group Positioning:**

| Raid Groups | Assignment |
|-------------|-----------|
| Groups 1 and 4 | Tank Fera Pangionug with "an Impish Bonder" adds |
| Groups 2 and 3 | Tank Irid Pangionug with "a Bumbling Bonder" adds |

**Auto-Target:**

- Fighters in each subgroup get auto-target lists set up for their respective boss and adds
- Assist is set to the fighter for each subgroup

**Class Ability Adjustments:**

- Same Guardian ability disabling as Oglth (Recapture, Hold the Line, Champion's Interception)
- Enables dynamic ignore of encounter nukes for fighters

### Player Notes

- Fully automatic group splitting by raid group number.
- Guardian abilities are re-enabled when the bosses die.
