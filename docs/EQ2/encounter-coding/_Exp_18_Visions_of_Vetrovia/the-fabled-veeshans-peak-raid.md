# The Fabled Veeshan's Peak [Raid]

**Expansion:** Visions of Vetrovia (Exp 18)

This zone has 8 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Kluzen the Protector](#kluzen-the-protector) | Mark warning jousting with minimum timer |
| [Elder Ekron](#elder-ekron) | Voltaic Mind Flay self-target |
| [Druushk](#druushk) | Statue clicking |
| [Taskmaster Nichok](#taskmaster-nichok) | Timed joust sequence on party summon |
| [Milyex Vioren](#milyex-vioren) | Power generator auto-targeting and positioning |
| [Xygoz](#xygoz) | Manual doppelganger clicking via MCP button |
| [Silverwing](#silverwing) | Mind's Eye archetype-specific clicking, add targeting |
| [Phara Dar](#phara-dar) | Gaze jousting with aggro verification |

---

## Kluzen the Protector

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a mark-based joust that includes a minimum timer to prevent premature return.

### What the Module Does

**Mark Warning Joust:**

- When marked by Kluzen, the character immediately offsets camp spot diagonally away
- A 10-second minimum timer ensures the character doesn't return too early
- Also monitors the Mental Protectorate detriment and jousts if detected
- Positions clear when the escape text fires and no detriment remains

### Player Notes

- The 10-second minimum timer prevents premature return from the joust

---

## Elder Ekron

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a self-targeting detriment.

### What the Module Does

**Voltaic Mind Flay:**

- When the detriment is detected, disables auto-target, saves the current target, and continuously targets self
- When the detriment clears, restores the original target and re-enables auto-target

### Player Notes

- Self-targeting is automatic during the detriment

---

## Druushk

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a statue clicking mechanic.

### What the Module Does

**Statue Clicking:**

- A flagged character searches for interactable dragon bust statue actors
- Automatically moves to the statue, clicks it, waits, then returns

### Player Notes

- Statue clicking is handled by the flagged character automatically

---

## Taskmaster Nichok

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a timed joust triggered by a party summon.

### What the Module Does

**Timed Joust Sequence:**

- When the party is summoned, two timed movements are scheduled:
    - At 13 seconds: moves the entire raid to a safe location
    - At 17 seconds: moves back to the boss with fighters in front and non-fighters behind

### Player Notes

- The joust is on a strict timer after the summon -- movement is fully automated

---

## Milyex Vioren

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with power generator add targeting.

### What the Module Does

**Power Generator Auto-Targeting:**

- The raid leader scans for power generators with health above 17%
- Sends cross-session commands to position the raid relative to each generator (fighters in front, non-fighters behind)
- After primary generators are dead, switches to a cleanup phase targeting remaining generators

### Player Notes

- Generator targeting and positioning is coordinated by the raid leader

---

## Xygoz

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a manual doppelganger clicking mechanic.

### What the Module Does

**Doppelganger Clicking:**

- An MCP console button is provided to trigger doppelganger clicking
- When activated, finds a NoKill NPC matching the player's name within 10m and double-clicks it

### Player Notes

- This mechanic is button-driven -- use the MCP console button to click your doppelganger

---

## Silverwing

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a Mind's Eye clicking mechanic and add targeting.

### What the Module Does

**Mind's Eye Click:**

- When a specific character can only see through their mind's eye, the module finds an archetype-specific target actor (e.g., priest_target for priests)
- Moves to the actor, performs a queued click, then clears camp spot
- Cleared when Silverwing becomes vulnerable again

**Add Targeting:**

- A flagged character scans for NamedNPC adds near Silverwing and auto-targets them
- When adds die, targeting reverts to Silverwing

### Player Notes

- The Mind's Eye click is archetype-specific and automated
- Add targeting rotates automatically between adds and the boss

---

## Phara Dar

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a gaze mechanic that requires dropping aggro before jousting.

### What the Module Does

**Gaze Jousting with Aggro Check:**

- When Phara Dar's Gaze is detected, auto-target is enabled on self to stop attacking and drop aggro
- The module waits in a loop until the boss is no longer targeting this character
- Only after aggro is fully transferred does the character move to the joust point
- When the gaze clears, positions reset and auto-target is cleared

### Player Notes

- The module ensures aggro is fully dropped before jousting
- Do not manually attack during the gaze -- the module handles the sequence
