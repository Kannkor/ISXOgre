# OgreBotAPI.Cures

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Members

### `CurseCalled`

`${OgreBotAPI.Cures.CurseCalled[victim]}`

TRUE while a cure-curse call is open for that character, made by RequestCurse or by Request with kind curse. With no argument it asks about you, and any asks whether a call is open for anyone.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `victim` | character name |  | who to ask about; blank means you; any means anyone |

**Returns:** bool: TRUE while a cure-curse call is open (a call lasts at most 8 seconds); FALSE otherwise, and FALSE out of world when no name is given.

```text
echo ${OgreBotAPI.Cures.CurseCalled[${Group[1].Name}]}
```

*Was (OldBot):* `Obj_CureCurseCalled.CastCureCurse`

### `CursedID`

`${OgreBotAPI.Cures.CursedID[-archetype X...,-uncurable,-uncurableonly,-GroupOnly]}`

The actor ID of the first cursed member found, searching the raid when you are in one and otherwise the group with you first. By default only curable curses count; 0 when nobody matches.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `-archetype X...` | flag + word |  | only members of this archetype: fighter, priest, mage or scout, any case. Repeat the switch to allow more than one archetype. |
| `-uncurable` | flag |  | also accept a member whose curse cannot be cured |
| `-uncurableonly` | flag |  | accept only a member whose curse cannot be cured |
| `-GroupOnly` | flag |  | search your group even when you are in a raid |

**Returns:** int64: the actor ID of the first matching member; 0 when nobody matches.

```text
echo ${OgreBotAPI.Cures.CursedID[-archetype,priest,-uncurable]}
```

*Was (OldBot):* `Obj_CureCurseCalled.GetID_CursedMember`, `Obj_CureCurseCalled.GetID_GroupCursedMember`, `Obj_CureCurseCalled.GetID_RaidCursedMember`

### `Detrimental`

`${OgreBotAPI.Cures.Detrimental[main,back,actorId,field]}`

One field of a detrimental, found by its main and backdrop icon IDs, on you or another actor, as a number. The default field, exists, reads 1 or 0; a detrimental that is not there reads 0.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `main` | int | `0` | the detrimental's main icon ID |
| `back` | int | `0` | the detrimental's backdrop icon ID |
| `actorId` | int64 | `0` | whose effects to look at: 0 or your own ID is you. Any other actor ID reads only that actor's first 10 effects, and there duration and maxduration always read 0. |
| `field` | text | `exists` | exists, iseffectinfoavailable, id, mainiconid, backdropiconid, currentincrements, duration or maxduration, any case. Any other word is read from the effect's examine info, and text such as Name reads 0 here - use DetrimentalText. cancel removes the detrimental from you and reads 0. |

**Returns:** float: the field's value; exists reads 1 or 0; 0 when the detrimental is not found or the field is text.

```text
echo ${OgreBotAPI.Cures.Detrimental[279,315,${Target.ID},exists]}
```

*Was (OldBot):* `GetInfoOb.CurrentIncrements`, `GetInfoOb.CurrentIncrements_ref`, `GetInfoOb.DetrimentalInfo`

### `DetrimentalText`

`${OgreBotAPI.Cures.DetrimentalText[main,back,actorId,field]}`

The same read as Detrimental, returned as text, so examine-info fields such as Name and Description can be read. Reads "" when the detrimental is not found.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `main` | int | `0` | the detrimental's main icon ID |
| `back` | int | `0` | the detrimental's backdrop icon ID |
| `actorId` | int64 | `0` | whose effects to look at: 0 or your own ID is you. Any other actor ID reads only that actor's first 10 effects, and there duration and maxduration always read 0. |
| `field` | text | `exists` | exists (1 or 0), iseffectinfoavailable, id, mainiconid, backdropiconid, currentincrements, duration, maxduration, or an examine-info field such as Name or Description. Examine-info text can be empty on the first read, so wait for iseffectinfoavailable to read 1. cancel removes the detrimental from you and reads "". |

**Returns:** string: the field's value; "" when the detrimental is not found.

```text
echo ${OgreBotAPI.Cures.DetrimentalText[279,315,0,exists]}
```

*Was (OldBot):* `GetInfoOb.DottedDescription_ref`, `GetInfoOb.DottedName_ref`, `OgreBotAPI.DetrimentalInfo_String`

### `GroupCurses`

`${OgreBotAPI.Cures.GroupCurses}`

