# OgreBotAPI.Travel

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Members

### `ZoneDoorValue`

`${OgreBotAPI.Travel.ZoneDoorValue[option]}`

Reads the row that ZoneDoor would pick for an option in the zone-door destination window that is open now, without clicking anything. It reads the window only when it is open and answers 0 otherwise.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `option` | string |  | A row number, a destination name (the whole name in any case, with or without its instance number), or LAST_ENTRY for the last listed row. |

**Returns:** int: the 1-based row of that destination in the open window; 0 when no window is open, the option is empty, no row matches, or a row number is past the end of the list.

```text
echo ${OgreBotAPI.Travel.ZoneDoorValue[LAST_ENTRY]}
```

*Was (OldBot):* `OgreBotAPI.Travel_Get_ZoneDoorValue`

## Methods

### `Bell`

`OgreBotAPI.Travel:Bell[fw, toWhere, exact=FALSE, mzo=LAST_ENTRY]`

Double-clicks a bell within reach (15 units unless the travel data says otherwise), picks toWhere on its map, clicks the zone button, answers the window that follows and closes the map. It runs in the background, replaces any travel in progress, and gives up with a console line when no bell is in reach or the destination is still missing after a second look.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `toWhere` | string |  | The destination button to pick, matched case-insensitively against the map's button labels as part of a label; the first match wins. When it is not found the console line lists every destination the bell offers. |
| `exact` | bool | `FALSE` | TRUE to match the whole label (still any case) instead of part of it. |
| `mzo` | string | `LAST_ENTRY` | When a zone-door destination window follows the zone button, the row to pick there: a row number, a destination name, or LAST_ENTRY for the last row. When a zone's sub-map follows instead, the last location on it is picked. |

```text
OgreBotAPI.Travel:Bell[${Me.Name},"Antonica"]
```

*Was (OldBot):* `OgreBotAPI:TravelBell`

### `Druid`

`OgreBotAPI.Travel:Druid[fw, toWhere, exact=FALSE, mzo=LAST_ENTRY]`

Double-clicks a druid ring within reach, or in a guild hall talks to the guild hall druid, if there is one, and uses the ring that conversation brings up, then picks toWhere on its map, clicks the zone button and closes the map. It runs in the background, replaces any travel in progress, and gives up with a console line when nothing opens or the destination is still missing after a second look.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `toWhere` | string |  | The destination button to pick, matched case-insensitively against the map's button labels as part of a label; the first match wins. When it is not found the console line lists every destination the ring offers. |
| `exact` | bool | `FALSE` | TRUE to match the whole label (still any case) instead of part of it. |
| `mzo` | string | `LAST_ENTRY` | When a zone-door destination window follows the zone button, the row to pick there: a row number, a destination name, or LAST_ENTRY for the last row. When a zone's sub-map follows instead, the last location on it is picked. |

```text
OgreBotAPI.Travel:Druid[${Me.Name},"Steamfont"]
```

*Was (OldBot):* `OgreBotAPI:TravelDruid`

### `Fast`

`OgreBotAPI.Travel:Fast[fw, toWhere, flag...]`

Opens the game's fast travel map, picks toWhere, clicks the zone button, answers the window that follows and closes the map. It runs in the background, replaces any travel in progress, and gives up with a console line when the map does not open or the destination is still missing after a second look.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `toWhere` | string |  | The destination button to pick, matched case-insensitively as part of a label unless -em is given; the first match wins. When it is not found the console line lists every destination the map offers. |
| `flag...` | string |  | Optional switches in any order. -em (or -exactmatch) matches the whole label. -mto &lt;option> picks that number of sub-map location, counting from 1, the one whose description contains that text, Random, or Last; without it the last location is picked. -loc &lt;x,y,z> (or -mtl) picks the sub-map location nearest that point. -mzo &lt;option> picks the zone-door row: a number, a name, or LAST_ENTRY (the default). -report echoes the sub-map's locations instead of picking one. Unknown words are ignored. |

```text
OgreBotAPI.Travel:Fast[${Me.Name},"Antonica",-mto,Random]
```

