# OgreBotAPI.HOs

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Members

### `DoEnabled`

`${OgreBotAPI.HOs.DoEnabled}`

TRUE while this character is running OgreBot's solo HO (started with DoSetup or DoSetEnabled); session only, never saved, and FALSE after a reload. It turns FALSE when the HO count is reached, the timeout runs out, the target dies or goes away, DoSetEnabled[...,FALSE] is called, or another group member takes over the solo HO.

**Returns:** bool: TRUE when the solo HO is running on this character; FALSE otherwise.

```text
echo ${OgreBotAPI.HOs.DoEnabled}
```

*Was (OldBot):* `OgreBotAPI.DoHO_Get_Enabled`

### `DoHOerID`

`${OgreBotAPI.HOs.DoHOerID}`

The actor ID of the OTHER group member who is running the solo HO, as that character announced it. Session only; 0 when this character is the one running it, or nobody is.

**Returns:** int64: the other HO'er's actor ID; 0 when it is this character or nobody.

```text
echo ${OgreBotAPI.HOs.DoHOerID}
```

*Was (OldBot):* `OgreBotAPI.DoHO_Get_HOerID`

### `DoPrimed`

`${OgreBotAPI.HOs.DoPrimed}`

TRUE once the solo HO has made its first full setup pass on this character (the group's HO settings set, stale casts cancelled, the HO'er announced); a later enable while primed only turns this character's own HO settings back on. Session only, and cleared by DoReset, by a disable, and when another session takes over.

**Returns:** bool: TRUE when the solo HO setup has been applied; FALSE otherwise.

```text
echo ${OgreBotAPI.HOs.DoPrimed}
```

*Was (OldBot):* `OgreBotAPI.DoHO_Get_Primed`

### `DoTargetID`

`${OgreBotAPI.HOs.DoTargetID}`

The actor ID given to DoSetup with -TargetID, the mob the solo HO is aimed at; 0 when no target was given, or after DoReset or a new DoSetup without one. Session only - note the casing: DoTargetID.

**Returns:** int64: the solo HO's target actor ID; 0 when none is set.

```text
echo ${OgreBotAPI.HOs.DoTargetID}
```

*Was (OldBot):* `OgreBotAPI.DoHo_Get_TargetID`

### `MyArchetypeStart`

`${OgreBotAPI.HOs.MyArchetypeStart}`

TRUE when the starter window is up and the heroic opportunity's centre icon is this character's own archetype, so the starter in progress is ours. FALSE when no starter is showing or it belongs to another archetype.

**Returns:** bool: TRUE when the starter showing is this character's archetype; FALSE otherwise, including when no heroic opportunity is up.

```text
echo ${OgreBotAPI.HOs.MyArchetypeStart}
```

*Was (OldBot):* `OgreBotAPI:MyArchetypeHOStart`

### `MyWheelTimeRemaining`

`${OgreBotAPI.HOs.MyWheelTimeRemaining}`

Seconds left on the HO timer, but only while the wheel is up and it is this character's archetype's wheel. Returns 0 when no heroic opportunity is up, it is still in the starter phase, or the wheel belongs to another archetype.

**Returns:** float: seconds left on this character's archetype's wheel; 0 otherwise.

```text
echo ${OgreBotAPI.HOs.MyWheelTimeRemaining}
```

*Was (OldBot):* `OgreBotAPI:MyArchetypeWheelTimeRemaining`

### `StarterClass`

`${OgreBotAPI.HOs.StarterClass}`

Which archetype's starter is up, from the starter window's centre icon, in lower case: fighter, priest, mage or scout. Empty when the starter window is not showing or no heroic opportunity is up.

**Returns:** string: fighter, priest, mage or scout; "" when no starter is showing.

```text
echo ${OgreBotAPI.HOs.StarterClass}
```

*Was (OldBot):* `OgreBotAPI.HO_Starter_Class`

### `StarterClassAvailable`

`${OgreBotAPI.HOs.StarterClassAvailable[class]}`

TRUE when the starter chain currently offers an icon that the given archetype can use. FALSE when the starter window is not up, no heroic opportunity is up, or class is not fighter, priest, mage or scout (any case).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `class` | string | `my archetype` | Archetype to check: fighter, priest, mage or scout (any case). Blank or left out means this character's own archetype. |

**Returns:** bool: TRUE when that archetype has an icon on the starter chain now; FALSE otherwise, including when no heroic opportunity is up.

