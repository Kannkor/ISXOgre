<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# ISXOgreEQ2.Targeting

## Members

### `ActiveList`

`${ISXOgreEQ2.Targeting.ActiveList}`

The name of the saved auto-target list last loaded or saved into the working list, like OgreBotAPI.AutoTarget.ListName. Reading it also refreshes the saved-list catalogue for the current zone.

**Returns:** string: the saved-list name; "" when none is loaded or when not in the world.

```text
echo ${ISXOgreEQ2.Targeting.ActiveList}
```

### `AssistId`

`${ISXOgreEQ2.Targeting.AssistId}`

The assist decision as one number, read fresh on each call - the same call as OgreBotAPI.Assist.TargetID. It answers even when the Auto Assist box is off.

**Returns:** int64: greater than 0 is the ID this character would target; 0 when it picks its own target; -1 when its current target should be left alone; NULL when not in the world.

```text
echo ${ISXOgreEQ2.Targeting.AssistId}
```

### `Enabled`

`${ISXOgreEQ2.Targeting.Enabled}`

Whether either targeting engine is switched on: the Auto Assist box or the auto-target box. This is not OgreBotAPI.AutoTarget.Enabled, which reads only the auto-target box.

**Returns:** bool: TRUE when the Auto Assist box or the auto-target box is ticked; FALSE when both are off.

```text
echo ${ISXOgreEQ2.Targeting.Enabled}
```

### `InControl`

`${ISXOgreEQ2.Targeting.InControl}`

Whether this character picks its own target instead of following someone else's - the same call as OgreBotAPI.Assist.InControl. With the Auto Assist box off it reads TRUE.

**Returns:** bool: TRUE when this character picks its own target; FALSE when it follows another player, and FALSE when not in the world.

```text
echo ${ISXOgreEQ2.Targeting.InControl}
```

### `SavedList`

`${ISXOgreEQ2.Targeting.SavedList[index]}`

The name of one saved auto-target list for the current zone, counting from 1 in file order, the same as OgreBotAPI.AutoTarget.SavedName.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `index` | int |  | Which saved list, counting from 1. 0, or text that is not a number, reads empty. |

**Returns:** string: the saved list's name; "" when index is 0 or past the count, when no index is given, or when not in the world.

```text
echo ${ISXOgreEQ2.Targeting.SavedList[1]}
```

### `SavedListCount`

`${ISXOgreEQ2.Targeting.SavedListCount}`

The number of saved auto-target lists for the current zone, like OgreBotAPI.AutoTarget.SavedCount. Unlike that member it reloads the zone's catalogue first when the zone has changed, so it never shows the previous zone.

**Returns:** int: the number of saved lists; 0 when the zone has none or when not in the world.

```text
echo ${ISXOgreEQ2.Targeting.SavedListCount}
```

## Methods

### `ClearList`

`ISXOgreEQ2.Targeting:ClearList`

Empties the working auto-target list and blanks ActiveList - OgreBotAPI.AutoTarget:Clear without the for-who. Auto-target then falls back to the profile's own AutoTarget entries (nothing to pick if it has none) until a list is loaded or entries are added, and saved lists on disk are not touched.

```text
ISXOgreEQ2.Targeting:ClearList
```

### `LoadList`

`ISXOgreEQ2.Targeting:LoadList[<name>]`

Replaces the working auto-target list with the saved list of that name for the current zone (the name is matched ignoring case) - OgreBotAPI.AutoTarget:LoadSaved without the for-who. If the zone has no list by that name, or you are not in the world, nothing changes and nothing is printed.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `<name>` | string |  | The saved list's name. |

```text
ISXOgreEQ2.Targeting:LoadList[Trash]
```

### `Status`

`ISXOgreEQ2.Targeting:Status`

Prints the assist state to this character's console, the same as `ogre assist`: the Auto Assist, auto-target and direct targeting boxes, the decision and why, the assist anchor, each assist-list entry with their target, and your own target. Prints nothing when not in the world.

```text
ISXOgreEQ2.Targeting:Status
```

### `Target`

`ISXOgreEQ2.Targeting:Target[id]`

Queues a one-time retarget to the actor ID, issued on the next pulse even while OgreBot is paused; it beats auto-target and assist but yields to a target lock or a manual target. It is skipped when that is already your target or is you, and does nothing without an ID.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `id` | int64 |  | The actor ID to target. |

```text
ISXOgreEQ2.Targeting:Target[${Target.ID}]
```

### `Tick`

`ISXOgreEQ2.Targeting:Tick`

Runs the assist and auto-target decision now and queues any retarget for the next pulse; it never targets during the call. The bot already does this on its own every 250 ms, and with auto-target on and entries to pick from each call can run a nearby-actor scan, so a script rarely needs it.

```text
ISXOgreEQ2.Targeting:Tick
```
