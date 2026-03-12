# Ragrax, the Sepulcher of the Twelve [Raid]

**Expansion:** Chaos Descending (Exp 15)

This zone has 1 boss encounter with an OgreBot automation module.

## Available Setups

| Boss | Description |
|------|-------------|
| [The Council](#the-council) | Pre-cure AE timing, Blind's Eye removal (item or clickable), raid spread positioning |

---

## The Council

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with timed AE pre-curing and a debuff removal mechanic.

### What the Module Does

**Pre-Cure AE Timing (Final Judgement):**

- When Favored Neglect is detected, starts an 18-second timer chain
- Triggers pre-cure so priests can cure the AE before it lands
- After the first AE, sets up a recurring 22-second timer for subsequent AEs
- HUD displays countdown to next pre-cure window

**Blind's Eye Removal:**

- When the debuff is detected, first tries to use a smooth pledge stone from inventory
- If no stones available, finds the interactable light actor, moves to it, and double-clicks it

**Raid Spread Positioning:**

- Spreads the raid into 4 groups at cardinal positions
- Sub-positions are assigned by archetype/role (bards, enchanters, priests, DPS, fighters)

### Player Notes

- Disable group cure in cast stack -- the module manages pre-cure timing
- The AE is pre-cured so it never visibly hits after the first occurrence
