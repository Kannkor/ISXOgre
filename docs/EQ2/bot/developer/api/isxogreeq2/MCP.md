<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# ISXOgreEQ2.MCP

## Members

### `ForWho`

`${ISXOgreEQ2.MCP.ForWho}`

The for-who text MCP buttons and bound keys use on this session, from the For Who picker or MCP:SetForWho. A button with its own for-who still uses its own.

**Returns:** string: the for-who text in force on this session; all when nothing has been picked (everyone).

```text
echo ${ISXOgreEQ2.MCP.ForWho}
```

### `IrcConnected`

`${ISXOgreEQ2.MCP.IrcConnected}`

Whether this session last heard that the IRC link is up. It starts FALSE on a new session and stays FALSE until the IRC hub reports in; while FALSE, MCP buttons that send over IRC go through OgreConsole instead.

**Returns:** bool: TRUE when the IRC hub last reported the link connected; FALSE when it reported it down or has not reported yet.

```text
echo ${ISXOgreEQ2.MCP.IrcConnected}
```

## Methods

### `AddBind`

`ISXOgreEQ2.MCP:AddBind[key,buttonId,name,event]`

Links a keyboard key or mouse button (an InnerSpace key name such as G600-G9) to an MCP button, so pressing it runs MCP:Fire on that button. The bind is saved to Scripts/OgreSave/EQ2/OgreMCPBinds.json, armed at once, and every EQ2 session on this PC picks it up; a bind with the same name is replaced, and a button id that has no command yet only prints a note.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `key` | string |  | The InnerSpace key name to bind, such as G600-G9 or F13. |
| `buttonId` | string |  | The MCP button to run, as MCP:Buttons lists it. |
| `name` | string | `MCP_<key>_<buttonId> with every other character turned into _` | A name for the bind, used by MCP:RemoveBind. |
| `event` | string | `press` | release fires when the key is let go; anything else fires on press. |

```text
ISXOgreEQ2.MCP:AddBind[G600-G9,static:0_0,G9Heal,press]
```

### `Buttons`

`ISXOgreEQ2.MCP:Buttons`

Prints every configured MCP button to the console with its id, label, page and command, so you can find the id to give MCP:Fire or MCP:AddBind. With no saved layout it prints a line saying there are no buttons yet.

```text
ISXOgreEQ2.MCP:Buttons
```

### `Close`

`ISXOgreEQ2.MCP:Close`

Closes the Master Control Panel together with its For Who, Build command and Assign keys windows. It also cancels a key test that is still waiting for a press.

```text
ISXOgreEQ2.MCP:Close
```

### `Fire`

`ISXOgreEQ2.MCP:Fire[buttonId]`

Runs an MCP button by its id, exactly as clicking it would: the button's command is read from the saved layout at that moment and sent with the button's own for-who, or this session's For Who when the button has none. A missing id, no saved layout, or a button with no command prints one console line and sends nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `buttonId` | string |  | The button's id as MCP:Buttons lists it: btn:&lt;id> (follows the button when it moves), static:&lt;row>_&lt;col> or page:&lt;page>:&lt;row>_&lt;col>. |

```text
ISXOgreEQ2.MCP:Fire[static:0_0]
```

### `FixHoistOrder`

`ISXOgreEQ2.MCP:FixHoistOrder`

Repairs buttons that an older MCP:Migrate wrote with some arguments in the wrong order, touching only the affected buttons and writing OgreMCP.json.bak first. It runs once per file (a second call prints that it is already done), prints how many buttons were fixed or need checking by hand, and has every EQ2 session on this PC reload when anything changed.

```text
ISXOgreEQ2.MCP:FixHoistOrder
```

### `ListBinds`

`ISXOgreEQ2.MCP:ListBinds`

Prints every saved key bind to the console: its name, key, press or release, the button it runs, and whether it is disabled.

```text
ISXOgreEQ2.MCP:ListBinds
```

### `Migrate`

`ISXOgreEQ2.MCP:Migrate[overwrite]`

