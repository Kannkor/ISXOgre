# ISXOgreEQ2.NpcCast

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Methods

### `Capture`

`ISXOgreEQ2.NpcCast:Capture`

Asks for the cast your target is casting right now to be captured, the window's Capture button.

```text
ISXOgreEQ2.NpcCast:Capture
```

### `Clear`

`ISXOgreEQ2.NpcCast:Clear`

Empties your script watch list. Watches from zone data and encounters stay.

```text
ISXOgreEQ2.NpcCast:Clear
```

### `End`

`ISXOgreEQ2.NpcCast:End`

Stops the Monitor and closes the window, the same as `ogre end npccast` and the window's X. The watch list is left alone.

```text
ISXOgreEQ2.NpcCast:End
```

### `Import`

`ISXOgreEQ2.NpcCast:Import`

Copies the shipped OldBot conversions into your own NPC cast data, never overwriting a file you have.

```text
ISXOgreEQ2.NpcCast:Import
```

### `Monitor`

`ISXOgreEQ2.NpcCast:Monitor[word]`

The Monitor: starts it on a set of mobs, stops it, or acts on its rows. No word starts it on your target, and any word it does not know prints its status.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `word` | string |  | target, named, all or on start it; off or stop stop it; copy and clear act on its rows; status prints its state. Optional. |

```text
ISXOgreEQ2.NpcCast:Monitor[named]
```

### `Open`

`ISXOgreEQ2.NpcCast:Open`

Opens the NPC Cast Monitoring window, the same as bare `ogre npccast`.

```text
ISXOgreEQ2.NpcCast:Open
```

### `Radius`

`ISXOgreEQ2.NpcCast:Radius[n]`

Sets the scan radius for the script watch list. With no value it prints one warning and changes nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `n` | int |  | The radius in meters; required. |

```text
ISXOgreEQ2.NpcCast:Radius[80]
```

### `Reload`

`ISXOgreEQ2.NpcCast:Reload`

Asks for the zone data to be read from disk again.

```text
ISXOgreEQ2.NpcCast:Reload
```

### `Status`

`ISXOgreEQ2.NpcCast:Status`

Prints the Monitor's state, the scan counters and the watch list to the console, with who holds each watch and whether it is casting.

```text
ISXOgreEQ2.NpcCast:Status
```

### `Unwatch`

`ISXOgreEQ2.NpcCast:Unwatch[name]`

Takes a mob off your script watch list. With no name it prints one warning and changes nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | string |  | The mob's name; several words are joined into one name; required. |

```text
ISXOgreEQ2.NpcCast:Unwatch["Ancient Guardian"]
```

### `Watch`

`ISXOgreEQ2.NpcCast:Watch[name]`

Adds a mob to your script watch list. With no name it prints one warning and changes nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | string |  | The mob's name; several words are joined into one name; required. |

```text
ISXOgreEQ2.NpcCast:Watch["Ancient Guardian"]
```

### `Zone`

`ISXOgreEQ2.NpcCast:Zone`

Prints what the zone data says for this zone to the console.

```text
ISXOgreEQ2.NpcCast:Zone
```
