# Gerion: Realm of Conquest [Untold Heroic]

**Expansion:** Rage of Cthurath (Exp 22)

This zone has 4 boss encounters with OgreBot automation modules. Each boss has a dedicated setup that handles fight mechanics automatically.

## Available Setups

| Boss | Setup Name | Description |
|------|-----------|-------------|
| [Sentry Dillius](#sentry-dillius) | Sentry Dillius | Mage dispels Pillar of Life. Cures disabled |
| [Sergeant-at-Arms Strongiron](#sergeant-at-arms-strongiron) | Strongiron | Bulwark on Shield Barrage/Bone-Bound Armor. HO if Bulwark on CD. Joust on Leveraged Strike |
| [Dread Marshal Keread](#dread-marshal-keread) | Keread | Singled Out curse handling with class-specific positioning |
| [The Arm of Lucan](#the-arm-of-lucan) | Arm of Lucan | Mage dispels The Reckoning Cometh. Auto-targets Siege Breaker adds |

---

## Sentry Dillius

Setup is automatic when engaged.

### Overview

A fight where the named has a buff called "Pillar of Life" that must be dispelled by a mage. Cures are disabled during the encounter to prevent interference with other mechanics. The named also casts "Unholy Touch" which is automatically interrupted.

### What the Module Does

- **Pillar of Life dispel** -- Mage automatically dispels the buff from the named when the dispel ability is ready
- **Cures disabled** -- All cures are disabled during the fight and re-enabled when the named dies
- **NPC cast monitoring** -- Enabled for the encounter
- **Unholy Touch interrupt** -- Automatically interrupted via NPC cast monitoring (XML-based)

### Player Notes

- Must have a **mage** in the group for dispelling
- Cures are turned off for this fight -- this is intentional

---

## Sergeant-at-Arms Strongiron

Setup is automatic when engaged.

### Overview

A complex encounter with multiple mechanics. The named has "Bone-Bound Armor" that must be stripped with Bulwark of Order. When Bulwark is on cooldown, Heroic Opportunities are used to reset it, making it available again. Players receive "Leveraged Strike" stacks that require jousting, and "Grave Error" curses that require description verification before curing.

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

The named applies "Singled Out" curses to players. Curing this curse has strict positioning requirements -- incorrect curing kills the target (and potentially nearby cursed allies). The module handles all positioning and cure timing automatically based on the cursed player's class.

### Requirements

- Must have a **scout** in the group (used as the cure partner for non-scouts)

### What the Module Does

**Singled Out Handling:**

When a player receives "Singled Out", the module waits 15 seconds then positions players based on the cursed player's class:

- **Scout with curse:** Moves to the joust spot alone. Once in position with no other PCs within 10 meters, requests a cure. Scouts survive being cured alone.

- **Fighter with curse:** Moves everyone in the group to the joust spot *except* the fighter and the first scout. The fighter and scout remain at the raid spot. Once in position with exactly 1 other PC nearby (the scout), requests a cure.

- **Other class with curse:** Moves to the joust spot along with the first scout. Once in position with exactly 1 other PC nearby (the scout), requests a cure. Having one scout nearby resets the priest's cure and prevents the curse from transferring.

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

The named has a buff called "The Reckoning Cometh" that must be dispelled by a mage. Siege Breaker adds spawn during the fight and are automatically targeted by the fighter.

### What the Module Does

- **The Reckoning Cometh dispel** -- Mage automatically dispels the buff from the named when the dispel ability is ready. Non-mages skip this check entirely for performance.
- **Auto-target adds** -- Fighter automatically targets "Siege Breaker" adds with the named as the primary target
- **Stand up** -- Automatic stand-up handling is active for this zone

### Player Notes

- Must have a **mage** in the group for dispelling
- Fighter handles add pickup automatically
