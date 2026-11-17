# ISXOgreEQ2.Tour

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Methods

### `Close`

`ISXOgreEQ2.Tour:Close`

Closes the New User Tour window, and its intro if that is still playing. The tour is not marked as seen, so it opens by itself again on the next load.

```text
ISXOgreEQ2.Tour:Close
```

### `Done`

`ISXOgreEQ2.Tour:Done`

Marks the New User Tour finished: prints 'tour: completed', saves it as seen so it no longer opens on load, and closes the window, then starts the Migration Assistant's automatic run, which copies any OldBot settings files that have no new copy yet and shows a progress window only when something is copied. A call when the tour is not open does nothing.

```text
ISXOgreEQ2.Tour:Done
```

### `Open`

`ISXOgreEQ2.Tour:Open`

Opens the New User Tour, the same as `ogre tour`: a short walkthrough of three window controls (drag to resize, right-click the title bar, Save Position), which also opens by itself on first load until it has been finished or skipped. It hides the InnerSpace console if that is showing and prints 'tour opened', and it does nothing while the tour is already up.

```text
ISXOgreEQ2.Tour:Open
```

### `Skip`

`ISXOgreEQ2.Tour:Skip`

Skips the New User Tour: prints 'tour: skipped', saves it as seen so it no longer opens on load, closes the window and, like Tour:Done, starts the Migration Assistant's automatic run of any OldBot settings not yet copied. A call when the tour is not open does nothing.

```text
ISXOgreEQ2.Tour:Skip
```

### `Step`

`ISXOgreEQ2.Tour:Step[step]`

Called by the tour window when it moves to a new step, and all it does is print 'tour: advanced to step N' to the console. Nothing is saved and the tour window does not change, so a script has no reason to call it.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `step` | int | `0` | the step number to print (the tour has steps 1 to 3); text that is not a number prints 0 |

```text
ISXOgreEQ2.Tour:Step[2]
```
