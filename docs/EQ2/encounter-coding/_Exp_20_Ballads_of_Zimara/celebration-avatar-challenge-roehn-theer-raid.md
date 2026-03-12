# Celebration Avatar Challenge: Roehn Theer [Raid]

**Expansion:** Ballads of Zimara (Exp 20)

This raid zone contains 1 boss encounter.

## Available Setups

| Boss | Description |
|------|-------------|
| [Roehn Theer](#roehn-theer) | Complex multi-mechanic fight with tile positioning and pair stacking |

---

## Roehn Theer

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Requirements

- **ERE (Effective Raid Elite)** must be unlocked to access this encounter's automation

### Overview

A complex encounter with multiple overlapping mechanics including rune targeting, archetype-based tile positioning, incurable curse handling, soul-charged pair stacking, and add management. The boss has two variants (Chaos and Order) that are targeted by different raid groups.

### What the Module Does

**Rune Auto-Targeting:**

- Detects 4 corner runes that spawn at 95% health
- Automatically targets and attacks the runes

**Inevitable Annihilation (Incurable Curse):**

- Detects this incurable curse on the player
- Moves the player to their archetype-specific tile:
    - Priests → Water tile
    - Fighters → Forest tile
    - Mages → Passion tile
    - Scouts → Wrath tile
- Coordinates positioning with other affected players to avoid overlap

**Soul-Charged Pair Stacking:**

- Void-charged Soul (noxious) -- players with this detriment are automatically stacked together
- Star-charged Soul (elemental) -- players with this detriment are automatically stacked together
- Coordinated movement ensures affected players reach each other

**Add Management:**

- Approaching Equilibrium add is announced via TTS ("Big add") for fighters

**Raid Group Targeting:**

- Groups 1-2 target the Chaos variant of the boss
- Groups 3-4 target the Order variant of the boss

**Item Management:**

- Vampiric items are disabled for the fight

### Player Notes

- ERE must be unlocked for this encounter to activate
- Pay attention to archetype tiles during Inevitable Annihilation -- positioning is automated
- Stay together with your pair partner during soul-charged mechanics
- Fighters should react quickly to the "Big add" TTS alert
