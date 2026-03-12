# Ruins of Kaesora: Ancient Xalgozian Temple [Raid]

**Expansion:** Kunark Ascending (Exp 13)

!!! warning "Work in Progress"
    This module is still under development. Some encounters may have partial or missing automation.

This zone has 2 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [The Strathbone Runelord](#the-strathbone-runelord) | Stops casting during suppression, cross-session auto-curing |
| [Xalgoz](#xalgoz) | Archetype-based tank swap, Staff of Control auto-usage |

---

## The Strathbone Runelord

Setup is automatic when engaged.

### Overview

A fight where players must stop casting during the Runelord's suppression phase or face punishment.

### What the Module Does

**Suppression Warning:**

- When the Runelord uses suppression, OgreBot pauses casting for 5 seconds as a preventive measure

**Do Not Cast Phase:**

- When the full "do not cast" warning fires, OgreBot immediately cancels any in-progress cast and stops all actions
- Targets self and waits to become cursed
- Once cursed, sends a cross-session auto-cure command so all sessions cure the curse
- Resumes normal behavior once the curse is removed

### Player Notes

- The IRC relay system must be active for the cross-session cure commands to work

---

## Xalgoz

Setup is automatic when engaged.

### Overview

A fight where Xalgoz periodically demands a specific archetype to tank him. The module handles stopping fighters from attacking when another archetype is called.

### What the Module Does

**Archetype Tank Swap:**

- When Xalgoz calls for a specific archetype's blood (fighter, scout, mage, or priest), the module displays which archetype must tank
- If fighters are NOT the called archetype, all fighters stop offensive actions automatically
- When fighters are called again, offensive actions resume
- Shows a HUD message indicating which archetype needs to tank

**Staff of Control Usage:**

- Marked toons of the currently-called archetype automatically use Xalgoz's Staff of Control from their at-hand inventory slot when it is off cooldown

### Player Notes

- Toons must be **marked** in the OgreBot UI for the Staff of Control usage to activate
- Tank swaps occur at health thresholds (approximately 85%, 65%, 40%)