*Was (OldBot):* `OgreBotAPI:FastTravel`, `call Obj_OgreUtilities.FastTravel`, `Obj_OgreUtilities.Obj_Travel`

### `Mesh`

`OgreBotAPI.Travel:Mesh[fw, zone, poi=""]`

Plans a route from this zone to zone across the travel network (zone doors, bells, spires, druid rings, the travel map, guild hall amenities and travel items such as call-to-home), echoes its hops, then walks and travels it hop by hop. A trip asked for while zoning starts once the zone settles, a new route replaces the one in progress only when it can be planned, and the route ends when OgreBot ends; a bot you paused stays paused on arrival.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `zone` | string |  | The destination zone: its display name in any case, or its travel-data id. An empty zone echoes "no destination zone given", and an unknown one echoes a "did you mean" list. |
| `poi` | string | `""` | A named point inside the destination zone to walk to at the end. A point the zone does not declare gets a console line and the route still goes to the zone. |

```text
OgreBotAPI.Travel:Mesh[${Me.Name},"Antonica"]
```

*Was (OldBot):* `OgreBotAPI:TravelMesh`

### `MeshFeatures`

`OgreBotAPI.Travel:MeshFeatures[fw, flag="", on=""]`

With no flag, echoes the account travel features the route planner knows for this character (the Friends and Family unlocks) and starts a scan for any still unanswered. With a flag and a yes or no, saves your answer for this character, which the planner then trusts and never scans again; a flag with no answer prints an error and saves nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `flag` | string | `""` | The feature id to set: sod_friends_and_family or roc_friends_and_family, in any case. Empty lists every feature instead of setting one; an id that is not one of those prints a line naming them and saves nothing. |
| `on` | bool |  | TRUE when the character holds the feature, FALSE when it does not. Needed with a flag; a word that is not a yes or no word leaves the feature as it is. |

```text
OgreBotAPI.Travel:MeshFeatures[${Me.Name},sod_friends_and_family,TRUE]
```

*Was (OldBot):* `OgreBotAPI:TravelMeshFeatures`

### `MeshGroup`

`OgreBotAPI.Travel:MeshGroup[fw, zone, poi=""]`

Starts the same route as Mesh on this character, then sends it to the rest of the group as a console command, and each member plans its own route from where it stands, staggered so the group does not move as one. Addressed to more than one character each plans its own route and nothing is sent, and when this character cannot plan the route nothing is sent.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `zone` | string |  | The destination zone: its display name in any case, or its travel-data id. An empty zone echoes "no destination zone given", and an unknown one echoes a "did you mean" list. |
| `poi` | string | `""` | A named point inside the destination zone to walk to at the end, sent to every member. A point the zone does not declare gets a console line and the route still goes to the zone. |

```text
OgreBotAPI.Travel:MeshGroup[${Me.Name},"The Commonlands"]
```

*Was (OldBot):* `Obj_OgreIH.Obj_OgreTravelMesh`, `OgreBotAPI:TravelMeshGroup`

### `MeshPreview`

`OgreBotAPI.Travel:MeshPreview[fw, zone]`

Plans the route from here to zone and echoes it, a summary line with the hop count and rough time and then one line per hop, without moving. When there is no route it echoes why, and the first use loads the travel data, which can take a moment.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `zone` | string |  | The destination zone: its display name in any case, or its travel-data id. An unknown one echoes a "did you mean" list. |

```text
OgreBotAPI.Travel:MeshPreview[${Me.Name},"Antonica"]
```

*Was (OldBot):* `OgreBotAPI:TravelMeshPreview`

### `MeshStop`

`OgreBotAPI.Travel:MeshStop[fw]`

Stops the route in progress, and a trip still waiting for its zone to settle, whoever started it. It echoes "travel: gave up (stopped by request)" when a route was running and is silent otherwise.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Travel:MeshStop[all]
```

*Was (OldBot):* `OgreBotAPI:TravelMeshStop`

### `SpewZoneDoorOptions`

`OgreBotAPI.Travel:SpewZoneDoorOptions[fw]`

Echoes every destination in the open zone-door destination window as "[#n] name", numbered by row so the number works with ZoneDoor and ZoneDoorValue. With no window open it says so and reads nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Travel:SpewZoneDoorOptions[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:SpewZoneDoorOptions`

