# ISXOgreEQ2.Experiment

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Methods

### `Boost`

`ISXOgreEQ2.Experiment:Boost[flag,count,...]`

Starts boosting the item already selected on the tradeskill window's Experiment tab, picking each queued stat and clicking Begin and the confirm dialog for every boost; it also turns on the crafting reaction handling. It refuses with a console line when you are not in the world, lack the Experiment AA, a run is already going or no stat is queued, and words it does not know are echoed and skipped.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `flag` | string |  | the stat to boost: -p, -pot or -potency for potency, -cb or -critbonus for crit bonus, or -&lt;stat> for any other stat label the game offers |
| `count` | int |  | how many boosts of that stat to queue |
| `...` | string |  | more flag, count pairs, run in the order given |

```text
ISXOgreEQ2.Experiment:Boost[-p,3,-cb,2]
```

### `Items`

`ISXOgreEQ2.Experiment:Items`

Lists the numbered item rows on the Experiment tab's item page to the console, briefly enlarging the tradeskill window to read them and then putting it back. It prints a warning instead when you are not in the world, lack the Experiment AA, a run is in progress or no list is showing.

```text
ISXOgreEQ2.Experiment:Items
```

### `Run`

`ISXOgreEQ2.Experiment:Run[row,flag,count,...]`

Boosts the item on row `row` of the Experiment item list (the numbers Items prints) with the same flags as Boost. A missing row, a row number out of range or no queued stat is refused with a console line and nothing starts.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `row` | int |  | the item row number from Experiment:Items, starting at 1 |
| `flag` | string |  | the stat to boost: -p, -pot or -potency, -cb or -critbonus, or -&lt;stat> for any other stat label |
| `count` | int |  | how many boosts of that stat to queue |
| `...` | string |  | more flag, count pairs, run in the order given |

```text
ISXOgreEQ2.Experiment:Run[2,-p,5]
```

### `Status`

`ISXOgreEQ2.Experiment:Status`

Prints the tradeskill experiment helper's state to the console: running or not, its last status, whether you have the Experiment AA, items done and skipped, boosts made, the last error and the usage lines. It is what a bare `ogre experiment` runs.

```text
ISXOgreEQ2.Experiment:Status
```

### `Stop`

`ISXOgreEQ2.Experiment:Stop`

Stops a running experiment and gives the tradeskill window back its size (the same as `ogre end experiment`). When nothing is running it only prints "experiment: not running" to the console.

```text
ISXOgreEQ2.Experiment:Stop
```
