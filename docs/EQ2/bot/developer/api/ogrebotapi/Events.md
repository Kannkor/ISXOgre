# OgreBotAPI.Events

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Methods

### `AddChatEntry`

`OgreBotAPI.Events:AddChatEntry[fw, text, oc, ding, code]`

Adds a row to the Chat Events tab of the loaded profile: when a line in the chat window contains text (any case), it announces in OgreConsole (oc), plays the ding sound (ding) and runs code as a command, in that order, with no arguments passed to the code. The row is unsaved until Save, only fires while the tab is ticked on the Settings tab (it warns if not), a blank text or an identical enabled row is refused with a console line, and every session's console is told it was added.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `text` | string |  | Text to watch for - matched as a case-insensitive substring of each incoming chat-window line |
| `oc` | bool |  | TRUE to send `<name> -> <kind> event -> (<text>) found -> <match>` to OgreConsole when it fires |
| `ding` | bool |  | TRUE to play the ding sound when it fires |
| `code` | string |  | A command line to run when it fires (run on the next frame, may be empty); any extra arguments after it are joined back on with commas |

```text
OgreBotAPI.Events:AddChatEntry[igw:${Me.Name},"tells you",TRUE,TRUE,"echo got a tell"]
```

*Was (OldBot):* `OgreBotAPI:ChatEvent_AddEntry`

### `AddDespawnEntry`

`OgreBotAPI.Events:AddDespawnEntry[fw, text, oc, ding, code]`

Adds a row to the Despawn Events tab of the loaded profile: when an actor despawns whose name contains text (case-sensitive), it announces in OgreConsole (oc), plays the ding sound (ding) and runs code as a command, in that order, with no arguments passed to the code. The row is unsaved until Save, only fires while the tab is ticked on the Settings tab (it warns if not), a blank text or an identical enabled row is refused with a console line, and every session's console is told it was added.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `text` | string |  | Text to watch for - matched as a case-sensitive substring of the despawning actor's name |
| `oc` | bool |  | TRUE to send `<name> -> <kind> event -> (<text>) found -> <match>` to OgreConsole when it fires |
| `ding` | bool |  | TRUE to play the ding sound when it fires |
| `code` | string |  | A command line to run when it fires (run on the next frame, may be empty); any extra arguments after it are joined back on with commas |

```text
OgreBotAPI.Events:AddDespawnEntry[${Me.Name},"a cursed spirit",TRUE,FALSE,"echo spirit is gone"]
```

*Was (OldBot):* `OgreBotAPI:DespawnEvent_AddEntry`

### `AddSpawnEntry`

`OgreBotAPI.Events:AddSpawnEntry[fw, text, oc, ding, code]`

Adds a row to the Spawn Events tab of the loaded profile: when an actor spawns whose name contains text (case-sensitive), it announces in OgreConsole (oc), plays the ding sound (ding) and runs code as a command, in that order, with no arguments passed to the code. The row is unsaved until Save, only fires while the tab is ticked on the Settings tab (it warns if not), a blank text or an identical enabled row is refused with a console line, and every session's console is told it was added.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `text` | string |  | Text to watch for - matched as a case-sensitive substring of the spawning actor's name |
| `oc` | bool |  | TRUE to send `<name> -> <kind> event -> (<text>) found -> <match>` to OgreConsole when it fires |
| `ding` | bool |  | TRUE to play the ding sound when it fires |
| `code` | string |  | A command line to run when it fires (run on the next frame, may be empty); any extra arguments after it are joined back on with commas |

```text
OgreBotAPI.Events:AddSpawnEntry[${Me.Name},"a cursed spirit",TRUE,TRUE,"echo spirit is up"]
```

*Was (OldBot):* `OgreBotAPI:SpawnEvent_AddEntry`

### `RemoveChatEntry`

`OgreBotAPI.Events:RemoveChatEntry[fw, text=all]`

Removes every Chat Events row whose text equals text (any case, disabled rows included), or every row for all, and tells every session's console which rows went. The change is unsaved until Save; no match, no loaded profile or a text passed but empty each print a console line and remove nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `text` | string | `all` | The watch text of the rows to remove, or all for every row |

```text
OgreBotAPI.Events:RemoveChatEntry[igw:${Me.Name},"tells you"]
```

*Was (OldBot):* `OgreBotAPI:ChatEvent_RemoveEntry`

### `RemoveDespawnEntry`

`OgreBotAPI.Events:RemoveDespawnEntry[fw, text=all]`

Removes every Despawn Events row whose text equals text (any case, disabled rows included), or every row for all, and tells every session's console which rows went. The change is unsaved until Save; no match, no loaded profile or a text passed but empty each print a console line and remove nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `text` | string | `all` | The watch text of the rows to remove, or all for every row |

```text
OgreBotAPI.Events:RemoveDespawnEntry[${Me.Name},all]
```

*Was (OldBot):* `OgreBotAPI:DespawnEvent_RemoveEntry`

### `RemoveSpawnEntry`

`OgreBotAPI.Events:RemoveSpawnEntry[fw, text=all]`

Removes every Spawn Events row whose text equals text (any case, disabled rows included), or every row for all, and tells every session's console which rows went. The change is unsaved until Save; no match, no loaded profile or a text passed but empty each print a console line and remove nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `text` | string | `all` | The watch text of the rows to remove, or all for every row |

```text
OgreBotAPI.Events:RemoveSpawnEntry[${Me.Name},"a cursed spirit"]
```

*Was (OldBot):* `OgreBotAPI:SpawnEvent_RemoveEntry`
