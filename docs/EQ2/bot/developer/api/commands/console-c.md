# Console commands: C

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## `-CallGH`

`-CallGH <who>`

Also: `-CallToGH`

Calls to guild hall if not already in one.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Movement:CallGH`

```text
oc !c -CallGH igw:${Me.Name}
```

## `-campspot`

`-campspot <who> <mindistance> <maxdistance>`

Also: `-cs-set-cs`, `-cs`

Sets campspot.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `mindistance` | float | `2` | Min. Distance |
| `maxdistance` | float | `200` | Max. Distance |

Runs: `OgreBotAPI.CampSpot:SetHere`

```text
oc !c -campspot igw:${Me.Name} 2 200
```

## `-CampToDesktop`

`-CampToDesktop <who> <loginonly>`

Also: `-Camp`

Camps to the login screen, then closes the session unless loginonly is TRUE. Refused while in combat.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `loginonly` | string | `FALSE` |  |

Runs: `OgreBotAPI.Bot:CampToDesktop`

```text
oc !c -CampToDesktop igw:${Me.Name} FALSE
```

## `-CancelCasting`

`-CancelCasting <who> <args>`

Also: `-Cancel_Casting`

Cancels the ability you are casting unless it is one of the ability names you list. -HOAbility, -HOAbilityUI and -CastTime &lt;seconds> narrow when it cancels, -CastAbility, -CastAbilityOnPlayer and -CastHOAbilityIconID queue a cast first, and any other -word cancels nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `args` | rest |  |  |

Runs: `OgreBotAPI.Abilities:CancelCasting`

```text
oc !c -CancelCasting igw:${Me.Name} "Bulwark of Order"
```

## `-cancelcastnoexport`

`-cancelcastnoexport <who> <abilityname>`

Also: `-ccstnoexport`, `-castnoexport`, `-CastAbilitynoexport`, `-cast_abilitynoexport`

Queues the named ability (a name or an id) only if the toon knows it and it is off cooldown, and silently does nothing otherwise. Despite the name it does not cancel the current cast.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `abilityname` | string | `Nothing` |  |

Runs: `OgreBotAPI.Abilities:CastNoExport`

```text
oc !c -cancelcastnoexport igw:${Me.Name} Kick
```

## `-CancelDetrimental`

`-CancelDetrimental <who> <mainid> <backdropid>`

Cancels the detrimental effect on you whose main icon id and backdrop icon id match the two values. Both 0 does nothing, and no match prints a console line.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `mainid` | string | `0` |  |
| `backdropid` | string | `0` |  |

Runs: `OgreBotAPI.Cures:CancelDetrimental`

```text
oc !c -CancelDetrimental igw:${Me.Name} 612 317
```

## `-CancelGroupWaterBreathing`

`-CancelGroupWaterBreathing <who>`

Cancels this class's group water-breathing effect if it is running. A class without one does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Abilities:CancelGroupWaterBreathing`

```text
oc !c -CancelGroupWaterBreathing igw:${Me.Name}
```

## `-CancelMaintained`

`-CancelMaintained <who> <abilityname> <args>`

Also: `-Cancel_Maintained`, `-CancelMaintainedForWho`, `-Cancel_MaintainedForWho`

Cancel Maintained ability

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who acts - leave blank to use the For Who window. |
| `abilityname` | string | `DefaultAbilityHere` | Ability to cancel |
| `args` | rest |  |  |

Runs: `OgreBotAPI.Abilities:CancelMaintainedFor`, `OgreBotAPI.Abilities:CancelMaintainedFor`

```text
oc !c -CancelMaintained igw:${Me.Name} "Spirit of the Wolf"
```

## `-CancelOnCast`

`-CancelOnCast <who> <abilityname>`

Fires the Cancel On Cast rows as if you had just cast this ability. Example: -CancelOnCast igw:${Me.Name} "Kick"

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `abilityname` | string |  | The ability name to trigger on. |

Runs: `OgreBotAPI.Abilities:CancelOnCast`

```text
oc !c -CancelOnCast igw:${Me.Name} Kick
```

## `-Cast_Interrupt`

`-Cast_Interrupt <who> <mobnameid> <calledfrom>`

Also: `-CastInterrupt`

