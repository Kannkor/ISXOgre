# OgreBotAPI.Options

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Members

### `Value`

`${OgreBotAPI.Options.Value[id]}`

Reads a stored OgreBot option for this character by its control id, matching the id in any case. Needs no for-who; an id the profile does not hold reads the same as an empty value.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `id` | string |  | The option's control id, as saved in the profile |

**Returns:** string: the option's current value (a checkbox reads TRUE or FALSE); "" when the id is absent, empty, or no id is given

```text
echo ${OgreBotAPI.Options.Value[checkbox_settings_enable_chatevents]}
```

*Was (OldBot):* `OgreOSA.Enabled`, `OgreOSA.ScanRadius`, `OgreOSA.TargetsOnly`

## Methods

### `LoadProfile`

`OgreBotAPI.Options:LoadProfile[fw, name]`

Loads the named OgreBot profile for this character, opening OgreBot first if it is not open; Use_UI reloads the current profile. A missing name gets one line and loads nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `name` | string |  | Profile name, or Use_UI for the current profile. Required. |

```text
OgreBotAPI.Options:LoadProfile[${Me.Name},Raid]
```

*Was (OldBot):* `ProfileConfig:LoadProfileForWho`, `OgreBotAPI:LoadProfile`, `ProfileConfig:LoadProfile`

### `Revert`

`OgreBotAPI.Options:Revert[fw, source]`

Puts back every option that scripts, commands or encounters changed since the last revert, then forgets those changes; changes you made yourself in the OgreBot window are never reverted. Prints "options: reverted N" with the source in the console.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `source` | string |  | Which writer's changes to put back: an encounter's key, command for typed and script changes, or all / empty for every source |

```text
OgreBotAPI.Options:Revert[${Me.Name},all]
```

*Was (OldBot):* `OgreBotAPI:RevertOptions`, `Obj_LICH:HODefaultSettings`

### `Set`

`OgreBotAPI.Options:Set[fw, silent|loud|verbose="", (id,value)..., silent=FALSE]`

Writes one or more OgreBot options by control id in the loaded profile, prints each real change in OgreConsole unless silenced, and remembers the old value so Revert can put it back. The write is unsaved until Save, and does nothing when no profile is loaded.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `silent\|loud\|verbose` | string | `""` | Optional, before an id: silent turns the change lines off, loud or verbose turns them on |
| `(id,value)...` | string |  | Pairs of control id and new value; a TRUE or FALSE after a value, with more pairs after it, sets silent too |
| `silent` | bool | `FALSE` | A TRUE or FALSE at the very end: TRUE makes the whole call silent |

```text
OgreBotAPI.Options:Set[all,checkbox_settings_enable_chatevents,TRUE]
```

*Was (OldBot):* `OgreBotAPI:ChangeOgreBotUIOption`, `OgreBotAPI:UplinkOptionChange`, `Obj_OgreUtilities:Set_EQ2_onQuestOffered`

### `WarnBeforeSave`

`OgreBotAPI.Options:WarnBeforeSave[fw]`

Shows a warning beside Save in this character's OgreBot window saying the Instance Controller has run and settings may have changed, until a profile is loaded. Save still works while it is up; the Instance Controller sends this to its group itself.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Options:WarnBeforeSave[igw:${Me.Name}]
```
