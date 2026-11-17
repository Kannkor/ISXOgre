<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# ISXOgreEQ2.OSA

## Methods

### `Close`

`ISXOgreEQ2.OSA:Close`

Closes the On-Screen Assistant window and stops its NPC scan, including an open that is still being retried. It does not untick the Enable On-Screen Assistant setting, so the window opens again only when that setting is next switched on (or at the next load while it is ticked).

```text
ISXOgreEQ2.OSA:Close
```

### `Open`

`ISXOgreEQ2.OSA:Open`

Opens the On-Screen Assistant (OSA) window, the same as `ogre osa`: a live list of the NPCs around you, named NPCs first and then by distance, up to 35 rows, refreshed about 5 times a second within the Settings scan radius (50 until a value is set, at most 200). It does nothing while the window is already up, and it does not tick the Enable On-Screen Assistant setting, which opens and closes the window by itself whenever it changes.

```text
ISXOgreEQ2.OSA:Open
```

### `Target`

`ISXOgreEQ2.OSA:Target[id]`

Targets the actor with the given ID at once by sending the `target <id>` command, which is what clicking a row in the OSA window does. A call with no ID prints a line and targets nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `id` | int |  | ID of the actor to target |

```text
ISXOgreEQ2.OSA:Target[${Target.Target.ID}]
```
