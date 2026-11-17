# ISXOgreEQ2.OgreBot

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Members

### `Character`

`${ISXOgreEQ2.OgreBot.Character}`

The character whose OgreBot profile is loaded.

**Returns:** string: the character name; empty when nothing is loaded.

```text
echo ${ISXOgreEQ2.OgreBot.Character}
```

### `Count`

`${ISXOgreEQ2.OgreBot.Count}`

How many single control values the loaded profile holds (checkboxes, text boxes, combo boxes). List sections such as the Cast Stack are not counted.

**Returns:** int: the number of stored control values; 0 when nothing is loaded.

```text
echo ${ISXOgreEQ2.OgreBot.Count}
```

### `Dirty`

`${ISXOgreEQ2.OgreBot.Dirty}`

TRUE when the loaded profile has changes that are not saved to disk yet. Only Save writes them; closing OgreBot, Reload, or loading another profile drops them.

**Returns:** bool: TRUE when there are unsaved changes; FALSE when there are none or nothing is loaded.

```text
echo ${ISXOgreEQ2.OgreBot.Dirty}
```

### `IsReady`

`${ISXOgreEQ2.OgreBot.IsReady}`

TRUE when OgreBot is up: its main window or mini toolbar is open AND a profile is loaded. This is the check the bot's own features use before they act.

**Returns:** bool: TRUE when a window is open and a profile is loaded; FALSE otherwise.

```text
echo ${ISXOgreEQ2.OgreBot.IsReady}
```

### `Loaded`

`${ISXOgreEQ2.OgreBot.Loaded}`

TRUE while an OgreBot profile is loaded for this session. Closing OgreBot unloads the profile, so this goes FALSE on close.

**Returns:** bool: TRUE when a profile is loaded; FALSE when none is.

```text
echo ${ISXOgreEQ2.OgreBot.Loaded}
```

### `PanelVisible`

`${ISXOgreEQ2.OgreBot.PanelVisible}`

TRUE when the OgreBot main window or the mini toolbar is open, whether or not a profile is loaded. Use IsReady to ask whether the bot can run.

**Returns:** bool: TRUE when either window is open; FALSE when both are closed.

```text
echo ${ISXOgreEQ2.OgreBot.PanelVisible}
```

### `Profile`

`${ISXOgreEQ2.OgreBot.Profile}`

The name of the loaded OgreBot profile, in the spelling stored in the profile file.

**Returns:** string: the profile name; empty when nothing is loaded.

```text
echo ${ISXOgreEQ2.OgreBot.Profile}
```

### `Value`

`${ISXOgreEQ2.OgreBot.Value[id]}`

The stored value of one OgreBot window control, read from the loaded profile in memory (unsaved changes included). The id must match exactly; OgreBotAPI.Options.Value is the case-insensitive version.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `id` | string |  | the control id (the same id the profile saves it under), for example checkbox_settings_enablealiases |

**Returns:** string: the control's value as text; empty when the id is not stored, no id is given, or nothing is loaded.

```text
echo ${ISXOgreEQ2.OgreBot.Value[checkbox_settings_enablealiases]}
```

## Methods

### `Alias`

`ISXOgreEQ2.OgreBot:Alias[verb,arg1,arg2,arg3,arg4]`

Edits the loaded profile's custom aliases in memory (Save keeps them) and refreshes the Aliases tab and Target list; names get a leading * if they lack one, and add refuses only the same name with the same For. Verbs are display (print what each alias resolves to now), add or edit (name,For,NoRaid), del (name), delat or toggle (index), editat (index,name,For,NoRaid) and move (from,to) with 0-based indexes, it does nothing with no profile loaded, and OgreBotAPI.ForWho:AddAlias and RemoveAlias use this same editor.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `verb` | string |  | display, add, edit, del, delat, editat, toggle or move |
| `arg1` | string |  | the alias name (add, edit, del) or a 0-based row index (delat, editat, toggle, move) |
| `arg2` | string |  | the For value (add, edit; an empty one on edit clears it), the new name (editat) or the target index (move) |
| `arg3` | string |  | No-Raid as a yes/no word (add, edit) or the For value (editat) |
| `arg4` | bool |  | editat only: No-Raid |

