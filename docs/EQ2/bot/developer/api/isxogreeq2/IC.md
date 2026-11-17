# ISXOgreEQ2.IC

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Members

### `FileArgs`

`${ISXOgreEQ2.IC.FileArgs}`

The IC File Args text from the IC window (or set with IC:SetFileArgs or the -fileArgs option). A running zone also sees it in its values as options.fileArgs.

**Returns:** string: the IC File Args text; "" when none.

```text
echo ${ISXOgreEQ2.IC.FileArgs}
```

### `FileOption`

`${ISXOgreEQ2.IC.FileOption[n]}`

Whether IC File Option n (1, 2 or 3) is ticked in the IC window; what each one means is up to the zone file. Any n outside 1-3 reads NULL.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `n` | int |  | which IC File Option, 1 to 3 |

**Returns:** bool: TRUE when that option is ticked; FALSE when not; NULL for n outside 1-3.

```text
echo ${ISXOgreEQ2.IC.FileOption[1]}
```

### `FileOptionLabel`

`${ISXOgreEQ2.IC.FileOptionLabel[n]}`

The text the IC window shows for IC File Option n: a label set with IC:SetFileOptionLabel, else the zone file's own label (the running file, else the one selected in the window), else "IC File Option n". Any n outside 1-3 reads NULL.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `n` | int |  | which IC File Option, 1 to 3 |

**Returns:** string: the option's label as shown; NULL for n outside 1-3.

```text
echo ${ISXOgreEQ2.IC.FileOptionLabel[2]}
```

### `Loaded`

`${ISXOgreEQ2.IC.Loaded}`

The number of zone files IC has loaded. It reads 0 until IC first reads its folders, which happens on Reload or the first IC call that needs them (reading this member does not load them).

**Returns:** int: how many zone files are loaded; 0 before the first load.

```text
echo ${ISXOgreEQ2.IC.Loaded}
```

### `MaxWait`

`${ISXOgreEQ2.IC.MaxWait}`

Max wait per zone, in seconds (default 3600, saved with the IC settings); 0 waits forever. A zone script still running past it is scored failed (the script itself is not ended) and a steps zone is stopped, and time spent with IC paused or staying in zone until a zone is ready does not count.

**Returns:** int: seconds a zone may run; 0 means no limit.

```text
echo ${ISXOgreEQ2.IC.MaxWait}
```

### `Note`

`${ISXOgreEQ2.IC.Note}`

Why the current or last run ended, such as "reported complete", a failure reason or "by user" after a stop. It is cleared when a new run starts.

**Returns:** string: the end reason of the last run; "" while a run is going or before any.

```text
echo ${ISXOgreEQ2.IC.Note}
```

### `Paused`

`${ISXOgreEQ2.IC.Paused}`

Whether IC's own pause is on (set by Pause, the IC window, a halt at end of zone or a no-trade shiny). This is not OgreBot's pause.

**Returns:** bool: TRUE while IC is paused; FALSE otherwise.

```text
echo ${ISXOgreEQ2.IC.Paused}
```

### `RunId`

`${ISXOgreEQ2.IC.RunId}`

The id of the current or last run, a short hex text that is new each time a zone file starts. The run's values are also saved as OgreSave/EQ2/IC/runs/&lt;RunId>.json.

**Returns:** string: the current or last run's id; "" before any zone has started.

```text
echo ${ISXOgreEQ2.IC.RunId}
```

### `Running`

`${ISXOgreEQ2.IC.Running}`

Whether a run is in flight: TRUE while IC is zoning in, launching a zone script or running a zone. FALSE when idle, done or failed.

**Returns:** bool: TRUE while a run is zoning in, launching or running; FALSE otherwise.

```text
echo ${ISXOgreEQ2.IC.Running}
```

### `RunState`

`${ISXOgreEQ2.IC.RunState}`

Where the current or last run stands, as a word: idle, zoning in, launching, running, done or failed.

**Returns:** string: "idle", "zoning in", "launching", "running", "done" or "failed".

```text
echo ${ISXOgreEQ2.IC.RunState}
```