```text
echo ${OgreBotAPI.HOs.StarterClassAvailable[scout]}
```

*Was (OldBot):* `OgreBotAPI.HO_Starter_Class_Available`

### `StarterVisible`

`${OgreBotAPI.HOs.StarterVisible}`

TRUE while the HO starter window (the chain of icons before the wheel) is showing. FALSE when no heroic opportunity is up or it has moved on to the wheel.

**Returns:** bool: TRUE when the starter window is up; FALSE otherwise, including when no heroic opportunity is up.

```text
echo ${OgreBotAPI.HOs.StarterVisible}
```

*Was (OldBot):* `OgreBotAPI.HO_Starter_Visible`

### `TargetID`

`${OgreBotAPI.HOs.TargetID}`

The actor ID the bot recorded as the HO target: set when this character's bot casts an HO start, and when another group member's bot announces one. Returns 0 when no heroic opportunity is up or that actor no longer exists.

**Returns:** int64: the HO target's actor ID; 0 when no heroic opportunity is up, the actor is gone, or no start has been recorded.

```text
echo ${OgreBotAPI.HOs.TargetID}
```

*Was (OldBot):* `OgreBotAPI.HO_TargetID`

### `Visible`

`${OgreBotAPI.HOs.Visible}`

TRUE while a heroic opportunity is up in any phase (starter, wheel or finishing); FALSE when none is up or out of world. The HO reads are refreshed at most every 250 ms, so a value can be up to a quarter second old.

**Returns:** bool: TRUE when a heroic opportunity is up; FALSE when none is up or not in world.

```text
echo ${OgreBotAPI.HOs.Visible}
```

*Was (OldBot):* `OgreBotAPI.HO_Visible`

### `WheelClassAvailable`

`${OgreBotAPI.HOs.WheelClassAvailable[class]}`

TRUE when the wheel currently has a step the given archetype can complete right now. FALSE when the wheel is not up, no heroic opportunity is up, or class is not fighter, priest, mage or scout (any case).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `class` | string | `my archetype` | Archetype to check: fighter, priest, mage or scout (any case). Blank or left out means this character's own archetype. |

**Returns:** bool: TRUE when that archetype has a completable step on the wheel now; FALSE otherwise, including when no heroic opportunity is up.

```text
echo ${OgreBotAPI.HOs.WheelClassAvailable[mage]}
```

*Was (OldBot):* `OgreBotAPI.HO_Class_Available`, `OgreBotAPI.HO_Wheel_Class_Available`

### `WheelName`

`${OgreBotAPI.HOs.WheelName}`

The heroic opportunity name shown on the wheel, read from the HO window itself. Empty when no heroic opportunity is up; it can also be empty or stale during the starter phase, so check WheelVisible first.

**Returns:** string: the wheel's HO name; "" when no heroic opportunity is up.

```text
echo ${OgreBotAPI.HOs.WheelName}
```

*Was (OldBot):* `OgreBotAPI.HO_Wheel_Name`

### `WheelVisible`

`${OgreBotAPI.HOs.WheelVisible}`

TRUE while the HO wheel is showing. FALSE when no heroic opportunity is up or it is still in the starter phase.

**Returns:** bool: TRUE when the wheel is up; FALSE otherwise, including when no heroic opportunity is up.

```text
echo ${OgreBotAPI.HOs.WheelVisible}
```

*Was (OldBot):* `OgreBotAPI.HO_Wheel_Visible`

## Methods

### `Advance`

`OgreBotAPI.HOs:Advance[fw]`

Takes one turn on an open wheel, casting each of this character's abilities once for the wheel steps its archetype can complete now; it follows "Offensive Only" and "HO - Change Target", works while the bot is paused, and suits scripts that keep "HO Wheel" off and drive the wheel themselves. It does nothing with no heroic opportunity or wheel up, no step for this archetype, "Last to Complete" on while other archetypes still have steps, "HO - allow unknown target" off with no known HO target, or within 1 second of the last advance.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.HOs:Advance[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:HO_Advance`, `OgreBotAPI:HO_Wheel_Advance`

### `AllowIcon`

`OgreBotAPI.HOs:AllowIcon[fw, icon]`

