<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# OgreBotAPI.Abilities

## Members

### `CanCastOn`

`${OgreBotAPI.Abilities.CanCastOn[ability,target]}`

Tells you whether you could cast an ability on a target right now, and if not, why. It runs the bot's own castability check (range measured edge to edge, power, cooldown, position, stealth, line of sight, target type), so a script never has to rebuild it.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `ability` | ability name or id |  | the ability to check |
| `target` | actor name or id |  | who to cast it on; blank = yourself |

**Returns:** string: "eligible" when it can be cast now. Otherwise the reason: "no ability given", "unresolved" (ability not found), "no valid target" (also when not in the world), "no target", "target gone", "cannot target self", "wrong target type", "target type unreadable", "ability not known", "on cooldown", "just cast this line", "not enough power", "not flanking", "not behind", "position unreadable", "requires stealth", "moving", "distance unreadable", "out of range", "line of sight unknown" or "line of sight blocked".

```text
echo ${OgreBotAPI.Abilities.CanCastOn["Intercept",${Target.ID}]}
```

### `CancelCurrentCast`

`${OgreBotAPI.Abilities.CancelCurrentCast}`

Reads the cancel-current-cast flag that :SetCancelCurrentCast raises. It stays TRUE until the next cast starts or ends, then clears itself.

**Returns:** bool: TRUE while a cancel of the current cast is pending, FALSE otherwise.

```text
echo ${OgreBotAPI.Abilities.CancelCurrentCast}
```

### `Count`

`${OgreBotAPI.Abilities.Count}`

The number of usable abilities in the loaded export: one per ability line, the highest rank your level allows.

**Returns:** int: the number of usable abilities, one per line. 0 when no export is loaded.

```text
echo ${OgreBotAPI.Abilities.Count}
```

### `FindCastableHOIconAbilityID`

`${OgreBotAPI.Abilities.FindCastableHOIconAbilityID[iconId,options...]}`

Finds an ability you own that matches a heroic opportunity icon and can be cast now, and gives its id without casting it. Your "no stuns"-style settings are honoured; -offensive keeps only hostile abilities, and -ActorID &lt;id> (or -HOTarget &lt;id>) checks against that actor instead of your current NPC target.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `iconId` | number | `0` | the heroic opportunity icon id |
| `options...` | text |  | -offensive, -ActorID &lt;id> or -HOTarget &lt;id>, and the -No options, each on top of your settings boxes: -NoStun, -NoDaze, -NoFear, -NoStifle, -NoInterrupt, -NoDispel, -NoRoot, -NoSnare, -NoCures, -NoGroupCures, -NoForceTargets, -NoThreatIncreases, -NoThreatDecreases. The console names any other option once, and it is ignored. |

**Returns:** int64: the id of the ability to cast. 0 when nothing you own matches the icon or can be cast now.

```text
echo ${OgreBotAPI.Abilities.FindCastableHOIconAbilityID[3,-offensive]}
```

*Was (OldBot):* `OgreBotAPI.Get_HOIconAbility`

### `FindCastableID`

`${OgreBotAPI.Abilities.FindCastableID[query...]}`

Picks an ability that is ready now by its properties instead of its name and gives its id without casting it; all terms have to match. Your "no stuns"-style settings still rule abilities out, except for the property you searched on, and a bad query is reported in the console.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `query...` | text |  | query terms, each member, comparison, value (such as "IsInterrupt","=","TRUE"), plus options such as -NPCRequired or -ActorID &lt;id> that check against a target |

**Returns:** int64: the id of the matching ability (fastest cast time wins). 0 when nothing matches, when the query is refused, or when no export is loaded.

```text
echo ${OgreBotAPI.Abilities.FindCastableID["IsInterrupt","=","TRUE","-NPCRequired"]}
```

*Was (OldBot):* `OgreBotAPI.Get_AbilityTypeID`, `OgreBotAPI.Get_AbilityTypeID_Ref`, `OgreBotAPI.Get_AbilityVia`

### `FindCastableInterruptID`

`${OgreBotAPI.Abilities.FindCastableInterruptID[actor]}`

