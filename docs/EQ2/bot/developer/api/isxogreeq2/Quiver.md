# ISXOgreEQ2.Quiver

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Members

### `Running`

`${ISXOgreEQ2.Quiver.Running}`

TRUE while a quiver refill is moving ammo out of your bags, or while the ammo depot pull it started is still running. A depot errand started by something else does not count.

**Returns:** bool: TRUE while either half of a quiver refill runs; FALSE when idle.

```text
echo ${ISXOgreEQ2.Quiver.Running}
```

### `Status`

`${ISXOgreEQ2.Quiver.Status}`

Progress of a quiver refill: the bag half with its count, then the ammo depot pull while that runs.

**Returns:** string: "idle", "filling from bags (done/total)", "arming the depot pull" or "pulling ammo from the depot".

```text
echo ${ISXOgreEQ2.Quiver.Status}
```

## Methods

### `Refill`

`ISXOgreEQ2.Quiver:Refill`

The engine behind `ogre quiver` and the quiver step of the Inventory Manager chain: moves matching ammo from your bags into the equipped quiver or pouch (1 s apart, 2 s in combat), then, in a guild hall, tops it up from the ammo depot, warning and stopping when no ammo container is equipped or the ammo kind cannot be told. To tell arrows, bolts or thrown ammo it makes ONE SERVER CALL (the equipped ranged weapon's `.ToItemInfo.SubType`, only when that item's info is already available), then falls back to what is in the container, then to the container's name.

```text
ISXOgreEQ2.Quiver:Refill
```

### `Stop`

`ISXOgreEQ2.Quiver:Stop`

Stops both halves of a quiver refill, the bag moves and the ammo depot pull it started, and prints "quiver: stopped.". Prints nothing when neither half is running; it is the same stop `ogre end quiver` uses.

```text
ISXOgreEQ2.Quiver:Stop
```
