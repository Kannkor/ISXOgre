# Kralet Penumbra: The Master's Chosen [Heroic]

**Expansion:** Terrors of Thalumbra (Exp 12)

This zone has 3 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Golguth](#golguth) | Dual curse jousting (far vs close) |
| [Servitor of Yothshaval](#servitor-of-yothshaval) | Auto-target tutors, group cure calling |
| [Yothshaval, Acolyte of Penumbra](#yothshaval-acolyte-of-penumbra) | Power drain assist via Sprint cycling |

---

## Golguth

Setup command: `Set up for Golguth`

### Overview

A fight with two different curses that require opposite positioning -- one makes you move away, the other makes you move close.

### What the Module Does

**Dual Curse Jousting:**

- Yothshaval Curse ("be far"): moves to the joust spot away from the boss
- The Chosen Curse ("be close"): moves to the raid spot near the boss, or to the boss itself if the raid spot is too far
- When both curses clear, returns to the normal raid position

### Player Notes

- Only one curse is active at a time

---

## Servitor of Yothshaval

Setup command: `Set up for Servitor`

### Overview

A fight with add targeting and group cure coordination.

### What the Module Does

**Auto-Targeting:**

- When you do NOT have the Servitude detriment, automatically targets the highest-HP "a Serving tutor" mob
- When you DO have the detriment, switches target to Servitor of Yothshaval

**Group Cure Calling:**

- When the Servitude detriment duration drops below 10 seconds, calls for a priest group cure

**Setup Actions:**

- Disables cure cast stack, enables dynamic ignore PBAoE and encounter nukes
- Non-fighters cast Singular Focus
- Templars have Mana Cure disabled

**Cleanup on Kill:**

- All modified options are reverted when the Servitor dies

### Player Notes

- You may wish to reload OgreBot when you are done with this fight, as it modifies and attempts to reset options (may not be perfect)
- Portal mechanic: campspot and stand within 27 meters of the portal you want to go through, then press `Special_ZoneSpecific` in MCP

---

## Yothshaval, Acolyte of Penumbra

Setup is automatic when engaged.

### Overview

A fight with a power drain mechanic where Sprint is used to rapidly burn power.

### What the Module Does

**Power Drain Assist:**

- When power is above 30% and Sprint is ready, automatically casts and immediately cancels Sprint to rapidly deplete power
- Stops cycling Sprint once power drops below 30%

### Player Notes

- This mechanic helps with the fight's power-drain requirement
