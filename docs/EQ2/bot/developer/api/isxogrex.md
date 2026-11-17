<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../index.md).
</div>

# ISXOgreX

The core extension: `${ISXOgreX}` and the objects under it.

## ISXOgreX

### Members

#### `Auth`

`${ISXOgreX.Auth}`

The login status object. Read its members: Authenticated, AccessLevel, Username and Status.

All of it: [ISXOgreX.Auth](#isxogrexauth)

**Returns:** ogrexauth: the login status object; as text it reads ISXOgreX.Auth.

```text
echo ${ISXOgreX.Auth.Status}
```

#### `Console`

`${ISXOgreX.Console}`

The Ogre console object. It has no members of its own; call its methods, such as ISXOgreX.Console:Toggle.

All of it: [ISXOgreX.Console](#isxogrexconsole)

**Returns:** ogrexconsole: the console object (methods only); as text it reads ISXOgreX.Console.

```text
echo ${ISXOgreX.Console}
```

#### `Login`

`${ISXOgreX.Login}`

The login box object. ISXOgreX.Login:Show opens the login box, and ISXOgreX.Login:Submit[username,password] saves a login and logs in again with it.

All of it: [ISXOgreX.Login](#isxogrexlogin)

**Returns:** ogrexlogin: the login box object (methods only); as text it reads ISXOgreX.Login.

```text
echo ${ISXOgreX.Login}
```

#### `Options`

`${ISXOgreX.Options}`

The Ogre options window object. Its methods are Open, Save, Close and Ready (fill the open window's fields again).

All of it: [ISXOgreX.Options](#isxogrexoptions)

**Returns:** ogrexoptions: the options window object (methods only); as text it reads ISXOgreX.Options.

```text
echo ${ISXOgreX.Options}
```

#### `Patch`

`${ISXOgreX.Patch}`

The patcher object: its members report the patcher's state and its methods run the patcher's commands. See the ISXOgreX.Patch rows.

All of it: [ISXOgreX.Patch](#isxogrexpatch)

**Returns:** ogrexpatch: the patcher object; as text it reads ISXOgreX.Patch.

```text
echo ${ISXOgreX.Patch}
```

#### `Release`

`${ISXOgreX.Release}`

The name of the release this PC was last patched to, the same name the What's new page uses. It is empty when this PC has never been patched or the last release had no name.

**Returns:** string: the release name (like 2026.10.16.005); empty when there is none.

```text
echo ${ISXOgreX.Release}
```

#### `UI`

`${ISXOgreX.UI}`

The in-game UI object: windows, their values and the UI store. See the ISXOgreX.UI rows for its members and methods.

All of it: [ISXOgreX.UI](#isxogrexui)

**Returns:** ogrexui: the in-game UI object; as text it reads ISXOgreX.UI.

```text
echo ${ISXOgreX.UI}
```

#### `Version`

`${ISXOgreX.Version}`

The build date of the loaded core extension. It is not the release name - use Release for that.

**Returns:** string: the core's build date as yyyymmdd.

```text
echo ${ISXOgreX.Version}
```

### Methods

#### `ReloadExtension`

`ISXOgreX:ReloadExtension[reason]`

Reloads this session's core (the game adapter reloads under it) when the core or adapter file on disk is newer than the one this session loaded; otherwise it prints that this session already runs the files on disk. It does nothing while a patch run is in progress on this session, and nothing before the patcher has started.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `reason` | string | `another session on this PC patched` | Text shown in the reload message, saying why the reload was asked for. |

```text
ISXOgreX:ReloadExtension["files updated"]
```

#### `ShowVersion`

`ISXOgreX:ShowVersion`

Prints the release this PC was patched to and the core's build date to the InnerSpace console, with a link to what changed. When this PC was never patched it says so, and when the release has no name it shows the release id instead.

```text
ISXOgreX:ShowVersion
```

## ISXOgreX.Auth

### Members

#### `AccessLevel`

`${ISXOgreX.Auth.AccessLevel}`

The access level name the Ogre server sent for this account at login. Before a login reply arrives it reads a default value.

**Returns:** string: the access level name from the server; a default value before a login reply arrives or when the server sent none.

```text
echo ${ISXOgreX.Auth.AccessLevel}
```

#### `Authenticated`

`${ISXOgreX.Auth.Authenticated}`

Whether this session's login to the Ogre server succeeded. It is FALSE while the login is still waiting for the server.

**Returns:** bool: TRUE when the login succeeded; FALSE when it has not started, is waiting, failed, or no login is saved.

```text
echo ${ISXOgreX.Auth.Authenticated}
```

#### `Status`

`${ISXOgreX.Auth.Status}`

Where this session's login stands, as one word.

**Returns:** string: idle (not started), pending (waiting for the server), authenticated, failed, or nocreds (no saved login).

```text
echo ${ISXOgreX.Auth.Status}
```

#### `Username`

`${ISXOgreX.Auth.Username}`

The account name of the saved login this session logs in with. It is filled from the saved login before the server answers, so use Authenticated to know whether the login succeeded.

**Returns:** string: the saved login's account name; empty when no login is saved.

```text
echo ${ISXOgreX.Auth.Username}
```

## ISXOgreX.Login

### Methods

#### `Show`

`ISXOgreX.Login:Show`

Opens the small Windows login box where you type your Ogre account username and password; if it is already open it is brought to the front instead. Its Login button saves what you typed and logs in, and Cancel just closes it (the Account tab of Ogre Options is the usual place for this - the box is the fallback when that window cannot load).

```text
ISXOgreX.Login:Show
```

#### `Submit`

`ISXOgreX.Login:Submit[username,password]`

Saves the given Ogre account username and password on this PC, closes the login box if it is open and logs in again on the next frame - even when you are already logged in. With either argument missing or blank nothing is saved and one console warning says so.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `username` | string |  | Your Ogre account name. |
| `password` | string |  | Your Ogre account password. |

```text
ISXOgreX.Login:Submit["MyOgreAccount","MyOgrePassword"]
```

## ISXOgreX.Options

### Methods

#### `Close`

`ISXOgreX.Options:Close`

Closes the Ogre Options window without saving anything.

```text
ISXOgreX.Options:Close
```

#### `Open`

`ISXOgreX.Options:Open`

Opens the Ogre Options window and fills its fields from the saved settings. If the window is already open it does nothing, so what you typed in it stays (the same as `ogre config`).

```text
ISXOgreX.Options:Open
```

#### `Save`

`ISXOgreX.Options:Save`

Saves the values the Ogre Options window's Save button hands over (this is the call that button makes): UI scale, the console setting, session watch, navmesh downloads and your Ogre login, which tries to log in again if you are not logged in. The window's status line then shows 'Saved.', 'Saved - logging in...' or 'Save FAILED', or 'Save failed (no data)' or 'Save failed (bad JSON)' when nothing usable was handed over.

```text
ISXOgreX.Options:Save
```

## ISXOgreX.Console

### Methods

#### `Clear`

`ISXOgreX.Console:Clear`

Clears the Ogre console's output and the lines it keeps on this session. New lines show as normal afterwards.

```text
ISXOgreX.Console:Clear
```

#### `Close`

`ISXOgreX.Console:Close`

Closes the Ogre console window on this session. It stays closed until opened again, even if the UI reloads.

```text
ISXOgreX.Console:Close
```

#### `Open`

`ISXOgreX.Console:Open`

Opens the Ogre console window on this session. Opening a console that is already open does nothing.

```text
ISXOgreX.Console:Open
```

#### `ReloadSchema`

`ISXOgreX.Console:ReloadSchema[game]`

Reads the console command lists again from disk on this session: the common list, the game's list and any command packs. A missing file just leaves its commands out, and pack problems are shown in the console's Commands tab.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `game` | string | `everquest2` | The game id whose command list to load, such as everquest2 or pantheon. |

```text
ISXOgreX.Console:ReloadSchema[everquest2]
```

#### `Send`

`ISXOgreX.Console:Send[message,-tab,tab,-rg,group,-cfw,who,-kind,kind]`

Sends message through the uplink to every session in the relay group: a message starting !c or !ci is a command that each session parses, anything else is a chat line. With no arguments it sends the line typed in the console's input box instead.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `message` | string | `the input box line` | The literal line to send; a leading !c or !ci makes it a command. Leave out every argument to send the input box line. |
| `-tab` | switch | `(none)` | Also show the line in the console tab named by the next argument; may be given more than once. |
| `tab` | string | `(none)` | The console tab name that follows -tab. |
| `-rg` | switch | `(none)` | Send to the relay group named by the next argument instead of the bot's own relay group. |
| `group` | string | `the bot's relay group` | The relay group name that follows -rg. |
| `-cfw` | switch | `(none)` | Give a command a for-who, used by its commands whose own for-who is left as auto. |
| `who` | for-who | `all` | [for-who](ogrebotapi/ForWho.md): this runs only when this character is one it names, for the commands in the line that leave theirs as auto. |
| `-kind` | switch | `(none)` | Show a chat line as a status line of the kind named by the next argument; ignored for a command. |
| `kind` | string | `(none)` | error, warn or system; the line then shows only in its -tab tabs and All, in that kind's colour. |

```text
ISXOgreX.Console:Send["Pulling now",-tab,Raid]
```

#### `Sessions`

`ISXOgreX.Console:Sessions[mode]`

With on or off, turns the uplink's session watch (it says when a session freezes, recovers or closes) on or off until the uplink restarts. With no argument it prints the sessions the uplink has heard from to this session's console; any other word prints the usage.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `mode` | string | `(none - print the table)` | on or off to switch the watch; leave it out to print the session table. |

```text
ISXOgreX.Console:Sessions[on]
```

#### `SetOption`

`ISXOgreX.Console:SetOption[key,value]`

Saves one console setting to the console's settings file (the same as the console's settings panel). It does nothing with fewer than two arguments, and an unknown key is ignored with nothing on screen.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `key` | string |  | hide_on_load, send_to_irc, show_timestamps, verb_trace, or a colour key starting color_. |
| `value` | string |  | 1 or true (lower case) for on, anything else (TRUE included) for off; for a color_ key, a hex colour of up to six digits. |

```text
ISXOgreX.Console:SetOption[show_timestamps,1]
```

#### `Toggle`

`ISXOgreX.Console:Toggle`

Opens the Ogre console window when it is closed, and closes it when it is open.

```text
ISXOgreX.Console:Toggle
```

## ISXOgreX.UI

### Members

#### `Get`

`${ISXOgreX.UI.Get[key]}`

Reads the value a UI page stored under `key` with ogreCall('set',key,value); there is one store, shared by every page, and the UI host is loaded first if needed. Returns NULL when the key was never stored, its value is empty, or the UI host is not loaded.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `key` | string |  | the store key the page used (case as the page wrote it) |

**Returns:** string: the stored value; NULL when the key is absent, its value is empty, or the UI host is not loaded

```text
echo ${ISXOgreX.UI.Get[radar_cfg]}
```

#### `Value`

`${ISXOgreX.UI.Value[name,id]}`

Reads element `id` of the open window `name` as the page last published it: a checkbox or radio reads TRUE or FALSE, an input or textarea its value (an empty box reads an empty string), any other element its text. NULL when the window is not open or the element never published - only windows opened with ISXOgreX.UI:Open publish, and a read right after your own ISXOgreX.UI:Set waits up to 50 ms for the page to apply it.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | string |  | the window name given to ISXOgreX.UI:Open (case-sensitive) |
| `id` | string |  | the element's HTML id inside that window |

**Returns:** string: the element's published value; NULL when the window is not open or the element never published a value

```text
echo ${ISXOgreX.UI.Value[hello,hello-name]}
```

#### `Window`

`${ISXOgreX.UI.Window[name]}`

Gives the open window `name` - your own, OgreBot's or a help window - as an ogrexuiwindow object (Name, Visible, X, Y, Width, Height) that prints as the window's name. NULL when no window by that name is open, so (exists) answers "is it open"; a window counts as open from the moment OgreUI_Opened fires for it.

All of it: [ISXOgreX.UI.Window](#isxogrexuiwindow)

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | string |  | the window name (case-sensitive) |

**Returns:** ogrexuiwindow: the open window; NULL when no window with that name is open

```text
echo ${ISXOgreX.UI.Window[hello](exists)}
```

### Methods

#### `Close`

`ISXOgreX.UI:Close[name]`

Closes the window `name` - your own or any other open UI window - and OgreUI_Closed fires with reason "closed". Nothing happens when no window by that name is open; a missing name is refused with one console warning.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | string |  | the window's name (case-sensitive) |

```text
ISXOgreX.UI:Close[hello]
```

#### `Drain`

`ISXOgreX.UI:Drain`

Runs, right now and in order, the commands UI pages have queued for the script side, stopping after about 1,000 in one call. The extension already does this every frame, so a script rarely needs it.

```text
ISXOgreX.UI:Drain
```

#### `Eval`

`ISXOgreX.UI:Eval[js]`

Runs the JavaScript js in the UI page, loading the UI host first if needed. Nothing comes back to the script, and without js it is refused with one console warning.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `js` | string |  | the JavaScript to run in the UI page |

```text
ISXOgreX.UI:Eval["radarSaveNow()"]
```

#### `EvalFile`

`ISXOgreX.UI:EvalFile[path]`

Reads the JavaScript file `path` from disk and runs it in the UI page, loading the UI host first if needed. A file that cannot be read writes a warning to the log file only, not the console, and a missing path is refused with one console warning.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `path` | string |  | full path of the .js file to run |

```text
ISXOgreX.UI:EvalFile["${LavishScript.HomeDirectory}/Scripts/Ogre/Common/OgreUI/common/WindowReset/windowreset.js"]
```

#### `Focus`

`ISXOgreX.UI:Focus[name,id]`

Gives the text field `id` in the open window `name` the keyboard, so keys go to that field and not the game until Escape or a click elsewhere; every call is logged. A hidden window, a missing element or anything that is not a text field is refused (logged only), and leaving out either argument prints a warning to the console.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | string |  | the open window's name (case-sensitive) |
| `id` | string |  | the HTML id of a text input, textarea or editable element in that window |

```text
ISXOgreX.UI:Focus[hello,hello-name]
```

#### `Help`

`ISXOgreX.UI:Help`

Opens, in the default web browser, the online documentation page of the window whose Full documentation button was pressed; the window name comes from what the help window stored under help_name. It takes no arguments, and a window with no documentation page only writes a warning to the log file.

```text
ISXOgreX.UI:Help
```

#### `Host`

`ISXOgreX.UI:Host`

Loads the UI host if it is not loaded yet; it does not open or show anything. Safe to call any number of times.

```text
ISXOgreX.UI:Host
```

#### `KeyboardDump`

`ISXOgreX.UI:KeyboardDump`

Prints a keyboard report to the console: Shift (as the game and the hardware see it), Caps Lock, Ctrl, Alt, the keys held down, whether the game window is in front, and the UI host's keyboard state. It is meant for pasting into a report about a key that seems stuck.

```text
ISXOgreX.UI:KeyboardDump
```

#### `Load`

`ISXOgreX.UI:Load[path]`

Loads the UI host, then replaces the whole UI page with the HTML file path, which takes away the desktop and every window on it: each window closes with OgreUI_Closed reason "reload", as UI:Reload does, and nothing waiting for the desktop runs until a page says it is ready. Without path it is refused with one console warning (ISXOgreX.UI:Host loads the host alone).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `path` | string |  | full path of the HTML file to show as the UI page |

```text
ISXOgreX.UI:Load["${LavishScript.HomeDirectory}/Scripts/Ogre/Common/OgreUI/common/Desktop/desktop.html"]
```

#### `Move`

`ISXOgreX.UI:Move[name,x,y]`

Moves the open window `name` (yours or any other) so its top-left corner sits at x,y in desktop pixels - the same numbers the Window object's X and Y read back. The move is not saved, so the window opens at its saved spot next time; anything but two whole numbers prints a warning to the console, and a window that is not open is left alone.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | string |  | the open window's name (case-sensitive) |
| `x` | int |  | left edge in desktop pixels (a whole number) |
| `y` | int |  | top edge in desktop pixels (a whole number) |

```text
ISXOgreX.UI:Move[hello,200,150]
```

#### `Open`

`ISXOgreX.UI:Open[name,path,helpPath]`

Opens your own window `name` from one HTML file `path`, with an optional markdown file `helpPath` as the text of the title bar's help (?) button; both files are read when you call it, and the window appears once the UI desktop is up, when OgreUI_Opened fires. If a window by that name is already open only its help text is refreshed, and a file that cannot be read prints a warning to the console and opens nothing; a missing name or path is refused with one console warning.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | string |  | the window's name, used by every other window call (case-sensitive) |
| `path` | string |  | full path of the HTML file: style, markup and &lt;script> blocks, plus an optional &lt;script type="ogre/window"> block holding the window's options as JSON (title, w, h ...) |
| `helpPath` | string | `"" (no help text)` | full path of a markdown file shown by the title bar's ? button |

```text
ISXOgreX.UI:Open[hello,"${LavishScript.HomeDirectory}/Scripts/Ogre/Common/OgreUI/examples/hello/hello.html","${LavishScript.HomeDirectory}/Scripts/Ogre/Common/OgreUI/examples/hello/hello.md"]
```

#### `Reload`

`ISXOgreX.UI:Reload`

Reloads the UI page: every open window goes away at once and OgreUI_Closed fires for each with reason "reload", which is the cue for a script to re-open its own window. The UI host is loaded first if needed; if it cannot load, nothing happens.

```text
ISXOgreX.UI:Reload
```

#### `SavePref`

`ISXOgreX.UI:SavePref`

Saves a UI page's own preferences: the JSON the page stored under uipref_blob is written into the saved UI state (UIState.json in the Common save folder) under the name it stored in uipref_name, replacing what that name held. Pages call it themselves; it takes no arguments, and missing or invalid values only write a warning to the log file.

```text
ISXOgreX.UI:SavePref
```

#### `SaveWindow`

`ISXOgreX.UI:SaveWindow`

Saves one window's position, size, scale and lock settings, read from the blob the page stored under wm_save_blob, into the saved UI state (UIState.json in the Common save folder), replacing what that window had. The window manager calls it from a window's Save Position; it takes no arguments, and a missing or invalid blob only writes a warning to the log file.

```text
ISXOgreX.UI:SaveWindow
```

#### `Set`

`ISXOgreX.UI:Set[name,id,value]`

Changes element `id` in the open window `name` as if the user did it: a checkbox or radio is checked for TRUE, 1, on or yes and unchecked for anything else, an input, textarea or dropdown takes the value, any other element shows it as its text, and a form element's change event fires. A missing window, id or value is refused with one console warning (a blank value is a value); nothing happens when the window is not open or no element has that id.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | string |  | the open window's name (case-sensitive) |
| `id` | string |  | the element's HTML id inside that window |
| `value` | string |  | the new value: TRUE/FALSE for a checkbox or radio, otherwise the text or value to put in |

```text
ISXOgreX.UI:Set[hello,hello-status,"Said hello"]
```

#### `Size`

`ISXOgreX.UI:Size[name,width,height]`

Sizes the open window `name` (yours or any other) to width by height pixels on screen with its scale applied - the same numbers the Window object's Width and Height read back. The size is not saved, so the window opens at its saved size next time; anything but two whole numbers above 0 prints a warning to the console, and a window that is not open is left alone.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | string |  | the open window's name (case-sensitive) |
| `width` | int |  | width in on-screen pixels (a whole number above 0) |
| `height` | int |  | height in on-screen pixels (a whole number above 0) |

```text
ISXOgreX.UI:Size[hello,320,200]
```

#### `WindowResetPanel`

`ISXOgreX.UI:WindowResetPanel`

Opens the Reset UI Windows window, centered on the screen, which lists the open windows and lets the player put each one back at its default spot. It waits for the desktop if that is not up yet, and does nothing if the Reset UI Windows window is already open.

```text
ISXOgreX.UI:WindowResetPanel
```

## ISXOgreX.Patch

### Members

#### `Enabled`

`${ISXOgreX.Patch.Enabled}`

Whether the Ogre patcher may update this PC, as the patcher last read its setting. The setting is read again whenever an update starts or Status runs, so a change shows here after that.

**Returns:** bool: TRUE when patching is on; FALSE when it is off for this PC, its setting cannot be read, or before the patcher has started.

```text
echo ${ISXOgreX.Patch.Enabled}
```

#### `InProgress`

`${ISXOgreX.Patch.InProgress}`

Whether an update run is going on in this session, including the short wait before the update check at load and a reload queued after an extension was updated. Background navmesh downloads do not count.

**Returns:** bool: TRUE while an update run is active in this session; FALSE when none is.

```text
echo ${ISXOgreX.Patch.InProgress}
```

#### `LastResult`

`${ISXOgreX.Patch.LastResult}`

The one-line result of the last update run on this PC, the same text the run printed after 'patch:' (for example a line starting 'up to date' or 'done - release', which counts the files updated and failed). It is kept in OgreSave/patcher-state.json, so it survives a restart.

**Returns:** string: the last run's result line; "" when no run has finished on this PC or patching was off when the session started.

```text
echo ${ISXOgreX.Patch.LastResult}
```

#### `ReleaseId`

`${ISXOgreX.Patch.ReleaseId}`

The id of the release the last update run on this PC checked against, kept in OgreSave/patcher-state.json. For the release name players see, use ${ISXOgreX.Release}.

**Returns:** string: the last run's release id; "" when this PC has never been patched or patching was off when the session started.

```text
echo ${ISXOgreX.Patch.ReleaseId}
```

#### `Tier`

`${ISXOgreX.Patch.Tier}`

The release channel number the update server sent with the release the last update run on this PC checked against, kept with ReleaseId in OgreSave/patcher-state.json.

**Returns:** int: that number; -1 when no update run has recorded one.

```text
echo ${ISXOgreX.Patch.Tier}
```

### Methods

#### `Ignore`

`ISXOgreX.Patch:Ignore[op,path]`

Manages the list of files the patcher never writes, kept in OgreSave/patcher-ignore.json, so your own copy of a file is left alone: add or remove a path, or list them. Paths are relative to the InnerSpace folder with forward slashes (backslashes are turned into them), and every change prints a confirmation line.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `op` | string | `list` | add, remove or list; leave it out to list. |
| `path` | string | `""` | The file for add or remove, relative to the InnerSpace folder, such as Scripts/Ogre/EQ2/x.json; not used by list. |

```text
ISXOgreX.Patch:Ignore[add,"Scripts/Ogre/EQ2/Commands/everquest2.json"]
```

#### `Mesh`

`ISXOgreX.Patch:Mesh[mode]`

Sets how navmeshes download and applies it at once: all (every zone in the background), ondemand (a zone's mesh when you need it) or off. With no argument it prints the navmesh download summary, and an unknown word prints the usage line.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `mode` | string | `""` | all, ondemand or off; leave it out to print the summary instead. |

```text
ISXOgreX.Patch:Mesh[ondemand]
```

#### `RevertExt`

`ISXOgreX.Patch:RevertExt`

Puts back the previous ISXOgreX DLL kept after a self-update (the .prev file) and reloads the extension, keeping the replaced one beside it as .reverted. It is refused while a run is in progress, says there is nothing to revert when no .prev exists, and the next update run installs the current release again.

```text
ISXOgreX.Patch:RevertExt
```

#### `Status`

`ISXOgreX.Patch:Status`

Prints the patcher's state to the console: whether patching is on, your login state, your file switches, the last release and run, whether this session runs older DLLs than the ones on disk, any run in progress and the navmesh download summary. It changes nothing.

```text
ISXOgreX.Patch:Status
```

#### `TestCorrupt`

`ISXOgreX.Patch:TestCorrupt`

A diagnostic switch: each call arms or disarms a one-time fault that flips one byte of the next downloaded file before it is checked, so you can see the check refuse it and keep the old file. It prints ARMED or disarmed and fires on the next update or navmesh download.

```text
ISXOgreX.Patch:TestCorrupt
```

#### `Update`

`ISXOgreX.Patch:Update`

Checks for an Ogre update now and installs it: fetches the current release, downloads every changed file, checks each one and swaps them in, reloading the extension if one of its DLLs changed, and afterwards every other session on this PC that runs older files reloads too. It runs in the background, prints 'patch: &lt;result>' when done, and refuses with a console line when a run is already going, patching is off or you are not logged in to Ogre.

```text
ISXOgreX.Patch:Update
```

## ISXOgreX.UI.Window

### Members

#### `Height`

`${ISXOgreX.UI.Window[name].Height}`

The window's on-screen height in pixels with its scale applied, as the page last published it - the number ISXOgreX.UI:Size takes. A hidden window keeps its last on-screen size (0 if it was never shown), and the member reads NULL once the window has closed.

**Returns:** int: on-screen height in pixels; NULL when the window has closed

```text
echo ${ISXOgreX.UI.Window[hello].Height}
```

#### `Name`

`${ISXOgreX.UI.Window[name].Name}`

The window's name, as given to ISXOgreX.UI.Window. It still answers after the window has closed, while every other member then reads NULL.

**Returns:** string: the window name

```text
echo ${ISXOgreX.UI.Window[hello].Name}
```

#### `Visible`

`${ISXOgreX.UI.Window[name].Visible}`

TRUE while the window is shown, FALSE while it is open but hidden. NULL once the window has closed.

**Returns:** bool: TRUE when the window is shown; FALSE when it is open but hidden; NULL when it has closed

```text
echo ${ISXOgreX.UI.Window[hello].Visible}
```

#### `Width`

`${ISXOgreX.UI.Window[name].Width}`

The window's on-screen width in pixels with its scale applied, as the page last published it - the number ISXOgreX.UI:Size takes. A hidden window keeps its last on-screen size (0 if it was never shown), and the member reads NULL once the window has closed.

**Returns:** int: on-screen width in pixels; NULL when the window has closed

```text
echo ${ISXOgreX.UI.Window[hello].Width}
```

#### `X`

`${ISXOgreX.UI.Window[name].X}`

The window's left edge in desktop pixels, as the page last published it - the number ISXOgreX.UI:Move takes. A hidden window keeps its last on-screen position (0 if it was never shown), and the member reads NULL once the window has closed.

**Returns:** int: left edge in desktop pixels; NULL when the window has closed

```text
echo ${ISXOgreX.UI.Window[hello].X}
```

#### `Y`

`${ISXOgreX.UI.Window[name].Y}`

The window's top edge in desktop pixels, as the page last published it - the number ISXOgreX.UI:Move takes. A hidden window keeps its last on-screen position (0 if it was never shown), and the member reads NULL once the window has closed.

**Returns:** int: top edge in desktop pixels; NULL when the window has closed

```text
echo ${ISXOgreX.UI.Window[hello].Y}
```

## ogretimer

### Members

#### `DeciLeft`

`${T.DeciLeft}`

Seconds left before the timer runs out, as text with one decimal, as Object_Timer's DeciLeft: 1500 ms left reads 1.5. It reads 0.0 once the timer has run out or was stopped.

**Returns:** string: seconds left with one decimal; "0.0" when the timer ran out, was stopped or was never set

```text
variable ogretimer T
echo ${T.DeciLeft}
```

#### `MinutesLeft`

`${T.MinutesLeft}`

Whole minutes left before the timer runs out, rounded down, as Object_Timer's MinutesLeft: 119 seconds left reads 1. It reads 0 in the last minute as well as once the timer has run out or was stopped.

**Returns:** int64: whole minutes left (rounded down); 0 when under a minute is left, or the timer ran out, was stopped or was never set

```text
variable ogretimer T
echo ${T.MinutesLeft}
```

#### `Running`

`${T.Running}`

Whether the timer still has time left. A timer set to 0, run out, stopped or never set is not running.

**Returns:** bool: TRUE while TimeLeft is above 0; FALSE when it has run out, was stopped or was never set

```text
variable ogretimer T
echo ${T.Running}
```

#### `SecondsLeft`

`${T.SecondsLeft}`

Whole seconds left before the timer runs out, rounded down, so 1999 ms left reads 1. It reads 0 in the last second as well as once the timer has run out or was stopped.

**Returns:** int64: whole seconds left (rounded down); 0 when under one second is left, or the timer ran out, was stopped or was never set

```text
variable ogretimer T
echo ${T.SecondsLeft}
```

#### `TimeLeft`

`${T.TimeLeft}`

Milliseconds left before the timer runs out - 0 once it has run out, and 0 for a timer that was stopped or never set. Reading the variable itself (${T}) gives the same number, so `if ${T}` means still running.

**Returns:** int64: milliseconds left; 0 when the timer has run out, was stopped or was never set

```text
variable ogretimer T
echo ${T.TimeLeft}
```

### Methods

#### `Dec`

`T:Dec[ms]`

Takes ms milliseconds off the time left - taking off as much as is left (or more) stops the timer, and a timer that is not running stays stopped. A missing or non-number argument prints a warning and leaves the timer unchanged, and zero or a negative number counts as 0.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `ms` | number |  | milliseconds to take off (fractions are rounded) |

```text
variable ogretimer T
T:Dec[1000]
```

#### `DecMinutes`

`T:DecMinutes[minutes]`

Takes that many minutes off the time left - taking off as much as is left (or more) stops the timer, and a timer that is not running stays stopped. A missing or non-number argument prints a warning and leaves the timer unchanged, and zero or a negative number counts as 0.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `minutes` | number |  | minutes to take off (fractions allowed) |

```text
variable ogretimer T
T:DecMinutes[1]
```

#### `DecSeconds`

`T:DecSeconds[seconds]`

Takes that many seconds off the time left - taking off as much as is left (or more) stops the timer, and a timer that is not running stays stopped. A missing or non-number argument prints a warning and leaves the timer unchanged, and zero or a negative number counts as 0.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `seconds` | number |  | seconds to take off (fractions allowed) |

```text
variable ogretimer T
T:DecSeconds[5]
```

#### `Inc`

`T:Inc[ms]`

Adds ms milliseconds to the time left, and a timer that has run out, was stopped or was never set counts from now instead. A missing or non-number argument prints a warning and leaves the timer unchanged, and zero or a negative number counts as 0.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `ms` | number |  | milliseconds to add (fractions are rounded) |

```text
variable ogretimer T
T:Inc[2000]
```

#### `IncMinutes`

`T:IncMinutes[minutes]`

Adds that many minutes to the time left, and a timer that has run out, was stopped or was never set counts from now instead. A missing or non-number argument prints a warning and leaves the timer unchanged, and zero or a negative number counts as 0.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `minutes` | number |  | minutes to add (fractions allowed) |

```text
variable ogretimer T
T:IncMinutes[1]
```

#### `IncSeconds`

`T:IncSeconds[seconds]`

Adds that many seconds to the time left, and a timer that has run out, was stopped or was never set counts from now instead. A missing or non-number argument prints a warning and leaves the timer unchanged, and zero or a negative number counts as 0.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `seconds` | number |  | seconds to add (fractions allowed) |

```text
variable ogretimer T
T:IncSeconds[5]
```

#### `Set`

`T:Set[ms]`

Starts the timer so it runs out ms milliseconds from now, replacing any time it had, and Set[0] makes it read as already run out. A missing or non-number argument prints a warning and leaves the timer unchanged, and zero or a negative number counts as 0.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `ms` | number |  | milliseconds from now until the timer runs out (fractions are rounded) |

```text
variable ogretimer T
T:Set[5000]
```

#### `SetHours`

`T:SetHours[hours]`

Starts the timer so it runs out that many hours from now, replacing any time it had (fractions work). A missing or non-number argument prints a warning and leaves the timer unchanged, and zero or a negative number counts as 0.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `hours` | number |  | hours from now until the timer runs out (fractions allowed) |

```text
variable ogretimer T
T:SetHours[1]
```

#### `SetMinimum`

`T:SetMinimum[ms]`

Makes the timer run for at least ms milliseconds from now, and a timer that already has more time left keeps it. A missing or non-number argument prints a warning and leaves the timer unchanged, and zero or a negative number counts as 0.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `ms` | number |  | the least milliseconds from now the timer should have left |

```text
variable ogretimer T
T:SetMinimum[3000]
```

#### `SetMinimumMinutes`

`T:SetMinimumMinutes[minutes]`

Makes the timer run for at least that many minutes from now, and a timer that already has more time left keeps it. A missing or non-number argument prints a warning and leaves the timer unchanged, and zero or a negative number counts as 0.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `minutes` | number |  | the least minutes from now the timer should have left (fractions allowed) |

```text
variable ogretimer T
T:SetMinimumMinutes[2]
```

#### `SetMinimumSeconds`

`T:SetMinimumSeconds[seconds]`

Makes the timer run for at least that many seconds from now, and a timer that already has more time left keeps it. A missing or non-number argument prints a warning and leaves the timer unchanged, and zero or a negative number counts as 0.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `seconds` | number |  | the least seconds from now the timer should have left (fractions allowed) |

```text
variable ogretimer T
T:SetMinimumSeconds[10]
```

#### `SetMinutes`

`T:SetMinutes[minutes]`

Starts the timer so it runs out that many minutes from now, replacing any time it had (fractions work). A missing or non-number argument prints a warning and leaves the timer unchanged, and zero or a negative number counts as 0.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `minutes` | number |  | minutes from now until the timer runs out (fractions allowed) |

```text
variable ogretimer T
T:SetMinutes[5]
```

#### `SetSeconds`

`T:SetSeconds[seconds]`

Starts the timer so it runs out that many seconds from now, replacing any time it had - fractions work, so SetSeconds[1.5] is 1500 ms. A missing or non-number argument prints a warning and leaves the timer unchanged, and zero or a negative number counts as 0.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `seconds` | number |  | seconds from now until the timer runs out (fractions allowed) |

```text
variable ogretimer T
T:SetSeconds[20]
```

#### `Stop`

`T:Stop`

Stops the timer at once, so TimeLeft reads 0 and Running reads FALSE. It takes no arguments and ignores any it is given.

```text
variable ogretimer T
T:Stop
```
