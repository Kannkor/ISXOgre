# Raj'Dur Plateaus: The Hunt [Raid]

**Expansion:** Renewal of Ro (Exp 19)

!!! warning "Work in Progress"
    Automation for Raj'Dur Foreman Yato is still under development.

This raid zone contains 4 boss encounters.

## Available Setups

| Boss | Description |
|------|-------------|
| [Avenging Desert Spectre](#avenging-desert-spectre) | Auto joust on text, "stay out" mechanic |
| [Raj'Dur Leader Mamu](#rajdur-leader-mamu) | Auto joust on text, pool jousting |
| [Poacher Paol](#poacher-paol) | Hide behind birds, archetype-ordered positioning |
| [Raj'Dur Foreman Yato](#rajdur-foreman-yato) | Auto joust on text, pool jousting (WIP) |

---

## Avenging Desert Spectre

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where non-fighters must joust away from the named on specific text triggers, with a "stay out" watching mechanic.

### What the Module Does

**Joust Away:**

- Non-fighters automatically joust away from the named when "Allow this to be a learning experience!" is detected

**Stay Out:**

- When the named is watching, a 20-second "stay out" period begins where players must remain away

### Player Notes

- Fighters are excluded from the joust mechanic
- Stay alert for the watching mechanic — remain away for the full duration

---

## Raj'Dur Leader Mamu

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a text-triggered joust and sizzling metal pool AoE avoidance.

### What the Module Does

**Power Drain Joust:**

- Automatically jousts away from the named when "Give me your power" is detected
- Tanks are excluded from this joust

**Sizzling Metal Pool:**

- Detects sizzling metal pool AoE spawns
- Automatically jousts away from the pool location
- Configurable joust duration (default 45 seconds)

### Player Notes

- Tanks stay on the named during the power drain joust
- Pool jousting is handled automatically

---

## Poacher Paol

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where players must hide behind peafowl birds, with positioning determined by archetype.

### What the Module Does

**Hide Behind Birds:**

- Automatically clicks on peafowl birds to activate them
- Positions players behind birds in archetype order (priests first, then non-priests)
- Uses 3 pairs of alternating spots for positioning

**Interrupt Healing:**

- Interrupts healing when required by the encounter

### Player Notes

- Positioning is handled automatically — priests are prioritized for placement
- Do not manually click birds as the module handles the sequence

---

## Raj'Dur Foreman Yato

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

!!! warning "Work in Progress"
    This encounter's automation is still under development.

### Overview

A fight where non-fighters must joust away on a text trigger, with sizzling metal pool AoE avoidance.

### What the Module Does

**Joust Away:**

- Non-fighters automatically joust away when "targets those nearby" is detected

**Sizzling Metal Pool:**

- Detects sizzling metal pool AoE spawns
- Automatically jousts away from the pool location

### Player Notes

- Fighters are excluded from the joust mechanic
- Pool jousting is handled automatically
