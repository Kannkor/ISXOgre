# Sodden Archipelago: Operation Cooperation [Raid]

**Expansion:** Scars of Destruction (Exp 21)

This raid zone contains 1 boss encounter.

## Available Setups

| Boss | Description |
|------|-------------|
| [Biethimut, Deepwater Titan](#biethimut-deepwater-titan) | Moves group if someone has Drag Beneath |

---

## Biethimut, Deepwater Titan

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A complex encounter with a Drag Beneath curse requiring interaction with frenzied Skulkers, corpse clicking for buffs, totem interaction at timed intervals, and alcohol maintenance.

### What the Module Does

**Drag Beneath:**

- Detects the Drag Beneath curse on any group member
- When detected, moves the group to find and approach a frenzied Skulker
- Complex movement coordination across the group using event-based communication
- Jousts the group away from danger and then back after the mechanic resolves

**Corpse Flower's Protection:**

- Detects when Corpse Flower's Protection is needed
- Finds and clicks a decomposing corpse to acquire the protection buff

**Totem Clicking:**

- At timed Confrontation intervals, the module clicks the totem
- Handles the timing automatically throughout the fight

**Alcohol Maintenance:**

- Automatically maintains the Pickleback alcohol buff
- Configurable timing and quantity for alcohol consumption

**Positioning:**

- Multiple position spots configured for tank, priest, and raid groups
- Joust-away-and-back mechanic for specific phases

### Player Notes

- This fight has many moving parts -- the module handles most of them automatically
- Make sure you have Pickleback alcohol in your inventory
- The frenzied Skulker mechanic involves group-wide movement coordination
