<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# ISXOgreEQ2.BgRender

## Members

### `Enabled`

`${ISXOgreEQ2.BgRender.Enabled}`

Whether background render skipping is turned on (ogre bgrender on). On does not mean it is skipping right now - see Skipping.

**Returns:** bool: TRUE after :On, FALSE after :Off and when the extension loads.

```text
echo ${ISXOgreEQ2.BgRender.Enabled}
```

### `Held`

`${ISXOgreEQ2.BgRender.Held[name]}`

Whether a hold stops BgRender from skipping draws. With no name it asks whether any hold is in place; with a name, whether that one is.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | string | `""` | the hold to ask about; leave it out to ask whether any hold is in place |

**Returns:** bool: TRUE when that hold (or any hold) is in place.

```text
echo ${ISXOgreEQ2.BgRender.Held[Crafting]}
```

### `Holds`

`${ISXOgreEQ2.BgRender.Holds}`

How many holds are in place. BgRender skips draws only while this is 0.

**Returns:** int: the number of distinct holds.

```text
echo ${ISXOgreEQ2.BgRender.Holds}
```

### `Skipping`

`${ISXOgreEQ2.BgRender.Skipping}`

Whether BgRender is skipping draws at this moment: it is on, nothing holds it, your character is settled in the world, and this client is in the background (or Force is on).

**Returns:** bool: TRUE while draws are being skipped; FALSE while every frame is drawn.

```text
echo ${ISXOgreEQ2.BgRender.Skipping}
```

## Methods

### `Clear`

`ISXOgreEQ2.BgRender:Clear`

Removes every hold, whoever added it.

```text
ISXOgreEQ2.BgRender:Clear
```

### `Draw`

`ISXOgreEQ2.BgRender:Draw[ms]`

Sets how often a background client still draws one frame, so its window or thumbnail keeps updating. Values are held between 0 and 60000.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `ms` | int | `1000` | milliseconds between background draws; 0 never draws while in the background |

```text
ISXOgreEQ2.BgRender:Draw[1000]
```

### `Force`

`ISXOgreEQ2.BgRender:Force[onoff]`

Treats this client as a background one even while it is the foreground window, so you can watch the effect on the window in front of you. For testing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `onoff` | string | `off` | on or off (also TRUE / FALSE or 1 / 0) |

```text
ISXOgreEQ2.BgRender:Force[on]
```

### `Hold`

`ISXOgreEQ2.BgRender:Hold[name]`

Adds a named hold: while any hold is in place every frame is drawn, as if BgRender were off. Use it around anything that needs the screen drawn and release the same name after; holding a name twice is one hold.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | string |  | your hold's name - any text; each caller releases only its own name |

```text
ISXOgreEQ2.BgRender:Hold[Crafting]
```

### `Hz`

`ISXOgreEQ2.BgRender:Hz[n]`

Sets the most loops per second a background client runs while it is skipping draws, so a loop with no draw cannot spin a core. The bot runs once per loop, so a low value also slows the bot.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `n` | int | `100` | loops per second, held between 0 and 1000; 0 is no cap |

```text
ISXOgreEQ2.BgRender:Hz[100]
```

### `Off`

`ISXOgreEQ2.BgRender:Off`

Turns background render skipping off (`ogre end bgrender`): every frame is drawn again. The hook stays installed but does nothing until :On.

```text
ISXOgreEQ2.BgRender:Off
```

### `On`

`ISXOgreEQ2.BgRender:On`

Turns background render skipping on and prints the status; while this client is the foreground window every frame is still drawn. The first time, it finds and hooks the game's draw function, and if that fails (for example after a game patch) it says why and stays off.

```text
ISXOgreEQ2.BgRender:On
```

### `Release`

`ISXOgreEQ2.BgRender:Release[name]`

Removes the named hold; when no hold is left, BgRender may skip draws again. Releasing a name that is not held does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | string |  | the hold to remove |

```text
ISXOgreEQ2.BgRender:Release[Crafting]
```

### `Status`

`ISXOgreEQ2.BgRender:Status`

Prints BgRender's state (`ogre bgrender`): on or off, the draw interval and loop cap, whether the draw hook is installed, whether it is skipping now and if not why (off, held, world not settled, foreground), the holds, and the last second's loop, draw and skip counts.

```text
ISXOgreEQ2.BgRender:Status
```
