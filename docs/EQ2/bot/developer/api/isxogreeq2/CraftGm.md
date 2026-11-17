# ISXOgreEQ2.CraftGm

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Methods

### `Close`

`ISXOgreEQ2.CraftGm:Close`

The same as :End: closing this window never leaves a run going. It takes no arguments.

```text
ISXOgreEQ2.CraftGm:Close
```

### `End`

`ISXOgreEQ2.CraftGm:End`

Stops a run and closes the window, the same as `ogre end craftgm` and the window's X. It takes no arguments.

```text
ISXOgreEQ2.CraftGm:End
```

### `Open`

`ISXOgreEQ2.CraftGm:Open[words]`

Opens the Craft Grandmasters window and does nothing else, the same as bare `ogre craftgm`. A word it cannot read prints why and the usage, and nothing changes.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `words` | string |  | A level range such as 131-135 or all, to seed the boxes, and depot or nodepot for the Scroll Depot box, one argument each. Optional. |

```text
ISXOgreEQ2.CraftGm:Open
```

### `Queue`

`ISXOgreEQ2.CraftGm:Queue[words]`

Opens the window, seeds it the same way, scans, then replaces the Ogre Craft queue with the Grandmaster recipes and stops - nothing is crafted, the Scroll Depot is never used, and the Craft window opens on the queue.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `words` | string |  | A level range, one argument. Optional. depot is refused: Queue never pulls from the Scroll Depot. |

```text
ISXOgreEQ2.CraftGm:Queue[131-135]
```

### `Scan`

`ISXOgreEQ2.CraftGm:Scan[words]`

Opens the window, seeds it the same way, and scans. It queues nothing and crafts nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `words` | string |  | A level range and depot or nodepot, one argument each. Optional. |

```text
ISXOgreEQ2.CraftGm:Scan[131-135,depot]
```

### `Start`

`ISXOgreEQ2.CraftGm:Start[words]`

Opens the window, seeds it the same way, then scans, queues and crafts.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `words` | string |  | A level range and depot or nodepot, one argument each. Optional. |

```text
ISXOgreEQ2.CraftGm:Start[all,nodepot]
```

### `Status`

`ISXOgreEQ2.CraftGm:Status`

Prints the state, filter, queue and Scroll Depot counters to the console. It takes no arguments.

```text
ISXOgreEQ2.CraftGm:Status
```

### `Stop`

`ISXOgreEQ2.CraftGm:Stop`

Stops a run and leaves the window as it is, so you can see what happened. It takes no arguments.

```text
ISXOgreEQ2.CraftGm:Stop
```