Picks the interrupt you would use right now (an interrupt that is not beneficial, ready, and usable on the target; fastest cast time wins) and gives its id without casting it. With no actor it checks against your current NPC target; a bad query is reported in the console.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `actor` | actor name or id |  | who to interrupt; blank = current NPC target |

**Returns:** int64: the id of the interrupt to cast. 0 when you have none usable right now.

```text
echo ${OgreBotAPI.Abilities.FindCastableInterruptID}
```

*Was (OldBot):* `OgreBotAPI.Get_InterruptID`

### `HaveMaintained`

`${OgreBotAPI.Abilities.HaveMaintained[name...]}`

Checks your maintained window for any of the names you give; names match partially and ignore case by default. An ability id is turned into the full name of the rank you hold.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name...` | ability name or id |  | maintained names or ability ids to look for; put -exact (or TRUE) before names that must match exactly and -partial (or FALSE) to switch back |

**Returns:** bool: TRUE when any of the names is in your maintained window, FALSE when none is.

```text
echo ${OgreBotAPI.Abilities.HaveMaintained[-exact,"Sprint"]}
```

*Was (OldBot):* `OgreBotAPI.HaveMaintained`

### `ID`

`${OgreBotAPI.Abilities.ID[name]}`

Looks an ability up in your loaded export and gives its id. A short name ("Assault"), any rank's full name ("Assault X") or any rank's id all give the best rank you can use now; name matching ignores case.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | ability name or id |  | the ability to look up |

**Returns:** int64: the id of the best usable rank. A number that is not in your export comes back unchanged. 0 when the name matches nothing or no export is loaded.

```text
echo ${OgreBotAPI.Abilities.ID["Sprint"]}
```

*Was (OldBot):* `Abilities.Ability`, `Abilities.GetIndexBy`, `Abilities.GetIndexByID`

### `Info`

`${OgreBotAPI.Abilities.Info[nameOrId, field]}`

Reads one field of an ability from your loaded export, for the best rank you can use. Flags the export leaves out (false flags are omitted) read as empty, not FALSE.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `nameOrId` | ability name or id |  | the ability to read |
| `field` | text |  | export field name, e.g. Name or CastingTime |

**Returns:** string: the field's value as text (TRUE/FALSE for flags). Empty when the ability or the field is not found, or no export is loaded.

```text
echo ${OgreBotAPI.Abilities.Info["Sprint",CastingTime]}
```

*Was (OldBot):* `OgreBotAPI.Get_AbilityInfo`, `SpellOb.AllowRaid`, `SpellOb.CastingTime`

### `InfoRaw`

`${OgreBotAPI.Abilities.InfoRaw[nameOrId]}`

Gives the whole export record of an ability (best rank you can use) as JSON, for reading several fields at once with jsonvalue.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `nameOrId` | ability name or id |  | the ability to read |

**Returns:** string: the record as a JSON object. {} when the ability is not found or no export is loaded.

```text
echo ${OgreBotAPI.Abilities.InfoRaw["Assault"]}
```

*Was (OldBot):* `OgreBotAPI.Get_AbilityInfo_RawData`

### `Loaded`

`${OgreBotAPI.Abilities.Loaded}`

Tells you whether an ability export is loaded for this character. Name lookups (casting by name, Info, ShortName and the rest) need a loaded export.

**Returns:** bool: TRUE when an ability export is loaded, FALSE when none is.

```text
echo ${OgreBotAPI.Abilities.Loaded}
```

### `RawCount`

`${OgreBotAPI.Abilities.RawCount}`

The number of entries in the loaded export before it is reduced to one rank per line, so every rank of every ability counts.

**Returns:** int: the total number of entries in the export file. 0 when no export is loaded.

```text
echo ${OgreBotAPI.Abilities.RawCount}
```

### `Ready`

`${OgreBotAPI.Abilities.Ready[fw,ability,actor]}`

Asks whether an ability is ready. Without an actor it checks only that the ability is off cooldown; with an actor it runs the full can-I-cast-this-on-them check (range, power, position, line of sight, target type), the same check as CanCastOn.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `ability` | ability name or id |  | the ability to check |
| `actor` | actor name or id |  | who you would cast it on; blank = cooldown only |

**Returns:** bool: TRUE when the ability is ready (and castable on the actor, if one is given). FALSE when it is not, when the ability or actor cannot be found, when you are not in the world, or when the for-who does not include this character.

```text
echo ${OgreBotAPI.Abilities.Ready[all,"Assault"]}
```

*Was (OldBot):* `OgreBotAPI.AbilityReady`

### `ScrollMaintainedDuration`

`${OgreBotAPI.Abilities.ScrollMaintainedDuration[name]}`

Gives the time left on the first maintained effect whose name ends with the text you give (case ignored). With no text it looks for Painlink.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | text | `Painlink` | end of the maintained effect's name |

**Returns:** int: seconds remaining on that maintained effect. -1 when none matches.

```text
echo ${OgreBotAPI.Abilities.ScrollMaintainedDuration[Painlink]}
```

*Was (OldBot):* `OgreBotAPI.ScrollOf_Get_MaintainedDuration`

### `ShortName`

`${OgreBotAPI.Abilities.ShortName[nameOrId]}`

Gives the line name of an ability, without its rank: "Assault X" or an Assault id gives "Assault". Reads your loaded export.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `nameOrId` | ability name or id |  | the ability to name |

**Returns:** string: the ability line name. Empty when the ability is not found or no export is loaded.

```text
echo ${OgreBotAPI.Abilities.ShortName["Sprint"]}
```

*Was (OldBot):* `OgreBotAPI.Get_AbilityShortName`, `SpellOb.AbilityName`, `SpellOb.GetAbilityShortName`

## Methods

### `AbilityDetails`

`OgreBotAPI.Abilities:AbilityDetails[fw, name or id]`

Opens the Ability Details window, which shows what your export holds for an ability, and selects the one you name. It also opens at character select.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `name or id` | ability name or id |  | the ability to select; blank selects nothing |

```text
OgreBotAPI.Abilities:AbilityDetails[${Me.Name},"Assault"]
```

*Was (OldBot):* `OgreBotAPI:SpewAbility`

### `AddEmbargo`

`OgreBotAPI.Abilities:AddEmbargo[fw, id, durationSec]`

Embargoes an ability: the cast stack skips it for that many seconds while the Enable Ability Embargo setting is ticked. Both the ability and the duration are required (an error is printed otherwise); 0 seconds expires at once.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `id` | ability name or id |  | the ability to embargo |
| `durationSec` | number |  | embargo length in seconds |

```text
OgreBotAPI.Abilities:AddEmbargo[all,"Assault",30]
```

*Was (OldBot):* `OgreBotAPI:AbilityEmbargo_AddRotateTimer`

### `AnnounceCasted`

`OgreBotAPI.Abilities:AnnounceCasted[fw, caster, seconds]`

Tells the bot sessions that a caster has put up a cast-while-moving effect: every session (this one too) in the caster's group lets its rotation cast while moving for that many seconds. A blank caster, or seconds that are missing, 0 or less, or not a number, is refused with a console line and nothing is sent.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `caster` | player name |  | who cast the effect (required) |
| `seconds` | number |  | how long the effect lasts, more than 0 (required) |

```text
OgreBotAPI.Abilities:AnnounceCasted[all,${Me.Name},30]
```

*Was (OldBot):* `OgreBotAPI:CastedCastOnTheMove`

### `AnnounceCasting`

`OgreBotAPI.Abilities:AnnounceCasting[fw, seconds]`

Like AnnounceCasted with you as the caster: every session in your group (this one too) lets its rotation cast while moving for that many seconds. Seconds that are missing, 0 or less, or not a number are refused with a console line and nothing is sent.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `seconds` | number |  | how long the effect lasts, more than 0 (required) |

```text
OgreBotAPI.Abilities:AnnounceCasting[${Me.Name},30]
```

*Was (OldBot):* `OgreBotAPI:CastingCastOnTheMove`

### `CancelCasting`

`OgreBotAPI.Abilities:CancelCasting[fw, except..., -HOAbility, -HOAbilityUI, -CastTime s, -CastAbility ability, -CastAbilityOnPlayer ability player, -CastHOAbilityIconID iconId, -CastAbilityOnNPC ability mob, -UnlessCasting ability]`

Cancels the spell you are casting, unless it is one of the abilities you name (any rank) or a guard option says to keep it. -CastAbility, -CastAbilityOnPlayer, -CastAbilityOnNPC and -CastHOAbilityIconID queue that cast first; any other -option cancels nothing (a warning is printed once).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `except...` | ability name or id |  | abilities never to cancel |
| `-HOAbility` | flag |  | cancel only an ability that has a heroic opportunity icon |
| `-HOAbilityUI` | flag |  | cancel a heroic opportunity ability only when your settings disable it |
| `-CastTime s` | flag + number |  | cancel only when at least s seconds of the cast remain |
| `-CastAbility ability` | flag + ability name or id |  | queue this ability first, then cancel |
| `-CastAbilityOnPlayer ability player` | flag + ability + player |  | queue this ability on that player first, then cancel |
| `-CastHOAbilityIconID iconId` | flag + number |  | queue the ability with this heroic opportunity icon id first, then cancel |
| `-CastAbilityOnNPC ability mob` | flag + ability + mob name or id |  | queue this ability on that mob first, then cancel |
| `-UnlessCasting ability` | flag + ability name or id |  | the same as naming the ability plainly: never cancel it |

```text
OgreBotAPI.Abilities:CancelCasting[all,-CastTime,0.5,-HOAbilityUI]
```

*Was (OldBot):* `OgreBotAPI:CancelCasting`

### `CancelGroupWaterBreathing`

`OgreBotAPI.Abilities:CancelGroupWaterBreathing[fw]`

Cancels your class's group water-breathing maintained buff. Skipped (noted in the log) when your class has none.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Abilities:CancelGroupWaterBreathing[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:CancelGroupWaterBreathing`, `Obj_OgreIH:CancelGroupWaterBreathing`