Casts an interrupt the toon has ready at the given mob (an exact name or an actor id), first cancelling its current cast unless that is already an interrupt. It echoes when the mob is not found or no interrupt is ready.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `mobnameid` | string |  |  |
| `calledfrom` | string | `OgreConsole_Cast_Interrupt` |  |

Runs: `OgreBotAPI.Abilities:CastInterrupt`

```text
oc !c -Cast_Interrupt igw:${Me.Name} ${Target.ID} MyScript
```

## `-CastAbility`

`-CastAbility <who> <abilityname>`

Also: `-cancelcast`, `-ccst`, `-cast`, `-cast_ability`

Casts an ability at your current target, by name or id.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `abilityname` | string | `Nothing` | Spell to be cast |

Runs: `OgreBotAPI.Abilities:Cast`

```text
oc !c -CastAbility igw:${Me.Name} Kick
```

## `-CastAbilityInSeconds`

`-CastAbilityInSeconds <who> <abilityname> <seconds>`

Casts the named ability after a delay, through the same checks as -CastAbility when the time is up. A bare number is seconds, a suffix such as 500ms is honoured, and a blank ability name only echoes an error.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `abilityname` | string | `Nothing` |  |
| `seconds` | string | `1` |  |

Runs: `OgreBotAPI.Abilities:CastInSeconds`

```text
oc !c -CastAbilityInSeconds igw:${Me.Name} Kick 5
```

## `-CastAbilityNoChecks`

`-CastAbilityNoChecks <who> <abilityname>`

Tells [Bots] to cast a specific [ability]. Note - Abilities must be base names. Kick will work. Kick III will not. Note - This does NO checks about the ability. It just clicks it.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `abilityname` | string | `Nothing` | Spell to be cast |

Runs: `OgreBotAPI.Abilities:CastNoChecks`

```text
oc !c -CastAbilityNoChecks igw:${Me.Name} Kick
```

## `-CastAbilityOnNPC`

`-CastAbilityOnNPC <who> <abilityname> <mobnameid>`

Also: `-castonnpc`, `-castonmob`

Tells [Bots] to cast a specific [ability] on an [NPC]. Note - Abilities must be base names. Kick will work. Kick III will not.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `abilityname` | string | `Nothing` | Spell to be cast |
| `mobnameid` | string | `0` | NPC ID or NPC Name. \${Target.ID} will work fine |

Runs: `OgreBotAPI.Abilities:CastOnNPC`

```text
oc !c -CastAbilityOnNPC igw:${Me.Name} Kick ${Target.ID}
```

## `-CastAbilityOnPlayer`

`-CastAbilityOnPlayer <who> <abilityname> <onplayer>`

Also: `-cancelcaston`, `-ccaston`, `-caston`, `-cast_ability_on_player`

Tells [Bots] to cast a specific [ability]. Note - Abilities must be base names. Kick will work. Kick III will not.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `abilityname` | string | `Nothing` | Spell to be cast |
| `onplayer` | string | `${Me.Name}` | Cast spell on this player |

Runs: `OgreBotAPI.Abilities:CastOnPlayer`

```text
oc !c -CastAbilityOnPlayer igw:${Me.Name} "Spirit of the Wolf" ${Me.Name}
```

## `-CastAbilityOnPlayerInSeconds`

`-CastAbilityOnPlayerInSeconds <who> <abilityname> <onplayer> <seconds>`

Casts the ability on the named player after a delay, through the same checks as -CastAbilityOnPlayer when the time is up. A bare number is seconds, and a blank player (or DoesNotExist) means the toon that sent the command.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `abilityname` | string | `Nothing` |  |
| `onplayer` | string | `${Me.Name}` |  |
| `seconds` | string | `1` |  |

Runs: `OgreBotAPI.Abilities:CastOnPlayerInSeconds`

```text
oc !c -CastAbilityOnPlayerInSeconds igw:${Me.Name} "Spirit of the Wolf" ${Group[1].Name} 10
```

## `-CastAbilityOnPlayerNoChecks`

`-CastAbilityOnPlayerNoChecks <who> <abilityname> <onplayer> <calledfrom>`