How many living group members, you included, have a curse that can be cured. Uncurable curses are not counted here - GroupUncurable counts those.

**Returns:** int: the number of living group members with a curable curse; 0 when nobody has one.

```text
echo ${OgreBotAPI.Cures.GroupCurses}
```

*Was (OldBot):* `GetInfoOb.CursesInGroup`, `GroupCureOb.NumOfPCsCursed`, `Obj_CureCurseCalled.GroupCurseCount`

### `GroupUncurable`

`${OgreBotAPI.Cures.GroupUncurable}`

How many group members, you included, carry a curse that cannot be cured. Curable curses are not counted.

**Returns:** int: the number of group members with an uncurable curse; 0 when nobody has one.

```text
echo ${OgreBotAPI.Cures.GroupUncurable}
```

*Was (OldBot):* `OgreBotAPI.Get_GroupUncurableCurseCount`

### `GroupUncurableIDs`

`${OgreBotAPI.Cures.GroupUncurableIDs}`

The actor IDs of the group members, you included, who carry an uncurable curse, as a JSON array sorted lowest first. Reads [] when there are none.

**Returns:** string: a JSON array of actor IDs, for example [1234,5678]; [] when nobody has an uncurable curse.

```text
echo ${OgreBotAPI.Cures.GroupUncurableIDs}
```

*Was (OldBot):* `OgreBotAPI.Get_GroupUncurableCurses_JSON`

### `HaveSickness`

`${OgreBotAPI.Cures.HaveSickness}`

TRUE while you have revive sickness (the detrimental with main icon 279 and backdrop icon 315). FALSE out of world.

**Returns:** bool: TRUE when you have revive sickness; FALSE when you do not or out of world.

```text
echo ${OgreBotAPI.Cures.HaveSickness}
```

*Was (OldBot):* `OgreBotAPI.HaveSickness`

### `PotionAvailable`

`${OgreBotAPI.Cures.PotionAvailable[type]}`

TRUE when you carry a Cure &lt;type> potion that is ready to use. It does not check whether you are afflicted.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `type` | text |  | arcane, elemental, noxious or trauma, matched as part of the item name. Any other word answers FALSE. |

**Returns:** bool: TRUE when a ready potion of that type is in your bags; FALSE when not, when it is still cooling down, when type is not one of the four, or out of world.

```text
echo ${OgreBotAPI.Cures.PotionAvailable[noxious]}
```

### `PotionNeeded`

`${OgreBotAPI.Cures.PotionNeeded}`

The cure type to drink a potion for right now: the first of arcane, elemental, noxious and trauma that is ticked in the cure potion settings, is on you, and has a ready Cure &lt;type> potion in your bags. Reads "" when none qualifies or out of world.

**Returns:** string: arcane, elemental, noxious or trauma; "" when no potion is both needed and ready.

```text
echo ${OgreBotAPI.Cures.PotionNeeded}
```

### `RaidCursedIDs`

`${OgreBotAPI.Cures.RaidCursedIDs}`

The actor IDs of every raid member with a curse, curable or not, as a JSON array sorted lowest first. Out of a raid it lists the group members with a curse, curable or not.

**Returns:** string: a JSON array of actor IDs, for example [1234,5678]; [] when nobody matches or out of world.

```text
echo ${OgreBotAPI.Cures.RaidCursedIDs}
```

*Was (OldBot):* `Obj_CureCurseCalled.ic_CursedToons`, `OgreBotAPI.Get_RaidCurableOrUncurableCurses_JSON`

### `RaidCurses`

`${OgreBotAPI.Cures.RaidCurses}`

How many raid members are alive and have a curse that can be cured. Out of a raid it gives the group count, the same as GroupCurses.

**Returns:** int: the number of living raid members with a curable curse (the group count when not in a raid); 0 when nobody has one.

```text
echo ${OgreBotAPI.Cures.RaidCurses}
```

*Was (OldBot):* `OgreBotAPI.Get_RaidCurseCount`, `OgreBotAPI.NumRaidWithCurses`

### `RaidUncurable`

`${OgreBotAPI.Cures.RaidUncurable}`

How many raid members carry a curse that cannot be cured. Out of a raid it gives the group count, the same as GroupUncurable, and it reads 0 out of world.

**Returns:** int: the number of raid members with an uncurable curse (the group count when not in a raid); 0 when nobody has one or out of world.

