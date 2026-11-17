# ISXOgreEQ2.HideEffects

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Methods

### `Clear`

`ISXOgreEQ2.HideEffects:Clear`

Un-hides every hidden effect on this client.

```text
ISXOgreEQ2.HideEffects:Clear
```

### `Delete`

`ISXOgreEQ2.HideEffects:Delete[id]`

Un-hides one effect by its id. With no id, or one that is not a positive number, it prints a line and changes nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `id` | int64 |  | The effect id, as the game's hidden list shows it. |

```text
ISXOgreEQ2.HideEffects:Delete[123456]
```

### `End`

`ISXOgreEQ2.HideEffects:End`

Stops a run and closes the panel, the same as `ogre end hideeffects` and the panel's X. What is already hidden stays hidden.

```text
ISXOgreEQ2.HideEffects:End
```

### `List`

`ISXOgreEQ2.HideEffects:List`

Asks the game to print its list of hidden effects in the EQ2 chat window.

```text
ISXOgreEQ2.HideEffects:List
```

### `Open`

`ISXOgreEQ2.HideEffects:Open`

Opens the Hide Effects panel.

```text
ISXOgreEQ2.HideEffects:Open
```

### `Reload`

`ISXOgreEQ2.HideEffects:Reload`

Re-reads the effect list from disk, off the pulse.

```text
ISXOgreEQ2.HideEffects:Reload
```

### `Reset`

`ISXOgreEQ2.HideEffects:Reset`

Removes your custom additions to the effect list.

```text
ISXOgreEQ2.HideEffects:Reset
```

### `Run`

`ISXOgreEQ2.HideEffects:Run`

Runs the hide pass now: walks your effects and hides everything the list claims for your class, the same as bare `ogre hideeffects`.

```text
ISXOgreEQ2.HideEffects:Run
```

### `Status`

`ISXOgreEQ2.HideEffects:Status`

Prints what is loaded, what applies to this character and how the last run went to the console. It makes no server call.

```text
ISXOgreEQ2.HideEffects:Status
```
