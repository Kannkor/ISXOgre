# Vex Thal: Beyond the Veil [Raid]

**Expansion:** Reign of Shadows (Exp 17)

This zone has 6 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Diabo Xi Va](#diabo-xi-va) | Increment management with orb positioning, red circle avoidance, scepter rotation |
| [Akhessa Va Liako Vess](#akhessa-va-liako-vess) | Auto-scepter on Coruscating Scales threshold, conduit handling, leech curing |
| [Thall Xundraux Diabo](#thall-xundraux-diabo) | Smoldering Stare self-target, side room management |
| [High Priest Verrkara](#high-priest-verrkara) | Room-swapping based on Occupational Hazard stacks |
| [Thall Va Xakra Fer](#thall-va-xakra-fer) | Shade Crowned curse curing, location warning jousting, scepter rotation |
| [Emperor Ssraeshza](#emperor-ssraeshza) | Scatterstorm curse jousting with raid ordering, portal add handling, scepter management |

---

## Diabo Xi Va

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight centered around managing Shadowlich Fealty stacks on the boss by positioning the raid near or away from glowing orbs, with red circle avoidance and scepter usage.

### What the Module Does

**Shadowlich Fealty Increment Management:**

- The raid must keep stacks within a target range (default 4-5 for Challenge Mode)
- When stacks exceed the maximum, the raid moves toward a glowing orb to reduce them
- When stacks are below the minimum, the raid moves away to increase them
- 8 joust positions arranged in a circle are used for increment management

**Red Circle Avoidance:**

- When a Targeting Location Warning spawns, the module jousts the group away from the warning location
- A 7-second timer governs avoidance positioning

**Scepter Rotation:**

- The flagged player uses Scepter of Illumination when the boss has "Protected by Shadows" and Scepter of Shadows when "Protected by Illumination"
- The flag passes to the next raid member when the scepter is on cooldown

**Challenge Mode:**

- Challenge Mode uses raid-wide commands and has a FailController phase for the first 4 red circles before transitioning to normal DXV control

### Player Notes

- Increment management is fully automated based on stack thresholds
- The scepter flag rotates through the raid as cooldowns expire
- Watch for red circle warnings -- the module handles avoidance positioning

---

## Akhessa Va Liako Vess

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with scepter management based on detriment stacks, conduit interaction, and leech curing.

### What the Module Does

**Auto-Scepter:**

- The flagged player monitors Coruscating Scales stacks on the boss
- When stacks exceed the configurable threshold (default 5), uses whichever scepter is available (Illumination or Shadows)
- Scepter usage is paused during Dance of the Damned

**Conduit Handling:**

- When a Summoned Pulsating Shadow Conduit spawns, the flagged character moves to it, double-clicks it, moves to the Location Warning, and interacts with it
- The flag passes to the next person after use

**Disconcerting Leech:**

- Non-priest characters auto-use arcane cure potions when they have the Disconcerting Leech detriment

### Player Notes

- Scepter usage is automated based on stack thresholds
- The conduit handler coordinates movement and interaction automatically
- Ensure arcane cure potions are available for the leech mechanic

---

## Thall Xundraux Diabo

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a self-targeting mechanic and side room management based on colored ring indicators.

### What the Module Does

**Smoldering Stare:**

- When a player has the Smoldering Stare detriment, the module automatically targets self
- When the detriment clears, targeting returns to the boss

**Side Room Management (Fighter):**

- Monitors green and red ring indicators and NPC positions using TintFlags
- When a red-tinted NPC is near the green ring, the group moves to the red room
- When a green-tinted NPC is near the red ring, the group moves to the green room
- A 15-second cooldown between room transitions prevents thrashing
- Supports both center-of-room and spread positioning modes

### Player Notes

- Self-targeting during Smoldering Stare is automatic
- Room transitions are managed by the fighter and coordinated group-wide

---

## High Priest Verrkara

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with room-swapping based on accumulating debuff stacks.

### What the Module Does

**Occupational Hazard Room-Swapping:**

- Monitors 3 variants of Occupational Hazard corresponding to center, east, and west rooms
- When stacks exceed 15 in the current room, the module moves the entire raid to a different room using raid-wide commands

### Player Notes

- Room transitions are automated when stack thresholds are reached
- Follow the raid movement when rooms change

---

## Thall Va Xakra Fer

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with timed curse curing, location-based jousting, and scepter rotation.

### What the Module Does

**Shade Crowned Curse:**

- When the Shade Crowned detriment duration drops below 10 seconds, the module broadcasts an AutoCurse request
- Also monitors Grasping Hold and requests cures when it appears (but not while Shade Crowned is active)

**Location Warning Jousting:**

- When a Targeting Location Warning spawns, the module checks its aura type:
    - Bad circle (spawn warning): jousts away from the boss
    - Good circle (green cage): moves toward it to benefit from the effect

**Scepter Rotation:**

- Same scepter mechanic as Diabo Xi Va: uses the correct scepter based on the boss's "Protected by" buff
- Flag passes to the next person when the scepter is on cooldown

### Player Notes

- Curse curing is timed automatically near detriment expiration
- The module distinguishes between good and bad location warnings and handles each appropriately
- Scepter flag rotates through the raid

---

## Emperor Ssraeshza

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

The final boss with multiple phases including curse-based jousting with raid-wide ordering, portal add encounters, and scepter management.

### What the Module Does

**Scatterstorm Curse Jousting:**

- When the Scatterstorm curse appears, the module determines the player's order among all cursed raid members
- Each cursed player is sent to a different joust spot (4 spots available, varying by Challenge Mode and difficulty)
- Players wait at their joust spot until the curse clears, then return
- Challenge Mode introduces a brief delay before jousting to allow the curse to tick

**Ghastly Strangle:**

- When Ghastly Strangle appears and Scatterstorm is NOT active, the module broadcasts an AutoCurse request

**Add Portal Handling:**

- Archetype-specific portals spawn with identifying TintFlags (priest, scout, mage, fighter)
- The matching archetype player enters the portal, auto-targets the archetype-specific add, positions, uses scepters, and resets after the add dies
- Fighters have special handling: they request Rescue and Cry of the Warrior first to drop aggro before entering the portal

**Scepter Management:**

- Scepter counts differ between Challenge Mode (8 at 50% and 8 at 15%) and normal (5 at 50%)
- Can be disabled via configuration

**HUD Timer:**

- A 20-second on-screen countdown timer is displayed when challengers are chosen

### Player Notes

- Scatterstorm jousting assigns each cursed player to a unique position -- follow the auto-positioning
- Portal encounters are handled per archetype with auto-targeting
- Fighters drop aggro before entering portals
- The 20-second timer HUD helps track portal phase timing
