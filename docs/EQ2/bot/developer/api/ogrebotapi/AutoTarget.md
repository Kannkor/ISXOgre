# OgreBotAPI.AutoTarget

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Members

### `Active`

`${OgreBotAPI.AutoTarget.Active}`

TRUE when the master checkbox is on, no Suppress reason is held, the working list has at least one entry, and the scanner may scan now: out of combat that needs Out Of Combat Scanning on or something hating you. It reads FALSE whenever nothing would be picked.

**Returns:** bool: TRUE when enabled, not suppressed, the list is not empty and the scanner may scan now; FALSE otherwise.

```text
echo ${OgreBotAPI.AutoTarget.Active}
```

### `Count`

`${OgreBotAPI.AutoTarget.Count}`

The number of entries in the working list - the list auto-target picks from right now.

**Returns:** int: the number of entries; 0 when the list is empty.

```text
echo ${OgreBotAPI.AutoTarget.Count}
```

*Was (OldBot):* `Ob_AutoTarget.Items`

### `Enabled`

`${OgreBotAPI.AutoTarget.Enabled}`

Reads the master auto-target checkbox from the profile. When it is off, auto-target never picks a target, whatever the list holds.

**Returns:** bool: TRUE when the auto-target checkbox is ticked; FALSE when it is unticked or was never set.

```text
echo ${OgreBotAPI.AutoTarget.Enabled}
```

*Was (OldBot):* `OgreBotAPI.AutoTarget_Enabled`

### `Entry`

`${OgreBotAPI.AutoTarget.Entry[n]}`

The working-list entry at position n, counting from 1, as JSON text with its fields: ActorName, MinHPToTarget, CheckCollision, AggroOnGroupOnly, MaxHPToTarget, AggroOnNonFighterOnly, AggroOnNotMe, and KeepLast when set.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `n` | int |  | Position in the working list, 1 = top. |

**Returns:** string: the entry as a JSON object; "{}" when n is out of range.

```text
echo ${OgreBotAPI.AutoTarget.Entry[1]}
```

*Was (OldBot):* `Ob_AutoTarget.AggroOnGroupOnly`, `Ob_AutoTarget.AggroOnGroupOnlyOrderedItem`, `Ob_AutoTarget.AggroOnNonFighterOnly`

### `EntryName`

`${OgreBotAPI.AutoTarget.EntryName[n]}`

The name of the working-list entry at position n, counting from 1 at the top.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `n` | int |  | Position in the working list, 1 = top. |

**Returns:** string: that entry's actor name; "" when n is out of range.

```text
echo ${OgreBotAPI.AutoTarget.EntryName[1]}
```

*Was (OldBot):* `Ob_AutoTarget.ActorName`, `Ob_AutoTarget.ActorNameOrderedItem`, `Ob_AutoTarget.OrderedItem`

### `HasActor`

`${OgreBotAPI.AutoTarget.HasActor[name]}`

Asks whether the working list has an entry with exactly this name, case not mattering. It compares entry names only - it does not test whether an entry would match a nearby actor.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | string |  | The entry name to look for (case does not matter). |

**Returns:** bool: TRUE when an entry's name equals the given name; FALSE when none does or no name is given.

```text
echo ${OgreBotAPI.AutoTarget.HasActor["a gnoll guard"]}
```

*Was (OldBot):* `Ob_AutoTarget.HasActor`

### `JSON`

`${OgreBotAPI.AutoTarget.JSON}`

The whole working list as JSON text, top entry first, each entry with the same fields Entry shows.

**Returns:** string: a JSON array of entries; "[]" when the list is empty.

```text
echo ${OgreBotAPI.AutoTarget.JSON}
```

*Was (OldBot):* `Ob_AutoTarget.Ob_AutoTargetList`

### `ListName`

`${OgreBotAPI.AutoTarget.ListName}`

The name of the saved list or built-in list the working list is: set by LoadSaved, Save and LoadPreset. It is blank after Clear, and after any entry is added, changed or removed, since the list then matches no saved list.

**Returns:** string: the saved-list or built-in list name; "" when none.

```text
echo ${OgreBotAPI.AutoTarget.ListName}
```

### `OutOfCombatScanning`

`${OgreBotAPI.AutoTarget.OutOfCombatScanning}`

