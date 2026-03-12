# Siren's Grotto [Heroic]

**Expansion:** Chains of Eternity (Exp 09)

This zone has 3 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Queen Dulseris](#queen-dulseris) | Automated shell clicking for portal mechanic |
| [Overlord Talan](#overlord-talan) | Mark/curse repositioning, doppelganger add management |
| [Mindscorcher Shelik](#mindscorcher-shelik) | Targeted joust |

---

## Queen Dulseris

Setup command: `Set up for Queen`

### Overview

A fight where portals must be sealed by clicking shells in the arena.

### What the Module Does

**Shell Clicking (Portal Mechanic):**

- When the Queen summons protectors, bards automatically run to click shells to put barriers back up
- When a specific player is called to close a portal, that player runs to the nearest shell
- Automatically finds the closest of three shell locations, moves to it, and double-clicks
- Non-fighters target themselves while running to avoid breaking the encounter
- Returns to camp and cancels Sprint after clicking

**Positioning:**

- Fighters at tank spot, everyone else at raid spot

### Player Notes

- Shell clicking is fully automated

---

## Overlord Talan

Setup command: `Set up for Talan`

### Overview

A fight with curse-based repositioning and doppelganger add management.

### What the Module Does

**Mark/Curse Repositioning:**

- When cursed with the Talan Mark detriment:
    - Fighters move to a curse spot (different spot depending on whether an add is up)
    - Non-fighters move to the raid curse spot
- When the curse clears, returns to normal positions
- Announces "Talan Mark!" to the group

**Study Tactics Timer:**

- When Talan studies your tactics, starts a 70-second HUD countdown
- Fighters target themselves for 10 seconds during the study phase if no add is up

**Scorching Faith AE Timer:**

- Starts a 120-second HUD countdown when the AE fires

**Doppelganger Add Management:**

- When a fake Talan spawns (non-KOS faction), fighters move to the add tank spot
- All players force-target the fake add
- HUD timers track add spawn cycles

### Player Notes

- Positions shift dynamically based on curse state and add presence

---

## Mindscorcher Shelik

Setup command: `Set up for Mindscorcher` (also accepts `Set up for Shelik`)

### Overview

A fight with a targeted destruction joust.

### What the Module Does

**Targeted Joust:**

- When Mindscorcher Shelik "focuses his destruction" on a specific player, that player jousts to the safe spot
- Returns to camp after 12 seconds

### Player Notes

- Only the targeted player moves
