# Blackhook Spiral: Fort Sunder [Heroic II]

**Expansion:** Scars of Destruction (Exp 21)

This Heroic II zone contains 5 boss encounters, all fully automated.

## Available Setups

| Boss | Description |
|------|-------------|
| [Argh the Anvil](#argh-the-anvil) | Setup then pull. Fully automated |
| [Igarn the Insurmountable](#igarn-the-insurmountable) | Fully automated |
| [Zeraxyl](#zeraxyl) | Fully automated |
| [Tajara the Vengeful](#tajara-the-vengeful) | Fully automated. Turns ON dispells |
| [Harmok the Hammer](#harmok-the-hammer) | Fully automated |

---

## Argh the Anvil

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight that requires precise positioning, goblin interaction for cure coordination, and dispell management.

### What the Module Does

**Positioning:**

- Places the group at a specific camp spot with movement disabled
- Enables Absorb Magic (dispells) for the fight

**Goblin Hailing:**

- Periodically hails a nearby goblin NPC to determine who needs to be cured
- Parses the goblin's response to identify the cure target

**Cure Coordination:**

- When a cure target is identified, cure curse is temporarily enabled for priests
- After the cure is applied, cure curse is disabled again to prevent unwanted curing

### Player Notes

- Set up before pulling -- do NOT pull first
- The module requires the goblin NPC to be alive and in range for cure target identification

---

## Igarn the Insurmountable

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight involving mine detriments and Bulwark of Order casting. The module also targets a secondary named (Winx the Unmountable).

### What the Module Does

**Bulwark of Order:**

- Monitors for mine-related detriments on the player
- When mines are detected, fighters automatically cast Bulwark of Order

**Cure Management:**

- Enables cure curse for the fight

**Targeting:**

- Auto-targets both Igarn and Winx the Unmountable

### Player Notes

- Fighters should have Bulwark of Order available in their cast stack

---

## Zeraxyl

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A bird-railing management fight where players must move between platforms when famished migrators land on their current location. The module handles movement between railings automatically.

### What the Module Does

**Railing Management:**

- Monitors for famished migrators landing on the player's current railing pad
- Automatically moves the group between two available railing pads to avoid birds

**Cast Monitoring:**

- Monitors for a specific feather burst ability being cast
- Blocks all movement while this ability is being cast to avoid deaths

**Auto-Targeting:**

- Sets auto-target scan radius to 40 to detect birds across the arena

### Player Notes

- The module alternates between two railing positions based on bird spawns
- Movement is locked during the feather burst cast -- stay still during this phase

---

## Tajara the Vengeful

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A simple fight where Absorb Magic (dispells) need to be enabled.

### What the Module Does

- Enables Absorb Magic for all characters
- That's it -- a straightforward dispell fight

### Player Notes

- No special mechanics to worry about beyond keeping Absorb Magic active

---

## Harmok the Hammer

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where the fighter needs to jump up onto a platform. The module automates the platform jump and walking mode.

### What the Module Does

**Fighter Platform Jump:**

- Automatically executes a camp spot jump script to get the fighter on top of the platform
- Sets the fighter to walking mode to maintain position on the platform
- Disables face-in-combat to prevent falling off
- Retries the jump if the fighter hasn't reached the correct height

### Player Notes

- Only fighters need to worry about the platform jump mechanic
- The module handles the jump automatically -- no manual intervention needed
