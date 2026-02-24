# Crowd Control

<!-- TODO: Add screenshot -->

This tab controls all crowd control abilities.

## Managing Abilities

### Adding abilities to the Cast Order

Double-click abilities on the left side to move them to the right (Cast Order) section.

### Removing abilities from the Cast Order

Select an ability by left-clicking, then right-click to remove it.

### Re-ordering your Cast Order

Click and hold an ability within the Cast Order, then drag it up or down to reposition it.

### Turning abilities On/Off

Double-click abilities in the Cast Order to toggle them:

- **White** - Active (will cast)
- **Black** - Inactive (will not cast)

## Behavior

The crowd control system accepts various crowd control spells including single-target mezes, group mezes, and root abilities.

Key behaviors:

- Does **not** affect your assist target or temporary assist targets (like those set via AssistUI)
- Mezes other hostile creatures that have aggro on you or your group members
- Re-applies crowd control to targets with less than 10 seconds remaining duration using the same ability
- Avoids attempting to mez epic-level creatures
- Will proceed to nuke after mezzing if you lack an assist designation with CAs enabled

<!-- Source: wiki.ogregaming.com - This page may need updating -->
