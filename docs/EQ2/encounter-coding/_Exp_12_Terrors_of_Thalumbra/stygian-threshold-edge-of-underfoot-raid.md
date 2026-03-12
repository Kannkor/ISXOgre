# Stygian Threshold: Edge of Underfoot [Raid]

**Expansion:** Terrors of Thalumbra (Exp 12)

This zone has 4 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Crohp the Mighty](#crohp-the-mighty) | Auto joust on siphon, sprint at high stacks, HUD timer |
| [King Lockt](#king-lockt) | Exile joust |
| [Jorik the Scourge](#jorik-the-scourge) | Cocoon auto-cure via kobold torch |
| [Iron Forged Constructs](#iron-forged-constructs) | Energized beam auto-clicking, protection check |

---

## Crohp the Mighty

Setup command: `Set up for Crohp` (also accepts `Set up for Mighty`)

Additional option: `Set up for Auto Crohp` for full auto mode with targeting.

### Overview

A fight with periodic jousting when the boss siphons power from the earth.

### What the Module Does

**Auto Joust:**

- When Crohp siphons power, jousts the raid out and moves to whichever of two positions is farther from the boss
- Jousts back in after 14 seconds
- At high detriment stacks (over 1000), casts Sprint for extra movement speed
- HUD countdown shows time until next joust (~51 seconds)

### Player Notes

- Fighters have separate tank spots at each position
- In auto mode, targeting is briefly paused during joust transitions

---

## King Lockt

Setup is automatic when engaged.

### Overview

A fight where a specific player is exiled and must move away from the group.

### What the Module Does

**Exile Joust:**

- When King Lockt exiles a player, all characters joust out
- The exiled player gets an additional positional offset to move further away
- After 12-13 seconds, everyone returns to their positions

### Player Notes

- The exiled player is automatically moved further from the group than other characters

---

## Jorik the Scourge

Setup command: `Set up for Jorik`

### Overview

A fight with a cocoon mechanic where wrapped players must be freed using a Kobold Torch.

### What the Module Does

**Cocoon Auto-Cure:**

- When a player is wrapped in a cocoon, the module automatically uses "A Kobold Torch" on the cocooned player
- Bards have priority for using the torch (if the cocooned player is in their group)
- Otherwise, any character with the torch item uses it

### Player Notes

- You must have "A Kobold Torch" in your inventory
- Fighters have 4 separate tank spots (one per raid group)

---

## Iron Forged Constructs

Setup command: `Set up for Iron`

### Overview

A fight involving Skottun and Dhael where energized players must click beams, and the raid must reposition based on protection status.

### What the Module Does

**Energized Beam Clicking:**

- When a non-fighter becomes energized, they automatically navigate to the beam and click it repeatedly for up to 50 seconds
- Returns to the raid spot when the protection is removed or the timer expires
- Uses Sprint for faster movement

**Protection Check:**

- The raid leader checks whether Skottun or Dhael has the Enriched Blood detriment and announces which construct needs to be moved to the middle

### Player Notes

- Fighters are excluded from the beam clicking mechanic
- The module uses OgreCraftMove for navigation
