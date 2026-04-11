# The Oogothl Sprawl: Adkern's Pools [Raid]

**Expansion:** Rage of Cthurath (Exp 22)

## Available Setups

| Boss | Setup Name | Description |
|------|-----------|-------------|
| [Thet-ki-dua](#thet-ki-dua) | Thet-ki-dua | Add targeting, enchanter power drain support |
| [Adkern, the Thorned](#adkern-the-thorned) | Adkern, the Thorned | Add kill, joust for curse, immunity phase alerts |
| [Adkern, the Returned](#adkern-the-returned) | Adkern, the Returned | Shockwave jousting, add spawn timer |

---

## Thet-ki-dua

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter with an add ("a hiding reverent dancer") that periodically spawns and must be handled while DPSing the named.

### Requirements

- **Enchanters** should have Absorb Magic and PowerDrain-tagged abilities available in their cast stack.

### What the Module Does

**Auto-Target Configuration:**

- Fighters: Auto-targets the add first, then the named.
- Enchanters: Enables auto-target, targets the named first then the add, enables Absorb Magic and PowerDrain-tagged abilities.
- All characters are set to joust out.

**CampSpot Positioning (when CampSpot system is active):**

- When the add spawns, fighters move in front of the add and non-fighters move behind the add.
- When the add despawns, fighters move in front of the named and non-fighters move behind the named.

**On Named Kill:**

- Clears all auto-target actors.
- Enchanters: Disables auto-target, turns off Absorb Magic and PowerDrain.

### Player Notes

- Fighters will automatically swap positioning between the add and the named as the add spawns and despawns.
- Enchanters handle power drain duties on this fight.

---

## Adkern, the Thorned

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with an add ("Adkern's Loyal Voidpet") that must be killed, a curse ("Tortured Animosity") that requires the cursed player to joust away from other players, and an immunity phase where the boss becomes temporarily invulnerable.

### Requirements

- None specific. All classes are supported.

### What the Module Does

**Auto-Target Configuration:**

- All characters: Auto-targets the add and the named.

**CampSpot Positioning:**

- Fighters are placed at the fighter spot (near the boss).
- Mages are placed at the mage spot (further back).
- All other classes are placed at the raid spot (middle distance).
- All characters are set to joust out.

**Tortured Animosity Curse Handling:**

- Detects when "Tortured Animosity" is applied to the player (deals increasing damage for each player within 8m; can only be cured when no players are within 8m).
- When detected, the player is sent to the joust spot via Rally CampSpot (RCS).
- When the curse is removed, RCS is cleared and the player returns to their normal position.

**Immunity Phase:**

- When the boss "splashes a strange potion on himself," a TTS alert "Immune" is played for fighters.
- When the text "begins to dissolve Adkern" appears (immunity removed), a TTS alert "immunity gone" is played for fighters.

**On Named Kill:**

- Clears all RCS positions.

### Player Notes

- The curse mechanic is fully automated: cursed players will joust out and return automatically.
- Fighters receive audio alerts for the immunity phase to help them manage their attacks accordingly.
- The add should be killed as part of normal auto-target priority.

---

## Adkern, the Returned

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a periodically spawning add ("Adkern's Loyal Voidpet") and a shockwave mechanic that requires non-fighters to joust away from the boss.

### Requirements

- None specific. All classes are supported.

### What the Module Does

**Auto-Target Configuration:**

- Fighters: Auto-targets the add and the named.
- Non-fighters: No specific auto-target (target the named by default).

**CampSpot Positioning:**

- Fighters are placed at the fighter spot (closest to the boss).
- Mages are placed at the mage spot (furthest from the boss).
- All other classes are placed at the raid spot (middle distance).
- All characters are set to joust out.

**Shockwave Mechanic:**

- Triggered by the text "collects surrounding energy as he prepares to unleash."
- Fighters: Ignored (they stay at tank spot through the shockwave).
- Mages: Sent to the mage joust spot via RCS.
- All other non-fighters: Sent to the raid joust spot via RCS.
- After 10 seconds, RCS is cleared and everyone returns to their normal positions.

**Add Spawn Timer:**

- When the add spawns, a 55-second on-screen timer ("Next Add:") is displayed to track the next add spawn.

**On Named Kill:**

- Clears all RCS positions.

### Player Notes

- Shockwave jousting is fully automated for non-fighters. They will move out and return after 10 seconds.
- Fighters stay in position during shockwaves.
- Watch the on-screen timer for upcoming add spawns.
