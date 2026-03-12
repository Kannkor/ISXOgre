# Kralet Penumbra: Uzulu Deep [Event Heroic]

**Expansion:** Terrors of Thalumbra (Exp 12)

This zone has 1 boss encounter plus an orb puzzle with OgreBot automation.

## Available Setups

| Boss | Description |
|------|-------------|
| [Urzzra-Uzulu](#urzzra-uzulu) | Auto dialog responses, orb puzzle solving |

---

## Urzzra-Uzulu

Setup is automatic when engaged.

### Overview

A fight with an automated dialog mechanic and a multi-round orb puzzle.

### What the Module Does

**Automated Dialog:**

- When Urzzra-Uzulu opens dialog with you, the module automatically selects the correct response based on your archetype:
    - Fighters: "I am a veteran"
    - Priests: "Free yourself"
    - Scouts: "Sorry Pal"
    - Mages: "I trust"

**Orb Puzzle (Special_ZoneSpecific):**

- Move ONE toon near the orbs then press `Special_ZoneSpecific` in MCP
- The module detects the current orb colors and executes the correct clicking sequence for each round:
    - Round 1: All white orbs
    - Round 2: Blue/Red/White/Red pattern
    - Round 3: Purple/White/Blue/Red pattern

### Player Notes

- Only ONE toon should be near the orbs when pressing the MCP button
- The orbs MUST be at their default colors before triggering the puzzle
- If the colors don't match a known pattern, the module will ask you to reset and try again
