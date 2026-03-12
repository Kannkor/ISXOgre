# The Ruins of Cabilis [Heroic]

**Expansion:** Kunark Ascending (Exp 13)

This zone has 1 boss encounter with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Smithy Xzatik](#smithy-xzatik) | Auto jousts anvil spawns |

---

## Smithy Xzatik

Setup command: `Set up for Smithy`

### Overview

A fight where an anvil spawns that must be jousted by non-fighters.

### What the Module Does

**Anvil Joust:**

- When an anvil actor spawns, all non-fighters shift their campspot away from the boss
- After the anvil despawns (or after an 8-second safety timer), everyone returns to their normal positions
- Fighters stay in place and do not joust

### Player Notes

- Fighters have a separate tank spot and are excluded from jousting
- The 8-second timer acts as a fallback in case the anvil despawn event is missed