Queues the ability on the named player without the readiness checks -CastAbilityOnPlayer makes, though the player must still be present. A blank player (or DoesNotExist) means yourself, and an ability the toon does not know does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `abilityname` | string | `Nothing` |  |
| `onplayer` | string | `DoesNotExist` |  |
| `calledfrom` | string | `OgreBotAPI` |  |

Runs: `OgreBotAPI.Abilities:CastOnPlayerNoChecks`

```text
oc !c -CastAbilityOnPlayerNoChecks igw:${Me.Name} "Spirit of the Wolf" ${Group[1].Name} MyScript
```

## `-CastBulwarkImmediately`

`-CastBulwarkImmediately <who>`

Casts Bulwark of Order right now: it queues the cast at high priority, cancels any other cast in the way and tries once more a second later if it has not gone off. If the ability is not in the toon's export or not ready, it casts nothing and warns everyone, at most once every 30 seconds.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Abilities:CastBulwark`

```text
oc !c -CastBulwarkImmediately igw:${Me.Name}
```

## `-CastGroupWaterBreathing`

`-CastGroupWaterBreathing <who>`

Casts this class's group water-breathing ability through the normal cast path. A class without one, or a character whose ability export does not list it, does nothing (the reason goes to the log file).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Abilities:CastGroupWaterBreathing`

```text
oc !c -CastGroupWaterBreathing igw:${Me.Name}
```

## `-CastHOIconID`

`-CastHOIconID <who> <iconid> <calledfrom>`

Casts the toon's own ability that matches the given heroic opportunity icon id, through the same checks as -CastAbility. An icon id of -2 or blank does nothing, and so does an icon no owned ability matches right now.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `iconid` | string | `-2` | The HO icon id to cast an ability for (a number, not an ability name); -2 casts nothing. |
| `calledfrom` | string | `CastHOIconID` |  |

Runs: `OgreBotAPI.Abilities:CastHOIcon`

```text
oc !c -CastHOIconID igw:${Me.Name} 3 MyScript
```

## `-CastRescue_AP`

`-CastRescue_AP <who> <calledfrom> <args>`

Casts a rescue at your NPC target: a threat-position-increase ability first, or a force-target ability when there is none (-NoForceTargets skips that step). -TargetID or -ActorID &lt;id> aims at that actor, other arguments narrow the ability query, and a console line says when nothing was found.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `calledfrom` | string | `OgreBotAPI:CastRescue` |  |
| `args` | rest |  |  |

Runs: `OgreBotAPI.Abilities:CastRescue`

```text
oc !c -CastRescue_AP ${Me.Name} CastRescue -NoForceTargets
```

## `-Champions_Zone_Resetter`

`-Champions_Zone_Resetter <who> <zonename>`

Uses your Champion's Zone Lockout Reset item to reset the lockout of the named zone, picking it from the item's select window, and skips when the reset is on cooldown. Runs in the action queue, and prints a console line and stops when the item is not in your bags.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `zonename` | string | `DoesNotExist` |  |

Runs: `OgreBotAPI.Zone:ChampionsResetter`

```text
oc !c -Champions_Zone_Resetter ${Me.Name} "${Zone.Name}"
```

## `-ChangeBeltAdorn`

`-ChangeBeltAdorn <who> <value> <unequip>`

Changes your belt adorn. Valid options are stun stifle mez fear medic.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string | `?` | Which adornment to put on the belt: Stun, Stifle, Mez, Fear or Medic. |
| `unequip` | string | `TRUE` | Unequip belt |

Runs: `OgreBotAPI.Inventory:ChangeBeltAdorn`

```text
oc !c -ChangeBeltAdorn igw:${Me.Name} Stun TRUE
```

## `-ChangeCampSpot`

`-ChangeCampSpot <who> <x> <y> <z>`

Also: `-Change_CampSpot`, `-ccs`, `-ChangeCampSpotWho`, `-Change_Campspot_Who`, `-ccsw`, `-ccsfw`

Relays a change to active campspots.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who acts - leave blank to use the For Who window. |
| `x` | string |  | X, or the name of a point of interest in this zone |
| `y` | string |  | YCord |
| `z` | string |  | ZCord |

Runs: `OgreBotAPI.CampSpot:SetLoc`

