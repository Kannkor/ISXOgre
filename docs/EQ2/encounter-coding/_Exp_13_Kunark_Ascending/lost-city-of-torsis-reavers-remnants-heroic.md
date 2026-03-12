# Lost City of Torsis: Reaver's Remnants [Heroic]

**Expansion:** Kunark Ascending (Exp 13)

This zone has 4 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Tzirathk](#tzirathk) | Reflection swap between two tank positions |
| [Dread Wraith](#dread-wraith) | Progressive campspot movement on soul burn |
| [Neh'Ashiir](#nehashiir) | Shockwave curse joust with dual-curse handling |
| [A Spectral Beguiler](#a-spectral-beguiler) | Mage/druid auto-dispelling |

---

## Tzirathk

Setup command: `Set up for Tzirathk`

### Overview

A fight where the tank must swap between two positions when reflections spawn.

### What the Module Does

**Reflection Swap:**

- When the brazier increases in heat and reflections spawn, the fighter's campspot swaps to whichever of the two tank positions is farther from the current one
- This alternates the tank position each time the mechanic fires
- Non-fighters have a separate fixed raid spot

### Player Notes

- **Campspot must be enabled on everyone including your tank**

---

## Dread Wraith

Setup command: `Set up for Dread`

### Overview

A fight with progressive movement from East to West as the Dread Wraith burns souls.

### What the Module Does

**Progressive Movement:**

- Each time the Dread Wraith's eyes burn into your soul, the campspot shifts further along the X axis (+10 meters each time)
- The first shift is doubled (+20 meters) to account for the initial position
- This creates a gradual movement from the East end toward the West end of the room

### Player Notes

- **Campspot must be enabled on everyone including your tank**
- The group starts at the East end and progresses toward the West end

---

## Neh'Ashiir

Setup command: `Set up for Neh`

### Overview

A fight with an uncurable shockwave curse that requires jousting, with smart handling when two players are cursed simultaneously.

### What the Module Does

**Shockwave Joust:**

- Monitors for the "Shockwave Undercuting" debuff
- When detected, jousts the character away from the group
- If two group members are cursed at the same time, they are sent to different joust spots (one left, one right) to avoid stacking
- When the debuff drops, returns to the normal camp position

### Player Notes

- Campspot your group minus your tank
- If campspot is not enabled, a message is shown that the player must joust manually
- Fighters have a slightly offset position from the main group

---

## A Spectral Beguiler

Setup is automatic when engaged.

### Overview

A fight where a buff must be removed from the boss.

### What the Module Does

**Auto Dispell:**

- Mages and Druids automatically dispel a specific buff from A Spectral Beguiler when detected
- Respects the dispel cooldown before attempting again

### Player Notes

- Only Mages and Druids perform the dispelling
