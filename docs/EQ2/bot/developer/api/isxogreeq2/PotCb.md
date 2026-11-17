# ISXOgreEQ2.PotCb

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Methods

### `End`

`ISXOgreEQ2.PotCb:End`

Stops the Potency / Crit Bonus / Fervor sampler if it runs and always closes its panel, keeping the history. This is what `ogre end potcb` and the panel's X do.

```text
ISXOgreEQ2.PotCb:End
```

### `Help`

`ISXOgreEQ2.PotCb:Help`

Prints the `ogre potcb` usage to the console: open, on / off, status, reset and interval.

```text
ISXOgreEQ2.PotCb:Help
```

### `Interval`

`ISXOgreEQ2.PotCb:Interval[ms]`

Sets how often the sampler reads Potency, Crit Bonus and Fervor, held between 50 and 10000 ms (a negative is 50), and prints the new value. With no value it prints the current interval; a value that is not a number keeps the interval in force and says so.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `ms` | int |  | Sampling interval in milliseconds, 50 to 10000 (the sampler starts at 200). Optional: leave it out to print the current interval. |

```text
ISXOgreEQ2.PotCb:Interval[500]
```

### `Off`

`ISXOgreEQ2.PotCb:Off`

Stops the Potency / Crit Bonus / Fervor sampler and closes its panel, keeping the recorded history. If it was not sampling it prints "potcb: not running." and leaves the panel open.

```text
ISXOgreEQ2.PotCb:Off
```

### `On`

`ISXOgreEQ2.PotCb:On`

Starts the Potency / Crit Bonus / Fervor sampler, which reads the three stats every interval (default 200 ms) while you are in world, and prints one line saying so. Does nothing if it is already sampling, and does not open the panel.

```text
ISXOgreEQ2.PotCb:On
```

### `Open`

`ISXOgreEQ2.PotCb:Open`

Opens the Potency / Crit Bonus / Fervor tracker panel, starting the sampler first if it was stopped (the same as bare `ogre potcb`). If the panel is already up it stays as it is, and without the Ogre UI desktop it prints a warning while sampling still starts.

```text
ISXOgreEQ2.PotCb:Open
```

### `Reset`

`ISXOgreEQ2.PotCb:Reset`

Clears every recorded Potency / Crit Bonus / Fervor figure and the sampled time, then prints "potcb: history cleared". The sampler stays on or off as it was.

```text
ISXOgreEQ2.PotCb:Reset
```

### `Status`

`ISXOgreEQ2.PotCb:Status`

Prints every Potency / Crit Bonus / Fervor figure to the console: running or stopped and time sampled, then per stat the current value and peak, the in-combat min / avg / max, time at cap, time at peak and combat time by tenth of the peak, and the overall min / avg / max. It also warns when readings were skipped because a stat showed no number.

```text
ISXOgreEQ2.PotCb:Status
```
