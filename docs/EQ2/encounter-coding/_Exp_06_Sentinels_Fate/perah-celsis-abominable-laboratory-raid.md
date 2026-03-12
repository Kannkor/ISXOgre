# Perah'Celsis' Abominable Laboratory [Raid]

**Expansion:** Sentinel's Fate (Exp 06)

This zone has 2 boss encounters with active OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Arkanthis](#arkanthis) | Curse calling, auto-target add management |
| [Xilaxis](#xilaxis) | AE red text timer |

---

## Arkanthis

Setup is automatic when engaged.

### Overview

A fight with curse calling and automated add targeting when debuffed.

### What the Module Does

**Curse Calling:**

- When the Destruction or Freeze detriment is detected, calls for cure curse
- Freeze curse triggers cure only for Priests, Fighters, or players who also have the Adds detriment

**Auto-Target Add Management:**

- When the Adds detriment is detected, enables AutoTarget with a 40-meter scan radius
- Prioritizes "a benthic defiler" and "a benthic warlord" as targets
- Falls back to Xilaxis and Arkanthis when no adds are present
- Clears AutoTarget when the detriment drops

### Player Notes

- Add targeting is automatic based on detriment detection

---

## Xilaxis

Setup is automatic when engaged.

### Overview

A fight with an AE red text timer.

### What the Module Does

**AE Red Text Timer:**

- When Xilaxis channels energy from the ocean, starts a 60-second HUD countdown
- Only fires for raid groups 2+ (group 1 excluded)

### Player Notes

- Timer-only module for non-group-1 players
