# The Fabled Kurn's Tower: Breaching the Void [Heroic]

**Expansion:** Visions of Vetrovia (Exp 18)

This zone has 5 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Jennre Warsinger](#jennre-warsinger) | Cannibalistic tune jousting, Song of War aura-based add targeting |
| [The Ancient Void-Touched Wumpus](#the-ancient-void-touched-wumpus) | Dual-layer text-triggered jousting |
| [Telvorsinn / Thovalakk](#telvorsinn--thovalakk) | Room-based auto-targeting, ability cancellation |
| [Zevorg the Warmonger / Nexion the Warmind](#zevorg-the-warmonger--nexion-the-warmind) | Room-based auto-targeting, ability cancellation, all cures disabled |
| [Yynzik the Scornridden](#yynzik-the-scornridden) | Class-based Riddance dispelling via illusion orb mechanic |

---

## Jennre Warsinger

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a joust mechanic and an aura-based add targeting system.

### What the Module Does

**Cannibalistic Tune Joust:**

- When the boss plays a cannibalistic tune, the entire group jousts away via cross-session commands

**Song of War Add Phase:**

- When the boss leads a Song of War, the group moves to an add spot
- The fighter reads the boss's aura value and queries all spectral minstrel adds matching that exact aura
- Only matching adds are added to auto-target, preventing the wrong adds from being killed
- Encounter nukes and PBAEs are disabled during the add phase to prevent friendly fire

### Player Notes

- Only adds matching the boss's aura should be killed -- the module handles targeting automatically
- Encounter nukes and PBAEs are re-enabled when the Song ends

---

## The Ancient Void-Touched Wumpus

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a text-triggered dual-layer joust.

### What the Module Does

**Boot Joust:**

- When the boss boots everyone, executes a dual-layer joust using both standard and secondary joust spots
- The relative camp spot clears automatically after 14 seconds

### Player Notes

- The joust uses two layers of positioning for safety
- Positions reset automatically after 14 seconds

---

## Telvorsinn / Thovalakk

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A twin-named fight where auto-targeting changes based on which room the group enters.

### What the Module Does

**Room-Based Auto-Targeting:**

- Entering Sunne Chamber targets Thovalakk as the kill target (Telvorsinn as backup)
- Entering Nerteros Chamber targets Telvorsinn as the kill target (Thovalakk as backup)
- Scan radius limited to 25m with 5m height

**Ability Cancellation:**

- Disables and cancels 4 maintained abilities: Sanguine Embrace, Union of Stone, Etherlord, Elemental Avatar

### Player Notes

- Auto-target switches automatically when entering different rooms
- Certain maintained abilities are disabled for the duration of the fight

---

## Zevorg the Warmonger / Nexion the Warmind

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A twin-named fight similar to Telvorsinn/Thovalakk with room-based targeting.

### What the Module Does

**Room-Based Auto-Targeting:**

- Entering Aurora Chamber targets Zevorg as the kill target
- Entering Vesper Chamber targets Nexion as the kill target

**Ability Cancellation:**

- Same 4 abilities disabled as the Telvorsinn fight

**All Cures Disabled:**

- Both regular cures and curse cures are fully turned off for this fight

### Player Notes

- Do not cure manually -- all cures are disabled by design
- Auto-target switches based on room entry

---

## Yynzik the Scornridden

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a class-based dispelling system where each archetype must dispel a matching Riddance detriment using an illusion orb.

### What the Module Does

**Class-Based Riddance Dispelling:**

- Four Riddance detriments on the boss, each requiring a specific archetype:
    - Physical = Fighter, Arcane = Priest, Noxious = Scout, Elemental = Mage
- The flagged character of each archetype handles its matching detriment

**Illusion Orb Mechanic:**

- To dispel, the character needs the Greater Chaos of Theer illusion
- If not in illusion, the module finds an orb by visual identifiers, moves near it, jumps to activate it, and waits for the illusion to apply
- Once in illusion, dispatches the dispel on the boss

### Player Notes

- Each archetype is responsible for its matching Riddance type
- The orb activation and dispelling sequence is automated
- Movement to orbs is disabled by default for fighters (configurable)
