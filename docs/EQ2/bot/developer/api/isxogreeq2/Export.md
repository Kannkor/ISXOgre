# ISXOgreEQ2.Export

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Members

### `Busy`

`${ISXOgreEQ2.Export.Busy}`

TRUE from the moment an ability export starts until its file is written or the export is stopped. ISXOgreEQ2.Export:Abilities returns at once and runs in the background, so poll this to know when it is done.

**Returns:** bool: TRUE while an ability export is running; FALSE when none is.

```text
echo ${ISXOgreEQ2.Export.Busy}
```

### `Processed`

`${ISXOgreEQ2.Export.Processed}`

How many abilities the running export has processed so far - the count its progress window shows. Reads 0 when no export is running.

**Returns:** int: abilities processed so far by the running export; 0 when idle.

```text
echo ${ISXOgreEQ2.Export.Processed}
```

### `Total`

`${ISXOgreEQ2.Export.Total}`

How many abilities the running export will process in all. Reads 0 when no export is running.

**Returns:** int: abilities the running export will process; 0 when idle.

```text
echo ${ISXOgreEQ2.Export.Total}
```

## Methods

### `Abilities`

`ISXOgreEQ2.Export:Abilities[flag...]`

Starts the ability export in the background and returns at once: it reads each ability's game info one ability at a time (a server request per ability) and writes OgreSave/EQ2/OgreBot/AbilityExports/&lt;Server>_&lt;Name>_&lt;SubClass>.json, the file OgreBotAPI.Abilities loads. With no flags it is the standard export (no passives, no tradeskill, merged into the existing file); a call while one is running is ignored with a console line, and when it finishes OgreBot reloads its abilities unless -noreloadbot or -nosave was given.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `flag...` | string |  | optional flags in any order: -passive (include passives), -tradeskill (tradeskill export to the crafting XML files), -nodesc, -minlevel &lt;n>, -maxlevel &lt;n>, -j / -a / -e / -m / -gm / -ancient (lowest tier to keep), -new (fresh file, no merge), -na (only abilities not already in the file), -nosave (dry run, nothing written), -noreloadbot; a word that starts with - and is none of these is refused with one line and nothing starts; any other word is an ability ID or name to export only those (a name is looked up by name, a server request) |

```text
ISXOgreEQ2.Export:Abilities[-passive]
```

### `Config`

`ISXOgreEQ2.Export:Config[word...]`

The `ogre export` command: with no words it opens the Ability Export options panel, or brings it back if a run hid it. With words it runs, starts or stops the export - see the parameter for each.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `word...` | string |  | optional words, any order. The export's own flags, or an ability name or ID, run the export now with exactly those, as Abilities does (a flag that takes a value is followed by it; the panel's saved options are not used or changed). -start runs it now with the panel's options, refused while one is running; -default uses the default options for this call only, without saving them; stop stops a running export (these three: any case, leading dash optional). A dash word that is no flag is named on the console and nothing runs. |

```text
ISXOgreEQ2.Export:Config[stop]
```

### `End`

`ISXOgreEQ2.Export:End`

Stops a running ability export (nothing is written, and abilities are not reloaded) and closes the export options window - the same as `ogre end export` or either window's X. When nothing is running and nothing is open it does nothing and says nothing.

```text
ISXOgreEQ2.Export:End
```