### `CancelInvis`

`OgreBotAPI.Abilities:CancelInvis[fw]`

Breaks invisibility: if you are invisible and Transmute is ready, it casts Transmute and presses Esc half a second later to close its window. Does nothing when you are not invisible or Transmute is not ready.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Abilities:CancelInvis[igw:${Me.Name}]
```

*Was (OldBot):* `call OgreBotAPI.CancelInvis`

### `CancelMaintained`

`OgreBotAPI.Abilities:CancelMaintained[ability...]`

Cancels each maintained ability you list on this character. It takes no for-who: every argument is an ability name or id, and a short name cancels whichever rank is up.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `ability...` | ability name or id |  | maintained abilities to cancel |

```text
OgreBotAPI.Abilities:CancelMaintained["Sprint"]
```

*Was (OldBot):* `OgreBotAPI:CancelMaintained`

### `CancelMaintainedFor`

`OgreBotAPI.Abilities:CancelMaintainedFor[fw, ability...]`

Cancels each maintained ability you list, on the characters the for-who names. A short name cancels whichever rank is up.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `ability...` | ability name or id |  | maintained abilities to cancel |

```text
OgreBotAPI.Abilities:CancelMaintainedFor[igw:${Me.Name},"Sprint"]
```

*Was (OldBot):* `OgreBotAPI:CancelMaintainedForWho`

### `CancelOnCast`

`OgreBotAPI.Abilities:CancelOnCast[fw, abilityName]`

Runs your Cancel On Cast list as if you had just cast this ability: any row that ability triggers cancels its maintained buff, held until combat ends when the row says so.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `abilityName` | ability name or id |  | the ability to treat as just cast |

```text
OgreBotAPI.Abilities:CancelOnCast[${Me.Name},"Assault"]
```

### `Cast`

`OgreBotAPI.Abilities:Cast[fw, ability, calledFrom=OgreBotAPI]`

Queues a cast of an ability at your current target; it is asynchronous and goes off when the cast bar is free. Nothing is queued when the ability cannot be found or is not ready.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `ability` | ability name or id |  | the ability to cast |
| `calledFrom` | text | `OgreBotAPI` | label shown in the cast debug log |

```text
OgreBotAPI.Abilities:Cast[${Me.Name},"Sprint"]
```

*Was (OldBot):* `OgreBotAPI:CastAbility`, `call Obj_OgreUtilities.CastAbilityID`

### `CastBulwark`

`OgreBotAPI.Abilities:CastBulwark[fw]`

Casts Bulwark of Order right now: queues it ahead of the rotation, cancels any other cast in progress, and tries again a second later if it has not gone off. If the ability is missing from your export or not ready, it broadcasts a notice (at most every 30 seconds) and does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Abilities:CastBulwark[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:CastBulwarkImmediately`

