<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# ISXOgreEQ2.Events

## Members

### `Count`

`${ISXOgreEQ2.Events.Count}`

How many native game events the extension listens to, currently 14, numbered from 0 for the event argument of Received, Dispatched, Subscribers, EventName and NativeName.

**Returns:** int: the number of events (14 today)

```text
echo ${ISXOgreEQ2.Events.Count}
```

### `Dispatched`

`${ISXOgreEQ2.Events.Dispatched[<event>]}`

How many arrivals of this game event have been handed out to the extension's features since it loaded, or the total for all events when the argument is left out. It trails Received only by what is still Pending, and an unknown event gives NULL.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `&lt;event>` | string |  | The event's 0-based number or its name, such as ActorSpawned; leave it out for the total across all events |

**Returns:** int64: arrivals handed out for that event since load (or for all events); NULL for an unknown event

```text
echo ${ISXOgreEQ2.Events.Dispatched[ActorSpawned]}
```

### `Dropped`

`${ISXOgreEQ2.Events.Dropped}`

Total game events thrown away since the extension loaded, because more than 4096 were waiting at once (oldest dropped first) or the event was not recognised. It never resets.

**Returns:** int64: events dropped since load

```text
echo ${ISXOgreEQ2.Events.Dropped}
```

### `EventName`

`${ISXOgreEQ2.Events.EventName[<event>]}`

The extension's name for a game event, such as IncomingChatText, looked up by its 0-based number or its name. A missing or unknown event gives NULL.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `&lt;event>` | string |  | The event's 0-based number (0 to Count minus 1) or its name |

**Returns:** string: the event's name; NULL for a missing or unknown event

```text
echo ${ISXOgreEQ2.Events.EventName[0]}
```

### `NativeName`

`${ISXOgreEQ2.Events.NativeName[<event>]}`

The ISXEQ2 event a game event is read from, such as EQ2_onIncomingChatText, which is also the name a script attaches its own atom to. A missing or unknown event gives NULL.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `&lt;event>` | string |  | The event's 0-based number (0 to Count minus 1) or its name, such as IncomingChatText |

**Returns:** string: the ISXEQ2 event name; NULL for a missing or unknown event

```text
echo ${ISXOgreEQ2.Events.NativeName[IncomingChatText]}
```

### `Pending`

`${ISXOgreEQ2.Events.Pending}`

How many received game events are waiting to be handed to the extension's features; they are handed out every pulse, so this is normally 0. At most 4096 can wait, and beyond that the oldest are dropped and counted in Dropped.

**Returns:** int: events waiting to be handed out right now

```text
echo ${ISXOgreEQ2.Events.Pending}
```

### `Received`

`${ISXOgreEQ2.Events.Received[<event>]}`

How many times this game event has arrived since the extension loaded, or the total for all events when the argument is left out. The event is its 0-based number or its name in any case (IncomingChatText, ActorSpawned and so on), and an unknown event gives NULL.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `&lt;event>` | string |  | The event's 0-based number or its name, such as IncomingChatText; leave it out for the total across all events |

**Returns:** int64: arrivals of that event since load (or of all events); NULL for an unknown event

```text
echo ${ISXOgreEQ2.Events.Received[IncomingChatText]}
```

### `Stats`

`${ISXOgreEQ2.Events.Stats}`

One summary line, such as attached=yes events=14 pending=0 dropped=0 recv=5120 disp=5120, with recv and disp totalled across all events. Echoing ${ISXOgreEQ2.Events} prints the same line after the word Events.

**Returns:** string: the summary line

```text
echo ${ISXOgreEQ2.Events.Stats}
```

### `StatsJSON`

`${ISXOgreEQ2.Events.StatsJSON}`

The full event table as one JSON object: attached, count, pending, dropped, and an events array giving each event's i, label, native, received, dispatched and subscribers.

**Returns:** string: a JSON object

```text
echo ${ISXOgreEQ2.Events.StatsJSON}
```

### `Subscribers`

`${ISXOgreEQ2.Events.Subscribers[<event>]}`

How many of the extension's own features are listening to this game event (such as the chat and spawn handling behind OgreBotAPI.Events), or the total when the argument is left out. Atoms a script attaches to the ISXEQ2 event itself are not counted, and an unknown event gives NULL.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `&lt;event>` | string |  | The event's 0-based number or its name, such as FinishedZoning; leave it out for the total across all events |

**Returns:** int: listeners on that event (or on all events); NULL for an unknown event

```text
echo ${ISXOgreEQ2.Events.Subscribers[FinishedZoning]}
```
