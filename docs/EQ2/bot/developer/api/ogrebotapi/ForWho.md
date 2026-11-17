<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# OgreBotAPI.ForWho

## Members

### `Alias`

`${OgreBotAPI.ForWho.Alias[name]}`

Returns the character name an alias points to right now, or "" when it names nobody present. It reads @me, @Tank, @Healer1 to @Healer3, @DPS1 to @DPS3, @Bard, @Enchanter, @Fighter / @Priest / @Mage / @Scout with an optional rank, @PCTarget, @NPCsTarget, *&lt;your alias> (only while the OgreBot enable-aliases setting is on and you are in the world) and *Team:&lt;group> (its first member present); a plain character name or class word returns "".

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | string |  | the alias to resolve, with its @ or * (any case) |

**Returns:** string: the character name the alias resolves to; "" when it resolves to nobody, is not an alias, or no argument is given.

```text
echo ${OgreBotAPI.ForWho.Alias[@Healer1]}
```

*Was (OldBot):* `OgreBotAPI.Get_Alias`, `GetInfoOb.Alias`

### `AliasesJSON`

`${OgreBotAPI.ForWho.AliasesJSON}`

Returns the loaded OgreBot profile's own alias list as JSON text, one object per row with its starred name, For (what it points to) and, when set, NR (no raid) and a disabled marker. Returns "[]" when no OgreBot profile is loaded or it has no aliases.

**Returns:** string: a JSON array of alias rows; "[]" when there are none or no profile is loaded.

```text
echo ${OgreBotAPI.ForWho.AliasesJSON}
```

*Was (OldBot):* `OgreBotAPI.Get_Aliases_JSON`

### `Me`

`${OgreBotAPI.ForWho.Me[expr]}`

Answers whether a call with this for-who would run on this character - the same test every OgreBotAPI method makes on its first argument. While zoning or at character select it answers from what it already knows: words that need a live read (id:, a bare actor id, eval_num_me:, @PCTarget, @NPCsTarget, *aliases) do not match, and group words use your last settled zone.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `expr` | string |  | a for-who expression, one word with no spaces or commas. \| separates alternatives (any one group matching is enough), + joins words that must all match, and a leading - or ! negates a word. Words, any case: all, auto, @all, @group, @raid (everyone); me, @me; a character name; your InnerSpace session name (is1); an archetype fighter, priest, mage, scout, or healer, melee, caster (plurals too), and not&lt;archetype> such as notfighter; a class or subclass (predator, ranger); an ascension class (geomancer); g1 to g4 (your raid group); groups:&lt;digits> (your raid group number appears in the digits); groupleader; igw:&lt;name> (that character is you or in your group), with irw: also counting the raid, igzw: / irzw: also needing them in your zone, and a bn ending (igwbn:, irzwbn:) leaving yourself out; not:&lt;name>; id:&lt;actor id> or a bare actor id; ToonFlagged:&lt;n>; eval_num_me:&lt;member>&lt;op>&lt;value> with op &lt; &lt;= > >= = or ==; @Tank, @Healer1 to @Healer3, @DPS1 to @DPS3, @Bard, @Enchanter; @Fighter, @Priest, @Mage, @Scout with an optional rank (@Scout2); @PCTarget, @NPCsTarget; *&lt;alias> (your own aliases) and *Team:&lt;group>. A word that is none of these simply does not match. |

**Returns:** int: 1 when the expression selects this character; 0 when it does not, including an empty expression (an empty for-who on a method means all); NULL with no argument.

```text
echo ${OgreBotAPI.ForWho.Me[igw:${Me.Name}+healer]}
```

*Was (OldBot):* `GetInfoOb.CommandForMe`, `GetInfoOb.CommandForMe_Check`, `GetInfoOb.CommandForMe_Eval_Me`

### `Member`

`${OgreBotAPI.ForWho.Member[expr,name]}`