### `CastGroupWaterBreathing`

`OgreBotAPI.Abilities:CastGroupWaterBreathing[fw]`

Casts your class's group water-breathing ability through :Cast. Skipped (noted in the log) when your class has none or your export does not have it.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Abilities:CastGroupWaterBreathing[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:CastGroupWaterBreathing`, `Obj_OgreIH:CastGroupWaterBreathing`

### `CastHOIcon`

`OgreBotAPI.Abilities:CastHOIcon[fw, iconId, calledFrom=CastHOIcon]`

Casts an ability you own that matches a heroic opportunity icon and can be cast now (the same pick as FindCastableHOIconAbilityID), through :Cast. No icon id is refused with a console line; -2, or an icon no ready ability matches, does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `iconId` | number |  | the heroic opportunity icon id (required); -2 casts nothing |
| `calledFrom` | text | `CastHOIcon` | label for the cast log |

```text
OgreBotAPI.Abilities:CastHOIcon[${Me.Name},5]
```

*Was (OldBot):* `OgreBotAPI:CastHOIconID`

### `CastInSeconds`

`OgreBotAPI.Abilities:CastInSeconds[fw, ability, delay, calledFrom=OgreBotAPI]`

Casts an ability after a delay by running :Cast when the time is up, so the ready check happens then. A bare number is seconds; "500ms" or "2m" style values are also accepted, and a bad delay is reported in the console.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `ability` | ability name or id |  | the ability to cast |
| `delay` | number or duration |  | how long to wait; bare number = seconds |
| `calledFrom` | text | `OgreBotAPI` | label for the cast log |

