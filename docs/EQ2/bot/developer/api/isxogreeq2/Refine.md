# ISXOgreEQ2.Refine

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Methods

### `Bags`

`ISXOgreEQ2.Refine:Bags[bags...]`

Sets which carried bags (1 to 6) a refine run scans - bags 1 and 2 by default - and echoes the new list. A missing list is refused with a console line, anything that is not bag numbers, all or none prints the usage line and changes nothing, and the setting is not saved.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `bags...` | string |  | bag numbers 1 to 6, as separate arguments or one list such as 1,2,5; each digit is one bag, so 12 means bags 1 and 2; or all / none |

```text
ISXOgreEQ2.Refine:Bags[1,2,3]
```

### `Plan`

`ISXOgreEQ2.Refine:Plan`

A dry run: scans the selected bags with the current settings and prints each item a run would refine (bag, slot, quantity, name) and why the others were skipped. Nothing is refined, and out of the world it only prints a warning.

```text
ISXOgreEQ2.Refine:Plan
```

### `Rare`

`ISXOgreEQ2.Refine:Rare[value]`

Turns refining of Rare resources on or off (off by default) and echoes the new setting. A missing value is refused with a console line, a value that is not on or off prints the usage line, and the setting is not saved.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `value` | string |  | on or off (1 / 0 and true / false also work) |

```text
ISXOgreEQ2.Refine:Rare[off]
```

### `Raw`

`ISXOgreEQ2.Refine:Raw[value]`

Turns refining of Raw resources on or off (on by default) and echoes the new setting. A missing value is refused with a console line, a value that is not on or off prints the usage line, and the setting is not saved.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `value` | string |  | on or off (1 / 0 and true / false also work) |

```text
ISXOgreEQ2.Refine:Raw[on]
```

### `Reload`

`ISXOgreEQ2.Refine:Reload`

Re-reads the refiner's resource list now: the shipped files under Ogre/EQ2/Refine/default plus your own under OgreSave/EQ2/Refine/custom. It echoes how many resources loaded, and a warning for any file it could not read or when no files were found.

```text
ISXOgreEQ2.Refine:Reload
```

### `Rewards`

`ISXOgreEQ2.Refine:Rewards[value]`

When on, every reward window that appears while a refine run is in progress is accepted automatically - including ones unrelated to refining, such as a quest reward. Off by default; a missing value is refused with a console line, and the setting is not saved.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `value` | string |  | on or off (1 / 0 and true / false also work) |

```text
ISXOgreEQ2.Refine:Rewards[off]
```

### `Start`

`ISXOgreEQ2.Refine:Start`

Starts one background pass over the selected carried bags: for each Raw or Rare resource on the refiner's list (provisioner resources skipped) it uses your Refine ability, refines the item until the stack is gone or a try limit is reached, and answers the refine confirm window itself while the run lasts. It refuses with a console line when a run is already going, you are not in the world, the resource list is empty, you lack the Refine ability, or Raw and Rare are both off.

```text
ISXOgreEQ2.Refine:Start
```

### `Status`

`ISXOgreEQ2.Refine:Status`

Prints the refiner's state to the console: how many resources its list holds, whether Raw and Rare are on, which bags it scans, whether reward windows are auto-accepted, and the progress of a run in flight, then the usage line. The same as `ogre refine` or `ogre refine status`.

```text
ISXOgreEQ2.Refine:Status
```

### `Stop`

`ISXOgreEQ2.Refine:Stop`

Stops a refine run in progress, the same as `ogre end refine`. When nothing is running it prints "refine: not running." to the console.

```text
ISXOgreEQ2.Refine:Stop
```