### `Spires`

`OgreBotAPI.Travel:Spires[fw, toWhere, exact=FALSE, mzo=LAST_ENTRY]`

Double-clicks a wizard spire within reach, picks toWhere on its map, clicks the zone button, answers the window that follows and closes the map. It runs in the background, replaces any travel in progress, and gives up with a console line when no spire is in reach or the destination is still missing after a second look.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `toWhere` | string |  | The destination button to pick, matched case-insensitively against the map's button labels as part of a label; the first match wins. When it is not found the console line lists every destination the spire offers. |
| `exact` | bool | `FALSE` | TRUE to match the whole label (still any case) instead of part of it. |
| `mzo` | string | `LAST_ENTRY` | When a zone-door destination window follows the zone button, the row to pick there: a row number, a destination name, or LAST_ENTRY for the last row. When a zone's sub-map follows instead, the last location on it is picked. |

```text
OgreBotAPI.Travel:Spires[${Me.Name},"The Commonlands"]
```

*Was (OldBot):* `OgreBotAPI:TravelSpires`

### `ToGuildHall`

`OgreBotAPI.Travel:ToGuildHall[fw]`

Double-clicks the nearest actor within 15 units whose name contains "Magic Door to the Guild Hall", the city door that takes you to your guild hall. With no such door in reach it prints one line.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Travel:ToGuildHall[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:PortalToGuildHall`

### `Travel`

`OgreBotAPI.Travel:Travel[fw, toWhere, exact=FALSE, mzo=LAST_ENTRY]`

Picks toWhere on a travel map that is already open, clicks the zone button, answers the window that follows and closes the map, so open the map first (a griffon station's map, for example). It runs in the background, replaces any travel in progress, and gives up with a console line when no map is up within 5 seconds or the destination is still missing after a second look.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `toWhere` | string |  | The destination button to pick, matched case-insensitively against the map's button labels as part of a label; the first match wins. When it is not found the console line lists every destination the map offers. |
| `exact` | bool | `FALSE` | TRUE to match the whole label (still any case) instead of part of it. |
| `mzo` | string | `LAST_ENTRY` | When a zone-door destination window follows the zone button, the row to pick there: a row number, a destination name, or LAST_ENTRY for the last row. When a zone's sub-map follows instead, the last location on it is picked. |

```text
OgreBotAPI.Travel:Travel[${Me.Name},"The Commonlands"]
```

*Was (OldBot):* `OgreBotAPI:Travel`

### `ZoneDoor`

`OgreBotAPI.Travel:ZoneDoor[door=1]`

Picks a destination in the zone-door destination window that is already open and confirms it half a second later. It takes no for-who and runs on the session that calls it, and with no window open, or a destination not in the list, it does nothing and echoes why (listing what the window offers).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `door` | string | `1` | A row number, a destination name (the whole name in any case, with or without its instance number), or LAST_ENTRY for the last row. SpewZoneDoorOptions shows the rows. |

```text
OgreBotAPI.Travel:ZoneDoor[LAST_ENTRY]
```

*Was (OldBot):* `OgreBotAPI:ZoneDoor`

### `ZoneDoorFor`

`OgreBotAPI.Travel:ZoneDoorFor[fw, door=1]`

The for-who form of ZoneDoor: picks door in the zone-door destination window that is already open and confirms it half a second later. With no window open, or a destination not in the list, it does nothing and echoes why (listing what the window offers).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `door` | string | `1` | A row number, a destination name (the whole name in any case, with or without its instance number), or LAST_ENTRY for the last row. SpewZoneDoorOptions shows the rows. |

```text
OgreBotAPI.Travel:ZoneDoorFor[igw:${Me.Name},LAST_ENTRY]
```

*Was (OldBot):* `OgreBotAPI:ZoneDoorForWho`, `call Obj_OgreUtilities.HandleZoneDoor`
