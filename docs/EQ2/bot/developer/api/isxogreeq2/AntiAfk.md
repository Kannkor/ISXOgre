<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# ISXOgreEQ2.AntiAfk

## Methods

### `Help`

`ISXOgreEQ2.AntiAfk:Help`

Prints the `ogre afk` usage lines to the console. It changes nothing.

```text
ISXOgreEQ2.AntiAfk:Help
```

### `Invites`

`ISXOgreEQ2.AntiAfk:Invites[state]`

Turns automatic acceptance of group invites on or off: an invite is accepted from any name on your characters list (every account, auth-only names included), a switch separate from the keepalive that starts off at every load. A missing value is refused with a warning and nothing changes.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `state` | string |  | on, 1 or TRUE to accept; off, 0 or FALSE to stop |

```text
ISXOgreEQ2.AntiAfk:Invites[on]
```

### `Off`

`ISXOgreEQ2.AntiAfk:Off`

Stops the keepalive /who and prints "anti-AFK keepalive OFF" to the console (the same as `ogre end afk`). The group-invite switch set by AntiAfk:Invites is left as it is.

```text
ISXOgreEQ2.AntiAfk:Off
```

### `On`

`ISXOgreEQ2.AntiAfk:On[silent]`

Starts the keepalive, which sends `/who all <your name>` to the game right away and then again after a random 10 to 15 minutes, only while you are in the world, until AntiAfk:Off or the extension unloads. Calling it while it is already on changes only the verbosity, and any other value is refused with an error and the usage.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `silent` | string |  | 1 or TRUE for silent; 0 or FALSE to also print "Ogre Anti AFK" to the console each time; leave out to keep the current setting (silent until changed) |

```text
ISXOgreEQ2.AntiAfk:On[1]
```
