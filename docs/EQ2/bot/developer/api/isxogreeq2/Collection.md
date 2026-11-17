<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# ISXOgreEQ2.Collection

## Members

### `Running`

`${ISXOgreEQ2.Collection.Running}`

TRUE while an `ogre cm` collection run is in progress, from the depot or from your bags. Starting another while one runs is refused with a busy warning.

**Returns:** bool: TRUE while a collection run is going; FALSE when idle.

```text
echo ${ISXOgreEQ2.Collection.Running}
```

### `Status`

`${ISXOgreEQ2.Collection.Status}`

Progress of the running collection run, or "idle". It is the same text `${ISXOgreEQ2.Collection}` returns.

**Returns:** string: "idle", "cm (done/total, n added)" for a depot run or "cm -inventory (done/total, n added)" for a bag scan.

```text
echo ${ISXOgreEQ2.Collection.Status}
```

## Methods

### `Run`

`ISXOgreEQ2.Collection:Run[flags...]`

The engine behind `ogre cm`: opens the collectible depot within 10 m, turns Hide Grey on, then withdraws each listed piece one at a time, examines it and clicks the quest journal's Add button; the final result line goes to OgreConsole prefixed with your name. With -inventory it scans your bags instead and MAKES A SERVER CALL PER ITEM (`.ToItemInfo.IsCollectible` and `.AlreadyCollected`, waiting up to 5 s for each item's info), so it is slow.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `flags...` | string |  | none = the nearest depot whose name contains Collectible Depot, else a Personal Collectible Stash; -small = exactly Collectible Depot; -large = exactly Collectible Depot (Large) (a named depot that is not found refuses the call); -inventory (also 1 or -1) scans your bags instead; unknown words are ignored |

```text
ISXOgreEQ2.Collection:Run[-large]
```

### `Stop`

`ISXOgreEQ2.Collection:Stop`

Stops a running collection run, closes the depot window if it is open and prints "cm: stopped.". Does nothing when idle.

```text
ISXOgreEQ2.Collection:Stop
```
