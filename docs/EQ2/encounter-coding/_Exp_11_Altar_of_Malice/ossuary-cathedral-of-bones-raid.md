# Ossuary: Cathedral of Bones [Raid]

**Expansion:** Altar of Malice (Exp 11)

This zone has 5 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Inquisitor Soronigus](#inquisitor-soronigus) | Cure curse coordination |
| [Virtuoso Edgar V'Zann](#virtuoso-edgar-vzann) | Pipe organ playing, chord joust, enchanter auto-dispel |
| [Sacrificer Aevila D'Serin](#sacrificer-aevila-dserin) | Blood pool mechanic, enchanter auto-dispel |
| [Protector of Bones](#protector-of-bones) | No automation needed |
| [Primordial Ritualist Villandre V'Zher](#primordial-ritualist-villandre-vzher) | Mage auto-dispel, pet management, add timers |

---

## Inquisitor Soronigus

Setup is automatic when engaged.

### Overview

A fight with a curse mechanic requiring coordinated cure timing.

### What the Module Does

**Cure Curse Coordination:**

- Disables normal curse curing
- Monitors the Palpitation curse duration
- When duration drops below 10 seconds, calls out for cure curse coordination via uplink

### Player Notes

- Normal cure curse is disabled to prevent wasting cures at the wrong time

---

## Virtuoso Edgar V'Zann

Setup command: `Set up for Edgar`

### Overview

A complex fight centered around a pipe organ mechanic where bards play counter-melodies, with jousting for uncurable chords and enchanter dispelling.

### What the Module Does

**Pipe Organ Playing:**

- When the boss calls out a song type (Water, Ice, or Flame), bards are assigned turns based on raid ID ordering
- Each bard navigates to the correct pipe organ key and plays the counter-melody
- Bards are staggered across turns to ensure continuous coverage

**Malicious Chord Joust:**

- When two players receive the uncurable chord curse, they joust to opposite spots based on actor ID comparison (lower ID goes to one spot, higher to the other)

**Enchanter Auto-Dispel:**

- Enchanters automatically dispel the boss's protective buff when detected

**Pipe Organ Cleaner:**

- When a Pipe Organ Cleaner add spawns, the bard whose turn it is targets and kills it

**HUD Timers:**

- Reflect timer (40 seconds)
- Health percentage thresholds for the next piano lesson (90/75/60/45/30/15%)

### Player Notes

- Multiple bards in the raid are needed for the organ mechanic

---

## Sacrificer Aevila D'Serin

Setup command: `Set up for Sacrificer`

### Overview

A fight with a blood pool mechanic where cursed players must run through specific waypoints to cleanse.

### What the Module Does

**Blood Pool Mechanic:**

- When a player receives the Sanguine Splash curse, they automatically run through a series of waypoints: general area, blood pool, clear room, and back to position
- The module determines left/right side based on proximity
- Fighters turn off autoattack and guardians cast Recapture while running
- Sprint is cast for movement speed during the run

**Enchanter Auto-Dispel:**

- Enchanters automatically dispel the Sacrificer's buff when detected

**HUD Timer:**

- Next splash timer (90-second countdown)

### Player Notes

- The blood pool run is fully automated once the curse is detected

---

## Protector of Bones

!!! warning "Work in Progress"
    This encounter module is a stub with no active automation. The ListSetups message says: "Make a good auto target list. No code required."

Setup is automatic when engaged.

### Overview

A fight where two bosses must be kept within 3% HP of each other, with adds that must be killed in the middle area.

### What the Module Does

No active automation -- this encounter relies on manual play and auto-target list configuration.

### Player Notes

- Keep the two bosses within 3% HP of each other
- Get adds (coagulated gore, Cruor of Vitae, Extinguisher of Life) to the middle
- Only kill adds in the middle area

---

## Primordial Ritualist Villandre V'Zher

Setup is automatic when engaged.

### Overview

A fight with add management, pet control, and mage dispelling.

### What the Module Does

**Mage Auto-Dispel:**

- Mages automatically dispel Villandre's Blood Lust buff using Absorb Magic

**Pet Management:**

- When a Bone Breaker add spawns, automatically sends special pets (mound of broken bones) to attack it

**HUD Timers:**

- Bone Breaker spawn timer (147 seconds)
- Bloody Corpse spawn timer (147 seconds)
- Marrow Sapper spawn timer (147 seconds)
- Malicious Pulse stun timer (53 seconds)
- Touch of Malign timer (45 seconds)

### Player Notes

- Multiple add wave timers help track the fight's progression
