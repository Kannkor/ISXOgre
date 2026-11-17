<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# ISXOgreEQ2.DepotTransfer

## Members

### `Running`

`${ISXOgreEQ2.DepotTransfer.Running}`

TRUE while a house-to-guild-hall, guild-hall-to-house or small-to-large depot transfer is running. Only one transfer runs at a time; starting another is refused with a busy warning.

**Returns:** bool: TRUE while a depot transfer is running; FALSE when idle.

```text
echo ${ISXOgreEQ2.DepotTransfer.Running}
```

### `Status`

`${ISXOgreEQ2.DepotTransfer.Status}`

The running transfer's current depot type, its place in the list and how many withdrawals have been made, or "idle". It is the same text `${ISXOgreEQ2.DepotTransfer}` returns.

**Returns:** string: "idle", or "&lt;type> (n/total, k pulled)" where type is harvest, ammo, adorn, food, lore, potion, collectible, fuel or scroll.

```text
echo ${ISXOgreEQ2.DepotTransfer.Status}
```

## Methods

### `GHToHouse`

`ISXOgreEQ2.DepotTransfer:GHToHouse[flags...]`

The engine behind `ogre ghtohouse`: must start in your guild hall, then withdraws each chosen guild hall depot and deposits it into the matching personal house depot, travelling back and forth until that depot is empty (at most 40 trips per type). If a house depot says it cannot hold any more, the rest goes back into the guild hall depot and that type is skipped; each house depot must be within 8 m of where you arrive in the house.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `flags...` | string |  | -all (the eight shared depot types, not scroll), or any of -harvest/-h, -ammo, -adorn, -food, -lore, -potion, -collect/-collectible/-c, -fuel, each with a -no twin (-noharvest/-nh, -nocollect/-nocollectible/-nc, -nofuel ...); read left to right so `-all -nofuel` is all but fuel; a bare word is the house owner to enter (default your own name); an unknown flag is warned about and ignored; at least one depot type must end up selected or the call is refused; -scroll adds the scroll depot, which -all does not include |

```text
ISXOgreEQ2.DepotTransfer:GHToHouse[-harvest,-scroll]
```

### `HouseToGH`

`ISXOgreEQ2.DepotTransfer:HouseToGH[flags...]`

The engine behind `ogre housetogh`: empties the chosen personal house depots into the matching guild hall depots, travelling between the guild hall and the house as often as needed (at most 40 trips per depot type), and pulling Superior Rune items one at a time. Started in the guild hall it first deposits what you carry there; each guild hall depot must be within 11 m of where you arrive, and a missing door or depot stops the run with a console warning.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `flags...` | string |  | -all (the eight shared depot types, not scroll), or any of -harvest/-h, -ammo, -adorn, -food, -lore, -potion, -collect/-collectible/-c, -fuel, each with a -no twin (-noharvest/-nh, -nocollect/-nocollectible/-nc, -nofuel ...); read left to right so `-all -nofuel` is all but fuel; a bare word is the house owner to enter (default your own name); an unknown flag is warned about and ignored; at least one depot type must end up selected or the call is refused; -scroll is warned about as unknown here (there is no house scroll depot) |

```text
ISXOgreEQ2.DepotTransfer:HouseToGH[-all,-nofuel]
```

### `SmallToLarge`

`ISXOgreEQ2.DepotTransfer:SmallToLarge[flags...]`

The engine behind `ogre smalldepottobigdepot`: in your guild hall, withdraws one depot type from "&lt;type> Depot" and deposits it into "&lt;type> Depot (Large)" (within 11 m), repeating until the small depot is empty. It is refused outside a guild hall or for an unknown type; with the do-not-deposit option it fills your bags once and stops.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `flags...` | string | `-harvest` | one depot type: -harvest, -adorn/-adornment, -ammo, -scroll/-spell, -collectible/-collectable, -food/-drink, -fuel, -lore/-legend or -potion/-poison/-totem (the last one given wins); TRUE, 1 or -donotdeposit only fills your bags, FALSE or 0 turns that off again; any other word refuses the call |

```text
ISXOgreEQ2.DepotTransfer:SmallToLarge[-adorn]
```

### `Stop`

`ISXOgreEQ2.DepotTransfer:Stop`

Stops the running depot transfer and prints "depot transfer: stopped."; does nothing when idle. You stay where the transfer had got to, and items already withdrawn stay in your bags.

```text
ISXOgreEQ2.DepotTransfer:Stop
```
