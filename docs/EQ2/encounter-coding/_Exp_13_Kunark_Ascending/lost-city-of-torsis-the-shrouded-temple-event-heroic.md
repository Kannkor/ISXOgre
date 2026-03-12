# Lost City of Torsis: The Shrouded Temple [Event Heroic]

**Expansion:** Kunark Ascending (Exp 13)

This zone has 1 boss encounter with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [The Meld of Haze](#the-meld-of-haze) | Auto-runs to and kills personal mirage |

---

## The Meld of Haze

Setup command: `Set up for Haze`

### Overview

A fight where each player's personal mirage spawns in the fog and must be found and destroyed.

### What the Module Does

**Mirage Handling:**

- When the mirage emote fires, the module scans for your personal mirage (named after your character)
- Checks multiple times with staggered delays (1s, 3.5s, 7s) since the mirage may take time to appear
- Once found, disables campspot and navigates to the mirage's location
- If AutoTarget is enabled, clears the auto-target list and adds the mirage as the target
- After the mirage is killed, automatically navigates back to the raid position and re-enables campspot

### Player Notes

- Navigation mapping may be required -- if the mirage is too far away (beyond 20 meters after movement), the module reports a navigation failure
- The module sets a campspot at a fixed raid position for all characters
