<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# OgreBotAPI.Inventory

## Members

### `AdornmentColour`

`${OgreBotAPI.Inventory.AdornmentColour[iconId]}`

Looks up the colour of an adornment from its icon id, using the bot's built-in table of known adornment icons.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `iconId` | number |  | the adornment's icon id |

**Returns:** string - White, Red, Blue, Cyan, Green, Purple or Black. Empty when the icon id is not in the table.

```text
echo ${OgreBotAPI.Inventory.AdornmentColour[3877]}
```

*Was (OldBot):* `OgreBotAPI.AdornmentIconIDColour`, `OgreBotAPI.Get_AdornmentColour`

### `AdornToRemoveSlot`

`${OgreBotAPI.Inventory.AdornToRemoveSlot[adorn]}`

The reverse of AdornToSlot: takes the slot number out of an adornment entry name, so _ADORN_&lt;slot>_&lt;name> becomes _ADORN_&lt;name>. Text that is not in that form comes back unchanged.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `adorn` | text |  | the adornment entry name, _ADORN_&lt;slot>_&lt;name> |

**Returns:** string - the entry name without the slot, or the input unchanged when it is not in the _ADORN_&lt;slot>_&lt;name> form.

```text
echo ${OgreBotAPI.Inventory.AdornToRemoveSlot["_ADORN_21_Raid Rune: Void Flow III"]}
```

*Was (OldBot):* `OgreBotAPI.ConvertAdornToRemoveSlot`

### `AdornToSlot`

`${OgreBotAPI.Inventory.AdornToSlot[adorn, slot=21]}`

Puts a slot number into an adornment entry name: _ADORN_&lt;name> becomes _ADORN_&lt;slot>_&lt;name>. Text that is not in the _ADORN_&lt;name> form (with no other underscores) comes back unchanged.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `adorn` | text |  | the adornment entry name, _ADORN_&lt;name> |
| `slot` | number | `21` | the slot number to insert |

**Returns:** string - the entry name with the slot inserted, or the input unchanged when it is not in the _ADORN_&lt;name> form.

```text
echo ${OgreBotAPI.Inventory.AdornToSlot["_ADORN_Raid Rune: Void Flow III",21]}
```

*Was (OldBot):* `OgreBotAPI.ConvertAdornToSlot`

### `Count`

`${OgreBotAPI.Inventory.Count[itemName, exact|contains]}`

Counts how many of an item you are carrying, adding up every stack in your bags and your Harvest Bag. The name match ignores case; it is exact unless you pass contains.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `itemName` | item name |  | the item to count |
| `exact\|contains` | text | `exact` | exact = the whole name must match, contains = any item whose name contains the text |

**Returns:** int - the total quantity on hand. 0 when nothing matches, the name is empty, you are not in the world, or the match word is not exact or contains (that last case also prints a line).

```text
echo ${OgreBotAPI.Inventory.Count[Ingot,contains]}
```

*Was (OldBot):* `Obj_OgreUtilities.ItemCount`, `OgreBotAPI.ItemCount`

### `CurrentImmunityRune`

`${OgreBotAPI.Inventory.CurrentImmunityRune}`

Names the immunity rune on the belt you are wearing; it only reads your own character. It needs the belt's item details: an empty answer means they are still loading (the read asks the game for them), so ask again shortly - never treat empty as no rune.

**Returns:** string - Stun, Stifle, Mez, Fear or Medic for the rune worn. Unknown when the details are loaded and no known rune is on the belt. Empty when the details are not loaded yet or you are not in the world.

```text
echo ${OgreBotAPI.Inventory.CurrentImmunityRune}
```

*Was (OldBot):* `OgreBotAPI.Get_CurrentImmunityRune`

### `IsAdornmentColour`

`${OgreBotAPI.Inventory.IsAdornmentColour[iconId, colour]}`

TRUE when an adornment icon id is a known icon of the given colour. The colour match ignores case, and a blank colour means White.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `iconId` | number |  | the adornment's icon id |
| `colour` | text | `White` | White, Red, Blue, Cyan, Green, Purple or Black |

**Returns:** bool - TRUE when the icon is in the table with that colour. FALSE when the colour differs or the icon id is not in the table.