```text
OgreBotAPI.Abilities:CastInSeconds[${Me.Name},"Sprint",5]
```

*Was (OldBot):* `OgreBotAPI:CastAbilityInSeconds`

### `CastInterrupt`

`OgreBotAPI.Abilities:CastInterrupt[fw, mobNameOrId="", calledFrom=Cast_Interrupt]`

Casts an interrupt at a mob: it picks a non-beneficial interrupt usable on that mob right now and, unless you are already casting an interrupt, cancels your current cast first. With no mob it uses your current NPC target (a name must match exactly); the console says when there is no mob or no interrupt available.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `mobNameOrId` | actor name or id | `""` | the mob to interrupt; blank = current NPC target |
| `calledFrom` | text | `Cast_Interrupt` | label for the cast log |

```text
OgreBotAPI.Abilities:CastInterrupt[igw:${Me.Name},${Target.ID}]
```

*Was (OldBot):* `OgreBotAPI:Cast_Interrupt`

### `CastNoChecks`

`OgreBotAPI.Abilities:CastNoChecks[fw, ability, calledFrom=OgreBotAPI]`

Queues a cast of an ability at your current target without checking first that it is ready. The cast is still dropped if the ability is not ready by the time it reaches the cast bar.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `ability` | ability name or id |  | the ability to cast |
| `calledFrom` | text | `OgreBotAPI` | label for the cast log |

```text
OgreBotAPI.Abilities:CastNoChecks[${Me.Name},"Sprint",MyScript]
```

*Was (OldBot):* `OgreBotAPI:CastAbilityNoChecks`

### `CastNoExport`

`OgreBotAPI.Abilities:CastNoExport[fw, ability, calledFrom=CastAbilityNoExport]`

Queues a cast of an ability at your current target, like :Cast, but checks only that you have the ability and it is off cooldown. Asynchronous: it goes off when the cast bar is free.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `ability` | ability name or id |  | the ability to cast |
| `calledFrom` | text | `CastAbilityNoExport` | label for the cast log |

