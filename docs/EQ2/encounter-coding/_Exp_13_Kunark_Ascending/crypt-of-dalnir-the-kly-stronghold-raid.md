# Crypt of Dalnir: The Kly Stronghold [Raid]

**Expansion:** Kunark Ascending (Exp 13)

!!! warning "Work in Progress"
    This module is still under development. Some encounters may have partial or missing automation.

This zone has 2 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [The Kly](#the-kly) | Orb color detection and waypointing |
| [The Lumpy Goo](#the-lumpy-goo) | Druid auto-dispelling |

---

## The Kly

Setup command: `Set up for Kly`

### Overview

A fight centered around power orb color identification. The module detects which orb is active and displays it on the HUD with a waypoint.

### What the Module Does

**Orb Color Detection:**

- When The Kly draws power from his orbs, the module reads the Active Power Orb's tint to determine its color (Purple, Red, Blue, or Green)
- Polls up to 10 times at 1-second intervals until the color resolves
- Displays the orb color on the HUD
- Sets an in-game waypoint to the matching static orb's location

### Player Notes

- The module provides information only -- players must manually navigate to the correct orb
- Full raid movement automation for the orb mechanic is not yet implemented

---

## The Lumpy Goo

Setup is automatic when engaged.

### Overview

A fight where Druids automatically dispel the boss.

### What the Module Does

**Auto Dispell:**

- Druids automatically dispel a buff from The Lumpy Goo when detected

### Player Notes

- Only Druid classes perform the dispelling
