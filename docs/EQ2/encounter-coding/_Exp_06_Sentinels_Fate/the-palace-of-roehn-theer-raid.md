# The Palace of Roehn Theer [Raid]

**Expansion:** Sentinel's Fate (Exp 06)

This zone has 4 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Azara the Seer](#azara-the-seer) | Ritual joust |
| [Maalus Imbued](#maalus-imbued) | Joust on dooming mist/incantation, cure curse, port detection with add targeting, charm detection |
| [Penda and Kendis](#penda-and-kendis) | Shield activation/deactivation offensive toggle |
| [The Three Sages](#the-three-sages) | Noxious cure with Necrotic Flashpot item |

---

## Azara the Seer

Setup is automatic when engaged.

### Overview

A fight with a ritual joust.

### What the Module Does

**Ritual Joust:**

- When Azara begins a powerful ritual, jousts out

### Player Notes

- Simple joust-out on trigger

---

## Maalus Imbued

Setup is automatic when engaged.

### Overview

A complex fight with directional jousting, curse curing, port detection with automatic add killing, and charm detection.

### What the Module Does

**Jousting:**

- On "dooming mist" hitting the player, jousts out
- On "Evil Incantation" hitting the player, jousts in

**Cure Curse:**

- Greater Curse of Devastation — detects the cursed player, displays on HUD with 54-second timer, and triggers auto-cure with an 8-second throttle

**Port Detection:**

- When the player is teleported to the port area, announces to the raid
- Enables AutoTarget to find and kill the player's own shadow clone add
- Clears all settings when the player returns from the port area

**Charm Detection:**

- When the charm detriment is detected, announces to the raid and stops all actions

### Player Notes

- Add targeting in the port phase is fully automated

---

## Penda and Kendis

Setup is automatic when engaged.

### Overview

A fight where the bosses activate retributive auras that require stopping all attacks.

### What the Module Does

**Shield Activation/Deactivation:**

- When Penda activates her Aura of Arcane Retribution, disables offensive abilities
- When Kendis activates his aura of physical retribution, disables offensive abilities
- Re-enables offensive when the auras are blocked in the correct order

### Player Notes

- Offensive toggling is automatic based on shield state

---

## The Three Sages

Setup is automatic when engaged.

### Overview

A fight where noxious-afflicted raid members need to be cured using the Necrotic Flashpot item.

### What the Module Does

**Noxious Cure (Necrotic Flashpot):**

- Scans all raid members for noxious debuffs
- If a debuffed member is within 70 meters and has line of sight, targets them and uses the Necrotic Flashpot item

### Player Notes

- Requires "Necrotic Flashpot" inventory item
