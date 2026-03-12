# Takish Badlands: The Boundless Gulf [Raid]

**Expansion:** Renewal of Ro (Exp 19)

!!! warning "Work in Progress"
    Automation for this zone is still under development. Some encounters may have limited or incomplete automation.

This raid zone contains 5 boss encounters.

## Available Setups

| Boss | Description |
|------|-------------|
| [Huhmuhngus Fuhngus Amuhngus](#huhmuhngus-fuhngus-amuhngus) | Vision/clicking mechanic, stack-based jousting |
| [Sleujess, Pride Guardian](#sleujess-pride-guardian) | Shield spawn jousting, on-screen timer |
| [Hambalumi](#hambalumi) | Depth charge joust out, drag joust in |
| [Ragtag the Despoiler](#ragtag-the-despoiler) | Stack and duration-based jousting |
| [Nirag the Boundless](#nirag-the-boundless) | On-screen add spawn timer, heal alerts |

---

## Huhmuhngus Fuhngus Amuhngus

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A complex fight involving a vision buff mechanic with add clicking, and stack-based jousting.

### What the Module Does

**Vision / Freihdy Fuhngus:**

- Tracks the Vision buff across archetypes
- Automatically clicks the Freihdy Fuhngus add to gain or refresh vision
- Moves the designated group (flag 4) to handle the vision mechanic

**All Tripped Up:**

- Tracks the All Tripped Up detriment stacks
- Automatically jousts out when stacks are high
- Automatically jousts back in when stacks are cleared

### Player Notes

- The vision mechanic requires clicking the Freihdy Fuhngus add — this is handled automatically
- Watch for the jousting transitions between in and out positions based on stack count
- Flag 4 players handle the group movement for the vision phase

---

## Sleujess, Pride Guardian

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with blue pyramid shield spawns that require jousting, and an on-screen timer to track the joust cycle.

### What the Module Does

**Shield Spawn Jousting:**

- Detects blue pyramid shield actor spawns
- Automatically jousts away from the shield location
- Displays a 75-second on-screen timer for the next joust cycle
- Uses a pre-joust timed event to prepare for repositioning

**Cat Positioning:**

- Flag 2 players are positioned at a designated cat spot

### Player Notes

- Watch the on-screen timer to prepare for the next shield spawn
- Flag 2 players have a specific positioning role

---

## Hambalumi

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with two opposing mechanics: jousting out on depth charges and jousting in on drags.

### What the Module Does

**Depth Charge:**

- Automatically jousts out (away from named) when depth charge is detected

**Drag to the Depths:**

- Automatically jousts in (toward named) when drag is detected

**Tank Handling:**

- Flag 1 (tanks) are excluded from the joust mechanics

### Player Notes

- Two opposite joust directions — out for depth charge, in for drag
- Tanks (flag 1) stay in position during both mechanics

---

## Ragtag the Despoiler

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a stack-and-duration-based jousting mechanic.

### What the Module Does

**Cascade of Spoiling:**

- Tracks the Cascade of Spoiling detriment stacks and remaining duration
- Automatically jousts when stacks reach a threshold and the duration drops below 11 seconds

### Player Notes

- The joust timing is based on both stack count and remaining duration — the module handles this automatically
- Do not joust prematurely as the module waits for the optimal timing

---

## Nirag the Boundless

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with timed add spawns and preventable heal alerts.

### What the Module Does

**Add Spawn Timer:**

- Displays a 45-second on-screen timer for the next add spawn wave

**Preventable Heal Alert:**

- Sends alerts when a preventable heal is detected on the boss

### Player Notes

- Watch the on-screen timer to prepare for add spawns every 45 seconds
- Respond to heal alerts to prevent the boss from healing