```text
OgreBotAPI.Abilities:CastNoExport[${Me.Name},${OgreBotAPI.Abilities.ID["Sprint"]}]
```

*Was (OldBot):* `OgreBotAPI:CastAbilityNoExport`

### `CastOnNPC`

`OgreBotAPI.Abilities:CastOnNPC[fw, ability, mob=target]`

Targets a mob, waits until it is your target, casts the ability at it and puts your target back. Nothing is cast if the mob is not given or cannot be found, you are dead, or the ability is not ready.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `ability` | ability name or id |  | the ability to cast |
| `mob` | actor name or id |  | the mob to cast on, by name or id; required |

```text
OgreBotAPI.Abilities:CastOnNPC[${Me.Name},"Assault",${Target.ID}]
```

*Was (OldBot):* `OgreBotAPI:CastAbilityOnNPC`

### `CastOnPlayer`

`OgreBotAPI.Abilities:CastOnPlayer[fw, ability, player=me, calledFrom=AbilityExportCastFromUplinkOnPlayer]`

Queues a cast of an ability on a named player without changing your target, after checking that it can be cast on them (ready, power, range, line of sight and the rest - the same check as CanCastOn); when it cannot, nothing is cast and the reason goes to the log file. The player can be a name or a role alias such as @Healer1, defaults to you, and must be you or in your group or raid; calledFrom is the label shown in the cast debug log.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `ability` | ability name or id |  | the ability to cast |
| `player` | player name or alias | `me` | who to cast it on |
| `calledFrom` | text | `AbilityExportCastFromUplinkOnPlayer` | label for the cast log |

```text
OgreBotAPI.Abilities:CastOnPlayer[igw:${Me.Name},"Intercept",${Target.Name}]
```

*Was (OldBot):* `OgreBotAPI:CastAbilityOnPlayer`

### `CastOnPlayerInSeconds`

`OgreBotAPI.Abilities:CastOnPlayerInSeconds[fw, ability, player, seconds, calledFrom=OgreBotAPI]`

Casts an ability on a player after a delay by running :CastOnPlayer when the time is up. A bare number is seconds ("500ms" style values also work); with no player it uses the sending character.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `ability` | ability name or id |  | the ability to cast |
| `player` | player name or alias |  | who to cast it on |
| `seconds` | number or duration |  | how long to wait; bare number = seconds |
| `calledFrom` | text | `OgreBotAPI` | label for the cast log |

```text
OgreBotAPI.Abilities:CastOnPlayerInSeconds[${Me.Name},"Intercept",${Target.Name},3]
```

*Was (OldBot):* `OgreBotAPI:CastAbilityOnPlayerInSeconds`

### `CastOnPlayerNoChecks`

`OgreBotAPI.Abilities:CastOnPlayerNoChecks[fw, ability, player, calledFrom=OgreBotAPI]`

Queues a cast of an ability on a named player without the checks CastOnPlayer makes first (ready, power, range, line of sight); it is still dropped if not ready when it reaches the cast bar. The player defaults to you and must be you or in your group or raid.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `ability` | ability name or id |  | the ability to cast |
| `player` | player name or alias |  | who to cast it on; blank = you |
| `calledFrom` | text | `OgreBotAPI` | label for the cast log |

```text
OgreBotAPI.Abilities:CastOnPlayerNoChecks[${Me.Name},"Intercept",${Target.Name}]
```

*Was (OldBot):* `OgreBotAPI:CastAbilityOnPlayerNoChecks`

### `CastRescue`

`OgreBotAPI.Abilities:CastRescue[fw, calledFrom=CastRescue, ...opts]`

Casts a rescue: an ability that raises your threat position, or, if you have none, a force-target ability (-NoForceTargets skips that fallback). It checks against your current NPC target unless -TargetID &lt;id> (or -ActorID &lt;id>) names one; other words are added to the ability query.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `calledFrom` | text | `CastRescue` | label for the cast log |
| `...opts` | text |  | -NoForceTargets, -NPCRequired, -TargetID &lt;id> / -ActorID &lt;id>, or extra query terms |

```text
OgreBotAPI.Abilities:CastRescue[${Me.Name},MyScript,-NoForceTargets]
```

