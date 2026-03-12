# Maldura: Forge of Ashes [Raid]

**Expansion:** Terrors of Thalumbra (Exp 12)

This zone has 4 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Cronnin the Axe / Dellmun the Hammer](#cronnin-the-axe--dellmun-the-hammer) | Enchanter auto-dispelling for stack reduction |
| [Kiernun the Lyrical](#kiernun-the-lyrical) | Lyrical Protection buff cycling, bard bubble casting |
| [Captain Ashenfell / Captain Graybeard](#captain-ashenfell--captain-graybeard) | Light curse auto-movement, sureshot intercept, cure toggle |
| [Kyrus of the Old Ways](#kyrus-of-the-old-ways) | Gaze joust, enrage auto-dispell, evade teleport recovery |

---

## Cronnin the Axe / Dellmun the Hammer

Setup is automatic when engaged.

### Overview

A fight where enchanters auto-dispel buffs from the bosses to reduce their stacks.

### What the Module Does

**Auto Dispelling (Enchanters Only):**

- Checks both Cronnin the Axe and Dellmun the Hammer for dispellable buffs
- Enchanters automatically dispel the buff when detected

### Player Notes

- Only Enchanter classes perform the dispelling

---

## Kiernun the Lyrical

Setup command: `Set up for Lyrical` (also accepts `Set up for Kiernun`)

Use `Set up for START` to begin the buff cycling rotation.

### Overview

A complex fight centered around maintaining the Lyrical Protection buff by cycling through orb spots.

### What the Module Does

**Buff Cycling:**

- `Set up for START` initiates a staggered rotation where each player runs to their group's orb to pick up the Lyrical Protection buff
- Players are staggered by 5-second intervals based on their sort order

**Bard Bubble Casting:**

- Bards monitor their Lyrical Protection ability cooldown
- When ready, they automatically move to the orb, cast the ability, and return

**Auto Buff Refresh:**

- All non-bard characters monitor their buff duration
- When the buff fades, they automatically move to the orb, wait for the buff, and return

**Scream HUD:**

- Displays health percentage thresholds for the next scream at 85/65/45/25/10%

### Player Notes

- Each raid group has its own orb spot
- Use `Set up for START` to begin the cycling after initial positioning

---

## Captain Ashenfell / Captain Graybeard

Setup command: `Set up for Ashenfell` (also accepts `Set up for Graybeard` or `Set up for Captain`)

### Overview

A fight with colored light curses, sureshot intercepts, and dynamic positioning based on which captain you engage.

### What the Module Does

**Dynamic Side Selection:**

- Automatically detects which side of the room you are on and sets positions accordingly (Ashenfell or Graybeard mirrored positions)

**Overwhelming Light Auto-Movement:**

- Golden Light curse: moves to the yellow portal, announces "yellow"
- Azure Light curse: moves to the blue portal, casts Tower of Stone, announces "blue"
- When curses clear, returns to the original camp position

**Touch of Maldura Auto-Targeting:**

- Non-fighters with the Touch of Maldura detriment automatically target the Sureshot add

**Sureshot Intercept:**

- When Sureshot targets a player, broadcasts an intercept request to group 1 fighters
- HUD timers show intercept countdown

**Cure Toggle:**

- When a Sureshot spawns, priest cure curse is disabled to prevent wasting cures
- When the Sureshot dies, cure curse is re-enabled

### Player Notes

- Raid groups 1-2 and priests/enchanters go to the main raid spot
- Raid groups 3-4 (non-priest/enchanter) go to a separate curse spot

---

## Kyrus of the Old Ways

Setup is automatic when engaged.

### Overview

A fight with gaze jousting, enrage/reflect dispelling, and teleport recovery mechanics.

### What the Module Does

**Gaze Joust:**

- Phase 1 ("focuses his gaze"): the targeted player moves away from the raid, fighters cast Recapture
- Phase 2 ("again focuses his gaze"): the targeted player returns to the group
- Phase 3 ("turns his gaze back"): gaze mechanic ends
- HUD timers show countdown between gaze phases (~90 seconds between cycles)

**Enrage/Reflect Dispelling:**

- When Kyrus enrages and reflects spells, all characters stop offensive actions
- Enchanters auto-dispel the reflect buff
- Offense resumes once dispelled (or after a 15-second failsafe)

**Evade Teleport Recovery:**

- When a player is teleported away ("will not evade me"), the module pauses OgreBot, navigates back to the fight, clicks the soulshard, and resumes

### Player Notes

- HUD displays show predicted health thresholds for the next evade (75%/25%) and dispell phases
