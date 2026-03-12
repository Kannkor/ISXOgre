# Siren's Grotto [Raid]

**Expansion:** Chains of Eternity (Exp 09)

This zone has 7 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Diviner Gelerin](#diviner-gelerin) | Curse self-cure, crippled armor management, NPC dispel |
| [Priestess](#priestess) | Crippled armor management, positioning |
| [Caella](#caella) | Add spawn notification, positioning |
| [Gen'ra](#genra) | Color detriment repositioning, personal add management |
| [Lisha](#lisha) | Memwipe timer |
| [Overlord Talan](#overlord-talan) | Venom cure, arc lightning joust, doppelganger add management, NPC dispel |
| [Psyllon'Ris](#psyllonris) | Venom joust, phoenix/class-specific add handling, dynamic tank positioning |

---

## Diviner Gelerin

Setup command: `Set up for Diviner`

### Overview

A fight with curse self-cures, crippled armor management, and NPC dispelling.

### What the Module Does

**Curse Self-Cure:**

- When cursed, priests automatically cure themselves

**Crippled Armor Management:**

- Fighters with more than 3 stacks of Crippled Armor disable offensive abilities
- Re-enables when stacks drop below the threshold

**NPC Dispel:**

!!! warning "Requires Elite 1"
    NPC dispel requires Elite 1 access.

- Enchanters in groups 1/2 dispel Diviner Gelerin
- Enchanters in groups 3/4 dispel Persecutor Barid

**Positioning:**

- Separate positions by raid group and role (groups 1/2 vs groups 3/4)

### Player Notes

- Positioning varies by raid group number

---

## Priestess

Setup command: `Set up for Priestess`

### Overview

A positioning setup with crippled armor management.

### What the Module Does

**Crippled Armor Management:**

- Fighters with more than 3 stacks of Crippled Armor disable offensive abilities

**Positioning:**

- Fighters in groups 1 or 4 go to tank spot, everyone else to raid spot

### Player Notes

- Shared crippled armor logic with Diviner Gelerin

---

## Caella

Setup command: `Set up for Caella`

### Overview

A fight with add spawn notifications.

### What the Module Does

**Add Spawn Notification:**

- When "a siren controller" spawns, fighters broadcast a message that the add has appeared

**Positioning:**

- Single position for all players

### Player Notes

- Simple positioning with add awareness

---

## Gen'ra

Setup command: `Set up for Genra`

### Overview

A fight with color-based detriment repositioning and personal add management.

### What the Module Does

**Color Detriment Repositioning:**

- Monitors three color detriments: Red, Blue, and Yellow
- When a color detriment is detected, fighters disable offensive and cast Recapture
- All players move to the corresponding color-safe position
- Returns to camp when the detriment clears

**Personal Add Management:**

- When "a stinging urchin" spawns that belongs to the player, fighters disable offensive and move to the add spot
- Resets when the add or Gen'ra despawns

### Player Notes

- Extended leash distance (250) is set on setup

---

## Lisha

Setup is automatic when engaged.

### Overview

A fight with a memwipe timer.

### What the Module Does

**Memwipe Timer:**

- When Lisha calls for her pet, starts a 30-second HUD countdown for the next memwipe

### Player Notes

- Timer-only module with no positioning

---

## Overlord Talan

Setup command: `Set up for Talan`

### Overview

A complex fight with venom curing, arc lightning jousting, doppelganger add management, and multi-tank positioning.

### What the Module Does

**Venom Cure:**

- When the venom detriment is detected, automatically uses the "a venomous spine" inventory item to cure it

**Arc Lightning Joust:**

- When the arc lightning detriment is detected, jousts everyone to arc-safe positions
- Different positions for tank groups vs. non-tanks
- Fighters announce and have offensive disabled

**Crippled Armor Management:**

- Fighters with more than 3 stacks of Crippled Armor disable offensive (group 4 fighters excluded)

**Doppelganger Add Management:**

- When a Psionic Doppelganger of Talan spawns, group 4+ fighters target it
- HUD timers track add spawn/despawn cycles (40-second timers)
- Dynamic assist switching between the real boss and adds

**NPC Dispel:**

- Enchanters in groups 1/2 dispel the real Talan (Psionic Knight)
- Enchanters in groups 3/4 dispel the fake Talan (Psionic Doppelganger)
- Will not dispel if the player is cursed

**Multi-Tank Positioning:**

- Four different tank positions by raid group (groups 1, 2, 3, and 4+)

### Player Notes

- Requires "a venomous spine" inventory item for venom curing

---

## Psyllon'Ris

Setup command: `Set up for Psyllon`

### Overview

The final boss with venom jousting, phoenix priority targeting, class-specific add handling, and dynamic tank positioning.

### What the Module Does

**Venom Joust:**

- Non-tank players with Living Venom joust to the safe spot
- Fighters with venom announce to the raid

**Phoenix Add (Full Heal Timer):**

- When a stinging phoenix spawns, starts a 40-second HUD countdown for the full heal
- Non-tanks force-target the phoenix (takes priority over all other adds)

**Class-Specific Add Handling:**

- "a kelp fiend" — only Mages target this add
- "an abyssal titan" — Scouts and non-tank Fighters target this add
- "an alluring siren" — assigned by spawn location (West vs. East) and raid group (groups 1/3 handle West, groups 2/4 handle East)
- Stun avoidance is disabled when targeting an alluring siren

**Crippled Armor Management:**

- Higher threshold (6 stacks) before disabling offensive

**Dynamic Tank Positioning:**

- Tank positions are calculated relative to Psyllon'Ris's actual location

### Player Notes

- Extended leash distance (250) is set on setup
- 75-second add spawn timer displayed on HUD
