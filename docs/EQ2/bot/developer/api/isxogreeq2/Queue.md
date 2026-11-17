<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# ISXOgreEQ2.Queue

## Members

### `Blocking`

`${ISXOgreEQ2.Queue.Blocking}`

Why the most urgent waiting entry cannot start yet, as a line like seq=5 CastAbility prio=100 age=900ms: resource busy: CastBar, or starved by a higher-priority haltQueue entry. Empty when nothing is waiting or the next entry is free to start.

**Returns:** string: the reason line; empty when nothing is held up

```text
echo ${ISXOgreEQ2.Queue.Blocking}
```

### `Count`

`${ISXOgreEQ2.Queue.Count}`

Number of entries in the action queue, running plus waiting.

**Returns:** int: entries running plus waiting; 0 when the queue is empty

```text
echo ${ISXOgreEQ2.Queue.Count}
```

### `Enqueue`

`${ISXOgreEQ2.Queue.Enqueue[priority,kind,arg0,arg1,ttlstart,ttlmax]}`

Adds an entry exactly like ISXOgreEQ2.Queue:Add and returns its seq, the id you pass to Status, IsDone and Remove. Reading the member is what adds the entry, so every read queues another one, and an unknown kind (ApplyVerbCastBar and DialogChoices included) or a flow name that is not registered adds nothing and returns 0.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `priority` | int | `100` | Higher runs first; 0 means the default 100 |
| `kind` | string |  | What to do, any case: CastAbility, CastItem, ClickCastBar, RawCommand, Movement or Flow. ApplyVerbCastBar and DialogChoices are not kinds here; OgreBotAPI.Actors:ApplyVerbIDQueued queues an apply-verb |
| `arg0` | string |  | Depends on kind: RawCommand the console command, CastAbility the ability id or name, CastItem the item name, ClickCastBar the actor id, Movement x,y,z with an optional precision, Flow the flow name |
| `arg1` | string |  | Depends on kind: CastAbility the target name (empty = current target), CastItem the equip slot (empty = the bag item by name), ClickCastBar the wait in tenths of a second (empty = 4 seconds), Flow its arguments |
| `ttlstart` | int | `0` | Milliseconds the entry may wait to start before it is dropped with status Expired; 0 = no limit |
| `ttlmax` | int | `0` | Milliseconds the entry may run before it is stopped with status Aborted; 0 = no limit |

**Returns:** int64: the new entry's seq (1 and up); 0 when the kind is unknown

```text
echo ${ISXOgreEQ2.Queue.Enqueue[100,RawCommand,"echo queued"]}
```

### `Entry`

`${ISXOgreEQ2.Queue.Entry[index]}`

One queue entry as a readable line, such as seq=12 prio=100 RawCommand waiting age=40ms arg0=echo hi, where seq is the entry's id. The index counts from 1, running entries first and then waiting ones, each sorted by priority then by the order they were added.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `index` | int |  | Position in the queue counting from 1: running entries first, then waiting ones, highest priority first |

**Returns:** string: the entry line; empty when the index is 0, past the end or missing

```text
echo ${ISXOgreEQ2.Queue.Entry[1]}
```

### `EntryJSON`

`${ISXOgreEQ2.Queue.EntryJSON[index]}`

One queue entry as a JSON object with seq, priority, kind, status (running or waiting), holds, haltQueue, haltCastStack, ageMs, blocked, arg0, arg1 and label. Same index as Entry, counting from 1, so a loop from 1 to Count reads the whole queue.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `index` | int |  | Position in the queue counting from 1: running entries first, then waiting ones, highest priority first |

**Returns:** string: the entry as a JSON object; {} when the index is 0, past the end or missing

```text
echo ${ISXOgreEQ2.Queue.EntryJSON[1]}
```

### `InFlight`

`${ISXOgreEQ2.Queue.InFlight}`

Whether any queue entry is running right now.

**Returns:** bool: TRUE when at least one entry is running; FALSE when none is

```text
echo ${ISXOgreEQ2.Queue.InFlight}
```

### `IsDone`

`${ISXOgreEQ2.Queue.IsDone[seq]}`

Whether the queue entry with that seq has finished in any way (Done, Failed, Expired, Aborted or Removed), so a wait loop never hangs on a failed entry; read Status for how it ended. A seq that finished and has since been forgotten also reads TRUE, while a seq never issued reads FALSE.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `seq` | int64 |  | The entry's id, from Enqueue or the seq= field of Entry and Spew |

**Returns:** bool: TRUE when the entry has finished, however it ended; FALSE while it is waiting or running, or when the seq was never issued

```text
echo ${ISXOgreEQ2.Queue.IsDone[1]}
```

### `Status`

`${ISXOgreEQ2.Queue.Status[seq]}`

The state of the queue entry with that seq. Unknown means the seq was never issued or finished too long ago to remember (only the most recent 256 are kept).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `seq` | int64 |  | The entry's id, from Enqueue or the seq= field of Entry and Spew |

**Returns:** string: Pending, InFlight, Done, Failed, Expired, Aborted, Removed or Unknown

```text
echo ${ISXOgreEQ2.Queue.Status[1]}
```

## Methods

### `Add`

`ISXOgreEQ2.Queue:Add[priority,kind,arg0,arg1,ttlstart,ttlmax]`

Adds an action to the priority queue, which runs it on its turn once the cast bar or movement it needs is free (highest priority first, even while OgreBot is paused), and prints an Add seq=N line to the console. Waiting and running entries are dropped on a zone change or when OgreBot ends, a Flow lives as its registered flow does, with that flow's holds and halts, and a flow name that is not registered gets one line; use the Enqueue member instead when you need the seq back.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `priority` | int | `100` | Higher runs first; 0 means the default 100 |
| `kind` | string |  | What to do, any case: CastAbility, CastItem, ClickCastBar, RawCommand, Movement or Flow. ApplyVerbCastBar and DialogChoices are not kinds here; OgreBotAPI.Actors:ApplyVerbIDQueued queues an apply-verb |
| `arg0` | string |  | Depends on kind: RawCommand the console command, CastAbility the ability id or name, CastItem the item name, ClickCastBar the actor id, Movement x,y,z with an optional precision, Flow the flow name |
| `arg1` | string |  | Depends on kind: CastAbility the target name (empty = current target), CastItem the equip slot (empty = the bag item by name), ClickCastBar the wait in tenths of a second (empty = 4 seconds), Flow its arguments |
| `ttlstart` | int | `0` | Milliseconds the entry may wait to start before it is dropped with status Expired; 0 = no limit |
| `ttlmax` | int | `0` | Milliseconds the entry may run before it is stopped with status Aborted; 0 = no limit. For a Flow it can only shorten the flow's own limit |

```text
ISXOgreEQ2.Queue:Add[100,RawCommand,"echo queued"]
```

### `Remove`

`ISXOgreEQ2.Queue:Remove[seq]`

Removes the waiting queue entry with that seq (its Status becomes Removed) and prints the result to the console. A running entry is not removed, and an unknown or missing seq only prints that there is no such entry.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `seq` | int64 |  | The entry's id, from Enqueue or the seq= field of Entry and Spew |

```text
ISXOgreEQ2.Queue:Remove[1]
```

### `Spew`

`ISXOgreEQ2.Queue:Spew`

Prints every queue entry to the console, running entries then waiting ones, one line each starting with its seq, then a line on how to remove one. Prints empty - 0 entries when the queue is empty.

```text
ISXOgreEQ2.Queue:Spew
```
