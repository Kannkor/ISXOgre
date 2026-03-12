# Shadeweaver Thicket: Spirit Harvest [Raid]

**Expansion:** Reign of Shadows (Exp 17)

This zone has 2 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Nelon Hes](#nelon-hes) | Distance-based jousting when power is siphoned |
| [Hoggith the Eternal Cinder](#hoggith-the-eternal-cinder) | Targeted debuff avoidance with joust mechanic |

---

## Nelon Hes

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a proximity-based jousting mechanic triggered by a power siphon.

### What the Module Does

**Power Siphon Joust:**

- When the boss begins siphoning power, the module calculates which of two predefined raid spots is farther from the boss
- The group is automatically moved to the farther position

### Player Notes

- The module automatically selects the optimal joust position based on distance from the boss

---

## Hoggith the Eternal Cinder

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a targeted debuff that requires the targeted player to stay put while everyone else jousts away.

### What the Module Does

**Tentacle Targeting:**

- When tentacles target an ally, the module checks after a brief delay whether the current character has the "Targeted!" detriment
- If targeted, the character stays at their current position to avoid moving into others
- If not targeted, the character jousts to whichever predefined raid spot is farther from the boss
- After 12 seconds, positioning returns to normal

### Player Notes

- Targeted players are pinned in place while everyone else moves away
- The module handles the distinction between targeted and non-targeted players automatically
