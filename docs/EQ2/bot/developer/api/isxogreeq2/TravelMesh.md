# ISXOgreEQ2.TravelMesh

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Members

### `TMActive`

`${ISXOgreEQ2.TravelMesh.TMActive}`

TRUE while a travel route is running on this character. It reads FALSE while idle, after arriving or giving up, and while a Go is still waiting for a zone to finish loading.

**Returns:** bool: TRUE when a route is running; FALSE otherwise

```text
echo ${ISXOgreEQ2.TravelMesh.TMActive}
```

### `TMBias`

`${ISXOgreEQ2.TravelMesh.TMBias[kind]}`

The cost multiplier the planner uses for one kind of hop (door, bell, spire, druid, map, amenity or item): 1 is neutral, below 1 prefers it, above 1 avoids it, 0 or less forbids it. Every kind starts at 1.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `kind` | string |  | the hop kind: door, bell, spire, druid, map, amenity or item |

**Returns:** float: the multiplier for that kind; -1 when the kind is unknown or missing

```text
echo ${ISXOgreEQ2.TravelMesh.TMBias[bell]}
```

### `TMCurrentHop`

`${ISXOgreEQ2.TravelMesh.TMCurrentHop}`

A one-line description of the hop in progress: the kind (door, bell, spire, druid, map, amenity or item), the from and to zone short names, and the travel action and destination label when there is one. Empty when no hop is in progress, including after arrival.

**Returns:** string: the current hop's description; empty when there is none

```text
echo ${ISXOgreEQ2.TravelMesh.TMCurrentHop}
```

### `TMDataErrors`

`${ISXOgreEQ2.TravelMesh.TMDataErrors}`

How many travel data files had a problem at the last load, counting files that were skipped and files that loaded with a warning. It reads 0 until the travel data has loaded.

**Returns:** int: the number of problem files; 0 when the data loaded cleanly

```text
echo ${ISXOgreEQ2.TravelMesh.TMDataErrors}
```

### `TMDataErrorText`

`${ISXOgreEQ2.TravelMesh.TMDataErrorText}`

The problem report from the last load, one line per file: its path, which layer it came from (default or custom) and the message. Empty when every file loaded cleanly, or until the travel data has loaded.

**Returns:** string: the problem report, one file per line; empty when clean

```text
echo ${ISXOgreEQ2.TravelMesh.TMDataErrorText}
```

### `TMEdges`

`${ISXOgreEQ2.TravelMesh.TMEdges}`

How many zone-to-zone connections (doors, zone lines, guild hall amenities, travel items and so on) the loaded travel data holds. It reads 0 until the travel data has loaded.

**Returns:** int: the number of connections in the travel data

```text
echo ${ISXOgreEQ2.TravelMesh.TMEdges}
```

### `TMFeatures`

`${ISXOgreEQ2.TravelMesh.TMFeatures}`

One line per account feature the travel data can require (the expansion Friends and Family features), with this character's answer: YES or no, and whether it was scanned or set by you, or unanswered. A no from a scan is checked again after a week, a YES or your own answer is kept, and the lines are read by the travel engine about once a second while you are in the world.

**Returns:** string: one line per account feature

```text
echo ${ISXOgreEQ2.TravelMesh.TMFeatures}
```

### `TMGoal`

`${ISXOgreEQ2.TravelMesh.TMGoal}`

The short zone name of the destination of the current or last route, such as antonica. Empty before any route has started.

**Returns:** string: the destination zone short name; empty before the first route

```text
echo ${ISXOgreEQ2.TravelMesh.TMGoal}
```

### `TMHop`

`${ISXOgreEQ2.TravelMesh.TMHop}`

The number of the hop the route is on, counting from 1. It reads 1 before any route has run and one more than TMHops once the route has arrived.

**Returns:** int: the current hop number, 1-based

```text
echo ${ISXOgreEQ2.TravelMesh.TMHop}
```

### `TMHops`

`${ISXOgreEQ2.TravelMesh.TMHops}`

How many hops the current plan has. After a re-plan this is the hop count of the new plan for the rest of the trip, not the original total.

