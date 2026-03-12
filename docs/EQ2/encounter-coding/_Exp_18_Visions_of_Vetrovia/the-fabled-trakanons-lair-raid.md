# The Fabled Trakanon's Lair [Raid]

**Expansion:** Visions of Vetrovia (Exp 18)

This zone has 1 boss encounter with an OgreBot automation module.

## Available Setups

| Boss | Description |
|------|-------------|
| [Trakanon](#trakanon) | Mark of Repulsion jousting, Summoned Ritualist item usage (WIP) |

---

## Trakanon

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

!!! warning "Work in Progress"
    This encounter's automation is still under development.

### Overview

A fight with a mark-based joust mechanic and a ritualist handling phase.

### What the Module Does

**Mark of Repulsion Jousting:**

- When the Mark of Repulsion detriment is detected, the character saves its current position, moves to a joust point approximately 50m away, and jumps
- When the mark clears, returns to the saved position

**Summoned Ritualist Handling:**

- A flagged character scans for Summoned Ritualists with high health
- Pauses ALL casting (offensive, defensive, and general), waits for current cast to finish
- Moves to the ritualist, targets it, uses a Crystal of Dark Energy item on it
- Returns to position and resumes casting after success

### Player Notes

- The joust saves and restores your exact position
- The ritualist phase pauses all casting temporarily to ensure the item is used correctly
