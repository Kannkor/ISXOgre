# Savage Weald: Shadow's Hold [Raid]

**Expansion:** Reign of Shadows (Exp 17)

This zone has 2 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Greta Gnitrat](#greta-gnitrat) | Auto cure curse for Grimling Cooties with timed curing |
| [Shadowcaster Grimlock](#shadowcaster-grimlock) | Self-target and pet attack disable during protection phase |

---

## Greta Gnitrat

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a timed curse that must be cured near the end of its duration.

### What the Module Does

**Grimling Cooties:**

- Monitors the Grimling Cooties detriment on the player
- When the detriment duration drops below 10 seconds remaining, the module broadcasts a cure curse request across all sessions and IRC
- Only announces once per detriment application to prevent spam, and resets when the detriment clears

### Player Notes

- Cure timing is automated -- the module waits until the curse is nearly expired before requesting a cure
- IRC announcements are posted for cure requests

---

## Shadowcaster Grimlock

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a damage reflection phase that requires players to stop attacking.

### What the Module Does

**Shadow Protection:**

- When Grimlock uses shadow energy to protect himself, the module:
    - Makes the character target itself to stop DPS on the boss
    - Turns off pet attacks to prevent reflected damage

### Player Notes

- During the protection phase, all damage is reflected -- the module handles self-targeting automatically
- Do not manually re-target the boss during the protection phase