```text
echo ${OgreBotAPI.Cures.RaidUncurable}
```

*Was (OldBot):* `OgreBotAPI.Get_RaidUncurableCurseCount`

### `RaidUncurableIDs`

`${OgreBotAPI.Cures.RaidUncurableIDs}`

The actor IDs of the raid members who carry an uncurable curse, as a JSON array sorted lowest first. Out of a raid it lists your group instead; [] when there are none or out of world.

**Returns:** string: a JSON array of actor IDs, for example [1234,5678]; [] when nobody has an uncurable curse or out of world.

```text
echo ${OgreBotAPI.Cures.RaidUncurableIDs}
```

*Was (OldBot):* `OgreBotAPI.Get_RaidUncurableCurses_JSON`

### `Uncurable`

`${OgreBotAPI.Cures.Uncurable[type,-GroupOnly]}`

The actor ID of the first member whose affliction of this type cannot be cured: the raid when you are in one, else the group with you first, else just you. 0 when nobody has one or out of world.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `type` | text | `Cursed` | the affliction to check, as the game names it: Cursed, Arcane, Noxious, Elemental or Trauma. Blank means Cursed. |
| `-GroupOnly` | flag |  | search your group even when you are in a raid |

**Returns:** int64: the actor ID of the first member with an uncurable affliction of that type; 0 when nobody has one or out of world.

```text
echo ${OgreBotAPI.Cures.Uncurable[Cursed,-GroupOnly]}
```

*Was (OldBot):* `OgreBotAPI.Get_Uncurable`

## Methods

### `CancelDetrimental`

`OgreBotAPI.Cures:CancelDetrimental[fw, mainId, backdropId]`

Cancels the detrimental with this main and backdrop icon ID on each matching character. Prints a console line when there is no such detrimental, and does nothing when both IDs are 0.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `mainId` | int |  | the detrimental's main icon ID |
| `backdropId` | int |  | the detrimental's backdrop icon ID |

```text
OgreBotAPI.Cures:CancelDetrimental[igw:${Me.Name},279,315]
```

*Was (OldBot):* `OgreBotAPI:CancelDetrimental`, `GetInfoOb:CancelEffect`, `GetInfoOb:CancelEffect_ref`

### `CancelRequests`

`OgreBotAPI.Cures:CancelRequests[fw, victimOrTag]`

Cancels, on each character the for-who matches, every curse, cure and group-cure request whose victim or -tag is the given name (any letter case). Says how many went when any did.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `victimOrTag` | text |  | the toon the requests were for, or the -tag they were given; a blank one is refused with one console line |

```text
OgreBotAPI.Cures:CancelRequests[igw:${Me.Name},${Group[1].Name}]
```

### `ItemCure`

`OgreBotAPI.Cures:ItemCure[fw, type]`

Drinks a cure potion now on each matching character, if a ready one is in their bags. With a type it drinks that potion whether or not you are afflicted or the type is ticked; with no type, or any, it drinks the one PotionNeeded names.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `type` | text |  | arcane, elemental, noxious or trauma; blank or any drinks whatever the cure potion settings need. Any other word prints a console line and does nothing. |

```text
OgreBotAPI.Cures:ItemCure[igw:${Me.Name},trauma]
```

*Was (OldBot):* `OgreBotAPI:AutoItemCure`

### `ReplenishPotions`

`OgreBotAPI.Cures:ReplenishPotions[fw, all|arcane|elemental|noxious|trauma]`

Tops up cure potions, up to a full stack, from a Poison, Potion, & Totem Depot within 11 meters, on each matching character. A type is restocked only if one of its potions is already in your bags; a blank or unknown type prints a console line and does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `all\|arcane\|elemental\|noxious\|trauma` | word |  | all four cure types, or just one of them, any case |

```text
OgreBotAPI.Cures:ReplenishPotions[igw:${Me.Name},all]
```

*Was (OldBot):* `OgreBotAPI:CurePotions_Replenish`, `OgreBotAPI:Get_CurePotions`

### `Request`

`OgreBotAPI.Cures:Request[fw, victim, kinds...]`

