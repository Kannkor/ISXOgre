# F.S. Distillery [Raid]

**Expansion:** Altar of Malice (Exp 11)

This zone has 6 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Brutas the Imbiber](#brutas-the-imbiber) | Cold water cure automation for sticky situation debuff |
| [Bull McCleran](#bull-mccleran) | Front/behind positional movement, enchanter auto-dispel |
| [Charanda](#charanda) | Crouch management, protected add detection |
| [Captain Mergin](#captain-mergin) | Auto-dispelling of rum buff |
| [Brunhildre the Wench](#brunhildre-the-wench) | Cure curse callout coordination |
| [Kildiun the Drunkard](#kildiun-the-drunkard) | Barrel roller auto-targeting |

---

## Brutas the Imbiber

Setup is automatic when engaged.

### Overview

A fight where bards and enchanters must free players stuck with the Sticky Situation debuff using cold water.

### What the Module Does

**Cold Water Automation:**

- Monitors for the Sticky Situation debuff on group members
- When detected, bards notify enchanters (and vice versa) that cold water is needed
- The automated character goes to the water barrel, picks up cold water, navigates to the affected player, and uses the item on them

### Player Notes

- Entire group must be controlled by you for this automation to work

---

## Bull McCleran

Setup is automatic when engaged.

### Overview

A fight with positional mechanics where the raid must move in front of or behind the boss based on his attacks.

### What the Module Does

**Positional Movement:**

- On "massive smash!" announcement, moves the raid behind Bull
- On "massive backlash!" announcement, moves the raid in front
- Non-fighters auto-return to behind position after 9 seconds

**Auto-Dispelling:**

- Enchanters automatically dispel Bull's stacking buff to prevent it from increasing

### Player Notes

- The module handles preventing the boss's stacking buff from growing

---

## Charanda

Setup is automatic when engaged.

### Overview

A fight where players must crouch to avoid noxious gas and identify which protected add type to avoid killing.

### What the Module Does

**Crouch Management:**

- Manages crouching and standing based on gas cloud phases
- After the gas dissipates, automatically stands up and re-crouches 20 seconds later

**Protected Add Detection:**

- When an Undead Despoiler spawns, scans Charanda's effects to determine which add type is protected (Focuser, Ruiner, or Despoiler)
- Displays the protected add type on HUD

### Player Notes

- Start the fight crouched
- Dying messes up the crouch state

---

## Captain Mergin

Setup is automatic when engaged.

### Overview

A fight with a buff that must be continuously dispelled.

### What the Module Does

**Auto-Dispelling:**

- All classes automatically dispel Captain Mergin's "the rum is not gone" buff when detected

### Player Notes

- Dispelling is not limited to enchanters -- all classes participate

---

## Brunhildre the Wench

Setup is automatic when engaged.

### Overview

A fight with a curse mechanic requiring coordinated cure timing.

### What the Module Does

**Cure Curse Callout:**

- Disables normal curse curing
- Monitors the Scabies curse duration
- When duration drops below 10 seconds, calls out for cure curse coordination via uplink

### Player Notes

- Normal cure curse is disabled to prevent wasting cures at the wrong time

---

## Kildiun the Drunkard

Setup is automatic when engaged.

### Overview

A fight with barrel roller adds that must be quickly targeted and killed.

### What the Module Does

**Barrel Roller Auto-Targeting:**

- When a barrel roller spawns, automatically targets the add
- HUD timer shows a 15-second countdown for the next barrel roller
- When the roller is called out targeting you, automatically switches target to it

### Player Notes

- The module handles target switching; focus on DPS when the add appears
