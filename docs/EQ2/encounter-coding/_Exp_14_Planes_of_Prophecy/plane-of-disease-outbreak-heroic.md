# Plane of Disease: Outbreak [Heroic]

**Expansion:** Planes of Prophecy (Exp 14)

This zone has 3 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [The Flesh Eater](#the-flesh-eater) | Auto Hirudin Extract item use, auto-dispelling |
| [Rallius Rattican](#rallius-rattican) | Full bard pull sequence (spore collection, mezzing, pulling), quarantine handling |
| [High Dragoon V'Aliar](#high-dragoon-valiar) | Planar static jousting |

---

## The Flesh Eater

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with automatic item usage and dispelling.

### What the Module Does

**Auto Item Use (Hirudin Extract):**

- When the boss approaches, detects the stone skin buff and automatically uses Hirudin Extract from inventory

**Auto-Dispelling:**

- Mages and druids automatically dispel the boss's buff when detected

### Player Notes

- Keep Hirudin Extract items in inventory

---

## Rallius Rattican

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A complex fight with a full automated pull sequence and quarantine handling.

### What the Module Does

**Full Pull Sequence (Bard/Marked):**

- Checks for Bileburn Spore items, collecting more if needed from NPCs
- Navigates to and mezzes 3 patrons of plagues using the spores
- Pulls Rallius Rattican with an appropriate class ability
- Returns to the raid position

**Quarantine Handling:**

- When quarantined, pauses all actions, targets self, and waits for the teleport to complete
- Resumes normal operation after returning from quarantine

### Player Notes

- The bard will automatically pull for you
- Camp spot tolerance is set very high to handle the massive vertical knockup

---

## High Dragoon V'Aliar

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with planar static jousting.

### What the Module Does

**Planar Static Jousting:**

- When planar static increases, moves the group to whichever of two positions is farther from the boss

### Player Notes

- The joust alternates between two positions based on boss proximity