### `State`

`${ISXOgreEQ2.IC.State}`

IC's whole state as JSON text: zone files loaded and skipped, its folders, both pauses, the run (state, id, zone, script, step, verdict, max wait), the list and the lockout table. A bare ${ISXOgreEQ2.IC} returns the same text.

**Returns:** string: IC's state as one JSON object.

```text
echo ${ISXOgreEQ2.IC.State}
```

### `Value`

`${ISXOgreEQ2.IC.Value[key]}`

The run's values that IC publishes for the zone file to read (zone, options, run, list, group and more): bare, the whole document as JSON text; with a key, one dotted key such as zone.fullName or run.completed.1 (arrays count from 1, keys are case-sensitive). True/false values read TRUE or FALSE, objects and arrays read as JSON text, an absent key reads NULL and a key that holds empty text reads empty.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `key` | string |  | a dotted key into the values, such as zone.fullName or options.fileArgs; leave it off for the whole document |

**Returns:** string: the whole values document as JSON, or one value as text; NULL before any run, for an absent key, or for a key that holds empty text.

```text
echo ${ISXOgreEQ2.IC.Value[zone.fullName]}
```

### `Verdict`

`${ISXOgreEQ2.IC.Verdict}`

The run's verdict: idle (nothing has run), pending (a run is in flight), completed, completedWithFailures (a steps zone ended but a step did not do its job) or failed. A skipped zone and a stopped zone script run read completed, while a stopped steps zone or a stopped zone-in reads failed.

**Returns:** string: "idle", "pending", "completed", "completedWithFailures" or "failed".

```text
echo ${ISXOgreEQ2.IC.Verdict}
```

### `Zone`

`${ISXOgreEQ2.IC.Zone}`

The full zone name (with its difficulty) of the current or last run. It is set when a zone file starts, so while IC is still zoning in it names the last zone.

**Returns:** string: the run's full zone name; "" before any zone has started.

```text
echo ${ISXOgreEQ2.IC.Zone}
```

### `ZoneEnd`

`${ISXOgreEQ2.IC.ZoneEnd}`

Where a script zone's zone end stands after it called IC:ZoneEnd: none (not asked), busy (calling the group to the guild hall or staying in the zone), halted (halt at end of zone, waiting for Resume), zoneOut (zone out now), calledGH (the group is in the guild hall, so do not zone out) or ghFailed (the call failed; end the zone as usual). It goes back to none when a new run starts or the run is stopped.

**Returns:** string: "none", "busy", "halted", "zoneOut", "calledGH" or "ghFailed".

```text
echo ${ISXOgreEQ2.IC.ZoneEnd}
```

## Methods

### `Check`

`ISXOgreEQ2.IC:Check[zone]`

Prints which zone files claim a zone (exact or prefix match) and whether the zone is available according to the lockout table; no zone means the one you are in. When the table is out of date it asks for a fresh read and says to ask again shortly, except while IC is paused, you are out of the world or a read is already pending, when it only says the table is not fresh.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `zone` | string |  | the zone name to check; leave it off for your current zone |

```text
ISXOgreEQ2.IC:Check["${Zone.Name}"]
```

### `Complete`

`ISXOgreEQ2.IC:Complete[note]`

For a zone run by a script: marks the run completed, so it is scored COMPLETED when the script exits, while a script that exits without calling this is scored FAILED. It does not end the run, prints nothing, does nothing when no run is in flight, and a steps zone, which completes itself, refuses it with one line.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `note` | string |  | optional text kept as the run's note; empty gives "reported complete" |

```text
ISXOgreEQ2.IC:Complete["all nameds killed"]
```

### `End`

`ISXOgreEQ2.IC:End`

Closes IC out, the same as the IC window's X and `ogre end ic`: the window closes, IC's pause clears, and a running zone and list stop as with Stop. Unlike Stop it does not cancel end-of-list actions already under way and says nothing when nothing is running.

```text
ISXOgreEQ2.IC:End
```

### `Fail`

`ISXOgreEQ2.IC:Fail[reason]`

