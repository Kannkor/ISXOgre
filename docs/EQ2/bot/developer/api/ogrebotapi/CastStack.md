# OgreBotAPI.CastStack

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Members

### `TagAllowRemaining`

`${OgreBotAPI.CastStack.TagAllowRemaining[tag]}`

Seconds left on an allow tag's clock on this session, as a decimal number; 0 when the tag is not held or has run out, and a tag tied to a maintained buff reads the time left on its limit. Tag names are case-insensitive, and reading changes nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `tag` | string |  | The allow tag name, case-insensitive. Blank returns 0. |

**Returns:** float: seconds left before the allow tag ends; 0 when it is absent, expired or blank. A tag tied to a maintained buff reads the time left on its limit, and 0 when it has none (such a tag can still be active).

```text
echo ${OgreBotAPI.CastStack.TagAllowRemaining[Burn]}
```

*Was (OldBot):* `OgreBotAPI.AbilityTag_GetTagAllowTimeRemaining`

### `TagEmbargoRemaining`

`${OgreBotAPI.CastStack.TagEmbargoRemaining[tag]}`

Seconds left on an embargo tag's clock on this session, as a decimal number; 0 when the tag is not held or has run out, and a tag tied to a maintained buff reads the time left on its limit. Tag names are case-insensitive, and reading changes nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `tag` | string |  | The embargo tag name, case-insensitive. Blank returns 0. |

**Returns:** float: seconds left before the embargo tag ends; 0 when it is absent, expired or blank. A tag tied to a maintained buff reads the time left on its limit, and 0 when it has none (such a tag can still be active).

```text
echo ${OgreBotAPI.CastStack.TagEmbargoRemaining[Stuns]}
```

*Was (OldBot):* `OgreBotAPI.AbilityTag_GetTagEmbargoTimeRemaining`

## Methods

### `AddEntry`

`OgreBotAPI.CastStack:AddEntry[fw, name, where, options...]`

Adds a row to the cast stack at the place you name, with any of its options. It takes effect at once, and is kept in the profile only when you Save.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `name` | text |  | The ability's name (or id), or Item:&lt;item name> for an item row. |
| `where` | text |  | top, bottom, or the row number the new row gets (1 to one past the last row). |
| `options...` | key, value pairs |  | Key, value pairs, as many as you like: Type, Target, Named, RD, Tag, ETag, ATag, EType, AType, ID, DT, MAX, IE, IAE, RIE, Conc, disabled, RW&lt;, HP&lt;, HP>, MP&lt;, MP>, N_HP&lt;, N_HP>, Aggro&lt;, Aggro>, Fervor&lt;, Fervor>, D&lt;, D>, Sav, % and #, the same options the Cast Stack window sets; all of them go on or none do, and a refusal prints why. A yes/no option takes TRUE or FALSE (FALSE unticks it). A number option takes a number, and having it at all is the condition. Type is one of the Cast Stack's types (Buff, CA, Heal ...); EType and AType are Both, Trigger Only or Listen Only. Type must be one of them. |

```text
OgreBotAPI.CastStack:AddEntry[${Me.Name},"Item:Eye of the Siren",bottom,Type,Buff,Target,Mailmanx]
```

### `ClearAllAllows`

`OgreBotAPI.CastStack:ClearAllAllows[fw]`

