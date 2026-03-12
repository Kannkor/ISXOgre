# Castle Mischief [Raid]

**Expansion:** Chaos Descending (Exp 15)

This zone has 1 boss encounter with an OgreBot automation module.

## Available Setups

| Boss | Description |
|------|-------------|
| [Fizzlethorpe Bristlebane](#fizzlethorpe-bristlebane) | Auto-execute movement command from buff examine (WIP) |

---

## Fizzlethorpe Bristlebane

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

!!! warning "Work in Progress"
    This encounter's automation is still under development.

### Overview

A fight where the boss gives players a buff that contains a movement command they must execute.

### What the Module Does

**Urge to Move Buff Reading:**

- Detects the Urge to Move buff on the character
- Automatically examines the buff via the UI to read the movement command text
- Executes the parsed movement command automatically
- Closes the examine window after processing

### Player Notes

- The module reads and executes movement commands from the buff automatically
- Other bosses in this zone (Maxima Kierran, Linneas the Stitcher, A Stringed Puppet) do not have automation
