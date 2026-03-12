# Vaashkaani, Alcazar of Zimara: Sovereign Summons [Raid]

**Expansion:** Ballads of Zimara (Exp 20)

This raid zone contains 3 boss encounters.

## Available Setups

| Boss | Description |
|------|-------------|
| [Galeistria the Polished](#galeistria-the-polished) | Reflecting mirror jousting |
| [Chaltieu, Mirrored Sentry](#chaltieu-mirrored-sentry) | Curse handling with interactable clicking |
| [Ikal-tam the Pensive](#ikal-tam-the-pensive) | Auto jousting, cure requests, and priest phase management |

---

## Galeistria the Polished

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight centered around the Reflecting Mirror mechanic that requires moving the group toward spawning mirrors.

### What the Module Does

**Reflecting Mirror:**

- Detects when a Reflecting Mirror spawns during the fight
- Calculates the closest joust position near the mirror
- Moves the group toward the mirror's location

### Player Notes

- Follow the automated movement when mirrors appear
- Some mirror mechanics may still be in development

---

## Chaltieu, Mirrored Sentry

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with the Chasing the Echo curse that requires finding and clicking the correct interactable object.

### What the Module Does

**Chasing the Echo:**

- Detects the Chasing the Echo curse on the player
- Finds the correct interactable object (identified by a blue circle aura)
- Automatically waypoints the player to the object and clicks it

### Player Notes

- The module handles finding and clicking the correct blue circle automatically
- Follow the automated waypointing when cursed

---

## Ikal-tam the Pensive

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with red ring AoE jousting, cure requests, and a priest-focused phase with specific healing requirements.

### What the Module Does

**Red Ring AoE Jousting:**

- Monitors for red ring AoE circles spawning during the fight
- Automatically jousts the group away from the rings

**Flash of Arcanum:**

- Detects Flash of Arcanum on the player
- Requests a mage arcane cure

**Fervent Wishes Phase:**

- During this 18-second phase, priests temporarily disable offensive abilities
- Druids automatically cast Natural Cleanse and Pact of the Cheetah
- Shamans automatically cast Soul Shackle
- All disabled abilities are re-enabled after the phase ends

### Player Notes

- Follow the automated jousting during red ring phases
- Priests will have their offensive abilities temporarily disabled during the Fervent Wishes phase
- Druids and shamans have specific healing roles during Fervent Wishes
