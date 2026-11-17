# OgreBotAPI.Consumables

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Methods

### `AddMercenaries`

`OgreBotAPI.Consumables:AddMercenaries[fw]`

Queues, for every item in your bags, Overseer bag and harvest bag whose name contains "Mercenary: ", an examine that answers the "What would you like to do?" dialog with its first choice and closes the examine window. It echoes how many it is adding, or that there are none.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Consumables:AddMercenaries[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Mercenary_AddMercenaries`

### `CheckFamiliar`

`OgreBotAPI.Consumables:CheckFamiliar[fw]`

Summons your familiar at once with summon_familiar, unless your Summon Familiar buff is already maintained. After a summon it ignores further calls for 2 seconds.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Consumables:CheckFamiliar[all]
```

*Was (OldBot):* `OgreBotAPI:Check_Familiar`

### `CheckMercenaryTraining`

`OgreBotAPI.Consumables:CheckMercenaryTraining[fw]`

Queues a check that resumes your mercenary if needed, opens Persona on the Mercenary tab and starts training when the button is enabled (it reports training already running or max level instead), then closes Persona, and suspends the mercenary again only when this check summoned it. It refuses in a full group of 6, reports every step to the console, and a new call replaces an earlier one.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Consumables:CheckMercenaryTraining[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:CheckMercenaryTraining`

### `CheckMountTraining`

`OgreBotAPI.Consumables:CheckMountTraining[fw]`

Queues a check that opens Persona on the Mounts tab and starts training your current mount when the Start Training button is showing, answering the confirm popup (it declines when the popup says training will be carried over from another mount), then closes Persona. You must be on a mount that is not a flight transport or it stops with a console line, and a new call replaces an earlier one.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Consumables:CheckMountTraining[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:CheckMountTraining`

### `CoV`

`OgreBotAPI.Consumables:CoV[fw, travel=Teleport, toon, allowSameZone=FALSE]`

Uses Call of the Veteran to bring up the veteran reward porter (or uses one already within 15, or a selection window already open), then picks the travel option and the named group or raid member in its two popups. It is skipped with a console line when you are in combat, name yourself, the member is not in your group (raid when you are in one), the member is already in your zone without allowSameZone, or there is no porter, no open window and the item is not ready.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `travel` | string | `Teleport` | the option to pick in the first popup, matched by its label in any case; the default takes you to the member, Summon brings the member to you |
| `toon` | string |  | the group or raid member to pick in the second popup, by full name; blank echoes that no toon was named and does nothing |
| `allowSameZone` | bool | `FALSE` | TRUE goes ahead even when the member is already in your zone; FALSE skips that case |

```text
OgreBotAPI.Consumables:CoV[${Me.Name},Summon,${Group[1].Name}]
```

*Was (OldBot):* `OgreBotAPI:CoV`

### `DrinkAlcohol`

`OgreBotAPI.Consumables:DrinkAlcohol[fw, item]`

Drinks the named item from your bags at once, using the game's drink_alcohol command on it. With no item named it says so on the console, and so does an item that is not in your bags.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `item` | string | `""` | the item's full name (case does not matter); it must be in your bags, not the bank; required |

```text
OgreBotAPI.Consumables:DrinkAlcohol[${Me.Name},"Flask of Ale"]
```

*Was (OldBot):* `OgreBotAPI:Drink_Alcohol`

### `MountDown`

`OgreBotAPI.Consumables:MountDown[fw]`

Queues a forced dismount: sit, toggle summon_mount once, then stand, about 3 seconds in all. It does nothing if you are moving when its turn comes, and with one line if you are not mounted.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Consumables:MountDown[all]
```

*Was (OldBot):* `OgreBotAPI:Force_MountOff`

### `MountUp`

`OgreBotAPI.Consumables:MountUp[fw]`

Queues a forced mount-up: sit, toggle summon_mount, stand, then toggle summon_mount again, about 4 seconds in all. It does nothing if you are moving when its turn comes, and with one line if you are already mounted.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Consumables:MountUp[all]
```

*Was (OldBot):* `OgreBotAPI:Force_MountOn`

### `RekindleHeartstone`

`OgreBotAPI.Consumables:RekindleHeartstone[fw]`

Applies the Rekindle Bond verb at once to the nearest actor whose name contains "Heartstone". Nothing happens, with no message, when there is none or it is more than 6 away.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Consumables:RekindleHeartstone[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Heartstone_RekindleBond`

### `ReplenishFoodDrink`

`OgreBotAPI.Consumables:ReplenishFoodDrink[fw]`

Opens the nearest Food & Drink Depot (it must be within 11) and tops your equipped food and drink up to stacks of 100, equipping a bag copy into the slot before and after the pull, then closes the depot window. It uses the names in your Food and Drink slots, or the configured fallback names when a slot is empty, runs in the background over a few seconds, and only one depot run can be in flight at a time (a second call echoes that it is busy).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Consumables:ReplenishFoodDrink[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:FoodDrink_Replenish`, `OgreBotAPI:Get_FoodDrink`

### `ReplenishStatPotions`

`OgreBotAPI.Consumables:ReplenishStatPotions[fw, potion=""]`

Opens the nearest Poison, Potion, & Totem Depot (it must be within 11) and pulls one potion until your bags hold 100 of it, then closes the depot window. Each step reports to the console (already stocked, depot out, depot low, no depot nearby), and only one depot run can be in flight at a time.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `potion` | string | `""` | the potion's name as the depot lists it; blank uses the statPotion name from replenish-names.json (your OgreSave/EQ2/Replenish/custom copy wins over the shipped one) |

```text
OgreBotAPI.Consumables:ReplenishStatPotions[${Me.Name},"Planar Elixir of intellect"]
```

*Was (OldBot):* `OgreBotAPI:Get_StatPotions`, `OgreBotAPI:StatPotions_Replenish`, `OgreBotAPI:Get_Poisons`

### `ScrollOf`

`OgreBotAPI.Consumables:ScrollOf[fw, name=Prowess, cancelIfDurationLessThan=0, useBest=FALSE]`

Keeps one scroll buff up: if a buff of that family is already maintained it does nothing (or cancels and recasts it when it has fewer than cancelIfDurationLessThan minutes left), otherwise it casts the family's ability already in your spellbook, or scribes one from your bags first when none is, and checks that it landed. It is queued, reports each outcome to the console, and a new call replaces one still running.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `name` | string | `Prowess` | the scroll family, any case: Prowess, forcelink, Pain, painlink, Power or powerlink; anything else is refused with a console warning |
| `cancelIfDurationLessThan` | int | `0` | minutes; a maintained buff of the family with less time left than this is cancelled and recast, 0 leaves any maintained one alone |
| `useBest` | bool | `FALSE` | only used when none of the family is in your spellbook yet: TRUE scribes the first bag scroll found from the bottom of the family's scroll list, FALSE from the top |

```text
OgreBotAPI.Consumables:ScrollOf[igw:${Me.Name},Prowess,10,TRUE]
```

*Was (OldBot):* `OgreBotAPI:ScrollOf`

### `SummonFamiliar`

`OgreBotAPI.Consumables:SummonFamiliar[fw]`

Sends summon_familiar at once, with no check of whether a familiar is already out. Use CheckFamiliar to summon only when needed.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Consumables:SummonFamiliar[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Summon_Familiar`
