<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# ISXOgreEQ2.ZoneReset

## Methods

### `Add`

`ISXOgreEQ2.ZoneReset:Add[zone]`

Adds one zone to the reset queue and prints how many it holds.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `zone` | string |  | The zone's name; several words are joined into one name; required. |

```text
ISXOgreEQ2.ZoneReset:Add["The Feerrott"]
```

### `AddFilter`

`ISXOgreEQ2.ZoneReset:AddFilter[filter]`

Adds every zone the filter picks from the last read to the reset queue and prints how many.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `filter` | string |  | resettable, noraid or notlocked. Optional: anything else reads as resettable. |

```text
ISXOgreEQ2.ZoneReset:AddFilter[resettable]
```

### `Clear`

`ISXOgreEQ2.ZoneReset:Clear`

Empties the reset queue.

```text
ISXOgreEQ2.ZoneReset:Clear
```

### `Dump`

`ISXOgreEQ2.ZoneReset:Dump`

Prints the zone table from the last read to the console.

```text
ISXOgreEQ2.ZoneReset:Dump
```

### `End`

`ISXOgreEQ2.ZoneReset:End`

Stops what this tool asked for, drops what it had queued to run, and closes the window, the same as `ogre end zone` and the window's X. A reset that an Instance Controller run or a script asked for carries on.

```text
ISXOgreEQ2.ZoneReset:End
```

### `Flags`

`ISXOgreEQ2.ZoneReset:Flags[flags]`

The flag form, the same as `ogre zone -zone ...`; -all with -force is refused. -h prints the usage.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `flags` | string |  | -zone names one zone and takes every word up to the next flag, -force force resets it and spends a charge, -all resets every resettable zone, -allowRaid includes raid zones, -fleet goes to the For Who selection; one argument each; required. |

```text
ISXOgreEQ2.ZoneReset:Flags[-zone,"The Feerrott"]
```

### `Force`

`ISXOgreEQ2.ZoneReset:Force[zone]`

Force resets one zone, which SPENDS one of your limited reset charges and cannot be undone. With no zone it prints one warning and does nothing, and it is refused while a flow runs.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `zone` | string |  | The zone's name; several words are joined into one name; required. |

```text
ISXOgreEQ2.ZoneReset:Force["The Feerrott"]
```

### `Help`

`ISXOgreEQ2.ZoneReset:Help`

Prints the `ogre zone` words and flags to the console.

```text
ISXOgreEQ2.ZoneReset:Help
```

### `List`

`ISXOgreEQ2.ZoneReset:List`

Reads the Zone Reuse window again; it opens and closes. Refused while a flow runs.

```text
ISXOgreEQ2.ZoneReset:List
```

### `Open`

`ISXOgreEQ2.ZoneReset:Open`

Opens the Zone Resetter window, which reads the Zone Reuse window, the same as bare `ogre zone`.

```text
ISXOgreEQ2.ZoneReset:Open
```

### `Queue`

`ISXOgreEQ2.ZoneReset:Queue`

Prints the reset queue to the console.

```text
ISXOgreEQ2.ZoneReset:Queue
```

### `Reset`

`ISXOgreEQ2.ZoneReset:Reset[word]`

Resets the timer of every zone in the queue. Refused while a flow runs.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `word` | string |  | fleet also sends it to the For Who window's selection. Optional. |

```text
ISXOgreEQ2.ZoneReset:Reset[fleet]
```

### `Status`

`ISXOgreEQ2.ZoneReset:Status`

Prints the flow state, zone and queue counts and counters to the console.

```text
ISXOgreEQ2.ZoneReset:Status
```
