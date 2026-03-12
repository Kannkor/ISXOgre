# Vaashkaani: Argent Sanctuary [Heroic II]

**Expansion:** Ballads of Zimara (Exp 20)

This heroic zone contains 3 boss encounters.

## Available Setups

| Boss | Description |
|------|-------------|
| [Akharys Sansobog](#akharys-sansobog) | Curse handling and boss-switching mechanic |
| [Uah'Lu the Unhallowed](#uahlu-the-unhallowed) | Archetype-specific NPC clicking |
| [General Ra'Zaal](#general-razaal) | HO management and add targeting |

---

## Akharys Sansobog

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A dual-boss encounter with curse handling that requires targeting specific bosses, and a mechanic where players must switch targets based on detriments.

### What the Module Does

**Twice Bitten:**

- Detects the Twice Bitten curse on the player
- Temporarily disables offensive abilities
- Targets the specific boss indicated by the curse
- Requests a cure

**Second Life:**

- Detects the Second Life detriment
- Automatically switches the group's target to the boss that does NOT have the detriment

### Player Notes

- Target switching is handled automatically
- The Twice Bitten curse requires targeting a specific boss for the cure to work

---

## Uah'Lu the Unhallowed

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where players must click archetype-specific "fallen" NPCs during the encounter.

### What the Module Does

**Fallen NPC Clicking:**

- Detects archetype-specific fallen NPCs during the fight
- Automatically moves the player to their matching fallen NPC
- Clicks the NPC to complete the mechanic

### Player Notes

- Each archetype has a specific fallen NPC to click
- Movement and clicking are handled automatically

---

## General Ra'Zaal

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with HO management, add targeting, and cure handling. The enchanter plays a key role in managing HOs on specific adds.

### What the Module Does

**Heroic Opportunity (HO) Management:**

- Enchanter is designated as the HO starter
- When ghul adds spawn with the Undeath After Undeath detriment, the enchanter solos HOs on these adds

**Add Targeting:**

- Auto-targets Ra'Zaal's ghul adds that do not have the Undeath After Undeath detriment

**Wounded Pride:**

- Detects the Wounded Pride detriment
- Automatically requests a cure

**Cure Management:**

- General cure abilities are disabled to prevent interfering with the HO mechanic

### Player Notes

- Enchanters have a critical role managing HOs on ghul adds
- Only target ghul adds that do NOT have Undeath After Undeath
- Wounded Pride is cured automatically