Records a cure request for the victim on each character the for-who matches, and their cure casting serves it. A request lasts 8 seconds unless -AutoRemove says otherwise, and is not sent anywhere else, so use oc !c to reach other characters.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `victim` | character name |  | who to cure; a blank one is refused with one console line |
| `kinds...` | words |  | which cures: arcane (a), noxious (n), elemental (e), trauma (t), curse, confrontfear or sickness, one per argument or comma-separated. None means the four basic kinds (arcane, noxious, elemental, trauma). Then the options -AutoRemove &lt;seconds> (how long the request lasts, 1 to 600, default 8) and -tag &lt;name> (a name Cures:CancelRequests can cancel it by). Any other word refuses the whole request with one console line naming it. confrontfear and sickness are kept only on a dirge. |

```text
OgreBotAPI.Cures:Request[igw:${Me.Name},${Group[1].Name},noxious,trauma,-AutoRemove,20]
```

*Was (OldBot):* `OgreBotAPI:AutoCure`, `Obj_CureCalled:AutoAdd`, `Obj_CurseCalled:AutoAdd`

### `RequestCurse`

`OgreBotAPI.Cures:RequestCurse[fw, victim, options...]`

Records a cure-curse request for the victim on each character the for-who matches, for their cure casting to serve. The request lasts 8 seconds unless -AutoRemove says otherwise, and is not sent anywhere else; a blank victim, or a word it does not know, refuses it with one console line.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `victim` | character name |  | who to cure of the curse; a blank one is refused with one console line |
| `options...` | words |  | -AutoRemove &lt;seconds> (how long the request lasts, 1 to 600, default 8) and -tag &lt;name> (a name Cures:CancelRequests can cancel it by). Any other word refuses the request with one console line naming it. |

```text
OgreBotAPI.Cures:RequestCurse[igw:${Me.Name},${Group[1].Name},-AutoRemove,20]
```

*Was (OldBot):* `OgreBotAPI:AutoCurse`, `OgreBotAPI:Cursed`, `Obj_CureCurseCalled:Add`

### `RequestGroup`

`OgreBotAPI.Cures:RequestGroup[fw]`

Asks each matching character to cast its class group cure within the next 2 seconds, when that ability is ready and someone in the group, you included, has an arcane, noxious, elemental or trauma detrimental. Curses are not group cured.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Cures:RequestGroup[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:GroupCure`

### `RequestGroupWatch`

`OgreBotAPI.Cures:RequestGroupWatch[fw, words...]`

Watches for a group cure on each matching character: the class group cure goes out as soon as it is ready and enough of the group, you included, carry one of the named kinds, each counted on its own (curses are not group cured). The watch lasts 8 seconds unless -AutoRemove says otherwise, and several can run at once.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `words...` | words |  | kinds: arcane (a), noxious (n), elemental (e), trauma (t), one per argument or comma-separated; none means any of the four. Options: -count &lt;n> (at least n of you and the group carry the kind, 1 to 6, default 1), -AutoRemove &lt;seconds> (how long to watch, 1 to 600, default 8), -tag &lt;name> (a name Cures:CancelRequests can cancel it by). Any other word refuses the request with one console line naming it. |

```text
OgreBotAPI.Cures:RequestGroupWatch[igw:${Me.Name},arcane,trauma,-count,3]
```

*Was (OldBot):* `OgreBotAPI:AutoGroupCure`

### `RequestItem`

`OgreBotAPI.Cures:RequestItem[fw, type]`

Queues a potion cure on each matching character, drunk once the cast bar is free; a potion only ever cures the one who drinks it. The request waits up to 8 seconds for a ready potion.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `type` | text |  | arcane, elemental, noxious or trauma. Blank or any picks the needed type when the request is served. Any other word prints a console line and queues nothing. |

```text
OgreBotAPI.Cures:RequestItem[igw:${Me.Name},arcane]
```

### `SetEnabled`

`OgreBotAPI.Cures:SetEnabled[fw, on=TRUE]`

Turns cures on or off on each matching character: the Disable CS_Cure setting and, for a Templar, Warden, Mystic or Monk, that class's cure ability in the Cast Stack. At character select it prints a line and changes nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `on` | bool | `TRUE` | TRUE turns cures on, FALSE turns them off. Off also unticks Enable Auto Cure Potions and cancels the running class ability (Mana Cure, Tranquility, Ancestral Balm or Will of the Heavens). The 'Use these while stunned / stifled / rooted' option is left as you set it. A word that is not yes or no changes nothing. |

```text
OgreBotAPI.Cures:SetEnabled[igw:${Me.Name},FALSE]
```

*Was (OldBot):* `OgreBotAPI:Enable_Cures`, `OgreBotAPI:Disable_Cures`