```text
oc !c -ChangeCampSpot igw:${Me.Name} ${Me.X} ${Me.Y} ${Me.Z}
```

## `-ChangeCastStackListBoxItem`

`-ChangeCastStackListBoxItem <who> <object> <value> <silentmode>`

Also: `-ChangeCastStack`, `-CCastStack`, `-CCStack`

Changes a list box item on the CAST STACK tab only.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `object` | string |  | Ability name |
| `value` | string | `TRUE` | TRUE - FALSE or TOGGLE |
| `silentmode` | bool | `FALSE` | Silent mode. TRUE or FALSE |

Runs: `OgreBotAPI.CastStack:SetEntry`

```text
oc !c -ChangeCastStackListBoxItem igw:${Me.Name} "Absorb Magic" TOGGLE FALSE
```

## `-ChangeCastStackListBoxItemByTag`

`-ChangeCastStackListBoxItemByTag <who> <object> <value> <partial> <silentmode>`

Also: `-ChangeCastStackByTag`, `-CCastStackByTag`, `-CCStackByTag`

Changes a list box item on the CAST STACK tab only by custom Tags.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `object` | string |  | Tag name |
| `value` | string | `TRUE` | Status: (Enabled/Disabled) TRUE or FALSE or Toggle |
| `partial` | bool | `FALSE` | Partial match: TRUE or FALSE (case sensitive) |
| `silentmode` | bool | `FALSE` | Silent mode. TRUE or FALSE (case sensitive) |

Runs: `OgreBotAPI.CastStack:SetEntryByTag`

```text
oc !c -ChangeCastStackListBoxItemByTag igw:${Me.Name} AE FALSE FALSE FALSE
```

## `-ChangeLootOptions`

`-ChangeLootOptions <who> <args>`

Changes loot options. Parameters after = Options you want. Such as LO or RR or FFA. See wiki for full possible parameters.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `args` | rest |  |  |

Runs: `OgreBotAPI.Loot:SetOptions`

```text
oc !c -ChangeLootOptions ${Me.Name} RR T AN
```

## `-ChangeOgreBotUIOption`

`-ChangeOgreBotUIOption <who> <args>`

Changes an OgreBot option: a checkbox (TRUE / FALSE / TOGGLE), a text box, a dropdown or a slider (its value). Param 1 = For who. Param 2 = the option's name - in OgreBot, right-click the option and choose Copy &lt;name>. Param 3 = the value.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `args` | rest |  |  |

Runs: `OgreBotAPI.Options:Set`

```text
oc !c -ChangeOgreBotUIOption igw:${Me.Name} checkbox_autotarget_enabled TRUE
```

## `-ChangeZoneTo`

`-ChangeZoneTo <who> <value>`

Changes your zone # to someone elses in your group. Example: You are in Phantom Seas 2 and your group is in Phantom Seas 3.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string |  | Toon name's zone to move to. Example: Bob. \${Me.Name} is acceptable also |

Runs: `OgreBotAPI.Zone:ChangeZoneTo`

```text
oc !c -ChangeZoneTo ${Me.Name} ${Group[1].Name}
```

## `-CheckGear`

`-CheckGear <who> <equalorunder>`

Also: `-Gear`

Reports gear conditions. Value to report. Will always report under 30. If you want it to report 90% or below use 90.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `equalorunder` | string | `100` |  |

Runs: `OgreBotAPI.Inventory:CheckGear`

```text
oc !c -CheckGear igw:${Me.Name} 90
```

## `-CheckKunarkAscendingRequirements`

`-CheckKunarkAscendingRequirements <who>`

Will report back any quests that you are missing for Kunark Ascending signature request line requirements.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Quest:CheckKunarkAscending`

```text
oc !c -CheckKunarkAscendingRequirements igw:${Me.Name}
```

## `-CheckMemberLevel`

`-CheckMemberLevel <who> <value>`

Reports EQ2's membership level. Such as Member or silver or free. Optional Parameter: Set to TRUE if you only want to see non-members.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string | `FALSE` |  |

Runs: `OgreBotAPI.Roster:CheckMemberLevel`

```text
oc !c -CheckMemberLevel igw:${Me.Name} FALSE
```

## `-CheckMercenaryTraining`

`-CheckMercenaryTraining <who>`

Resumes your mercenary when it is not out, opens Persona, Mercenary and prints the training progress or starts training; in a full group it stops at once with a console line. Runs in the action queue, and a second press replaces the first.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Consumables:CheckMercenaryTraining`

