# ISXOgreEQ2.Scheduler

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Members

### `Active`

`${ISXOgreEQ2.Scheduler.Active[key]}`

Whether a timer with this key still has a fire pending. Keys ignore case; a one-shot timer reads FALSE once it has fired.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `key` | string |  | the timer's key (its event name unless it was armed with -key) |

**Returns:** bool: TRUE when a fire is still pending for this key; FALSE when there is no such timer.

```text
echo ${ISXOgreEQ2.Scheduler.Active[MyTimerEvent]}
```

### `Count`

`${ISXOgreEQ2.Scheduler.Count}`

How many keyed timers are pending in the scheduler. The encounter engine's timers live in the same table, so they count too.

**Returns:** int: number of pending keyed timers.

```text
echo ${ISXOgreEQ2.Scheduler.Count}
```

### `Remaining`

`${ISXOgreEQ2.Scheduler.Remaining[key]}`

Milliseconds until the next fire of the timer with this key. Reads 0 when there is no such timer or it is due now.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `key` | string |  | the timer's key (its event name unless it was armed with -key) |

**Returns:** int64: milliseconds to the next fire; 0 when there is no such timer or it is due.

```text
echo ${ISXOgreEQ2.Scheduler.Remaining[MyTimerEvent]}
```

## Methods

### `Cancel`

`ISXOgreEQ2.Scheduler:Cancel[key]`

Stops the timer with this key before it fires again. Keys ignore case, and a key with no timer does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `key` | string |  | the timer's key (its event name unless it was armed with -key) |

```text
ISXOgreEQ2.Scheduler:Cancel[MyTimerEvent]
```

### `ClearNonPersistent`

`ISXOgreEQ2.Scheduler:ClearNonPersistent`

Cancels every script and encounter timer that was not armed with -persistent, and leaves the bot's own pending delayed casts and actions. Finishing a zone clears every non-persistent timer, the bot's included.

```text
ISXOgreEQ2.Scheduler:ClearNonPersistent
```

### `FireEvent`

`ISXOgreEQ2.Scheduler:FireEvent[delay,eventName,payload,-persistent,-key]`

Fires the LavishScript event eventName once after the delay, always with exactly one argument (the payload, or an empty string). Arming a key that is already pending replaces that timer, and unless -persistent is given the timer is dropped when you finish zoning; a bad delay such as 30x fires nothing and warns on the console.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `delay` | string |  | how long to wait: a whole number of milliseconds, or a number with ms, s, m or h (30s, 1.5s, 2m) |
| `eventName` | string |  | the LavishScript event to fire |
| `payload` | string | `""` | the one argument passed to the event; the first extra word not starting with a dash |
| `-persistent` | switch | `off` | keep the timer across zoning |
| `-key` | switch | `the event name` | -key &lt;k>: the timer's key, case-insensitive |

```text
ISXOgreEQ2.Scheduler:FireEvent[5s,MyTimerEvent,hello]
```

### `FireEventEvery`

`ISXOgreEQ2.Scheduler:FireEventEvery[interval,eventName,repeats,payload,-persistent,-key]`

Fires the LavishScript event eventName every interval, repeats times, always with exactly one argument (the payload, or an empty string); a missing, 0 or negative repeats means forever. Re-arming a pending key replaces it, and unless -persistent is given the timer is dropped when you finish zoning; a bad interval fires nothing and warns on the console.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `interval` | string |  | time between fires: a whole number of milliseconds, or a number with ms, s, m or h; the first fire comes one interval after the call |
| `eventName` | string |  | the LavishScript event to fire |
| `repeats` | int | `forever` | how many times to fire; 0 or less fires until cancelled |
| `payload` | string | `""` | the one argument passed to the event; the first extra word not starting with a dash |
| `-persistent` | switch | `off` | keep the timer across zoning |
| `-key` | switch | `the event name` | -key &lt;k>: the timer's key, case-insensitive |

```text
ISXOgreEQ2.Scheduler:FireEventEvery[10s,MyTimerEvent,6,tick]
```

### `Spew`

`ISXOgreEQ2.Scheduler:Spew`

Prints every pending keyed timer to the console, the encounter engine's included: a count line, then one line per timer with its key, event, milliseconds to the next fire, how many times it has fired, and whether it is persistent.

```text
ISXOgreEQ2.Scheduler:Spew
```
