# OgreBotAPI.Paths

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Members

### `Count`

`${OgreBotAPI.Paths.Count}`

How many saved paths the zone you are in has. It reads 0 in a zone with none, while you are not settled in a zone and while the travel data loads.

**Returns:** int: the current zone's saved paths.

```text
echo ${OgreBotAPI.Paths.Count}
```

### `Running`

`${OgreBotAPI.Paths.Running}`

TRUE while a path is being walked on this character, a Paths:Start walk or AutoHunt's. It is FALSE again once the walk finishes, is stopped or ends at a zone.

**Returns:** bool: TRUE while a walk is in flight on this character.

```text
echo ${OgreBotAPI.Paths.Running}
```

## Methods

### `AddPoint`

`OgreBotAPI.Paths:AddPoint[fw, name, point]`

Adds a point to the end of a saved path of the zone you are in, and a new name makes the path, walked by nav with no loop. A POI name is not looked up here, so its POI can come later: Paths:Start checks every point.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on. Paths are shared by every box on the PC, so a line that reaches several boxes names one, or each box it lands on does it. |
| `name` | string |  | The path's name, in any case. |
| `point` | string |  | A POI name, or x,y,z. A script that writes x,y,z without quotes gets the same point. |

```text
OgreBotAPI.Paths:AddPoint[${Me.Name},autohuntpath1,bell]
```

*Was (OldBot):* `OgreBotAPI:AutoHunt_AddPath`, `OgreBotAPI:AutoHunt_AddPoint`

### `Clear`

`OgreBotAPI.Paths:Clear[fw, name]`

Takes every point off a saved path of the zone you are in. The path stays, with its mover and its loop setting.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on. Paths are shared by every box on the PC, so a line that reaches several boxes names one, or each box it lands on does it. |
| `name` | string |  | The path's name, in any case. |

```text
OgreBotAPI.Paths:Clear[${Me.Name},autohuntpath1]
```

*Was (OldBot):* `OgreBotAPI:AutoHunt_ClearPoints`

### `Delete`

`OgreBotAPI.Paths:Delete[fw, name]`

Deletes a saved path of the zone you are in. An unknown name prints one line and changes nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on. Paths are shared by every box on the PC, so a line that reaches several boxes names one, or each box it lands on does it. |
| `name` | string |  | The path's name, in any case. |

```text
OgreBotAPI.Paths:Delete[${Me.Name},autohuntpath1]
```

### `InsertPoint`

`OgreBotAPI.Paths:InsertPoint[fw, name, at, point]`

Puts a point into a saved path of the zone you are in at a place in the list, and the point at that place and the ones after it move down one. An unknown path, a place outside the list or a point that cannot be one prints one line and changes nothing, and a walk under way keeps the points it had at its Start.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on. Paths are shared by every box on the PC, so a line that reaches several boxes names one, or each box it lands on does it. |
| `name` | string |  | The path's name, in any case. It must exist: a place is a place in a list, so this never makes a path. |
| `at` | number |  | The place the point takes, counted from 1. One past the last point puts it on the end. |
| `point` | string |  | A POI name, or x,y,z. A script that writes x,y,z without quotes gets the same point. |

```text
OgreBotAPI.Paths:InsertPoint[${Me.Name},autohuntpath1,2,bell]
```

### `MovePoint`

`OgreBotAPI.Paths:MovePoint[fw, name, from, to]`

Moves a point of a saved path of the zone you are in to another place in the list, and the points between shift one place. An unknown path or a place outside the list prints one line and changes nothing, and a walk under way keeps the points it had at its Start.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on. Paths are shared by every box on the PC, so a line that reaches several boxes names one, or each box it lands on does it. |
| `name` | string |  | The path's name, in any case. |
| `from` | number |  | The place of the point to move, counted from 1. |
| `to` | number |  | The place it ends at, counted from 1. Moving a point to the place it holds changes nothing. |

```text
OgreBotAPI.Paths:MovePoint[${Me.Name},autohuntpath1,5,2]
```

### `RemovePoint`

`OgreBotAPI.Paths:RemovePoint[fw, name, point]`

Takes the first point of that text off a saved path of the zone you are in, so a path that passes a point twice keeps the later one. An unknown path or point prints one line and changes nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on. Paths are shared by every box on the PC, so a line that reaches several boxes names one, or each box it lands on does it. |
| `name` | string |  | The path's name, in any case. |
| `point` | string |  | The point as the path holds it, in any case: a POI name, or x,y,z. |

```text
OgreBotAPI.Paths:RemovePoint[${Me.Name},autohuntpath1,bell]
```

*Was (OldBot):* `OgreBotAPI:AutoHunt_RemovePoint`

### `Start`

`OgreBotAPI.Paths:Start[fw, name]`

Walks a saved path of the zone you are in, point by point, by the path's own mover, in place of any walk under way and through a pause of OgreBot; a point that does not resolve stops it before anything moves, and OgreBot must be open. It waits while something else has the character (a fight, a death, an AutoHunt pull, a movement block) and goes on from the same point, and one line says when it finishes, cannot reach a point, or ends at a zone or OgreBot closing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `name` | string |  | The path's name, in any case. A path of one point goes there and finishes, looping or not. A path walked by camp spot leaves the camp spot at its last point when it finishes, and no earlier camp spot comes back. |

```text
OgreBotAPI.Paths:Start[${Me.Name},autohuntpath1]
```

### `Stop`

`OgreBotAPI.Paths:Stop[fw]`

Stops the path being walked, a Paths:Start walk or AutoHunt's: the character stands where it is, and a walk by camp spot has its camp spot cleared. With no walk it prints one line.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.Paths:Stop[${Me.Name}]
```
