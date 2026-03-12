# Maldura: Bhoughbh's Folly [Raid]

**Expansion:** Terrors of Thalumbra (Exp 12)

This zone has 5 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Bhoughbh Nova-Prime](#bhoughbh-nova-prime) | Dent joust, suppressor auto-run, pylon/add timers |
| [Bhoughbh Model XVII](#bhoughbh-model-xvii) | Static pulse alternating position swap |
| [The Tinkered Abomination](#the-tinkered-abomination) | Tank bomb stack management with auto-taunt |
| [Short-Circuited Construct Bot](#short-circuited-construct-bot) | Priest cure toggle |
| [MCP-Powered Pulsar](#mcp-powered-pulsar) | Auto-run to center for curse cleansing |

---

## Bhoughbh Nova-Prime

Setup command: `Set up for Nova`

### Overview

A complex fight with a suppressor kill mechanic, dent jousting, and multiple add phases tracked with HUD timers.

### What the Module Does

**GET OFF ME (Suppressor Mechanic):**

- When the boss shouts "Get off me" targeting a specific player, that player's name is tracked
- When the Suppressor XXVI add spawns, the targeted non-fighter character automatically navigates to the suppressor's location, kills it, and returns to position
- The suppressor can spawn at 4 known locations (Top, Bottom, North, South)

**Dent Joust:**

- When the dent mechanic fires, raid group 1 characters move to the raid spot
- After the dent resolves, fighters return to their tank spot
- HUD countdown displays time until the next dent (~44 seconds)

**Pylon Tracking:**

- Displays a HUD showing the boss health percentage for the next pylon spawn and next add wave
- At 10% health (all pylons spawned), repositions the raid to a bottom strategy

### Player Notes

- On pull, place the boss as far away from the raid as possible (Raid - Tank - Named)
- Group 1 has tank spots and will joust the dent automatically
- You should play your second group manually
- Bards automatically cast Quick Tempo when the suppressor spawns

---

## Bhoughbh Model XVII

Setup command: `Set up for Model` (also accepts `Set up for Bhoughbh`)

### Overview

A fight where tanks and non-tanks must alternate positions during static pulses.

### What the Module Does

**Static Pulse Position Swap:**

- When the boss prepares static pulses, fighters and non-fighters swap positions every 5 seconds in an alternating pattern
- Fighters start at the raid spot (away), non-fighters start at the tank spot (close), then they alternate 4 times

### Player Notes

- Campspot must be enabled on everyone including tanks

---

## The Tinkered Abomination

Setup is automatic when engaged.

### Overview

A fight where fighters must manage their Ticking Time Bomb stacks to avoid wiping the raid.

### What the Module Does

**Bomb Stack Management (Fighters Only):**

- When a fighter's bomb stacks reach 11, they stop attacking to prevent additional stacks
- When stacks clear, the fighter re-engages with a class-specific taunt priority chain (Guardian, Berserker, Paladin, Shadowknight, Monk, and Bruiser each have their own taunt sequence)
- At 14 stacks (emergency), attempts Recapture as a last resort

### Player Notes

- You MUST complete the first tank swap yourself before the automation kicks in

---

## Short-Circuited Construct Bot

Setup is automatic when engaged.

### Overview

A fight where curing must be toggled off during certain phases.

### What the Module Does

**Cure Toggle:**

- When a deactivated sentinel bot spawns, priest cure cast stack is disabled
- When the Construct Bot despawns, priest cure cast stack is re-enabled

### Player Notes

- This mechanic may need further refinement

---

## MCP-Powered Pulsar

Setup command: `Set up for Pulsar`

### Overview

A fight where cursed players must run to the center of the room to cleanse the curse.

### What the Module Does

**Curse Cleansing:**

- When a player becomes cursed, the module detects an invisible cleansing actor
- Continuously moves the player's campspot to the cleansing actor's location until the curse clears
- Returns to the normal camp position once cleansed

### Player Notes

- Fighters have a separate tank spot
