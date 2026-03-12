# Fordel Midst: Bizarre Bazaar [Heroic]

**Expansion:** Blood of Luclin (Exp 16)

This heroic zone contains 3 boss encounters with OgreBot automation modules. The Cat's Eye Agate and Paludal Catnip clicking mechanics are zone-level and shared across multiple encounters.

## Available Setups

| Boss | Description |
|------|-------------|
| [Trade Baroness Elsindir](#trade-baroness-elsindir) | Auto-clicking Cat's Eye Agate |
| [Bazaar Baron Brixwald](#bazaar-baron-brixwald) | Auto-clicking Cat's Eye Agate and Paludal Catnip, auto stand-up |
| [Mannee/Mandee Quin](#mannee-mandee-quin) | Smart cure curse targeting based on emotes |

---

## Trade Baroness Elsindir

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a clickable item mechanic. The Cat's Eye Agate must be clicked when it glows during the encounter.

### What the Module Does

**Cat's Eye Agate:**

- Automatically detects when the Cat's Eye Agate begins glowing
- Clicks the agate when triggered

### Player Notes

- The agate clicking is handled automatically. Focus on DPS.

---

## Bazaar Baron Brixwald

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with multiple clickable item mechanics and a knockdown recovery mechanic. Both the Cat's Eye Agate and Paludal Catnip must be clicked when triggered, and players must stand back up if knocked down.

### What the Module Does

**Cat's Eye Agate:**

- Automatically detects when the Cat's Eye Agate begins glowing
- Clicks the agate when triggered

**Paludal Catnip:**

- Automatically detects when the Paludal Catnip is triggered
- Clicks the catnip when needed

**Auto Stand-Up:**

- If the player is knocked down during the fight, the module automatically stands back up

### Player Notes

- All clickable mechanics and the knockdown recovery are handled automatically.
- The Cat's Eye Agate and Paludal Catnip mechanics are shared zone-level mechanics that also apply to the Elsindir fight.

---

## Mannee/Mandee Quin

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A curse management encounter where curses must be cured on a specific player based on emotes. The boss announces which player needs to be cured, and only that player should receive the cure.

### What the Module Does

**Smart Cure Targeting:**

- Monitors emotes for the message indicating the boss "likes what [player] is wearing"
- Identifies the specific player mentioned in the emote
- Instructs priests to cure curse on that specific player only
- Prevents priests from curing curse on anyone else

### Player Notes

- Do NOT manually cure curses during this fight. Only the player mentioned in the emote should be cured.
- The module reads the emote text to determine exactly who needs the cure.
