# Zon Zobboz: The Graftwerk [Untold Heroic]

**Expansion:** Rage of Cthurath (Exp 22)

This zone has 5 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Setup Name | Description |
|------|-----------|-------------|
| [Bludge the Bludgeoner](#bludge-the-bludgeoner) | Bludge the Bludgeoner | Position and targeting and dispells |
| [The Abominable Dreadarou](#the-abominable-dreadarou) | The Abominable Dreadarou | Auto target |
| [Lu'Gul of Zob](#lugul-of-zob) | Lu'Gul of Zob | Auto-interrupt |
| [The Orozorgon](#the-orozorgon) | Orozorgon | Auto-jousting |
| [Senzu](#senzu) | Senzu | Turns on HOs and auto-jousting of Gaze |

---

## Bludge the Bludgeoner

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter where the boss gains offensive and defensive buffs that must be dispelled by mages before both can stack (which makes them permanent).

### Requirements

- **Mage** (dispels boss buffs)
- **Fighter** (auto-targets adds)

### What the Module Does

**Auto Dispelling:**

- Mages automatically check if the boss has "Mincemeat" (offensive buff) or "Meatshield" (defensive buff)
- Dispels whichever is present before both can stack simultaneously
- If both are present at the same time, neither can be dispelled

**Auto-Target:**

- Fighters auto-target adds with health-based thresholds:
    - "a dumped prototype" (at 95% health)
    - "an unsightly voidcyst" (at 75% and 35% health)
    - The boss as fallback

### Player Notes

- Mages automatically handle dispelling boss buffs.
- Adds are prioritized via auto-target with health-based thresholds.

---

## The Abominable Dreadarou

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter with a dangerous curse interaction -- Hoof and Mouth Disease causes offensive abilities to apply Bulbous Blisters, which kills at 10 stacks. The module uses smart conditional cure logic.

### Requirements

- **Fighter** (auto-target)
- **Priest** (curse curing, carefully managed)

### What the Module Does

**Smart Cure Logic:**

- When the player gets **Hoof and Mouth Disease**, the module stops all offensive actions
- Cure curse is only requested when Hoof and Mouth is present but **Bulbous Blisters is NOT** present (safe to cure)
- Curing while Bulbous Blisters is active kills the player
- **Bloodgraft** curse is also auto-cure-cursed when detected
- Priest curse cures are disabled to prevent premature/unsafe curing

**Auto-Target:**

- Fighters auto-target the boss

### Player Notes

- The module automatically stops offensive abilities when Hoof and Mouth Disease is detected.
- Cure timing is managed precisely to prevent deaths from Bulbous Blisters interaction.
- On kill, priest curse curing and offensive actions are restored.

---

## Lu'Gul of Zob

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter where the boss has a cast that must be interrupted.

### Requirements

- All group members (for interrupt)

### What the Module Does

**Auto-Interrupt:**

- NPC Cast Monitoring is enabled
- When the boss begins casting a specific ability, the module automatically casts an interrupt for all group members

**Auto-Target:**

- Fighters auto-target the boss

### Player Notes

- Automatic interrupting of the boss's ability -- no manual intervention needed.

---

## The Orozorgon

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter with two jousting mechanics -- Constricting Coils requires everyone except the affected player to move away, and Flesh-Eating Fumes requires repositioning at high stacks.

### Requirements

- **Fighter** (auto-targets adds)

### What the Module Does

**Constricting Coils Joust:**

- When a player gets Constricting Coils, all OTHER players in the group joust away:
    - Fighters move to a farther joust spot
    - Non-fighters move to a closer joust spot
- The affected player stays in place
- When the detriment clears, everyone returns to normal positions

**Flesh-Eating Fumes:**

- A stacking poison that requires repositioning
- When stacks exceed 10, the module moves the affected player to a clearing spot
- When the detriment drops, positioning is restored

**Auto-Target:**

- Fighters auto-target "flesh-eating worm" adds and the boss

### Player Notes

- All jousting and fumes repositioning is fully automated.

---

## Senzu

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A complex encounter with HO management, ring tracking, and a Grafting Gaze curse that requires precise joust positioning. The module assigns a bard/scout as the ring handler.

### Requirements

- **Bard or Scout** (ring handler, HO starting)
- **Fighter** (positioning)

### What the Module Does

**HO (Heroic Opportunity) System:**

- Enables HO starting, HO wheel, allow unknown target, and change target options for all
- A bard (or first scout if no bard) is flagged as the ring handler

**Ring Positioning:**

- The flagged bard/scout moves to the location of the ring actor when it spawns
- During Gaze casts, all players are moved to the raid spot; when the cast ends, they return

**Grafting Gaze Joust:**

- An uncurable curse placed on the two farthest players
- On expiration, kills the player if in front of the boss or within 30 meters of another cursed player
- The module assigns each cursed player to a separate joust spot
- IRC announcements indicate which spot each player is heading to

**Auto-Target:**

- The flagged bard/scout targets only the boss
- All others target "eyes without a face" adds and "vein of Senzu" at various health thresholds, with the boss as fallback

**Poison Pressure (on Boss):**

- Stacks that kill everyone at 10 increments
- Reduced by completing HOs initiated by scouts

### Player Notes

- IRC announcements indicate joust spot assignments for Grafting Gaze.
- HO settings are restored when the boss dies.
