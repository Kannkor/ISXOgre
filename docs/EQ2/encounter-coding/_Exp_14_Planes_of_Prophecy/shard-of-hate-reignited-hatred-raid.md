# Shard of Hate: Reignited Hatred [Raid]

**Expansion:** Planes of Prophecy (Exp 14)

This zone has 9 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Bleeder of Ire](#bleeder-of-ire) | Front/behind poison jousting, auto-dispelling |
| [The Phantom Wraith](#the-phantom-wraith) | Automated Thought Bleed/Spike alternating jousting |
| [High Priest M'kari](#high-priest-mkari) | Green/Purple portal detriment jousting |
| [Hand of Maestro](#hand-of-maestro) | Continuous movement (anti-snap), JumpSnap curse response |
| [Kpul D'Vngur](#kpul-dvngur) | Emote-based curse curing (scream/meditate/notice), tag-based cure ordering |
| [The Culler of Bones](#the-culler-of-bones) | Disorientate and Noxious Jolt jousting |
| [Innoruuk](#innoruuk) | Abhorrence detriment auto-joust |
| [Avatar of Abhorrence](#avatar-of-abhorrence) | Seething Abhorrence auto cure-curse relay |
| [Avatar of Bone](#avatar-of-bone) | Discarded bones spawn timer HUD |

---

## Bleeder of Ire

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with directional poison jousting and dispellable buffs.

### What the Module Does

**Front/Behind Poison Jousting:**

- When poison sprays behind, non-fighters move to the front
- When poison sprays in front, non-fighters move behind
- Positions reset after 12 seconds

**Auto-Dispelling:**

- Mages and druids automatically dispel the boss's buff

### Player Notes

- Camp spot everyone and they will auto-move -- no setup required

---

## The Phantom Wraith

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight alternating between two positions based on Thought Bleed and Thought Spike mechanics.

### What the Module Does

**Alternating Jousting:**

- On Thought Bleed, schedules movement to the Spike position after 5 seconds
- On Thought Spike, schedules movement back to the Bleed position after 5 seconds
- HUD shows 15-second countdown timers for each mechanic

### Player Notes

- Camp spot everyone and do a set up for -- everyone will auto-move

---

## High Priest M'kari

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with color-coded portal detriment jousting.

### What the Module Does

**Portal Detriment Jousting:**

- Characters with the Green detriment automatically move to the green portal
- Characters with the Purple detriment automatically move to the purple portal
- Returns to the raid spot when the detriment clears

### Player Notes

- Camp spot everyone and do a set up for -- everyone will auto-move

---

## Hand of Maestro

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight requiring continuous movement to avoid a snap mechanic.

### What the Module Does

**Continuous Movement (Anti-Snap):**

- Cycles through 4 camp spot positions every 10 seconds in a square pattern to keep everyone moving

**JumpSnap Response:**

- When the boss stares at you, stops movement and waits for the curse to apply and clear before resuming

### Player Notes

- The continuous movement prevents the snap mechanic from landing

---

## Kpul D'Vngur

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with three different curse types, each requiring a specific emote to cure.

### What the Module Does

**Emote-Based Curse Curing:**

- Dulled Alertness is cured by /scream
- Vocal Disruption is cured by /meditate
- Divert Focus is cured by /notice
- Cursed players broadcast their curse type, and the designated curer performs the matching emote

**Tag-Based Cure Ordering:**

- Tag target numbers determine cure priority -- #1 cures first, others wait their turn

### Player Notes

- The cure assignment is coordinated via cross-session commands

---

## The Culler of Bones

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with two jousting triggers.

### What the Module Does

**Jousting:**

- On Disorientate, non-healers in group 1 move to the joust spot
- On Noxious Jolt, moves to a third position after a short delay

### Player Notes

- Camp spot is set on setup

---

## Innoruuk

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where the Abhorrence detriment requires jousting away.

### What the Module Does

**Abhorrence Auto-Joust:**

- Characters with the Abhorrence detriment automatically move 15 meters away via a relative camp spot offset
- Returns to position when the detriment clears

### Player Notes

- Camp spot everyone -- people with Abhorrence will joust away automatically

---

## Avatar of Abhorrence

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a timed curse relay.

### What the Module Does

**Auto Cure-Curse Relay:**

- When Seething Abhorrence curse duration drops below 9 seconds, automatically broadcasts a cure relay

### Player Notes

- Curse relay is handled automatically

---

## Avatar of Bone

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with discarded bones spawns tracked via HUD.

### What the Module Does

**Spawn Timer HUD:**

- Displays a 60-second countdown when discarded bones actors spawn

### Player Notes

- The HUD timer helps coordinate bone management