Ends the current run at once as FAILED with the reason, printed on the console; a zone script keeps running, a steps zone stops at its current step without its exit steps, and a zone-in stops its route. Does nothing when no run is in flight.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `reason` | string |  | why it failed; empty gives "the script reported failure", or on a steps zone "IC:Fail was called with no reason" |

```text
ISXOgreEQ2.IC:Fail["group member missing"]
```

### `List`

`ISXOgreEQ2.IC:List[filter]`

Prints every loaded zone file (folder, path, zone, difficulties, and [delegates] for one that hands off to another file or a script) and a count. A filter keeps only files whose zone or path contains it, any case, with its words joined by a space.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `filter` | string |  | text to match in the zone name or file path; leave it off to list all |

```text
ISXOgreEQ2.IC:List[Zobboz]
```

### `Open`

`ISXOgreEQ2.IC:Open`

Opens the IC window, the same as `ogre ic`. Already open does nothing, and it warns when the UI host is not available.

```text
ISXOgreEQ2.IC:Open
```

### `Options`

`ISXOgreEQ2.IC:Options[switches...]`

Sets IC options by switch: -&lt;option> turns a tick-box on and -&lt;option>=off turns it off (on, off, true, false, 1, 0, yes or no, any case), while -afterWipe=, -maxWait=, -fileArgs= and -stopAfterZone take values. No argument prints every option and its state; changes are saved and reported in one line, and switches that could not be set are listed.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `switches...` | string |  | one or more option switches, each starting with - |

```text
ISXOgreEQ2.IC:Options[-loop,-skipShinies=off,-maxWait=5400]
```

### `Pause`

`ISXOgreEQ2.IC:Pause`

Turns on IC's own pause, which stops IC moving the zone and the list along while OgreBot, and any fight already under way, keep going. Prints "IC PAUSED" when it changes, and time paused does not count against the max wait.

```text
ISXOgreEQ2.IC:Pause
```

### `Queue`

`ISXOgreEQ2.IC:Queue[action,args...]`

Edits the IC list: add,&lt;tier>,&lt;path>, add,&lt;tier>,&lt;zone name> or add,&lt;zone name> adds a zone file, startat,&lt;row>,&lt;N> makes that row start at step N (N of 1 or less clears it), and clear empties the list. No action, or any other word, prints the list, and add or startat without their arguments is refused.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `action` | string |  | add, startat or clear; anything else or nothing prints the list |
| `args...` | string |  | the action's arguments: a tier and path or a zone name for add, a row and step number for startat |

```text
ISXOgreEQ2.IC:Queue[add,default,"Rage of Cthurath/_04_Zon_Zobboz_The_Graftwerk.json"]
```

### `Refresh`

`ISXOgreEQ2.IC:Refresh`

Marks IC's cached zone lockout table out of date, so the next check reads it from the game again. Prints "lock table invalidated - it re-seeds on the next check".

```text
ISXOgreEQ2.IC:Refresh
```

### `Reload`

`ISXOgreEQ2.IC:Reload`

Re-reads every zone file from IC's folders and prints "N zone(s) from M file(s) - X skipped, Y warning(s)". Same as the IC window's Reload and `ogre ic reload`.

```text
ISXOgreEQ2.IC:Reload
```

### `Resume`

`ISXOgreEQ2.IC:Resume`

Clears IC's own pause and prints "IC resumed" when it changes. It is also how you go on after a halt at end of zone or a pause for a no-trade shiny.

```text
ISXOgreEQ2.IC:Resume
```

### `Run`

`ISXOgreEQ2.IC:Run[tier,relPath]`

Starts one zone file (not the list): when you are not in its zone and the travel data knows the way, IC first takes the group there, then a zone that hands off to a script launches it with no arguments (the script reads ${ISXOgreEQ2.IC.Value}) and a steps zone runs its own steps. It refuses with a console line when you are not in the world, a run is already in flight, IC is paused, OgreBot has no profile loaded, or the file is missing, not valid or disabled.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `tier` | string |  | which zone file folder: default (the shipped files) or custom (your own, under OgreSave/EQ2/IC/custom) |
| `relPath` | string |  | the zone file's path inside that folder; further arguments are joined to it with a space |

