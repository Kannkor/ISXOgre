<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# OgreBotAPI.Client

## Methods

### `ResetCamera`

`OgreBotAPI.Client:ResetCamera[fw]`

Recentres the camera: in first person it uses the game's camera recentre, otherwise it sets the camera pitch to 0 the way Client:SetCameraPitch does. While a camera pitch from Client:SetCameraPitch is still running, the pitch is not changed and one line says so.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Client:ResetCamera[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:ResetCameraAngle`, `call Obj_OgreUtilities.ResetCameraAngle`

### `SetCameraPitch`

`OgreBotAPI.Client:SetCameraPitch[fw, pitch=0, endInFirstPerson=FALSE]`

Queued: switches to third person if needed, sets the camera pitch, and goes back to first person when endInFirstPerson is TRUE. A pitch outside -75 to 75, or a call while one is still running, prints a console line and is dropped.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `pitch` | int | `0` | Camera pitch from -75 to 75; 0 is level |
| `endInFirstPerson` | bool | `FALSE` | TRUE to switch to first person after setting the pitch |

```text
OgreBotAPI.Client:SetCameraPitch[${Me.Name},-20,FALSE]
```

*Was (OldBot):* `OgreBotAPI:Set_CameraPitch`, `call Obj_OgreUtilities.Set_LookDown`, `call Obj_OgreUtilities.Set_LookUp`

### `SetMousePosition`

`OgreBotAPI.Client:SetMousePosition[fw, x, y]`

Moves the mouse cursor to x,y with Inner Space's Mouse:SetPosition, right away. A missing x or y prints "Client:SetMousePosition needs fw,X,Y" and does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `x` | int |  | Horizontal position in pixels |
| `y` | int |  | Vertical position in pixels |

```text
OgreBotAPI.Client:SetMousePosition[${Me.Name},800,450]
```

*Was (OldBot):* `OgreBotAPI:SetMousePosition`

### `SetMousePositionMiddle`

`OgreBotAPI.Client:SetMousePositionMiddle[fw]`

Moves the mouse cursor to the centre of the display (half its width and height), right away.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Client:SetMousePositionMiddle[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:SetMousePosition_Middle`