Removes every allow tag, including ones set by cast stack entries, on this session, at once and with or without the console hub, then on every session on this PC in this session's relay group whose for-who matches, sent through the hub and applied on each session's next pulse. Only a session that is itself in the for-who sends it, and nothing is saved.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.CastStack:ClearAllAllows[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:AbilityTag_ResetAllAbilityTagAllows`

### `ClearAllEmbargos`

`OgreBotAPI.CastStack:ClearAllEmbargos[fw]`

Removes every embargo tag, including ones set by cast stack entries, on this session, at once and with or without the console hub, then on every session on this PC in this session's relay group whose for-who matches, sent through the hub and applied on each session's next pulse. Only a session that is itself in the for-who sends it, and nothing is saved.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.CastStack:ClearAllEmbargos[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:AbilityTag_ResetAllAbilityTagEmbargos`

### `ClearAllow`

`OgreBotAPI.CastStack:ClearAllow[fw, tag]`

Removes one allow tag on this session, at once and with or without the console hub, then on every session on this PC in this session's relay group whose for-who matches, sent through the hub and applied on each session's next pulse. Only a session that is itself in the for-who sends it, a blank tag gets one line, and nothing is saved.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `tag` | string |  | The allow tag to remove, case-insensitive. A blank gets one line - use ClearAllAllows to remove them all. |

```text
OgreBotAPI.CastStack:ClearAllow[igw:${Me.Name},Burn]
```

*Was (OldBot):* `OgreBotAPI:AbilityTag_ResetAbilityTagAllow`

### `ClearEmbargo`

`OgreBotAPI.CastStack:ClearEmbargo[fw, tag]`

Removes one embargo tag on this session, at once and with or without the console hub, then on every session on this PC in this session's relay group whose for-who matches, sent through the hub and applied on each session's next pulse. Only a session that is itself in the for-who sends it, a blank tag gets one line, and nothing is saved.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `tag` | string |  | The embargo tag to remove, case-insensitive. A blank gets one line - use ClearAllEmbargos to remove them all. |

```text
OgreBotAPI.CastStack:ClearEmbargo[igw:${Me.Name},Stuns]
```

*Was (OldBot):* `OgreBotAPI:AbilityTag_ResetAbilityTagEmbargo`

### `ClearEntryOption`

`OgreBotAPI.CastStack:ClearEntryOption[fw, row, keys...]`

Removes options from a cast stack row, as blanking a field or unticking a box in the window does. It takes effect at once, and is kept in the profile only when you Save.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `row` | number or text |  | The row: its number as the Cast Stack shows it (1 is the top row), or its name when exactly one row has that name (case-insensitive). An item row's name is Item:&lt;item name>. |
| `keys...` | option names |  | The options to remove, by the same names SetEntryOption takes. One the row does not have is fine; an unknown name removes nothing and prints why. |

```text
OgreBotAPI.CastStack:ClearEntryOption[${Me.Name},"Battle Tactics",HP<,RD]
```

### `ClearItemCache`

`OgreBotAPI.CastStack:ClearItemCache[fw]`

Empties the shared item effect file on disk at once, for every character on this PC, and prints a line to the console. This session then re-examines its item entries from the next pulse, including ones that failed earlier.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.CastStack:ClearItemCache[${Me.Name}]
```

### `Dump`

`OgreBotAPI.CastStack:Dump[fw]`

On the next pulse, checks every cast stack entry against the current game state, prints one line per entry with its verdict to the console, and sends the same list to the OgreBot window. It casts nothing and changes nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.CastStack:Dump[${Me.Name}]
```

### `ExamineItems`

`OgreBotAPI.CastStack:ExamineItems[fw]`

From the next pulse, examines the cast stack's item entries that are not in the shared item effect file yet, and rebuilds the list of adornments on your equipped gear. What it learns is written to the shared item effect file, which every character on this PC reads.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.CastStack:ExamineItems[${Me.Name}]
```

### `HoldTag`

`OgreBotAPI.CastStack:HoldTag[fw, tag, duration, type, -m]`

Sets an embargo or allow tag for some seconds on this session, at once and with or without the console hub, then sends it through the hub to every session on this PC in this session's relay group whose for-who matches, applied on each session's next pulse, for that session only. Only a session that is itself in the for-who sends it, so run it on every session (oc !c) or from one inside the for-who, and the tag only blocks or allows entries while Enable Tag Embargo or Enable Tag Allow is ticked.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `tag` | string |  | The tag name, case-insensitive. A blank gets one line. |
| `duration` | int |  | How long the tag lasts, in seconds. 0, blank or not a number ends it at once. A new hold never shortens a tag that is already running longer. |
| `type` | string |  | Allow sets an allow tag. Any other word, blank included, sets an embargo tag. |
| `-m` | switch |  | Optional: -m followed by a maintained buff name or ability id ties this session's hold to its own buff: the hold ends when the buff drops, or at the duration if that comes first, after a grace of the cast time plus 1 second (5 seconds for an item). Other sessions hold plain until this one tells them to let go. |

```text
OgreBotAPI.CastStack:HoldTag[igw:${Me.Name},Stuns,13,Embargo]
```

*Was (OldBot):* `OgreBotAPI:AbilityTag_AddRotateTagTimer`

### `Import`

`OgreBotAPI.CastStack:Import[fw, path, profile=""]`

Replaces this session's cast stack with the cast stack from an OgreBot EQ2Save XML file, and prints the entry count and any notes, or why it failed, to the console. It takes effect at once and lasts only until the profile is next opened, reloaded or edited.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `path` | string |  | Full path of the EQ2Save XML file. A relative path is read from the game's working folder, not from Scripts. |
| `profile` | string | `""` | The profile inside the file whose cast stack to take. Blank takes the first profile that has a cast stack. |

```text
OgreBotAPI.CastStack:Import[${Me.Name},"${LavishScript.HomeDirectory}/Scripts/MyCastStack.xml",Raid]
```

### `Load`

`OgreBotAPI.CastStack:Load[fw, path]`

Replaces this session's cast stack with the entries in a JSON cast stack file, and prints the entry count, or why it failed, to the console. It takes effect at once and lasts only until the profile is next opened, reloaded or edited - the profile and the OgreBot window are not changed.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `path` | string |  | Full path of the JSON file, which must hold an "entries" array. A relative path is read from the game's working folder, not from Scripts. An ability entry may give its name alone: names are looked up in this toon's ability export, as a profile load does. |

```text
OgreBotAPI.CastStack:Load[${Me.Name},"${LavishScript.HomeDirectory}/Scripts/MyCastStack.json"]
```

### `LoadFromProfile`

`OgreBotAPI.CastStack:LoadFromProfile[fw]`

Reloads this session's cast stack from the OgreBot profile already open, including edits not saved yet, matches each ability name to your ability export, and re-examines item entries from the next pulse. Nothing is read from disk or saved, and with no profile open the stack is left empty.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.CastStack:LoadFromProfile[${Me.Name}]
```

### `MoveEntry`

`OgreBotAPI.CastStack:MoveEntry[fw, row, to]`

Moves a cast stack row up or down one place, to the top or bottom, or to a row number. It takes effect at once, and is kept in the profile only when you Save.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `row` | number or text |  | The row: its number as the Cast Stack shows it (1 is the top row), or its name when exactly one row has that name (case-insensitive). An item row's name is Item:&lt;item name>. |
| `to` | text |  | up, down, top, bottom, or the row number it moves to. |

```text
OgreBotAPI.CastStack:MoveEntry[${Me.Name},"Item:Eye of the Siren",top]
```

### `ReloadRangeExtenders`

`OgreBotAPI.CastStack:ReloadRangeExtenders[fw]`

Re-reads the per-zone range extender file, Ogre/EQ2/Encounters/RangeExtenders.json (it comes with the bot), at once and prints how many zones and entries it loaded, or a warning. The file lists, per zone, detrimental effects that change your ability range; nothing is saved.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.CastStack:ReloadRangeExtenders[${Me.Name}]
```

### `RemoveEntry`

`OgreBotAPI.CastStack:RemoveEntry[fw, row]`

Removes a row from the cast stack. It takes effect at once, and is kept in the profile only when you Save.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `row` | number or text |  | The row: its number as the Cast Stack shows it (1 is the top row), or its name when exactly one row has that name (case-insensitive). An item row's name is Item:&lt;item name>. |

```text
OgreBotAPI.CastStack:RemoveEntry[${Me.Name},5]
```

### `SetEntry`

`OgreBotAPI.CastStack:SetEntry[fw, ability, TRUE|FALSE|toggle, silent=FALSE]`

Enables, disables or flips the cast stack entries that match the name, and prints a line to OgreConsole for each entry that actually changed unless silent is TRUE. It takes effect at once in the rotation and the OgreBot window, and is kept in the profile only when you Save.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `ability` | string |  | The entry: its whole name (case-insensitive), an ability id (finds the entry that holds that ability), or one of IsStun, IsInterrupt, IsDaze, IsFear, IsStifle or Ascension to match every entry of that kind. Blank does nothing. |
| `TRUE\|FALSE\|toggle` | string |  | TRUE enables (1, yes and on count as TRUE too). toggle, or blank, flips each matching entry. Any other word disables. |
| `silent` | bool | `FALSE` | TRUE skips the OgreConsole lines. |

```text
OgreBotAPI.CastStack:SetEntry[igw:${Me.Name},Assault,FALSE]
```

*Was (OldBot):* `OgreBotAPI:ChangeCastStackListBoxItem`, `ChangeCastStackListBoxItem`

### `SetEntryByTag`

`OgreBotAPI.CastStack:SetEntryByTag[fw, tag, TRUE|FALSE|toggle, partial=FALSE, silent=FALSE]`

Enables, disables or flips the cast stack entries whose tag matches, and prints a line to OgreConsole for each entry that actually changed unless silent is TRUE. It takes effect at once in the rotation and the OgreBot window, and is kept in the profile only when you Save.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `tag` | string |  | The entry tag to match, case-insensitive. This is the entry's own tag, not an embargo or allow tag. Blank does nothing. |
| `TRUE\|FALSE\|toggle` | string |  | TRUE enables (1, yes and on count as TRUE too). toggle, or blank, flips each matching entry. Any other word disables. |
| `partial` | bool | `FALSE` | TRUE matches every entry whose tag contains the word; FALSE needs the whole tag. |
| `silent` | bool | `FALSE` | TRUE skips the OgreConsole lines. |

```text
OgreBotAPI.CastStack:SetEntryByTag[igw:${Me.Name},AE,toggle,TRUE]
```

*Was (OldBot):* `OgreBotAPI:ChangeCastStackListBoxItemByTag`, `ChangeCastStackListBoxItemByTag`

### `SetEntryOption`

`OgreBotAPI.CastStack:SetEntryOption[fw, row, options...]`

Sets one or more options on a cast stack row. It takes effect at once, and is kept in the profile only when you Save.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `row` | number or text |  | The row: its number as the Cast Stack shows it (1 is the top row), or its name when exactly one row has that name (case-insensitive). An item row's name is Item:&lt;item name>. |
| `options...` | key, value pairs |  | Key, value pairs, as many as you like: Type, Target, Named, RD, Tag, ETag, ATag, EType, AType, ID, DT, MAX, IE, IAE, RIE, Conc, disabled, RW&lt;, HP&lt;, HP>, MP&lt;, MP>, N_HP&lt;, N_HP>, Aggro&lt;, Aggro>, Fervor&lt;, Fervor>, D&lt;, D>, Sav, % and #, the same options the Cast Stack window sets; all of them go on or none do, and a refusal prints why. A yes/no option takes TRUE or FALSE (FALSE unticks it). A number option takes a number, and having it at all is the condition. Type is one of the Cast Stack's types (Buff, CA, Heal ...); EType and AType are Both, Trigger Only or Listen Only. |

```text
OgreBotAPI.CastStack:SetEntryOption[${Me.Name},3,HP<,50,Named,TRUE]
```

### `TestCast`

`OgreBotAPI.CastStack:TestCast[fw, ability=""]`

Arms one real cast for the next pulse and then stops: the given ability, or with no ability the first entry the cast stack would cast right now; a name this toon's export does not know gets one line and arms nothing. It fires even while the bot is paused, but needs OgreBot loaded and is ignored while a cast is already in flight.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `ability` | string | `""` | The ability to cast: a name (short or any rank) or an ability id. It is cast with no target, and skipped with a console line if it is not ready. Blank casts the first eligible cast stack entry instead; a name that cannot be found gets one line and casts nothing. |

```text
OgreBotAPI.CastStack:TestCast[${Me.Name},Assault]
```

### `Tick`

`OgreBotAPI.CastStack:Tick[fw]`

Runs one evaluation of the cast stack straight away and casts nothing, even while the bot is paused. It prints only when the Debug tab's cast stack eval or casting boxes are ticked, and it changes and saves nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.CastStack:Tick[${Me.Name}]
```
