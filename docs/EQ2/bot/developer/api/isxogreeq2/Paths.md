# ISXOgreEQ2.Paths

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Methods

### `End`

`ISXOgreEQ2.Paths:End`

Closes the Points of Interest and Paths window, which is what `ogre end paths` and the window's X do. A path being walked goes on.

```text
ISXOgreEQ2.Paths:End
```

### `Open`

`ISXOgreEQ2.Paths:Open[path]`

Opens the Points of Interest and Paths window (the same as `ogre paths`), on a saved path of the zone you are in when you name one: this is the one way to open it, from a panel, a button or a script. A window already open comes to the front on that path, a path this zone does not have prints one line and the window opens with nothing picked, and without the Ogre UI desktop it prints a warning.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `path` | string | `none (nothing picked)` | The path to open on, in any case. A name with spaces may be quoted or written as several words. Leave it out to open the window with nothing picked. |

```text
ISXOgreEQ2.Paths:Open["North Loop"]
```