```text
oc !c -CheckMercenaryTraining ${Me.Name}
```

## `-CheckMountTraining`

`-CheckMountTraining <who>`

Opens Persona, Mounts and starts mount training when it is not running, answering the confirm popup. Runs in the action queue, and you must be on a mount (not a flight transport).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Consumables:CheckMountTraining`

```text
oc !c -CheckMountTraining ${Me.Name} FALSE
```

## `-CheckResearch`

`-CheckResearch <who> <value>`

Checks if your research of abilities is done. Only reports completed by default. Pass TRUE if you want to see how long remaining.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string | `FALSE` | Report all values |

Runs: `OgreBotAPI.Util:CheckResearch`

```text
oc !c -CheckResearch igw:${Me.Name} TRUE
```

## `-CheckVersion`

`-CheckVersion <who> <compareversionto>`

Each session compares its version to the one you pass and reports the verdict to IRC. Leave the version blank to just report versions.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `compareversionto` | string |  | Version to compare against. Blank = just report the version. |

Runs: `OgreBotAPI.Comms:ReportVersion`

```text
oc !c -CheckVersion all
```

## `-ChoiceWindow`

`-ChoiceWindow <who> <value>`

Clicks option N (default 1) on the yes/no choice window on screen. Nothing happens when none is open.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | int64 | `1` |  |

Runs: `OgreBotAPI.Windows:Choice`

```text
oc !c -ChoiceWindow igw:${Me.Name} 1
```

## `-ClassInfo_ChangeValue`

`-ClassInfo_ChangeValue <who> <member> <value>`

Overrides one class check (such as IsFighter) for this character, so the bot treats the class as having that value; auto removes the override. A member that is not a class name, or a value that is not TRUE, FALSE or auto, is refused with a console line, and the override is dropped when you switch characters.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `member` | string | `DoesNotExist` |  |
| `value` | string | `FALSE` |  |

Runs: `OgreBotAPI.Roster:SetClassValue`

```text
oc !c -ClassInfo_ChangeValue ${Me.Name} IsFighter TRUE
```

## `-Clear_Allow_HOICon`

`-Clear_Allow_HOICon <who> <variablename>`

Removes one HO icon id from the allow list.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `variablename` | int64 |  |  |

Runs: `OgreBotAPI.HOs:ClearAllowIcon`

```text
oc !c -Clear_Allow_HOICon ${Me.Name} 12
```

## `-Clear_Allow_HOICons`

`-Clear_Allow_HOICons <who>`

Empties the HO icon allow list, so Heroic Opportunity abilities are no longer limited to it.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.HOs:ClearAllowIcons`

```text
oc !c -Clear_Allow_HOICons ${Me.Name}
```

## `-Clear_Disable_HOICon`

`-Clear_Disable_HOICon <who> <variablename>`

Removes one HO icon id from the disable list.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `variablename` | int64 |  |  |

Runs: `OgreBotAPI.HOs:ClearDisableIcon`

```text
oc !c -Clear_Disable_HOICon ${Me.Name} 24
```

## `-Clear_Disable_HOICons`

`-Clear_Disable_HOICons <who>`

Empties the HO icon disable list.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.HOs:ClearDisableIcons`

```text
oc !c -Clear_Disable_HOICons ${Me.Name}
```

## `-clear_Internalvariable`

`-clear_Internalvariable <who> <variablename>`

Removes the named entry from the bot's internal variable store on this session.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `variablename` | string |  |  |

Runs: `OgreBotAPI.Vars:ClearInternal`

```text
oc !c -clear_Internalvariable ${Me.Name} PullCount
```

## `-clear_Internalvariables`

`-clear_Internalvariables <who>`

Empties the bot's internal variable store on this session.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Vars:ClearAllInternal`

```text
oc !c -clear_Internalvariables ${Me.Name}
```

## `-clear_variable`

`-clear_variable <who> <variablename>`

Removes the named entry from the script variable store on this session.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `variablename` | string |  |  |

