<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# ISXOgreEQ2.TaskRunner

## Methods

### `Clear`

`ISXOgreEQ2.TaskRunner:Clear[toon,task]`

Clears error and backoff records and saves them. Last-completed stamps are left alone.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `toon` | string |  | Only this character. Optional: with none, every character. |
| `task` | string |  | Only this task. Optional. |

```text
ISXOgreEQ2.TaskRunner:Clear[Bob,packpony]
```

### `Close`

`ISXOgreEQ2.TaskRunner:Close`

Closes the Lists window and leaves a run going. :End stops it too.

```text
ISXOgreEQ2.TaskRunner:Close
```

### `End`

`ISXOgreEQ2.TaskRunner:End`

Stops a run and closes the Lists window, the same as `ogre end taskrunner` and the window's X.

```text
ISXOgreEQ2.TaskRunner:End
```

### `Lists`

`ISXOgreEQ2.TaskRunner:Lists`

Prints the configured lists and their characters to the console.

```text
ISXOgreEQ2.TaskRunner:Lists
```

### `Now`

`ISXOgreEQ2.TaskRunner:Now`

Scans for due work now rather than at the next interval. Only while the runner is idle.

```text
ISXOgreEQ2.TaskRunner:Now
```

### `Open`

`ISXOgreEQ2.TaskRunner:Open`

Opens the TaskRunner Lists window, the same as bare `ogre taskrunner`.

```text
ISXOgreEQ2.TaskRunner:Open
```

### `Plan`

`ISXOgreEQ2.TaskRunner:Plan[list]`

Prints what is due to the console.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `list` | string |  | Only this list. Optional: with none, the list this session runs. |

```text
ISXOgreEQ2.TaskRunner:Plan[daily]
```

### `Reload`

`ISXOgreEQ2.TaskRunner:Reload`

Reads the config again. Refused while a batch is in flight; if the list you are on is gone, the run stops.

```text
ISXOgreEQ2.TaskRunner:Reload
```

### `Run`

`ISXOgreEQ2.TaskRunner:Run[list,options]`

Starts this session on one list, the same as `ogre taskrunner run <list>` and `ogre taskrunner -list <list>`. An unknown option, or no list, prints one warning and nothing starts.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `list` | string |  | The list's name, after an optional -list or -l; required. |
| `options` | string |  | once or loop, stagger or nostagger, with or without a leading dash, one argument each. Optional. |

```text
ISXOgreEQ2.TaskRunner:Run[daily,once]
```

### `Start`

`ISXOgreEQ2.TaskRunner:Start`

Starts cycling all configured characters. Refused while a batch is in flight, when the config is off, with no characters, or when lists exist and none was named: use :Run then.

```text
ISXOgreEQ2.TaskRunner:Start
```

### `Status`

`ISXOgreEQ2.TaskRunner:Status`

Prints what the runner is doing to the console.

```text
ISXOgreEQ2.TaskRunner:Status
```

### `Stop`

`ISXOgreEQ2.TaskRunner:Stop`

Stops a run and leaves the window up.

```text
ISXOgreEQ2.TaskRunner:Stop
```