```text
echo ${OgreBotAPI.Inventory.IsAdornmentColour[3877,White]}
```

*Was (OldBot):* `OgreBotAPI.IsAdornmentColour`

### `PackPonyRunning`

`${OgreBotAPI.Inventory.PackPonyRunning}`

TRUE while a pack pony run is in progress, whether CheckPackPony or the bot's own pack pony chore started it.

**Returns:** bool: TRUE while a pack pony run is in progress; FALSE otherwise.

```text
echo ${OgreBotAPI.Inventory.PackPonyRunning}
```

*Was (OldBot):* `OgreBotAPI.Get_APIPackPonyRunning`, `OgreBotAPI.Get_PackPonyRunning`, `OgreBotAPI.bAPIPackPonyRunning`

### `SlotAvailable`

`${OgreBotAPI.Inventory.SlotAvailable[slot name]}`

TRUE when the item worn in the named equipment slot can be used (activated) right now - for example, a clicky cloak on cooldown reads FALSE. It does not tell you whether the slot is empty or can hold an item.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `slot name` | text |  | one of: primary, secondary, head, cloak, chest, shoulders, forearms, hands, legs, feet, left_ring, right_ring, ears, ears2, neck, left_wrist, right_wrist, ranged, ammo, waist, activate1, activate2, event_slot, food, drink (any case) |

**Returns:** bool - TRUE when the item in that slot is usable now. FALSE when it is not, when the name is not one of the slot names (a warning is printed), or when the slot could not be read.

```text
echo ${OgreBotAPI.Inventory.SlotAvailable[cloak]}
```

*Was (OldBot):* `OgreBotAPI.EquipmentSlotAvailable`

### `SlotModifier`

`${OgreBotAPI.Inventory.SlotModifier[slot, modifier]}`

Reads one stat modifier from the item equipped in a slot, matching the modifier name without regard to case. It reads the item's detail record, which the game may have to fetch first, so it can return empty until that has loaded.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `slot` | slot name or number |  | the equipment slot, as the game's equipment list accepts it |
| `modifier` | text |  | the modifier name, e.g. Potency |

**Returns:** string - the modifier's value. Empty when the item has no such modifier, its details are not loaded yet, or you are not in the world.

```text
echo ${OgreBotAPI.Inventory.SlotModifier[primary,Potency]}
```

*Was (OldBot):* `OgreBotAPI.Get_EquipmentModifierValue`

### `SlotName`

`${OgreBotAPI.Inventory.SlotName[n=1]}`

Turns one of the bot's slot numbers (1 to 22) into the bot's short slot name: primary, secondary, head, chest, shoulders, Forearms, Hands, legs, feet, LRing, RRing, ear, ear2, neck, lwrist, rwrist, ranged, ammo, waist, cloak, Activate1, Activate2.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `n` | number | `1` | the slot number, 1 to 22 |

**Returns:** string - the slot name. Empty when n is outside 1 to 22.

```text
echo ${OgreBotAPI.Inventory.SlotName[20]}
```

*Was (OldBot):* `OgreBotAPI.Get_SlotNum_To_SlotNames`, `OgreBotAPI.SlotNum_SlotNames`, `OgreBotAPI.Slot_SlotNames`

### `SlotNumAvailable`

`${OgreBotAPI.Inventory.SlotNumAvailable[slot number 1-22]}`

The same check as SlotAvailable, with the slot given as a number from 1 to 22 in the bot's own numbering (not the game's equipment index): 1 primary, 2 secondary, 3 head, 4 chest, 5 shoulders, 6 forearms, 7 hands, 8 legs, 9 feet, 10 left_ring, 11 right_ring, 12 ears, 13 ears2, 14 neck, 15 left_wrist, 16 right_wrist, 17 ranged, 18 ammo, 19 waist, 20 cloak, 21 activate1, 22 activate2.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `slot number 1-22` | number |  | the slot, in the bot's numbering (whole digits only) |

**Returns:** bool - TRUE when the item in that slot is usable now. FALSE when it is not, when the number is not 1 to 22 (a warning is printed), or when the slot could not be read. event_slot, food and drink have no number; use SlotAvailable for them.

```text
echo ${OgreBotAPI.Inventory.SlotNumAvailable[20]}
```

