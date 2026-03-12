# The Blinding: Twisted Vista [Raid]

**Expansion:** Blood of Luclin (Exp 16)

This zone has 4 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Thought Horror Overfiend](#thought-horror-overfiend) | Thought Gaze joust with 3-position rotation (WIP) |
| [Praetorian K'Tikrn](#praetorian-ktikrn) | Auto-joust on AE attack with 3-spot rotation |
| [Shik'Nar Imperiatrix](#shiknar-imperiatrix) | Delayed curse curing for Colony's Deadly Contagion |
| [Rockhopper Pouncer](#rockhopper-pouncer) | Auto-joust on pounce with egg-handling automation |

---

## Thought Horror Overfiend

> **:warning: Work In Progress**
>
> This encounter's automation is still under development. Some mechanics may not be fully automated yet.

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A jousting encounter where the Thought Gaze detriment forces the group to rotate through multiple positions. Both tank and raid positions cycle through 3 spots. Challenge mode (Thought Horror Aberration) is also supported.

### What the Module Does

**Thought Gaze Rotation:**

- When the Thought Gaze detriment is detected, the group automatically rotates to the next camp spot position
- Both tank and raid positions cycle through 3 positions
- Challenge mode (Thought Horror Aberration) uses the same rotation logic

### Player Notes

- The group rotates positions each time Thought Gaze is detected.
- There are 3 positions in the rotation for both tanks and non-tanks.
- Challenge mode (Thought Horror Aberration) is supported with the same mechanics.
- This module is a work in progress.

---

## Praetorian K'Tikrn

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A jousting encounter where the named performs a large AE attack (BLARRRRGRRRRRGG) that requires the group to move to the next position in a 3-spot rotation. Fighters and non-fighters have separate positions.

### What the Module Does

**AE Joust Rotation:**

- When the named performs its AE attack (BLARRRRGRRRRRGG), the group moves to the next camp spot in a 3-spot rotation
- Fighters and non-fighters have separate position sets
- The rotation cycles through all 3 positions before repeating

### Player Notes

- The group automatically repositions each time the AE attack fires.
- Fighters and non-fighters move to different positions.
- Three positions are used in a repeating rotation.

---

## Shik'Nar Imperiatrix

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter with the Colony's Deadly Contagion curse that must NOT be cured immediately. The curse must be allowed to tick down before it is safe to cure. Premature curing is dangerous.

### What the Module Does

**Delayed Curse Curing:**

- Monitors the Colony's Deadly Contagion curse duration on all players
- When the curse duration drops below 18 seconds remaining, the module requests a cure from all sessions
- Prevents premature curing by holding off until the safe window

### Player Notes

- Do NOT manually cure Colony's Deadly Contagion early -- the module handles the timing.
- Cures are only requested when the curse has less than 18 seconds remaining.
- Premature curing is dangerous and the module is designed to prevent it.

---

## Rockhopper Pouncer

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A jousting encounter where the named prepares to pounce and the group must move to avoid it. If marked, the player also handles rockhopper eggs by picking them up, carrying them to the brazier, and dropping them in.

### What the Module Does

**Pounce Jousting:**

- When the named prepares to pounce, the group automatically jousts to the next position
- Fighters and non-fighters have separate positions
- Uses a 2-position rotation

**Rockhopper Egg Handling (Marked Player):**

- If the player is marked, the module handles rockhopper eggs automatically
- Picks up the egg, carries it to the brazier location, and drops it in
- Uses first-person view and mouse clicking automation to interact with the brazier

### Player Notes

- The group jousts automatically when the pounce is detected.
- Fighters and non-fighters are positioned separately using a 2-spot rotation.
- If you are the marked player, egg handling is fully automated -- the module picks up eggs, moves to the brazier, and drops them in.
- The egg drop uses first-person view automation, so do not interfere with camera controls during this phase.