Adds an HO icon ID to the allow list; while the list has any icon, cast stack abilities that carry a different HO icon are skipped (abilities with no HO icon are not affected, the disable list wins over it, and the bot's own HO starter and wheel casts are not steered). Session only - never saved to the profile, kept until cleared, LetsGo or the extension reloads.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `icon` | int |  | HO icon ID: fighter 0-5, priest 12-17, mage 24-29, scout 36-41. Required; an icon already in the list does nothing. A missing icon, or a word that is not a whole number, is refused with a console line and changes nothing. |

```text
OgreBotAPI.HOs:AllowIcon[${Me.Name},25]
```

*Was (OldBot):* `OgreBotAPI:Set_Allow_HOICon`

### `CancelStarter`

`OgreBotAPI.HOs:CancelStarter[fw]`

Cancels the HO starter window right away by sending the game's cancel HO starter command. Does nothing when no heroic opportunity is up or the starter window is not showing (a running wheel is never cancelled).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.HOs:CancelStarter[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:HO_Cancel_Starter`

### `ClearAllowIcon`

`OgreBotAPI.HOs:ClearAllowIcon[fw, icon]`

Removes one HO icon ID from the allow list (session only). When the list becomes empty, no ability is skipped for its HO icon by this list.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `icon` | int |  | HO icon ID to remove from the allow list. Required; an icon not in the list does nothing. A missing icon, or a word that is not a whole number, is refused with a console line and changes nothing. |

```text
OgreBotAPI.HOs:ClearAllowIcon[${Me.Name},25]
```

*Was (OldBot):* `OgreBotAPI:Clear_Allow_HOICon`

### `ClearAllowIcons`

`OgreBotAPI.HOs:ClearAllowIcons[fw]`

Empties the HO icon allow list (session only), so the cast stack no longer skips abilities for being outside it. The disable list is not touched.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.HOs:ClearAllowIcons[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Clear_Allow_HOICons`

### `ClearDisableIcon`

`OgreBotAPI.HOs:ClearDisableIcon[fw, icon]`

Removes one HO icon ID from the disable list, so abilities with that icon can be cast again (subject to the allow list). Session only; an icon not in the list does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `icon` | int |  | HO icon ID to remove from the disable list. Required. A missing icon, or a word that is not a whole number, is refused with a console line and changes nothing. |

```text
OgreBotAPI.HOs:ClearDisableIcon[${Me.Name},14]
```

*Was (OldBot):* `OgreBotAPI:Clear_Disable_HOICon`

### `ClearDisableIcons`

`OgreBotAPI.HOs:ClearDisableIcons[fw]`

Empties the HO icon disable list (session only). The allow list is not touched, and the per-icon disable checkboxes in the profile are a separate setting and stay as they are.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.HOs:ClearDisableIcons[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Clear_Disable_HOICons`

### `DisableIcon`

`OgreBotAPI.HOs:DisableIcon[fw, icon]`

Adds an HO icon ID to the disable list, so cast stack abilities that carry that HO icon are skipped even if the icon is also in the allow list; the bot's own HO starter and wheel casts are not steered. Session only - never saved to the profile, kept until cleared, LetsGo or the extension reloads.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `icon` | int |  | HO icon ID: fighter 0-5, priest 12-17, mage 24-29, scout 36-41. Required. A missing icon, or a word that is not a whole number, is refused with a console line and changes nothing. |

```text
OgreBotAPI.HOs:DisableIcon[${Me.Name},14]
```

*Was (OldBot):* `OgreBotAPI:Set_Disable_HOICon`

### `DoReset`

`OgreBotAPI.HOs:DoReset[fw]`

Clears this character's solo HO record (session only): target, HO count and completions, the leave-open and cast stack options, the other HO'er's ID and the primed flag. It does not turn the solo HO on or off, change the timeout, or change any settings.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.HOs:DoReset[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:DoHO_Reset`

### `DoSetEnabled`

`OgreBotAPI.HOs:DoSetEnabled[fw, on=TRUE, option...]`

Turns OgreBot's solo HO on or off on this character without clearing its record (use DoSetup to set the target and count); calling it with the state it already has does nothing unless -Force, and a value that is not a yes/no word does nothing. On/off is session only, and the settings it writes are profile options in memory, kept on disk only if the profile is saved before they are put back.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `on` | bool | `TRUE` | TRUE to run the solo HO here: makes this character the HO'er, tells the rest of the group to stand down, cancels another archetype's starter if one is up, writes the group's HO settings, cancels group casts with more than 0.5 seconds left, holds the first start for -DelayStart seconds (default 1) and extends the timeout to at least 25 seconds (or sets it to -TimeOut n). FALSE to stop it: puts back this character's HO settings and asks the group to put back theirs. |
| `option...` | flags |  | Any of -Force (run even if already in that state), -NoEnable / -PrimeOnly / -NoStart (set the group up but leave this character's HO settings off), -NoHoAbilities (on FALSE, keep HO abilities disabled on the rest of the group), -TimeOut n, -DelayStart n. Unknown words are ignored. |

```text
OgreBotAPI.HOs:DoSetEnabled[${Me.Name},FALSE]
```

*Was (OldBot):* `OgreBotAPI:DoHO_Set_Enable`

### `DoSetup`

`OgreBotAPI.HOs:DoSetup[fw, option...]`

Starts OgreBot's solo HO with this character as the one who starts it (no HO needs to be up): it clears the previous record, starts a 25 second timeout and enables it as DoSetEnabled[fw,TRUE,...] with the same options, turning HO Start, Starter and Wheel off for the group and on for this character and setting the group's HO helper settings. It ends after -NumHOsToComplete completions (default 1), on timeout, or when the -TargetID mob dies or goes away, and every session then puts back the HO settings it had; the record is session only, and the changed HO settings are profile options in memory, written to disk only if the profile is saved while they are changed.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `option...` | flags |  | Any of -TargetID id, -NumHOsToComplete n, -TimeOut n (instead of 25 seconds), -LeaveStartOpen, -LeaveWheelOpen, -AllowCastStack (keep this character's cast stack on), -NoModifyOptions (change no settings), -Force (when the solo HO is already running, apply the settings again instead of only recording the new options), -NoEnable, -DelayStart n, -NoHoAbilities, in any order; the DoSetEnabled options work here too. Unknown words are ignored. |

```text
OgreBotAPI.HOs:DoSetup[${Me.Name},-TargetID,${Target.ID},-NumHOsToComplete,1,-TimeOut,30]
```

*Was (OldBot):* `OgreBotAPI:DoHO_Setup`

### `RestoreSetUpFor`

`OgreBotAPI.HOs:RestoreSetUpFor[fw]`

Puts "Heroic Surge (ROC Adorn)" back to the value SetUpFor remembered, quietly, and forgets it. Does nothing if SetUpFor was not called since the last restore, or the extension was reloaded in between.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.HOs:RestoreSetUpFor[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Restore_SetUpFor_HOs`

### `SetUpFor`

`OgreBotAPI.HOs:SetUpFor[fw]`

Readies a fight that needs HOs controlled, with or without an HO up: remembers the current "Heroic Surge (ROC Adorn)" setting (only on the first call before a RestoreSetUpFor), then turns it off quietly so the adornment cannot start or advance HOs on its own. The remembered value is session only; the setting itself is a profile option changed in memory, so saving the profile before RestoreSetUpFor keeps it off on disk.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.HOs:SetUpFor[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:SetUpFor_HOs`

### `Start`

`OgreBotAPI.HOs:Start[fw, -ActorID id, -SkipTimer]`

Casts this character's archetype HO starter ability (Fighting Chance, Lucky Break, Divine Providence or Arcane Augur) once, immediately, even while the bot is paused, and tells the group which actor the HO is on. Nothing happens within 1 second of the last start unless -SkipTimer is given, or when the ability is not ready, out of range or the cast bar is busy - call it again to retry.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `-ActorID id` | flag + number |  | Start the HO on this actor ID instead of the current target; -TargetID id is the same flag. Without it the cast goes at the current target and does nothing while any heroic opportunity is already up. With it, nothing happens if that actor is gone or a wheel is already running, and if another archetype's starter is up it is cancelled and the cast goes on the actor once the starter closes and the ability is ready (giving up after about 8 seconds). |
| `-SkipTimer` | flag |  | Ignore the 1 second wait after the last start. |

```text
OgreBotAPI.HOs:Start[${Me.Name},-ActorID,${Target.ID}]
```

*Was (OldBot):* `OgreBotAPI:HO_Start`

### `Starter`

`OgreBotAPI.HOs:Starter[fw]`

Takes one turn on an open starter chain, casting this character's abilities for the starter icons its archetype is offered; it follows "HO - Change Target" and works while the bot is paused. It does nothing when no heroic opportunity or starter window is up, this archetype has no icon in the chain, "HO - allow unknown target" is off and no HO target is known, or within 1 second of the last starter cast.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.HOs:Starter[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:HO_Starter`, `OgreBotAPI:HO_Starter_Advance`
