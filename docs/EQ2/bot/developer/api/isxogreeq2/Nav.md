# ISXOgreEQ2.Nav

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Members

### `NavActive`

`${ISXOgreEQ2.Nav.NavActive}`

TRUE while a nav trip is in progress - planning its route, waiting for this zone's navmesh, or moving. A paused trip still counts as in progress.

**Returns:** bool: TRUE while a trip is planning, waiting for its navmesh or moving; FALSE when idle or once the last trip has ended (Arrived, Stopped, Failed).

```text
echo ${ISXOgreEQ2.Nav.NavActive}
```

### `NavDistance`

`${ISXOgreEQ2.Nav.NavDistance}`

Straight-line distance from the character to the trip's destination, refreshed every pulse while it moves, on foot or flying. It is -1 when idle, while a trip is still planning or waiting for its navmesh, and after a trip ends.

**Returns:** float: distance in game units to the destination; -1 when no trip is moving.

```text
echo ${ISXOgreEQ2.Nav.NavDistance}
```

### `NavMeshOn`

`${ISXOgreEQ2.Nav.NavMeshOn}`

TRUE unless nav has been switched off with Nav:Set[mesh,off] or `ogre nav -off`. While it is off, new trips are refused; the switch is not saved and starts TRUE each time the extension loads.

**Returns:** bool: TRUE when nav is allowed to move this character; FALSE when it is switched off.

```text
echo ${ISXOgreEQ2.Nav.NavMeshOn}
```

### `NavMeshPolys`

`${ISXOgreEQ2.Nav.NavMeshPolys}`

How many walkable polygons the loaded navmesh has. It is 0 when no mesh is loaded in this zone yet.

**Returns:** int: polygon count of the loaded mesh; 0 when none is loaded.

```text
echo ${ISXOgreEQ2.Nav.NavMeshPolys}
```

### `NavMeshTiles`

`${ISXOgreEQ2.Nav.NavMeshTiles}`

How many tiles the loaded navmesh has. It is 0 when no mesh is loaded in this zone yet.

**Returns:** int: tile count of the loaded mesh; 0 when none is loaded.

```text
echo ${ISXOgreEQ2.Nav.NavMeshTiles}
```

### `NavMeshZone`

`${ISXOgreEQ2.Nav.NavMeshZone}`

Name of the navmesh that is loaded - the zone's short name in lower case, or the base zone's name when this zone is a copy that uses it. It is "" until a mesh is loaded in this zone (see NavOnMap).

**Returns:** string: the loaded mesh's zone name; "" when none is loaded.

```text
echo ${ISXOgreEQ2.Nav.NavMeshZone}
```

### `NavOnMap`

`${ISXOgreEQ2.Nav.NavOnMap}`

TRUE when a navmesh is loaded right now, so nav can plan a route without waiting. The mesh loads on the first trip or route request in a zone and is set aside on every zone change, so this reads FALSE after zoning until something asks for a route.

**Returns:** bool: TRUE when a navmesh is loaded; FALSE when none is loaded yet in this zone.

```text
echo ${ISXOgreEQ2.Nav.NavOnMap}
```

### `NavOnMesh`

`${ISXOgreEQ2.Nav.NavOnMesh}`

TRUE while the current trip is driven over a navmesh route. It is FALSE when idle, while a trip still waits for its navmesh or plans its first route, and once a trip ends.

**Returns:** bool: TRUE while a trip is driven over a navmesh route; FALSE otherwise.

```text
echo ${ISXOgreEQ2.Nav.NavOnMesh}
```

### `NavReason`

`${ISXOgreEQ2.Nav.NavReason}`

Plain words about the trip: while it plans or moves, what the plan is doing; once it has ended or while it waits for a navmesh, why. It is empty before the first trip, and reads "already there" when a trip was asked for the spot the character already stands on.

**Returns:** string: the plan in force, or why the last trip ended; "" before any trip.

```text
echo ${ISXOgreEQ2.Nav.NavReason}
```

### `NavState`

`${ISXOgreEQ2.Nav.NavState}`

The trip's state as one word; Arrived, Stopped and Failed stay until the next trip starts, and a paused trip still reads Moving. Stopped means somebody ended the trip on purpose, Failed means nav gave up - NavReason says why.

**Returns:** string: a state word such as Idle, Planning, WaitingForMesh, Moving, Arrived, Stopped or Failed.

