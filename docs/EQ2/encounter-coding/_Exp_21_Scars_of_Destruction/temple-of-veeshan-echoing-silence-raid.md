# Temple of Veeshan: Echoing Silence [Raid]

**Expansion:** Scars of Destruction (Exp 21)

> **:warning: Work In Progress**
>
> This zone's automation is still under development. Some mechanics may not be fully automated yet.

This raid zone contains 1 boss encounter.

## Available Setups

| Boss | Description |
|------|-------------|
| [Revenant of Shaekk](#revenant-of-shaekk) | Timed cure curse, jousting, and position management (WIP) |

---

## Revenant of Shaekk

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A complex encounter with timed cure curses, 3-spot AoE circle jousting, timed joust-away mechanics, HUD timers, and fighter-specific positioning.

### What the Module Does

**Entrancing Ether (Timed Cure Curse):**

- Detects the Entrancing Ether curse on the player
- Waits a configurable amount of time (default 12 seconds) before allowing the cure
- Scouts have an optional fast-cure setting to cure earlier
- Timed curing is critical to prevent premature removal

**Necrotic Touch:**

- Detects Necrotic Touch on the player
- Automatically requests a cure immediately (no delay)

**3-Spot AoE Jousting:**

- Monitors for blue fire AoE circles at 3 positions
- When a circle appears at the current position, the group rotates to the next safe position
- The rotation cycles through all 3 positions continuously

**Lifeleecher (Timed Joust):**

- 48-second timed joust-away mechanic
- The group jousts away from the named at the timed interval
- Returns to position after the danger passes

**HUD Timers:**

- Spellfrenzy timer: 55-second countdown
- Bloodfrenzy timer: 55-second countdown
- Both displayed as on-screen HUD timers for awareness

**Fighter Management:**

- Enables Bulwark of Order for fighters
- Fighter-specific positioning with dedicated spots
- Threat management options for the 2nd fighter
- Stops offensive actions if the fighter gets too far from the named (>13 meters)

**Druid Natural Cleanse:**

- Druids automatically use Natural Cleanse for specific mechanics

### Player Notes

- The timed cure for Entrancing Ether is critical -- curing too early causes problems
- Follow the automated position rotation during AoE phases
- Watch the HUD timers for Spellfrenzy and Bloodfrenzy
- Fighters should pay attention to their positioning
