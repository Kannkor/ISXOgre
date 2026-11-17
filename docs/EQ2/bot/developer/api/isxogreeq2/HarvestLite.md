# ISXOgreEQ2.HarvestLite

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Methods

### `Interval`

`ISXOgreEQ2.HarvestLite:Interval[ms]`

Sets how often the light harvester runs a pass, in milliseconds (250 to 10000, default 500), and prints the new value; it is not saved. A missing, non-numeric or out-of-range value is refused with a warning and nothing changes.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `ms` | int |  | milliseconds between passes, 250 to 10000 |

```text
ISXOgreEQ2.HarvestLite:Interval[1000]
```

### `Off`

`ISXOgreEQ2.HarvestLite:Off`

Turns the light harvester off (`ogre end hl`): no more scans or harvests from the next frame, and it prints 'harvestlite: off'. Your current target is left as it is.

```text
ISXOgreEQ2.HarvestLite:Off
```

### `On`

`ISXOgreEQ2.HarvestLite:On`

Turns the light harvester on (`ogre hl`; it starts off and the switch is not saved): every 500 ms it double-clicks your target when that is a resource node within reach (5 units plus both model sizes), and when you have no target, are not moving or casting and have no loot window open it targets the nearest node in reach through the bot's targeting, paused or not. It never walks to a node, drops the node while you are in combat with something within 15 units targeting you, and prints 'harvestlite: ON'.

```text
ISXOgreEQ2.HarvestLite:On
```

### `Status`

`ISXOgreEQ2.HarvestLite:Status`

Prints the light harvester's state: on or off, the pass interval, the reach, threat and scan radius, its pass, scan, harvest, target and back-off counts, whether a combat back-off is holding, and what it last did.

```text
ISXOgreEQ2.HarvestLite:Status
```
