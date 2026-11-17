# OgreBotAPI.Util

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Members

### `Between`

`${OgreBotAPI.Util.Between[v,lo,hi]}`

TRUE when v is from lo to hi with both ends included, compared as whole numbers, so decimals are cut off before comparing. If lo is greater than hi the answer is always FALSE.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `v` | int64 | `0` | The number to test. |
| `lo` | int64 | `0` | The lowest allowed value, included. |
| `hi` | int64 | `0` | The highest allowed value, included. |

**Returns:** bool: TRUE when lo &lt;= v &lt;= hi; FALSE otherwise.

```text
echo ${OgreBotAPI.Util.Between[${Me.Level},50,60]}
```

*Was (OldBot):* `OgreBotAPI.Between`

### `BetweenFloat`

`${OgreBotAPI.Util.BetweenFloat[v,lo,hi]}`

TRUE when v is from lo to hi with both ends included, compared as decimal numbers. If lo is greater than hi the answer is always FALSE.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `v` | float | `0` | The number to test. |
| `lo` | float | `0` | The lowest allowed value, included. |
| `hi` | float | `0` | The highest allowed value, included. |

**Returns:** bool: TRUE when lo &lt;= v &lt;= hi; FALSE otherwise.

```text
echo ${OgreBotAPI.Util.BetweenFloat[${Target.Distance},0,7.5]}
```

*Was (OldBot):* `OgreBotAPI.BetweenFloat`

### `Clean`

`${OgreBotAPI.Util.Clean[s]}`

Tidies a name: when it has a dot, only the part after the last dot is kept, otherwise the brackets ( and ) are removed. A name starting with Skyshrine Infiltrator or Skyshrine Guardian comes back as Skyshrine_Infiltrator or Skyshrine_Guardian.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `s` | string |  | The name to tidy, usually an actor or effect name. |

**Returns:** string: the tidied name.

```text
echo ${OgreBotAPI.Util.Clean[${Target.Name}]}
```

*Was (OldBot):* `Obj_OgreUtilities.CleanName`, `OgreBotAPI.CleanNameWithSpaces`, `GetInfoOb.Clean`

### `FileExists`

`${OgreBotAPI.Util.FileExists[path]}`

TRUE when the file exists, also trying it with .iss added; a path without a colon is looked up under the Inner Space Scripts folder. A folder is not a file, and an empty path returns FALSE.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `path` | string |  | A full path, or a path relative to the Scripts folder such as EQ2OgreBot/OgreBot. The .iss ending may be left off. |

**Returns:** bool: TRUE when the file exists, as given or with .iss added; FALSE otherwise.

```text
echo ${OgreBotAPI.Util.FileExists["EQ2OgreBot/OgreBot"]}
```

*Was (OldBot):* `OgreBotAPI.FileExists`

### `Hours`

`${OgreBotAPI.Util.Hours[n]}`

Returns the hours part of a number of seconds, wrapped at 24 so whole days are dropped. 90000 seconds (25 hours) gives 1.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `n` | int64 | `0` | The number of seconds. |

**Returns:** int64: the hours, 0 to 23.

```text
echo ${OgreBotAPI.Util.Hours[7500]}
```

*Was (OldBot):* `Obj_OgreUtilities.Get_Hours`, `OgreBotAPI.Get_Hours`

### `IEquals`

`${OgreBotAPI.Util.IEquals[a,b]}`

TRUE when the two texts are the same, ignoring upper and lower case. Two empty texts count as equal.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `a` | string |  | The first text. |
| `b` | string |  | The second text. |

**Returns:** bool: TRUE when a and b match ignoring case; FALSE otherwise.

```text
echo ${OgreBotAPI.Util.IEquals[${Target.Name},${Me.Name}]}
```

*Was (OldBot):* `OgreBotAPI.PE_ThisMember`

### `MD5`

`${OgreBotAPI.Util.MD5[s]}`

Returns the MD5 hash of the text as 32 lowercase hex characters. With no argument it hashes empty text.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `s` | string |  | The text to hash, exactly as given. |

**Returns:** string: the 32-character lowercase hex MD5 of the text.

```text
echo ${OgreBotAPI.Util.MD5["hello"]}
```

*Was (OldBot):* `ISXOgre.MD5`, `OgreBotAPI.MD5`

### `Minutes`

`${OgreBotAPI.Util.Minutes[n]}`

Returns the minutes part of a number of seconds, 0 to 59. 7500 seconds gives 5.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `n` | int64 | `0` | The number of seconds. |

**Returns:** int64: the minutes, 0 to 59.

```text
echo ${OgreBotAPI.Util.Minutes[7500]}
```

*Was (OldBot):* `Obj_OgreUtilities.Get_Minutes`, `OgreBotAPI.Get_Minutes`

### `RomanToInt`

`${OgreBotAPI.Util.RomanToInt[s]}`

Reads a Roman numeral made of I, V, X and L (upper or lower case) and returns its value, so XLIV gives 44. Any other character, including C, D, M or a space, makes the whole answer 0.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `s` | string |  | The Roman numeral, for example XLIV. Only I, V, X and L are understood. |