```text
ISXOgreEQ2.OgreBot:Alias[add,Healer,${Group[1].Name},FALSE]
```

### `Close`

`ISXOgreEQ2.OgreBot:Close`

Closes OgreBot entirely: both windows close, the profile is unloaded (unsaved changes are dropped with a warning in the console), travel routes stop, and follow and camp spots are cleared unless OgreBotAPI.Movement:UseWithoutOgreBot is on. It is the same close as the X on either window, `ogre end bot` and OgreBotAPI.Bot:End.

```text
ISXOgreEQ2.OgreBot:Close
```

### `CreateProfile`

`ISXOgreEQ2.OgreBot:CreateProfile[name]`

Makes a new profile from the current settings, unsaved changes included, writes it to disk and switches to it. It fails with a console line when the name is already used (case does not matter).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | string |  | the new profile's name; a b64: prefix marks a base64 name |

```text
ISXOgreEQ2.OgreBot:CreateProfile[Solo]
```

### `DeleteProfile`

`ISXOgreEQ2.OgreBot:DeleteProfile[name]`

Deletes a named profile from the character's profile file on disk. It refuses, with a console line, the loaded profile, the default profile, the last remaining profile and a name that does not exist.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | string |  | the profile name (case does not matter); a b64: prefix marks a base64 name |

```text
ISXOgreEQ2.OgreBot:DeleteProfile[Solo]
```

### `Dump`

`ISXOgreEQ2.OgreBot:Dump[path]`

Writes every stored control value of the loaded profile (unsaved changes included) to a JSON file and prints the count and path. List sections such as the Cast Stack are not included, and the file is overwritten each time.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `path` | string |  | the file to write |

```text
ISXOgreEQ2.OgreBot:Dump["${LavishScript.HomeDirectory}/ogrebot_values.json"]
```

### `List`

`ISXOgreEQ2.OgreBot:List[section,op,arg1,arg2]`

Edits one list section of the loaded profile (the Cast Stack or any other ordered list tab) in memory; Save keeps it, and a Cast Stack edit reaches the running cast stack at once. Ops are add (entry), insert or update (index,entry), del or toggle (index) and move (from,to), with 0-based indexes and each entry as base64-encoded JSON; it does not refresh the open window and does nothing with no profile loaded.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `section` | string |  | the profile section name, for example CastStack |
| `op` | string |  | add, insert, update, del, move or toggle |
| `arg1` | string |  | the base64 JSON entry (add) or a 0-based row index (every other op) |
| `arg2` | string |  | the base64 JSON entry (insert, update) or the target index (move) |

```text
ISXOgreEQ2.OgreBot:List[CastStack,toggle,0]
```

### `LoadProfile`

`ISXOgreEQ2.OgreBot:LoadProfile[name]`

Switches to another named profile of the loaded character and refreshes the cast stack and window; if OgreBot is not open it opens it with that profile. Unsaved changes to the current profile are dropped, with one warning line unless you named the profile already loaded, a name that is not found prints a line and keeps the current profile, and OgreBotAPI.Options:LoadProfile calls this.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | string |  | the profile name (case does not matter); a b64: prefix marks a base64 name |

```text
ISXOgreEQ2.OgreBot:LoadProfile[Raid]
```

### `Open`

`ISXOgreEQ2.OgreBot:Open[character,profile]`

Loads the character's profile from disk and opens the OgreBot main window and mini toolbar with it, then scans gear and inventory for the Items tab. Calling it while OgreBot is open loads the profile again and drops unsaved changes with one warning line; unlike the `ogre` command it leaves the pause state as it was, and a failed load (no character, profile not found) prints a line and changes nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `character` | string | `${Me.Name}` | the character whose profile to load |
| `profile` | string | `the character's default profile` | the profile name to load |

```text
ISXOgreEQ2.OgreBot:Open[${Me.Name},Group]
```

### `OpenMini`

`ISXOgreEQ2.OgreBot:OpenMini`

Opens the OgreBot mini toolbar on its own, without loading a profile, and prints a line. If the mini toolbar is already open it does nothing.