Runs: `OgreBotAPI.Vars:Clear`

```text
oc !c -clear_variable igw:${Me.Name} Phase
```

## `-clear_variables`

`-clear_variables <who>`

Empties the script variable store on this session.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Vars:ClearAll`

```text
oc !c -clear_variables igw:${Me.Name}
```

## `-ClearNoOffensiveOn`

`-ClearNoOffensiveOn <who>`

Empties the no-offensive mob name list. The -SetNoOffensive switch is not changed.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Combat:ClearNoOffensive`

```text
oc !c -ClearNoOffensiveOn igw:${Me.Name}
```

## `-CloseExamineWindow`

`-CloseExamineWindow <who>`

Clicks the Close button of the item examine window.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Windows:CloseExamine`

```text
oc !c -CloseExamineWindow ${Me.Name}
```

## `-CloseWindow`

`-CloseWindow <who>`

Also: `-ClsWdn`

Close Window. Closes the top most window in the game.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Windows:Close`

```text
oc !c -CloseWindow igw:${Me.Name}
```

## `-Come2Me`

`-Come2Me <who> <moveto> <precision>`

Also: `-ComeTome`

Tells [Bots] to move to a specific [player].

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to move - leave blank to use the For Who window. |
| `moveto` | string | `${Me.Name}` | Player to move to (the destination toon) |
| `precision` | float | `3` | Precision |

Runs: `OgreBotAPI.Movement:Come2Me`

```text
oc !c -Come2Me igw:${Me.Name} ${Me.Name} 3
```

## `-CompareQuest`

`-CompareQuest <who> <questname> <sender>`

Asks the boxes named whether they are on the same step of a quest as you. Only the box that sends the line asks.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who is asked - leave blank to use the For Who window. all asks your group. |
| `questname` | string |  | The quest to compare. Quote a name with spaces. IE: "A Quest Name" |
| `sender` | string | `${Me.Name}` | The box that asks. Leave this out: it is the box that sent the line. |

Runs: `OgreBotAPI.Quest:CompareUpdate`

```text
oc !c -CompareQuest all "The Quest Name"
```

## `-Consume_Familiars`

`-Consume_Familiars <who>`

Adds Familiars to collection if possible otherwise consumes for experience.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Inventory:ConsumeFamiliars`

```text
oc !c -Consume_Familiars igw:${Me.Name}
```

## `-Consume_Status_Ingots`

`-Consume_Status_Ingots <who> <value>`

Also: `-Consume_Status_Ignots`

Consumes Ingots.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string | `99999` | How Many to consume |

Runs: `OgreBotAPI.Inventory:ConsumeStatusIngots`

```text
oc !c -Consume_Status_Ingots igw:${Me.Name} 10
```

## `-Consume_Status_Tokens`

`-Consume_Status_Tokens <who> <value>`

Consumes Status Tokens.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string | `99999` | How Many to consume |

Runs: `OgreBotAPI.Inventory:ConsumeStatusTokens`

```text
oc !c -Consume_Status_Tokens igw:${Me.Name} 10
```

## `-ConsumeItems_ProcessList_AP`

`-ConsumeItems_ProcessList_AP <who> <args>`

Uses the items on your profile's Consume Items tab, top to bottom, skipping disabled rows, in-combat-only rows out of combat, items on their snack timer and items not ready; it stops after the first item used unless -all is given. -fc ignores the in-combat-only marks and the in-combat throttle, and -st ignores the snack timers.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `args` | rest |  |  |

Runs: `OgreBotAPI.Inventory:ConsumeList`

```text
oc !c -ConsumeItems_ProcessList_AP igw:${Me.Name} -all -st
```

## `-ConversationBubble`

`-ConversationBubble <who> <num>`

Also: `-Conversation_Bubble`

After hailing you can use this to converse with an NPC.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `num` | string | `1` | chat option to choose |

Runs: `OgreBotAPI.Comms:ConversationBubble`

```text
oc !c -ConversationBubble igw:${Me.Name} 1
```

## `-countdown`

`-countdown <who> <time>`

Starts the in-game group countdown for the given number of seconds. Only a grouped group leader does it, everyone else does nothing, and a time of 0 or over 30 echoes an error instead.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `time` | string | `1` |  |

Runs: `OgreBotAPI.Combat:Countdown`

```text
oc !c -countdown ${Me.Name} 10
```

## `-CoV`

`-CoV <who> <traveloption> <toonoption> <allowsamezone>`

Uses Call of the Veteran.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `traveloption` | string | `Teleport` | TravelOption. Teleport or Summon |
| `toonoption` | string | `ToonName` | Toon to interact with |
| `allowsamezone` | string | `FALSE` | Allow Same zone |

Runs: `OgreBotAPI.Consumables:CoV`

```text
oc !c -CoV ${Me.Name} Summon ${Group[1].Name} FALSE
```

## `-Crouch`

`-Crouch <who>`

Presses the crouch key once.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Movement:Crouch`