```text
echo ${ISXOgreEQ2.Nav.NavState}
```

### `NavWaypoint`

`${ISXOgreEQ2.Nav.NavWaypoint}`

The waypoint on the current route the character is heading for, counted from 1 (the first point after the start) up to NavWaypoints on the last leg. It is 0 when no route is being walked, a finished trip included.

**Returns:** int: the waypoint being walked to, 1 to NavWaypoints; 0 when no route is being walked.

```text
echo ${ISXOgreEQ2.Nav.NavWaypoint}
```

### `NavWaypoints`

`${ISXOgreEQ2.Nav.NavWaypoints}`

How many waypoints the current route has after its start point, so NavWaypoint reaches it on the last leg. It is 0 when no route is being walked, a finished trip included.

**Returns:** int: number of waypoints after the start; 0 when no route is being walked.

```text
echo ${ISXOgreEQ2.Nav.NavWaypoints}
```

## Methods

### `End`

`ISXOgreEQ2.Nav:End`

Ends the trip under way and closes the nav window, the same as `ogre end nav`, `ogre nav end` or the window's X. It prints "nav: stopped (...)" only when a trip was under way.

```text
ISXOgreEQ2.Nav:End
```

### `Flags`

`ISXOgreEQ2.Nav:Flags[flag...]`

Runs the `ogre nav -<flag> ...` line: -loc x,y,z (or -to) starts a trip and applies -precision, -nodoors/-doors and -reset with it (it ignores -set, -on/-off and -panel/-nopanel on the same line), while a line without -loc takes -set key value, -reset [key], -on/-off, -panel/-nopanel, -stop, -status or -help. With no flag it prints a warning and a bad or unknown flag prints an error naming it; -precision and -nodoors stay in force after the trip.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `flag...` | string |  | The flags and their values, one per argument; a -loc point may be one "x,y,z" argument or three. |

```text
ISXOgreEQ2.Nav:Flags[-loc,${Me.X},${Me.Y},${Math.Calc[${Me.Z}+30]},-precision,3]
```

### `Help`

`ISXOgreEQ2.Nav:Help`

Prints the `ogre nav` command help to the console, one line at a time. This is bare `ogre nav` or `ogre nav help`.

```text
ISXOgreEQ2.Nav:Help
```

### `Open`

`ISXOgreEQ2.Nav:Open`

Opens the nav panel (trip state with Stop and Pause buttons) now; if the window cannot open it prints "nav panel: &lt;reason>". This is `ogre nav panel`.

```text
ISXOgreEQ2.Nav:Open
```

### `Set`

`ISXOgreEQ2.Nav:Set[key,value]`

Changes one nav setting for this session (not saved) and prints "nav: &lt;key> = &lt;value>"; an unknown key, or a value the setting refuses, prints an error and changes nothing. The key is case-insensitive, and `mesh` (alias `on`) never refuses: a yes word switches nav on and any other value switches it off.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `key` | string |  | The setting's name, such as arrive, finalarrive, doors or avoid. |
| `value` | string |  | The new value - a number for distances and counts, on or off for switches. |

```text
ISXOgreEQ2.Nav:Set[arrive,4]
```

### `Status`

`ISXOgreEQ2.Nav:Status`

Prints what nav is doing to the console - state, reason, paused, waypoint progress, the loaded mesh and every setting changed from its default. This is `ogre nav status`.

```text
ISXOgreEQ2.Nav:Status
```

### `Stop`

`ISXOgreEQ2.Nav:Stop`

Ends the trip under way (NavState becomes Stopped) and prints "nav: stopped"; the nav panel stays open. With no trip under way it changes nothing but still prints the line - this is `ogre nav stop`.

```text
ISXOgreEQ2.Nav:Stop
```

### `To`

`ISXOgreEQ2.Nav:To[x,y,z]`

Starts a trip that moves the character to the point, replacing any trip already under way; it returns at once and the route is planned over the next frames (watch NavState). A missing value, or one that is not a number, prints an error and starts nothing, and a refusal (not in world, movement held by another system, no navmesh) prints "nav: &lt;reason>".

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `x` | float |  | X of the destination. |
| `y` | float |  | Y of the destination - Y is up in EQ2. |
| `z` | float |  | Z of the destination. |

```text
ISXOgreEQ2.Nav:To[${Me.X},${Me.Y},${Math.Calc[${Me.Z}+30]}]
```
