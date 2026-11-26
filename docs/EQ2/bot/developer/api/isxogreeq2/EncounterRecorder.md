# ISXOgreEQ2.EncounterRecorder

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Methods

### `BuildPages`

`ISXOgreEQ2.EncounterRecorder:BuildPages[zone,rebuild]`

Builds the readable pages from every recording on this PC, the window's Build pages button; it needs Node.js. It returns at once, and the window and the console say how the build ended.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `zone` | string | `none` | The word zone: only this zone's recordings. Leave it out for all of them. |
| `rebuild` | string | `none` | The word rebuild: every pull is read and every page made again. Leave it out to make only what changed. |

```text
ISXOgreEQ2.EncounterRecorder:BuildPages
```

### `End`

`ISXOgreEQ2.EncounterRecorder:End`

Stops everything - recording, an open fight's file and a page build this session started - and closes the window, the same as `ogre end er` and the window's X.

```text
ISXOgreEQ2.EncounterRecorder:End
```

### `EveryDet`

`ISXOgreEQ2.EncounterRecorder:EveryDet[state]`

Whether every det is examined, not one for each pair of icons - for dets that share their icons. Saved for every box of this PC.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `state` | string | `none` | on or off. Leave it out to be told what it is now. |

```text
ISXOgreEQ2.EncounterRecorder:EveryDet["on"]
```

### `Help`

`ISXOgreEQ2.EncounterRecorder:Help`

Prints the words of `ogre er` to the console.

```text
ISXOgreEQ2.EncounterRecorder:Help
```

### `Mark`

`ISXOgreEQ2.EncounterRecorder:Mark[text]`

Writes a note on the fight's timeline, the same as `ogre er mark <text>`. Recording must be on.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `text` | string | `none` | The note. Several arguments are joined with spaces. |

```text
ISXOgreEQ2.EncounterRecorder:Mark["boss at 50%"]
```

### `NpcEffects`

`ISXOgreEQ2.EncounterRecorder:NpcEffects[state]`

Whether this session reads the names of effects on NPCs, saved for this session on this PC. The session is1 reads them unless switched off; no other session does unless switched on.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `state` | string | `none` | on or off. Leave it out to be told what it is now. |

```text
ISXOgreEQ2.EncounterRecorder:NpcEffects["on"]
```

### `Off`

`ISXOgreEQ2.EncounterRecorder:Off`

Stops recording, the same as `ogre er off`: an open fight's file is ended. The window stays open.

```text
ISXOgreEQ2.EncounterRecorder:Off
```

### `OffForWho`

`ISXOgreEQ2.EncounterRecorder:OffForWho`

Sends `off` to every box the MCP For Who window names, the same way as :OnForWho.

```text
ISXOgreEQ2.EncounterRecorder:OffForWho
```

### `On`

`ISXOgreEQ2.EncounterRecorder:On`

Records every fight by itself from the pull on and opens the window, the same as `ogre er on`. It is never on by itself: each box is switched on after every login, and out of the world nothing happens.

```text
ISXOgreEQ2.EncounterRecorder:On
```

### `OnForWho`

`ISXOgreEQ2.EncounterRecorder:OnForWho`

Sends `on` to every box the MCP For Who window names, over oc or IRC as that window says. This box switches on only when the For Who names it too.

```text
ISXOgreEQ2.EncounterRecorder:OnForWho
```

### `Open`

`ISXOgreEQ2.EncounterRecorder:Open`

Opens the Encounter Recorder window, the same as bare `ogre er`.

```text
ISXOgreEQ2.EncounterRecorder:Open
```

### `Pets`

`ISXOgreEQ2.EncounterRecorder:Pets[state]`

Whether rows are written for pets, saved for every box of this PC. Off unless switched on.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `state` | string | `none` | on or off. Leave it out to be told what it is now. |

```text
ISXOgreEQ2.EncounterRecorder:Pets["on"]
```

### `RecordTrash`

`ISXOgreEQ2.EncounterRecorder:RecordTrash[state]`

"Record trash pulls": whether a fight with no named is written too, saved for every box of this PC. Off unless switched on, and it takes hold with the next fight.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `state` | string | `none` | on or off. Leave it out to be told what it is now. |

```text
ISXOgreEQ2.EncounterRecorder:RecordTrash["on"]
```

### `Start`

`ISXOgreEQ2.EncounterRecorder:Start`

Begins a fight's file by hand, for an event that never puts you in combat; it ends on :Stop. Recording must be on.

```text
ISXOgreEQ2.EncounterRecorder:Start
```

### `Status`

`ISXOgreEQ2.EncounterRecorder:Status`

Prints what it is doing, what it has written and its switches to the console, the same as `ogre er status`.

```text
ISXOgreEQ2.EncounterRecorder:Status
```

### `Stop`

`ISXOgreEQ2.EncounterRecorder:Stop`

Ends the open fight's file that :Start began, the same as `ogre er stop`.

```text
ISXOgreEQ2.EncounterRecorder:Stop
```

### `UploadFights`

`ISXOgreEQ2.EncounterRecorder:UploadFights[state]`

The switch "Upload each finished fight", saved for every box of this PC: each box sends its own file to the raid's Encounters page a few seconds after the fight ends. On unless switched off; now sends this toon's files the raid does not have yet.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `state` | string | `none` | on, off, or now. Leave it out to be told what it is now. |

```text
ISXOgreEQ2.EncounterRecorder:UploadFights["now"]
```

### `UploadRaid`

`ISXOgreEQ2.EncounterRecorder:UploadRaid[slug]`

The raid whose Encounters page gets the recordings, saved for every box of this PC. With no raid named nothing is sent.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `slug` | string | `none` | The last part of the raid page's address (lower-case letters, digits and -), or none for no raid. Leave it out to be told the raid. |

```text
ISXOgreEQ2.EncounterRecorder:UploadRaid["my-raid"]
```

### `UploadRaids`

`ISXOgreEQ2.EncounterRecorder:UploadRaids`

Asks the site for the raids this PC may send to, the window's Refresh. The answer comes a moment later, in the console and as a list under the window's raid field.

```text
ISXOgreEQ2.EncounterRecorder:UploadRaids
```