**Returns:** int: the hop count of the current plan; 0 before any route

```text
echo ${ISXOgreEQ2.TravelMesh.TMHops}
```

### `TMParty`

`${ISXOgreEQ2.TravelMesh.TMParty}`

For the current or last route: the route id, how many group members it counted, and either "everyone is here" or the names of members not yet in this zone and settled. It is empty before any route has started, and read by the travel engine about once a second while you are in the world.

**Returns:** string: the group status line; empty before the first route

```text
echo ${ISXOgreEQ2.TravelMesh.TMParty}
```

### `TMReason`

`${ISXOgreEQ2.TravelMesh.TMReason}`

Why the last route stopped, or what its last step reported, such as "stopped by request" or "replaced by a new route". Empty while a route runs normally.

**Returns:** string: the stop reason or last step message; empty when there is none

```text
echo ${ISXOgreEQ2.TravelMesh.TMReason}
```

### `TMReplans`

`${ISXOgreEQ2.TravelMesh.TMReplans}`

How many times the current route has re-planned around a hop that failed. A route gives up after 3 re-plans.

**Returns:** int: the re-plan count for the current or last route

```text
echo ${ISXOgreEQ2.TravelMesh.TMReplans}
```

### `TMRoute`

`${ISXOgreEQ2.TravelMesh.TMRoute}`

The whole current plan as text, one numbered hop per line in the same form as TMCurrentHop. It still holds the last plan after the route ends.

**Returns:** string: the plan, one hop per line; empty before any route

```text
echo ${ISXOgreEQ2.TravelMesh.TMRoute}
```

### `TMStagger`

`${ISXOgreEQ2.TravelMesh.TMStagger}`

The start delay in milliseconds per group member for group travel, so members do not all set off at once. The default is 10000, and 0 means everybody starts at once.

**Returns:** int: milliseconds of start delay per group member

```text
echo ${ISXOgreEQ2.TravelMesh.TMStagger}
```

### `TMState`

`${ISXOgreEQ2.TravelMesh.TMState}`

The step the route is on: idle, hop-start, walk, wait-for-group, ride, act, verify, done or failed. It keeps done or failed after a route ends until the next route starts.

**Returns:** string: the current route step name

```text
echo ${ISXOgreEQ2.TravelMesh.TMState}
```

### `TMValidate`

`${ISXOgreEQ2.TravelMesh.TMValidate}`

A health check of the loaded travel data, one issue per line. Empty when no issues are found, or until the travel data has loaded.

**Returns:** string: the issues, one per line; empty when there are none

```text
echo ${ISXOgreEQ2.TravelMesh.TMValidate}
```

### `TMZones`

`${ISXOgreEQ2.TravelMesh.TMZones}`

How many zones the loaded travel data knows. It reads 0 until the travel data has loaded.

**Returns:** int: the number of zones in the travel data

```text
echo ${ISXOgreEQ2.TravelMesh.TMZones}
```

## Methods

### `Go`

`ISXOgreEQ2.TravelMesh:Go[destination,poi]`

Starts a route like OgreBotAPI.Travel:Mesh, from your current zone to the destination, walking and using doors, zone lines, bells, spires, druid rings, the fast-travel map, guild hall amenities and travel items in your bags as needed; it replaces a running route, whoever started it, only when the new one can be planned. Problems (no destination, unknown destination with suggestions, current zone not in the travel data, no route) are echoed to the console, a Go made while zoning waits for the zone to settle, and the route moves with OgreBot closed too - TravelMesh:Stop ends it.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `destination` | string |  | the zone to travel to - its display name, an alias or its short name, any case |
| `poi` | string | `none` | optional point of interest in the destination zone to finish at; one the zone data does not list is reported and the trip still goes to the zone |

```text
ISXOgreEQ2.TravelMesh:Go[Antonica,"Druid Rings"]
```

### `GoGroup`

`ISXOgreEQ2.TravelMesh:GoGroup[destination,poi]`

