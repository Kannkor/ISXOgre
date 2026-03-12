# Aurelian Coast: The Emergent Eclipse [Raid]

**Expansion:** Blood of Luclin (Exp 16)

This zone has 3 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [The Sambata Champion](#the-sambata-champion) | Placement/positioning with grime repositioning (WIP) |
| [The Stonegrabber Colossus](#the-stonegrabber-colossus) | General placement with prismatic shield management |
| [Xi Xia Xius](#xi-xia-xius) | Detriment cancellation and challenge mode cloth mechanics |

---

## The Sambata Champion

> **:warning: Work In Progress**
>
> This encounter's automation is still under development. Some mechanics may not be fully automated yet.

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A placement and positioning fight where the boss deals AE damage in melee range and periodically teleports, requiring the group to reposition to multiple locations based on a grime mechanic.

### What the Module Does

**Placement and Positioning:**

- Only tanks should be near the boss due to AE damage around him
- When the boss teleports and the grime mechanic triggers, the group is repositioned to multiple camp locations

**Add Tracking:**

- Adds (Mutagenic Reishi) spawn periodically
- A HUD timer is displayed showing when adds are expected

### Player Notes

- Stay away from the boss unless you are a tank -- his AE damage hits anyone nearby.
- Watch for the grime mechanic teleport -- the module will reposition the group automatically.
- The HUD timer tracks Mutagenic Reishi add spawns.
- This module is a work in progress.

---

## The Stonegrabber Colossus

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A general placement fight with a prismatic shield mechanic. Fighters are given a separate tank position while the rest of the raid is positioned at range.

### What the Module Does

**General Placement:**

- Fighters receive a separate tank position
- Non-fighters are placed at a raid position

**Prismatic Shield Handling:**

- If the player is marked, they will automatically attempt to pop shield bubbles when the boss has more than 1 stack
- The module tracks the cooldown between bubble pops -- you cannot chain-pop bubbles back to back

### Player Notes

- The marked player handles prismatic shield bubbles automatically.
- Shield bubbles can only be popped when the boss has more than 1 stack, and there is an internal cooldown between pops.
- Fighters are positioned separately from the rest of the raid.

---

## Xi Xia Xius

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter centered around a shadow-feeding detriment that must be periodically cancelled. Challenge mode (Dark Xius Lord) adds cloth-management mechanics involving frayed robes and shadowed cloaking.

### What the Module Does

**Feeding From the Shadows:**

- Automatically cancels the "Feeding From the Shadows" detriment on a periodic timer
- Normal mode: cancels every 30 seconds
- Challenge mode (Dark Xius Lord): cancels every 5 seconds

**Challenge Mode -- Cloth Management:**

- When the robe is frayed, automatically grabs cloth by right-clicking "Rip a Piece of Cloth"
- When the named becomes cloaked, uses "Ripped Piece of Shadowed Cloth" to remove the cloak
- Manages enraged stacks -- will not grab cloth if already above 5 stacks to avoid pushing enrage too high

### Player Notes

- The "Feeding From the Shadows" detriment is cancelled automatically at the correct intervals for both normal and challenge mode.
- In challenge mode, cloth grabbing and usage is fully automated.
- The module tracks enraged stacks and will stop grabbing cloth above 5 stacks.
