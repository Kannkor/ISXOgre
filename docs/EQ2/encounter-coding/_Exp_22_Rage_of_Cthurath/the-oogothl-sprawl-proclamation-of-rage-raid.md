# The Oogothl Sprawl: Proclamation of Rage [Raid]

**Expansion:** Rage of Cthurath (Exp 22)

## Available Setups

| Boss | Setup Name | Description |
|------|-----------|-------------|
| [Darathar, Void Bound Ancient](#darathar-void-bound-ancient) | Darathar, Void Bound Ancient | Overwhelming Destruction cure management, Draconic Misdirection spread |

---

## Darathar, Void Bound Ancient

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight featuring two overlapping curse mechanics. "Overwhelming Destruction" propagates to a new target each time it is cured, requiring precise timing. "Draconic Misdirection" deals increasing damage per nearby player and can only be cured when the affected player is isolated — requiring everyone else to move away. Healers' auto-cure is disabled so these curses can be cured at the right moment.

### Requirements

- **Enchanters** should have PowerDrain-tagged abilities and Cannibalize Thoughts available.
- Multiple fighters are recommended; tank swapping is prepared during setup.

### What the Module Does

**Setup Configuration:**

- Curse-cure from the cast stack is disabled for all characters so healers do not auto-cure at the wrong time.
- Tank swapping is prepared for fighters.
- Enchanters: Auto-target enabled with a 35m scan radius and 15m height, targets the named, enables PowerDrain and Cannibalize Thoughts, disables Absorb Magic.
- Warlocks: Force myth on Dark Siphoning is disabled.
- Force named combat arts/abilities is enabled for all characters.
- PowerRestore tag is enabled for all characters.
- All characters are set to joust out.

**Overwhelming Destruction Cure Management:**

- Detects when "Overwhelming Destruction" is applied to your character. This curse propagates to a new target each time it is cured or the bearer dies, so timing is critical.
- When the curse is active and the remaining duration drops below 10 seconds, the module automatically requests an auto-cure via IRC.
- Cure requests are throttled to once every 5 seconds to avoid spamming.

**Draconic Misdirection Spread:**

- Detects when "Draconic Misdirection" is applied to your character. This curse deals increasing slashing damage for each player within 10m and can only be cured when the afflicted player has no other players within 10m.
- If your character has the curse and is also rooted by "Forced Worship":
    - An IRC alert is broadcast ("ROOTED! Raid needs to move") so the rest of the raid knows to clear the area.
    - All non-afflicted, non-fighter characters move to the spread joust spot via RCS.
- If your character has the curse and is not rooted:
    - Your character moves to the spread joust spot via RCS.
    - Other non-fighter characters also move to the spread joust spot via RCS.
- When the curse is cleared, a broadcast event returns all characters to their normal positions.
- While the curse is active and the character is cursed, an auto-cure request is issued every 5 seconds via IRC.

**On Named Kill:**

- Curse-cure is re-enabled for all characters.
- All RCS positions are cleared.
- Tank swapping cleanup is performed.

### Player Notes

- Healers must not manually cure Overwhelming Destruction at the wrong time — the module handles cure timing automatically. Curse-cure is disabled in the cast stack for the entire fight.
- Draconic Misdirection spread is fully automated. If you have the curse and are mobile, you will joust out automatically. If you are rooted, the rest of the raid will move away from you.
- Fighters do not move away on Draconic Misdirection — only non-fighters spread.
- Keep power topped off; PowerRestore abilities are enabled to support this.
