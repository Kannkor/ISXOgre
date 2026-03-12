# Zimara Breadth: Crested Expanse [Raid]

**Expansion:** Ballads of Zimara (Exp 20)

This raid zone contains 3 boss encounters.

## Available Setups

| Boss | Description |
|------|-------------|
| [Chohnki](#chohnki) | Auto jousting from earthquake AoE |
| [Chohnkasaurus](#chohnkasaurus) | Auto jousting on feign death |
| [Chohnkanon](#chohnkanon) | Charge and spin jousting with fighter repositioning |

---

## Chohnki

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with ground AoE earthquake jousting that requires moving away from affected areas.

### What the Module Does

**Earthquake Jousting:**

- Monitors for earthquake ground AoE zones during the fight
- When an earthquake zone appears near the group, jousts to a safe position
- Handles delayed actor detection for accurate joust timing

**Combined Mob Mode:**

- Supports combined mob mode with position swapping for multi-mob scenarios

### Player Notes

- Follow the automated jousting when earthquake zones appear
- The module handles joust timing automatically

---

## Chohnkasaurus

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where the boss feigns death, requiring the group to joust away, plus red aura tracking.

### What the Module Does

**Feign Death Jousting:**

- Detects when the boss feigns death
- Jousts the group away from the boss for 7 seconds
- Returns to position after the danger passes

**Red Aura Tracking:**

- Monitors for a red aura on the boss
- Adjusts group behavior based on the aura state

**Combined Mob Mode:**

- Supports combined mob mode with Chohnkanon

### Player Notes

- Follow the automated joust when the boss feigns death
- Watch for the red aura phase changes

---

## Chohnkanon

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a charge-up mechanic that pushes non-fighters away and a spin aura that requires a far joust, plus fighter repositioning.

### What the Module Does

**Charge-Up Mechanic:**

- Non-fighters are automatically pushed away from the boss during the charge-up phase

**Spin Aura Jousting:**

- Detects the spin aura on the boss
- Jousts the group far away to a safe position during the spin

**Fighter Repositioning:**

- Fighters are automatically repositioned after the spin phase ends

**On-Screen Timers:**

- Displays timers for tracking mechanic cycles

### Player Notes

- Non-fighters will be pushed away during the charge-up -- this is automated
- Follow the far joust during the spin phase
- Fighters will be repositioned automatically after spins
