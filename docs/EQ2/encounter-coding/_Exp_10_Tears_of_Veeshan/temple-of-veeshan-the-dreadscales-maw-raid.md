# Temple of Veeshan: The Dreadscale's Maw [Raid]

**Expansion:** Tears of Veeshan (Exp 10)

This zone has 5 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Cer'matal the Gatekeeper](#cermatal-the-gatekeeper) | Lockdown joust, machine tracking, barrage timer |
| [Lord Feshlak](#lord-feshlak) | Melting soles mechanic, super-heated curse handling |
| [Lord Kreizenn](#lord-kreizenn) | Chromatic storm type tracking, add timers |
| [Irdul of the Glacier](#irdul-of-the-glacier) | Corner positioning, ice block mechanic, barrage/rain timers |
| [Telkorenar](#telkorenar) | Power bomb joust, priestly destructor add targeting |

---

## Cer'matal the Gatekeeper

Setup command: `Set up for Cermatal`

### Overview

A fight with a lockdown mechanic, machine state tracking, and barrage timing.

### What the Module Does

**Lockdown Joust:**

- Monitors the Lockdown detriment on raid groups 1 and 2
- When lockdown duration exceeds 8 seconds, jousts to a separate spot
- Returns when the detriment clears

**Machine Tracking:**

- Tracks machine energize/de-energize events for three locations (Center, NE, NW) with HUD status

**Barrage Timer:**

- Awakened Barrage dual timer (50/110 seconds)

### Player Notes

- Only raid groups 1 and 2 are affected by the lockdown joust

---

## Lord Feshlak

Setup command: `Set up for Lord Feshlak`

### Overview

A complex fight with melting soles positioning and super-heated curse handling.

### What the Module Does

**Melting Soles Mechanic:**

- Monitors the Melting Soles detriment
- Uses Fire Resistant Coating item if available
- Assigns the 3 players who get Melting Soles to different joust locations with staggered distances
- Waits for the super-heated pool to spawn before returning

**Super-Heated Curse:**

- Fighters announce when cursed, joust to a curse spot, and request cure curse in raid chat
- Priests self-cure when affected

### Player Notes

- The melting soles mechanic tracks 3 players simultaneously with different positions

---

## Lord Kreizenn

Setup is automatic when engaged.

### Overview

A fight with chromatic storm type changes and add management.

### What the Module Does

**Storm Type Tracking:**

- Monitors storm type changes via red text
- HUD shows current damage type and which add to kill

**Add Timers:**

- Super-Charged Storm Lord spawn timer (77 seconds)
- Super-Charged Flame Lord spawn timer (77 seconds)
- "Eaten" timer (55 seconds)

### Player Notes

- HUD helps identify which add to prioritize based on storm type

---

## Irdul of the Glacier

Setup command: `Set up for Irdul`

Additional command: `Set up for UpdateIrdul` (triggers ice positioning)

### Overview

A fight with corner positioning, ice block mechanics, and multiple timers.

### What the Module Does

**Corner Positioning:**

- 4 corner positions (NW, NE, SW, SE) plus a center raid spot
- When a player is frozen in a block of ice, moves the raid to the closest corner

**HUD Timers:**

- Icy Barrage countdown (55 seconds)
- Freezing Rain AE dual timer (30/45 seconds)
- Ice block explosion countdown (60 seconds)

### Player Notes

- The ice block mechanic triggers automatic corner repositioning

---

## Telkorenar

Setup command: `Set up for Telkorenar`

### Overview

A fight with power bomb jousting and priestly destructor add targeting.

### What the Module Does

**Power Bomb Joust:**

- Monitors the Power Bomb detriment
- When detected, jousts to the joust spot and announces

**Priestly Destructor Targeting:**

- When a Priestly Destructor targets a player, that player moves to the add spot with TempAssist enabled
- When the assigned add despawns, returns to the raid spot

### Player Notes

- DPS assignment is tracked when weaknesses are detected