```text
oc !c -Crouch igw:${Me.Name}
```

## `-CS_ClearAll`

`-CS_ClearAll <who>`

Clears Campspot data

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.CampSpot:ClearAll`

```text
oc !c -CS_ClearAll igw:${Me.Name}
```

## `-CS_ClearCampSpot`

`-CS_ClearCampSpot <who>`

Clears Campspot location only

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.CampSpot:ClearCampSpot`

```text
oc !c -CS_ClearCampSpot igw:${Me.Name}
```

## `-CS_ClearRelative`

`-CS_ClearRelative <who>`

Clears Relative data

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.CampSpot:ClearRelative`

```text
oc !c -CS_ClearRelative igw:${Me.Name}
```

## `-CS_Set_ChangeCampSpot`

`-CS_Set_ChangeCampSpot <who> <x> <y> <z>`

Changes the base campspot.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `x` | string | `${Me.X}` | X, or the name of a point of interest in this zone |
| `y` | string | `${Me.Y}` | Y |
| `z` | string | `${Me.Z}` | Z |

Runs: `OgreBotAPI.CampSpot:SetLoc`

```text
oc !c -CS_Set_ChangeCampSpot igw:${Me.Name} ${Me.X} ${Me.Y} ${Me.Z}
```

## `-CS_Set_ChangeCampSpotBy`

`-CS_Set_ChangeCampSpotBy <who> <x> <y> <z>`

Also: `-ccsbw`, `-ccsbfw`, `-ccsbyforwho`, `-ccsb`, `-ChangeCampSpotBy`, `-cs-set-ccs-by`

Changes the base campspot by.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `x` | string | `0` | X |
| `y` | string | `0` | Y |
| `z` | string | `0` | Z |

Runs: `OgreBotAPI.CampSpot:NudgeBy`

```text
oc !c -CS_Set_ChangeCampSpotBy igw:${Me.Name} 5 0 -5
```

## `-CS_Set_ChangeRelativeCampSpotBy`

`-CS_Set_ChangeRelativeCampSpotBy <who> <x> <y> <z>`

Changes the relative campspot by.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `x` | string | `0` | X delta to ADD to the relative campspot (0 = no change) |
| `y` | string | `0` | Y/height delta to add (0 = no change) |
| `z` | string | `0` | Z delta to add (0 = no change) |

Runs: `OgreBotAPI.CampSpot:SetRelativeBy`

```text
oc !c -CS_Set_ChangeRelativeCampSpotBy igw:${Me.Name} 0 0 10
```

## `-CS_Set_Formation_Circle`

`-CS_Set_Formation_Circle <who> <distance> <x> <y> <z> <userelativecs>`

Also: `-cs-circle`

Creates a circle.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `distance` | float | `7` | Distance from center. Example: 7 |
| `x` | string | `${Me.X}` | X Position of Center, or the name of a point of interest in this zone. \${Me.X} is acceptable |
| `y` | string | `${Me.Y}` | Y Position of Center. \${Me.Y} is acceptable |
| `z` | string | `${Me.Z}` | Z Position of Center. \${Me.Z} is acceptable |
| `userelativecs` | bool | `FALSE` | Use Relative campspot instead of campspot: TRUE or FALSE. |

Runs: `OgreBotAPI.CampSpot:SetFormation`

```text
oc !c -CS_Set_Formation_Circle igw:${Me.Name} 7 ${Me.X} ${Me.Y} ${Me.Z} FALSE
```

## `-CS_Set_Formation_MonkeyInMiddle`

`-CS_Set_Formation_MonkeyInMiddle <who> <distance> <x> <y> <z> <middleman> <userelativecs>`

Also: `-cs-monkey`

Creates a circle with one person in the middle.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `distance` | float | `7` | Distance from center. Example: 7 |
| `x` | string | `${Me.X}` | X Position of Center, or the name of a point of interest in this zone. \${Me.X} is acceptable |
| `y` | string | `${Me.Y}` | Y Position of Center. \${Me.Y} is acceptable |
| `z` | string | `${Me.Z}` | Z Position of Center. \${Me.Z} is acceptable |
| `middleman` | string | `${Me.Name}` | Who will be in the middle. \${Me.Name} is acceptable |
| `userelativecs` | bool | `FALSE` | Use Relative campspot instead of campspot: TRUE or FALSE. |

Runs: `OgreBotAPI.CampSpot:SetFormation`

```text
oc !c -CS_Set_Formation_MonkeyInMiddle igw:${Me.Name} 7 ${Me.X} ${Me.Y} ${Me.Z} ${Me.Name} FALSE
```

## `-CS_Set_Formation_MonkeyInMiddleRaid`

`-CS_Set_Formation_MonkeyInMiddleRaid <who> <middleforwho> <distance> <x> <y> <z> <circlespots> <userelativecs>`

Also: `-cs-monkeyRaid`

Gives each matched toon its own spot on a ring of circlespots spots (default 5, placed by raid order) at distance (default 7) around x y z, while the toons middleforwho matches stand on the centre. userelativecs TRUE sets the relative campspot instead of the base one, and nothing is set (a console line says so) while OgreBot is not open.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `middleforwho` | string |  |  |
| `distance` | float | `7` |  |
| `x` | string | `${Me.X}` | X, or the name of a point of interest in this zone |
| `y` | string | `${Me.Y}` |  |
| `z` | string | `${Me.Z}` |  |
| `circlespots` | string | `5` |  |
| `userelativecs` | bool | `FALSE` |  |

Runs: `OgreBotAPI.CampSpot:SetFormation`

```text
oc !c -CS_Set_Formation_MonkeyInMiddleRaid all igw:${Me.Name} 15 ${Me.X} ${Me.Y} ${Me.Z} 5 FALSE
```

## `-CS_Set_HowClose`

`-CS_Set_HowClose <who> <value>`

Changes the HowClose for CampSpot

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | float | `1` | HowClose |

Runs: `OgreBotAPI.CampSpot:SetHowClose`

```text
oc !c -CS_Set_HowClose igw:${Me.Name} 3
```

## `-CS_Set_HowFar`

`-CS_Set_HowFar <who> <value>`

Changes the HowFar for CampSpot

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | float | `200` | HowFar |

Runs: `OgreBotAPI.CampSpot:SetHowFar`

```text
oc !c -CS_Set_HowFar igw:${Me.Name} 200
```

## `-CS_Set_Relative`

`-CS_Set_Relative <who> <x> <y> <z>`

Sets the relative camp spot to this location (an absolute location, not an offset; -CS_Set_ChangeRelativeCampSpotBy moves it by an offset).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `x` | string | `${Me.X}` | X of the flat relative campspot (absolute coordinate, NOT a diff/offset) |
| `y` | string | `${Me.Y}` | Y/height of the flat relative campspot (absolute, not a diff) |
| `z` | string | `${Me.Z}` | Z of the flat relative campspot (absolute, not a diff) |

Runs: `OgreBotAPI.CampSpot:SetRelativeLoc`

```text
oc !c -CS_Set_Relative igw:${Me.Name} ${Me.X} ${Me.Y} ${Me.Z}
```

## `-CurePotions_Replenish`

`-CurePotions_Replenish <who> <potion>`

Replenishes cure potions from the depot. Default is all. Other options are: Arcane, Trauma, Noxious, Elemental. All other options will be assumed to be the full name.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `potion` | string | `all` | Optional. Which cure: all, arcane, elemental, noxious or trauma. |

Runs: `OgreBotAPI.Cures:ReplenishPotions`

```text
oc !c -CurePotions_Replenish igw:${Me.Name} trauma
```
