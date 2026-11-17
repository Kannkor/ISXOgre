# ISXOgreEQ2.InvOps

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Members

### `Busy`

`${ISXOgreEQ2.InvOps.Busy}`

TRUE while an inventory flow started through this object (Overflow, MoveBag or Trade) is running. Only one of the three runs at a time, and starting another while one runs is refused with a busy warning.

**Returns:** bool: TRUE while an overflow, bag move or trade flow is running; FALSE when idle.

```text
echo ${ISXOgreEQ2.InvOps.Busy}
```

### `Status`

`${ISXOgreEQ2.InvOps.Status}`

One line naming the running inventory flow and its progress, or "idle". It is the same text `${ISXOgreEQ2.InvOps}` returns.

**Returns:** string: "idle", "overflow (N popped)", "mbc (done/total)" or "trade (done/total)".

```text
echo ${ISXOgreEQ2.InvOps.Status}
```

## Methods

### `MoveBag`

`ISXOgreEQ2.InvOps:MoveBag[from,to]`

The engine behind `ogre mbc`: moves every item in carried bag `from` into bag `to`, one item every 0.2 s, where a bag's number is its inventory slot (1-6). It is refused with a console warning when a number is missing or out of range, both are the same bag, a slot holds no bag, the source bag is empty, or another inventory flow is running.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `from` | int |  | bag number (1-6) to empty |
| `to` | int |  | bag number (1-6) to move the items into |

```text
ISXOgreEQ2.InvOps:MoveBag[2,3]
```

### `Overflow`

`ISXOgreEQ2.InvOps:Overflow`

The engine behind `ogre overflow`: pops items out of the overflow window into your bags, one every 0.2 s, until the game says the overflow is empty or has no room, only one bag slot is left free, or 300 items have been popped. It returns at once and the work runs on later frames; it is refused with a console warning when another inventory flow is running or you are not in the world.

```text
ISXOgreEQ2.InvOps:Overflow
```

### `Stop`

`ISXOgreEQ2.InvOps:Stop`

Drops whichever overflow, bag move or trade flow is running, without printing anything; does nothing when idle. An open trade window is left as it is.

```text
ISXOgreEQ2.InvOps:Stop
```

### `Trade`

`ISXOgreEQ2.InvOps:Trade[count]`

The engine behind `ogre trade`: opens a trade with your current target, adds up to `count` whole stacks from your bags of the item you have EXAMINED (exact name, any case), then accepts. You need a target and an open examine window; when nothing is examined or no stack matches, the run rejects the trade it opened and ends with a console line.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `count` | int | `12` | most stacks to hand over; missing, not a whole number, or 0 or less uses 12 |

```text
ISXOgreEQ2.InvOps:Trade[4]
```
