# Arena of the Gods [Raid]

**Expansion:** Chains of Eternity (Exp 09)

This zone has 2 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Tunare](#tunare) | Archetype-based four-corner positioning |
| [Bristlebane](#bristlebane) | Jester interactions, bomb riddle solver |

---

## Tunare

Setup command: `Set up for Tunare`

### Overview

A positioning setup that separates the raid by archetype.

### What the Module Does

**Archetype-Based Positioning:**

- Fighters, Scouts, Priests, and Mages are each sent to a different position in the arena

### Player Notes

- Four separate positions based on class archetype

---

## Bristlebane

Setup command: `Set up for Bristlebane`

!!! warning "Requires Elite 2"
    This boss module requires Elite 2 access to activate.

### Overview

A complex encounter with jester interactions and a bomb riddle game that determines who holds the real vs. fake bomb.

### What the Module Does

**Jester Interactions:**

- When the jester hides, automatically performs the /taunt emote on it
- When the jester is immune and needs a bard dispel, bards interact with it to stop the lute
- When the jester needs a raid dispel, enchanters dispel the NPC
- When the jester wants to dance with a specific player, that player performs /dance

**Bomb Game:**

- When Bristlebane gives everyone a bomb, tracks remaining bomb count on the HUD
- Parses Bristlebane's clue to determine if your bomb is real or fake based on:
    - **Race size:** Small, medium, or large race clues
    - **Gender:** Male or female clues
    - **Archetype:** Fighter, Mage, Priest, or Scout clues
    - **Subclass:** Specific weapon name clues matching each of the 24 classes
- If your bomb is real, automatically uses it
- On the final round, players still holding a bomb are jousted to a safe spot

### Player Notes

- The bomb riddle solver handles all clue types automatically