**Returns:** int: the value of the numeral; 0 when the text is empty or has any other character.

```text
echo ${OgreBotAPI.Util.RomanToInt[XLIV]}
```

*Was (OldBot):* `OgreBotAPI.RomanToInt`

### `RoundToNearest`

`${OgreBotAPI.Util.RoundToNearest[value,step,incBy]}`

Rounds a whole number to the nearest multiple of step, then adds incBy; an exact half rounds up, so 45 with step 10 gives 50 and 44 gives 40. 0 and negative values are rounded the same way, and a step below 1 is used as 1.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `value` | int | `0` | The number to round. Decimals are cut off; 0 and negatives are kept. |
| `step` | int | `1` | Round to a multiple of this, for example 10. Anything below 1 is used as 1. |
| `incBy` | int | `0` | Added to the rounded result. |

**Returns:** int: the rounded value plus incBy.

```text
echo ${OgreBotAPI.Util.RoundToNearest[${Me.Level},10,0]}
```

*Was (OldBot):* `OgreBotAPI.RoundNumToNearestValue`

### `Seconds`

`${OgreBotAPI.Util.Seconds[n]}`

Returns the seconds part of a number of seconds, 0 to 59. 7530 seconds gives 30.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `n` | int64 | `0` | The number of seconds. |

**Returns:** int64: the seconds, 0 to 59.

```text
echo ${OgreBotAPI.Util.Seconds[7530]}
```

*Was (OldBot):* `Obj_OgreUtilities.Get_Seconds`, `OgreBotAPI.Get_Seconds`

### `SecondsToHMS`

`${OgreBotAPI.Util.SecondsToHMS[n]}`

Formats a number of seconds as timer text in days, hours, minutes and seconds, like "1d 2h 5m 30s". A part that is 0 is left out, so 300 gives "5m" and 45 gives "45s".

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `n` | int64 | `0` | The number of seconds to format. |

**Returns:** string: the time, for example "2h 5m"; "0s" for 0 or less.

```text
echo ${OgreBotAPI.Util.SecondsToHMS[7500]}
```

*Was (OldBot):* `Obj_OgreUtilities.ConvertSecondsToHMS`, `OgreBotAPI.ConvertSecondsToHMS`

### `SlotArrayToSlot`

`${OgreBotAPI.Util.SlotArrayToSlot[n]}`

Returns n plus 1, turning a 0-based equipment slot position (the item Slot member) into a 1-based slot number. Nothing is looked up or checked.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `n` | int | `0` | The 0-based slot position. |

**Returns:** int: n + 1.

```text
echo ${OgreBotAPI.Util.SlotArrayToSlot[0]}
```

*Was (OldBot):* `OgreBotAPI.ConvertSlotArrayToSlot`

### `StripColourCodes`

`${OgreBotAPI.Util.StripColourCodes[s]}`

