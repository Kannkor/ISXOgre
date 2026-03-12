# Dragon Necropolis: Disturbed Vaults [Raid]

**Expansion:** Scars of Destruction (Exp 21)

This raid zone features Lady Karkona, Lord Ulvaxazoviak, and a challenge mode where both are fought simultaneously.

## Available Setups

| Boss | Description |
|------|-------------|
| [Lady Karkona](#lady-karkona) | Jousting and tank swapping |
| [Lord Ulvaxazoviak](#lord-ulvaxazoviak) | Jousting and tank swapping. YOU need to get an add and remove the protections of the adds |
| [Challenge Mode](#challenge-mode) | Both bosses simultaneously |

---

## Lady Karkona

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a joust-then-cure mechanic for Spiritual Release and a tank swap via Lady's Remembrance. The named also has an inhale mechanic that can be interrupted with a special item.

### What the Module Does

**Spiritual Release (Joust-Then-Cure):**

- Detects Spiritual Release detriment on the player
- Automatically jousts to one of several safe positions around the named
- Requests a cure once at the safe position

**Lady's Remembrance (Tank Swap):**

- Detects Lady's Remembrance on the tank
- Stops all offensive actions
- Activates Subtle Strikes and disables threat-generating abilities
- Adds the affected fighter to the threat ignore list
- Once the detriment fades, resets all threat settings and resumes DPS

**Inhale Mechanic:**

- If the player has the special item (Transient Phantasmagnetic Disturbance Mechanisms), enables NPC cast monitoring
- When the named begins to inhale, uses the item to interrupt
- On-screen timer tracks the next inhale

**Cure Management:**

- Priest cure curse is disabled during the fight (cures are handled through the joust-then-cure system)

### Player Notes

- The Transient Phantasmagnetic Disturbance Mechanisms item is needed for the inhale interrupt
- Tank swap is handled automatically -- the off-tank will pick up aggro when the main tank goes into Subtle Strikes

---

## Lord Ulvaxazoviak

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with Draconic Release requiring joust-then-cure, Lord's Remembrance tank swap, and a Skulking Festerwound mechanic requiring interaction with chetari skulkers.

### What the Module Does

**Draconic Release (Joust-Then-Cure):**

- Detects Draconic Release detriment on the player
- Automatically jousts to safe positions around the named
- Requests a cure once at a safe position
- On-screen timer (60 seconds) tracks the next purge

**Lord's Remembrance (Tank Swap):**

- Detects Lord's Remembrance on the tank
- Stops all offensive actions, activates Subtle Strikes, disables threat-generating abilities
- Adds the affected fighter to the threat ignore list
- Resets all threat settings once the detriment fades

**Skulking Festerwound:**

- Detects Skulking Festerwound curse on the player
- Finds a nearby chetari skulker add that has an active target
- Moves the player to within range of the skulker to remove the curse
- Uses TTS alert to announce who has the curse
- After reaching the skulker, requests a cure

### Player Notes

- YOU need to handle getting adds and removing their protections manually
- The Skulking Festerwound mechanic requires a chetari skulker to be active and in range
- The configurable skulker search distance defaults to 60 meters

---

## Challenge Mode

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

Challenge mode fights both Lady Karkona and Lord Ulvaxazoviak simultaneously, combining mechanics from both encounters with additional item coordination.

### What the Module Does

**Positioning:**

- Automatically determines whether the player is closer to Lady or Lord and positions accordingly
- Players can also be manually assigned to Lady's spot or Lord's spot via configuration

**Both Boss Mechanics:**

- Handles both Lady's and Lord's joust-then-cure mechanics independently
- Handles both Lady's and Lord's Remembrance tank swaps independently
- Each boss has its own on-screen purge timer

**Skulking Festerwound:**

- Same as Lord's solo encounter -- detects the curse, moves to a skulker, and requests cure

**Item Coordination (Inhale Interrupt):**

- Players with the special item register themselves for the inhale interrupt rotation
- The module rotates through registered players so each person takes a turn using the item
- Players who run out of items are automatically removed from the rotation
- If a player is "glared at" by the boss (indicating the item caused problems), they are removed from the rotation

**Guardian Recapture:**

- Disabled during the fight to prevent aggro issues

### Player Notes

- Challenge mode requires strong coordination between the two groups
- Item rotation for the inhale interrupt is handled automatically
- Players need the Transient Phantasmagnetic Disturbance Mechanisms item for the inhale interrupt
- Fighters should be aware that encounter-wide nukes are dynamically ignored