*Was (OldBot):* `OgreBotAPI.EquipmentSlotNumAvailable`

### `SlotUIName`

`${OgreBotAPI.Inventory.SlotUIName[n=1]}`

Turns one of the bot's slot numbers (1 to 22) into the slot's name as the game's character window spells it: primary, secondary, head, chest, shoulders, Forearms, Hands, legs, feet, left_ring, right_ring, ears, ears2, neck, left_wrist, right_wrist, ranged, ammo, waist, cloak, Activate1, Activate2.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `n` | number | `1` | the slot number, 1 to 22 |

**Returns:** string - the window's slot name. Empty when n is outside 1 to 22.

```text
echo ${OgreBotAPI.Inventory.SlotUIName[10]}
```

*Was (OldBot):* `OgreBotAPI.Get_SlotNum_EQ2UIPageSlotNames`, `OgreBotAPI.SlotNum_EQ2UIPageSlotNames`

## Methods

### `AddEmbargo`

`OgreBotAPI.Inventory:AddEmbargo[fw, linkId, durationSec]`

Stops the bot's casting from using an item, given by its LinkID, for a number of seconds (while item embargo is enabled in the bot's settings). Both arguments are required; a new embargo on the same item only ever extends it, and the signed and unsigned forms of a LinkID both work.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `linkId` | number |  | the item's LinkID, a whole number from -2147483648 to 4294967295 |
| `durationSec` | number |  | how long, in seconds; 0 expires at once |

```text
OgreBotAPI.Inventory:AddEmbargo["all",-1112810742,30]
```

*Was (OldBot):* `OgreBotAPI:ItemEmbargo_AddRotateTimer`

### `AutoConsumeFamiliarXP`

`OgreBotAPI.Inventory:AutoConsumeFamiliarXP[fw]`

