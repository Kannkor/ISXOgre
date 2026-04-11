# The Oogothl Sprawl: Unseen Horrors [Raid]

**Expansion:** Rage of Cthurath (Exp 22)

## Available Setups

| Boss | Setup Name | Description |
|------|-----------|-------------|
| [Temper](#temper) | Temper | Joust for Raging Curse |
| [Agent of Disgust](#agent-of-disgust) | Agent of Disgust | Add tank management, GATC for Explosion of Disgust, Mental Disgust threat handling |
| [the Unseen](#the-unseen) | the Unseen | SP/VBE add management, fighter repositioning, power drain support |

---

## Temper

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where the boss places "Raging Curse" on players, which deals increasing damage and must be cured while the player is more than 30m away from Temper.

### Requirements

- None specific. All classes are supported.

### What the Module Does

**Auto-Target Configuration:**

- All characters: Auto-targets the named.

**CampSpot Positioning:**

- Fighters are placed at the tank spot (closest to the boss).
- Priests are placed at the priest spot (middle distance).
- All other classes are placed at the raid spot.
- All characters are set to joust out.

**Raging Curse Handling:**

- Detects when "Raging Curse" is applied to the player (deals increasing physical damage; can only be removed when the target is more than 30m from Temper).
- When detected, the player is sent to the joust spot via Rally CampSpot (RCS).
- When the curse is removed, RCS is cleared and the player returns to their normal position.

**On Named Kill:**

- Clears all RCS positions.

### Player Notes

- The curse jousting is fully automated. Cursed players will move to the joust spot and return once cured.
- Priests get their own dedicated position between the tanks and the raid to maintain healing range.

---

## Agent of Disgust

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A complex encounter with multiple disgust-themed debuffs that require careful threat and aggro management. An add ("a malglare aberration") spawns periodically, and the fighter tanking it must temporarily drop all threat on the named. The boss also places "Explosion of Disgust" which uses the Get Away To Cure (GATC) system, and "Mental Disgust" which permanently prevents the affected fighter from holding aggro on the named.

### Requirements

- **Guardian** or **Fighter** tank. Guardians will use Focus Offensive; other fighters use Singular Focus.
- Multiple tank classes are recommended to handle the add rotation.

### What the Module Does

**Setup Configuration:**

- Fighters: Dynamic Ignore PBAE is enabled.
- Guardians: Casts Focus Offensive.
- Other Fighters: Casts Singular Focus.
- All characters are set to joust out.

**Explosion of Disgust (GATC):**

- The "Explosion of Disgust" curse is handled via the Get Away To Cure system.
- When "senses a feeling of disgust building up" is detected, the affected player is reported to the GATC system.
- The player is automatically sent to one of three cure spots and must self-cure (Noxious type).

**Add Management (a malglare aberration):**

- When an add spawns, a 45-second on-screen timer ("Next Add:") is displayed.
- After 1 second, the module checks who the add is targeting.
- If the add targets your fighter:
    - All threat generation is disabled (no threat position increases, no force targets, no threat increases).
    - The fighter is added to the ThreatFighterIgnoreList so other fighters ignore them.
    - Subtle Strikes is cast to reduce threat.
    - Auto-target is switched to only the add.
    - A 25-second recovery timer is displayed ("Resuming Tanking Duties in:").
- After 25 seconds (AddTankRecovery):
    - If Mental Disgust is not active, threat generation is re-enabled and the fighter is removed from the ignore list.
    - Subtle Strikes is cancelled.
    - Auto-target is switched back to the named.

**Confounding Disgust Handling (Fighters):**

- When detected, all threat generation is disabled (the curse puts you at the bottom of the hate list).
- When removed, threat generation is re-enabled (unless Mental Disgust is still active).

**Mental Disgust Handling:**

- When detected, all threat generation is disabled and the fighter is added to the ThreatFighterIgnoreList (you cannot have aggro on the named again while this is active).
- When removed, threat generation is re-enabled and the fighter is removed from the ignore list (unless the add tank recovery timer is still running).

**On Named Kill:**

- Clears the ThreatFighterIgnoreList.
- Re-enables all threat generation options.
- Cancels Focus Offensive, Singular Focus, and Subtle Strikes.

### Player Notes

- This is a heavily automated fight with multiple interacting debuffs that affect fighter threat management.
- Fighters will automatically swap between tanking the named and handling the add as needed.
- The GATC system handles Explosion of Disgust automatically -- affected players will be moved to a cure spot.
- Mental Disgust effectively removes a fighter from the tanking rotation on the named. Multiple tanks are needed.
- Confounding Disgust temporarily suppresses threat while active; the module handles this automatically.

---

## the Unseen

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A complex encounter with two types of adds that require coordinated tank management. "Summoned presence" (SP) adds are time-based and lock onto fighters, while "Void-borne Emergence" (VBE) adds are health-based and heal the named. Fighters must dynamically reposition between the tank spot and joust spot based on which adds they are tanking. The boss also has a power drain mechanic that triggers a major debuff if a player falls below 5% power.

### Requirements

- **Multiple fighters** required for add tanking rotation.
- **Fighters in raid groups 3 or 4** are auto-flagged as FlagToon 1 (primary add tanks).
- **Enchanters** should have PowerDrain-tagged abilities and Cannibalize Thoughts available.
- **Warlocks** should have Dark Siphoning available (force myth setting is disabled for this fight).

### What the Module Does

**Setup Configuration:**

- Fighters: Placed at the tank spot, Dynamic Ignore PBAE enabled, force targets disabled, tank swapping prepared.
    - Guardians: Casts Focus Offensive, disables Champion's Interception.
    - Other Fighters: Casts Singular Focus.
    - Fighters in raid groups 3 or 4 are set to FlagToon 1.
    - Auto-targets the named.
- Non-Fighters: Placed at the raid spot.
- Enchanters: Auto-target enabled with 35m scan radius and 15m height, targets the named, enables PowerDrain and Cannibalize Thoughts, disables Channeled Focus/Absorb Magic/Mana Flow.
- Warlocks: Force myth on Dark Siphoning is disabled.
- All characters: Force named combat arts/abilities enabled, PowerRestore tag enabled, set to joust out.

**"I see YOU!" Mechanic:**

- When the boss says "I see YOU!", enchanters automatically cast Channeled Focus.

**Low Power Alert:**

- When a player falls below 5% power, the event is logged and announced via IRC.

**Summoned Presence (SP) Add Management (Fighters):**

- SP spawns are tracked by actor ID.
- When a fighter detects it is tanking an SP (the add is targeting them):
    - Threat generation (position increases, threat increases) is disabled.
    - The fighter is added to the ThreatFighterIgnoreList.
    - Auto-target is switched to the add.
    - RCS is cleared (fighter stays at tank spot with the add).
- When a fighter stops tanking an SP:
    - Threat generation is re-enabled.
    - The fighter is removed from the ThreatFighterIgnoreList.
    - Auto-target is switched back to the named.

**Void-borne Emergence (VBE) Add Management:**

- VBE spawns are tracked and announced via IRC (with named HP percentage) by the raid leader.
- VBE spawn/despawn is tracked by actor ID.

**Dynamic Fighter Positioning:**

- Fighters tanking any add: Stay at tank spot (RCS cleared).
- Fighters not tanking an add but an add is alive somewhere: Sent to the tank joust spot via RCS.
- Fighters with no adds alive: Stay at tank spot (RCS cleared).

**On Named Kill:**

- Resets all SP/VBE tracking.
- Clears the ThreatFighterIgnoreList.
- Re-enables all threat generation options.
- Disables force named combat arts/abilities.
- Cancels Focus Offensive and Singular Focus.
- Clears all RCS positions.
- Removes tank swapping preparation.

### Player Notes

- Fighter positioning is fully automated based on which adds are alive and who is tanking them.
- Fighters in raid groups 3 and 4 are prioritized as add tanks (FlagToon 1).
- Enchanters will automatically cast Channeled Focus when the boss uses "I see YOU!" to help manage the power drain mechanic.
- Keep power above 5% to avoid triggering the boss's major debuff. PowerDrain and PowerRestore abilities are enabled to help with this.
- VBE adds heal the named, so they should be killed quickly.
- Multiple SPs can be alive simultaneously; the module handles this by tracking which fighters are tanking which adds.
