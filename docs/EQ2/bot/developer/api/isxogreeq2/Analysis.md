# ISXOgreEQ2.Analysis

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Methods

### `Close`

`ISXOgreEQ2.Analysis:Close`

Closes the window and leaves everything running. :End stops it too.

```text
ISXOgreEQ2.Analysis:Close
```

### `Demo`

`ISXOgreEQ2.Analysis:Demo`

Fills the window with sample data and opens it, for looking at the layout. Nothing is saved.

```text
ISXOgreEQ2.Analysis:Demo
```

### `End`

`ISXOgreEQ2.Analysis:End`

Turns the monitor and the taps off, drops a scan in progress, a + Cursor countdown and the spawn watch, and closes the window, the same as `ogre end analysis` and the window's X. What was recorded stays.

```text
ISXOgreEQ2.Analysis:End
```

### `Export`

`ISXOgreEQ2.Analysis:Export[name]`

Saves the monitored actors and scan results to a file and says where.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | string |  | The file name. Optional: with none it is session_ and the date and time. |

```text
ISXOgreEQ2.Analysis:Export["My Run"]
```

### `Import`

`ISXOgreEQ2.Analysis:Import[name]`

Loads a saved session, replacing what is in memory and stopping live monitoring. With no name, or one that cannot be read, it prints one warning and changes nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | string |  | A session name from :Sessions, or a path; required. |

```text
ISXOgreEQ2.Analysis:Import["My Run"]
```

### `Monitor`

`ISXOgreEQ2.Analysis:Monitor[word,actor]`

The monitor: starts or stops sampling, empties or prints the list, or adds or removes an actor. With no word, or another word, it prints one warning listing the words.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `word` | string |  | on and off start and stop sampling, clear empties the list, list prints it, add and remove take an actor; required. |
| `actor` | string |  | For add and remove: an actor id, or target or cursor for the actor you have targeted or are pointing at. |

```text
ISXOgreEQ2.Analysis:Monitor[add,target]
```

### `Open`

`ISXOgreEQ2.Analysis:Open`

Opens the Analysis window, the same as bare `ogre analysis`.

```text
ISXOgreEQ2.Analysis:Open
```

### `Rate`

`ISXOgreEQ2.Analysis:Rate[ms]`

Sets how often monitored actors are sampled. A value outside 100 to 10000, or none, prints one warning and changes nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `ms` | int |  | Milliseconds between samples, 100 to 10000; the default is 250; required. |

```text
ISXOgreEQ2.Analysis:Rate[500]
```

### `Scan`

`ISXOgreEQ2.Analysis:Scan[terms]`

Snapshots the actors that match, reusing the window's terms if you give none; with none there either it scans the whole zone. It refuses to start while a scan runs or out of the world.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `terms` | string |  | Terms like Level>120: a member, then =, &lt; or >, then a value, one argument each; a term that does not read that way prints a warning and is skipped. Optional. |

```text
ISXOgreEQ2.Analysis:Scan["Level>120"]
```

### `Sessions`

`ISXOgreEQ2.Analysis:Sessions`

Prints the names of the saved sessions to the console.

```text
ISXOgreEQ2.Analysis:Sessions
```

### `Status`

`ISXOgreEQ2.Analysis:Status`

Prints the monitor, taps, scan and sample counters to the console, with the last error if there is one.

```text
ISXOgreEQ2.Analysis:Status
```

### `Taps`

`ISXOgreEQ2.Analysis:Taps[state]`

Turns the passive event logs on or off and prints the status.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `state` | string |  | on or off. Optional: anything but off, or nothing, turns it on. |

```text
ISXOgreEQ2.Analysis:Taps[on]
```
