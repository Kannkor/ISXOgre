# Maldura: Bar Brawl [Event Heroic]

**Expansion:** Terrors of Thalumbra (Exp 12)

This zone has 1 boss encounter with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Bingling](#bingling) | Color-based auto-positioning between portals |

---

## Bingling

Setup command: `Set up for Bingling`

### Overview

A fight where the group must move between three colored portals (Red, Blue, Yellow) based on the boss's current color phase.

### What the Module Does

**Color-Based Movement:**

- Monitors Bingling's current color phase by checking detriments on the boss
- Automatically moves the group to the matching colored portal:
    - Blue phase: navigates to the Blue ring
    - Yellow phase: navigates to the Yellow ring
    - Red phase: navigates back to the Red ring (starting position)
- Uses intermediate waypoints for safe pathing between portals to avoid zone geometry issues

### Player Notes

- The starting position is at the Red portal
- Movement is waypoint-based (step by step) so it may take a moment to navigate between distant portals
- The module waits until the character has stopped moving before evaluating the next color change
