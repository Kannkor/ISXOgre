# Ssraeshza Temple: Echoes of Time [Raid]

**Expansion:** Altar of Malice (Exp 11)

This zone has 3 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Farozth Ssravizh](#farozth-ssravizh) | Hiss tracking, vengeance joust, cure management |
| [Ka'Rah Ferun](#karah-ferun) | Shadowy figure portal mechanic, stealth navigation |
| [Arch Lich Rhag'Zadune](#arch-lich-rhagzadune) | Totem running mechanic, mark assignments |

---

## Farozth Ssravizh

Setup is automatic when engaged.

### Overview

A fight with hiss targeting, scaled vengeance jousting, and coordinated curse curing.

### What the Module Does

**Hiss Tracking:**

- Parses the hiss target name and shows HUD timer for hiss duration (30 seconds) and next hiss (60 seconds)

**Scaled Vengeance Joust:**

- On vengeance announcement, shows HUD timer (60 seconds) and triggers a joust out
- Priests check if the vengeance target is in their group for prioritized curing

**Cure Management:**

- Self-curse detection triggers group say and timed raid announcement for cure coordination

**HUD Timer:**

- Ancient Devastation timer (18/24 seconds) shared across all bosses in the zone

### Player Notes

- Cure timing is coordinated between priests based on group membership

---

## Ka'Rah Ferun

Setup command: `Set up for Ferun`

### Overview

A fight with a shadowy figure portal mechanic where a player must navigate to the correct portal, stealth to an upper level, and kill a Disciple.

### What the Module Does

**Shadowy Figure Portal Mechanic:**

- When a player is called to handle the shadowy figure, automatically navigates to the correct portal (East, South, or West)
- Clicks up to the upper level
- Casts class-appropriate stealth (Predator: Stealth, Rogue: Sneak, Beastlord: Spiritshroud)
- Moves to the Disciple of Luclin and auto-targets it

**Portal Identification:**

- Three portal locations are dynamically matched to three Disciple spawn locations

**HUD:**

- Shows who can see the Shadowy Figure (30-second timer)

### Player Notes

- The portal mechanic is fully automated for scout classes with stealth abilities

---

## Arch Lich Rhag'Zadune

Setup command: `Set up for Lich` (also accepts pre-pull: `Set up for Totem`)

### Overview

A fight with a totem running mechanic where players with specific marks must sprint to their class-appropriate totem.

### What the Module Does

**Totem Running:**

- When a player receives Mark of Strength/Intelligence/Agility/Wisdom, they automatically sprint to their class-specific totem location
- Each archetype has a different totem and run path with 2 waypoints
- After clicking the totem, the player returns to position
- Bards and Enchanters are excluded from running (they stay on the boss and cast Quick Tempo)

**Pre-Pull Positioning:**

- `Set up for Totem` spreads non-bard/non-enchanter classes to their pre-pull positions near their respective totems

**HUD:**

- Shows mark assignments (who got which mark)
- Next totem clickie percentage thresholds (75/50/25/10%)
- Fighter-specific timeout warnings

### Player Notes

- Bards and Enchanters stay on the boss during the totem phase
- Use `Set up for Totem` for pre-pull positioning near totems, then `Set up for Lich` to move to center