```text
ISXOgreEQ2.IC:Run[default,"Rage of Cthurath/_04_Zon_Zobboz_The_Graftwerk.json"]
```

### `RunList`

`ISXOgreEQ2.IC:RunList[row]`

Starts the queued list from a row (1-based, default the top); a row the queue does not have, or one that is not a number, prints "no row N (the queue has M)" and starts nothing. It refuses with a console line when you are not in the world, a run or the end-of-list actions are still going, or the queue is empty.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `row` | int | `1` | the list row to start at, counting from 1 |

```text
ISXOgreEQ2.IC:RunList[2]
```

### `SetFileArgs`

`ISXOgreEQ2.IC:SetFileArgs[text]`

Sets the IC File Args text and saves it; no argument clears it. Only the first argument is used, so quote text that holds commas.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `text` | string |  | the new IC File Args text; empty clears it |

```text
ISXOgreEQ2.IC:SetFileArgs["fast loot"]
```

### `SetFileOptionLabel`

`ISXOgreEQ2.IC:SetFileOptionLabel[n,text]`

Sets the text the IC window shows for IC File Option n (1-3); empty text goes back to the zone file's own label or "IC File Option n". The label is cleared when the next zone starts, and n outside 1-3 prints a warning.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `n` | int |  | which IC File Option, 1 to 3 |
| `text` | string |  | the label to show; empty restores the default |

```text
ISXOgreEQ2.IC:SetFileOptionLabel[1,"Kill the optional named"]
```

### `SetMaxWait`

`ISXOgreEQ2.IC:SetMaxWait[seconds]`

Sets Max wait per zone in seconds and saves it; 0 waits forever. A fraction rounds up, a number below 0 becomes 1 and a huge one is held at the largest value, while text that is not a number (or no argument) changes nothing, each with a console line.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `seconds` | number |  | seconds a zone may run; 0 means no limit |

```text
ISXOgreEQ2.IC:SetMaxWait[5400]
```

### `Status`

`ISXOgreEQ2.IC:Status`

Prints IC's report on the console: zone files loaded and their folders, both pauses, the lockout table, the run, its verdict and max wait, the current step, the list and the options that are on. Same as `ogre ic status`.

```text
ISXOgreEQ2.IC:Status
```

### `Stop`

`ISXOgreEQ2.IC:Stop`

Stops the run and the list where they stand and clears IC's pause: a zone script is no longer tracked but is NOT ended, and a steps zone stops at its current step without running its exit steps. With nothing running it cancels end-of-list actions still under way, or prints "nothing is running" (same as the IC window's End and `ogre ic stop`).

```text
ISXOgreEQ2.IC:Stop
```

### `Value`

`ISXOgreEQ2.IC:Value[key]`

Prints the run's values on the console: no key prints the whole document and the path of its saved copy, a dotted key prints one value, "" (empty) for empty text, or "NULL (absent)". Before any run it prints "no values - nothing has run yet"; a script reads values with ${ISXOgreEQ2.IC.Value[key]} instead.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `key` | string |  | a dotted key such as zone.fullName; leave it off to print the whole document |

```text
ISXOgreEQ2.IC:Value[zone.fullName]
```

### `Wipe`

`ISXOgreEQ2.IC:Wipe`

Declares a wipe now: a steps zone that is running its enter or steps list stops and runs its wipe recovery. Out of the world, or with no such zone running, it prints why and does nothing.

```text
ISXOgreEQ2.IC:Wipe
```

### `ZoneEnd`

`ISXOgreEQ2.IC:ZoneEnd`

Called by a zone script where it would zone out: IC runs the zone end a steps zone gets (halt at end of zone, then Call to GH after each zone or Stay in zone until a zone is ready, as ticked), and the script then reads ${ISXOgreEQ2.IC.ZoneEnd} until it is not busy or halted. With no zone script running, or on a steps zone, it prints a warning and does nothing.

```text
ISXOgreEQ2.IC:ZoneEnd
```