Like OgreBotAPI.Travel:MeshGroup: starts your own route as Go does, then sends -TravelMesh for the same destination to the rest of your group through OgreConsole, so each member plans its own route from where it stands, with starts staggered by TMStagger. If your own route cannot be planned the error is echoed and nothing is sent; the other members' copies run as OgreBot routes, so they are stopped with -TravelMeshStop.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `destination` | string |  | the zone to travel to - its display name, an alias or its short name, any case |
| `poi` | string | `none` | optional point of interest in the destination zone to finish at; one the zone data does not list is reported and the trip still goes to the zone |

```text
ISXOgreEQ2.TravelMesh:GoGroup[Antonica]
```

### `Preview`

`ISXOgreEQ2.TravelMesh:Preview[destination]`

Plans a route from your current zone to the destination and prints it to the console without moving: a summary line with the hop count and rough time in seconds, then one numbered hop per line. An unknown destination prints an "unknown destination" line with suggestions, and no destination prints an error.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `destination` | string |  | the zone to plan to - its display name, an alias or its short name, any case |

```text
ISXOgreEQ2.TravelMesh:Preview[Antonica]
```

### `Reload`

`ISXOgreEQ2.TravelMesh:Reload`

Re-reads the travel data from Ogre/EQ2/Travel/default and your own OgreSave/EQ2/Travel/custom files and echoes a summary of zones, connections, files and errors. Any running route is stopped first, whoever started it; if the first load has not finished within 5 seconds it says so and changes nothing.

```text
ISXOgreEQ2.TravelMesh:Reload
```

### `ScanFeatures`

`ISXOgreEQ2.TravelMesh:ScanFeatures`

Runs the game's show_account_features command to answer this character's unanswered or expired account features, and echoes a status line. Each feature is scanned at most once per session, a scan also starts by itself when a route is planned, and when nothing is scanned (out of the world included) the line says every feature is already answered.

```text
ISXOgreEQ2.TravelMesh:ScanFeatures
```

### `SetBias`

`ISXOgreEQ2.TravelMesh:SetBias[kind,multiplier]`

Sets how much the planner likes one kind of hop: 1 is neutral, below 1 prefers it, above 1 avoids it, 0 or less forbids it, and the new value is echoed. It applies to the next plan and is not saved; a multiplier that is not a number sets the normal bias of 1 and says so.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `kind` | string |  | the hop kind: door, bell, spire, druid, map, amenity or item; anything else is refused with a console error |
| `multiplier` | float |  | the cost multiplier: 1 neutral, below 1 prefer, above 1 avoid, 0 or less forbid; a word is 1 |

```text
ISXOgreEQ2.TravelMesh:SetBias[druid,0.5]
```

### `SetFeature`

`ISXOgreEQ2.TravelMesh:SetFeature[flag,value]`

Saves your own answer for one account feature for this character in OgreSave/EQ2/Travel/account-features.json; it is permanent and never scanned over, and the answer is echoed. A feature name the travel data does not use is refused with a line naming the ones it does, a blank value prints an error, and a word that is not yes or no leaves the feature as it is and says so.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `flag` | string |  | the account feature name as TMFeatures shows it, such as roc_friends_and_family, in any case |
| `value` | bool |  | TRUE, 1, yes or on means this character has the feature; FALSE, 0, no or off means it does not |

```text
ISXOgreEQ2.TravelMesh:SetFeature[roc_friends_and_family,TRUE]
```

### `SetStagger`

`ISXOgreEQ2.TravelMesh:SetStagger[ms]`

Sets the start delay in milliseconds per group member for group travel (0 = everybody at once) and echoes it. A negative number is stored as 0, a value that is not a number counts as 0, and the setting is not saved.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `ms` | int |  | milliseconds of start delay per group member; 0 starts everybody at once |

```text
ISXOgreEQ2.TravelMesh:SetStagger[5000]
```

### `Stop`

`ISXOgreEQ2.TravelMesh:Stop[-force]`

Cancels a route started with this object's Go or GoGroup, including one still waiting for a zone to settle. A route someone else started is refused with one line naming the owner and how to stop it, and -force stops it anyway.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `-force` | switch |  | stop the route whoever started it |

```text
ISXOgreEQ2.TravelMesh:Stop
```
