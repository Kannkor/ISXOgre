<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# ISXOgreEQ2.Radar

## Methods

### `Budget`

`ISXOgreEQ2.Radar:Budget[n,ms]`

The read budget: how many actors a pulse may read their slow fields, and how old a slow field may get. With no argument it prints both; an age out of range is refused, but the actor count is still written.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `n` | int |  | Actors per pulse, 0-5000. Optional. |
| `ms` | int |  | The oldest a slow field may get, 0-600000 ms. Optional. |

```text
ISXOgreEQ2.Radar:Budget[60,3000]
```

### `Cap`

`ISXOgreEQ2.Radar:Cap[n]`

Draws only the nearest n blips, where 0 means no cap; it bounds what is drawn, not what is read. With no argument it prints the cap, and out of range is refused.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `n` | int |  | The cap, 0-5000. Optional. |

```text
ISXOgreEQ2.Radar:Cap[200]
```

### `CfgPath`

`ISXOgreEQ2.Radar:CfgPath`

Prints the path of the radar's settings file.

```text
ISXOgreEQ2.Radar:CfgPath
```

### `CfgSave`

`ISXOgreEQ2.Radar:CfgSave`

Writes the settings the panel left in the host store to the radar's settings file, and says whether it worked. The Save button sends this.

```text
ISXOgreEQ2.Radar:CfgSave
```

### `Chunk`

`ISXOgreEQ2.Radar:Chunk[n]`

Spreads a refresh over frames: n actors a frame, 0 to 500, where 0 means the whole refresh on one frame. With no argument it prints it.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `n` | int |  | Actors per frame, 0-500. Optional. |

```text
ISXOgreEQ2.Radar:Chunk[50]
```

### `Click`

`ISXOgreEQ2.Radar:Click[word]`

on lets the mouse pass through the panel to the game; off captures it again. A click-through panel can never be clicked back, so this is the way out.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `word` | string |  | on or off (any yes or no word). With neither it prints the usage. |

```text
ISXOgreEQ2.Radar:Click[off]
```

### `Dump`

`ISXOgreEQ2.Radar:Dump[n]`

Prints the first n blips of the last snapshot to the console.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `n` | int |  | How many. 10 when absent. |

```text
ISXOgreEQ2.Radar:Dump[25]
```

### `Fields`

`ISXOgreEQ2.Radar:Fields[word]`

full reads level, health and con on the slow budget; lean stops reading them, so they stop updating. It is not saved, and any other word prints the usage.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `word` | string |  | lean or full. |

```text
ISXOgreEQ2.Radar:Fields[lean]
```

### `Help`

`ISXOgreEQ2.Radar:Help`

Prints every radar word to the console, the same as `ogre radar help`.

```text
ISXOgreEQ2.Radar:Help
```

### `LoadTest`

`ISXOgreEQ2.Radar:LoadTest[range,labels,glide]`

Panel only: widens the zoom so that many blips are really drawn, for measuring a loaded panel.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `range` | int |  | The range to draw. 400 when absent. |
| `labels` | string |  | on to draw labels. Optional. |
| `glide` | string |  | on to glide. Optional. |

```text
ISXOgreEQ2.Radar:LoadTest[800,on,on]
```

### `MaxRate`

`ISXOgreEQ2.Radar:MaxRate[n]`

Never refreshes faster than n a second, where 0 means no ceiling and a number outside 0-240 is clamped. Without the number it prints the usage.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `n` | int |  | The ceiling. Required. |

```text
ISXOgreEQ2.Radar:MaxRate[30]
```

### `Off`

`ISXOgreEQ2.Radar:Off`

Stops scanning and closes the panel, the same as `ogre end radar` and the panel's X.

```text
ISXOgreEQ2.Radar:Off
```

### `On`

`ISXOgreEQ2.Radar:On`

Starts scanning and opens the panel, the same as bare `ogre radar`. On a radar already on and open it says nothing.

```text
ISXOgreEQ2.Radar:On
```

### `Panel`

`ISXOgreEQ2.Radar:Panel[word]`

The panel only, scanning left as it is: on opens it, off closes it, reload reads radar.html and radar.js from disk again. Any other word prints the usage.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `word` | string |  | on, off or reload. |

```text
ISXOgreEQ2.Radar:Panel[reload]
```

### `Parity`

`ISXOgreEQ2.Radar:Parity`

Prints every field of every blip in the last snapshot, one line each sorted by id, so two captures compare as a line diff. It reads the snapshot only.

```text
ISXOgreEQ2.Radar:Parity
```

### `Perf`

`ISXOgreEQ2.Radar:Perf[word]`

Prints the radar's cost report to the console. With reset it clears the counters, so the next report covers from now.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `word` | string |  | reset. Optional. |

```text
ISXOgreEQ2.Radar:Perf
```

### `Push`

`ISXOgreEQ2.Radar:Push[word]`

off stops handing snapshots to the panel while refreshes still run, so Perf shows the data cost alone; on hands them over again.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `word` | string |  | on or off (any yes or no word). With neither it prints the usage. |

