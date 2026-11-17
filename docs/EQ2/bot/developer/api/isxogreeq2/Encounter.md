<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# ISXOgreEQ2.Encounter

## Members

### `ActiveCount`

`${ISXOgreEQ2.Encounter.ActiveCount}`

The number of encounters that are setting up or running right now.

**Returns:** int: encounters in setup or active; 0 when none.

```text
echo ${ISXOgreEQ2.Encounter.ActiveCount}
```

### `Current`

`${ISXOgreEQ2.Encounter.Current}`

The encounters setting up or running right now, as a JSON array. Each entry has primary (the first named mob), state ("setup" or "active"), named (every named mob), expansion and zone.

**Returns:** string: a JSON array of the active encounters; "[]" when none.

```text
echo ${ISXOgreEQ2.Encounter.Current}
```

### `IsActive`

`${ISXOgreEQ2.Encounter.IsActive[mob]}`

Whether any loaded encounter naming that mob is setting up or running. The mob name is matched ignoring case, whatever zone you are in.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `mob` | string |  | The named mob's name. |

**Returns:** bool: TRUE when that mob's encounter is in setup or active; FALSE when it is not, when no encounter owns that name, or when no name is given.

```text
echo ${ISXOgreEQ2.Encounter.IsActive[${Target.Name}]}
```

### `Loaded`

`${ISXOgreEQ2.Encounter.Loaded}`

The number of encounter files loaded, across every zone. It changes when a reload or a zone-in picks up new or edited files.

**Returns:** int: the number of loaded encounters.

```text
echo ${ISXOgreEQ2.Encounter.Loaded}
```

### `Sequences`

`${ISXOgreEQ2.Encounter.Sequences}`

Every live encounter sequence as a JSON array, so you can see which step a fight is waiting on. Each entry names its encounter and holds either its condition rules or the list it is running (setup, a trigger and so on) with the current step.

**Returns:** string: a JSON array of live sequences; "[]" when none.

```text
echo ${ISXOgreEQ2.Encounter.Sequences}
```

### `Validation`

`${ISXOgreEQ2.Encounter.Validation}`

The answer of the last Encounter:Validate, as JSON: ok (true when the file would load), errors and warnings (how many), fileErrors and ruleErrors (the errors split: a file error stops the file from loading, a rule error does not), and issues - one for each line it printed, with the list, the rule and the step it belongs to (counted from 1), the message, and whether it is only a warning. Empty until Encounter:Validate has run.

**Returns:** string: JSON, for example {"ok":true,"errors":0,"warnings":0,"fileErrors":0,"ruleErrors":0,"issues":[]}; "" before the first Encounter:Validate.

```text
echo ${ISXOgreEQ2.Encounter.Validation}
```

More: [developer/zone-files/builder.md](../../zone-files/builder.md)

## Methods

### `Debug`

`ISXOgreEQ2.Encounter:Debug[switch,value]`

Turns the console echo of encounter messages (comms) or step changes (steps) on or off, then prints both settings; with no switch it only prints them - the same as `ogre encounter debug`. Both are always written to the log; an unknown switch or a missing on/off prints a warning and changes nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `switch` | string | `""` | comms or steps; blank just prints the current settings. |
| `value` | string | `""` | on or off; needed when switch is given. |

```text
ISXOgreEQ2.Encounter:Debug[steps,on]
```

### `Fire`

`ISXOgreEQ2.Encounter:Fire[mob]`

Sets up for an encounter on the next pulse: the fight of the named mob given, or with no name the nearest or engaged named in this zone; a setup already running is started again. It is OgreBotAPI.Bot:SetUpFor without the for-who, and it is ignored with a warning when Enable Raid Setups (raid zones) or Enable Heroic Setups (other zones) is off, or when no encounter owns that name.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `mob` | string | `""` | The named mob whose encounter to set up; blank picks the nearest or engaged named in this zone. |

```text
ISXOgreEQ2.Encounter:Fire[${Target.Name}]
```

### `Help`

`ISXOgreEQ2.Encounter:Help`

Prints the `ogre encounter` words (reload, debug and sequences) with one line each to the console, the same as typing a bare `ogre encounter`.

```text
ISXOgreEQ2.Encounter:Help
```

### `List`

`ISXOgreEQ2.Encounter:List`

Prints this zone's encounter coding to the console: one line per fight with its named mobs, (DISABLED) when switched off, and its file. It always answers, even "No encounter coding for this zone", and is OgreBotAPI.Encounter:List without the for-who.

```text
ISXOgreEQ2.Encounter:List
```

### `Reload`

`ISXOgreEQ2.Encounter:Reload`

Re-reads every encounter file from disk in the background and swaps the new set in when it is done, which ends every encounter setup and sequence in progress - the same as `ogre encounter reload`. It prints one line at once and a second with the loaded, scanned and error counts when the swap lands.

```text
ISXOgreEQ2.Encounter:Reload
```

### `Sequences`

`ISXOgreEQ2.Encounter:Sequences`

Prints the Sequences JSON to the console, or "(none live)" when nothing is running - the same as `ogre encounter sequences`.

```text
ISXOgreEQ2.Encounter:Sequences
```

### `Validate`

`ISXOgreEQ2.Encounter:Validate[root,path]`

Checks one fight file by the same rules the game uses when it loads fight files, and changes nothing: a file on disk by its root and path (the same as `ogre encounter validate`), or the base64 text of a fight file's JSON. It prints whether the file would load and each problem, and keeps the answer for Encounter.Validation.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `root` | string |  | The root the fight file is in: default or custom. With no path, this one argument is read as the base64 text of a fight file's JSON, checked as a new file of your own. |
| `path` | string | `none` | The fight file's path inside that root, ending in .json. A path with spaces may be quoted or written as several words. |

```text
ISXOgreEQ2.Encounter:Validate[custom,"My Zone/My Mob.json"]
```

More: [developer/zone-files/builder.md](../../zone-files/builder.md)
