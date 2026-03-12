# The Merchant's Den [Heroic II]

**Expansion:** Visions of Vetrovia (Exp 18)

This zone has 7 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Captain Twoshanks](#captain-twoshanks) | Magic square puzzle solving, race-based curse curing, add management |
| [Grimalda Goodhand](#grimalda-goodhand) | Auto-destroy vendor trash items |
| [Gelda Glintswift](#gelda-glintswift) | Bubble popping, add dispelling, Trade Secrets timed curse cure |
| [Elder Furdock](#elder-furdock) | Scroll combination puzzle with multi-toon coordination, jewelry box clicking |
| [Liegess Lavalle](#liegess-lavalle) | Blood In/Out jousting, Arch Enemy colored arch puzzle, lever matching |
| [Beefcake](#beefcake) | Directional reflection positioning, Three's a Crowd jousting, Death's Head intercept, cat familiar quest |
| [Arachlord Dyrraga](#arachlord-dyrraga) | Mage flag reading, Tangled Web silk thread, Behind the Schemes contract clicking, SURVIVE rotation, CC switching |

---

## Captain Twoshanks

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a magic square puzzle, race-based curse identification, and frozen add management.

### What the Module Does

**Magic Square Puzzle:**

- A 3x3 grid of "x" and "o" actors spawns on the floor
- The module maps each actor to a grid position, calculates which empty position makes two X positions sum to 15, and moves the group to the solution spot
- Mages then dispel "X marks the Spot" from the boss with coordinated timing

**Overboard Race-Based Curse:**

- Priests read the Overboard detriment's effect text to extract a race name
- The module matches the race to a group member and cures that specific person

**Frozen Bilge Add Management:**

- Frozen bilge adds take absolute priority over movement
- Camp spot changes are deferred until frozen adds are dead

### Player Notes

- The puzzle is solved automatically by reading the grid
- Curse curing targets the correct player by matching races

---

## Grimalda Goodhand

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A simple fight with automatic inventory cleanup.

### What the Module Does

**Auto-Destroy Vendor Trash:**

- Scans inventory every 3 seconds for items named "vendor trash" and destroys them automatically

### Player Notes

- Vendor trash items are cleaned up automatically during the fight

---

## Gelda Glintswift

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with bubble popping, add dispelling, and a timed curse mechanic.

### What the Module Does

**Bubble Popping (Enchanter):**

- A flagged enchanter moves to random bubble actors and clicks them
- In Challenge Mode, compares player's bubble stacks against the boss's stacks and only pops when behind

**Add Dispelling (Enchanter):**

- A second flagged enchanter finds lycan thug adds and dispels them using abilities or items

**Trade Secrets Curse:**

- When the Trade Secrets detriment lands, all movement halts
- When duration drops below 12 seconds, requests a curse cure from healers
- In Challenge Mode, waits for a chat confirmation before requesting the cure

### Player Notes

- Curse curing, dispels, and dazes are disabled on setup -- the module manages them
- Two enchanters handle bubble popping and add dispelling respectively

---

## Elder Furdock

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a multi-toon scroll combination puzzle and a jewelry box destruction mechanic.

### What the Module Does

**Scroll Combination Puzzle:**

- When the scroll unfurls, a flagged character clicks it to reveal a number sequence
- Each digit is assigned to a different flagged character via cross-session variables
- Each character navigates to and clicks their assigned block to enter the combination

**Jewelry Box Clicking:**

- After the combination succeeds, a flagged character moves to the jewelry box and clicks it to destroy it

**Bill of Lading Group Cures:**

- Priests monitor the Bill of Lading detriment stacks and fire group cures when stacks exceed 7

### Player Notes

- Non-fighter characters are assigned combination slots automatically
- The combination puzzle is solved cooperatively across multiple characters

---

## Liegess Lavalle

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with blood jousting, a colored arch puzzle, and lever matching mechanics.

### What the Module Does

**Blood In/Out Jousting:**

- Blood In: moves toward the boss, jumps, and requests a cure
- Blood Out: moves to the farthest joust spot from the boss
- Offensive casting stops during both mechanics

**Arch Enemy Puzzle:**

- When the Arch Enemy detriment is active, colored symbol arches (red/yellow/blue) spawn
- The module maps symbol colors to arch positions and clicks them in sequence

**Lever Matching (Challenge Mode):**

- A flagged scout/bard scans portal and add symbol actors, matches them by heading, and signals a flagged enchanter to click the correct lever

### Player Notes

- Blood jousting direction depends on the specific detriment variant
- The arch puzzle and lever matching are solved automatically

---

## Beefcake

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A complex fight with directional reflection positioning, crowd jousting, intercept mechanics, and a cat familiar quest.

### What the Module Does

**Directional Reflection:**

- When the boss gains the reflection buff, all DPS stops
- The fighter reads a direction (North/South/East/West) from a detriment on the boss and moves the entire group to the correct cardinal position

**Three's a Crowd Jousting:**

- Three flagged characters joust away from the boss
- If a jouster has the Chew Toy detriment, a backup is called instead

**Death's Head Intercept:**

- When a player gets Death's Head, the fighter repeatedly casts Intercept on them until cured or 15 seconds elapse

**Cat Familiar Quest:**

- A flagged character finds the crone's familiar, clicks it, then clicks the old crone

### Player Notes

- Directional positioning is fully automated based on the boss's detriment
- Multiple mechanics run simultaneously -- the module coordinates all of them

---

## Arachlord Dyrraga

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

The most complex encounter in this zone with mage flag reading, web mechanics, contract clicking, a SURVIVE phase, and dynamic CC switching.

### What the Module Does

**Mage Flag Reading (Enchanter):**

- When mage flag actors spawn, a flagged enchanter moves to the flag, reads the UI to determine the owner's name, then commands that specific character to click the flag

**Tangled Web:**

- When the Tangled Web detriment is active and a silk thread exists, the group moves to the silk thread and it is added to the auto-target priority

**Behind the Schemes (Bard):**

- When the bard accumulates 2+ stacks, they go invisible, move to the door, and click "shady contract" objects until stacks are removed

**SURVIVE Phase:**

- When SURVIVE fires, all casting is disabled and the group rotates between 4 corner positions every 2 seconds to evade adds

**Silken Lining CC Switching:**

- Dynamically toggles which CC type is blocked (stun/stifle/daze/fear) based on the boss's announcements

### Player Notes

- Multiple mechanics run simultaneously
- The SURVIVE phase is fully automated with corner rotation
- CC type blocking switches dynamically during the fight
