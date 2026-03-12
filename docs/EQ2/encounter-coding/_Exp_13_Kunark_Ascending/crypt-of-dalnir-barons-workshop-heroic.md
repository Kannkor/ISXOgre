# Crypt of Dalnir: Baron's Workshop [Heroic]

**Expansion:** Kunark Ascending (Exp 13)

This zone has 3 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Haggle Baron Dalnir](#haggle-baron-dalnir) | Full bard forge runner automation |
| [Sword and Shield](#sword-and-shield) | Arcanic flurry joust, mage/druid auto-dispelling |
| [The Googantuan](#the-googantuan) | Bard/enchanter valve clicking |

---

## Haggle Baron Dalnir

Setup command: `Set up for Haggle` (also accepts `Set up for Baron` or `Set up for Dalnir`)

### Overview

A complex fight where the Bard automatically runs the forge repair mechanic while the rest of the group fights.

### What the Module Does

**Forge Runner (Bard Only):**

When a Broken Forge Lever spawns:

- The Bard automatically runs the entire forge repair sequence:
    1. Moves to the coal bin and picks up Dalnir's infused coal
    2. Moves to the pail of water and picks it up
    3. Returns and waits for molten obulus ore (auto-assigned via Leader Only loot)
    4. Navigates to the correct forge (Western, Central, or Eastern) based on which lever spawned
    5. Crafts the Repair Forge Maw Control Lever at the forge
    6. Installs the repaired lever at the Forge Lever Base
    7. Returns to the group
- Non-bards are moved to the group spot during the forge phase
- Loot settings are temporarily adjusted so only the bard receives the ore, and restored when the fight ends

**HUD Timer:**

- Displays a countdown showing when the next forge will spawn

### Player Notes

- Campspot must be enabled for the bard movement to work
- Leader Only loot must be enabled so the ore can be auto-assigned to the bard
- The module handles door collision detection -- if a forge door is closed, it will open it automatically

---

## Sword and Shield

Setup command: `Set up for Sword` (also accepts `Set up for Shield` or `Set up for Enchanted`)

### Overview

A fight with arcanic flurry jousting and automatic buff dispelling from the boss.

### What the Module Does

**Arcanic Flurry Joust:**

- When the boss prepares to flurry with arcanic energy, all non-fighters move to the joust spot
- After 7 seconds, everyone returns to their normal camp spots
- Fighters remain in place

**Auto Dispell:**

- Mages and Druids automatically dispel the Enchanted Shield's defensive infusion or the Enchanted Sword's offensive infusion

### Player Notes

- Fighters have a separate tank spot and do not joust

---

## The Googantuan

Setup command: `Set up for Googantuan`

### Overview

A fight where Bards and Enchanters automatically run to and click valves when triggered.

### What the Module Does

**Valve Clicking:**

- When standing in the middle of 2 valves, press `Special_ZoneSpecific` in MCP
- The Enchanter automatically runs to one valve and clicks it
- The Bard automatically runs to the paired valve and clicks it
- Both return to their previous camp spots after clicking

**Key Waypoint:**

- When The Googantuan dies, if a key drops, a waypoint is set to its location

### Player Notes

- Campspot is required for this mechanic
- You must be standing between the two valves before pressing `Special_ZoneSpecific`
- Only Bards and Enchanters will run valves -- all other classes stay in place
