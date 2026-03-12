# Zek, the Scourge Wastes: The Siege [Raid]

**Expansion:** Terrors of Thalumbra (Exp 12)

This zone has 4 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Fergul the Protector](#fergul-the-protector) | Constant movement to prevent dust buildup |
| [Durtung the Arm of War](#durtung-the-arm-of-war) | Color circle archetype movement, add tracking |
| [Sanctifier Goortuk](#sanctifier-goortuk) | Shift Vision casting, flame waypoints |
| [The Weapon of War](#the-weapon-of-war) | Auto-dispell, mark of tactics tank management, Tallon positioning |

---

## Fergul the Protector

Setup command: `Set up for Fergul`

### Overview

A fight where players must keep moving to prevent Dust Build-up stacks from reducing their effectiveness.

### What the Module Does

**Constant Movement:**

- Every second, the module moves each character to whichever of two camp positions is farther from their current location
- This creates continuous ping-pong movement between two spots, preventing dust buildup

### Player Notes

- Cast while moving is active for this fight
- Fighters and non-fighters each have their own pair of positions

---

## Durtung the Arm of War

Setup command: `Set up for Durtung`

Color commands (used when the colored circle appears):

- `Set up for Durtung black` -- everyone runs to the portal
- `Set up for Durtung yellow` -- scouts run to the portal
- `Set up for Durtung green` -- healers/priests run to the portal
- `Set up for Durtung blue` -- mages run to the portal
- `Set up for Durtung red` -- fighters run to the portal

### Overview

A fight where colored circles appear and specific archetypes must move to them.

### What the Module Does

**Color Circle Mechanic:**

- When a colored circle spawns, jousts everyone out and displays a 45-second HUD countdown
- When the raid leader identifies the color and issues the matching setup command, the correct archetype moves to the portal while everyone else moves to the opposite side

**Add Tracking:**

- Logs Weapon of War add spawns with Durtung's current health

### Player Notes

- The raid leader must identify the circle color and issue the corresponding command
- Two sets of positions are available (one for each side of the encounter)

---

## Sanctifier Goortuk

Setup is automatic when engaged.

### Overview

A fight with heat signature mechanics requiring Shift Vision from illusionists.

### What the Module Does

**Shift Vision:**

- When heat signatures need to be found, automatically casts Shift Vision on illusionists
- Broadcasts Shift Vision cast requests across all sessions when smoke is detected

**Flame of War Waypoints:**

- When a Flame of War spawns, illusionists broadcast a waypoint for the raid
- When the flame despawns, cancels and re-casts Shift Vision

### Player Notes

- Cast while moving is active for this fight
- Illusionists are critical for the heat signature detection

---

## The Weapon of War

Setup is automatic when engaged.

### Overview

A complex fight with auto-dispelling, tank management during Mark of Tactics, and automatic repositioning based on Tallon Zek's location.

### What the Module Does

**Auto Dispelling:**

- Mages and Druids auto-dispel a buff from The Weapon of War

**Mark of Tactics (Fighters):**

- When a fighter gets Mark of Tactics, they cast Recapture and stop offensive actions
- When the mark fades, offensive actions resume

**Tallon Zek Positioning:**

- When Tallon Zek spawns at one of 6 known locations, the raid camp spot is automatically moved to the corresponding opposite-side position
- HUD shows countdown to the next Tallon move (28 seconds)

**Push/Knockback Handling:**

- HUD shows countdown to next knockback (40 seconds)
- Fighters move to the center of the room before the knockback hits, then return to position

### Player Notes

- HUD timers track Tallon Zek moves, knockbacks, and curse timings
