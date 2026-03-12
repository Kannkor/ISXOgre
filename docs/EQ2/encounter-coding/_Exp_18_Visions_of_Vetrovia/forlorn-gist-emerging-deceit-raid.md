# Forlorn Gist: Emerging Deceit [Raid]

**Expansion:** Visions of Vetrovia (Exp 18)

This zone has 5 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Envoy to Bloodrite](#envoy-to-bloodrite) | Archetype-based confusion jousting |
| [G'Dalt Spirit-stitcher](#gdalt-spirit-stitcher) | Stitching Lips cure via well clicking |
| [The Hand of Lithania](#the-hand-of-lithania) | Front/behind jousting, Hand of Judgement self-target, fighter defensives |
| [The Reanimated Horror](#the-reanimated-horror) | Front/behind jousting, imprisonment key system with Rogue/Predator flag rotation |
| [Lithania Dyrmelia](#lithania-dyrmelia) | Proximity Hex rescue via cross-session verb |

---

## Envoy to Bloodrite

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where the boss targets a specific archetype, and characters of that archetype must joust away when confused.

### What the Module Does

**Archetype-Based Confusion Joust:**

- When the boss motions toward a specific archetype (mages, scouts, priests, or fighters), the module tracks which archetype is targeted
- When the Confusion detriment is detected on a character of the targeted archetype, they joust 28m away from the boss
- When the detriment clears, positions reset and everyone repositions around the boss

### Player Notes

- Only the targeted archetype jousts -- other archetypes stay in place
- Jousting is based on the boss's announcement of which archetype is being targeted

---

## G'Dalt Spirit-stitcher

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a detriment that must be cured by clicking a well object.

### What the Module Does

**Stitching Lips Cure:**

- When the Stitching Lips detriment is detected, the character saves its current location
- Moves to the well location, finds the well actor by visual identifiers, and double-clicks it
- Waits for the cast to complete, then returns to the previous position

### Player Notes

- The well clicking is fully automated -- the module handles movement, clicking, and return

---

## The Hand of Lithania

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with front/behind jousting, a self-targeting detriment, and fighter defensive ability usage.

### What the Module Does

**Front/Behind Jousting:**

- Massive face slap (frontal) triggers standard positioning (tanks in front, everyone else behind)
- Slap to the wrist (behind) repositions everyone 180 degrees behind the boss with a timed reset

**Hand of Judgement:**

- When the detriment is detected, the character targets itself until it clears

**Fighter Defensives:**

- On both frontal and tail attacks, fighters automatically cast their best available defensive ability

### Player Notes

- Front/behind positioning alternates based on attack type
- Fighters pop defensives automatically during attacks

---

## The Reanimated Horror

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with front/behind jousting and an imprisonment mechanic requiring Rogues or Predators to free captured players with keys.

### What the Module Does

**Front/Behind Jousting:**

- Same pattern as The Hand of Lithania -- frontal and tail attacks trigger opposite positioning

**Imprisonment and Key System:**

- When a raid member is imprisoned, a flagged character with a key moves to the cage and clicks the interactable to free them
- If the flagged character lacks a key, the flag passes to the next eligible Rogue or Predator
- Rogues use "Rob" and Predators use "Bounty" on the jailer to obtain keys

### Player Notes

- Keys are obtained automatically by Rogues and Predators
- The flag rotates through eligible classes as keys are used

---

## Lithania Dyrmelia

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a proximity hex that requires a specific player to rescue the afflicted character.

### What the Module Does

**Proximity Hex Rescue:**

- When a player gets the Proximity Hex, the module reads the effect text to extract the name of the character who must cure it
- A cross-session event is fired to that specific character, who uses "Rescue from the Hex!" on the afflicted player

### Player Notes

- The hex rescue is coordinated automatically across sessions
- The correct rescuer is identified from the detriment's effect text