Reads the out-of-combat scanning checkbox. When it is off, auto-target only looks for a target while you are in combat or something hates you.

**Returns:** bool: TRUE when out-of-combat scanning is ticked; FALSE when it is unticked or was never set (unset counts as off).

```text
echo ${OgreBotAPI.AutoTarget.OutOfCombatScanning}
```

### `PresetCount`

`${OgreBotAPI.AutoTarget.PresetCount}`

The number of built-in lists LoadPreset can load. There are two today: Named and AddsThenNamed.

**Returns:** int: the number of built-in lists.

```text
echo ${OgreBotAPI.AutoTarget.PresetCount}
```

### `PresetName`

`${OgreBotAPI.AutoTarget.PresetName[n]}`

The name of built-in list n, counting from 1.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `n` | int |  | Which built-in list, 1 = first. |

**Returns:** string: the built-in list's name; "" when n is out of range.

```text
echo ${OgreBotAPI.AutoTarget.PresetName[1]}
```

### `SavedCount`

`${OgreBotAPI.AutoTarget.SavedCount}`

The number of saved lists for the zone (lists are kept per zone), loading the current zone's lists first. Reads 0 out of the world.

**Returns:** int: the number of saved lists; 0 when the zone has none.

```text
echo ${OgreBotAPI.AutoTarget.SavedCount}
```

### `SavedName`

`${OgreBotAPI.AutoTarget.SavedName[n]}`

The name of saved list n for the zone, counting from 1, in file order, from the same lists as SavedCount. Reads "" out of the world.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `n` | int |  | Which saved list, 1 = first. |

**Returns:** string: the saved list's name; "" when n is out of range.

```text
echo ${OgreBotAPI.AutoTarget.SavedName[1]}
```

### `ScanHeight`

`${OgreBotAPI.AutoTarget.ScanHeight}`

Reads the scan height setting as stored - the largest height difference an actor may have from you and still be picked (it must be less than this). An unset or 0 value reads 0 here, but auto-target then uses 5.

**Returns:** int: the stored scan height; 0 when unset.

```text
echo ${OgreBotAPI.AutoTarget.ScanHeight}
```

### `ScanRadius`

`${OgreBotAPI.AutoTarget.ScanRadius}`

Reads the scan radius setting as stored. An unset or 0 value reads 0 here, but auto-target then scans 50.

**Returns:** int: the stored scan radius; 0 when unset.

```text
echo ${OgreBotAPI.AutoTarget.ScanRadius}
```

### `Suppressed`

`${OgreBotAPI.AutoTarget.Suppressed[key]}`

Asks whether auto-targeting is paused by Suppress. With no key it asks whether any reason is holding it; with a key it asks about that reason only (case does not matter).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `key` | string |  | Optional. The reason name given to Suppress; leave it out to ask about any reason. |

**Returns:** bool: TRUE when the reason (or, with no key, any reason) is holding targeting paused; FALSE otherwise.

```text
echo ${OgreBotAPI.AutoTarget.Suppressed[myscript]}
```

*Was (OldBot):* `OgreBotAPI.AutoTarget_Disabled`

### `WhenHated`

`${OgreBotAPI.AutoTarget.WhenHated}`

Reads the auto-target-when-hated checkbox. When it is on and the character has nothing to fight, the bot about once a second targets an NPC within 30 that is attacking the group, and says so in the console.

**Returns:** bool: TRUE when the checkbox is ticked; FALSE when it is unticked or was never set.

```text
echo ${OgreBotAPI.AutoTarget.WhenHated}
```

## Methods

### `AddActor`

`OgreBotAPI.AutoTarget:AddActor[fw, name, minHP=0, checkCollision=FALSE, aggroOnGroupOnly=TRUE, maxHP=0, aggroOnNonFighterOnly=FALSE, aggroOnNotMe=FALSE, keepLast=FALSE]`

