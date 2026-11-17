# ISXOgreEQ2.Spawn

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Members

### `ChestId`

`${ISXOgreEQ2.Spawn.ChestId}`

The actor ID of the Exquisite Chest that spawned in this zone, taken from the spawn feed. It goes back to 0 when that chest despawns or you zone.

**Returns:** int64: the chest's actor ID; 0 when there is none.

```text
echo ${ISXOgreEQ2.Spawn.ChestId}
```

### `DespawnsDispatched`

`${ISXOgreEQ2.Spawn.DespawnsDispatched}`

The number of despawn events handed on to the bot's internal listeners since the extension loaded.

**Returns:** int64: despawn events dispatched.

```text
echo ${ISXOgreEQ2.Spawn.DespawnsDispatched}
```

### `Dispatched`

`${ISXOgreEQ2.Spawn.Dispatched}`

The total number of spawn and despawn events handed on to the bot's internal listeners since the extension loaded. It is SpawnsDispatched plus DespawnsDispatched.

**Returns:** int64: spawn plus despawn events dispatched.

```text
echo ${ISXOgreEQ2.Spawn.Dispatched}
```

### `HasChest`

`${ISXOgreEQ2.Spawn.HasChest}`

Whether an Exquisite Chest is up in this zone, the same test as ChestId being non-zero.

**Returns:** bool: TRUE when ChestId is not 0; FALSE otherwise.

```text
echo ${ISXOgreEQ2.Spawn.HasChest}
```

### `IsLive`

`${ISXOgreEQ2.Spawn.IsLive[id]}`

Whether the actor ID is in the live set: seen spawning (or present when the zone settled) and not yet despawned. The set is wiped when you zone and filled again once the new zone settles, so it can read FALSE for a moment after zoning.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `&lt;id>` | int64 |  | The actor ID to test. |

**Returns:** bool: TRUE when that actor is live; FALSE when it is not, or when no ID is given.

```text
echo ${ISXOgreEQ2.Spawn.IsLive[${Target.ID}]}
```

### `LiveCount`

`${ISXOgreEQ2.Spawn.LiveCount}`

How many actor IDs are in the live set for this zone. It drops to 0 while zoning and refills once the new zone settles.

**Returns:** int: the number of live actors tracked.

```text
echo ${ISXOgreEQ2.Spawn.LiveCount}
```

### `OnSpawnDelay`

`${ISXOgreEQ2.Spawn.OnSpawnDelay}`

How long after an actor spawns the delayed spawn event EQ2_ActorSpawned_Delayed fires for it (only if it is still live). The default is 1000 ms and the most is 60000; SetOnSpawnDelay changes it for this session only.

**Returns:** int: the delay in milliseconds.

```text
echo ${ISXOgreEQ2.Spawn.OnSpawnDelay}
```

### `Received`

`${ISXOgreEQ2.Spawn.Received}`

The total number of actor spawn and despawn events received from the game since the extension loaded. It is a diagnostic counter and is not reset by zoning.

**Returns:** int64: spawn plus despawn events received.

```text
echo ${ISXOgreEQ2.Spawn.Received}
```

### `SpawnsDispatched`

`${ISXOgreEQ2.Spawn.SpawnsDispatched}`

The number of spawn events handed on to the bot's internal listeners since the extension loaded.

**Returns:** int64: spawn events dispatched.

```text
echo ${ISXOgreEQ2.Spawn.SpawnsDispatched}
```

### `Subscribers`

`${ISXOgreEQ2.Spawn.Subscribers}`

How many internal listeners are attached to the spawn feed. It counts spawn, despawn and delayed-spawn listeners together.

**Returns:** int: the number of attached listeners.

```text
echo ${ISXOgreEQ2.Spawn.Subscribers}
```

## Methods

### `DelayStatus`

`ISXOgreEQ2.Spawn:DelayStatus`

Prints the delayed spawn event's state to the console: the delay, the per-drain cap, what is waiting and ready, and the counters since the last zone-in.

```text
ISXOgreEQ2.Spawn:DelayStatus
```

### `ResetOnSpawnDelay`

`ISXOgreEQ2.Spawn:ResetOnSpawnDelay`

Puts the delay before EQ2_ActorSpawned_Delayed back to the default of 1000 ms and prints the value to the console.

```text
ISXOgreEQ2.Spawn:ResetOnSpawnDelay
```

### `SetOnSpawnCap`

`ISXOgreEQ2.Spawn:SetOnSpawnCap`

Sets how many due spawns one drain may emit, for this session only, held between 1 and 5000 (0 or a negative is 1), and prints the value in force to the console. A value that is not a number keeps the cap and says so; with no value it prints one warning and changes nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `&lt;k>` | int |  | The per-drain cap, 1 to 5000. |

```text
ISXOgreEQ2.Spawn:SetOnSpawnCap[25]
```

### `SetOnSpawnDelay`

`ISXOgreEQ2.Spawn:SetOnSpawnDelay[<ms>]`

Sets the delay before EQ2_ActorSpawned_Delayed fires, for this session only (it is not saved), and prints the value in force to the console. More than 60000 ms is held at 60000; a value that is not a whole number of 0 or more is refused with a warning and the delay is unchanged.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `&lt;ms>` | int |  | The delay in milliseconds, 0 to 60000. |

```text
ISXOgreEQ2.Spawn:SetOnSpawnDelay[1500]
```

### `Status`

`ISXOgreEQ2.Spawn:Status`

Prints the spawn consumer's counters to the console: spawns and despawns seen, duplicate and unknown ids, the live actor count, the chest id and the router's subscribers and throughput.

```text
ISXOgreEQ2.Spawn:Status
```
