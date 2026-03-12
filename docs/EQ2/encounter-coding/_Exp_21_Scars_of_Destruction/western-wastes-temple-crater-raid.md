# Western Wastes: Temple Crater [Raid]

**Expansion:** Scars of Destruction (Exp 21)

This raid zone contains 4 boss encounters.

## Available Setups

| Boss | Description |
|------|-------------|
| [Digger Grendok](#digger-grendok) | Fully automated |
| [Marrowseeker Hazzir](#marrowseeker-hazzir) | HUD timers for tracking |
| [Lacetor the Fiendish](#lacetor-the-fiendish) | TTS alerts and distance-based curing |
| [Grand Shaman Shaekk](#grand-shaman-shaekk) | Fully automated |

---

## Digger Grendok

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with Monitored Locale curse jousting (similar to Guard Imobiun), a Monitored Attention self-targeting mechanic, and dispell management.

### What the Module Does

**Monitored Locale:**

- Detects the Monitored Locale curse on the player
- Jousts the player away from the named to a safe position (similar to Imobiun's Doomed Familiarity)

**Monitored Attention:**

- Detects Monitored Attention on the player
- Automatically self-targets when this detriment is active

**Dispell Setup:**

- Enables dispells for the fight

**Fighter Dethreat:**

- Manages fighter dethreat during curse phases to prevent aggro issues

### Player Notes

- The Monitored Locale joust works the same way as Imobiun's Doomed Familiarity
- Monitored Attention requires self-targeting -- handled automatically

---

## Marrowseeker Hazzir

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with Selfish Ambition curse tracking and multiple HUD timers for the Thirsts mechanic.

### What the Module Does

**Selfish Ambition:**

- Tracks the Selfish Ambition curse on players via HUD events

**Thirsts HUD Timers:**

- Displays three on-screen HUD timers:
    - Eating add timer (9 seconds)
    - Next Thirsts timer (60 seconds)
    - Next Curses timer (60 seconds)
- These timers help track the fight's rhythm

**Add Targeting:**

- Auto-targets marrow thirster adds

### Player Notes

- Watch the HUD timers for upcoming mechanics
- The timers help you anticipate Thirsts and Curse phases

---

## Lacetor the Fiendish

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with Left in the Cold requiring 18-meter distance for cure, Balanced Synergy management for fighters, and TTS alerts.

### What the Module Does

**Left in the Cold:**

- Detects Left in the Cold detriment on the player
- Uses TTS (Text-to-Speech) alert to announce who has the detriment
- Requires 18-meter distance from the named for the cure curse to work
- The module ensures the player is at the correct distance before curing

**Balanced Synergy:**

- Enables Balanced Synergy in the cast stack for fighters
- Synergetic Storm requires Balanced Synergy to be active in order to be cleared

### Player Notes

- The TTS alert for Left in the Cold helps coordinate the group
- 18 meters is the required distance for the cure -- make sure you're far enough away
- Fighters need Balanced Synergy active for the Synergetic Storm mechanic

---

## Grand Shaman Shaekk

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A positional fight with 3-spot jousting based on lightning pillar AoE circles. Similar jousting pattern to the Revenant of Shaekk in Temple of Veeshan: Echoing Silence but with different positions.

### What the Module Does

**3-Spot Lightning Pillar Jousting:**

- Monitors for lightning pillar AoE circles at 3 positions around the arena
- When a pillar appears at or near the current position, the group rotates to the next safe position
- The rotation cycles through all 3 positions continuously
- Uses the same rotation pattern as the Temple of Veeshan version of Shaekk

### Player Notes

- Follow the automated position rotation when lightning pillars appear
- The fight uses the same jousting concept as the Revenant of Shaekk encounter but at different locations
