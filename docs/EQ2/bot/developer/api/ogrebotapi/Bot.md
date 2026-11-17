<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# OgreBotAPI.Bot

## Members

### `Paused`

`${OgreBotAPI.Bot.Paused}`

TRUE while the bot is paused, whether by Pause, the mini toolbar's pause button or a camp in progress. The bot starts out paused, so this is also TRUE before OgreBot has been loaded.

**Returns:** bool: TRUE when the bot is paused or has not been loaded yet; FALSE when it is running.

```text
echo ${OgreBotAPI.Bot.Paused}
```

*Was (OldBot):* `OgreBotAPI.Paused`

### `ScriptBaseName`

`${OgreBotAPI.Bot.ScriptBaseName[path,removeExtension]}`

Returns the last part of a script path with its folders removed; back slashes count as forward slashes. A trailing .iss (any case) is removed unless removeExtension is FALSE.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `path` | string |  | The script path or file name. |
| `removeExtension` | bool | `TRUE` | TRUE strips a trailing .iss; FALSE keeps it. A word that is not a yes word reads as FALSE. |

**Returns:** string: the file name, without .iss unless removeExtension is FALSE; the whole text when it has no slash.

```text
echo ${OgreBotAPI.Bot.ScriptBaseName["${LavishScript.HomeDirectory}/Scripts/EQ2OgreBot/OgreBotDev.iss"]}
```

*Was (OldBot):* `OgreBotAPI.Get_ScriptBaseName`

## Methods

### `CampToDesktop`

`OgreBotAPI.Bot:CampToDesktop[fw, loginOnly=FALSE]`

Queues a camp out: it stops following, pauses the bot for the camp and camps to the login screen, then closes the session unless loginOnly is TRUE. It refuses with a console line while you are in combat mode, and if the camp fails the bot's run state is put back.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `loginOnly` | bool | `FALSE` | TRUE stops at the login screen and keeps the session open; FALSE camps out and then closes the session. |

```text
OgreBotAPI.Bot:CampToDesktop[${Me.Name},TRUE]
```

*Was (OldBot):* `OgreBotAPI:CampToDesktop`

### `End`

`OgreBotAPI.Bot:End[fw]`

Closes OgreBot on the next frame, the same as typing ogre end bot. Closing also clears the no-offensive, no-defensive and threat ignore settings.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Bot:End[all]
```

*Was (OldBot):* `OgreBotAPI:End_Bot`

### `EndScript`

`OgreBotAPI.Bot:EndScript[fw, script]`

Ends a running script on each selected character, matched by its file name with folders and .iss removed, and shows the name in OgreConsole. Does nothing when no script of that name is running, and needs the character in the world.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `script` | string |  | The script's name or path. Only the file name counts, with .iss removed. |

```text
OgreBotAPI.Bot:EndScript[all,"MyScripts/hello"]
```

### `ExitClient`

`OgreBotAPI.Bot:ExitClient[fw, seconds=30]`

Queues an exit of this game client: a message box warns that the client closes in the given number of seconds, and clicking OK on it cancels. If the time runs out with the box still open, the session is closed with the character still in the world (no camp).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `seconds` | int | `30` | Seconds to wait before the exit. Anything that is not a whole number of at least 1 uses the default. |

```text
OgreBotAPI.Bot:ExitClient[${Me.Name},60]
```

*Was (OldBot):* `OgreBotAPI:ExitClient`

### `Load`

`OgreBotAPI.Bot:Load[fw]`

Starts OgreBot on the next frame, the same as typing ogre: it opens resumed with its main window hidden. Unlike Reload it also runs when OgreBot is not running, and on a running bot it reopens it the way Reload does.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Bot:Load[igw:${Me.Name}]
```

### `OgreCommand`

`OgreBotAPI.Bot:OgreCommand[fw, cmd...]`

Runs an Ogre sub-command (ogre, the name, then each remaining argument quoted) on each selected character, and shows the line it ran in OgreConsole. Needs the character in the world; with no command name it says so in OgreConsole and runs nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `cmd...` | string |  | The sub-command name, then its arguments. Each argument is passed on as its own quoted argument. |

```text
OgreBotAPI.Bot:OgreCommand[igw:${Me.Name},quiver]
```

*Was (OldBot):* `OgreBotAPI:OgreCommand`

### `OnDeactivate`

`OgreBotAPI.Bot:OnDeactivate[fw]`

Releases the Alt key, so an Alt held down when the game window lost focus does not stay stuck. When Alt reads as pressed it first prints a line saying so to the console.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Bot:OnDeactivate[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:OnDeactivate`

### `Pause`

`OgreBotAPI.Bot:Pause[fw]`

Pauses the bot so it stops casting and its other automatic actions until Resume. Takes effect at once and also works while zoning.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Bot:Pause[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Pause`, `Obj_OgreIH:Pause`

### `RawCommand`

`OgreBotAPI.Bot:RawCommand[fw, cmd...]`

Runs the arguments as one console command line on each selected character, and shows the line in OgreConsole. Needs the character in the world; an argument holding a space is quoted again, and an empty line runs nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `cmd...` | string |  | The command and its arguments, joined by single spaces into one line. |

```text
OgreBotAPI.Bot:RawCommand[all,echo,hello]
```

*Was (OldBot):* `OgreBotAPI:RawCommand`

### `Reload`

`OgreBotAPI.Bot:Reload[fw]`

Reloads OgreBot on the next frame: it reopens resumed with its main window hidden, and the no-offensive, no-defensive and threat ignore settings are cleared. Does nothing on a session where OgreBot is not running - it never starts the bot (Load does that).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Bot:Reload[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Reload_Bot`

### `Resume`

`OgreBotAPI.Bot:Resume[fw]`

Resumes a paused bot so it acts again. Takes effect at once and also works while zoning.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Bot:Resume[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Resume`, `Obj_OgreIH:Resume`

### `RunScript`

`OgreBotAPI.Bot:RunScript[fw, script, args...]`

Runs a script on each selected character, passing each later argument as its own quoted parameter, and shows the line in OgreConsole. It refuses with an OgreConsole line when the script is not found or a script of the same name is already running, and needs the character in the world.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `script` | string |  | The script path, relative to the Scripts folder; the .iss ending is optional. A path containing a colon is used as it is. |
| `args...` | string |  | The script's parameters. Every argument after script is passed on, each as its own quoted parameter. |

```text
OgreBotAPI.Bot:RunScript[${Me.Name},"MyScripts/hello","126","TRUE"]
```

### `SetUpFor`

`OgreBotAPI.Bot:SetUpFor[fw, what="", restart=TRUE]`

Sets up for an encounter on the next pulse: the fight of the named mob given in what, or with what blank the nearest or engaged named in this zone. Needs the character in the world; a name no encounter owns prints a warning to the console.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `what` | string | `""` | The named mob whose encounter to set up. Blank picks the nearest or engaged named in this zone. |
| `restart` | bool | `TRUE` | TRUE re-runs a setup that is already running; FALSE only sets up an encounter that is not running yet. |

```text
OgreBotAPI.Bot:SetUpFor[igw:${Me.Name},"${Target.Name}",TRUE]
```

*Was (OldBot):* `OgreBotAPI:SetUpFor`