Converts the old OgreBot MCP buttons (Scripts/EQ2OgreBot/MCP/MCPCustomSettings.xml) into the new panel's Scripts/OgreSave/EQ2/OgreMCP.json and prints a summary; button types with no command equivalent come across as label only. It refuses to replace an existing OgreMCP.json unless you pass overwrite, and on success every EQ2 session on this PC reloads the panel.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `overwrite` | string | `off - an existing file is kept` | The word overwrite (or 1, TRUE, yes, on) replaces an existing OgreMCP.json, discarding its current layout. |

```text
ISXOgreEQ2.MCP:Migrate
```

### `Open`

`ISXOgreEQ2.MCP:Open`

Opens the Master Control Panel (MCP), the window of buttons that send commands to your characters, with its saved layout; the same as `ogre mcp`, and alt+backtick toggles it. Calling it while the panel is already open does nothing; if the in-game UI host is not running or a panel file cannot be read, nothing opens and one console line says which, and a missing command catalog opens the builder empty with a line.

```text
ISXOgreEQ2.MCP:Open
```

### `Reload`

`ISXOgreEQ2.MCP:Reload`

Re-reads Scripts/OgreSave/EQ2/OgreMCP.json and updates an open panel to match, which is how a change saved on one session shows up on the others. It is skipped when the file is exactly what this session just saved, or when the file is not valid JSON.

```text
ISXOgreEQ2.MCP:Reload
```

### `ReloadBinds`

`ISXOgreEQ2.MCP:ReloadBinds`

Re-reads Scripts/OgreSave/EQ2/OgreMCPBinds.json, removes this session's live key binds and arms the saved ones again. Adding or removing a bind on any session runs this on every EQ2 session on the PC.

```text
ISXOgreEQ2.MCP:ReloadBinds
```

### `RemoveBind`

`ISXOgreEQ2.MCP:RemoveBind[name]`

Removes a saved key bind by name, disarms it and tells every EQ2 session on this PC to drop it. An unknown name prints a console line and changes nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | string |  | The bind's name as MCP:ListBinds shows it. |

```text
ISXOgreEQ2.MCP:RemoveBind[G9Heal]
```

### `Send`

`ISXOgreEQ2.MCP:Send[message,-tab,tab,-rg,group,-cfw,who]`

With arguments it sends message exactly as ISXOgreX.Console:Send does (a leading !c or !ci makes it a command, anything else is a chat line). With no arguments it sends the button just clicked on this session, once, through the same route a click uses, and otherwise the console input box line.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `message` | string | `the button just clicked, or the input box line` | The literal line to send; a leading !c or !ci makes it a command. Leave out every argument for the button just clicked, or the console input box line. |
| `-tab` | switch | `(none)` | Also show the line in the console tab named by the next argument; may be given more than once. |
| `tab` | string | `(none)` | The console tab name that follows -tab. |
| `-rg` | switch | `(none)` | Send to the relay group named by the next argument instead of the bot's own relay group. |
| `group` | string | `the bot's relay group` | The relay group name that follows -rg. |
| `-cfw` | switch | `(none)` | Give the command a for-who, used by its commands whose own for-who is left as auto. |
| `who` | for-who | `everyone` | [for-who](../ogrebotapi/ForWho.md): this runs only when this character is one it names - the value that follows -cfw. |

```text
ISXOgreEQ2.MCP:Send["!c -pause","-cfw","igw:${Me.Name}"]
```

### `SetForWho`

`ISXOgreEQ2.MCP:SetForWho[value]`

Sets the For Who that MCP buttons and bound keys use on this session only, held in memory (not saved, not shared, back to everyone after a restart). With a value it sets that as a custom For Who and shows it in the picker (spaces are removed; all or an empty value clears it back to everyone); with no value it takes the choice the For Who picker just made.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `value` | string | `(none) - the picker's choice` | The for-who text to use, such as igw:&lt;name> or several names joined with \|. Leave it out to take the For Who picker's current choice. |

```text
ISXOgreEQ2.MCP:SetForWho[igw:${Me.Name}]
```

### `Toggle`

`ISXOgreEQ2.MCP:Toggle`

Opens the Master Control Panel when it is closed and closes it when it is open. This is what alt+backtick runs.

```text
ISXOgreEQ2.MCP:Toggle
```