Adds one entry to the working list (with no name it does nothing, and the same name can be added twice) and blanks ListName; auto-target tries entries top-down and takes the first entry that matches anything, keeping your current target if it matches. The working list lasts for this session only (it survives zoning) - use Save to keep it.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `name` | string |  | What to target: part of an actor name (matches any actor whose name contains it, case not mattering), NPC (any normal NPC), NamedNPC or Named (any named NPC), or a number for an actor ID. |
| `minHP` | int | `0` | Only pick the actor while its health is at least this percent; 0 = no limit. |
| `checkCollision` | bool | `FALSE` | TRUE to only pick actors you have a clear line to. |
| `aggroOnGroupOnly` | bool | `TRUE` | TRUE to only pick actors whose target is in your group. A word that is not yes/no keeps the default, TRUE. |
| `maxHP` | int | `0` | Only pick the actor while its health is below this percent; 0 = no limit. |
| `aggroOnNonFighterOnly` | bool | `FALSE` | TRUE to only pick actors targeting a player who is not a fighter. |
| `aggroOnNotMe` | bool | `FALSE` | TRUE to skip actors that are targeting you. |
| `keepLast` | bool | `FALSE` | TRUE to keep this entry at the bottom: later adds go in above it. |

```text
OgreBotAPI.AutoTarget:AddActor[igw:${Me.Name},"a gnoll guard",0,FALSE,TRUE]
```

*Was (OldBot):* `OgreBotAPI:AutoTarget_AddActor`, `Ob_AutoTarget:AddActor`

### `Clear`

`OgreBotAPI.AutoTarget:Clear[fw]`

