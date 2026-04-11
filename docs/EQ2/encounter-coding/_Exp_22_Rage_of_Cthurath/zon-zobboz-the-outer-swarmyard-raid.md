# Zon Zobboz: The Outer Swarmyard [Raid]

**Expansion:** Rage of Cthurath (Exp 22)

This zone has 4 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Setup Name | Description |
|------|-----------|-------------|
| [Oogiloi Eye](#oogiloi-eye) | Oogiloi | YOU must handle looting of the item. The using of the item is automated |
| [Illicus, Zon Zobboz Swarmer](#illicus-zon-zobboz-swarmer) | Illicus | YOU must handle the mezzing. The rest is automated. The person mezzing will have to come back to get cures |
| [The Summoned Swarmguard](#the-summoned-swarmguard) | The Summoned Swarmguard | Delay cures Overloading Destruction curse and auto-targets adds |
| [Cuko the Watcher](#cuko-the-watcher) | Cuko the Watcher | Delay cures Void Shackled curse. Positioning |

---

## Oogiloi Eye

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter where the boss becomes immune with Void Bubble of Protection. Players must loot Voidborne Spears from Oogiloi Lancer adds and use them on the boss. The module automates item usage but players must loot the spear manually.

### Requirements

- **Fighter** (auto-uses Voidborne Spear, manages aggro)

### What the Module Does

**Void Bubble Detection and Item Use:**

- When the boss gains Void Bubble of Protection, a TTS "Void Protection" alert is given to fighters
- If the player has a Voidborne Spear in inventory, the module automatically uses the item on the boss

**Aggro Lock Handling:**

- When the boss locks aggro to a specific fighter:
    - That fighter enables all threat/force target options
    - All OTHER fighters disable threat increases, stop offensive attacks, and cast Subtle Strikes
- When the aggro lock ends, all settings are restored

### Player Notes

- **You must manually loot the Voidborne Spear** from Oogiloi Lancer adds. The module only automates using it.
- TTS alert when Void Bubble appears.
- Automatic threat management during aggro lock phases.

---

## Illicus, Zon Zobboz Swarmer

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter with a reflect phase and a spreading curse that requires players to spread out. The module handles reflect phase management and curse jousting, but mezzing must be done manually.

### Requirements

- **Fighter** (auto-target, reflect handling)
- **Priest** (curse curing enabled)

### What the Module Does

**Reflect Phase Handling:**

- When the boss gains its reflect buff:
    - Displays a 45-second on-screen "REFLECT UP" timer
    - Fighters receive a TTS "reflect up" alert
    - Turns off pets
    - Switches auto-target to adds ("a Summoned Swarmguard" and "Manifested Protector") plus self-targeting
    - PBAoE abilities are disabled
- When the reflect drops:
    - Auto-target returns to the boss
    - PBAoE is re-enabled
    - "Reflect down" TTS plays

**Crowded Animosity Joust:**

- When this curse appears, each cursed player is assigned a separate joust spot
- IRC announcements indicate which spot each player is heading to
- When the curse clears, positions are reset

### Player Notes

- **You must handle mezzing manually.** The module does not automate crowd control.
- The person doing the mezzing will need to return to the group to receive cures.
- On-screen timer and TTS for reflect phases.
- IRC announcements for joust spot assignments.

---

## The Summoned Swarmguard

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter with a propagating curse that must be delay-cured. Curing too early lets the boss power up; letting it expire also powers the boss. The module times cures precisely.

### Requirements

- **Fighter** (auto-targets adds)
- **Priest** (curse curing, managed by module)

### What the Module Does

**Delay Cure Logic:**

- Monitors the Overloading Destruction curse's remaining duration
- Only requests a curse cure when 15 seconds or less remain
- This ensures the curse is carried as long as safely possible while preventing expiration
- When cured, the curse propagates to a new target
- Priest curse cures are disabled to prevent premature curing

**Auto-Target:**

- Fighters auto-target adds in priority order:
    - "a Swarming Monstrous Elemental"
    - "a Swarming Deliquescent"
    - "a Swarming Goo"
    - The boss as fallback

### Player Notes

- All adds are automatically targeted in priority order.
- Curse cure timing is fully automated -- do not manually cure.
- On kill, priest curse curing is re-enabled after a short delay.

---

## Cuko the Watcher

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter with a spreading curse that roots the target. The module uses triangle positioning to prevent curse propagation and only cures when nearby players have moved away.

### Requirements

- **Priest** (curse curing, managed by module)

### What the Module Does

**Triangle Positioning:**

- The group is positioned at one of three triangle spots
- Everyone starts at spot 1
- When a player gets Void Shackled, all NON-cursed players move to a different spot (the cursed player stays put since they are rooted)
- Second curse instance moves remaining players to the third spot

**Proximity-Safe Cure Logic:**

- The module only requests a curse cure when the cursed player has 2 or fewer other players within 10 meters
- This prevents the curse from propagating to nearby players when cured
- Priest curse cures are disabled to prevent premature/unsafe curing

**Curse Round Tracking:**

- The module tracks how many players are currently cursed
- When all cursed players are cured (count reaches 0), everyone resets to the starting position

### Player Notes

- Automatic triangle positioning prevents curse propagation.
- Do not manually cure -- the module manages proximity-based cure timing.
- On kill, priest curse curing is restored.
