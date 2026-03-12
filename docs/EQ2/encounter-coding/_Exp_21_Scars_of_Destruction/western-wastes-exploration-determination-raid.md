# Western Wastes: Exploration Determination [Raid]

**Expansion:** Scars of Destruction (Exp 21)

This raid zone contains 4 boss encounters.

## Available Setups

| Boss | Description |
|------|-------------|
| [Guard Imobiun](#guard-imobiun) | Fully automated |
| [Court Sorcerer Viranor](#court-sorcerer-viranor) | Fully automated |
| [Enforcer Rimefield](#enforcer-rimefield) | Fully automated |
| [Frostking Jund'Erin](#frostking-junderin) | Crystal clicking coordination (button available) |

---

## Guard Imobiun

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a Doomed Familiarity curse that requires jousting away, fighter dethreat management, and priest cure positioning.

### What the Module Does

**Doomed Familiarity:**

- Detects the Doomed Familiarity curse on the player
- Jousts the player away from the named to a safe position
- Fighter dethreat is applied during the joust to manage aggro
- Event-based coordination ensures the whole group responds appropriately

**Priest Cure Spots:**

- Priests are positioned at specific cure spots for optimal cure range

**Direct Assist Targeting:**

- Auto-targeting is configured for direct assist on the named

### Player Notes

- The joust for Doomed Familiarity is handled automatically
- Priests will be positioned at specific spots for cure coverage

---

## Court Sorcerer Viranor

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with Brain Fog increment tracking, jousting from the tank's target position, and add management.

### What the Module Does

**Brain Fog:**

- Tracks Brain Fog increment counts on the player
- Jousts from the tank's target position at a set offset to avoid the fog

**Jousting:**

- Jousts from the named's position with a directional offset to maintain safe distance
- Fighter jousting is configurable

**Direct Assist Targeting:**

- Auto-targeting is configured for direct assist on the named

**Add Targeting:**

- Auto-targets Riftcaster Wyvern adds

### Player Notes

- The module tracks Brain Fog stacks and manages jousting automatically
- Fighters have configurable joust behavior

---

## Enforcer Rimefield

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with Pressured Release requiring a joust-then-cure at 25 meters distance, plus dispell management for adds.

### What the Module Does

**Pressured Release (Joust-Then-Cure):**

- Detects Pressured Release detriment on the player
- Jousts away to at least 25 meters from the named
- Requests a cure once at the safe distance

**Dispell Setup:**

- Enables dispells for handling summoned power cache adds

### Player Notes

- The 25-meter distance requirement for Pressured Release is stricter than most joust-then-cure mechanics
- Dispells handle the add protections automatically

---

## Frostking Jund'Erin

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight centered around Crystallizing Compression curses that require clicking specific crystals. This encounter shares the same module as Kael Drakkel: Abdicated Throne [Raid].

### What the Module Does

**Crystallizing Compression:**

- Detects the Crystallizing Compression curse on the player
- Coordinates crystal assignment across the raid using a sorted index system
- Each player is assigned a crystal based on their position in the collection
- Moves the player to the assigned crystal and clicks it
- Random crystal fallback if the indexed assignment fails

**Crystal Button:**

- Use `Obj_OgreMCP:PasteButton[OgreConsoleCommand,Jund,-ExecuteEvent_AP,auto,Jund_AtCrystal]` to signal you are at your crystal

**Protection Phase:**

- When the boss "prepares to protect himself," all offensive actions stop for a configurable duration (default 15 seconds)
- DPS resumes automatically after the phase

**Fighter Management:**

- Fighter dethreat during Crystallizing Compression to prevent aggro issues

### Player Notes

- Crystal assignment is coordinated automatically -- follow the module's positioning
- Stop DPS during the protection phase (automated)
- The crystal button can be used for manual crystal coordination
- This is the same fight module as the Kael Drakkel version
