# Fabled Temple of Rallos Zek: Foundations of Stone [Raid]

**Expansion:** Chaos Descending (Exp 15)

This zone has 5 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Prime-Cornicen Munderrad](#prime-cornicen-munderrad) | Nox AE timer, curse tracking (Toxic Implosion) (WIP) |
| [Prime-Curator Undr](#prime-curator-undr) | Knockback AE timer (WIP) |
| [Proto-Exarch Finnrdag](#proto-exarch-finnrdag) | Summon and red text HUD timers (WIP) |
| [Supreme Imperium Valdemar](#supreme-imperium-valdemar) | Reflect mechanic (auto cancel cast + self target) (WIP) |
| [Statue of Rallos Zek](#statue-of-rallos-zek) | HUD timers, red text jousting, curse alert, add targeting (WIP) |

---

## Prime-Cornicen Munderrad

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

!!! warning "Work in Progress"
    This encounter's automation is still under development.

### Overview

A fight with AE timing and curse tracking.

### What the Module Does

**Nox AE Timer:**

- HUD displays a 30-second countdown when Toxic Tornado hits

**Curse Tracking (Toxic Implosion):**

- Parses the cursed player's name from combat text
- Displays the curse target on HUD and adds them to the cure curse queue

### Player Notes

- The HUD timers help coordinate healing around the AE pattern

---

## Prime-Curator Undr

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

!!! warning "Work in Progress"
    This encounter's automation is still under development.

### Overview

A fight with a knockback AE timer.

### What the Module Does

**Knockback AE Timer:**

- HUD displays a 40-second countdown when Cyclonic Freeze hits
- Different camp spots for group 1 vs other groups

### Player Notes

- Watch the HUD timer to brace for knockback

---

## Proto-Exarch Finnrdag

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

!!! warning "Work in Progress"
    This encounter's automation is still under development.

### Overview

A fight with summon and red text mechanics tracked via HUD timers.

### What the Module Does

**Summon Timer:**

- HUD displays a 36-second kill countdown when a destructor is summoned

**Red Text Timer:**

- HUD displays a 60-second countdown on red text announcement

### Player Notes

- Kill the summoned destructor before the timer expires

---

## Supreme Imperium Valdemar

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

!!! warning "Work in Progress"
    This encounter's automation is still under development.

### Overview

A fight with a reflect mechanic that requires stopping attacks.

### What the Module Does

**Reflect Mechanic:**

- When the boss reflects attacks, displays a 15-second HUD countdown
- If the character is targeting the boss, automatically cancels the current spellcast and targets self
- Prevents casting offensive spells during the reflect window

### Player Notes

- Group 1 priests have a separate camp spot from other characters

---

## Statue of Rallos Zek

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

!!! warning "Work in Progress"
    This encounter's automation is still under development.

### Overview

A fight with multiple timed mechanics and add management.

### What the Module Does

**HUD Timers:**

- Trauma AE countdown (30 seconds)
- Nox AE countdown (30 seconds)
- Red text countdown (60 seconds)

**Red Text Jousting:**

- When the statue prepares a devastating blow, all characters move to the position player

**Curse Alert:**

- Broadcasts a cure curse request to the raid when cursed

**Add Targeting:**

- When a greater warboar spawns, group 2+ fighters auto-target it

### Player Notes

- Multiple timed mechanics overlap -- the HUD timers help track them all