Answers whether a for-who expression selects a given member of your group or raid, using the same words as ForWho.Me with that member in your place. The member must be in your current group or raid; g1 to g4, groups:, groupleader, session names and ascension words never match a member, and eval_num_me: only reads Health, HealthPct, Power and PowerPct.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `expr` | string |  | a for-who expression, the same grammar and words as ForWho.Me |
| `name` | string |  | the group or raid member to test, by character name (any case) |

**Returns:** int: 1 when the expression selects that member; 0 when it does not, when the name is not in your group or raid, or when you are not in the world; NULL with fewer than two arguments.

```text
echo ${OgreBotAPI.ForWho.Member[priest,${Group[1].Name}]}
```

## Methods

### `AddAlias`

`OgreBotAPI.ForWho:AddAlias[fw, alias, value, noRaid=FALSE]`

Adds a row to the loaded OgreBot profile's alias list, so *&lt;alias> names the first character present that value matches: you, a group member by name, a raid member by name, then whoever of you, the group and the raid first fits value as a class word. Several rows may share one name (the first that resolves wins) but an exact repeat is refused with a warning; with no OgreBot profile loaded nothing happens and one console line says so, and the change is kept in memory until the profile is saved.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `alias` | string |  | the alias name; a leading * is added when you leave it off |
| `value` | string |  | what the alias points to: a character name or a class word (archetype, class or subclass) |
| `noRaid` | bool | `FALSE` | TRUE = only you and your group count, raid members are not matched |

```text
OgreBotAPI.ForWho:AddAlias[${Me.Name},MainHealer,${Group[1].Name},TRUE]
```

*Was (OldBot):* `OgreBotAPI:Alias_AddEntry`

### `ChangeAlias`

`OgreBotAPI.ForWho:ChangeAlias[fw, from, to, silent=FALSE]`

Points the first alias row named from at to instead (a blank to clears it, so the alias names nobody), and announces the change in the Ogre console unless silent is TRUE. When no alias of that name exists nothing changes and one console line says so (not when silent); with no OgreBot profile loaded nothing happens and one console line says so.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `from` | string |  | the alias to change (with or without its *) |
| `to` | string |  | the new character name or class word it points to |
| `silent` | bool | `FALSE` | TRUE = make the change without the Ogre console announce |

```text
OgreBotAPI.ForWho:ChangeAlias[${Me.Name},MainHealer,Templar]
```

*Was (OldBot):* `OgreBotAPI:Alias_ChangeEntry`

### `ForceUpdate`

`OgreBotAPI.ForWho:ForceUpdate[fw]`

Drops the cached alias answers, so the next *alias is worked out against the group and raid as they are now. The cache lasts about a second and every alias edit already drops it, so this matters only straight after the group changes.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.ForWho:ForceUpdate[all]
```

*Was (OldBot):* `OgreBotAPI:ForceAliasUpdate`

### `RemoveAlias`

`OgreBotAPI.ForWho:RemoveAlias[fw, name|all]`

Removes the first alias row with that name from the loaded OgreBot profile, or every alias row when the name is all or blank. With no OgreBot profile loaded nothing happens and one console line says so; the change is kept in memory until the profile is saved.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `name\|all` | string |  | the alias to remove (with or without its *), or all to clear the whole list |

```text
OgreBotAPI.ForWho:RemoveAlias[${Me.Name},MainHealer]
```

*Was (OldBot):* `OgreBotAPI:Alias_RemoveEntry`

### `RenameAlias`

`OgreBotAPI.ForWho:RenameAlias[fw, from, to, silent=FALSE]`

Renames the first alias row named from to to (stars added when missing), keeping what it points to, and announces it in the Ogre console unless silent is TRUE. The row keeps its place and its no-raid and disabled settings; a blank name, no alias named from or a to name already taken gets one line and renames nothing, and with no OgreBot profile loaded nothing happens.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `from` | string |  | the alias to rename (with or without its *) |
| `to` | string |  | the new alias name (with or without its *) |
| `silent` | bool | `FALSE` | TRUE = rename without the Ogre console announce |

```text
OgreBotAPI.ForWho:RenameAlias[${Me.Name},MainHealer,BackupHealer]
```

*Was (OldBot):* `OgreBotAPI:Alias_ChangeEntryAlias`