Uses "(Temporary 4 hour) Familiar Experience" from your bags up to 10 times, waiting while you are in combat or moving. Only one temporary auto-consume run (this, mount training or research) runs at a time; a new call replaces the one before.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Inventory:AutoConsumeFamiliarXP[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:AutoConsumeTemporaryFamiliarExperience`

### `AutoConsumeFoodDrink`

`OgreBotAPI.Inventory:AutoConsumeFoodDrink[fw, value=TRUE]`

Turns auto-consume on or off for the food and drink in your equipped provision slots, flipping only a slot whose setting differs from what you asked. It is queued, with a 1-second pause after.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `value` | true/false or word | `TRUE` | TRUE = on, FALSE = off, toggle = flip, report = change nothing; any other word means TRUE |

```text
OgreBotAPI.Inventory:AutoConsumeFoodDrink[igw:${Me.Name},TRUE]
```

*Was (OldBot):* `OgreBotAPI:Change_FoodDrinkAutoConsume`, `OgreBotAPI:FoodDrink_AutoConsume`

### `AutoConsumeMountTraining`

`OgreBotAPI.Inventory:AutoConsumeMountTraining[fw]`

Checks that mount training is running, then uses "(Temporary 4 hour) Mount Training Reduction" from your bags up to 10 times, waiting while you are in combat or moving. If training is not running nothing is consumed; a new call replaces any temporary auto-consume run already going.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Inventory:AutoConsumeMountTraining[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:AutoConsumeTemporaryMountTrainingReduction`

### `AutoConsumeResearch`

`OgreBotAPI.Inventory:AutoConsumeResearch[fw]`

Uses "(Temporary 4 hour) Research Reduction" from your bags up to 10 times, waiting while you are in combat or moving. It opens the research window if needed and stops when research is complete or nothing is being researched; a new call replaces any temporary auto-consume run already going.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Inventory:AutoConsumeResearch[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:AutoConsumeTemporaryResearchReduction`

### `AutoConsumeStatPotions`

`OgreBotAPI.Inventory:AutoConsumeStatPotions[fw, value=TRUE, potion=""]`

Turns auto-consume on or off for a stat potion in your bags (exact name); with no potion named it uses the bot's configured stat potion. It flips only when the setting differs from what you asked, is queued with a 1-second pause after, and prints a line if the potion is not in your bags.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `value` | true/false or word | `TRUE` | TRUE = on, FALSE = off, toggle = flip, report = change nothing; any other word means TRUE |
| `potion` | item name | `""` | the potion; blank = the configured stat potion |

```text
OgreBotAPI.Inventory:AutoConsumeStatPotions[igw:${Me.Name},TRUE]
```

*Was (OldBot):* `OgreBotAPI:Change_StatPotionsAutoConsume`, `OgreBotAPI:StatPotions_AutoConsume`, `OgreBotAPI:Change_PoisonAutoConsume`

### `ChangeBeltAdorn`

`OgreBotAPI.Inventory:ChangeBeltAdorn[fw, adornType, unequip=TRUE]`

Applies an immunity rune from your bags to your belt; it is queued and refuses while you are moving or in combat. A rune it replaces is accepted back and moved next to where the new rune was.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `adornType` | text |  | Stun, Stifle, Mez, Fear or Medic |
| `unequip` | true/false | `TRUE` | TRUE takes the belt off, applies the rune and puts the belt back on; FALSE applies the rune to the worn belt |

```text
OgreBotAPI.Inventory:ChangeBeltAdorn[${Me.Name},Stun,TRUE]
```

*Was (OldBot):* `OgreBotAPI:ChangeBeltAdorn`

### `CheckGear`

`OgreBotAPI.Inventory:CheckGear[fw, threshold=100]`

Checks the condition of the item in your primary slot and prints "&lt;name> gear N%" when it is at or below the threshold (and always at 30, 20, 10 and 0). It is queued, waits up to 5 seconds for the item's details to load, and fires the gear-condition event on every check.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `threshold` | number | `100` | the percent at or below which to print; TRUE means 100 |

```text
OgreBotAPI.Inventory:CheckGear[igw:${Me.Name},90]
```

*Was (OldBot):* `OgreBotAPI:CheckGear`

### `CheckPackPony`

`OgreBotAPI.Inventory:CheckPackPony[fw, forceCheck=FALSE]`

Runs the Artisan's Pack Pony chore now: summons the pony, works through its conversation and dismisses it, pausing the bot for the run (and resuming it after, if it was not already paused). It does not need the pack pony settings enabled, but it waits out the re-check interval unless forced, and prints why if it cannot start (already running, not in the world, no pack pony ability, in combat).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `forceCheck` | true/false | `FALSE` | TRUE = run even within the re-check interval |

```text
OgreBotAPI.Inventory:CheckPackPony[${Me.Name},TRUE]
```

*Was (OldBot):* `OgreBotAPI:CheckPackPony`

### `ClearAllEmbargos`

`OgreBotAPI.Inventory:ClearAllEmbargos[fw]`

Removes every item embargo. Ability embargoes are not touched.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Inventory:ClearAllEmbargos["all"]
```

### `ClearEmbargo`

`OgreBotAPI.Inventory:ClearEmbargo[fw, linkId]`

Removes the item embargo on one item, by the same LinkID AddEmbargo took. Does nothing if that item has no embargo.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `linkId` | number |  | the item's LinkID |

```text
OgreBotAPI.Inventory:ClearEmbargo["all",-1112810742]
```

### `ConsumeFamiliars`

`OgreBotAPI.Inventory:ConsumeFamiliars[fw]`

Goes through each familiar already loose in your bags: one not yet in your collection is added, one you already have is consumed for familiar experience. It does not unpack Familiar Cages - UnpackConsumeFamiliars does both.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Inventory:ConsumeFamiliars[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Consume_Familiars`

### `ConsumeList`

`OgreBotAPI.Inventory:ConsumeList[fw, -fc, -all, -st]`

Runs the bot's Consume Items list once: it uses the first entry that is ready and in your bags, or every one with -all. It skips disabled entries, in-combat-only entries outside combat and entries whose own timer has not run out, and stops if you are dead or moving.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `-fc` | flag |  | force combat: ignore the in-combat-only setting and the in-combat wait between items |
| `-all` | flag |  | use every eligible entry, not just the first |
| `-st` | flag |  | skip timers: ignore each item's own timer |

```text
OgreBotAPI.Inventory:ConsumeList[igw:${Me.Name},-all]
```

*Was (OldBot):* `OgreBotAPI:ConsumeItems_ProcessList`

### `ConsumeStatusIngots`

`OgreBotAPI.Inventory:ConsumeStatusIngots[fw, amount=99999]`

Targets yourself and consumes status ingots - every bag item whose name contains Ingot - by examining each and confirming, until the amount is used. An item that fails twice in a row is skipped (tradeskill ingots match the name too); it is queued, stops if you lose the target, makes at most 250 tries a run, and sends a finished line to every session.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `amount` | number | `99999` | how many to consume; 0 or less means all |

```text
OgreBotAPI.Inventory:ConsumeStatusIngots[${Me.Name},10]
```

*Was (OldBot):* `OgreBotAPI:Consume_Status_Ignots`, `OgreBotAPI:Consume_Status_Ingots`

### `ConsumeStatusTokens`

`OgreBotAPI.Inventory:ConsumeStatusTokens[fw, amount=99999]`

Targets yourself and consumes Status Token items, then Status Coin items, by examining each and confirming. Every try counts toward the amount whether or not it consumed one; it is queued, stops if you lose the target, makes at most 250 tries a run, and sends a finished line to every session.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `amount` | number | `99999` | how many tries to make; 0 or less means all |

```text
OgreBotAPI.Inventory:ConsumeStatusTokens[${Me.Name},10]
```

*Was (OldBot):* `OgreBotAPI:Consume_Status_Tokens`

### `DestroyItem`

`OgreBotAPI.Inventory:DestroyItem[fw, itemName, charges=0]`

Destroys an item in your carried bags by name, but only when it has no charges or its charges equal the number you give, so a partly used charged item is kept. It is queued, waits a second for the item's details to load and refuses with a line if they did not arrive; the destroy cannot be undone.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `itemName` | item name |  | the item to destroy |
| `charges` | number | `0` | the charge count the item must have to be destroyed |

```text
OgreBotAPI.Inventory:DestroyItem[${Me.Name},"Rusty Dagger",0]
```

*Was (OldBot):* `OgreBotAPI:DestroyItem`

### `DestroyItemNoChecks`

`OgreBotAPI.Inventory:DestroyItemNoChecks[fw, itemName]`

Destroys an item in your carried bags (not the bank) whose name matches exactly, ignoring case - the whole stack, with no charge check. This cannot be undone; use DestroyItem to keep a partly used charged item safe.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `itemName` | item name |  | the item to destroy |

```text
OgreBotAPI.Inventory:DestroyItemNoChecks[${Me.Name},"Rusty Dagger"]
```

*Was (OldBot):* `OgreBotAPI:DestroyItem_NoChecks`

### `EquipCharm`

`OgreBotAPI.Inventory:EquipCharm[fw, slot=1]`

Equips the item set as charm option 1 or 2 in the bot's Equipment settings, finding it in your bags by name. This only asks the game to equip it; the game can still refuse (slot rules, relic limits).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `slot` | number | `1` | which charm option to equip, 1 or 2 |

```text
OgreBotAPI.Inventory:EquipCharm[igw:${Me.Name},2]
```

*Was (OldBot):* `OgreBotAPI:EquipCharm`

### `Examine`

`OgreBotAPI.Inventory:Examine[fw, item=DoesNotExist]`

Opens the examine window for an item in your main bags, matched by exact name. Does nothing when no such item is there.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `item` | item name | `DoesNotExist` | the item to examine |

```text
OgreBotAPI.Inventory:Examine[${Me.Name},"Spirit of the Cat"]
```

*Was (OldBot):* `OgreBotAPI:ExamineInventoryItem`, `Obj_OgreIH:ExamineInventoryItem`

### `ExamineAll`

`OgreBotAPI.Inventory:ExamineAll[fw, item...]`

Examines every carried item whose name contains any of the given texts (main bags, Overseer Bag and Harvest Bag), each stack as many times as its quantity plus two, closing the examine window after each stack. It is queued and reads the bags when it runs; it prints a line if nothing matches.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `item...` | item names |  | one or more name texts to match (contains, any case) |

```text
OgreBotAPI.Inventory:ExamineAll[${Me.Name},Potion]
```

*Was (OldBot):* `OgreBotAPI:ExamineAllOfItem`

### `InitAdornmentInfo`

`OgreBotAPI.Inventory:InitAdornmentInfo[fw]`

Fills the adornment icon colour table that AdornmentColour and IsAdornmentColour read. The table is filled automatically, so a script does not normally need this.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Inventory:InitAdornmentInfo[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Initialize_AdornmentInfo`

### `RedeemKrono`

`OgreBotAPI.Inventory:RedeemKrono[fw]`

Redeems a Krono from the Krono page of your character window and confirms it, then prints whether it worked and fires the Krono redemption event. With no Krono to redeem it prints a line and stops.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Inventory:RedeemKrono[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:RedeemKrono`

### `SpewSlotNames`

`OgreBotAPI.Inventory:SpewSlotNames[fw]`

Prints one console line per gear slot 1 to 22: the slot number, the bot's name for that number, and the item equipped there (NULL when nothing reads).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Inventory:SpewSlotNames[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Spew_SlotNum_To_SlotNames`

### `Unpack`

`OgreBotAPI.Inventory:Unpack[fw, item, ...]`

Unpacks an item in your bags (exact name), with flags after the item in any order: -qty N unpacks N (1 to 1000), -all keeps going until none is left (up to 1000), and -pick &lt;number \| name \| lowest> chooses the reward when the window offers a choice (lowest = the choice you hold the fewest of). It is queued and waits out an open reward window; a bad flag is refused with one line before anything is queued.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `item` | item name |  | the item to unpack |
| `...` | flags |  | -qty N or -all, and -pick &lt;number \| name \| lowest> |

```text
OgreBotAPI.Inventory:Unpack[${Me.Name},"Reward Crate",-all,-pick,lowest]
```

*Was (OldBot):* `OgreBotAPI:Unpack`, `OgreBotAPI:Unpack_EmpyralStones`, `OgreBotAPI:Unpack_PlanarStones`

### `UnpackConsumeFamiliars`

`OgreBotAPI.Inventory:UnpackConsumeFamiliars[fw]`

Unpacks every Familiar Cage in your bags, then goes through each familiar in your bags: one not yet in your collection is added, one you already have is consumed for familiar experience (summoning a familiar if one is needed). A finished line is sent to every session when it is done.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Inventory:UnpackConsumeFamiliars[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Unpack_Consume_Familiars`

### `UnpackFamiliars`

`OgreBotAPI.Inventory:UnpackFamiliars[fw]`

Unpacks every Familiar Cage in your bags, one at a time (up to 20). It is queued, and prints a line if there is no Familiar Cage.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Inventory:UnpackFamiliars[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Unpack_Familiars`

### `UpgradeItem`

`OgreBotAPI.Inventory:UpgradeItem[fw]`

Moves the adornments from the old item in bag 1 slot 1 onto the new item in bag 1 slot 2, moves the old item to the end of bag 1 and equips the new one. Both must be for the same slot and the new one must have no adornments; an adornment with no free slot of its colour goes back on the old item.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Inventory:UpgradeItem[${Me.Name}]
```

### `Use`

`OgreBotAPI.Inventory:Use[fw, item, ...]`

Uses an item by name: equipped items (gear, food and drink) are checked first, then your carried bags (exact name, any case). The use is queued and fires when the cast bar is free; an item that is not found prints a line, and an empty name or Nothing does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `item` | item name |  | the item to use |
| `...` | any |  | extra arguments are ignored |

```text
OgreBotAPI.Inventory:Use[${Me.Name},"Spirit of the Cat"]
```

*Was (OldBot):* `OgreBotAPI:UseItem`

### `UseOnPlayer`

`OgreBotAPI.Inventory:UseOnPlayer[fw, item, player=me, ...]`

Uses an item on another player: it targets that player, uses the item (equipped first, then bags) and puts your old target back. It does nothing if the item is on cooldown, if an effect the item is known to give is already maintained by you, or if the cast bar is busy; an item or player that is not found prints a line.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `item` | item name |  | the item to use |
| `player` | player name or actor id | `me` | who to use it on |
| `...` | any |  | extra arguments are ignored |

```text
OgreBotAPI.Inventory:UseOnPlayer[${Me.Name},"Spirit of the Cat",${Target.Name}]
```

*Was (OldBot):* `OgreBotAPI:UseItemOnPlayer`
