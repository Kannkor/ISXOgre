# Yon Gorroth: The Infinite Abyss [Raid]

**Expansion:** Rage of Cthurath (Exp 22)

This zone has 3 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Setup Name | Description |
|------|-----------|-------------|
| [Dondari, Darou Archmage](#dondari-darou-archmage) | Dondari, Darou Archmage | Handles curse, aggro, and jousting |
| [Frejn, Darou Protector](#frejn-darou-protector) | Frejn, Darou Protector | WIP |
| [Tha'Bael the Invader](#thabael-the-invader) | Tha'Bael the Invader | WIP |

---

## Dondari, Darou Archmage

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

A reposition command is also available: `Obj_OgreMCP:PasteButton[OgreConsoleCommand,Dondari,-ExecuteEvent_AP,auto,DondariDarou_Reposition]`

### Overview

A raid encounter with timed curse curing, aggro management, and proximity-based jousting. The module handles all three major mechanics automatically.

### Requirements

- **Fighter** (designated tanks, placed at tank spot)
- **Priest** (curse cure disabled to prevent premature curing of Forced Procrastination)

### What the Module Does

**Setup:**

- Disables priest curse cures
- Disables enchanter Mana Flow, Manasoul, Channel, and Enchanted Vigor (cancels Enchanted Vigor if active)
- Disables guardian Recapture
- Disables channeler Emergency Power
- Disables Unfeeling Pack Mentality adorn for all
- Enables NPC cast monitoring on the boss
- All fighters are flagged as tanks and sent to the tank camp spot
- Non-tank-flagged fighters activate Subtle Strikes
- Non-tank-flagged toons get auto-target set to add then named
- Supports an alternate "land spots" position set via the `Dondari_UseLandSpots` variable

**Forced Procrastination Curse:**

- A 60-second curse that wounds health/power
- When a player gets the curse and is not the boss's current target, they move to the raid spot
- Fighters with the curse also stop offensive actions, activate Subtle Strikes, and are added to the fighter threat ignore list
- The module waits until the curse has 1-10 seconds remaining, then requests a curse cure
- Curing early heals the boss more (the heal is based on remaining duration), so delayed curing is critical
- When the curse clears, tank-flagged toons return to the tank spot and non-tanks reposition relative to the boss or add

**Spotted Weakness Aggro Management:**

- When a player gets Spotted Weakness, the module immediately:
    - Stops all offensive actions
    - Casts Subtle Strikes (stealth)
    - Adds the player to the fighter threat ignore list
- When the detriment clears, offensive actions resume and the ignore list is cleared
- Being targeted again while already having Spotted Weakness kills the group
- Announcements are posted to IRC

**Repair Robes Jousting:**

- NPC cast monitoring detects when the boss casts Maelstrom of Ice
- A 50-second on-screen countdown timer is displayed for the next Repair Robes
- 45 seconds after Maelstrom of Ice (5 seconds before Repair Robes is expected), non-tank-flagged toons move to a joust spot
- Once the Repair Robes detriment clears, the group returns to normal positions

**Add-Based Repositioning:**

- When "Archmage's Chosen" (the add) spawns, non-priest fighters position in front of it and non-fighters behind it
- Priests are excluded from repositioning and stay at their current position
- When the add despawns, the group repositions relative to the boss

### Player Notes

- On-screen timer shows countdown to next Repair Robes cast.
- IRC announcements are posted for Spotted Weakness and curse cure requests.
- Non-tank-flagged toons automatically joust away before Repair Robes hits and return after the detriment clears.
- The reposition command can be used to manually trigger repositioning relative to the boss or add.

---

## Frejn, Darou Protector

> **:warning: Work In Progress**
>
> This encounter's automation is still under development.

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A complex raid encounter with multiple overlapping mechanics including a tank-swap detriment, proximity-based jousting, several detriments requiring players to move away to self-cure, and timed group cures.

### Requirements

- **Fighter** (tanks, auto-target on named only, force-targets disabled)
- **Priest** (group cures triggered on demand)

### What the Module Does

**Setup:**

- All cures are disabled for the entire raid
- Disables enchanter Mana Flow, Manasoul, Channel, and Enchanted Vigor (cancels Enchanted Vigor if active)
- Disables guardian Recapture
- Disables channeler Emergency Power
- Disables Unfeeling Pack Mentality adorn for all
- Fighters get force-targets disabled, are sent to the tank spot, and get auto-target set to named only

**Prepared Stare (Tank Swap):**

- When a player gets Prepared Stare, the module immediately:
    - Stops all offensive actions
    - Casts Subtle Strikes (stealth)
    - Adds the player to the fighter threat ignore list
- When the detriment clears, offensive actions resume and the ignore list is cleared
- Being targeted again while already having Prepared Stare kills the player and heals the boss
- Announcements are posted to IRC

**Siphon Fortitude Jousting:**

- When Arcane Whirlwind hits, a 25-second on-screen timer for Siphon Fortitude is displayed
- 22 seconds after Arcane Whirlwind, non-fighters joust to a safe spot (if no other mechanic is active)
- Non-fighters return when Siphon Fortitude clears and a minimum wait period has passed

**Eye Gouge:**

- When a player gets Eye Gouge (and no other mechanic is active), they reposition to a dedicated spot
- An auto-cure is requested
- When the detriment clears, they return to normal position

**Strategic Misdirection:**

- Cannot be cured while near the boss or Frejn's Doomclock
- When a player gets this detriment (and no other mechanic is active), they are repositioned away from both the boss and the Doomclock
- The module picks the joust spot that is farther from the Doomclock
- When the detriment clears, they return to normal position

**Purge Physical Pain (GetAwayToCure):**

- When the chat message "prepares to purge physical pain" appears, the named player moves to an isolated cure spot
- The player self-cures with a Trauma cure
- A 25-second on-screen timer for Blinding Shockwave is displayed
- Any other active mechanic (Eye Gouge, Strategic Misdirection) is cleared to prioritize this

**Blinding Shockwave (GetAwayToCure):**

- When the chat message "begins to purge a blinding shockwave" appears, the named player moves to an isolated cure spot
- The player self-cures with a Noxious cure
- A 26-second on-screen timer for Noxious Whirlwind is displayed
- Any other active mechanic is cleared to prioritize this

**Group Cure Requests:**

- When Siphon Fortitude, Arcane Whirlwind, or Noxious Whirlwind is detected on the player, a group cure is requested from priests across the raid
- Group cure requests have a 3-second cooldown and a 10-second detection cooldown to prevent spam

**On-Screen Timers:**

- Siphon Fortitude: 25s after Arcane Whirlwind hits
- Purge Physical Pain: 24s after Siphon Fortitude hits
- Blinding Shockwave: 25s after Purge Physical Pain message
- Noxious Whirlwind: 26s after Blinding Shockwave message

### Player Notes

- On-screen timers display countdowns to each upcoming mechanic in the ability cycle.
- Multiple detriments require players to move away from the raid to self-cure -- the module handles this automatically.
- Only one repositioning mechanic is active at a time; higher-priority mechanics (Purge Physical, Blinding Shockwave) override lower-priority ones.
- IRC announcements are posted for Prepared Stare.

---

## Tha'Bael the Invader

> **:warning: Work In Progress**
>
> This encounter's automation is still under development.

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A raid encounter with two curse mechanics that require careful positioning, add management, and a timed ability cycle with on-screen timers.

### Requirements

- **Fighter** (force-targets disabled, auto-target on named)
- **Enchanter** (auto-target on named)
- **Priest** (curse cures disabled to prevent premature curing)

### What the Module Does

**Setup:**

- Disables priest curse cures
- Disables guardian Recapture
- Fighters get force-targets disabled
- Fighters and enchanters get auto-target set to named only
- Fighters briefly reposition the named by moving to a fighter reposition spot, then return to the main joust spot after 5 seconds
- The raid is repositioned based on add location (see below)

**Void Shackled II:**

- A 90-second curse that roots and silences the target; becomes dispellable after 5 seconds
- Curing it propagates the curse to any player within 10m
- When a player gets Void Shackled, the raid is notified and non-cursed players move to alternate joust spots (different spots for 1st vs 2nd+ cursed player)
- A cure is requested only when 2 or fewer other players are within 12m of the cursed player
- When all cursed players are cured, the fight resets positioning via SetUpFor

**Touch of Tha'Bael:**

- A 25-second curse that dazes and disables hostile spells within 15m
- A cure is requested when the curse has 10 or fewer seconds remaining, or when the number of cursed players equals or exceeds the number of nearby players (meaning everyone nearby already has it)
- When all cursed players are cured, the fight resets positioning via SetUpFor

**Timed Repositioning:**

- 20 seconds after Corrosive Wounding hits, everyone is repositioned to the home joust spot and add-based repositioning is blocked for 30 seconds
- 18 seconds after Invader's Dissection hits, fighters only are repositioned to the home joust spot

**Ancient Curse Jousting:**

- When the named "prepares to apply an ancient curse," everyone except the current tank (determined by target or 90%+ threat) jousts away to a safe spot
- A 7-second on-screen timer for Touch of Tha'Bael is displayed
- Fighters who are not tanking stop offensive actions
- Add-based repositioning is blocked for 20 seconds after the joust

**Add Management (Infectious Crawler):**

- When the add spawns or despawns, the raid repositions:
    - Fighters and enchanters go to the primary joust spot
    - Priests go to the joust spot farthest from the add
    - Other classes position near the add
- Add-based repositioning is suppressed while timed repositioning blocks are active

**On-Screen Timers:**

- Corrosive Wounding: 20s after Ferocious Snarl hits
- Void Shackled: 24s after Corrosive Wounding hits
- Invader's Dissection: 24s after Void Shackled hits
- Ancient Curse: 22s after Invader's Dissection hits
- Touch of Tha'Bael: 7s after Ancient Curse emote

### Player Notes

- On-screen timers display countdowns to each upcoming mechanic in the ability cycle.
- IRC announcements are used for cure coordination.
- The module automatically repositions the raid based on add location and active mechanics.
- Cure requests for Void Shackled are only sent when the cursed player is sufficiently isolated from others.