Empties the working list and blanks ListName. Saved lists on disk are not touched.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.AutoTarget:Clear[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:AutoTarget_Clear`, `OgreBotAPI:AutoTarget_ClearActors`, `Ob_AutoTarget:Clear`

### `DeleteSaved`

`OgreBotAPI.AutoTarget:DeleteSaved[fw, name]`

Deletes a saved list from the current zone's file on disk; a blank name, or one that is not found, deletes nothing and says so on the console. The working list is not touched, but ListName is blanked when it named that list; it needs the character in the world.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `name` | string |  | The saved list to delete, matched whole, case not mattering. |

```text
OgreBotAPI.AutoTarget:DeleteSaved[${Me.Name},"Trash"]
```

*Was (OldBot):* `Ob_AutoTarget:DeleteList`

### `LoadPreset`

`OgreBotAPI.AutoTarget:LoadPreset[fw, name]`

Replaces the working list with a built-in list, reading nothing from disk, and sets ListName to it. An unknown name prints a message to the Inner Space console and leaves the list as it was.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `name` | string |  | The built-in list's name (see PresetName): Named (any named NPC) or AddsThenNamed (normal NPCs first, then the named), matched whole, case not mattering. |

```text
OgreBotAPI.AutoTarget:LoadPreset[igw:${Me.Name},AddsThenNamed]
```

### `LoadSaved`

`OgreBotAPI.AutoTarget:LoadSaved[fw, name]`

Replaces the working list with a saved list for the current zone and sets ListName. A blank name, or a name the zone has no list for, changes nothing and says so on the console; it needs the character in the world.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `name` | string |  | The saved list's name (see SavedName), matched whole, case not mattering. |

```text
OgreBotAPI.AutoTarget:LoadSaved[igw:${Me.Name},"Trash"]
```

*Was (OldBot):* `OgreBotAPI:LoadAutoTargetList`, `Ob_AutoTarget:LoadListFromSaveList`, `Ob_AutoTarget:LoadListFromSaveListForWho`

### `Release`

`OgreBotAPI.AutoTarget:Release[fw, reason]`

Releases the pause held under this reason name (case does not matter); a blank reason gets one line and a name that is not held does nothing. Targeting resumes only when no other reason is still held.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `reason` | string |  | The reason name given to Suppress. |

```text
OgreBotAPI.AutoTarget:Release[${Me.Name},myscript]
```

*Was (OldBot):* `OgreBotAPI:AutoTarget_Enable`

### `RemoveActor`

`OgreBotAPI.AutoTarget:RemoveActor[fw, name]`

Removes every working-list entry whose name is exactly this name, case not mattering. Nothing happens when no entry matches or the name is blank.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `name` | string |  | The entry name to remove (whole name, case does not matter). |

```text
OgreBotAPI.AutoTarget:RemoveActor[igw:${Me.Name},"a gnoll guard"]
```

*Was (OldBot):* `OgreBotAPI:AutoTarget_RemoveActor`, `Ob_AutoTarget:RemoveActor`

### `Save`

`OgreBotAPI.AutoTarget:Save[fw, name]`

Saves the working list to disk as a named list for the current zone and sets ListName; an existing list whose name matches, case not mattering, is replaced and moves to the end. A blank name, or a write that fails, saves nothing and says so on the console; it needs the character in the world.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `name` | string |  | The name to save the list under, kept as you typed it. |

```text
OgreBotAPI.AutoTarget:Save[${Me.Name},"Trash"]
```

*Was (OldBot):* `Ob_AutoTarget:SaveList`

### `SetEnabled`

`OgreBotAPI.AutoTarget:SetEnabled[fw, bool=TRUE]`

Turns the master auto-target checkbox on or off and prints the change to the OgreConsole when the value changes. The change goes to this profile's setting (the same one the panel shows) and reaches disk the next time the profile is saved; nothing is written when no profile is loaded.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `bool` | bool | `TRUE` | TRUE to turn auto-target on, FALSE to turn it off. Blank turns it on; a word that is not yes/no leaves it as it is. |

```text
OgreBotAPI.AutoTarget:SetEnabled[igw:${Me.Name},TRUE]
```

*Was (OldBot):* `ogre autotarget`

### `SetOutOfCombatScanning`

`OgreBotAPI.AutoTarget:SetOutOfCombatScanning[fw, bool=TRUE]`

Turns out-of-combat scanning on or off and prints the change to the OgreConsole when the value changes. The change goes to this profile's setting (the same one the panel shows) and reaches disk the next time the profile is saved; nothing is written when no profile is loaded.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `bool` | bool | `TRUE` | TRUE to let auto-target look for targets out of combat, FALSE to wait for combat or aggro. Blank turns it on; a word that is not yes/no leaves it as it is. |

```text
OgreBotAPI.AutoTarget:SetOutOfCombatScanning[igw:${Me.Name},TRUE]
```

### `SetScanHeight`

`OgreBotAPI.AutoTarget:SetScanHeight[fw, n=5]`

Silently sets the largest height difference an actor may have from you and still be picked. The change goes to this profile's setting (the same one the panel shows) and reaches disk the next time the profile is saved; nothing is written when no profile is loaded.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `n` | int | `5` | The scan height (the actor's height difference must be less than this). 0 or a non-number is treated as 5. |

```text
OgreBotAPI.AutoTarget:SetScanHeight[igw:${Me.Name},10]
```

*Was (OldBot):* `OgreBotAPI:AutoTarget_SetScanHeight`

### `SetScanRadius`

`OgreBotAPI.AutoTarget:SetScanRadius[fw, n=50]`

Silently sets how far auto-target looks for targets. The change goes to this profile's setting (the same one the panel shows) and reaches disk the next time the profile is saved; nothing is written when no profile is loaded.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `n` | int | `50` | The scan radius. A non-number stores 0, which auto-target treats as 50. |

```text
OgreBotAPI.AutoTarget:SetScanRadius[igw:${Me.Name},40]
```

*Was (OldBot):* `OgreBotAPI:AutoTarget_SetScanRadius`

### `SetWhenHated`

`OgreBotAPI.AutoTarget:SetWhenHated[fw, bool=TRUE]`

Turns auto-target-when-hated on or off and prints the change to the OgreConsole when the value changes. The change goes to this profile's setting (the same one the panel shows) and reaches disk the next time the profile is saved; nothing is written when no profile is loaded.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `bool` | bool | `TRUE` | TRUE to target an NPC attacking the group when you have nothing to fight, FALSE to stop. Blank turns it on; a word that is not yes/no leaves it as it is. |

```text
OgreBotAPI.AutoTarget:SetWhenHated[${Me.Name},TRUE]
```

### `Suppress`

`OgreBotAPI.AutoTarget:Suppress[fw, reason]`

Pauses automatic targeting under a reason name and holds the current target without touching the master checkbox; a direct target command still works, and a blank reason gets one line. Each reason lasts for this session only, until Release is called with the same name (case does not matter), LetsGo runs or you change zones.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `reason` | string |  | A name for this pause, so it can be released on its own. |

```text
OgreBotAPI.AutoTarget:Suppress[${Me.Name},myscript]
```

*Was (OldBot):* `OgreBotAPI:AutoTarget_Disable`
