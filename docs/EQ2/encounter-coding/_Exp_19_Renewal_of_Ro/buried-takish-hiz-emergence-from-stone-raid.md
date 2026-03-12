# Buried Takish'Hiz: Emergence from Stone [Raid]

**Expansion:** Renewal of Ro (Exp 19)

!!! warning "Work in Progress"
    Automation for this zone is still under development. Some encounters may have limited or incomplete automation.

This raid zone contains 7 boss encounters.

## Available Setups

| Boss | Description |
|------|-------------|
| [Sanum Ordast](#sanum-ordast) | Symbol jousting, Weakened Veil handling, Stone Silent curing, Worshiper targeting |
| [Malachiel Caedor](#malachiel-caedor) | Tyrannical Torturing drake riding, AoE management |
| [Veagth](#veagth) | Corrosion auto-cure via item, polarity announcements |
| [Vischt Stormbones](#vischt-stormbones) | Advantage detriment portal clicking, Summoner repositioning |
| [Stonesong](#stonesong) | AoE pool jousting |
| [The Monument of Stone](#the-monument-of-stone) | Stone Hex curse room navigation |
| [Rugrat the Thief](#rugrat-the-thief) | Room positioning based on text commands |

---

## Sanum Ordast

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A complex multi-mechanic fight involving symbol jousting, curse curing interactions between players, and add management.

### What the Module Does

**Symbol Jousting:**

- When Sanum begins spelling doom, automatically positions to the correct safe spot based on spawned symbol and dial locations
- Returns to camp when the safe location is confirmed

**Weakened Veil:**

- Detects the Weakened Veil detriment on your character
- Automatically moves to and clicks a glowing actor to remove it

**Stone Silent / Malachiel's Touch Interaction:**

- Detects Stone Silent curse and reports it to the raid
- Players who have Malachiel's Touch are automatically moved to cursed players and use "Break Through the Stone Magic!" to cure them

**Crazed Worshiper:**

- Non-fighters automatically target and move to kill the Crazed Worshiper when it becomes vulnerable
- Returns to camp if an Amalgam of Resonance spawns during the worshiper phase

### Player Notes

- Multiple mechanics can overlap — the module prioritizes symbol jousting over other mechanics
- Malachiel's Touch and Stone Silent work together: if you have the Touch, you cure those with Stone Silent
- Stay aware of Amalgam spawns as they interrupt worshiper handling

---

## Malachiel Caedor

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where players afflicted with Tyrannical Torturing must click drakes on cages to fly around and remove the curse.

### What the Module Does

**Tyrannical Torturing:**

- Detects the Tyrannical Torturing detriment when it is applied
- Coordinates with other afflicted players to determine which drake to use
- Automatically moves to and clicks the assigned drake
- Waits for the flight to complete, then returns to camp

**AoE Management:**

- Disables encounter nukes and PBAoE at the start of the fight
- Re-enables them when the boss is killed

### Player Notes

- The module handles drake clicking automatically — do not manually click drakes
- If manual intervention is needed (module cannot find the drake), an alert will be sent
- The add cannot be killed until the named is under 10%, and then must die before the named

---

## Veagth

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with a corrosion curse that must be cured using a specific item, and polarity mechanics that require add positioning.

### What the Module Does

**Takish'Hiz Corrosion:**

- Detects the Takish'Hiz Corrosion detriment
- Automatically uses the "Vial of Bilibin Extract" item from your inventory to cure it
- Alerts you if the item is not found in your inventory

**Polarity Announcements:**

- Announces REPEL and ATTRACT polarity changes via chat and text-to-speech
- REPEL means get the adds together
- ATTRACT means separate the adds

### Player Notes

- Make sure you have a "Vial of Bilibin Extract" in your inventory before the fight
- Pay attention to polarity announcements for add positioning

---

## Vischt Stormbones

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight against multiple Stormbones variants (Vischt, Phlent, Maerzi, Eliszy, Nrehzi) with Advantage detriments that must be removed by clicking portals, and Temporal Summoner adds that require quick response.

### What the Module Does

**Advantage Detriments:**

- Tracks four types of Advantage detriments (Forceful, Rotting, Blazing, Frenzied)
- When stacks drop to 5 or fewer, automatically moves to and clicks "a summoned portal of swirling energy" to remove the detriment

**Temporal Summoner:**

- When a Temporal Summoner spawns, automatically repositions non-flag 1 players to the summoner's location

### Player Notes

- Raid group 4 is automatically flagged (flag 1) and excluded from summoner repositioning
- Keep Vischt Stormbones separated from the other Stormbones variants

---

## Stonesong

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight with hazardous ground pools that must be avoided.

### What the Module Does

**Pool Jousting:**

- Detects spawned hazardous pool actors on the ground
- Automatically jousts away from their locations
- Uses two predefined joust spots

### Player Notes

- The module handles pool avoidance automatically
- Stay alert for multiple pools spawning in quick succession

---

## The Monument of Stone

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight against multiple stone variants (The Monument of Stone, The Cenotaph of Stone, The Statue of Stone, The Titan of Stone) where players must navigate to specific rooms to cure an incurable curse.

### What the Module Does

**Stone Hex Curse:**

- Detects when you receive the Stone Hex incurable curse
- Searches for a glowing portal actor to identify the correct room
- Automatically navigates to the room entrance, enters, and jumps to cure the curse
- If the portal is not immediately visible, systematically checks each of the 6 doorways to find it
- Returns to camp after the curse is removed

### Player Notes

- The module handles room navigation automatically when you are cursed
- There are 6 possible room locations the module will check

---

## Rugrat the Thief

Setup is automatic when engaged. Or you can use `Obj_OgreMCP:PasteButton[SetUpFor__,SetUpFor]` to do the set up immediately.

### Overview

A fight where the boss gives text commands requiring players to move to specific rooms. Three different room commands must be followed correctly.

### What the Module Does

**Room Commands:**

- **"Be in same room"** — Automatically moves to the named's location
- **"NOT be in same room"** — Automatically moves to the room farthest from the named
- **"Class rooms"** — Automatically moves to your archetype-specific room (fighters, scouts, priests, and mages each have a designated room identified by special markers)

**Configurable Timing:**

- Room joust duration defaults to 20 seconds

### Player Notes

- Three different room commands require different positioning — the module handles all three automatically
- Each command has a short delay before repositioning to allow actors to spawn
- The "dizzies" mechanic requires manual handling
