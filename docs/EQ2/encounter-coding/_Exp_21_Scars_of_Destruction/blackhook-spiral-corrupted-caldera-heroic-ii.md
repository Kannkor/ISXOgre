# Blackhook Spiral: Corrupted Caldera [Heroic II]

**Expansion:** Scars of Destruction (Exp 21)

This Heroic II zone contains 5 boss encounters with varying levels of automation.

## Available Setups

| Boss | Description |
|------|-------------|
| [Atreyes](#atreyes) | Mages turn on Absorb Magic for the fight |
| [Gahilga the Ingrate](#gahilga-the-ingrate) | Keeps the named at range if tank has camp spot set |
| [Blackgut the Promised](#blackgut-the-promised) | Semi-automated; players may die from across-the-wall mechanic |
| [Blackgut the Rewarded](#blackgut-the-rewarded) | Automated. Does NOT handle the dispell yet |
| [Lord Tarinax](#lord-tarinax) | Fully automated |

---

## Atreyes

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where dispells and Absorb Magic are key to handling the boss mechanics. The module enables Absorb Magic and sets up auto-targeting for adds.

### What the Module Does

- Enables Absorb Magic in the cast stack for all characters
- Enables dispells
- Enables dynamic ignore for PBAEs (non-fighters)
- Sets up auto-targeting with multiple priority tiers for both named NPCs and regular NPCs

### Player Notes

- Auto-targeting is cleared and Absorb Magic is disabled after the fight

---

## Gahilga the Ingrate

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where the group needs to be kept away from the named while the tank manages positioning. The module handles tank positioning to keep the named at range.

### What the Module Does

**Tank Positioning:**

- The tank is placed at a forward position to engage the named
- If the named moves away from the tank (distance > 5) and the tank does not have aggro, the tank retreats to the raid position
- When the tank regains aggro, the module moves the tank back to the pull position

**Non-Tank Positioning:**

- Non-fighters are positioned at the raid spot, away from the named

### Player Notes

- Auto-targeting is set to focus on the named NPC

---

## Blackgut the Promised

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a gate mechanic where players get ported to the other side. The module handles joust-away from dangerous locations.

### What the Module Does

**Gate Mechanic:**

- When the message "Get back over the gate, stat!" is detected, the module handles recovery positioning

**Jousting:**

- Jousts away from dangerous AoE locations that spawn during the fight

### Player Notes

- Players will occasionally die from the across-the-wall mechanic. Rez them and continue.
- Two joust spots are configured for the fight

---

## Blackgut the Rewarded

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where archetype-specific summoned adds spawn that need to be clicked. The module handles moving to and clicking these adds.

### What the Module Does

**Summoned Add Handling:**

- Detects archetype-specific summoned adds (fighters get destroyers, mages get headbangers, scouts get splinters, priests get corruptors)
- Automatically moves the group to the add's location
- Clicks the add to dismiss it

**Healer Exception:**

- The first healer in the group stays in place to continue curing curses instead of chasing adds

### Player Notes

- The dispell mechanic is NOT yet handled by this module
- The module does NOT currently handle the assembly notification mechanic

---

## Lord Tarinax

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with void stacks on the named that trigger an add-clearing phase, plus a chain mechanic requiring clicking the named. Fully automated.

### What the Module Does

**Void Stacks Monitoring:**

- Monitors the named for Void Connection stacks
- When stacks reach 6-10, initiates an add-clearing patrol through multiple locations in the room
- At each location, waits until all nearby adds (soulchained Geomagus) are killed before moving to the next spot
- Returns the group to the raid spot after clearing all locations

**Chain Mechanic:**

- When the named gets shackled (ice shackles), automatically double-clicks the named to free it

**Auto-Targeting:**

- Non-fighters auto-target the soulchained Geomagus adds
- All characters target the named NPC

### Player Notes

- The add patrol visits 5 locations around the room
- The module waits at each location until adds within 15 meters are cleared before moving on
