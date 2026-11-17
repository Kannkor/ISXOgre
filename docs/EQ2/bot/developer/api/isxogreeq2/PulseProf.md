# ISXOgreEQ2.PulseProf

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Methods

### `Help`

`ISXOgreEQ2.PulseProf:Help`

Prints the `ogre pulseprof` usage to the console, the same as bare `ogre pulseprof`.

```text
ISXOgreEQ2.PulseProf:Help
```

### `Off`

`ISXOgreEQ2.PulseProf:Off`

Turns the profiler off: no overhead, and the counters stay frozen. `ogre end pulseprof` is this.

```text
ISXOgreEQ2.PulseProf:Off
```

### `On`

`ISXOgreEQ2.PulseProf:On`

Turns the profiler on and resets the counters.

```text
ISXOgreEQ2.PulseProf:On
```

### `Overhead`

`ISXOgreEQ2.PulseProf:Overhead`

Prints what the profiler itself costs to the console.

```text
ISXOgreEQ2.PulseProf:Overhead
```

### `Report`

`ISXOgreEQ2.PulseProf:Report[count,reads]`

Prints the top subsystems by frame time to the console, with their native read counts.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `count` | int |  | How many rows. Optional: 20 when left out. |
| `reads` | string |  | The word reads breaks the rows down by reads instead. Optional. |

```text
ISXOgreEQ2.PulseProf:Report[40,reads]
```

### `Reset`

`ISXOgreEQ2.PulseProf:Reset`

Resets the counters.

```text
ISXOgreEQ2.PulseProf:Reset
```

### `Scans`

`ISXOgreEQ2.PulseProf:Scans[what]`

Actor lookups by call site and by filter: prints the report, or controls it with reset, on or off.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `what` | string |  | A number of rows for the report, or reset, on or off. Optional: 20 rows when left out. |

```text
ISXOgreEQ2.PulseProf:Scans[reset]
```
