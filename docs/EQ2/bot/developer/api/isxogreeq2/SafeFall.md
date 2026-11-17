# ISXOgreEQ2.SafeFall

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Methods

### `End`

`ISXOgreEQ2.SafeFall:End`

Stops the trainer and closes the window, the same as `ogre end safefall` and the window's X. It takes no arguments.

```text
ISXOgreEQ2.SafeFall:End
```

### `Help`

`ISXOgreEQ2.SafeFall:Help`

Prints the `ogre safefall` usage to the console.

```text
ISXOgreEQ2.SafeFall:Help
```

### `Off`

`ISXOgreEQ2.SafeFall:Off`

Stops the trainer on the next tick and leaves the window up. It takes no arguments.

```text
ISXOgreEQ2.SafeFall:Off
```

### `On`

`ISXOgreEQ2.SafeFall:On[ticks]`

Arms the trainer: on the next tick it flies up, falls and repeats, gaining flight time as it goes. Already running, it restarts; a bad value prints why and the usage.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `ticks` | int |  | Flight time in tenths of a second, 5 to 600. Optional: 30 when left out. |

```text
ISXOgreEQ2.SafeFall:On[45]
```

### `Open`

`ISXOgreEQ2.SafeFall:Open`

Opens the Safe Fall Trainer window. It takes no arguments.

```text
ISXOgreEQ2.SafeFall:Open
```

### `Status`

`ISXOgreEQ2.SafeFall:Status`

Prints the trainer's state and usage to the console, the same as bare `ogre safefall`. It takes no arguments.

```text
ISXOgreEQ2.SafeFall:Status
```
