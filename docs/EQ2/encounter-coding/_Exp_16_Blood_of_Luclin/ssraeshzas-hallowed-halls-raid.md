# Ssraeshza's Hallowed Halls [Raid]

**Expansion:** Blood of Luclin (Exp 16)

This zone has 4 boss encounters with OgreBot automation modules.

## Available Setups

| Boss | Description |
|------|-------------|
| [Kua, Watcher of Wanes](#kua-watcher-of-wanes) | Automatic tank self-targeting for Stone Gaze with HUD timer |
| [Vyzh'dra the Unleashed](#vyzbdra-the-unleashed) | Sparkle grabbing, detriment handling, and add intercept |
| [Zeltheen of the Fang / R'thessil of the Fang](#zeltheen-of-the-fang--rthessil-of-the-fang) | Non-fighter jousting during Sustainment casts |
| [Remnant Ferahhal](#remnant-ferahhal) | Forced Silence detection and action pausing |

---

## Kua, Watcher of Wanes

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter where Stone Gaze targets a fighter, and that fighter must target themselves to prevent the named from healing off the mechanic. The module manages tank self-targeting and tracks cooldown timers so other fighters know when to retake aggro.

### What the Module Does

**Stone Gaze Self-Targeting:**

- When Stone Gaze targets a fighter, that fighter automatically targets themselves for 60 seconds
- This prevents the named from healing off the Stone Gaze mechanic
- When the 60-second timer expires, the fighter retargets the named

**HUD Timer:**

- A HUD timer is displayed showing which fighter cannot tank and for how long
- Other fighters can see the timer and know when to pick up tanking duties

### Player Notes

- Fighters affected by Stone Gaze will automatically self-target for 60 seconds.
- The HUD timer shows who is unable to tank and the remaining duration.
- Other fighters should be ready to maintain aggro while a tank is self-targeting.

---

## Vyzh'dra the Unleashed

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A multi-mechanic encounter involving sparkle collection from the named, a self-targeting detriment, and an add that must be intercepted. The module handles all three mechanics automatically.

### What the Module Does

**Sparkle Handling:**

- Announces in chat who is eligible to grab sparkles
- When the sparkle message appears, automatically grabs the sparkling object from the named

**Falsified Targeting:**

- When the Falsified Targeting detriment is detected, the affected player automatically targets themselves until the detriment fades

**Incendiary Spark Hoarder Add:**

- Displays a HUD showing who the Incendiary Spark Hoarder is targeting
- If the hoarder is targeting you, automatically moves to intercept it

### Player Notes

- Sparkle grabbing is automatic when you are eligible.
- If you get Falsified Targeting, you will self-target until it fades -- do not manually change targets.
- Watch the HUD for the Incendiary Spark Hoarder's target. If it is targeting you, the module moves you to intercept.

---

## Zeltheen of the Fang / R'thessil of the Fang

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A dual-named encounter where one of the named casts Sustainment, which non-fighters must avoid by jousting away. Staying near the named during the cast feeds it, so distance is critical.

### What the Module Does

**Sustainment Jousting:**

- When one of the named starts casting Sustainment, non-fighters automatically joust away to avoid feeding the named
- Once the Sustainment cast ends, non-fighters return to their normal positions
- Fighters remain in position throughout

### Player Notes

- Non-fighters will be moved away automatically during Sustainment casts.
- Fighters stay in place and continue tanking.
- Do not manually run back to position during the cast -- the module returns you when it is safe.

---

## Remnant Ferahhal

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

An encounter with the Forced Silence mechanic that requires all players to stop casting and acting for a period of time.

### What the Module Does

**Forced Silence:**

- When the warning announcement appears, the module immediately cancels the current spell cast
- All actions are paused until the Forced Silence detriment fades
- Once the detriment clears, normal actions resume automatically

### Player Notes

- When Forced Silence is announced, all casting and actions stop immediately.
- Do not attempt to manually cast during Forced Silence -- the module will resume actions once it is safe.