*Was (OldBot):* `OgreBotAPI:CastRescue`

### `Clear`

`OgreBotAPI.Abilities:Clear[fw]`

Unloads the ability export. Until you :Load again, Loaded is FALSE and anything that looks an ability up by name finds nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Abilities:Clear[${Me.Name}]
```

### `ClearAllEmbargos`

`OgreBotAPI.Abilities:ClearAllEmbargos[fw]`

Removes every ability embargo. Item embargoes are not touched.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Abilities:ClearAllEmbargos[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:AbilityEmbargo_ResetAllAbilityEmbargos`

### `ClearEmbargo`

`OgreBotAPI.Abilities:ClearEmbargo[fw, ability]`

Removes the embargo on one ability. Does nothing when the ability cannot be found or is not embargoed; item embargoes are not touched.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `ability` | ability name or id |  | the ability to release |

```text
OgreBotAPI.Abilities:ClearEmbargo[${Me.Name},"Sprint"]
```

*Was (OldBot):* `OgreBotAPI:AbilityEmbargo_ResetAbilityEmbargo`

### `DispellNPC`

`OgreBotAPI.Abilities:DispellNPC[fw, mob, op]`

Queues a dispel on a mob that runs as soon as your cast bar is free, and each call queues another. Characters with no dispel for the chosen op do nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `mob` | actor name or id |  | the mob to dispel (required) |
| `op` | text |  | how to dispel: any (your class dispel, else a dispel item; the default), ability or spell (class dispel only), item (dispel item only) |

```text
OgreBotAPI.Abilities:DispellNPC[igw:${Me.Name},${Target.ID},any]
```

### `Dump`

`OgreBotAPI.Abilities:Dump[fw, path]`

Writes the loaded ability list (one usable rank per line) to a file as JSON, replacing the file if it exists. Nothing is written when no path is given.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `path` | text |  | file to write the JSON to |

```text
OgreBotAPI.Abilities:Dump[${Me.Name},"abilities.json"]
```

### `FindAndCast`

`OgreBotAPI.Abilities:FindAndCast[fw, query...]`

Picks an ability by its properties and casts it: the same query as FindCastableID (terms like "IsInterrupt","=","TRUE" plus options such as -NPCRequired). A refused query is reported in the console; if nothing matches, nothing is cast.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `query...` | text |  | query terms (member, comparison, value) and options |

```text
OgreBotAPI.Abilities:FindAndCast["all","IsInterrupt","=","TRUE","-NPCRequired"]
```

*Was (OldBot):* `OgreBotAPI:CastAbility_Via`

### `Load`

`OgreBotAPI.Abilities:Load[fw, toon=me, level=myLevel]`

Loads a character's ability export and keeps, for each ability line, the highest rank at or below the level, then prints a loaded or failed line to the console. Outside the world you must give both toon and level.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `toon` | text | `me` | character whose export to load; left out = your own name (must be given outside the world) |
| `level` | number | `myLevel` | highest ability level to keep; left out = your own level (must be given outside the world) |

```text
OgreBotAPI.Abilities:Load[${Me.Name}]
```

### `Rebuff`

`OgreBotAPI.Abilities:Rebuff[fw]`

