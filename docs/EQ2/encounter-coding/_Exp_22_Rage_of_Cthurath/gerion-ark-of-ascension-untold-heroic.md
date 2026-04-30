# Gerion: Ark of Ascension [Untold Heroic]

**Expansion:** Rage of Cthurath (Exp 22)

This zone has 5 boss encounters with OgreBot automation modules. Each boss has a dedicated setup that handles fight mechanics automatically.

## Available Setups

| Boss | Setup Name | Description |
|------|-----------|-------------|
| [The Dogmadog](#the-dogmadog) | Dogmadog | Tank uses inverters to manage adds |
| [Nazkun](#nazkun) | Nazkun | Fully automated. Requires a scout and mage |
| [Surinon](#surinon) | Surinon | Fully automated. Requires a scout |
| [Xelha Nevagon](#xelha-nevagon) | Xelha | Fully automated |
| [Paragon of the Overlord](#paragon-of-the-overlord) | Paragon | Fighters auto-switch stance for adds. Auto-curing |

---

## The Dogmadog

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A straightforward encounter where the tank manages spawning adds using inverter items. OgreBot monitors add counts and automatically uses inverters when needed.

### Requirements

- Fighter (tank) should have **inverters** in inventory. A warning will be displayed during setup if none are detected.

### What the Module Does

- **Add monitoring** -- Tracks the number of "a heretick" adds in the encounter area
- **Inverter usage** -- The fighter automatically uses an inverter on the boss when the add count falls below threshold:
    - Fewer than 3 adds present: Uses inverter
    - Fewer than 6 adds present AND any add is below 50% health: Uses inverter
- **Throttle** -- 5-second cooldown between inverter uses to prevent spam

### Player Notes

- The tank handles add management. Other group members just DPS as normal.
- If the fighter does not have inverters, adds must be managed manually.

---

## Nazkun

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

Nazkun spawns sconces in different locations that must be clicked in sequence. Two group members are assigned as runners to handle the two sconce detriment phases.

### Requirements

- Must have a **scout** in the group -- handles the first detriment phase
- Must have a **mage** in the group -- handles the second detriment phase

### What the Module Does

**Role Assignment:**

- **First Detriment Handler** (first Scout): Clicks sconces when the first detriment appears on the boss
- **Second Detriment Handler** (first Mage): Clicks sconces when the second detriment appears

**Detriment Tracking:**

- Monitors two separate detriments on the boss that indicate sconces have spawned
- First detriment triggers the scout to begin clicking sconces
- Second detriment (when the first detriment is no longer active) triggers the mage to handle sconces at the alternate location

**Sconce Clicking:**

- Each phase has up to 6 sconces to click in sequence (01 through 06)
- The assigned runner automatically moves to each sconce, clicks it, then advances to the next
- Sconces are named by location (center or left side of the room)

**Teleporter Navigation (Second Detriment Phase):**

- When the second detriment is active, the mage may need to navigate through a teleporter to reach sconces in the opposite room
- The module moves the mage through the teleporter, adjusts camp spots after arrival, clicks the sconces, then returns the mage through the return teleporter back to center
- Camp spots for the rest of the group are adjusted after teleporting as well

### Player Notes

- Once set up, the scout and mage handle their respective sconce phases without manual input.
- The scout handles sconces in whichever room they are currently in. The mage navigates to the alternate room if needed.

---

## Surinon

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

Surinon (Apostle of Pain) is a multi-room encounter involving curse management, Heroic Opportunities (HOs), and a runner who clicks sconces in side alcoves. The fight takes place across a center room with teleporters to left and right alcoves.

### Requirements

- Must have a **scout** in the group -- acts as the runner for sconce mechanics

### What the Module Does

**Runner Assignment:**

- The first scout in the group is designated as the runner
- The runner travels between alcoves to click sconces when Pain Management stacks appear on the boss

**HO (Heroic Opportunity) Management:**

- HO Starter and HO Wheel are enabled for all group members at setup
- When any player has the **Tenets of Torment** curse, the module automatically starts a Heroic Opportunity
- Completing the HO removes Tenets of Torment and the associated Pleasure from Pain buff
- 5-second cooldown between HO attempts

**Curse Cure Safety:**

- Priest curse cure is **disabled** during this fight (priests cannot freely cure curses)
- The module only requests a curse cure when it is safe:
    - Surinon's Pain Management on the boss has 0 increments, OR
    - The player has 7 stacks of Pain Management (would die at 8 -- emergency cure)
- 8-second throttle between cure requests

**Sconce Mechanics (Runner):**

- When Pain Management increments appear on the boss, the runner acts:
    - Checks which teleporter has a red sparkle aura (indicating the active alcove)
    - If the active sconce is in the center room, clicks it directly
    - If the active sconce is in a side alcove, navigates through the teleporter, clicks the sconce, then returns through the return teleporter back to center
- Sconces are clicked sequentially; the runner loops through all available interactable sconces in the alcove

### Player Notes

- Keep the group at the center camp spot. The runner handles all sconce mechanics.
- Do NOT manually cure curses -- the module manages curse timing to prevent deaths.
- The module enables HO Starter and HO Wheel UI options during the fight.
- On kill, the module cancels any remaining detriments and restores cure settings.

---

## Xelha Nevagon

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

Xelha Nevagon is a positioning-heavy fight involving a spreading disease (Dismal Phage) that must be carefully managed. The boss moves between three locations, and the group must follow while keeping infected players isolated.

### Requirements

- No strict class requirements, but the module assigns roles based on available archetypes.

### What the Module Does

**Role Assignment (Flags):**

| Flag | Role | Assigned To |
|------|------|-------------|
| Flag 1 | First Phage receiver / joust out | First Scout |
| Flag 2 | Second Phage receiver / joust out | First Mage |
| Flag 3 | Group cure priest | First Priest |

**Dismal Phage Management:**

- **Dismal Phage** is a disease that spreads to the 2 nearest targets after 10 seconds, then every 20 seconds
- When a player gets Dismal Phage, the module immediately moves them to a **joust spot** away from the group
- The module also signals Flag 1 or Flag 2 players (based on which phage phase is active) to adjust their positioning -- flagged players joust out, non-flagged players move back to the camp spot
- This prevents the disease from reaching the rest of the group

**Boss Movement Tracking:**

The boss moves between three locations. The module detects which location the boss is at and adjusts camp spots accordingly:

| Location | Named Position | Group Spot | Joust Spot |
|----------|---------------|------------|------------|
| Center | Center of the room | Near center | Off to the side |
| West | Western platform | Western position | Western isolated spot |
| East | Eastern platform | Eastern position | Eastern isolated spot |

**Leap of Faith / Leap of Doubt:**

- When the boss casts Leap of Faith and the boss is more than 25 meters away, the module moves the group to the boss's position (10-second cooldown before moving again)
- The Flag 3 priest triggers a group cure when Leap of Doubt is active, the boss is distant (> 25 meters), and the player has Trauma damage -- 6-second throttle between group cures

### Player Notes

- Cures are **disabled** during this fight. The module manages disease spreading through positioning.
- Ability collision checks are disabled to prevent movement issues.
- The fight is fully automated once set up -- positioning and phage management happen without manual input.
- On kill, cures are re-enabled and camp spots are cleared.

---

## Paragon of the Overlord

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

The Paragon of the Overlord is the final boss of the zone. This encounter involves add management with stance switching, a statue mechanic, and careful cure management. The fight has specific positioning for each role.

### Requirements

- No strict class requirements, but fighters benefit from having supported subclasses for automatic stance switching.

### What the Module Does

**Camp Spot Placement:**

Each role gets a specific position around the boss:

| Role | Position |
|------|----------|
| Fighter (Tank) | Front of the boss |
| Priest 1 | Right side, front |
| Priest 2 | Right side, back |
| DPS 1 | Behind the boss |
| Enchanter | Back left |
| Others | General raid spot |

**Fighter Stance Switching:**

When adds spawn, fighters automatically manage their stance:

| Class | Offensive Stance | Defensive Stance |
|-------|-----------------|-----------------|
| Guardian | Forward Charge | Armored |
| Berserker | Abandoned Fury | Unflinching Will |
| Shadowknight | Dark Blade | Lucan's Pact |
| Paladin | Wrath Stance | Knight's Stance |
| Bruiser | Smoldering Fists | Bodyguard |

- When **"a fortified thrall"** (offensive add) spawns, the fighter cancels their defensive stance
- When **"an advancing thrall"** (defensive add) spawns, the fighter cancels their offensive stance and casts their defensive stance
- 5-second cooldown between stance changes
- A follow-up timer verifies the defensive stance was applied and retries if needed

> **:memo: Unsupported Classes**
>
> If your fighter's subclass is not listed above, a warning will appear during setup. Contact Kannkor with the exact spelling of your offensive and defensive stance names to get it added.

**Add Dispelling (Mages):**

- Mages automatically dispel **Paragon's Protection** from both "a fortified thrall" and "an advancing thrall" adds within 30 meters
- The module scans for the adds, checks if they have the protection buff, and targets them for dispelling

**Statue Mechanic:**

- When a player gets the **"Is Statue?"** debuff, the module:
    - Finds a matching statue (NoKill NPC with the same visual variant as the player)
    - Moves the player to the statue
    - Double-clicks the statue to break the debuff
    - Returns the player to their camp spot
- The engagement check also uses this debuff to detect if the fight is active even when the named NPC is not visible

**Shackled Senses:**

- When the **Shackled Senses** debuff is active (prevents beneficial spell casting), the module enables "ignore stun checks" so the bot continues operating
- Automatically toggled off when the debuff fades

**Cure Management:**

- All cures are **disabled** at the start of the fight
- The module manually monitors for Trauma, Arcane, and Noxious detriments
- If the player has any of these (and does NOT have an Elemental detriment), the module requests a cure
- 10-second throttle between cure requests

**Auto-Target:**

- Non-fighters are flagged for auto-targeting adds
- Both "a fortified thrall" and "an advancing thrall" adds are added to the auto-target list with the named as fallback
- When a relevant add is detected, the whole group is notified and target priority updates dynamically
- Scan radius set to 36 meters

### Player Notes

- Cures are disabled -- the module handles cure requests selectively (ignoring Elemental detriments).
- PBAoE abilities are disabled for fighters to prevent pulling unintended adds.
- Ability collision checks are disabled during this fight.
- On kill, all UI settings (cures, stances, collision checks, PBAoE, auto-target) are restored to normal.
