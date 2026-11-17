# OgreBotAPI.POI

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Members

### `Count`

`${OgreBotAPI.POI.Count}`

How many points of interest the current zone has, shipped and your own together. It reads 0 in a zone with none, while you are not settled in a zone and while the travel data loads.

**Returns:** int: the current zone's total. A POI of yours that overrides a shipped one counts once.

```text
echo ${OgreBotAPI.POI.Count}
```

### `Loc`

`${OgreBotAPI.POI.Loc[name]}`

Where a point of interest of the current zone is, shipped or your own. It reads empty for an unknown name, for a POI that names only an actor, while you are not settled in a zone and while the travel data loads.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | string |  | The POI's name, in any case. |

**Returns:** string: x,y,z to two decimals, or empty when there is no such location.

```text
echo ${OgreBotAPI.POI.Loc[bell]}
```

## Methods

### `Add`

`OgreBotAPI.POI:Add[name, x, y, z, sender]`

Saves a named point of interest in the zone you are in, where you stand or at x,y,z, for every character on this PC. A shipped name is overridden, a name of your own moves to the new spot, and a refusal prints one line and saves nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | string |  | The name, in any case. It cannot be empty, hold a comma or read as a number. |
| `x` | float |  | X of the spot. Leave x, y and z out to use where you stand. With any of them given all three are needed, and 0,0,0 is refused. |
| `y` | float |  | Y (height) of the spot. |
| `z` | float |  | Z of the spot. |
| `sender` | string |  | Leave this out in a script. The -POI_Add row fills it with the box that sent the line, and every other box does nothing. |

```text
OgreBotAPI.POI:Add["Quest giver",100,20,-250]
```

### `Remove`

`OgreBotAPI.POI:Remove[name]`

Removes a point of interest of your own from the zone you are in, and a shipped POI it was overriding is back. A shipped POI cannot be removed: that and an unknown name print one line and change nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | string |  | The POI's name, in any case. |

```text
OgreBotAPI.POI:Remove["Quest giver"]
```

### `Rename`

`OgreBotAPI.POI:Rename[old, new]`

Renames a point of interest of your own in the zone you are in. A shipped POI, an unknown name and a new name that another POI here holds each print one line and change nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `old` | string |  | The POI's name now, in any case. |
| `new` | string |  | The new name. It cannot be empty, hold a comma or read as a number. |

```text
OgreBotAPI.POI:Rename["Quest giver","Quest giver east"]
```
