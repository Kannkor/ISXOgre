<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# ISXOgreEQ2.LootScan

## Methods

### `Interval`

`ISXOgreEQ2.LootScan:Interval[ms]`

Sets how often the driver scans, for this session only. A value out of range prints the range and changes nothing; with no value it prints one warning.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `ms` | int |  | The scan interval in milliseconds, 500 to 30000. |

```text
ISXOgreEQ2.LootScan:Interval[2000]
```

### `Reset`

`ISXOgreEQ2.LootScan:Reset`

Forgets which actors were looted, so they are looked at again.

```text
ISXOgreEQ2.LootScan:Reset
```

### `Status`

`ISXOgreEQ2.LootScan:Status`

Prints the auto-loot driver to the console: its gates, interval, last scan, what it opened and what it remembers.

```text
ISXOgreEQ2.LootScan:Status
```
