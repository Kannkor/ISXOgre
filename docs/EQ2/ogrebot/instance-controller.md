# Instance Controller

The Instance Controller is OgreBot's system for automating boss fight mechanics in EverQuest 2 dungeons and raids. Instead of manually handling every mechanic (jousting, target switching, clicking objects, etc.), the Instance Controller runs specialized scripts that handle these mechanics for you.

---

## What Does It Do?

When you enter a supported zone, the Instance Controller can:

- **Joust automatically** -- Move characters out of AoE range and back in at the right time
- **Switch targets** -- Automatically target adds, specific NPCs, or objects during fight phases
- **Click objects** -- Interact with zone objects during scripted events
- **Handle curses and detriments** -- Respond to specific debuffs that require player action
- **Manage positioning** -- Move characters to safe spots during dangerous mechanics
- **Coordinate the group** -- Issue commands to all characters simultaneously

> **:memo: Zone Support**
>
> The Instance Controller only works in zones that have scripts written for them. Not every zone is supported, and new zone scripts are added over time as content is released.

---

## How It Works

1. When you zone into a supported instance, OgreBot detects the zone
2. If an Instance Controller script exists for that zone, it loads automatically
3. The script monitors the fight and triggers mechanics as needed
4. You can also start instance scripts manually from the OgreBot UI

<!-- TODO: Add screenshot of Instance Controller UI -->

---

## Supported Zones

Instance Controller scripts are organized by expansion:

| Expansion | Folder |
|-----------|--------|
| Rage of Cthurath (current) | `_Exp_22_Rage_of_Cthurath` |
| Scars of Destruction | `_Exp_21_Scars_of_Destruction` |
| Ballads of Zimara | `_Exp_20_Ballads_of_Zimara` |

Each expansion folder contains scripts for both heroic instances and raid zones. The number of supported encounters varies per expansion.

---

## Using the Instance Controller

### Automatic Mode

In most cases, Instance Controller scripts load and run automatically when you enter a supported zone. No manual intervention is needed.

### Manual Control

If you need to start or restart an instance script:

1. Open the OgreBot main UI
2. Navigate to the Instance Controller section
3. Select the zone and encounter
4. Start the script

---

## Tips

> **:bulb: Group Leader**
>
> Instance Controller commands are typically issued by the group leader's session. Make sure OgreBot is running on your group leader character for full functionality.

> **:warning: Stay Updated**
>
> Instance Controller scripts are updated when encounter mechanics change. Keep ISXOgre up to date to ensure you have the latest scripts for current content.

<!-- Source: wiki.ogregaming.com/eq2/index.php/OgreInstanceController - This page may need updating -->
