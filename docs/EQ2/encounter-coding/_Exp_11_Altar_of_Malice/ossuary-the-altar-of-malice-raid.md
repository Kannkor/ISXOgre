# Ossuary: The Altar of Malice [Raid]

**Expansion:** Altar of Malice (Exp 11)

This zone has 3 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Ritual Keeper V'derin](#ritual-keeper-vderin) | Rain of malice timers, sentry tracking, defensive auto-casting |
| [Tserrina Syl'tor](#tserrina-syltor) | Brazier charm mechanic, shadowbeast handling |
| [The Construct of Malice](#the-construct-of-malice) | Touch mechanics, shockwave handling, spread positioning, curse pairing |

---

## Ritual Keeper V'derin

Setup is automatic when engaged.

### Overview

A fight with rain of malice phases, sentry add tracking, and timed defensive ability usage.

### What the Module Does

**Rain of Malice Timers:**

- HUD timers for Rain of Malice I/II/III phases (58-65 second timers)
- HUD timer for Malicious Barrage (42 seconds)

**Defensive Auto-Casting:**

- On Rain of Malice I, automatically queues defensive abilities (Champion's Interception, Stone Cold, Redirection, Divine Guidance, Equilibrium) with appropriate timing

**Sentry Tracking:**

- When a Malicious Sentry spawns, casts Hawk Attack and shows HUD for next sentry spawn percentage (95/85/75/65/55/45/35/25/15/5%)
- Add shuffle timer (31/62 seconds)

### Player Notes

- Adds spawn approximately every 10% HP
- The boss goes immune while adds are alive
- The furthest person gets an uncurable curse and must run to the boss

---

## Tserrina Syl'tor

Setup is automatic when engaged.

### Overview

A fight with a shadowbeast charm mechanic where a troubador charms a pet to destroy braziers.

### What the Module Does

**Brazier Charm Mechanic:**

- When a summoned shadowbeast spawns, a designated Troubador in raid group 4 auto-charms it using Bria's Entrancing Sonnet
- The charmed pet is then sent to attack the shadowy brazier
- Includes charm retry and error handling logic

**HUD Timers:**

- Brazier spawn timer (60 seconds)
- Echo of Shadows timer (105 seconds)
- Alert when Shadowy Cultist spawns

### Player Notes

- A Troubador in raid group 4 is needed for the charm automation
- Coercers can also charm using their Charm ability

---

## The Construct of Malice

Setup command: `Set up for Construct`

Additional commands: `Set up for Test` (spread), `Set up for Reset` (reset positions), `Set up for Curse` (curse movement)

### Overview

An extremely complex fight with colored touch mechanics, shockwave phases, spread positioning, curse pairing, and timed defensive cooldowns.

### What the Module Does

**Touch Mechanics:**

- Tracks three colored detriments: Green (Noxious Binding), Blue (Touch of Malice), Red (Touch of Spite)
- Automatically moves players to the correct bubble position based on their detriment color
- Green-tagged players use ID comparison to determine positioning

**Curse Pairing:**

- Malaise and Spitefulness curses trigger campspot shifts and callout announcements
- Delayed cure curse checks after 8 seconds if still cursed

**Spread Positioning:**

- On Spiteful Shockwave I, the raid spreads into per-group positions
- Each raid group (1-4) has its own set of 8 positions with priests prioritized first

**DPS Toggle:**

- "Godly protection" disables named combat art casting
- "Zapped" re-enables casting with a 35-second HUD timer for next immunity

**Defensive Cooldowns:**

- Shockwave III: auto-casts Tortoise Shell and Divine Guidance with timed cancellation
- Shockwave V: casts Equilibrium and cancels Tortoise Shell after 10 seconds
- Powerful Malicious Strike: auto-queues Paladin Faith and Guardian Tower of Stone with timing

**HUD Timers:**

- Malicious Barrage (30-45 seconds)
- Shockwave (80 seconds)
- Named immunity (35 seconds)
- Powerful Malicious Strike (80 seconds)
- Bubble phase (80 seconds)

### Player Notes

- This is one of the most complex encounter modules in the expansion
- Multiple defensive ability rotations are automated