```text
ISXOgreEQ2.OgreBot:OpenMini
```

### `RefreshTargets`

`ISXOgreEQ2.OgreBot:RefreshTargets`

Re-reads which aliases and targets resolve right now and sends them to the OgreBot window's Target dropdown. It does nothing when the main window is closed.

```text
ISXOgreEQ2.OgreBot:RefreshTargets
```

### `Reload`

`ISXOgreEQ2.OgreBot:Reload`

Reads the loaded profile again from disk, dropping unsaved changes with one warning line, and refreshes the cast stack and the open window. It does nothing when no profile is loaded; OgreBotAPI.Bot:Reload is a different call that restarts the whole bot.

```text
ISXOgreEQ2.OgreBot:Reload
```

### `ReloadKeyBinds`

`ISXOgreEQ2.OgreBot:ReloadKeyBinds`

Reads the shared key binds file again (forward, backward and the other movement keys) and prints the new forward and backward keys. Another EQ2 session on this PC sends it after a key is changed.

```text
ISXOgreEQ2.OgreBot:ReloadKeyBinds
```

### `ReloadUi`

`ISXOgreEQ2.OgreBot:ReloadUi`

Reloads the in-game window pages from disk, then reopens the OgreBot main window and mini toolbar if they were open, with the same profile and settings. Nothing in the bot is reloaded or reset; this is what `ogre ui reload` runs.

```text
ISXOgreEQ2.OgreBot:ReloadUi
```

### `Research`

`ISXOgreEQ2.OgreBot:Research[mode]`

Runs the Ability Research check: it opens the Knowledge window and, with go or run, claims finished research and starts the next ability from the saved priority list, then closes the window. With no mode or any other word it only reads the window and says what it would do (trace also logs each window read), and a call while a check is running is ignored.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `mode` | string | `preview` | go or run for the real run, trace for a logged preview; anything else is a preview |

```text
ISXOgreEQ2.OgreBot:Research[go]
```

### `Save`

`ISXOgreEQ2.OgreBot:Save`

Writes the loaded profile's changes to disk and prints each file it wrote. With nothing loaded or nothing changed it prints that and writes nothing.

```text
ISXOgreEQ2.OgreBot:Save
```

### `SaveProfileAs`

`ISXOgreEQ2.OgreBot:SaveProfileAs[name]`

Overwrites another profile with the current settings, unsaved changes included, and switches to it. It fails with a console line when that profile does not exist or is the loaded one.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | string |  | the profile to overwrite; a b64: prefix marks a base64 name |

```text
ISXOgreEQ2.OgreBot:SaveProfileAs[Solo]
```

### `ScanItems`

`ISXOgreEQ2.OgreBot:ScanItems`

Asks for a scan of equipped gear, inventory and adornments on the next pulse, to fill the Items tab's source list. The request is dropped when no profile is loaded or the in-game UI is not ready, and opening OgreBot already runs one.

```text
ISXOgreEQ2.OgreBot:ScanItems
```

### `SetDefault`

`ISXOgreEQ2.OgreBot:SetDefault[name]`

Makes a named profile the one this character loads by default, and writes that to the profile file at once. It fails with a console line when nothing is loaded or the profile does not exist.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | string |  | the profile name (case does not matter); a b64: prefix marks a base64 name |

```text
ISXOgreEQ2.OgreBot:SetDefault[Group]
```

### `UplinkConnect`

`ISXOgreEQ2.OgreBot:UplinkConnect`

Connects this PC's uplink to every PC on the Uplink Info list except this one, spaced out, and prints how many it did (or that there is nothing to do). A second connect or disconnect from the same session within 3 seconds is ignored and only written to the log.

```text
ISXOgreEQ2.OgreBot:UplinkConnect
```

### `UplinkDisconnect`

`ISXOgreEQ2.OgreBot:UplinkDisconnect`

Disconnects this PC's uplink from every PC on the Uplink Info list except this one, and prints how many it did (or that there is nothing to do). A second connect or disconnect from the same session within 3 seconds is ignored and only written to the log.

```text
ISXOgreEQ2.OgreBot:UplinkDisconnect
```
