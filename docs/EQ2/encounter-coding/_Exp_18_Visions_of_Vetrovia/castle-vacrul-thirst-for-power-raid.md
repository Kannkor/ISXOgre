# Castle Vacrul: Thirst for Power [Raid]

**Expansion:** Visions of Vetrovia (Exp 18)

This zone has 3 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Lady of the Lute](#lady-of-the-lute) | Self-target during Melodic Distraction |
| [Lysander Mistmoore](#lysander-mistmoore) | Self-target on Libant Decree, bat form tracking, magical attack jousting |
| [Vorigan Mistmoore](#vorigan-mistmoore) | Bloody Buffet jousting, vampiric boil popping, sewage pool mechanic |

---

## Lady of the Lute

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a damage-reflection detriment that requires self-targeting.

### What the Module Does

**Melodic Distraction:**

- When the detriment is detected, auto-target is disabled and the character targets itself
- Loops until the detriment expires, then restores the previous target and re-enables auto-target

### Player Notes

- Self-targeting is automatic during Melodic Distraction
- Do not manually re-target the boss while the detriment is active

---

## Lysander Mistmoore

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A multi-phase fight with self-targeting, bat form transitions, and proximity-based jousting.

### What the Module Does

**Libant Decree:**

- Same self-targeting pattern as Lady of the Lute -- forces self-target until the detriment expires

**Bat Form Transition:**

- When Lysander changes back into a vampire, the module finds his actor (or the vampire bat form) and repositions the group relative to him

**Magical Attack Joust:**

- When Lysander focuses magical attacks closer to him, non-fighters joust to a high point away from the boss
- Configurable delay timing for the joust and return

### Player Notes

- Self-targeting during Libant Decree is automatic
- Non-fighters are jousted away during the magical attack phase

---

## Vorigan Mistmoore

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A complex fight with NPC cast monitoring, vampiric boil popping, and sewage pool mechanics. All cures are disabled to prevent accidentally curing a detriment that heals the boss.

### What the Module Does

**Bloody Buffet Joust:**

- Detected via NPC cast monitoring
- The group jousts to a preset spot with configurable timing

**Vampiric Boil Popping:**

- A flagged character moves to the sewage location, jumps to acquire the Sanguinated Sewage curse
- Then iterates through all vampiric boil actors, moving to each one and performing key presses to pop them
- Requests a cure curse afterward

**Uncurable Detriment Pool:**

- When the uncurable detriment is detected, the character moves to one of two sewage pool locations and jumps repeatedly until the detriment clears

### Player Notes

- All cures are disabled during this fight to prevent accidentally healing the boss
- The boil popping sequence is handled by a flagged character
- Sewage pool location is configurable
