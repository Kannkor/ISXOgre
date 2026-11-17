# ISXOgreEQ2.LevelTransmuting

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Methods

### `End`

`ISXOgreEQ2.LevelTransmuting:End`

Stops a run and closes the panel, the same as `ogre end leveltransmuting` and the panel's X. It takes no arguments.

```text
ISXOgreEQ2.LevelTransmuting:End
```

### `Help`

`ISXOgreEQ2.LevelTransmuting:Help`

Prints the `ogre leveltransmuting` usage to the console.

```text
ISXOgreEQ2.LevelTransmuting:Help
```

### `Off`

`ISXOgreEQ2.LevelTransmuting:Off`

Stops a run and leaves the panel up. It takes no arguments.

```text
ISXOgreEQ2.LevelTransmuting:Off
```

### `On`

`ISXOgreEQ2.LevelTransmuting:On[count,rounds]`

Starts a run: buys stones and transmutes them until the rounds are used up. A bad value prints why and the usage.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `count` | int |  | Stones to hold per merchant visit, 1 to 800. Optional: 60 when left out. |
| `rounds` | int |  | The hard stop, 1 to 500. Optional: 20 when left out. |

```text
ISXOgreEQ2.LevelTransmuting:On[60,20]
```

### `Open`

`ISXOgreEQ2.LevelTransmuting:Open`

Opens or refreshes the Level Transmuting panel, the same as bare `ogre lt`. It takes no arguments.

```text
ISXOgreEQ2.LevelTransmuting:Open
```

### `Status`

`ISXOgreEQ2.LevelTransmuting:Status`

Prints the run's state and usage to the console. It takes no arguments.

```text
ISXOgreEQ2.LevelTransmuting:Status
```
