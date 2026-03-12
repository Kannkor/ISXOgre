# Solusek Ro's Tower: Citadel of the Sun [Raid]

**Expansion:** Planes of Prophecy (Exp 14)

This zone has 4 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Amohn](#amohn) | Fiery Gaze pre-curing, HUD timers |
| [Rizlona](#rizlona) | Automated archetype-based add targeting and tagging |
| [Grezou](#grezou) | Auto-dispelling Healing Flames, HUD timer |
| [Solusek Ro](#solusek-ro) | Meltdown and Dancing Flames ability broadcasts |

---

## Amohn

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with pre-cure timing and trap mechanics.

### What the Module Does

**Fiery Gaze Pre-Curing:**

- Non-shaman priests wait 4 seconds after the Fiery Gaze warning, then fire a group cure before the hit lands
- HUD displays a 50-second countdown to the next Fiery Gaze

**Trapped Timer:**

- HUD displays a 65-second countdown when a player is trapped in a fiery cage

### Player Notes

- Non-shamans handle the pre-cure automatically

---

## Rizlona

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where archetype-specific adds must be targeted by matching characters.

### What the Module Does

**Archetype-Based Add Targeting:**

- When Golden Defender adds spawn, each character targets the add matching their archetype (Scout, Mage, Priest, Fighter)
- Scouts help kill other archetypes' adds after their own dies (Fighter first, then Priest)
- Adds are automatically tagged with raid markers (skull, shield, sword, flame)
- Characters retarget Rizlona when their assigned add dies

### Player Notes

- Targeting and tagging are fully automated based on archetype matching

---

## Grezou

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a dispellable healing buff.

### What the Module Does

**Auto-Dispelling:**

- Checks every second for Healing Flames buff on the boss and dispels it automatically
- HUD displays a 30-second countdown to the next Healing Flame

### Player Notes

- Dispelling is handled automatically

---

## Solusek Ro

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with two major mechanics requiring specific ability responses.

### What the Module Does

**Meltdown Response:**

- When the boss prepares meltdown conditions, the raid leader broadcasts Thermal Depletion to the whole group

**Dancing Flames Response:**

- When the boss prepares dancing flames, the raid leader broadcasts Siphoned Fervor to the whole group

### Player Notes

- The raid leader coordinates the ability responses via cross-session commands