Cancels every maintained buff from your export that lasts until cancelled (links such as Powerlink are kept), so the rotation casts them again fresh. The recast only happens while the bot is casting.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Abilities:Rebuff[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Rebuff`

### `SetAOEsDisabled`

`OgreBotAPI.Abilities:SetAOEsDisabled[fw, disable=TRUE, -verbose, -allowcounters, -AllowEncounters, -aggressive]`

Stops (TRUE) or allows (FALSE) AE casting: it sets the ignore-PBAE, ignore-encounter-nukes and ignore-counter-abilities options, casts Singular Focus (Focus Offensive on a Guardian) and cancels class buffs that proc AEs; FALSE cancels the focus buff instead. -allowcounters keeps counter abilities and counter buffs, -AllowEncounters leaves encounter nukes on while disabling, -verbose announces the setting changes, and -aggressive does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `disable` | true/false | `TRUE` | TRUE stops AEs, FALSE allows them |
| `-verbose` | flag |  | announce the setting changes |
| `-allowcounters` | flag |  | leave counter abilities and counter buffs alone |
| `-AllowEncounters` | flag |  | keep encounter nukes when disabling |
| `-aggressive` | flag |  | accepted, does nothing |

```text
OgreBotAPI.Abilities:SetAOEsDisabled[igw:${Me.Name},TRUE,-allowcounters]
```

*Was (OldBot):* `OgreBotAPI:Set_DisableAllAOEs`

### `SetCancelCurrentCast`

`OgreBotAPI.Abilities:SetCancelCurrentCast[fw, on=TRUE]`

TRUE asks the bot to abort the cast it has in progress and raises the CancelCurrentCast flag; FALSE lowers the flag and withdraws an abort not yet acted on. The flag clears itself at the next cast start or end.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `on` | true/false | `TRUE` | TRUE cancels, FALSE withdraws |

```text
OgreBotAPI.Abilities:SetCancelCurrentCast[igw:${Me.Name},TRUE]
```

*Was (OldBot):* `OgreBotAPI:CancelCurrentCast`

### `SetDispellsEnabled`

`OgreBotAPI.Abilities:SetDispellsEnabled[fw, on=TRUE]`

Turns the bot's dispel casting on or off through the "no dispels" setting. A value that is not a yes/no word changes nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `on` | true/false | `TRUE` | TRUE enables dispels, FALSE disables them |

```text
OgreBotAPI.Abilities:SetDispellsEnabled[igw:${Me.Name},FALSE]
```

*Was (OldBot):* `OgreBotAPI:Enable_Dispells`, `OgreBotAPI:Disable_Dispells`

### `SetInterruptsEnabled`

`OgreBotAPI.Abilities:SetInterruptsEnabled[fw, on=TRUE]`

Turns the bot's interrupt casting on or off through the "no interrupts" setting; a value that is not a yes/no word changes nothing. Enabling also turns Daring Advance back on in the cast stack, and disabling on a Rogue turns Daring Advance off and cancels it.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `on` | true/false | `TRUE` | TRUE enables interrupts, FALSE disables them |

```text
OgreBotAPI.Abilities:SetInterruptsEnabled[igw:${Me.Name},FALSE]
```

*Was (OldBot):* `OgreBotAPI:Enable_Interrupts`, `OgreBotAPI:Disable_Interrupts`

### `SetStunsEnabled`

`OgreBotAPI.Abilities:SetStunsEnabled[fw, on=TRUE]`

Turns the bot's stun casting on or off through the "no stuns" setting; a value that is not a yes/no word changes nothing. Enabling also turns Blessed Weapon back on in the cast stack, and disabling on a Paladin turns Blessed Weapon off and cancels it.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `on` | true/false | `TRUE` | TRUE enables stuns, FALSE disables them |

```text
OgreBotAPI.Abilities:SetStunsEnabled[igw:${Me.Name},FALSE]
```

*Was (OldBot):* `OgreBotAPI:Disable_Stuns`, `OgreBotAPI:Enable_Stuns`

### `SetUpForDispells`

`OgreBotAPI.Abilities:SetUpForDispells[fw, on=TRUE]`

Sets the cast stack up for a dispel fight: TRUE turns the Absorb Magic, Tease and Cuss entries on, FALSE turns them back off. Nothing is cancelled either way, and a value that is not a yes/no word changes nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `on` | true/false | `TRUE` | TRUE sets up, FALSE resets |

```text
OgreBotAPI.Abilities:SetUpForDispells[igw:${Me.Name},TRUE]
```

*Was (OldBot):* `OgreBotAPI:SetUpFor_Dispells`, `OgreBotAPI:ResetFor_Dispells`

### `TrackerAdd`

`OgreBotAPI.Abilities:TrackerAdd[fw, ability]`

Adds an ability to the Ability Tracker watch list in the open profile (an id is stored as its name). The change is not saved until you save the profile; the console says if it is already on the list.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `ability` | ability name or id |  | the ability to watch |

```text
OgreBotAPI.Abilities:TrackerAdd[${Me.Name},"Sprint"]
```

*Was (OldBot):* `OgreBotAPI:AbilityTracker_Add`
