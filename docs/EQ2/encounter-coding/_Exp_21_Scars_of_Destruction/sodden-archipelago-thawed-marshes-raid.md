# Sodden Archipelago: Thawed Marshes [Raid]

**Expansion:** Scars of Destruction (Exp 21)

> **:warning: Work In Progress**
>
> This zone's automation is still under development. Some mechanics may not be fully automated yet.

This raid zone contains 8 boss encounters.

## Available Setups

| Boss | Description |
|------|-------------|
| [Vitoth of the Gnarled Roots](#vitoth-of-the-gnarled-roots) | Joust to arcane/elemental areas based on curse type |
| [Grand Shaman Grungizt](#grand-shaman-grungizt) | Joust-then-cure and AoE circle jousting |
| [Chieftain Maferi](#chieftain-maferi) | Joust and totem interaction |
| [Bucko, Loyal Pet to Maferi](#bucko-loyal-pet-to-maferi) | Tank swap and joust-then-cure |
| [Sommumun the Frenzied](#sommumun-the-frenzied) | Scout stealth mechanic |
| [Joggu the Steadfast](#joggu-the-steadfast) | Joust from named on emote |
| [Monuseru, Titan of the Depths](#monuseru-titan-of-the-depths) | Circular position rotation |
| [Barlsbit the Scavenger](#barlsbit-the-scavenger) | Priest cure curse with archetype priority |

---

## Vitoth of the Gnarled Roots

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with two curse types that each require jousting to a different element area.

### What the Module Does

**Mindwrithe:**

- Detects the Mindwrithe curse on the player
- Jousts to the arcane (dark fire) area to handle the curse

**Flamewrithe:**

- Detects the Flamewrithe curse on the player
- Jousts to the elemental (blue fire) area to handle the curse

**Add Targeting:**

- Auto-targets Fireant Mound adds (reducing the named's damage taken)

### Player Notes

- Each curse type requires jousting to the correct area -- the module handles this automatically
- Killing Fireant Mound adds helps reduce the named's damage resistance

---

## Grand Shaman Grungizt

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a joust-then-cure mechanic for Aftershock Release, a purge arcane phase that disables cures, and AoE circle jousting.

### What the Module Does

**Aftershock Release (Joust-Then-Cure):**

- Detects Aftershock Release detriment on the player
- Jousts away from the named to a safe position
- Requests a cure once at the safe position

**Purge Arcane:**

- During the purge arcane phase, cures are temporarily disabled
- Re-enabled after the phase ends

**AoE Circle Jousting:**

- Detects red ring AoE circles on the ground
- Jousts the group away from these circles to avoid damage

**Add Targeting:**

- Auto-targets Minimonuseru Titan adds

### Player Notes

- Cures are automatically disabled during the purge arcane phase -- don't panic when cures aren't landing
- Watch for AoE circles on the ground

---

## Chieftain Maferi

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a joust mechanic for Monkey Around and a curse requiring interaction with a totem actor.

### What the Module Does

**Monkey Around:**

- Detects the Monkey Around detriment on the player
- Jousts the player to a relative position away from the named

**Curse of the Totem:**

- Detects Curse of the Totem on the player
- Finds the totem actor (shield barrier heal)
- Automatically moves the player to the totem to remove the curse

**Add Targeting:**

- Auto-targets Mandoko Chanter adds

### Player Notes

- The totem must be alive and in range for the curse mechanic to work

---

## Bucko, Loyal Pet to Maferi

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a tank swap via Favored Mark, a joust-then-cure for Aftershock Release, and a dome joust mechanic.

### What the Module Does

**Favored Mark (Tank Swap):**

- Detects Favored Mark via chat message parsing
- Manages threat transfer between tanks

**Aftershock Release (Joust-Then-Cure):**

- Same as Grungizt -- detects the detriment, jousts away, and requests a cure

**Dome Joust:**

- Detects a dome aura spawning during the fight
- Jousts the group inside or away from the dome as needed

**Add Targeting:**

- Auto-targets Shelled Repairer adds

### Player Notes

- Tank swap happens automatically based on chat message detection
- The dome mechanic requires correct positioning relative to the dome

---

## Sommumun the Frenzied

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where scouts must use stealth abilities when they receive Monitored Detection.

### What the Module Does

**Monitored Detection (Scout Stealth):**

- Detects Monitored Detection on the player
- Scouts automatically activate their class-specific stealth ability:
    - Assassin/Ranger: Sneak
    - Swashbuckler/Brigand: Stealth
    - Dirge: Shroud
    - Troubador: Spiritshroud
- The module waits until stealth drops or the curse clears before resuming

### Player Notes

- Only scouts need to worry about this mechanic
- The correct stealth ability is chosen automatically based on your class
- Stay in stealth until the curse clears

---

## Joggu the Steadfast

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A straightforward fight with a Swampquake emote that requires jousting away from the named.

### What the Module Does

**Swampquake:**

- Detects the Swampquake emote
- Jousts the group away from the named
- Pets are pulled back for 13 seconds during the joust
- Pets are re-enabled after the joust

### Player Notes

- Simple joust mechanic -- move away when Swampquake is announced, then return

---

## Monuseru, Titan of the Depths

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A positional fight where the group rotates through 6 positions around the named, advancing to the next position when AoE circles appear.

### What the Module Does

**Circular Position Rotation:**

- Maintains 6 positions around the named in a circular pattern
- When an AoE circle spawns at or near the current position, the group advances to the next position
- The rotation is continuous throughout the fight

**Double Joust:**

- When an AoE circle appears near the tank's position, the module performs a double-joust (joust away then return to the next position)

**Tank Management:**

- The 2nd fighter uses Subtle Strikes for threat management

**Add Targeting:**

- Auto-targets animated droplet adds

### Player Notes

- The group continuously rotates positions -- follow the automated positioning
- The fight requires smooth movement between the 6 spots

---

## Barlsbit the Scavenger

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where priests manage cure curse with a randomized archetype priority system.

### What the Module Does

**Priest Cure Curse Priority:**

- Priests cure curses in a specific archetype order that is partially randomized:
    - First priority group (randomized order): Scouts, Priests, Mages
    - Last priority: Fighters
- The randomization prevents predictable cure patterns

**Priest Offensive Stance:**

- Priests disable offensive abilities while actively curing curses
- Offensive abilities are re-enabled after curing is complete

**Add Targeting:**

- Auto-targets small scavenger adds

### Player Notes

- Cure priority is handled automatically by the module
- Priests should expect their offensive abilities to be toggled on/off during the fight as they handle cures
