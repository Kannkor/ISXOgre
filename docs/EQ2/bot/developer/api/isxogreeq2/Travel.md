<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# ISXOgreEQ2.Travel

## Methods

### `End`

`ISXOgreEQ2.Travel:End`

Stops a list it is opening and reading and closes the window, the same as `ogre end travel` and the window's X. A pick already sent is the group's travel and goes on.

```text
ISXOgreEQ2.Travel:End
```

### `Help`

`ISXOgreEQ2.Travel:Help`

Prints the `ogre travel` usage to the console.

```text
ISXOgreEQ2.Travel:Help
```

### `Open`

`ISXOgreEQ2.Travel:Open[method]`

Opens the Travel Helper window, and with a method also lists that map's destinations. An unknown method prints a warning and still opens the window.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `method` | string |  | fast, spire, druid, bell or map. Optional: leave it out to only open the window. |

```text
ISXOgreEQ2.Travel:Open[spire]
```
