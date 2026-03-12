# The Fabled Djinn Master's Prism [Raid]

**Expansion:** Tears of Veeshan (Exp 10)

This zone has 4 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Guardian Tyniss](#guardian-tyniss) | Timed curse callout |
| [Honorguard Maro Joavao](#honorguard-maro-joavao) | Red text joust between two positions |
| [Honorguard Taro Joavao](#honorguard-taro-joavao) | No active mechanics |
| [The Djinn Master](#the-djinn-master) | Elemental sigil portal navigation, stun control, instrument placement and playing |

---

## Guardian Tyniss

Setup is automatic when engaged.

### Overview

A fight with a timed curse mechanic.

### What the Module Does

**Timed Curse Callout:**

- Monitors the curse detriment
- Calls for cure curse in raid chat when detected

### Player Notes

- Cure timing is coordinated via raid chat

---

## Honorguard Maro Joavao

Setup command: `Set up for Maro`

### Overview

A fight with a heat-based joust mechanic.

### What the Module Does

**Red Text Joust:**

- When the djinn is engulfed in flames, shows a 40-second HUD countdown
- Determines if the boss is closer to the normal or joust positions, then moves the raid to the opposite set

### Player Notes

- Ping-pong joust between two position sets

---

## Honorguard Taro Joavao

Setup is automatic when engaged.

### Overview

This boss has no active mechanic automation.

### What the Module Does

No active automation.

### Player Notes

- No coded mechanics for this encounter

---

## The Djinn Master

Setup command: `Set up for Master`

### Overview

An extremely complex fight with elemental sigil portals, stun management, and an instrument placement/playing mechanic.

### What the Module Does

**Elemental Sigil Portals:**

- Tracks 4 elemental curses: Earth, Fire, Water, and Ice
- Each curse requires running to the opposing element's portal (Earth curse goes to Water portal, etc.)
- Portal locations are tracked dynamically as they spawn and broadcast to all sessions
- When cursed, automatically navigates to the correct portal and waits until the curse clears

**Stun Control:**

- Melodic fury adds spawn with different guild names controlling stun permissions
- "Spinner of Mayhem" and "Spinner of Fury": stuns disabled
- "Spinner of Malice": stuns enabled
- HUD shows current add status and 50-second timer for next add

**Instrument Mechanic:**

- 6 instruments can be placed at specific locations and played in sequence
- Auto-placement mode walks instruments to their positions
- Play mode walks to each instrument in a specified order and uses the Play verb
- Song success/failure tracked with HUD

**Knockback Timer:**

- Rage of the Djinn timer (36/72 seconds)

### Player Notes

- Requires OgreCraftMove script for physical movement during portal cleansing and instrument placement
- Stuns are automatically disabled on setup
- Enchanter Possess Essence is disabled and pets are dismissed
