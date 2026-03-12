# Sultan's Mahallah: Daggers Drawn [Raid]

**Expansion:** Renewal of Ro (Exp 19)

This raid zone contains 5 boss encounters.

## Available Setups

| Boss | Description |
|------|-------------|
| [Poacher Paol the Persistent](#poacher-paol-the-persistent) | Hide behind birds, archetype-ordered positioning |
| [Raaijs Viruniq, Rath'Mana](#raaijs-viruniq-rathmana) | Flame Kissed auto cure curse |
| [Stonesong, Death's Throes](#stonesong-deaths-throes) | Radiation-based positioning, pool jousting, AoE heal joust |
| [Veagth the Unnatural](#veagth-the-unnatural) | Corrosion auto-cure via item, polarity announcements |
| [Aldys, Sultan of Daggers](#aldys-sultan-of-daggers) | Epic ability, crouch/motivate mechanic, lantern clicking |

---

## Poacher Paol the Persistent

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where players must hide behind peafowl birds, with positioning determined by archetype. Similar to the Poacher Paol encounter in The Hunt.

### What the Module Does

**Hide Behind Birds:**

- Automatically clicks on peafowl birds to activate them
- Positions players behind birds in archetype order (priests first, then non-priests)
- Uses alternating spot pairs for positioning

### Player Notes

- Positioning is handled automatically — priests are prioritized for placement
- Do not manually click birds as the module handles the sequence

---

## Raaijs Viruniq, Rath'Mana

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with the Flame Kissed detriment that requires priests to cure curse with specific timing. Similar to the Raaijs Viruniq encounter in The Standing Storm.

### What the Module Does

**Flame Kissed:**

- Detects the Flame Kissed detriment
- Automatically requests a cure curse from priests only
- Uses delayed cure timing (3-second and 6-second delays) to ensure proper cure order
- Cure curse is disabled during the fight to prevent premature curing

### Player Notes

- Only priests handle the Flame Kissed cure — it is automated with proper timing delays
- Do not manually cure curse during this fight as the module manages the timing

---

## Stonesong, Death's Throes

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A complex fight with radiation-based positioning, hazardous pool avoidance, and AoE heal jousting.

### What the Module Does

**Radiation Positioning:**

- Monitors which mob or add has the "Radiated" status
- Automatically positions fighters/scouts and priests/mages to different spots based on which target is radiated vs. not radiated
- Uses 2 tank spots and 2 raid spots for positioning

**Pool Jousting:**

- Detects hazardous boiling water pool spawns
- Automatically jousts away from pool locations

**AoE Heal Joust:**

- Jousts when an AoE heal mechanic is detected

### Player Notes

- Positioning changes dynamically based on which enemy is radiated — the module handles this automatically
- Watch for pool spawns as they may require quick repositioning
- Fighter/scout and priest/mage groups are positioned separately

---

## Veagth the Unnatural

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a corrosion curse that must be cured using a specific item, and polarity mechanics requiring add positioning.

### What the Module Does

**Takish'Hiz Corrosion:**

- Detects the Takish'Hiz Corrosion detriment
- Automatically collects "Vial of Bilibin Extract" from a nearby prism actor
- Uses the item to cure the corrosion

**Polarity Announcements:**

- Announces REPEL and ATTRACT polarity changes via chat and text-to-speech
- REPEL means get the adds together
- ATTRACT means separate the adds

### Player Notes

- The vial is automatically collected from a nearby prism — ensure you are within range
- Pay attention to polarity announcements for add positioning

---

## Aldys, Sultan of Daggers

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A complex fight with epic ability usage, a crouch/motivate mechanic, and a lantern clicking sequence.

### What the Module Does

**Foresought Punishment:**

- Detects the Foresought Punishment detriment
- Automatically uses the epic ability to handle it

**Demotivational Mindset:**

- Detects the Demotivational Mindset detriment
- Automatically crouches and uses the motivate mechanic
- Each person can only motivate once per cycle

**Lantern Sequence:**

- Automatically clicks lanterns in the correct order when music notes are detected
- Follows the sequence: Plum → Scorched → Turquoise

### Player Notes

- The epic ability, crouch/motivate, and lantern mechanics are all handled automatically
- Each player can only motivate one other player per cycle
- Do not manually click lanterns as the module handles the correct sequence