Removes one colour code from the start of the text (#RRGGBB, or \#RRGGBB in its escaped form) and returns the rest; colour codes later in the text are left alone. With no argument it uses the current zone name, which is empty when you are not in the world.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `s` | string |  | The text to strip. Leave it out to use ${Zone.Name}. |

**Returns:** string: the text without its leading colour code; unchanged when it does not start with one.

```text
echo ${OgreBotAPI.Util.StripColourCodes[${Zone.Name}]}
```

*Was (OldBot):* `OgreBotAPI.RemoveColourCode`

### `StripZoneNumber`

`${OgreBotAPI.Util.StripZoneNumber[s]}`

Returns the text with a leading #RRGGBB colour code, every #00FF00 and /c colour token, and any trailing spaces and digits removed, so "Antonica 2" gives Antonica. With no argument it uses the current zone name, which is empty when you are not in the world.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `s` | string | `${Zone.Name}` | The zone name to clean. Leave it out to use ${Zone.Name}. |

**Returns:** string: the zone name without colour codes or its trailing number.

```text
echo ${OgreBotAPI.Util.StripZoneNumber[${Zone.Name}]}
```

*Was (OldBot):* `GetInfoOb.RemoveZoneNumber`, `OgreBotAPI.RemoveZoneNumber`

### `StripZoneNumberOnly`

`${OgreBotAPI.Util.StripZoneNumberOnly[s]}`

Returns the text with any trailing spaces and digits removed, so "Antonica 2" gives Antonica, and leaves colour codes in place. With no argument it uses the current zone name, which is empty when you are not in the world.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `s` | string | `${Zone.Name}` | The zone name to clean. Leave it out to use ${Zone.Name}. The first character is always kept. |

**Returns:** string: the text without its trailing spaces and digits.

```text
echo ${OgreBotAPI.Util.StripZoneNumberOnly[${Zone.Name}]}
```

*Was (OldBot):* `Obj_OgreUtilities.RemoveZoneNumber`, `OgreBotAPI.RemoveZoneNumberOnly`

### `ToFloat`

`${OgreBotAPI.Util.ToFloat[s]}`

Turns text into a decimal number, dropping commas first; text that does not start with a number gives 0. Quote a value that has commas in it, or the comma splits it into a second argument.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `s` | string |  | The text to read, for example "1,234.5". |

**Returns:** float: the number read from the text; 0 when it does not start with a number.

```text
echo ${OgreBotAPI.Util.ToFloat["1,234.5"]}
```

*Was (OldBot):* `OgreBotAPI.To_Float`

### `ToInt`

`${OgreBotAPI.Util.ToInt[s]}`

Turns text into a whole number, dropping commas first; reading stops at the first character that is not a digit, and text that does not start with a number gives 0. Quote a value that has commas in it, or the comma splits it into a second argument.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `s` | string |  | The text to read, for example "1,234,567". Leading spaces and a + or - sign are allowed. |

**Returns:** int64: the number read from the text; 0 when it does not start with a number.

```text
echo ${OgreBotAPI.Util.ToInt["1,234,567"]}
```

*Was (OldBot):* `OgreBotAPI.To_Int`, `SpellOb.ConvertToInt64`

### `ToNumber`

`${OgreBotAPI.Util.ToNumber[s]}`

Returns the text with every comma and percent sign removed, so "1,234%" comes back as 1234. It does not check that what is left is a number.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `s` | string |  | The text to clean, for example "1,234%". Quote it when it has commas. |

**Returns:** string: the text without commas or percent signs.

```text
echo ${OgreBotAPI.Util.ToNumber["1,234%"]}
```

*Was (OldBot):* `OgreBotAPI.To_Number`

## Methods

### `CheckResearch`

`OgreBotAPI.Util:CheckResearch[fw, forceReport=FALSE]`

Queues a look at the research (Knowledge) window, opening it first when it is not up, and echoes "Research: &lt;name> --> &lt;progress>." to the console. Without forceReport it echoes only when the research reads Complete.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `forceReport` | bool | `FALSE` | TRUE echoes the progress whatever it says; FALSE echoes only when it is Complete. |

```text
OgreBotAPI.Util:CheckResearch[igw:${Me.Name},TRUE]
```

*Was (OldBot):* `OgreBotAPI:CheckResearch`

### `CheckResearchMaterials`

`OgreBotAPI.Util:CheckResearchMaterials[fw]`

Queues a pass over every Advancement, Companion, Mount, Tradeskill, Upgrade and General Research Material in your bags: each is examined and the first choice in the window it opens is picked, or the windows are closed with a console line when it has no eligible research. With none in the bags it echoes that and does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Util:CheckResearchMaterials[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Research_Material_Check`

### `DelayedAction`

`OgreBotAPI.Util:DelayedAction[fw, delay, command...]`

Runs a console command after a delay on each character the for-who picks at the time of the call; the timer is dropped if that character zones before it fires. Give the command as one quoted argument (escape any comma inside it), and note that a bare number for the delay is milliseconds.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `delay` | string |  | How long to wait: a bare whole number is milliseconds, or add a unit - 500ms, 10s, 1.5s, 2m, 1h. Anything else (30x, "30 s", -5) echoes an error and nothing is armed. |
| `command...` | string |  | The command to run, quoted as one argument, for example "eq2execute sit". If it arrives in several pieces they are joined back with commas and a warning is echoed; an empty command echoes an error and nothing is armed. |

```text
OgreBotAPI.Util:DelayedAction[igw:${Me.Name},10s,"eq2execute sit"]
```

### `OnScreenTimer`

`OgreBotAPI.Util:OnScreenTimer[fw, time=30, slot=1, message="Timer:", minUpdate=1]`

Shows a message with a live countdown in one of the ten on-screen timer slots, opening the on-screen display if it is closed; the line is removed 5 seconds after the countdown ends. A slot below 1 uses slot 1 and one above 10 uses slot 10, and a slot that was set less than minUpdate seconds ago silently keeps its old timer.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `time` | float | `30` | Seconds to count down from. Decimals are cut off. |
| `slot` | int | `1` | Which timer line to use, 1 to 10. A number outside is moved to the nearest of them. |
| `message` | string | `"Timer:"` | The text shown before the countdown. Empty uses "Timer:". |
| `minUpdate` | int | `1` | Seconds after this call during which a new timer for the same slot is refused. 0 allows an immediate replacement. |

```text
OgreBotAPI.Util:OnScreenTimer[igw:${Me.Name},45,2,"Adds in:",1]
```

*Was (OldBot):* `OgreBotAPI:OnScreenTimer`

### `OnScreenTimerReset`

`OgreBotAPI.Util:OnScreenTimerReset[fw, slot=1]`

Clears one on-screen timer slot; the line disappears within a second. It does not lift the minUpdate hold of the timer it clears, so a new timer for that slot inside that time is still refused.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `slot` | int | `1` | Which timer line to clear, 1 to 10. A number outside is moved to the nearest of them. |

```text
OgreBotAPI.Util:OnScreenTimerReset[igw:${Me.Name},2]
```

*Was (OldBot):* `OgreBotAPI:OnScreenTimerReset`