```text
ISXOgreEQ2.Radar:Push[off]
```

### `Quest`

`ISXOgreEQ2.Radar:Quest[word]`

on makes the radar read UpdatesMyQuest for the panel's quest-only filter and off stops it, so it costs nothing unless it is used. With no argument it prints the setting.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `word` | string |  | on or off. Optional. |

```text
ISXOgreEQ2.Radar:Quest[on]
```

### `QuestNpc`

`ISXOgreEQ2.Radar:QuestNpc[word]`

on makes the radar find quest NPCs for the panel's quest NPC filter and off stops it. With no argument it prints the setting.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `word` | string |  | on or off. Optional. |

```text
ISXOgreEQ2.Radar:QuestNpc[on]
```

### `Radius`

`ISXOgreEQ2.Radar:Radius[n]`

Sets the display radius in game units; the panel applies it, so no game read is saved. With no argument it prints the radius, and out of range is refused.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `n` | int |  | The radius, 5-500. Optional. |

```text
ISXOgreEQ2.Radar:Radius[150]
```

### `Rate`

`ISXOgreEQ2.Radar:Rate[hz]`

Sets refreshes per second, where 0 means every pulse. With no argument it prints the rate, and out of range is refused.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `hz` | int |  | The rate, 0-60. Optional. |

```text
ISXOgreEQ2.Radar:Rate[20]
```

### `Reload`

`ISXOgreEQ2.Radar:Reload`

Reads radar.html and radar.js from disk again and redraws the panel, with no rebuild and no client restart.

```text
ISXOgreEQ2.Radar:Reload
```

### `Scan`

`ISXOgreEQ2.Radar:Scan`

Forces one refresh on the next pulse, ignoring the rate.

```text
ISXOgreEQ2.Radar:Scan
```

### `Settings`

`ISXOgreEQ2.Radar:Settings`

Opens the panel's settings drawer and forces mouse capture on while it is open, so it works on a click-through or borderless panel.

```text
ISXOgreEQ2.Radar:Settings
```

### `Shake`

`ISXOgreEQ2.Radar:Shake[word,rotate]`

Panel only: synthetic blip motion every tick, no running required. on starts it, anything else stops it; a second argument of on rotates as well.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `word` | string |  | on or off (any yes or no word). With neither it prints the usage. |
| `rotate` | string |  | on to rotate too. Optional. |

```text
ISXOgreEQ2.Radar:Shake[on,on]
```

### `Status`

`ISXOgreEQ2.Radar:Status`

Prints the radar's state to the console: scanning, panel, push, radius, rate, fields, chunk and cap, what the rate really works out to, where the actors come from, the last snapshot and the settings file.

```text
ISXOgreEQ2.Radar:Status
```

### `Target`

`ISXOgreEQ2.Radar:Target[id]`

Targets an actor through the targeting arbiter on the radar's next pulse: what a blip click sends. No id prints the usage; an id that reads as 0 is refused.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `id` | string |  | The actor id. Required. |

```text
ISXOgreEQ2.Radar:Target[12345]
```

### `TestPattern`

`ISXOgreEQ2.Radar:TestPattern[word]`

A pink dot orbits the scope on the panel's own clock, with no game data, so the eye can judge the panel's smoothness alone.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `word` | string |  | on or off (any yes or no word). With neither it prints the usage. |

```text
ISXOgreEQ2.Radar:TestPattern[on]
```

### `Toggle`

`ISXOgreEQ2.Radar:Toggle`

Turns the radar on with its panel if it is off, and off if it is on.

```text
ISXOgreEQ2.Radar:Toggle
```

### `TypeLive`

`ISXOgreEQ2.Radar:TypeLive[word]`

on reads Type every pass, so a corpse draws as a corpse on the next refresh; off puts Type on the slow budget. With no argument it prints the setting.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `word` | string |  | on or off. Optional. |

```text
ISXOgreEQ2.Radar:TypeLive[on]
```

### `UiDump`

`ISXOgreEQ2.Radar:UiDump[word]`

Prints what the panel itself reports: draw rate, render cost and JS errors, or says it has published nothing. With reset it clears the panel's held peaks.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `word` | string |  | reset. Optional. |

```text
ISXOgreEQ2.Radar:UiDump
```

### `UiEcho`

`ISXOgreEQ2.Radar:UiEcho[words]`

Prints its words to the console: the panel's way of putting a value where a redirect can capture it.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `words` | string |  | What to print, joined with spaces. |

```text
ISXOgreEQ2.Radar:UiEcho[hello]
```

### `UiReset`

`ISXOgreEQ2.Radar:UiReset`

Puts the panel's look back to its defaults, for a look that left nothing on screen to click. It is not saved until you press Save in the drawer.

```text
ISXOgreEQ2.Radar:UiReset
```

### `Verify`

`ISXOgreEQ2.Radar:Verify`

Compares the held actor index against a fresh scan and names any drift on the console; on drift it rebuilds the index and clears the radar's field cache. The Verify button sends this.

```text
ISXOgreEQ2.Radar:Verify
```
