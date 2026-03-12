# The Fabled Kurn's Tower [x2 Raid]

**Expansion:** Visions of Vetrovia (Exp 18)

This zone has 5 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Haggle Baron Klok](#haggle-baron-klok) | Color cube jousting, elemental/arcane cure management, NPC cast monitoring |
| [Sir Rouland](#sir-rouland) | Pact of Shadows coordinated cross-session curse curing |
| [Ilenee's Betrayal / Ilenee's Despair](#ilenees-betrayal--ilenees-despair) | Port warning (minimal) |
| [Ione the Lifebringer](#ione-the-lifebringer) | Host shell entry with special ability cycling |
| [Warlord Kurn Machta](#warlord-kurn-machta) | Dance with Death jousting, Iron Maiden key/intercept, pain threshold cures, bone spawning, torture stack tracking |

---

## Haggle Baron Klok

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with color-coded cube jousting and manual cure management.

### What the Module Does

**Color Cube Jousting:**

- Cobalt Sense of Impending Doom (blue): moves to the blue charm cube actor
- Crimson Sense of Impending Doom (red): moves to the red charm cube actor
- Returns when both detriments clear

**Elemental Cure:**

- Dead as a Doornail detriment MUST be cured
- First tries Forlorn Cure Elemental potion from inventory, then falls back to requesting elemental-only cure from the group

**Arcane Cure:**

- Draw Life detriment requests arcane-only cure from the group

### Player Notes

- Regular cures are disabled -- the module manages specific cure types manually
- NPC cast monitoring is enabled for fighters and bards for interrupting
- Shield Break (trauma) and Corruption (noxious) are deliberately NOT cured

---

## Sir Rouland

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a coordinated cross-session curse curing system requiring specific cure order.

### What the Module Does

**Pact of Shadows (Raid Mode):**

- Priests auto-request curse cure on themselves when the detriment is detected

**Pact of Shadows (Group Mode):**

- Chat text identifies exactly 2 people as key to curing the curse
- The module parses both names and sends events to those specific players
- The cure sequence is: mage cure first (via potion or auto-remove), then priest curse cure
- Enchanters optionally disable their cast stack for up to 20 seconds to avoid interfering

### Player Notes

- Cure order matters: mage cure before priest curse cure
- The module coordinates which specific players need to be cured
- Stifle belt adorn is auto-equipped on setup

---

## Ilenee's Betrayal / Ilenee's Despair

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A twin-named encounter with minimal automation.

### What the Module Does

**Port Warning:**

- Tracks the text message about the twins parting ways (placeholder for future automation)

### Player Notes

- Minimal automation for this encounter

---

## Ione the Lifebringer

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where a flagged character enters an empty host shell to gain special abilities.

### What the Module Does

**Host Shell Entry:**

- A flagged bard or priest checks multiple conditions (no Mental Exhaustion, no active host, empty shell exists, no mystical chains nearby)
- When all conditions are met, hails the shell to enter it

**Inside Host -- Special Abilities:**

- While inside the host (Host of the Dread Torturer detriment active), enables auto-target on Ione
- Cycles through 5 special host-only abilities, casting each that is ready

**Mental Exhaustion Cooldown:**

- Prevents re-entering the host while this cooldown debuff is active

### Player Notes

- The host entry is handled by a flagged bard or priest
- Special abilities inside the host are cycled automatically

---

## Warlord Kurn Machta

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

The most complex encounter in this zone with dual-mode operation (raid vs group), jousting, key mechanics, cure coordination, and bone spawning.

### What the Module Does

**Dance with Death:**

- Most characters joust to a far spot when detected (tank and healer1 stay)
- Priests also request curse cure on themselves

**Iron Maiden -- Group Mode:**

- The key holder announces themselves, the fighter casts Intercept on them
- The key holder uses the Iron Maiden key on the first fighter in range

**Iron Maiden -- Raid Mode:**

- Fighters intercept the other fighter in the raid

**Induce Agony / Pain Threshold Cures:**

- If Pain Threshold exists with low stacks, requests curse cures from priests
- If Induce Agony is present without Pain Threshold, priests fire group cures and non-priests try trauma potions

**Torture Technique Stack Broadcasting:**

- Fighter reads the boss's stack count and broadcasts it group-wide
- Group cures are disabled when stacks appear and re-enabled when they clear

**Grim Vision Bone Spawning:**

- When Grim Vision is detected, moves to discarded bones actors and jumps to wake them
- Sets up auto-target with bones at descending HP tiers
- Starts a 20-second kill timer when bones despawn

### Player Notes

- The module operates differently in raid vs group mode
- Multiple mechanics interact -- torture stacks affect cure availability
- Bone spawning and kill timing are fully automated
