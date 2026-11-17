# ISXOgreEQ2.Lag

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Methods

### `Budget`

`ISXOgreEQ2.Lag:Budget[first,second]`

Sets the two frame budgets the reports count against and saves them, then prints them. A first budget of 1 ms or less, or a second that is not above it, is not taken; with either value missing it prints one warning.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `first` | float |  | The first budget in ms. |
| `second` | float |  | The second budget in ms, above the first. |

```text
ISXOgreEQ2.Lag:Budget[33,50]
```

### `Clear`

`ISXOgreEQ2.Lag:Clear`

Clears the recorded frames; recording carries on.

```text
ISXOgreEQ2.Lag:Clear
```

### `Close`

`ISXOgreEQ2.Lag:Close`

Closes the Lag window, the same as `ogre end lag`. The ledger keeps recording; :Off stops it.

```text
ISXOgreEQ2.Lag:Close
```

### `Dump`

`ISXOgreEQ2.Lag:Dump[seconds]`

Writes the recorded frames to the dump file and says where.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `seconds` | float |  | How far back to dump. Optional: everything recorded when left out. |

```text
ISXOgreEQ2.Lag:Dump[120]
```

### `Minutes`

`ISXOgreEQ2.Lag:Minutes[minutes]`

Sets how many minutes of frames the ledger holds, saves it, and starts the ledger empty. With no value it prints one warning and changes nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `minutes` | int |  | Minutes to hold, held between 1 and 60. |

```text
ISXOgreEQ2.Lag:Minutes[10]
```

### `Off`

`ISXOgreEQ2.Lag:Off`

Turns the ledger off and saves it: nothing is recorded, and the frames already recorded are kept.

```text
ISXOgreEQ2.Lag:Off
```

### `On`

`ISXOgreEQ2.Lag:On`

Turns the ledger on and saves it: every frame is recorded.

```text
ISXOgreEQ2.Lag:On
```

### `Open`

`ISXOgreEQ2.Lag:Open`

Opens the Lag window, the same as bare `ogre lag`.

```text
ISXOgreEQ2.Lag:Open
```

### `Overhead`

`ISXOgreEQ2.Lag:Overhead`

Prints what the ledger itself costs per frame to the console.

```text
ISXOgreEQ2.Lag:Overhead
```

### `Report`

`ISXOgreEQ2.Lag:Report[seconds]`

Prints the report for the last stretch of frames to the console: frame rate, stability, and what cost the most.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `seconds` | float |  | How far back to look. Optional: 60 when left out. |

```text
ISXOgreEQ2.Lag:Report[30]
```
