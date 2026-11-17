<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# ISXOgreEQ2.EffectTracker

## Methods

### `Bench`

`ISXOgreEQ2.EffectTracker:Bench`

Times the reads of the open examine window and prints the result.

```text
ISXOgreEQ2.EffectTracker:Bench
```

### `Close`

`ISXOgreEQ2.EffectTracker:Close`

Closes the window and leaves the captures as they are. :End disarms them too.

```text
ISXOgreEQ2.EffectTracker:Close
```

### `CloseWindow`

`ISXOgreEQ2.EffectTracker:CloseWindow[word]`

Closes the top examine window. They stack, so all closes the whole stack, up to 12.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `word` | string |  | all closes every one. Optional. |

```text
ISXOgreEQ2.EffectTracker:CloseWindow[all]
```

### `Demo`

`ISXOgreEQ2.EffectTracker:Demo`

Fills the window with sample data and opens it, for looking at the layout. Nothing is saved.

```text
ISXOgreEQ2.EffectTracker:Demo
```

### `Describe`

`ISXOgreEQ2.EffectTracker:Describe[state]`

Turns the Description capture on or off and prints the status. On, each new effect costs one server read, once ever; off, only Description is lost.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `state` | string |  | on or off. Optional: anything but off, or nothing, turns it on. |

```text
ISXOgreEQ2.EffectTracker:Describe[off]
```

### `End`

`ISXOgreEQ2.EffectTracker:End`

Disarms both captures, which saves them, and closes the window, the same as `ogre end effecttracker` and the window's X.

```text
ISXOgreEQ2.EffectTracker:End
```

### `Merge`

`ISXOgreEQ2.EffectTracker:Merge`

Merges this zone's temporary capture files into the dataset and prints the result.

```text
ISXOgreEQ2.EffectTracker:Merge
```

### `Npc`

`ISXOgreEQ2.EffectTracker:Npc[state]`

Arms or disarms the NPC effect capture and prints the status.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `state` | string |  | on or off. Optional: anything but off, or nothing, turns it on. |

```text
ISXOgreEQ2.EffectTracker:Npc[on]
```

### `Off`

`ISXOgreEQ2.EffectTracker:Off`

Disarms both captures and prints the status. The window stays up.

```text
ISXOgreEQ2.EffectTracker:Off
```

### `On`

`ISXOgreEQ2.EffectTracker:On`

Arms the player capture and prints the status.

```text
ISXOgreEQ2.EffectTracker:On
```

### `Open`

`ISXOgreEQ2.EffectTracker:Open`

Opens the Effect Tracker window, the same as bare `ogre effecttracker`.

```text
ISXOgreEQ2.EffectTracker:Open
```

### `Probe`

`ISXOgreEQ2.EffectTracker:Probe`

Prints what the open examine window reports to the console and leaves the window open.

```text
ISXOgreEQ2.EffectTracker:Probe
```

### `Reload`

`ISXOgreEQ2.EffectTracker:Reload`

Discards what is in memory and reads the dataset from disk again.

```text
ISXOgreEQ2.EffectTracker:Reload
```

### `Status`

`ISXOgreEQ2.EffectTracker:Status`

Prints what is armed and what has been captured to the console.

```text
ISXOgreEQ2.EffectTracker:Status
```

### `Trace`

`ISXOgreEQ2.EffectTracker:Trace[state]`

Turns tracing on or off: with it on, every admit, fire and drain decision goes to the log.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `state` | string |  | on or off. Optional: anything but off, or nothing, turns it on. |

```text
ISXOgreEQ2.EffectTracker:Trace[on]
```

### `UiDiag`

`ISXOgreEQ2.EffectTracker:UiDiag[word]`

Asks the panel what state it is in and prints the answer to the console.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `word` | string |  | expand also expands a row first. Optional. |

```text
ISXOgreEQ2.EffectTracker:UiDiag[expand]
```
