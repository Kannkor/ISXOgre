# Gerion: Dominion of Pain [Untold Heroic]

**Expansion:** Rage of Cthurath (Exp 22)

This zone has 5 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Setup Name | Description |
|------|-----------|-------------|
| [Sir Rendal Cauldthorn](#sir-rendal-cauldthorn) | Rendal | Full auto |
| [The Exhumed Executioner](#the-exhumed-executioner) | Executioner | Full auto |
| [The Soulbleeder](#the-soulbleeder) | Soulbleeder | Full auto |
| [Dominator Zerada](#dominator-zerada) | Zerada | Auto Bulwark |
| [Raynax S'Vere](#raynax-svere) | Raynax | Full auto. WIP. Not perfect |

---

## Sir Rendal Cauldthorn

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A multi-phase encounter where the group must complete Heroic Opportunities to trigger lights, then click lights and spawn Knights of Truth to reduce the boss's stacking buff. The fighter drives the group through the entire encounter.

### Requirements

- **Fighter** drives the fight logic (clicking lights, spawning knights, HO starts)

### What the Module Does

**Heroic Opportunity Management:**

- Enables HO starter and HO wheel for the whole group
- The fighter starts HOs on the named to trigger the "Light Shines" mechanic

**Knight of Truth Spawning:**

- The fighter automatically clicks light objects to spawn "a Knight of Truth" adds
- Knights reduce the "Truth Hurts" stacks on the boss

**Group Pathing:**

- The module moves the entire group in stages (center, halfway, final) to both north and south areas
- Waits for all members to arrive at each waypoint before advancing
- A special finale process handles the final lights when the boss reaches very low health

**Auto-Target:**

- Fighters target "a Knight of Truth" adds before the named

### Player Notes

- Fully automated fight flow -- the fighter drives the group through the encounter from north to south.
- The group moves together with the module checking that all members have arrived before proceeding.

---

## The Exhumed Executioner

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter involving a verdict system and ward management through Heroic Opportunities. Mages dispel postures off the boss while fighters manage HOs.

### Requirements

- **Mage** (dispels postures off the boss)
- **Fighter** (starts HOs to manage wards)

### What the Module Does

**Verdict System:**

- Detects whether the player has "Verdict: Guilty" or "Verdict: Innocent"
- If Guilty, automatically requests a cure

**Ward / HO Management:**

- When the boss has "Up Ward" active, the fighter starts an HO to shift it back to "Down Ward"
- 7-second cooldown between HO attempts

**Posture Dispelling:**

- Mages automatically dispel "Upward Offensive Posture" and "Downward Defensive Posture" off the boss

**Cure Management:**

- All cures are disabled during this fight to prevent harmful interactions
- HO starter and HO wheel are enabled

### Player Notes

- Fully automated -- mages dispel postures, fighters start HOs, and guilty verdicts are auto-cured.
- On kill, all HO and cure settings are restored.

---

## The Soulbleeder

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A blood pool rotation encounter where the boss cycles through three blood types. Each blood type requires a specific archetype to stand in the corresponding pool.

### Requirements

- **Fighter** -- goes into the Dragon pool
- **Priest** -- goes into the Wyvern pool
- **Scout or Mage** -- goes into the Drake pool

### What the Module Does

**Blood Pool Rotation:**

- Monitors three detriments on the boss: Blood of the Dragon, Blood of the Drake, and Blood of the Wyvern
- When a blood type activates, the module moves the entire group to the corresponding pool area
- The assigned archetype stands in the pool center; everyone else goes to a nearby safe spot

**Role Assignment:**

- At higher tiers: Scouts and mages are assigned to Drake duty, priests to Wyvern duty
- At lower tiers: A bard (or first scout) handles Drake, first priest handles Wyvern

**Curse Cure Safety:**

- Priest curse cures are disabled during the fight
- The module detects Dragonrot, Wyvernrot, and Drakerot curses on the player
- Cure requests are only sent when the corresponding blood phase is NOT active (safe to cure)

### Player Notes

- Camp spots shift dynamically as the boss cycles through blood phases.
- The group automatically moves to the correct pool area without manual intervention.
- On kill, curse cure settings are restored.

---

## Dominator Zerada

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter where the boss builds stacks of "High Horse" that wipe the raid at 100 stacks. Fighters counter this with Bulwark of Order. The boss also announces frontal/behind attacks that require repositioning.

### Requirements

- **Fighter** (casts Bulwark of Order to counter High Horse)

### What the Module Does

**Bulwark of Order:**

- When the boss's "High Horse" buff reaches 40 or more stacks, the fighter auto-casts Bulwark of Order to remove it
- 7-second cooldown between casts

**Front/Behind Jousting:**

- When the boss announces an attack "in front of her," all players move behind the boss (after a 2-second delay)
- When the boss announces an attack "behind her," all players move in front (after a 2-second delay)
- After 5 seconds, players return to their normal camp spots

**Auto-Target:**

- Fighters auto-target "a Lucanic Enforcer" adds before the boss

### Player Notes

- The primary automation is the auto-Bulwark. The joust system for front/behind attacks is also fully automated.

---

## Raynax S'Vere

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

> **:warning: Work In Progress**
>
> This encounter's automation is not perfect. Some mechanics may require manual intervention.

### Overview

A complex multi-phase encounter involving pad assignments, guillotine mechanics, conditional curing, and HO-based boss buff removal.

### Requirements

- **Fighter** (manages auto-target, HO starts for Lifeblood, Guillotine handling)
- **Mage** (cures Crime and Punishment)
- **Priest** (cures Caged Beneficials and Grave Shackles)

### What the Module Does

**Undying Authority Pad Assignment:**

- When the boss has "Undying Authority" stacks, each group member is moved to stand on a "souls of the forgiven" pad
- Players are assigned to pads based on their group order
- All cure requests are suppressed during this phase

**Guillotine Slash Handling:**

- When a player gets Guillotine Slash, they move to a safe joust spot
- A group mate mimics their movement for safety
- The module waits for Undying Authority stacks to reach 0, then requests a priest cure
- NPC cast monitoring attempts to interrupt the Guillotine Slash cast

**Guilt Bubble / Solitary Confinement:**

- When a player is elevated (Y coordinate > 15), indicating they are in a cage, the module:
    - Disables camp spot following
    - Scans for "boss_05_sphere_guilt" (guilt bubble) actors
    - Automatically clicks the guilt bubble to break free
    - Returns the player to their camp spot after escaping

**Conditional Curing:**

- Crime and Punishment: Detected on the player, requests a mage-only cure
- Caged Beneficials / Grave Shackles: Detected on the player, requests a priest cure

**Auto-Target:**

- Fighters auto-target "guilty conscience" and "Blades of Captivity" adds before the boss

**Lifeblood of The Overlord:**

- When this buff is on the boss (reduces damage by 90%), the fighter starts an HO to remove it

**Cure Management:**

- All cures, curse cures, and resurrections are disabled at setup
- Re-enabled when the boss dies

### Player Notes

- Complex multi-phase fight with pad assignments, jousting, and conditional cure requests.
- The module actively suppresses cures during dangerous phases to prevent accidental deaths.
- HO starter and HO wheel are enabled during the fight.
