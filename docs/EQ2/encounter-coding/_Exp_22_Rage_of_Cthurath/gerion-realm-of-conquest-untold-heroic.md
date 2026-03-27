# Gerion: Realm of Conquest [Untold Heroic]

**Expansion:** Rage of Cthurath (Exp 22)

This zone has 5 boss encounters with OgreBot automation modules. Each boss has a dedicated setup that handles fight mechanics automatically.

## Available Setups

| Boss | Setup Name | Description |
|------|-----------|-------------|
| [Sentry Dillius](#sentry-dillius) | Sentry Dillius | Mage dispels Pillar of Life/Veil of Lies. Priest dispels Pillar of Truth. HO on adds. Cures disabled |
| [Sergeant-at-Arms Strongiron](#sergeant-at-arms-strongiron) | Strongiron | Bulwark on Shield Barrage/Bone-Bound Armor. HO if Bulwark on CD. Joust on Leveraged Strike. Fighter auto-targets adds |
| [Dread Marshal Keread](#dread-marshal-keread) | Keread | Singled Out curse handling. Outmaneuvered triggers scout Escape. Class-specific positioning |
| [The Arm of Lucan](#the-arm-of-lucan) | Arm of Lucan | Mage dispels The Reckoning Cometh. Auto-targets Siege Breaker adds. Frontal assault dodge |
| [Lazirah Darkmoore](#lazirah-darkmoore) | Lazirah Darkmoore | Banner-based side detection. Defensive Pressure repositioning. Order of Execution add targeting. Mage's Block handling |

---

## Sentry Dillius

Setup is automatic when engaged.

### Overview

A fight with multiple dispel mechanics across the named and an add. The named has "Pillar of Life" (mage dispel) and "Pillar of Truth" (priest dispel). The add "a Spirit of Truth" has "Veil of Lies" which mages dispel or non-mages remove via Heroic Opportunities. Cures are disabled during the encounter.

### Requirements

- Must have a **mage** in the group for dispelling Pillar of Life and Veil of Lies
- A **priest** (healer 1) is flagged for Pillar of Truth dispel

### What the Module Does

**Pillar of Life (on named):**

- Mage automatically dispels the buff from the named when ready

**Pillar of Truth (on named):**

- The first priest (healer 1) is flagged at setup
- Flagged priest dispels using ability or item fallback (`DispellNPCWithAny`)

**Veil of Lies (on add "a Spirit of Truth"):**

- Mage automatically dispels when ready
- Non-mages start a Heroic Opportunity on the add (4-second cooldown between attempts)

**Other Settings:**

- Cures disabled for the encounter, re-enabled when named dies
- NPC cast monitoring enabled
- HO Starter and HO Wheel enabled for all
- Auto-target enabled for all: "a Spirit of Truth" first, then the named

### Player Notes

- Cures are turned off for this fight -- this is intentional
- Auto-targeting is enabled for everyone, not just the fighter

---

## Sergeant-at-Arms Strongiron

Setup is automatic when engaged.

### Overview

A complex encounter with multiple mechanics. The named has "Bone-Bound Armor" that must be stripped with Bulwark of Order. When Bulwark is on cooldown, Heroic Opportunities are used to reset it. Players receive "Leveraged Strike" stacks that require jousting, and "Grave Error" curses that require description verification before curing. The add "a Risen Royal Antonican Guard" is auto-targeted by the fighter.

### Requirements

- Must have a **fighter** in the group for Bulwark of Order
- HO Starter, HO Wheel, and HO Change Target checkboxes are enabled automatically

### What the Module Does

**Shield Barrage:**

- When the named says "SHIELD BARRAGE!", the fighter casts Bulwark of Order immediately
- If Bulwark is on cooldown, a 3-second window watches for it to become available

**Bone-Bound Armor:**

- Monitors the "Bone-Bound Armor" buff on the named each pulse
- When increments are greater than 0, the fighter casts Bulwark of Order (8-second cooldown)

**Bulwark HO Fallback:**

- Independently checks every pulse: if the fighter's Bulwark is on cooldown, starts a Heroic Opportunity on the named to reset it
- 4-second cooldown to prevent spam

**Leveraged Strike Joust:**

- Non-fighters with "Leveraged Strike" stacks at or above the threshold are jousted to a safe spot using relative camp spots
- Returns to normal position when the curse falls off
- Default threshold is **5 stacks**, configurable per group

**Grave Error:**

- When a player receives "Grave Error", the module reads the curse description from the server
- Checks if the player's name, subclass, and race all appear in the description
- If the description is correct, requests an auto-cure
- If incorrect, does nothing (curing with wrong description kills the player)
- Priest cure curses are disabled during this fight

**Auto-Target (Fighter):**

- Fighter auto-targets "a Risen Royal Antonican Guard" first, then the named

### Customization

**Leveraged Strike threshold** (default: 5):

To change the number of stacks before jousting:

```
oc !c -Set_Variable igw:${Me.Name} Strongiron_LeverageStacks NUMBER
```

Replace `NUMBER` with the desired stack count.

### Player Notes

- The fighter should focus on the named -- Bulwark and HO management is automatic
- If you are not a fighter and get Leveraged Strike, you will be moved automatically
- Grave Error cures are automatic -- do not try to manually cure

---

## Dread Marshal Keread

Setup is automatic when engaged.

### Overview

The named applies "Singled Out" curses to players. Curing this curse has strict positioning requirements -- incorrect curing kills the target (and potentially nearby cursed allies). The named also applies "Outmaneuvered" which requires a scout to cast Escape.

### Requirements

- Must have a **scout** in the group (used as the cure partner and for Escape)

### What the Module Does

**Singled Out Handling:**

When a player receives "Singled Out", the module waits 15 seconds then positions players based on the cursed player's class:

- **Scout with curse:** Moves to the joust spot alone. Once in position with no other PCs within 10 meters, requests a cure. Scouts survive being cured alone.

- **Fighter with curse:** Moves everyone in the group to the joust spot *except* the fighter and the first scout. The fighter and scout remain at the raid spot. Once in position with exactly 1 other PC nearby (the scout), requests a cure.

- **Other class with curse:** Moves to the joust spot along with the first scout. Once in position with exactly 1 other PC nearby (the scout), requests a cure. Having one scout nearby resets the priest's cure and prevents the curse from transferring.

**Outmaneuvered Handling:**

- When any player detects the "Outmaneuvered" debuff, they fire a cross-session event every 8 seconds while the debuff persists
- On the receiving end, scout 1 checks if Escape is ready and casts it
- If scout 1's Escape is not ready, the next scout in the group is tried
- 5-second cooldown on Escape attempts to prevent spam

**Positioning Verification:**

- Waits until the cursed player is at their camp spot before requesting cure
- Verifies the correct number of nearby PCs using actor count checks
- All relative camp spots are cleared when the curse falls off or the named dies

### Player Notes

- Do **not** manually cure Singled Out -- the module handles positioning and timing
- Priest cure curses are disabled during this fight
- The 15-second delay before movement is intentional -- allows time for the initial curse damage to stabilize

---

## The Arm of Lucan

Setup is automatic when engaged.

### Overview

The named has a buff called "The Reckoning Cometh" that must be dispelled by a mage. Siege Breaker adds spawn during the fight. The named also performs a "frontal assault" that requires the group to move behind the boss.

### What the Module Does

**The Reckoning Cometh dispel:**

- Mage automatically dispels the buff from the named when the dispel ability is ready
- Non-mages skip this check entirely for performance

**Auto-target adds (Fighter):**

- Fighter automatically targets "Siege Breaker" adds with the named as the primary target

**Frontal Assault:**

- When the named announces "prepares for a frontal assault", a 2-second timer starts
- After the delay, all characters (including the tank) are moved behind the named using `SetCS_BehindNPC`

**Stand up:**

- Automatic stand-up handling is active for this zone

### Player Notes

- Must have a **mage** in the group for dispelling
- Fighter handles add pickup automatically
- The group will automatically move behind the boss during frontal assault -- do not manually reposition

---

## Lazirah Darkmoore

Setup is automatic when engaged.

### Overview

A complex encounter with two sides to the room (Lucanic and Qeynos), determined by banner positions. Multiple mechanics require players to move between sides relative to the boss. The named applies "Defensive Pressure" (requiring opposite-side positioning), "Tap Strength" (requiring same-side positioning), and "Order of Execution" (requiring targeted add kills). Adds "a Lucanic Wraithlancer" have "Mage's Block" that requires a mage on the Lucanic side.

### Requirements

- Must have a **mage** in the group (for Mage's Block positioning)
- Must have a **fighter** in the group (for add targeting and Bulwark)

### What the Module Does

**Setup:**

- Cures and cure curses disabled for the encounter
- All characters moved to a starting camp spot
- Banner positions resolved to determine Lucanic vs Qeynos sides
- Fighter auto-targets "a Lucanic Wraithlancer" (only when HP <= 99%) then the named

**Defensive Pressure (highest priority):**

- When a player gets this elemental debuff, they must move to the opposite side of Lazirah
- The module checks which side the named is on by comparing the named's location to the two banner positions
- The player is moved to the camp spot on the opposite side
- An autocure is requested after repositioning
- Re-checks every 6 seconds in case the named moves
- When the debuff falls off, the player stays where they are (no snap-back)

**Tap Strength:**

- When a player gets this debuff, they must be on the **same side** as the named
- Fighter casts Bulwark of Order on first detection
- The module moves the player to the camp spot on the named's side
- Defensive Pressure takes priority -- if both are active, Defensive Pressure positioning wins

**Order of Execution:**

- When a player gets this curse, the module scans all "a Militia Guard" adds for the one with the matching "Order of Execution" debuff (different icon IDs than the player version)
- If a matching add is found, a cross-session event tells all fighters to retarget: the specific add by ID first, then the default target list
- The add's ID is cached -- no rescanning while it's alive
- Once the add is killed, the module tracks that a kill has occurred
- Only after an add has been killed AND the debuff duration is under the threshold will the module request an autocurse (8-second cooldown between requests)
- Announces via `oc` when the debuff is gained and when it falls off

**Mage's Block:**

- When "a Lucanic Wraithlancer" has the "Mage's Block" debuff, the mage is moved to the Lucanic side camp spot
- Defensive Pressure takes priority -- the mage will not be moved for Mage's Block while Defensive Pressure is active
- Once Defensive Pressure clears, Mage's Block can re-evaluate and move the mage again

**Banner Resolution:**

- On setup, the module finds the two banner actors (`boss_05_banner_lucanic_side` and `boss_05_banner_qeynos_side`) and records their positions
- Two fixed camp spots near the banners are compared to the banner positions to determine which spot is on which side
- If banners aren't available at setup, resolution is retried each pulse

### Player Notes

- Cures and cure curses are disabled for this fight -- this is intentional
- Positioning is automatic -- do not manually reposition between sides
- The fight uses absolute camp spot changes (not relative), so characters stay on whatever side they were last moved to
- When Defensive Pressure and Tap Strength are both active, Defensive Pressure always wins

<!-- Source: Generated from Gerion_Realm_of_Conquest_Untold_Heroic.iss raid module -->
