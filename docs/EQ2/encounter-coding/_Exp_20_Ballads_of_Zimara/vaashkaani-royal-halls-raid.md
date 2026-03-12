# Vaashkaani, Royal Halls [Raid]

**Expansion:** Ballads of Zimara (Exp 20)

> **:warning: Work In Progress**
>
> This zone's automation is still under development. Some mechanics may not be fully automated yet.

This raid zone contains 2 boss encounters.

## Available Setups

| Boss | Description |
|------|-------------|
| [Sti'Vyrn the Persecutor](#stivyrn-the-persecutor) | Persecution chamber rescue and add timers (WIP) |
| [Zakir-Sar-Ussur](#zakir-sar-ussur) | Maze phases and add management (WIP) |

---

## Sti'Vyrn the Persecutor

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A complex encounter where players get trapped in Persecution Chambers and must be rescued by other raid members.

### What the Module Does

**Persecution Chamber Rescue:**

- Detects when players are trapped in chambers
- Coordinates rescue by moving players to the chamber location
- Handles chamber killing to free trapped players

**Ambitious Defamation:**

- Tracks the Ambitious Defamation detriment which prevents players from approaching chambers

**Add Timers:**

- Tracks alternating add spawn timers for Metallic Mindmelter and Vicar of Alloys adds (60-second cycles)
- Chamber spawn timer at 150 seconds when boss is below 50% health

### Player Notes

- This encounter is a work in progress
- Chamber rescue mechanics are still being refined
- Pay attention to Ambitious Defamation -- affected players cannot go near chambers

---

## Zakir-Sar-Ussur

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with maze phases at specific health thresholds and add management between phases.

### What the Module Does

**Maze Phases:**

- Maze phases trigger at 95%, 50%, and 20% health
- TTS alert announces "Maze time" for fighters

**Add Management:**

- Auto-targets summoned Ritual Caster adds outside the maze

**Ability Management:**

- Temporal Mimicry is disabled for enchanters during this fight

### Player Notes

- This encounter is a work in progress
- Watch for the "Maze time" TTS alert at each health threshold
- Kill Ritual Caster adds outside the maze between phases
