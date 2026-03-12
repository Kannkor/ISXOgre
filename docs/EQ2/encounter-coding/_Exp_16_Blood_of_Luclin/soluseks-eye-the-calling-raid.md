# Solusek's Eye: The Calling [Raid]

**Expansion:** Blood of Luclin (Exp 16)

This zone has 1 boss encounter with an OgreBot automation module.

## Available Setups

| Boss | Description |
|------|-------------|
| [The Iron Widow](#the-iron-widow) | Color panel assignment for raid members (WIP) |

---

## The Iron Widow

> **:warning: Work In Progress**
>
> This encounter's automation is still under development. Some mechanics may not be fully automated yet.

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A color-matching encounter where the boss calls out colored mechanics and non-fighter raid members must stand on the correct colored panels. Colors can be primary (Red, Blue, Yellow) or mixed (Orange, Purple, Green, White), requiring players to stand on specific panel combinations.

### What the Module Does

**Color Panel Assignment:**

- When the boss calls a color, non-fighter raid members are assigned to the correct colored panels
- Color assignments follow these rules:
    - **Red** = red panels
    - **Blue** = blue panels
    - **Yellow** = yellow panels
    - **Orange** = red + yellow panels
    - **Purple** = red + blue panels
    - **Green** = yellow + blue panels
    - **White** = all three panels (red + blue + yellow)
- Players are assigned to specific panels based on their raid position
- The "Set up for widow" command repeats the last color assignment

### Player Notes

- Non-fighter raid members are automatically moved to the correct panels when a color is called.
- Fighters are excluded from panel assignments.
- Mixed colors (Orange, Purple, Green, White) require players to cover multiple panel types.
- You can use "Set up for widow" to repeat the last color assignment if needed.
- This module is a work in progress.
