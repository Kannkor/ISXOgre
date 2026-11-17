<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# ISXOgreEQ2.Game

## Members

### `Busy`

`${ISXOgreEQ2.Game.Busy}`

Whether a login or camp started by ISXOgreEQ2.Game:Login or :Camp is still running. It goes FALSE when the flow finishes, times out or is aborted.

**Returns:** bool: TRUE while a login or camp is in progress; FALSE when idle.

```text
echo ${ISXOgreEQ2.Game.Busy}
```

### `State`

`${ISXOgreEQ2.Game.State}`

The step the login or camp flow is on, as a short phrase such as login: wait for login screen or camp: wait for camp to complete. It reads idle when nothing is running.

**Returns:** string: the current login/camp step; idle when nothing is running.

```text
echo ${ISXOgreEQ2.Game.State}
```

## Methods

### `Abort`

`ISXOgreEQ2.Game:Abort`

Stops a login or camp that ISXOgreEQ2.Game:Login or :Camp started, resumes the bot if the camp had paused it, and prints aborted. Does nothing when nothing is running.

```text
ISXOgreEQ2.Game:Abort
```

### `Camp`

`ISXOgreEQ2.Game:Camp[mode]`

Camps out the current character, pausing the bot first and retrying the camp once if it fails; a failed camp resumes the bot if it was running. It refuses with a console line when you are not in the world or are in combat, and with no word it camps to the login screen and then closes the InnerSpace session.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `mode` | string | `""` | where to stop: charselect (or cs, select) camps to character select and stays; login (or loginscene, loginscreen) camps to the login screen and stays; empty or any other word camps to the login screen and closes the session |

```text
ISXOgreEQ2.Game:Camp[charselect]
```

### `ConvertAccounts`

`ISXOgreEQ2.Game:ConvertAccounts[overwrite]`

Copies every account and character from the legacy OldBot file EQ2OgreCommon/DoNotShareWithOthers/EQ2Chars.xml into the account store OgreSavePrivate/EQ2/Accounts.json, and prints how many it wrote. If the store already holds data it refuses with a console line unless you pass overwrite; the XML file is left untouched.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `overwrite` | string | `""` | overwrite, force or TRUE to replace an existing account store; anything else, or nothing, keeps it |

```text
ISXOgreEQ2.Game:ConvertAccounts
```

### `Login`

`ISXOgreEQ2.Game:Login[character]`

Logs the named character in from the saved account store, on its only or default server unless -s,&lt;server> follows the name, and as whatever class it was unless -c,&lt;class> does: it fills the login screen, clicks Connect, picks the character at character select if it stops there (first 10 slots only), and when that list does not hold it enters the world on the first listed character the account can play and camps to the login screen to log in from there, waiting up to 180 s to reach the world. It runs over the next frames with progress on the console; it stops with a message when no name is given, the character is locked, every listed character is locked, you are already in as that character, or no saved login exists for it, and if you are in the world on another character it first camps that one (not in combat, bot paused for the camp).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `character` | string |  | the character to log in; its account, password and server come from the saved account store |

```text
ISXOgreEQ2.Game:Login[${Me.Name}]
```
