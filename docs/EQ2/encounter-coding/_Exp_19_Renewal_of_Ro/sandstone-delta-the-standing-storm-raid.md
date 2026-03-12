# Sandstone Delta: The Standing Storm [Raid]

**Expansion:** Renewal of Ro (Exp 19)

This raid zone contains 5 boss encounters.

## Available Setups

| Boss | Description |
|------|-------------|
| [Embodiment of Fright](#embodiment-of-fright) | Joust behind named, walk/crouch during fear |
| [Tsmang Blightswarm Broodmaster](#tsmang-blightswarm-broodmaster) | On-screen timers for adds and weakness |
| [Malformed Prophet](#malformed-prophet) | Location-aware jousting (WIP) |
| [Beckut, the Mad Zealot](#beckut-the-mad-zealot) | Auto cure curse, epic ability usage (WIP) |
| [Raaijs Viruniq](#raaijs-viruniq) | Flame Kissed auto cure curse |

---

## Embodiment of Fright

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where players must joust behind the named when eyes are watching, and handle a fear mechanic with walk/crouch movement.

### What the Module Does

**Eyes Watching:**

- Detects the "eyes watching" text trigger
- Automatically positions players 20 meters behind the named
- Players are responsible for removing the shield

**Fear Mechanic:**

- Detects the fear detriment
- Automatically switches movement to walk and crouches during the fear
- Jumps to clear the effect afterward

### Player Notes

- When jousted behind the named, you are responsible for removing the shield
- The walk/crouch mechanic during fear is handled automatically
- A jump is triggered after the fear to clear movement effects

---

## Tsmang Blightswarm Broodmaster

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with timed add spawns and a weakness timer mechanic.

### What the Module Does

**Add Spawn Timer:**

- Displays an on-screen timer showing when the next add spawn is expected based on previous add timing

**Weakness Timer:**

- Starts a 600-second (10-minute) death timer when "figure out all your weaknesses" text is detected

### Player Notes

- Watch the on-screen timers to prepare for add spawns
- The weakness timer gives you a deadline to defeat the boss

---

## Malformed Prophet

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

!!! warning "Work in Progress"
    This encounter's automation is still under development.

### Overview

A fight with location-aware jousting across multiple fight areas.

### What the Module Does

**Flame Jousting:**

- Detects "flames on your skin" text trigger
- Automatically jousts based on the current fight area location
- Supports 4 different fight areas with separate tank, raid, and joust spots
- Tanks and their assigned priests are excluded from jousting

### Player Notes

- The module determines the correct joust spot based on your location in the zone
- Tanks and their priests stay on the named during the joust

---

## Beckut, the Mad Zealot

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

!!! warning "Work in Progress"
    This encounter's automation is still under development.

### Overview

A fight with auto cure curse and automated epic ability usage.

### What the Module Does

**Auto Cure Curse:**

- Detects the "no longer being watched" text trigger
- Automatically requests a cure curse

**Epic Ability:**

- Automatically uses the Renewal of Ro epic ability when needed
- The first healer is flagged for epic usage; if unavailable, the flag passes to the next priest
- Certain epic abilities are disabled during the fight to prevent conflicts

### Player Notes

- Cure curse is handled automatically via text detection
- Epic ability usage is automated — ensure your epic is available
- Some abilities are temporarily disabled during the fight

---

## Raaijs Viruniq

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with the Flame Kissed detriment that requires priests to cure curse with specific timing.

### What the Module Does

**Flame Kissed:**

- Detects the Flame Kissed detriment
- Automatically requests a cure curse from priests only
- Uses delayed cure timing (3-second and 6-second delays) to ensure proper cure order
- Cure curse is disabled during the fight to prevent premature curing

### Player Notes

- Only priests handle the Flame Kissed cure — it is automated with proper timing delays
- Do not manually cure curse during this fight as the module manages the timing
