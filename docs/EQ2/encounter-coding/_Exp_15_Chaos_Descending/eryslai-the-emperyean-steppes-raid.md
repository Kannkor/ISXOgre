# Eryslai: The Emperyean Steppes [Raid]

**Expansion:** Chaos Descending (Exp 15)

This zone has 1 boss encounter with an OgreBot automation module.

## Available Setups

| Boss | Description |
|------|-------------|
| [Rinturion Windblade](#rinturion-windblade) | Dance of Blades jousting with phase tracking |

---

## Rinturion Windblade

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with jousting triggered by the Dance of Blades mechanic.

### What the Module Does

**Dance of Blades Jousting:**

- When the boss announces the Dance of Blades, calculates which of two positions is farther and moves there
- Tracks the dance phase number (1, 2, or 3) based on the boss's announcement
- HUD displays the current dance phase and a countdown to the next dance (45 seconds)

### Player Notes

- Fighters and non-fighters have separate position sets
- The joust alternates between two positions based on boss proximity
