<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# ISXOgreEQ2.PulseBudget

## Methods

### `Ceiling`

`ISXOgreEQ2.PulseBudget:Ceiling[us]`

Sets the shared frame ceiling and saves it; below 0 reads as 0. With no value it prints one warning and changes nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `us` | float |  | The ceiling in microseconds; 0 means none. |

```text
ISXOgreEQ2.PulseBudget:Ceiling[4000]
```

### `Close`

`ISXOgreEQ2.PulseBudget:Close`

Closes the Pulse Budget window, the same as `ogre end pulse`. The budget keeps running.

```text
ISXOgreEQ2.PulseBudget:Close
```

### `JobTest`

`ISXOgreEQ2.PulseBudget:JobTest[state]`

A test mode for this session only: every pulse job pauses at every checkpoint, so state that does not survive a frame shows up at once. It is never saved.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `state` | string |  | on or 1 turns it on; any other word turns it off. Required. |

```text
ISXOgreEQ2.PulseBudget:JobTest[on]
```

### `Off`

`ISXOgreEQ2.PulseBudget:Off`

Turns the shared frame ceiling off and saves it. Each section still keeps its own slice.

```text
ISXOgreEQ2.PulseBudget:Off
```

### `On`

`ISXOgreEQ2.PulseBudget:On`

Turns the shared frame ceiling on, resets the counters and saves it.

```text
ISXOgreEQ2.PulseBudget:On
```

### `Open`

`ISXOgreEQ2.PulseBudget:Open`

Opens the Pulse Budget window, the same as bare `ogre pulse`.

```text
ISXOgreEQ2.PulseBudget:Open
```

### `Report`

`ISXOgreEQ2.PulseBudget:Report`

Prints the per-section table to the console.

```text
ISXOgreEQ2.PulseBudget:Report
```

### `Reset`

`ISXOgreEQ2.PulseBudget:Reset`

Resets the counters.

```text
ISXOgreEQ2.PulseBudget:Reset
```

### `Slice`

`ISXOgreEQ2.PulseBudget:Slice[section,us]`

Sets how long a resumable section may run per frame and saves it; a slice paces the work and never skips any of it. A missing section or value prints one warning, and a section nothing matches prints another.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `section` | string |  | The section's name, or its number from :Report. |
| `us` | float |  | Microseconds per frame; 0 lets it run to completion. |

```text
ISXOgreEQ2.PulseBudget:Slice[3,200]
```
