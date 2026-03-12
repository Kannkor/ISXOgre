# Vegarlson: The Terrene Rift [Event Heroic]

**Expansion:** Chaos Descending (Exp 15)

This zone has 1 boss encounter with an OgreBot automation module.

## Available Setups

| Boss | Description |
|------|-------------|
| [Krogrock the Earthcrasher](#krogrock-the-earthcrasher) | Earth Rumble jousting, frontal rock spit avoidance (WIP) |

---

## Krogrock the Earthcrasher

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

!!! warning "Work in Progress"
    This encounter's automation is still under development.

### Overview

A fight with earth rumble jousting and frontal avoidance.

### What the Module Does

**Earth Rumble Jousting:**

- When the boss rumbles the earth, the module calculates which of two positions is farther from the boss
- Moves the group to the farther position after a short delay

**Frontal Rock Spit Avoidance:**

- When the boss rears back to spit rocks, all characters move behind the boss
- Positions reset automatically after 10 seconds

### Player Notes

- Fighters and non-fighters have separate position sets
- The joust alternates between two positions based on boss proximity
