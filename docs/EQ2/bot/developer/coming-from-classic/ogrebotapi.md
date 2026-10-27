<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../index.md).
</div>

# OgreBotAPI

Every name Classic's *OgreBotAPI Reference* page listed, and what it is in the new bot. The flat `OgreBotAPI:Name` list became groups (`OgreBotAPI.Movement`, `OgreBotAPI.Cures`, …): each section below is one group. Use your browser's find (Ctrl+F) with the old name.

> **:warning: An old call does nothing now - it does not give an error**
>
> The new bot does not keep the old names. A call to an old method silently does nothing and a read of an old member gives `NULL`. Find your name below and write what the row says instead.

## At a glance

| What happened | Names |
|---|---|
| ⚠️ Arguments changed | 70 |
| ⚠️ Argument order changed | 7 |
| ✏️ Renamed | 341 |
| ➡️ Moved | 112 |
| ➡️ Lives somewhere else | 10 |
| 📄 In a data file now | 4 |
| ⛔ Exists, does nothing yet | 1 |
| ⛔ Not ported yet | 81 |
| ⛔ Removed | 42 |
| ✅ Works as is | 17 |
| **Total** | **685** |

The camp-spot calls are on the [Camp spot](campspot.md) page, the `Ask` calls on [Ask query system](ask.md) and the `…Preferred` calls on [Preferred group members](preferred.md).

## Worked examples

One real Classic line per kind of change, and the line that replaces it.

### ⚠️ Arguments changed: `OgreBotAPI:Unpack_PlanarStones`

```
; before (Classic)
OgreBotAPI:Unpack_PlanarStones["${_CommandForWho}","${_Option}"]
; after (new bot)
OgreBotAPI.Inventory:Unpack["${_CommandForWho}","Planar Stones",-all,-pick,lowest]
```

The stone unpack is the general unpack with the item named: -all until none is left, -pick lowest for the stone you have fewest of.

### ✏️ Renamed: `OgreBotAPI:Select_Window_Spew`

```
; before (Classic)
OgreBotAPI:Select_Window_Spew["${_CommandForWho}",${Args}]
; after (new bot)
OgreBotAPI.Windows:SelectSpew["${_CommandForWho}"]
```

The Classic method only ever read the for-who (Select_Window_Spew(string _ForWho=all)); the extra arguments this console line passed were ignored, so the new call takes the for-who alone.

### ➡️ Moved: `OgreBotAPI:Jump`

```
; before (Classic)
OgreBotAPI:Jump
; after (new bot)
OgreBotAPI.Movement:Jump[all]
```

## OgreBotAPI.Abilities

Old names whose job is now in `OgreBotAPI.Abilities`.

**Note A** (3 rows below): The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:AbilityEmbargo_AddRotateTimer` | does nothing | `OgreBotAPI.Abilities:AddEmbargo` `[fw,id,durationSec]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. does NOT take a for-who. `[abilityId, durationSeconds]`. Note its sibling `:ClearEmbargo` is `[forwho, abilityName]` - different arg 0, different key type. |
| `OgreBotAPI:AbilityEmbargo_ResetAbilityEmbargo` | does nothing | `OgreBotAPI.Abilities:ClearEmbargo` `[fw,ability]` | ✏️ Renamed |  |
| `OgreBotAPI:AbilityEmbargo_ResetAllAbilityEmbargos` | does nothing | `OgreBotAPI.Abilities:ClearAllEmbargos` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI.AbilityReady` | reads NULL | `OgreBotAPI.Abilities.Ready` | ✏️ Renamed |  |
| `OgreBotAPI:AbilityTracker_Add` | does nothing | `OgreBotAPI.Abilities:TrackerAdd` `[fw,ability]` | ✏️ Renamed |  |
| `OgreBotAPI:CancelCasting` | reads NULL | `OgreBotAPI.Abilities:CancelCasting` `[fw,except...,-HOAbility,-HOAbilityUI,-CastTime s]` | ➡️ Moved |  |
| `OgreBotAPI:CancelCasting_OLD` | does nothing | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI.Abilities:CancelCastingOld` was a stub that did nothing, and it was removed 2026-10-22. Use Abilities:CancelCasting. |
| `OgreBotAPI:CancelCurrentCast` | reads NULL | `OgreBotAPI.Abilities:SetCancelCurrentCast` `[fw,on=TRUE]` | ✏️ Renamed |  |
| `OgreBotAPI:CancelGroupWaterBreathing` | does nothing | `OgreBotAPI.Abilities:CancelGroupWaterBreathing` `[fw]` | ➡️ Moved |  |
| `call OgreBotAPI.CancelInvis` | does nothing | `OgreBotAPI.Abilities:CancelInvis` `[fw]` | ⚠️ Arguments changed | Note A |
| `OgreBotAPI:CancelMaintained` | does nothing | `OgreBotAPI.Abilities:CancelMaintained` `[ability...]` | ➡️ Moved | does NOT take a for-who. Argument 0 is an ability name, exactly as in Classic. `OgreBotAPI.Abilities:CancelMaintainedFor["all","Sprint"]` is the gated twin. Doc 21 lists this verb as having gained a for-who; the implementation says otherwise and the implementation is what runs. |
| `OgreBotAPI:CancelMaintainedForWho` | does nothing | `OgreBotAPI.Abilities:CancelMaintainedFor` `[fw,ability...]` | ✏️ Renamed | the gated twin, renamed to `:CancelMaintainedFor`. For-who at arg 0, ability names from arg 1. |
| `OgreBotAPI:Cast_Interrupt` | does nothing | `OgreBotAPI.Abilities:CastInterrupt` `[fw,mobNameOrId="",calledFrom=Cast_Interrupt]` | ✏️ Renamed |  |
| `OgreBotAPI:CastAbility` | does nothing | `OgreBotAPI.Abilities:Cast` `[fw,ability,calledFrom=OgreBotAPI]` | ✏️ Renamed |  |
| `OgreBotAPI:CastAbility_Relay` | does nothing | `OgreBotAPI.Abilities:CastRelay` `[fw,ability]` | ✏️ Renamed |  |
| `OgreBotAPI:CastAbility_Via` | does nothing | `OgreBotAPI.Abilities:CastVia` `[fw,query...]` | ✏️ Renamed |  |
| `OgreBotAPI:CastAbilityInSeconds` | does nothing | `OgreBotAPI.Abilities:CastInSeconds` `[fw,ability,delay,calledFrom=OgreBotAPI]` | ✏️ Renamed | `[fw, ability, delay, calledFrom]` - positionally identical to Classic. A BARE delay is SECONDS: the scheduler's global default is milliseconds, and this verb overrides it because its name states the unit, so `[...,25]` is 25 seconds exactly as Classic meant it. An explicit unit still wins (`"500ms"`, `"2m"`), and a bare decimal is legal (Classic took a `float`). `calledFrom` rides through to the cast log's "called from:" label - pass it, it is how you find where a cast came from. Ability may be an id or a NAME (names resolve off the export catalog, no server call). |
| `OgreBotAPI:CastAbilityInSeconds_Relay` | does nothing | `OgreBotAPI.Abilities:CastInSeconds` `[fw,ability,delay,calledFrom=OgreBotAPI]` | ✏️ Renamed | see `CastAbilityInSeconds` for the arguments - and note the bare-delay-is-SECONDS rule. |
| `OgreBotAPI:CastAbilityNoChecks` | does nothing | `OgreBotAPI.Abilities:CastNoChecks` `[fw,ability,calledFrom=OgreBotAPI]` | ✏️ Renamed |  |
| `OgreBotAPI:CastAbilityNoExport` | does nothing | `OgreBotAPI.Abilities:CastNoExport` `[fw,ability,calledFrom=CastAbilityNoExport]` | ✏️ Renamed |  |
| `OgreBotAPI:CastAbilityNoExport_Relay` | does nothing | `OgreBotAPI.Abilities:CastNoExportRelay` `[fw,ability,calledFrom=OgreBotAPI:CastAbilityNoExport_Relay]` | ✏️ Renamed |  |
| `OgreBotAPI:CastAbilityOnNPC` | does nothing | `OgreBotAPI.Abilities:CastOnNPC` `[fw,ability,mob=target]` | ✏️ Renamed | Not taken any more: `_CalledFrom`. |
| `OgreBotAPI:CastAbilityOnPlayer` | does nothing | `OgreBotAPI.Abilities:CastOnPlayer` `[fw,ability,player=me,calledFrom=AbilityExportCastFromUplinkOnPlayer]` | ✏️ Renamed |  |
| `OgreBotAPI:CastAbilityOnPlayer_Relay` | does nothing | `OgreBotAPI.Abilities:CastOnPlayerRelay` `[fw,ability,player=me]` | ✏️ Renamed |  |
| `OgreBotAPI:CastAbilityOnPlayerInSeconds` | does nothing | `OgreBotAPI.Abilities:CastOnPlayerInSeconds` `[fw,ability,player,seconds,calledFrom=OgreBotAPI]` | ✏️ Renamed | the command must be ONE QUOTED argument - LavishScript ends the outer call at the first `]` otherwise. Unlike `:CastInSeconds`, `Util:DelayedAction` keeps the scheduler's default: a BARE number there is MILLISECONDS, so write `"10s"`. |
| `OgreBotAPI:CastAbilityOnPlayerNoChecks` | does nothing | `OgreBotAPI.Abilities:CastOnPlayerNoChecks` `[fw,ability,player,calledFrom=OgreBotAPI]` | ✏️ Renamed |  |
| `OgreBotAPI:CastBulwarkImmediately` | does nothing | `OgreBotAPI.Abilities:CastBulwark` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:CastedCastOnTheMove` | does nothing | `OgreBotAPI.Abilities:AnnounceCasted` `[fw,caster,seconds=0]` | ⚠️ Arguments changed | Note A |
| `OgreBotAPI:CastGroupWaterBreathing` | does nothing | `OgreBotAPI.Abilities:CastGroupWaterBreathing` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI:CastHOIconID` | does nothing | `OgreBotAPI.Abilities:CastHOIcon` `[fw,iconId,calledFrom=CastHOIcon]` | ✏️ Renamed |  |
| `OgreBotAPI:CastingCastOnTheMove` | does nothing | `OgreBotAPI.Abilities:AnnounceCasting` `[fw,seconds=0]` | ⚠️ Arguments changed | Note A |
| `OgreBotAPI:CastRescue` | does nothing | `OgreBotAPI.Abilities:CastRescue` `[fw,...opts]` | ➡️ Moved |  |
| `OgreBotAPI:Disable_Dispells` | does nothing | `OgreBotAPI.Abilities:SetDispellsEnabled` `[fw,on=TRUE]` | ⚠️ Arguments changed | Pass FALSE as the value argument. |
| `OgreBotAPI:Disable_Interrupts` | does nothing | `OgreBotAPI.Abilities:SetInterruptsEnabled` `[fw,on=TRUE]` | ⚠️ Arguments changed | Pass FALSE as the value argument. |
| `OgreBotAPI:Disable_Stuns` | does nothing | `OgreBotAPI.Abilities:SetStunsEnabled` `[fw,on=TRUE]` | ⚠️ Arguments changed | the OFF half. You must pass `FALSE` after the for-who: `OgreBotAPI.Abilities:SetStunsEnabled["all",FALSE]`. A bare `[FALSE]` puts FALSE in the for-who slot and addresses the call to nobody. Pass FALSE as the value argument. |
| `OgreBotAPI:Enable_Dispells` | does nothing | `OgreBotAPI.Abilities:SetDispellsEnabled` `[fw,on=TRUE]` | ✏️ Renamed |  |
| `OgreBotAPI:Enable_Interrupts` | does nothing | `OgreBotAPI.Abilities:SetInterruptsEnabled` `[fw,on=TRUE]` | ✏️ Renamed |  |
| `OgreBotAPI:Enable_Stuns` | does nothing | `OgreBotAPI.Abilities:SetStunsEnabled` `[fw,on=TRUE]` | ⚠️ Arguments changed | the ON half of a collapsed polarity pair. `OgreBotAPI.Abilities:SetStunsEnabled["all",TRUE]` (TRUE is the default, so `["all"]` also works). Pass TRUE as the value argument. |
| `OgreBotAPI.Get_AbilityInfo` | reads NULL | `OgreBotAPI.Abilities.Info` `[nameOrId,field]` | ✏️ Renamed |  |
| `OgreBotAPI.Get_AbilityInfo_RawData` | reads NULL | `OgreBotAPI.Abilities.InfoRaw` `[nameOrId]` | ✏️ Renamed | Not taken any more: `_Member`. |
| `OgreBotAPI.Get_AbilityShortName` | reads NULL | `OgreBotAPI.Abilities.ShortName` `[nameOrId]` | ✏️ Renamed |  |
| `OgreBotAPI.Get_AbilityTypeID` | reads NULL | `OgreBotAPI.Abilities.TypeID` | ✏️ Renamed |  |
| `OgreBotAPI.Get_AbilityTypeID_Ref` | reads NULL | `OgreBotAPI.Abilities.TypeIDRef` | ✏️ Renamed |  |
| `OgreBotAPI.Get_AbilityVia` | reads NULL | — | ⛔ Not ported yet |  |
| `OgreBotAPI.Get_AbilityVia_ref` | reads NULL | — | ⛔ Not ported yet | as Get_AbilityVia |
| `OgreBotAPI.Get_HOIconAbility` | reads NULL | `OgreBotAPI.Abilities.HOIconAbility` | ✏️ Renamed |  |
| `OgreBotAPI.Get_InterruptID` | reads NULL | `OgreBotAPI.Abilities.InterruptID` | ✏️ Renamed |  |
| `OgreBotAPI.Get_RotationData` | reads NULL | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI.Abilities.RotationData` was a stub that did nothing, and it was removed 2026-10-22. |
| `OgreBotAPI.GetAbilityID` | reads NULL | `OgreBotAPI.Abilities.ID` `[name]` | ✏️ Renamed |  |
| `OgreBotAPI.HaveMaintained` | reads NULL | `OgreBotAPI.Abilities.HaveMaintained` | ➡️ Moved |  |
| `OgreBotAPI:ItemEmbargo_AddRotateTimer` | does nothing | `OgreBotAPI.Abilities:AddEmbargo` `[fw,id,durationSec]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. same verb as `AbilityEmbargo_AddRotateTimer` - they shared one id store and are one verb now. `[id, durationSeconds]`, no for-who. |
| `OgreBotAPI:NoCasting` | does nothing | `OgreBotAPI.Abilities:NoCasting` `[fw]` | ➡️ Moved | Not taken any more: `_TorF`. |
| `OgreBotAPI:Rebuff` | does nothing | `OgreBotAPI.Abilities:Rebuff` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI:ResetFor_Dispells` | does nothing | `OgreBotAPI.Abilities:SetUpForDispells` `[fw,on=TRUE]` | ⚠️ Arguments changed | the OFF half of `SetUpFor_Dispells`: `OgreBotAPI.Abilities:SetUpForDispells["all",FALSE]`. Not the same toggle as `Enable_/Disable_Dispells`, which is the master checkbox. Pass FALSE as the value argument. |
| `OgreBotAPI:ResolveBuffCheck` | does nothing | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI.Abilities:ResolveBuffCheck` was a stub that did nothing, and it was removed 2026-10-22. The resolve buffs were removed from the game, so there is nothing to de-duplicate. |
| `OgreBotAPI.ScrollOf_Get_MaintainedDuration` | reads NULL | `OgreBotAPI.Abilities.ScrollMaintainedDuration` | ✏️ Renamed |  |
| `OgreBotAPI:Set_DisableAllAOEs` | does nothing | `OgreBotAPI.Abilities:SetAOEsDisabled` `[fw,disable=TRUE,-verbose,-allowcounters,-AllowEncounters,-aggressive]` | ✏️ Renamed |  |
| `OgreBotAPI:Set_VampiricRequiem_Cancelling_Active` | does nothing | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI.Abilities:SetVampiricRequiemCancelling` was a stub that did nothing, and it was removed 2026-10-22. |
| `OgreBotAPI:SetUpFor_Dispells` | does nothing | `OgreBotAPI.Abilities:SetUpForDispells` `[fw,on=TRUE]` | ✏️ Renamed |  |
| `OgreBotAPI:Spew_Get_AbilityVia` | does nothing | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI.Abilities:SpewAbilityVia` was a stub that did nothing, and it was removed 2026-10-22. SpewAbility was the one to port instead: it is Abilities:AbilityDetails, the Ability Details window. |
| `OgreBotAPI:SpewAbility` | does nothing | `OgreBotAPI.Abilities:AbilityDetails` `[fw,"name or id"]` | ⚠️ Arguments changed | **Old:** `OgreBotAPI:SpewAbility["Assault"]. New: OgreBotAPI.Abilities:AbilityDetails[all,"Assault"] - the for-who comes first, like every OgreBotAPI method. It opens the Ability Details window instead of printing to the console: the ability's own name selects the rank the bot uses, a rank's full name or an ID selects exactly that rank. Humans type: ogre abilitydetails Assault` |

## OgreBotAPI.Actors

Old names whose job is now in `OgreBotAPI.Actors`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:Actor_Click` | does nothing | `OgreBotAPI.Actors:Click` `[fw,nameOrId,...]` | ✏️ Renamed |  |
| `OgreBotAPI:Actor_ClickQueued` | does nothing | `OgreBotAPI.Actors:ClickQueued` `[fw,nameOrId,...]` | ✏️ Renamed | Not taken any more: `_WaitTime`. |
| `OgreBotAPI:AltarOfTheAncients` | does nothing | `OgreBotAPI.Actors:ClickQueued` `[fw,nameOrId,...]` | ✏️ Renamed |  |
| `OgreBotAPI:ApplyVerb` | does nothing | `OgreBotAPI.Actors:ApplyVerb` `[fw,actor,verb]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. |
| `OgreBotAPI:ApplyVerbForWho` | does nothing | `OgreBotAPI.Actors:ApplyVerb` `[fw,actor,verb]` | ✏️ Renamed |  |
| `OgreBotAPI:ApplyVerbID` | does nothing | `OgreBotAPI.Actors:ApplyVerbID` `[fw,actorId,verb]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. |
| `OgreBotAPI:ApplyVerbIDForWho` | does nothing | `OgreBotAPI.Actors:ApplyVerbID` `[fw,actorId,verb]` | ✏️ Renamed |  |
| `OgreBotAPI:ApplyVerbIDQueuedForWho` | does nothing | `OgreBotAPI.Actors:ApplyVerbIDQueued` `[fw,actorId,verb,waitDs=40]` | ✏️ Renamed |  |
| `OgreBotAPI:ApplyVerbQueuedForWho` | does nothing | `OgreBotAPI.Actors:ApplyVerbQueued` `[fw,actor,verb,waitDs=40]` | ✏️ Renamed |  |
| `OgreBotAPI.CursorActor_Tooltip_Text` | reads NULL | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI.Actors.CursorTooltipText` was a stub that did nothing, and it was removed 2026-10-22. Classic's read the mouse-over actor bubble text off the HUD. |
| `OgreBotAPI.CursorActor_Tooltip_Visible` | reads NULL | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI.Actors.CursorTooltipVisible` was a stub that did nothing, and it was removed 2026-10-22. Classic's read whether that bubble was shown. |
| `OgreBotAPI.GetActorCountByName` | reads NULL | `OgreBotAPI.Actors.CountByName` `[name,...]` | ✏️ Renamed |  |
| `OgreBotAPI.GetActorCountByType` | reads NULL | `OgreBotAPI.Actors.CountByType` `[-distance F,-Type S]` | ✏️ Renamed |  |
| `OgreBotAPI.GetMobID` | reads NULL | `OgreBotAPI.Actors.MobID` `[name]` | ✏️ Renamed |  |
| `OgreBotAPI:HailNPC` | does nothing | `OgreBotAPI.Actors:Hail` `[fw,nameOrId]` | ✏️ Renamed |  |
| `OgreBotAPI.IsAPC` | reads NULL | `OgreBotAPI.Actors.IsPC` `[actorType]` | ✏️ Renamed |  |
| `OgreBotAPI:NPC_CastMonitoring` | does nothing | `OgreBotAPI.Actors:SetCastMonitoring` `[fw, -watch "<mob>" ..., -unwatch "<mob>", -clear, -radius N]` | ⚠️ Arguments changed | **Old:** `OgreBotAPI:NPC_CastMonitoring[all,"Raynax S'Vere",-radius,80]. New: OgreBotAPI.Actors:SetCastMonitoring[all,-watch,"Raynax S'Vere",-radius,80] - every mob needs -watch in front of it. -watch ticks NPC Cast Monitoring as before; -unwatch and -clear drop only what scripts watched (zone and fight-file watches stay); -radius takes 5 to 500 and lasts until the next zone with cast data` |
| `OgreBotAPI.NPCsWithinRange` | reads NULL | `OgreBotAPI.Actors.NPCsWithin` `[distance]` | ⚠️ Arguments changed | **Old:** `${OgreBotAPI.NPCsWithinRange[<ability name>]}. New: ${OgreBotAPI.Actors.NPCsWithin[<radius>]} - pass the AE's effect radius instead of the ability name. Counts every live NPC/NamedNPC whose edge is within that radius of your edge (not only aggro)` |
| `OgreBotAPI:TargetAndDoubleClickActor` | does nothing | `OgreBotAPI.Actors:ClickQueued` `[fw,nameOrId,...]` | ✏️ Renamed | ONE difference to convert deliberately: Classic did `Actor[id,X]:DoTarget` and waited for the target to take BEFORE clicking; `:ClickQueued` clicks without that step. If the caller depends on the target being set afterwards, pair it with `Actors:Target`. `Actors:Click` is the immediate, un-queued form (no cast waits). |

## OgreBotAPI.Ascension

Old names whose job is now in `OgreBotAPI.Ascension`.

**Note A** (4 rows below): as above

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:AscensionEmbargo_Add_DoNotCombo` | does nothing | — | ⛔ Not ported yet |  |
| `OgreBotAPI:AscensionEmbargo_Change_Disable_Status` | does nothing | — | ⛔ Not ported yet | Note A |
| `OgreBotAPI:DisplayMyAscensionCombos` | does nothing | — | ⛔ Not ported yet | Note A |
| `OgreBotAPI:GenerateMyAscensionCombos` | does nothing | — | ⛔ Not ported yet | Note A |
| `OgreBotAPI:GuidedAscension` | does nothing | — | ⛔ Not ported yet | Note A |

## OgreBotAPI.Assist

Old names whose job is now in `OgreBotAPI.Assist`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:Assist` | does nothing | `OgreBotAPI.Assist:Anchor` `[fw, who=me]` | ⚠️ Argument order changed | The for-who moved from argument 2 to argument 1 (first). put the for-who at slot 1, behind the person being assisted. The new form is contract-shaped: `OgreBotAPI.Assist:Anchor["<forwho>","<who to assist>"]`. |
| `OgreBotAPI:AssistForWho` | does nothing | `OgreBotAPI.Assist:Anchor` `[fw, who=me]` | ✏️ Renamed |  |
| `OgreBotAPI.GetAssistID` | reads NULL | `OgreBotAPI.Assist.TargetID` | ✏️ Renamed |  |
| `OgreBotAPI.InControlOfAssisting` | reads NULL | `OgreBotAPI.Assist.InControl` | ✏️ Renamed |  |
| `OgreBotAPI.IsAssisting` | reads NULL | `OgreBotAPI.Assist.IsAssisting` | ➡️ Moved |  |
| `OgreBotAPI:NoTarget` | works | — | ✅ Works as is |  |
| `OgreBotAPI:Prepare_TankSwapping` | works | — | ✅ Works as is |  |
| `OgreBotAPI:ResetFor_Intercept` | works | — | ✅ Works as is |  |
| `OgreBotAPI:SetUpFor_Intercept` | works | — | ✅ Works as is |  |
| `OgreBotAPI:Target` | works | — | ✅ Works as is |  |
| `OgreBotAPI:UpdateNPCTarget` | works | `OgreBotAPI:UpdateNPCTarget` `[fw]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. |
| `OgreBotAPI.ValidKillTarget` | works | — | ✅ Works as is |  |

## OgreBotAPI.AutoHunt

Old names whose job is now in `OgreBotAPI.AutoHunt`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:AutoHunt_AddPath` | does nothing | — | ⛔ Not ported yet | Deleted rather than moved so a stub does not carry a lie. They return as :AddPoint / :ClearPoints when the walker lands. |
| `OgreBotAPI:AutoHunt_AddPoint` | does nothing | — | ⛔ Not ported yet | as AutoHunt_AddPath |
| `OgreBotAPI:AutoHunt_CheckHP` | does nothing | `OgreBotAPI.AutoHunt:SetCheckHP` `[fw,n]` | ✏️ Renamed |  |
| `OgreBotAPI:AutoHunt_CheckMana` | does nothing | `OgreBotAPI.AutoHunt:SetCheckMana` `[fw,n]` | ✏️ Renamed |  |
| `OgreBotAPI:AutoHunt_ClearPoints` | does nothing | — | ⛔ Not ported yet | as AutoHunt_AddPath |
| `OgreBotAPI:AutoHunt_ScanRadius` | does nothing | `OgreBotAPI.AutoHunt:SetScanRadius` `[fw,n]` | ✏️ Renamed |  |

## OgreBotAPI.AutoTarget

Old names whose job is now in `OgreBotAPI.AutoTarget`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:AutoTarget_AddActor` | does nothing | `OgreBotAPI.AutoTarget:AddActor` `[fw, name, minHP=0, checkCollision=FALSE, aggroOnGroupOnly=TRUE, maxHP=0, aggroOnNonFighterOnly=FALSE, aggroOnNotMe=FALSE, keepLast=FALSE]` | ✏️ Renamed |  |
| `OgreBotAPI:AutoTarget_Clear` | does nothing | `OgreBotAPI.AutoTarget:Clear` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:AutoTarget_ClearActors` | does nothing | `OgreBotAPI.AutoTarget:Clear` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:AutoTarget_Disable` | does nothing | `OgreBotAPI.AutoTarget:Suppress` `[fw, reason]` | ✏️ Renamed | suppression is keyed: `:Suppress["all","YOUR_KEY"]`, released by the same key. It is not a boolean. |
| `OgreBotAPI.AutoTarget_Disabled` | reads NULL | `OgreBotAPI.AutoTarget.Suppressed` `[key]` | ✏️ Renamed |  |
| `OgreBotAPI:AutoTarget_Enable` | does nothing | `OgreBotAPI.AutoTarget:Release` `[fw, reason]` | ✏️ Renamed | releases a keyed suppression: `:Release["all","YOUR_KEY"]`. |
| `OgreBotAPI.AutoTarget_Enabled` | reads NULL | `OgreBotAPI.AutoTarget.Enabled` | ✏️ Renamed |  |
| `OgreBotAPI:AutoTarget_RemoveActor` | does nothing | `OgreBotAPI.AutoTarget:RemoveActor` `[fw, name]` | ✏️ Renamed |  |
| `OgreBotAPI:AutoTarget_SetRescanTime` | does nothing | `OgreBotAPI.AutoTarget:SetRescanTime` `[fw, n=50]` | ✏️ Renamed |  |
| `OgreBotAPI:AutoTarget_SetScanHeight` | does nothing | `OgreBotAPI.AutoTarget:SetScanHeight` `[fw, n=5]` | ✏️ Renamed |  |
| `OgreBotAPI:AutoTarget_SetScanRadius` | does nothing | `OgreBotAPI.AutoTarget:SetScanRadius` `[fw, n=50]` | ✏️ Renamed |  |

## OgreBotAPI.Bot

Old names whose job is now in `OgreBotAPI.Bot`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:CampToDesktop` | does nothing | `OgreBotAPI.Bot:CampToDesktop` `[fw,loginOnly=FALSE]` | ➡️ Moved |  |
| `OgreBotAPI:DisplayAvailableSetups` | does nothing | `OgreBotAPI.Bot:ListSetups` `[fw]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. |
| `OgreBotAPI:End_Bot` | does nothing | `OgreBotAPI.Bot:End` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:ExitClient` | does nothing | `OgreBotAPI.Bot:ExitClient` `[fw,seconds=30]` | ➡️ Moved |  |
| `OgreBotAPI:FlushQueued` | does nothing | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI.Bot:FlushQueued` was a stub that did nothing, and it was removed 2026-10-22. |
| `OgreBotAPI.Get_ScriptBaseName` | reads NULL | `OgreBotAPI.Bot.ScriptBaseName` `[path,removeExtension=TRUE]` | ✏️ Renamed |  |
| `OgreBotAPI.Get_Turbo` | reads NULL | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI.Bot.Turbo` was a stub that did nothing, and it was removed 2026-10-22. The new bot does not set LavishScript turbo. |
| `OgreBotAPI:Initialize` | does nothing | `OgreBotAPI.Bot:Initialize` `[fw,...]` | ➡️ Moved |  |
| `OgreBotAPI:OnDeactivate` | does nothing | `OgreBotAPI.Bot:OnDeactivate` `[fw]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. |
| `OgreBotAPI:Pause` | does nothing | `OgreBotAPI.Bot:Pause` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI.Paused` | reads NULL | `OgreBotAPI.Bot.Paused` | ➡️ Moved |  |
| `OgreBotAPI.QueuedCommands` | reads NULL | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI.Bot.QueuedCommands` was a stub that did nothing, and it was removed 2026-10-22. The new bot has no LavishScript command queue to report. |
| `OgreBotAPI:Reload_Bot` | does nothing | `OgreBotAPI.Bot:Reload` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:Resume` | does nothing | `OgreBotAPI.Bot:Resume` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI:SetUpFor` | does nothing | `OgreBotAPI.Bot:SetUpFor` `[fw,what="",restart=TRUE]` | ➡️ Moved |  |
| `OgreBotAPI:Update_Turbo` | does nothing | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI.Bot:SetTurbo` was a stub that did nothing, and it was removed 2026-10-22. |

## OgreBotAPI.CastStack

Old names whose job is now in `OgreBotAPI.CastStack`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:AbilityTag_AddRotateTagTimer` | does nothing | `OgreBotAPI.CastStack:HoldTag` `[fw,tag,duration,type,-m]` | ⚠️ Arguments changed | The arguments are different: Classic took `(string _ForWho, string _TagName, uint _Duration, ... Args)`, the new call takes `[fw,tag,duration,type,-m]`. |
| `OgreBotAPI.AbilityTag_GetTagAllowTimeRemaining` | reads NULL | `OgreBotAPI.CastStack.TagAllowRemaining` `[tag]` | ✏️ Renamed | was a stub returning FALSE, read as "expired". |
| `OgreBotAPI.AbilityTag_GetTagEmbargoTimeRemaining` | reads NULL | `OgreBotAPI.CastStack.TagEmbargoRemaining` `[tag]` | ✏️ Renamed | was a stub returning FALSE, read as "expired". It answers the clock, not liveness - a tag coupled to a maintained buff reports 0 and is still active. |
| `OgreBotAPI:AbilityTag_ResetAbilityTagAllow` | does nothing | `OgreBotAPI.CastStack:ClearAllow` `[fw,tag]` | ✏️ Renamed |  |
| `OgreBotAPI:AbilityTag_ResetAbilityTagEmbargo` | does nothing | `OgreBotAPI.CastStack:ClearEmbargo` `[fw,tag]` | ✏️ Renamed |  |
| `OgreBotAPI:AbilityTag_ResetAllAbilityTagAllows` | does nothing | `OgreBotAPI.CastStack:ClearAllAllows` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:AbilityTag_ResetAllAbilityTagEmbargos` | does nothing | `OgreBotAPI.CastStack:ClearAllEmbargos` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:ChangeCastStackListBoxItem` | does nothing | `OgreBotAPI.CastStack:SetEntry` `[fw,ability,TRUE\|FALSE\|toggle,silent=FALSE]` | ✏️ Renamed |  |
| `OgreBotAPI:ChangeCastStackListBoxItemByTag` | does nothing | `OgreBotAPI.CastStack:SetEntryByTag` `[fw,tag,TRUE\|FALSE\|toggle,partial=FALSE,silent=FALSE]` | ✏️ Renamed |  |

## OgreBotAPI.Client

Old names whose job is now in `OgreBotAPI.Client`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:ChangeRadarYAxis` | does nothing | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI.Client:SetRadarYAxis` was a stub that did nothing, and it was removed 2026-10-22. Its console row -ChangeRadarYAxis went with it. |
| `OgreBotAPI:ResetCameraAngle` | does nothing | `OgreBotAPI.Client:ResetCamera` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:Set_CameraPitch` | does nothing | `OgreBotAPI.Client:SetCameraPitch` `[fw,pitch=0,endInFirstPerson=FALSE]` | ✏️ Renamed |  |
| `OgreBotAPI:SetMousePosition` | does nothing | `OgreBotAPI.Client:SetMousePosition` `[fw,x,y]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. |
| `OgreBotAPI:SetMousePosition_Middle` | does nothing | `OgreBotAPI.Client:SetMousePositionMiddle` `[fw]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. |

## OgreBotAPI.Combat

Old names whose job is now in `OgreBotAPI.Combat`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:AddNoOffensiveOn` | does nothing | `OgreBotAPI.Combat:AddNoOffensive` `[fw,mobName,exactOnly=TRUE]` | ✏️ Renamed | Left out, the name must be the target's whole name - as Classic matched. Pass FALSE to match any name that contains it. |
| `OgreBotAPI.bNoReqBowAbilities` | reads NULL | `OgreBotAPI.Combat.NoReqBowAbilities` | ✏️ Renamed |  |
| `OgreBotAPI.CheckNoDefensiveOn` | reads NULL | `OgreBotAPI.Combat.NoDefensive` | ✏️ Renamed |  |
| `OgreBotAPI.CheckNoOffensiveOn` | reads NULL | `OgreBotAPI.Combat.NoOffensive` | ✏️ Renamed |  |
| `OgreBotAPI.CheckNoReqBowAbilities` | reads NULL | `OgreBotAPI.Combat.NoReqBowAbilities` | ✏️ Renamed |  |
| `OgreBotAPI:ClearNoOffensiveOn` | does nothing | `OgreBotAPI.Combat:ClearNoOffensive` `[fw,...]` | ✏️ Renamed |  |
| `OgreBotAPI:Countdown` | does nothing | `OgreBotAPI.Combat:Countdown` `[fw,seconds=10,...]` | ➡️ Moved |  |
| `OgreBotAPI.InCombat` | reads NULL | `OgreBotAPI.Combat.InCombat` | ➡️ Moved |  |
| `OgreBotAPI.IsReady` | reads NULL | `OgreBotAPI.Combat.IsReady` | ➡️ Moved |  |
| `OgreBotAPI.MaybeAnotherTime_CheckNoOffensive` | reads NULL | `OgreBotAPI.Combat.MaybeAnotherTime` | ✏️ Renamed |  |
| `OgreBotAPI.NoOffensiveOn` | reads NULL | `OgreBotAPI.Combat.NoOffensive` | ✏️ Renamed |  |
| `OgreBotAPI:SetNoDefensive` | does nothing | `OgreBotAPI.Combat:SetNoDefensive` `[fw,on,reason]` | ⚠️ Arguments changed | The arguments are different: Classic took `(string _ForWho=all, bool _Value=TRUE)`, the new call takes `[fw,on,reason]`. |
| `OgreBotAPI:SetNoReqBowAbilities` | does nothing | `OgreBotAPI.Combat:SetNoReqBowAbilities` `[fw,on=TRUE]` | ➡️ Moved |  |
| `OgreBotAPI.ThreatFighterIgnoreList` | reads NULL | `OgreBotAPI.Combat:ThreatIgnoreList` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:ThreatFighterIgnoreList_Add` | does nothing | `OgreBotAPI.Combat:ThreatIgnoreAdd` `[fw,name]` | ⚠️ Arguments changed | The arguments are different: Classic took `(string _ForWho="all", ... Args)`, the new call takes `[fw,name]`. |
| `OgreBotAPI:ThreatFighterIgnoreList_Clear` | does nothing | `OgreBotAPI.Combat:ThreatIgnoreClear` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:ThreatFighterIgnoreList_List` | does nothing | `OgreBotAPI.Combat:ThreatIgnoreList` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:ThreatFighterIgnoreList_Remove` | does nothing | `OgreBotAPI.Combat:ThreatIgnoreRemove` `[fw,name...]` | ✏️ Renamed |  |
| `OgreBotAPI.Zoning` | reads NULL | `OgreBotAPI.Combat.Zoning` | ➡️ Moved |  |

## OgreBotAPI.Comms

Old names whose job is now in `OgreBotAPI.Comms`.

**Note A** (4 rows below): Nothing is broken today - there is exactly ONE group, so nothing can leave it and nothing can become unreachable. `oc` cannot substitute: it rides a FIXED group (`"relayGroup": "ogre_everquest2"`, one per game), so a session that moved to another group cannot be called back by a broadcast confined to the one it left. If fleet partitioning is ever wanted, mutable groups and cross-group addressing must land TOGETHER. See the 'Relay groups - PARKED' entry in.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:Announce_AddEntry` | does nothing | `OgreBotAPI.Comms:AddAnnounce` `[fw,ability,to,text]` | ✏️ Renamed |  |
| `OgreBotAPI:ConversationBubble` | does nothing | `OgreBotAPI.Comms:ConversationBubble` `[fw,...]` | ➡️ Moved |  |
| `OgreBotAPI:ConversationBubbleSpew` | does nothing | `OgreBotAPI.Comms:SpewConversationBubbles` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:ExecuteEvent` | does nothing | `OgreBotAPI.Comms:ExecuteEvent` `[fw,name,...]` | ➡️ Moved |  |
| `OgreBotAPI:ExecuteEvent_JSON` | does nothing | `OgreBotAPI.Comms:ExecuteEventJSON` `[fw,name,json]` | ⚠️ Arguments changed | The arguments are different: Classic took `(string _ForWho="all", string _EventName, ... Args)`, the new call takes `[fw,name,json]`. |
| `OgreBotAPI:InjectChat` | does nothing | `OgreBotAPI.Comms:InjectChat` `[fw,chat=Nothing]` | ➡️ Moved |  |
| `OgreBotAPI:Message` | does nothing | `OgreBotAPI.Comms:Message` `[fw,text,-tab name...,-sound ding\|alarm]` | ⚠️ Arguments changed | moved to `OgreBotAPI.Comms:Message` - renders on THIS session only. Classic's positional `noise, NoiseToPlay` became FLAGS after the text (2026-10-16): `-sound ding` (Classic `TRUE` / `Default`) or `-sound alarm` (Classic `Loud`) - both PLAY (ding.wav / chatalarm.wav, Ogre/Common/OgreSounds) - and `-tab <name>` (repeatable) also shows the line in that OgreConsole tab. A leftover positional `TRUE` is just ignored (no sound). SIGNATURE CHANGED - drop the positional noise / NoiseToPlay pair; for a sound put `"-sound","ding"` (Classic TRUE / Default) or `"-sound","alarm"` (Classic Loud) after the text. `"-tab","<name>"` also shows the line in that OgreConsole tab. |
| `OgreBotAPI:Message_NT` | does nothing | `OgreBotAPI.Comms:Message` `[fw,text,-tab name...,-sound ding\|alarm]` | ⚠️ Arguments changed | identical to `Message` - the "no timestamp" distinction stopped existing when the stamp was removed. Classic's positional `noise, NoiseToPlay` became FLAGS after the text (2026-10-16): `-sound ding` (Classic `TRUE` / `Default`) or `-sound alarm` (Classic `Loud`) - both PLAY (ding.wav / chatalarm.wav, Ogre/Common/OgreSounds) - and `-tab <name>` (repeatable) also shows the line in that OgreConsole tab. A leftover positional `TRUE` is just ignored (no sound). SIGNATURE CHANGED - drop the positional noise / NoiseToPlay pair; for a sound put `"-sound","ding"` (Classic TRUE / Default) or `"-sound","alarm"` (Classic Loud) after the text. `"-tab","<name>"` also shows the line in that OgreConsole tab. |
| `OgreBotAPI:Message_Relay` | does nothing | `OgreBotAPI.Comms:Broadcast` `[fw,text,-tab name...,-sound ding\|alarm]` | ⚠️ Arguments changed | renamed to `:Broadcast`. `:Message` renders locally; `:Broadcast` reaches the fleet. Classic's positional `noise, NoiseToPlay` became FLAGS after the text (2026-10-16): `-sound ding` (Classic `TRUE` / `Default`) or `-sound alarm` (Classic `Loud`) - both PLAY (ding.wav / chatalarm.wav, Ogre/Common/OgreSounds) - and `-tab <name>` (repeatable) also shows the line in that OgreConsole tab. A leftover positional `TRUE` is just ignored (no sound). SIGNATURE CHANGED - drop the positional noise / NoiseToPlay pair; for a sound put `"-sound","ding"` (Classic TRUE / Default) or `"-sound","alarm"` (Classic Loud) after the text. `"-tab","<name>"` also shows the line in that OgreConsole tab. |
| `OgreBotAPI:OgreIRC_AuthIfInRaid` | does nothing | `OgreBotAPI.Comms:IrcAuthIfInRaid` `[nick,toon]` | ✏️ Renamed |  |
| `OgreBotAPI:OptNum` | does nothing | `OgreBotAPI.Comms:ConversationBubble` `[fw,...]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. |
| `OgreBotAPI:Pushover` | does nothing | `OgreBotAPI.Comms:Pushover` `[fw,message...,-title t,-priority n]` | ➡️ Moved |  |
| `OgreBotAPI:Send_Tell` | does nothing | `OgreBotAPI.Comms:SendTell` `[fw,target,message]` | ✏️ Renamed |  |
| `OgreBotAPI:SetRelayGroup` | does nothing | — | ⛔ Not ported yet | Note A |
| `OgreBotAPI:SetRelayGroup_Relay` | does nothing | — | ⛔ Not ported yet | Note A |
| `OgreBotAPI:SetRelayGroupToDefault` | does nothing | — | ⛔ Not ported yet | Note A |
| `OgreBotAPI:SetRelayGroupToDefault_Relay` | does nothing | — | ⛔ Not ported yet | Note A |
| `OgreBotAPI:Spew_RelayGroup` | does nothing | `OgreBotAPI.Comms:SpewRelayGroup` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:TTS` | does nothing | `OgreBotAPI.Comms:TTS` `[fw,text]` | ➡️ Moved |  |
| `OgreBotAPI.UplinkName` | reads NULL | `OgreBotAPI.Comms.UplinkName` | ➡️ Moved |  |

## OgreBotAPI.Consumables

Old names whose job is now in `OgreBotAPI.Consumables`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:Check_Familiar` | does nothing | `OgreBotAPI.Consumables:CheckFamiliar` `[fw,...]` | ✏️ Renamed |  |
| `OgreBotAPI:CheckMercenaryTraining` | does nothing | `OgreBotAPI.Consumables:CheckMercenaryTraining` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI:CheckMountTraining` | does nothing | `OgreBotAPI.Consumables:CheckMountTraining` `[fw,force=FALSE]` | ➡️ Moved |  |
| `OgreBotAPI:CoV` | does nothing | `OgreBotAPI.Consumables:CoV` `[fw,...]` | ➡️ Moved | Not taken any more: `_ToonOption`, `_AllowSameZone`. |
| `OgreBotAPI:Drink_Alcohol` | does nothing | `OgreBotAPI.Consumables:DrinkAlcohol` `[fw,...]` | ✏️ Renamed |  |
| `OgreBotAPI:Force_MountOff` | does nothing | `OgreBotAPI.Consumables:MountDown` `[fw]` | ✏️ Renamed | same action-queue flow shape as `:MountUp`, holding {Movement} and gated on `!Me.IsMoving` exactly as Classic's f_ForceMountOff is - one `summon_mount` toggle instead of two, since the command is a toggle. |
| `OgreBotAPI:Force_MountOn` | does nothing | `OgreBotAPI.Consumables:MountUp` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:Get_FoodDrink` | does nothing | `OgreBotAPI.Consumables:ReplenishFoodDrink` `[fw,...]` | ✏️ Renamed | Classic's member RETURNED the chosen name; the new verb acts on it rather than handing it back |
| `OgreBotAPI:Get_StatPotions` | does nothing | `OgreBotAPI.Consumables:ReplenishStatPotions` `[fw,...]` | ✏️ Renamed | as Get_FoodDrink - the new verb acts, it does not return the name |
| `OgreBotAPI:Heartstone_RekindleBond` | does nothing | `OgreBotAPI.Consumables:RekindleHeartstone` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:Mercenary_AddMercenaries` | does nothing | `OgreBotAPI.Consumables:AddMercenaries` `[fw,...]` | ✏️ Renamed |  |
| `OgreBotAPI:ScrollOf` | does nothing | `OgreBotAPI.Consumables:ScrollOf` `[fw,name=Prowess,cancelIfDurationLessThan=0,useBest=FALSE]` | ➡️ Moved |  |
| `OgreBotAPI:Summon_Familiar` | does nothing | `OgreBotAPI.Consumables:SummonFamiliar` `[fw,...]` | ✏️ Renamed |  |

## OgreBotAPI.Cures

Old names whose job is now in `OgreBotAPI.Cures`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:AutoCure` | does nothing | `OgreBotAPI.Cures:Request` `[fw,victim,kinds...]` | ✏️ Renamed |  |
| `OgreBotAPI:AutoCurse` | does nothing | `OgreBotAPI.Cures:RequestCurse` `[fw,victim]` | ✏️ Renamed |  |
| `OgreBotAPI:AutoGroupCure` | does nothing | `OgreBotAPI.Cures:RequestGroupWatch` `[fw]` | ✏️ Renamed | Not taken any more: `_Toon`. |
| `OgreBotAPI:AutoItemCure` | does nothing | `OgreBotAPI.Cures:ItemCure` `[fw,type]` | ⚠️ Arguments changed | The arguments are different: Classic took `(string _ForWho, ... Args)`, the new call takes `[fw,type]`. |
| `OgreBotAPI:CancelDetrimental` | does nothing | `OgreBotAPI.Cures:CancelDetrimental` `[fw,mainId,backdropId]` | ➡️ Moved |  |
| `OgreBotAPI.Count_CursesInGroup` | reads NULL | `OgreBotAPI.Cures.GroupCurses` | ✏️ Renamed |  |
| `OgreBotAPI:Cursed` | does nothing | `OgreBotAPI.Cures:RequestCurse` `[fw,victim]` | ✏️ Renamed |  |
| `OgreBotAPI:Cursed_Relay` | does nothing | `OgreBotAPI.Cures:RequestCurse` `[fw,victim]` | ✏️ Renamed |  |
| `OgreBotAPI.DetrimentalInfo` | reads NULL | `OgreBotAPI.Cures.Detrimental` `[main=0,back=0,actorId=0,field=exists]` | ✏️ Renamed |  |
| `OgreBotAPI.DetrimentalInfo_ref` | reads NULL | `OgreBotAPI.Cures.Detrimental` `[main=0,back=0,actorId=0,field=exists]` | ⚠️ Arguments changed | Watch the icon pair order. Classic's `Object_IconIDs` declares the BACKDROP icon FIRST: `variable Object_IconIDs X=A B` means main=B, backdrop=A. The new call takes `[main,back,actorId,field]`, so `X=815 33803` becomes `Detrimental[33803,815,<actorId>]`. Copying the numbers left-to-right compiles, runs, and asks about a detriment nobody has. If the script's own comment names the icons the other way round, Classic read them backdrop-first anyway - convert what Classic actually checked, and say so in your report. |
| `OgreBotAPI.DetrimentalInfo_ref_String` | reads NULL | `OgreBotAPI.Cures.DetrimentalText` `[main=0,back=0,actorId=0,field=exists]` | ⚠️ Arguments changed | Watch the icon pair order. Classic's `Object_IconIDs` declares the BACKDROP icon FIRST: `variable Object_IconIDs X=A B` means main=B, backdrop=A. The new call takes `[main,back,actorId,field]`, so `X=815 33803` becomes `Detrimental[33803,815,<actorId>]`. Copying the numbers left-to-right compiles, runs, and asks about a detriment nobody has. If the script's own comment names the icons the other way round, Classic read them backdrop-first anyway - convert what Classic actually checked, and say so in your report. |
| `OgreBotAPI.DetrimentalInfo_String` | reads NULL | `OgreBotAPI.Cures.DetrimentalText` `[main=0,back=0,actorId=0,field=exists]` | ✏️ Renamed |  |
| `OgreBotAPI:Disable_Cures` | does nothing | `OgreBotAPI.Cures:SetEnabled` `[fw,on=TRUE]` | ⚠️ Arguments changed | Pass FALSE as the value argument. |
| `OgreBotAPI:Enable_Cures` | does nothing | `OgreBotAPI.Cures:SetEnabled` `[fw,on=TRUE]` | ✏️ Renamed |  |
| `OgreBotAPI:Get_CurePotions` | does nothing | `OgreBotAPI.Cures:ReplenishPotions` `[fw,all\|arcane\|elemental\|noxious\|trauma]` | ✏️ Renamed | as Get_FoodDrink - the new verb acts, it does not return the name |
| `OgreBotAPI.Get_CursedID` | reads NULL | `OgreBotAPI.Cures.CursedID` `[-archetype X...,-uncurable,-uncurableonly,-GroupOnly]` | ✏️ Renamed |  |
| `OgreBotAPI.Get_CursedID_ArchetypeCheck` | reads NULL | `OgreBotAPI.Cures.CursedID` `[-archetype X...,-uncurable,-uncurableonly,-GroupOnly]` | ✏️ Renamed | was a stub returning FALSE. Use `.CursedID` with the `-archetype` option, which is what this was meant to do. pass the -archetype option |
| `OgreBotAPI.Get_GroupCurseCount` | reads NULL | `OgreBotAPI.Cures.GroupCurses` | ✏️ Renamed |  |
| `OgreBotAPI.Get_GroupUncurableCurseCount` | reads NULL | `OgreBotAPI.Cures.GroupUncurable` | ✏️ Renamed |  |
| `OgreBotAPI.Get_GroupUncurableCurses_JSON` | reads NULL | `OgreBotAPI.Cures.GroupUncurableIDs` | ✏️ Renamed |  |
| `OgreBotAPI.Get_RaidCurableOrUncurableCurses_JSON` | reads NULL | `OgreBotAPI.Cures.RaidCursedIDs` | ✏️ Renamed |  |
| `OgreBotAPI.Get_RaidCurseCount` | reads NULL | `OgreBotAPI.Cures.RaidCurses` | ✏️ Renamed |  |
| `OgreBotAPI.Get_RaidUncurableCurseCount` | reads NULL | `OgreBotAPI.Cures.RaidUncurable` | ✏️ Renamed |  |
| `OgreBotAPI.Get_RaidUncurableCurses_JSON` | reads NULL | `OgreBotAPI.Cures.RaidUncurableIDs` | ✏️ Renamed |  |
| `OgreBotAPI.Get_Uncurable` | reads NULL | `OgreBotAPI.Cures.Uncurable` `[type="Cursed", -GroupOnly]` | ✏️ Renamed |  |
| `OgreBotAPI:GroupCure` | does nothing | `OgreBotAPI.Cures:RequestGroup` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:GroupCure_Relay` | does nothing | `OgreBotAPI.Cures:RequestGroup` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI.HaveSickness` | reads NULL | `OgreBotAPI.Cures.HaveSickness` | ➡️ Moved | was a stub returning FALSE - it answered "no" to every caller. Ported. |
| `OgreBotAPI.NumGroupWithCurses` | reads NULL | `OgreBotAPI.Cures.GroupCurses` | ✏️ Renamed |  |
| `OgreBotAPI.NumRaidWithCurses` | reads NULL | `OgreBotAPI.Cures.RaidCurses` | ✏️ Renamed |  |

## OgreBotAPI.Debug

Old names whose job is now in `OgreBotAPI.Debug`.

**Note A** (4 rows below): The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI.bDebugLoading` | reads NULL | `OgreBotAPI.Debug.DebugLoading` | ✏️ Renamed |  |
| `OgreBotAPI.CheckVersion` | reads NULL | `OgreBotAPI.Debug.CheckVersion` `[fw,compareTo]` | ➡️ Moved |  |
| `OgreBotAPI.DebugMessage` | reads NULL | `OgreBotAPI.Debug.DebugPrefix` | ✏️ Renamed |  |
| `OgreBotAPI:Echo` | does nothing | `OgreBotAPI.Debug:Echo` `[fw,text,text2=""]` | ⚠️ Arguments changed | Note A |
| `OgreBotAPI.Get_DebugLoading` | reads NULL | `OgreBotAPI.Debug.DebugLoading` | ✏️ Renamed |  |
| `OgreBotAPI:Get_Faction` | does nothing | `OgreBotAPI.Debug:BroadcastStat` `[fw,type,value,where=oc]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. Classic's second argument was a spewstat OBJECT to fill; the new verb emits the rows itself. The READ half, `Debug.SpewStat`, was a stub and was removed 2026-10-22 - reading a stat back into a script is not ported. |
| `OgreBotAPI:SetDebugLoading` | does nothing | `OgreBotAPI.Debug:SetDebugLoading` `[fw,on=TRUE]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. gained a for-who; argument 0 *was* the bool. |
| `OgreBotAPI:SetDebugMode` | does nothing | `OgreBotAPI.Debug:SetDebugMode` `[fw,on=TRUE]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. gained a for-who; argument 0 *was* the bool. |
| `OgreBotAPI:Spew_BoZ_Research` | does nothing | `OgreBotAPI.Debug:SpewResearchWindow` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:Spew_InternalVariables` | does nothing | `OgreBotAPI.Debug:SpewInternalVariables` `[fw]` | ⚠️ Arguments changed | Note A |
| `OgreBotAPI:Spew_Variables` | does nothing | `OgreBotAPI.Debug:SpewVariables` `[fw]` | ⚠️ Arguments changed | Note A |
| `OgreBotAPI.SpewStat` | reads NULL | `OgreBotAPI.Debug:BroadcastStat` `[fw,type,value,where=oc]` | ⚠️ Arguments changed | Note A |
| `OgreBotAPI:SpewSubscriptionStatus` | does nothing | `OgreBotAPI.Debug:SpewSubscriptionStatus` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI.Version` | reads NULL | `OgreBotAPI.Debug.Version` | ➡️ Moved |  |

## OgreBotAPI.Events

Old names whose job is now in `OgreBotAPI.Events`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:ChatEvent_AddEntry` | does nothing | `OgreBotAPI.Events:AddChatEntry` `[fw,text,oc,ding,code]` | ✏️ Renamed |  |
| `OgreBotAPI:ChatEvent_RemoveEntry` | does nothing | `OgreBotAPI.Events:RemoveChatEntry` `[fw,text=all]` | ✏️ Renamed |  |
| `OgreBotAPI:DespawnEvent_AddEntry` | does nothing | `OgreBotAPI.Events:AddDespawnEntry` `[fw,text,oc,ding,code]` | ✏️ Renamed |  |
| `OgreBotAPI:DespawnEvent_RemoveEntry` | does nothing | `OgreBotAPI.Events:RemoveDespawnEntry` `[fw,text=all]` | ✏️ Renamed |  |
| `OgreBotAPI:OgreEvent_AskReply` | does nothing | IC file: the `groupQuery` step (ic-actions/09-groupQuery.md) - counts, allYes / anyYes / allNo / anyNo, per-member flags, raw answers, ready-made for-who lists. Script: the same engine - ${OgreBotAPI.Comms.GroupQuery[&lt;fw&gt;, -question, &lt;question&gt;, ...]} starts it and reads as its id; then ${OgreBotAPI.Comms.GroupQuery.Done[id]} / .Result[id] (JSON, the same names), or the event OgreEvent_GroupQueryDone(id, json). | ➡️ Lives somewhere else |  |
| `OgreBotAPI:SpawnEvent_AddEntry` | does nothing | `OgreBotAPI.Events:AddSpawnEntry` `[fw,text,oc,ding,code]` | ✏️ Renamed |  |
| `OgreBotAPI:SpawnEvent_RemoveEntry` | does nothing | `OgreBotAPI.Events:RemoveSpawnEntry` `[fw,text=all]` | ✏️ Renamed |  |

## OgreBotAPI.ForWho

Old names whose job is now in `OgreBotAPI.ForWho`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:Alias_AddEntry` | does nothing | `OgreBotAPI.ForWho:AddAlias` `[fw,alias,value,noRaid=FALSE]` | ✏️ Renamed |  |
| `OgreBotAPI:Alias_ChangeEntry` | does nothing | `OgreBotAPI.ForWho:ChangeAlias` `[fw,from,to,silent=FALSE]` | ✏️ Renamed |  |
| `OgreBotAPI:Alias_ChangeEntryAlias` | does nothing | `OgreBotAPI.ForWho:RenameAlias` `[fw,from,to,silent=FALSE]` | ✏️ Renamed |  |
| `OgreBotAPI:Alias_RemoveEntry` | does nothing | `OgreBotAPI.ForWho:RemoveAlias` `[fw,name\|all]` | ✏️ Renamed |  |
| `OgreBotAPI.CommandForMe` | reads NULL | `OgreBotAPI.ForWho.Me` | ✏️ Renamed | was a duplicate of `ForWho.Me`. Use `${OgreBotAPI.ForWho.Me["<expr>"]}`. |
| `OgreBotAPI:ForceAliasUpdate` | does nothing | `OgreBotAPI.ForWho:ForceUpdate` `[fw]` | ✏️ Renamed | `:ForceUpdate` is a deliberate no-op: the native store resolves aliases live, so there is no cache to force. |
| `OgreBotAPI.Get_Alias` | reads NULL | `OgreBotAPI.ForWho.Alias` `[name]` | ✏️ Renamed | An alias that names nobody present reads empty now. Classic handed the alias text back unchanged, the new member returns `""` ( case Alias, ResolveAliasName). A line that uses the result as a name - `Actor[exactname,${...Alias[@healer1]}]` - now gets an empty name: check `${OgreBotAPI.ForWho.Alias[@healer1].Length}` first. |
| `OgreBotAPI.Get_Aliases_JSON` | reads NULL | `OgreBotAPI.ForWho.AliasesJSON` | ✏️ Renamed |  |

## OgreBotAPI.HOs

Old names whose job is now in `OgreBotAPI.HOs`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:Clear_Allow_HOICon` | does nothing | `OgreBotAPI.HOs:ClearAllowIcon` `[fw,icon]` | ✏️ Renamed |  |
| `OgreBotAPI:Clear_Allow_HOICons` | does nothing | `OgreBotAPI.HOs:ClearAllowIcons` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:Clear_Disable_HOICon` | does nothing | `OgreBotAPI.HOs:ClearDisableIcon` `[fw,icon]` | ✏️ Renamed |  |
| `OgreBotAPI:Clear_Disable_HOICons` | does nothing | `OgreBotAPI.HOs:ClearDisableIcons` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI.DoHO_Get_Enabled` | reads NULL | `OgreBotAPI.HOs.DoEnabled` | ✏️ Renamed |  |
| `OgreBotAPI.DoHO_Get_HOerID` | reads NULL | `OgreBotAPI.HOs.DoHOerID` | ✏️ Renamed |  |
| `OgreBotAPI.DoHO_Get_Primed` | reads NULL | `OgreBotAPI.HOs.DoPrimed` | ✏️ Renamed |  |
| `OgreBotAPI.DoHo_Get_TargetID` | reads NULL | `OgreBotAPI.HOs.DoTargetID` | ✏️ Renamed |  |
| `OgreBotAPI:DoHO_Reset` | does nothing | `OgreBotAPI.HOs:DoReset` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:DoHO_Set_Enable` | does nothing | `OgreBotAPI.HOs:DoSetEnabled` `[fw,on=TRUE,option...]` | ✏️ Renamed |  |
| `OgreBotAPI:DoHO_Setup` | does nothing | `OgreBotAPI.HOs:DoSetup` `[fw,...]` | ✏️ Renamed |  |
| `OgreBotAPI:HO_Advance` | does nothing | `OgreBotAPI.HOs:Advance` `[fw,...]` | ✏️ Renamed |  |
| `OgreBotAPI:HO_Cancel_Starter` | does nothing | `OgreBotAPI.HOs:CancelStarter` `[fw]` | ✏️ Renamed | Not taken any more: `_CalledFrom`. |
| `OgreBotAPI.HO_Class_Available` | reads NULL | `OgreBotAPI.HOs.WheelClassAvailable` `[class]` | ✏️ Renamed |  |
| `OgreBotAPI:HO_Start` | does nothing | `OgreBotAPI.HOs:Start` `[fw,...]` | ✏️ Renamed |  |
| `OgreBotAPI:HO_Starter` | does nothing | `OgreBotAPI.HOs:Starter` `[fw,...]` | ✏️ Renamed |  |
| `OgreBotAPI:HO_Starter_Advance` | does nothing | `OgreBotAPI.HOs:Starter` `[fw,...]` | ✏️ Renamed |  |
| `OgreBotAPI.HO_Starter_Class` | reads NULL | `OgreBotAPI.HOs.StarterClass` | ✏️ Renamed |  |
| `OgreBotAPI.HO_Starter_Class_Available` | reads NULL | `OgreBotAPI.HOs.StarterClassAvailable` `[class]` | ✏️ Renamed |  |
| `OgreBotAPI.HO_Starter_Visible` | reads NULL | `OgreBotAPI.HOs.StarterVisible` | ✏️ Renamed |  |
| `OgreBotAPI.HO_TargetID` | reads NULL | `OgreBotAPI.HOs.TargetID` | ✏️ Renamed |  |
| `OgreBotAPI.HO_Visible` | reads NULL | `OgreBotAPI.HOs.Visible` | ✏️ Renamed |  |
| `OgreBotAPI:HO_Wheel_Advance` | does nothing | `OgreBotAPI.HOs:Advance` `[fw,...]` | ✏️ Renamed |  |
| `OgreBotAPI.HO_Wheel_Class_Available` | reads NULL | `OgreBotAPI.HOs.WheelClassAvailable` `[class]` | ✏️ Renamed |  |
| `OgreBotAPI.HO_Wheel_Name` | reads NULL | `OgreBotAPI.HOs.WheelName` | ✏️ Renamed |  |
| `OgreBotAPI.HO_Wheel_Visible` | reads NULL | `OgreBotAPI.HOs.WheelVisible` | ✏️ Renamed |  |
| `OgreBotAPI:Restore_SetUpFor_HOs` | does nothing | `OgreBotAPI.HOs:RestoreSetUpFor` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:Set_Allow_HOICon` | does nothing | `OgreBotAPI.HOs:AllowIcon` `[fw,icon]` | ✏️ Renamed |  |
| `OgreBotAPI:Set_Disable_HOICon` | does nothing | `OgreBotAPI.HOs:DisableIcon` `[fw,icon]` | ✏️ Renamed |  |
| `OgreBotAPI:SetUpFor_HOs` | does nothing | `OgreBotAPI.HOs:SetUpFor` `[fw]` | ✏️ Renamed |  |

## OgreBotAPI.Inventory

Old names whose job is now in `OgreBotAPI.Inventory`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI.AdornmentIconIDColour` | reads NULL | `OgreBotAPI.Inventory.AdornmentColour` `[iconId]` | ✏️ Renamed |  |
| `OgreBotAPI:ApplyTempAdorn` | does nothing | `OgreBotAPI.Inventory:PoPTempAdorns` `[fw,...]` | ✏️ Renamed | Not taken any more: `_Slot`. |
| `OgreBotAPI:AutoConsumeTemporaryFamiliarExperience` | does nothing | `OgreBotAPI.Inventory:AutoConsumeFamiliarXP` `[fw,...]` | ✏️ Renamed |  |
| `OgreBotAPI:AutoConsumeTemporaryMountTrainingReduction` | does nothing | `OgreBotAPI.Inventory:AutoConsumeMountTraining` `[fw,...]` | ✏️ Renamed |  |
| `OgreBotAPI:AutoConsumeTemporaryResearchReduction` | does nothing | `OgreBotAPI.Inventory:AutoConsumeResearch` `[fw,...]` | ✏️ Renamed |  |
| `OgreBotAPI.bAPIPackPonyRunning` | reads NULL | `OgreBotAPI.Inventory.PackPonyRunning` | ✏️ Renamed |  |
| `OgreBotAPI:Change_FoodDrinkAutoConsume` | does nothing | `OgreBotAPI.Inventory:AutoConsumeFoodDrink` `[fw,...]` | ✏️ Renamed | the argument after the for-who is true\|false\|toggle |
| `OgreBotAPI:Change_StatPotionsAutoConsume` | does nothing | `OgreBotAPI.Inventory:AutoConsumeStatPotions` `[fw,...]` | ✏️ Renamed | Not taken any more: `_PotionName`. |
| `OgreBotAPI:ChangeBeltAdorn` | does nothing | `OgreBotAPI.Inventory:ChangeBeltAdorn` `[fw,...]` | ➡️ Moved | Not taken any more: `_Unequip`, `_SkipAdornMoving`. |
| `OgreBotAPI:CheckGear` | does nothing | `OgreBotAPI.Inventory:CheckGear` `[fw,...]` | ➡️ Moved |  |
| `OgreBotAPI:CheckPackPony` | does nothing | `OgreBotAPI.Inventory:CheckPackPony` `[fw,forceCheck=FALSE]` | ➡️ Moved |  |
| `OgreBotAPI:Consume_Familiars` | does nothing | `OgreBotAPI.Inventory:ConsumeFamiliars` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:Consume_Status_Ignots` | does nothing | `OgreBotAPI.Inventory:ConsumeStatusIngots` `[fw,amount=99999]` | ✏️ Renamed |  |
| `OgreBotAPI:Consume_Status_Ingots` | does nothing | `OgreBotAPI.Inventory:ConsumeStatusIngots` `[fw,amount=99999]` | ✏️ Renamed |  |
| `OgreBotAPI:Consume_Status_Tokens` | does nothing | `OgreBotAPI.Inventory:ConsumeStatusTokens` `[fw,amount=99999]` | ✏️ Renamed |  |
| `OgreBotAPI:ConsumeDeityBaubles` | does nothing | `OgreBotAPI.Inventory:ConsumeDeityBaubles` `[fw,...]` | ➡️ Moved |  |
| `OgreBotAPI:ConsumeItems_ProcessList` | does nothing | `OgreBotAPI.Inventory:ConsumeList` `[fw,-fc,-all,-st]` | ✏️ Renamed |  |
| `OgreBotAPI.ConvertAdornToRemoveSlot` | reads NULL | `OgreBotAPI.Inventory.AdornToRemoveSlot` `[adorn]` | ✏️ Renamed |  |
| `OgreBotAPI.ConvertAdornToSlot` | reads NULL | `OgreBotAPI.Inventory.AdornToSlot` `[adorn,slot=21]` | ✏️ Renamed |  |
| `OgreBotAPI:DestroyItem` | does nothing | `OgreBotAPI.Inventory:DestroyItem` `[fw,itemName]` | ➡️ Moved | Not taken any more: `_Charges`. |
| `OgreBotAPI:DestroyItem_NoChecks` | does nothing | `OgreBotAPI.Inventory:DestroyItem` `[fw,itemName]` | ✏️ Renamed |  |
| `OgreBotAPI:EquipCharm` | does nothing | `OgreBotAPI.Inventory:EquipCharm` `[fw,...]` | ➡️ Moved |  |
| `OgreBotAPI.EquipmentSlotAvailable` | reads NULL | `OgreBotAPI.Inventory.SlotAvailable` `[slot name]` | ✏️ Renamed | **Old:** `${OgreBotAPI.EquipmentSlotAvailable[cloak]}. New: ${OgreBotAPI.Inventory.SlotAvailable[cloak]} - TRUE when the item in that slot can be used now. Names (any case): primary, secondary, head, cloak, chest, shoulders, forearms, hands, legs, feet, left_ring, right_ring, ears, ears2, neck, left_wrist, right_wrist, ranged, ammo, waist, activate1, activate2, event_slot, food, drink. Pass the name: there is no default slot` |
| `OgreBotAPI.EquipmentSlotNumAvailable` | reads NULL | `OgreBotAPI.Inventory.SlotNumAvailable` `[slot number 1-22]` | ✏️ Renamed | **Old:** `${OgreBotAPI.EquipmentSlotNumAvailable[20]}. New: ${OgreBotAPI.Inventory.SlotNumAvailable[20]} - Classic's numbers 1-22 (1 primary, 2 secondary, 3 head, 4 chest, ... 19 waist, 20 cloak, 21 activate1, 22 activate2), not ${Me.Equipment[N]}'s. Pass the number: there is no default` |
| `OgreBotAPI:ExamineAllOfItem` | does nothing | `OgreBotAPI.Inventory:ExamineAll` `[fw,item...]` | ✏️ Renamed |  |
| `OgreBotAPI:ExamineInventoryItem` | does nothing | `OgreBotAPI.Inventory:Examine` `[fw,item=DoesNotExist]` | ✏️ Renamed |  |
| `OgreBotAPI.Get_AdornmentColour` | reads NULL | `OgreBotAPI.Inventory.AdornmentColour` `[iconId]` | ✏️ Renamed |  |
| `OgreBotAPI.Get_APIPackPonyRunning` | reads NULL | `OgreBotAPI.Inventory.PackPonyRunning` | ✏️ Renamed |  |
| `OgreBotAPI.Get_CurrentImmunityRune` | reads NULL | `OgreBotAPI.Inventory.CurrentImmunityRune` | ✏️ Renamed |  |
| `OgreBotAPI.Get_EquipmentModifierValue` | reads NULL | `OgreBotAPI.Inventory.SlotModifier` `[slot,modifier]` | ✏️ Renamed |  |
| `OgreBotAPI.Get_PackPonyRunning` | reads NULL | `OgreBotAPI.Inventory.PackPonyRunning` | ✏️ Renamed |  |
| `OgreBotAPI.Get_SlotNum_EQ2UIPageSlotNames` | reads NULL | `OgreBotAPI.Inventory.SlotUIName` `[n=1]` | ✏️ Renamed |  |
| `OgreBotAPI.Get_SlotNum_To_SlotNames` | reads NULL | `OgreBotAPI.Inventory.SlotName` `[n=1]` | ✏️ Renamed |  |
| `OgreBotAPI:Initialize_AdornmentInfo` | does nothing | `OgreBotAPI.Inventory:InitAdornmentInfo` `[fw]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. |
| `OgreBotAPI.IsAdornmentColour` | reads NULL | `OgreBotAPI.Inventory.IsAdornmentColour` `[iconId,colour]` | ➡️ Moved |  |
| `OgreBotAPI.ItemCount` | reads NULL | `OgreBotAPI.Inventory.Count` `[itemName,exact\|contains]` | ⚠️ Arguments changed | Write OgreBotAPI.Inventory.Count[&lt;name&gt;,contains] - Classic matched a PART of the name (=-); `exact` (the default) needs the whole name. Both count every stack in the bags and the Harvest Bag. |
| `OgreBotAPI:KronoWindowCheck` | does nothing | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI.Inventory:KronoWindowCheck` was a stub that did nothing, and it was removed 2026-10-22. OgreBotAPI.Inventory:RedeemKrono already covers it: its flow (ogre::redeemkrono,) includes the result-window check. |
| `OgreBotAPI:Overseer_SpewMissionsInInventory` | does nothing | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI.Inventory:SpewOverseerMissions` was a stub that did nothing, and it was removed 2026-10-22. |
| `OgreBotAPI:PoP_TempAdorns` | does nothing | `OgreBotAPI.Inventory:PoPTempAdorns` `[fw,...]` | ✏️ Renamed | Not taken any more: `_Overwrite`. |
| `OgreBotAPI:RedeemKrono` | does nothing | `OgreBotAPI.Inventory:RedeemKrono` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI.Slot_SlotNames` | reads NULL | `OgreBotAPI.Inventory.SlotName` `[n=1]` | ✏️ Renamed |  |
| `OgreBotAPI.SlotNum_EQ2UIPageSlotNames` | reads NULL | `OgreBotAPI.Inventory.SlotUIName` `[n=1]` | ✏️ Renamed |  |
| `OgreBotAPI.SlotNum_SlotNames` | reads NULL | `OgreBotAPI.Inventory.SlotName` `[n=1]` | ✏️ Renamed |  |
| `OgreBotAPI:Spew_SlotNum_To_SlotNames` | does nothing | `OgreBotAPI.Inventory:SpewSlotNames` `[fw]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. |
| `OgreBotAPI:Unpack` | does nothing | `OgreBotAPI.Inventory:Unpack` `[fw,item,...]` | ⚠️ Arguments changed | **Old:** `OgreBotAPI:Unpack[<fw>,<item>,<choice>]`<br>**New:** `OgreBotAPI.Inventory:Unpack[<fw>,<item>,-pick,<choice>]`<br>The reward choice is a flag now; a bare third argument is refused with a line naming -pick. -qty &lt;N&gt; unpacks N, -all keeps going until none is left, -pick &lt;number \| name \| lowest&gt; takes that reward when the window offers a choice (lowest = the one the character holds fewest of in its bags; a tie goes to the first in window order). An already-open reward window is waited out, up to 10 s. |
| `OgreBotAPI:Unpack_Consume_Familiars` | does nothing | `OgreBotAPI.Inventory:UnpackConsumeFamiliars` `[fw,...]` | ✏️ Renamed |  |
| `OgreBotAPI:Unpack_EmpyralStones` | does nothing | `OgreBotAPI.Inventory:Unpack` `[fw,item,...]` | ⚠️ Arguments changed | **Old:** `OgreBotAPI:Unpack_EmpyralStones[<fw>,<choice=Lowest>]`<br>**New:** `OgreBotAPI.Inventory:Unpack[<fw>,"Empyral Stones",-all,-pick,lowest]`<br>Or -pick,"&lt;stone name&gt;" for one kind. The same flags unpack any item. |
| `OgreBotAPI:Unpack_Familiars` | does nothing | `OgreBotAPI.Inventory:UnpackFamiliars` `[fw,...]` | ✏️ Renamed |  |
| `OgreBotAPI:Unpack_PlanarStones` | does nothing | `OgreBotAPI.Inventory:Unpack` `[fw,item,...]` | ⚠️ Arguments changed | **Old:** `OgreBotAPI:Unpack_PlanarStones[<fw>,<choice=Lowest>]`<br>**New:** `OgreBotAPI.Inventory:Unpack[<fw>,"Planar Stones",-all,-pick,lowest]`<br>Or -pick,"&lt;stone name&gt;" for one kind. The same flags unpack any item. |
| `OgreBotAPI:Unpack_Quantity` | does nothing | `OgreBotAPI.Inventory:Unpack` `[fw,item,...]` | ⚠️ Arguments changed | **Old:** `OgreBotAPI:Unpack_Quantity[<fw>,<item>,<N>,<choice>]`<br>**New:** `OgreBotAPI.Inventory:Unpack[<fw>,<item>,-qty,<N>,-pick,<choice>]`<br>Leave -pick and its value out when there is no choice. The old "examine" item name (the item in the open examine window) is gone: name the item. |
| `OgreBotAPI:UseItem` | does nothing | `OgreBotAPI.Inventory:Use` `[fw,item,...]` | ✏️ Renamed |  |
| `OgreBotAPI:UseItem_Relay` | does nothing | `OgreBotAPI.Inventory:UseRelay` `[fw,item]` | ✏️ Renamed |  |
| `OgreBotAPI:UseItemOnPlayer` | does nothing | `OgreBotAPI.Inventory:UseOnPlayer` `[fw,item,player=me,...]` | ✏️ Renamed |  |
| `OgreBotAPI:UseItemOnPlayer_Relay` | does nothing | `OgreBotAPI.Inventory:UseOnPlayerRelay` `[fw,item,player=me]` | ✏️ Renamed |  |

## OgreBotAPI.Loot

Old names whose job is now in `OgreBotAPI.Loot`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:ChangeLootOptions` | does nothing | `OgreBotAPI.Loot:SetOptions` `[fw,token,...]` | ✏️ Renamed | NOT `Loot:SetAutoLootMode` - that is only this toon's auto-loot dropdown. A family nobody names is left alone, so you can set the method without disturbing rarity. |
| `OgreBotAPI.Get_LootWindowID` | reads NULL | `OgreBotAPI.Loot.WindowID` | ✏️ Renamed |  |
| `OgreBotAPI:HandleLootWindow` | does nothing | — | ⛔ Not ported yet |  |
| `OgreBotAPI.LootWindowExists` | reads NULL | `OgreBotAPI.Loot.WindowExists` | ✏️ Renamed |  |
| `OgreBotAPI:LootWindowLootAll` | does nothing | `OgreBotAPI.Loot:LootAll` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:ResetActorsLooted` | does nothing | `OgreBotAPI.Loot:ResetLootedActors` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:SetAutoLootMode` | does nothing | `OgreBotAPI.Loot:SetAutoLootMode` `[fw,n]` | ➡️ Moved | Not taken any more: `_Silent`. |
| `OgreBotAPI:SmartLoot_BuildToonItemsToBeZeroed` | does nothing | `OgreBotAPI.Loot:BuildToonItemsToBeZeroed` `[fw,toon,item,...]` | ✏️ Renamed |  |
| `OgreBotAPI:SmartLoot_ProcessToonItemsToBeZeroed` | does nothing | `OgreBotAPI.Loot:ProcessToonItemsToBeZeroed` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:SmartLoot_ReloadDataFromFile` | does nothing | `OgreBotAPI.Loot:Reload` `[fw]` | ✏️ Renamed |  |

## OgreBotAPI.Merchant

Old names whose job is now in `OgreBotAPI.Merchant`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:BuyFromMerchant` | does nothing | `OgreBotAPI.Merchant:Buy` `[fw,item,qty=1]` | ✏️ Renamed |  |
| `OgreBotAPI:OpenAndBuyFromMerchant` | does nothing | `OgreBotAPI.Merchant:OpenAndBuy` `[fw,merchant,item,qty=1]` | ✏️ Renamed |  |
| `OgreBotAPI:OpenAndBuyFromMerchantXTimes` | does nothing | `OgreBotAPI.Merchant:OpenAndBuyXTimes` `[fw,merchant,item,qty,times]` | ✏️ Renamed |  |
| `OgreBotAPI:RepairGear` | does nothing | `OgreBotAPI.Merchant:Repair` `[fw,...]` | ✏️ Renamed |  |
| `OgreBotAPI:SellToMerchant` | does nothing | `OgreBotAPI.Merchant:Sell` `[fw,item,qty=1]` | ✏️ Renamed |  |

## OgreBotAPI.Movement

Old names whose job is now in `OgreBotAPI.Movement`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:AscensionEmbargo_Remove_DoNotCombo` | does nothing | — | ⛔ Not ported yet | as above |
| `OgreBotAPI:AutoHunt_RemovePoint` | does nothing | — | ⛔ Not ported yet | as AutoHunt_AddPath |
| `OgreBotAPI:AutoRun` | does nothing | `OgreBotAPI.Movement:AutoRun` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI:CallGH` | does nothing | `OgreBotAPI.Movement:CallGH` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI:Come2Me` | does nothing | `OgreBotAPI.Movement:Come2Me` `[fw,toWho=me,precision=3]` | ⚠️ Argument order changed | The for-who moved from argument 2 to argument 1 (first). |
| `OgreBotAPI:Crouch` | does nothing | `OgreBotAPI.Movement:Crouch` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI:Evac` | does nothing | `OgreBotAPI.Movement:Evac` `[fw,mode=""]` | ➡️ Moved |  |
| `OgreBotAPI:FaceActor` | does nothing | `OgreBotAPI.Movement:FaceActor` `[fw,nameOrId]` | ➡️ Moved |  |
| `OgreBotAPI:FaceAngle` | does nothing | `OgreBotAPI.Movement:FaceAngle` `[fw,angle]` | ➡️ Moved |  |
| `OgreBotAPI:FaceLoc` | does nothing | `OgreBotAPI.Movement:FaceLoc` `[fw,x,y,z]` | ➡️ Moved |  |
| `OgreBotAPI:FlyDown` | does nothing | `OgreBotAPI.Movement:FlyDown` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI:FlyStop` | does nothing | `OgreBotAPI.Movement:FlyStop` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI:FlyUp` | does nothing | `OgreBotAPI.Movement:FlyUp` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI:ForceFollow` | does nothing | `OgreBotAPI.Movement:ForceFollow` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI.GettingToGH` | reads NULL | `OgreBotAPI.Movement.GettingToGH` | ➡️ Moved |  |
| `OgreBotAPI:GetToConcentration` | does nothing | `OgreBotAPI.Movement:GetToConcentration` `[fw,concentration=4]` | ➡️ Moved |  |
| `OgreBotAPI:GetToGH` | does nothing | `OgreBotAPI.Movement:GetToGH` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI:HoldUp` | does nothing | `OgreBotAPI.Movement:HoldUp` `[fw]` | ➡️ Moved |  |
| `call OgreBotAPI.HouseWindowToGH` | does nothing | `OgreBotAPI.Movement:GetToGH` `[fw]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. the house-window leg is one route inside the ported driver, not a separate verb |
| `OgreBotAPI:JoustIn` | does nothing | `OgreBotAPI.Movement:JoustIn` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI:JoustOff` | does nothing | `OgreBotAPI.Movement:JoustOff` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI:JoustOn` | does nothing | `OgreBotAPI.Movement:JoustOn` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI:JoustOut` | does nothing | `OgreBotAPI.Movement:JoustOut` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI:Jump` | does nothing | `OgreBotAPI.Movement:Jump` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI:LandFlyingMount` | does nothing | `OgreBotAPI.Movement:LandFlyingMount` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI:Move2Area` | does nothing | `OgreBotAPI.Movement:Move2Area` `[fw,x,y,z,precision=3]` | ⚠️ Arguments changed | **Old:** `OgreBotAPI:Move2Area[x,z,who,precision] (Classic's second number is the Z). New: OgreBotAPI.Movement:Move2Area[who,x,y,z,precision] - the for-who comes first and y is new but ignored (a ground move: pass ${Me.Y} or 0). Only toons that have a target move, as in Classic` |
| `OgreBotAPI:Move2AreaNoTarget` | does nothing | `OgreBotAPI.Movement:Move2AreaNoTarget` `[fw,x,y,z,precision=3]` | ⚠️ Arguments changed | **Old:** `OgreBotAPI:Move2AreaNoTarget[x,z,who,precision] (Classic's second number is the Z). New: OgreBotAPI.Movement:Move2AreaNoTarget[who,x,y,z,precision] - the for-who comes first and y is new but ignored (a ground move: pass ${Me.Y} or 0). Moves with or without a target, as in Classic` |
| `OgreBotAPI:NoMove` | does nothing | `OgreBotAPI.Movement:StopFollow` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:OFolDecDistance` | does nothing | `OgreBotAPI.Movement:FollowDistanceDown` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:OFolIncDistance` | does nothing | `OgreBotAPI.Movement:FollowDistanceUp` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:Pull` | does nothing | `OgreBotAPI.Movement:Pull` `[fw]` | ➡️ Moved | Not taken any more: `_Named`. |
| `OgreBotAPI:Remove_Prepare_TankSwapping` | works | — | ✅ Works as is |  |
| `OgreBotAPI:RemoveNoOffensiveOn` | works | — | ✅ Works as is |  |
| `OgreBotAPI:RunWalk` | does nothing | `OgreBotAPI.Movement:SetRunMode` `[fw,run]` | ⚠️ Arguments changed | SIGNATURE CHANGED - add TRUE (run) or FALSE (walk) after the for-who; there is no toggle. |
| `OgreBotAPI:Set_CampSpotJump_Handle` | does nothing | `OgreBotAPI.Movement:JumpRoute` `[fw,start,jump,end,completed="",flag...]` | ✏️ Renamed | Same arguments in the same order; each option is its own argument. The jump distance and max time Classic kept on Obj_CampSpotJump (Set_JumpDistance / Set_MaxTimer) are per-route options now - see the Obj_CampSpotJump rows. |
| `OgreBotAPI:Stand` | does nothing | `OgreBotAPI.Movement:Stand` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI:Waypoint` | does nothing | `OgreBotAPI.Movement:Waypoint` `[fw,x,y,z]` | ➡️ Moved |  |

## OgreBotAPI.OneOff

Old names whose job is now in `OgreBotAPI.OneOff`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:ArcannaseEffigyOfRebirth` | works | — | ✅ Works as is |  |
| `OgreBotAPI:C4M` | does nothing | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI:C4M` was a stub that did nothing, and it was removed 2026-10-22. Classic's was a debug echo of whether a for-who string matches this session. |
| `OgreBotAPI:DoVDebuff` | works | — | ✅ Works as is |  |
| `OgreBotAPI:DoVDebuff_Half` | works | — | ✅ Works as is |  |
| `OgreBotAPI:GO_CryptofDalnir_WizardsDen_EventHeroic_King` | does nothing | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI:GO_CryptofDalnir_WizardsDen_EventHeroic_King` was a stub that did nothing, and it was removed 2026-10-22. The fight is the encounter file (The Gooblin). |
| `OgreBotAPI:HQEar_Recheck` | does nothing | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI:HQEar_Recheck` was a stub that did nothing, and it was removed 2026-10-22. The HQEar (goblin earring) subsystem was declined 2026-08-26 and its console verbs deleted then. |
| `OgreBotAPI:HQEar_ReEquipOriginalEar` | does nothing | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI:HQEar_ReEquipOriginalEar` was a stub that did nothing, and it was removed 2026-10-22. Same declined HQEar subsystem. |
| `OgreBotAPI:HQEar_ReportStuckEar` | does nothing | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI:HQEar_ReportStuckEar` was a stub that did nothing, and it was removed 2026-10-22. Same declined HQEar subsystem. |
| `OgreBotAPI.NPCUnkillableBug` | works | — | ✅ Works as is |  |
| `OgreBotAPI:RO_FSD_BB_Brutas_DoNotNeedColdWater` | does nothing | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI:RO_FSD_BB_Brutas_DoNotNeedColdWater` was a stub that did nothing, and it was removed 2026-10-22. The fight is the encounter file (Brutas the). |
| `OgreBotAPI:RO_FSD_BB_Brutas_DoNotNeedColdWater_Relay` | does nothing | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI:RO_FSD_BB_Brutas_DoNotNeedColdWater_Relay` was a stub that did nothing, and it was removed 2026-10-22. It only relayed to RO_FSD_BB_Brutas_DoNotNeedColdWater, removed with it. |
| `OgreBotAPI:RO_FSD_BB_Brutas_NeedColdWater` | does nothing | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI:RO_FSD_BB_Brutas_NeedColdWater` was a stub that did nothing, and it was removed 2026-10-22. The fight is the encounter file (Brutas the, events Brutas_NeedWater / Brutas_NoWater). |
| `OgreBotAPI:RO_FSD_BB_Brutas_NeedColdWater_Relay` | does nothing | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI:RO_FSD_BB_Brutas_NeedColdWater_Relay` was a stub that did nothing, and it was removed 2026-10-22. It only relayed to RO_FSD_BB_Brutas_NeedColdWater, removed with it. |
| `OgreBotAPI.RoR_Epic_AbilityID` | reads NULL | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI.RoR_Epic_AbilityID` was a stub that did nothing, and it was removed 2026-10-22. Classic's read the class's Renewal of Ro epic ability; a fight file casts an ability by its id. |
| `OgreBotAPI.RoR_Epic_Available` | reads NULL | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI.RoR_Epic_Available` was a stub that did nothing, and it was removed 2026-10-22. Classic's read the class's Renewal of Ro epic ability; a fight file casts an ability by its id. |
| `OgreBotAPI:RoR_Epic_ChangeInCastStack` | does nothing | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI:RoR_Epic_ChangeInCastStack` was a stub that did nothing, and it was removed 2026-10-22. Classic's ticked or unticked the class RoR epic in the cast stack. |
| `OgreBotAPI.RoR_Epic_Ready` | reads NULL | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI.RoR_Epic_Ready` was a stub that did nothing, and it was removed 2026-10-22. Classic's read the class's Renewal of Ro epic ability; a fight file casts an ability by its id. |
| `OgreBotAPI:Scribe_Empyral` | works | — | ✅ Works as is |  |
| `OgreBotAPI:Special` | works | — | ✅ Works as is |  |
| `OgreBotAPI:Test` | does nothing | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI:Test` was a stub that did nothing, and it was removed 2026-10-22. Classic's was a debug echo of a variable by name. |
| `OgreBotAPI:TestAll` | works | `OgreBotAPI:TestAll` `[fw]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. |

## OgreBotAPI.Options

Old names whose job is now in `OgreBotAPI.Options`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:ChangeOgreBotUIOption` | does nothing | `OgreBotAPI.Options:Set` `[fw, (id,value)...]` | ✏️ Renamed |  |
| `OgreBotAPI:F2PWindow_SetOptions` | works | — | ✅ Works as is |  |
| `OgreBotAPI:LoadProfile` | does nothing | `OgreBotAPI.Options:LoadProfile` `[fw, name, tabOnly]` | ➡️ Moved |  |
| `OgreBotAPI:OLD_ChangeOgreBotUIOption` | does nothing | — | ⛔ Not ported yet | Use Options:Set. |
| `OgreBotAPI:PopulatePCOptionLists` | does nothing | — | ⛔ Not ported yet |  |
| `OgreBotAPI:UplinkOptionChange` | does nothing | `OgreBotAPI.Options:Set` `[fw, (id,value)...]` | ✏️ Renamed |  |

## OgreBotAPI.Overseer

Old names whose job is now in `OgreBotAPI.Overseer`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:Overseer_AddAgentsToCollection` | does nothing | `OgreBotAPI.Overseer:AddAgents` `[fw,destroy=TRUE]` | ✏️ Renamed |  |
| `OgreBotAPI:Overseer_AutoAddOverseerQuests` | does nothing | `OgreBotAPI.Overseer:AutoAddQuests` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:Overseer_CheckQuests` | does nothing | `OgreBotAPI.Overseer:CheckQuests` `[fw]` | ✏️ Renamed |  |

## OgreBotAPI.Pet

Old names whose job is now in `OgreBotAPI.Pet`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:PetAssist` | does nothing | `OgreBotAPI.Pet:Assist` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:PetAttack` | does nothing | `OgreBotAPI.Pet:Attack` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:PetGetLost` | does nothing | `OgreBotAPI.Pet:GetLost` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:PetOff` | does nothing | `OgreBotAPI.Pet:Off` `[fw]` | ✏️ Renamed |  |

## OgreBotAPI.Position

Old names whose job is now in `OgreBotAPI.Position`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI.GameDistanceToActor` | reads NULL | `OgreBotAPI.Position.DistanceToActor` `[nameOrId=Target]` | ✏️ Renamed |  |
| `OgreBotAPI.GetActorModelSize` | reads NULL | `OgreBotAPI.Position.ActorModelSize` `[nameOrId]` | ✏️ Renamed |  |
| `OgreBotAPI.GetFarthestActorFrom` | reads NULL | `OgreBotAPI.Position.FarthestActorFrom` `[anchorNameOrId,actorName,minDist=20]` | ✏️ Renamed | was a dead stub returning FALSE, so callers acted on actor 0, which is the player. Ported. |
| `OgreBotAPI.GetFarthestActorFrom_ref` | reads NULL | `OgreBotAPI.Position.FarthestActorFrom` `[anchorNameOrId,actorName,minDist=20]` | ✏️ Renamed |  |
| `OgreBotAPI.GetFarthestGroupDistance` | reads NULL | `OgreBotAPI.Position.FarthestGroupDistance` | ✏️ Renamed |  |
| `OgreBotAPI.GetMyModelSize` | reads NULL | `OgreBotAPI.Position.MyModelSize` | ✏️ Renamed |  |
| `OgreBotAPI.PointAtAngle` | reads NULL | `OgreBotAPI.Position.AtAngle` `[angle,actorNameOrId,dist=3]` | ✏️ Renamed |  |
| `OgreBotAPI.PointAtAngleNoSize` | reads NULL | `OgreBotAPI.Position.AtAngleNoTargetSize` | ✏️ Renamed |  |
| `OgreBotAPI.PointTowardDist` | reads NULL | `OgreBotAPI.Position.Toward` `[fx,fy,fz,tx,ty,tz,dist=15]` | ✏️ Renamed |  |
| `OgreBotAPI.RoomID` | reads NULL | — | ⛔ Not ported yet | Needs a different mechanism than a temporary label. |

## OgreBotAPI.Quest

Old names whose job is now in `OgreBotAPI.Quest`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:AcceptQuest` | does nothing | `OgreBotAPI.Quest:Accept` `[fw,questName=""]` | ✏️ Renamed |  |
| `OgreBotAPI.ActorHasQuest` | reads NULL | `OgreBotAPI.Quest.ActorHas` `[actorId=0]` | ✏️ Renamed |  |
| `OgreBotAPI:CheckKunarkAscendingRequirements` | does nothing | `OgreBotAPI.Quest:CheckKunarkAscending` `[fw,...]` | ✏️ Renamed |  |
| `OgreBotAPI:CheckToShareQuest` | does nothing | `OgreBotAPI.Quest:CheckToShare` `[fw,zoneName]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. |
| `OgreBotAPI:CompareQuestUpdate` | does nothing | `OgreBotAPI.Quest:CompareUpdate` `[fw,questName]` | ✏️ Renamed |  |
| `OgreBotAPI:DailyEtherealMissionReset` | does nothing | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI.Quest:DailyMissionReset` was a stub that did nothing, and it was removed 2026-10-22. |
| `OgreBotAPI:DeleteQuest` | does nothing | `OgreBotAPI.Quest:Delete` `[fw,questName]` | ✏️ Renamed |  |
| `OgreBotAPI:DisplayEtherealMissionInfo` | does nothing | `OgreBotAPI.Quest:ShowMissionInfo` `[fw,...]` | ✏️ Renamed |  |
| `OgreBotAPI.GetDeityPoints` | does nothing (stub) | `OgreBotAPI.Quest.DeityPoints` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI.HaveQuest` | reads NULL | `OgreBotAPI.Quest.Have` `[name]` | ✏️ Renamed |  |
| `OgreBotAPI.LootQuestion` | reads NULL | `OgreBotAPI.Quest.SkipShinies` | ✏️ Renamed |  |
| `OgreBotAPI:ShareAllMissions` | does nothing | `OgreBotAPI.Quest:ShareAllMissions` `[fw,...]` | ➡️ Moved |  |
| `OgreBotAPI:ShareMission` | does nothing | `OgreBotAPI.Quest:ShareMission` `[fw,questName]` | ➡️ Moved |  |
| `OgreBotAPI:ShareQuest` | does nothing | `OgreBotAPI.Quest:ShareQuest` `[fw,questName]` | ➡️ Moved |  |
| `OgreBotAPI:ShareQuestWhenAble` | does nothing | `OgreBotAPI.Quest:ShareQuestWhenAble` `[fw,questName,zoneName]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. |
| `OgreBotAPI:ShowWikiForQuest` | does nothing | `OgreBotAPI.Quest:ShowWiki` `[fw,name=""]` | ✏️ Renamed |  |
| `OgreBotAPI:Spew_MissionTimerInfo` | does nothing | `OgreBotAPI.Quest:SpewMissionTimers` `[fw,...searches]` | ✏️ Renamed |  |

## OgreBotAPI.Roster

Old names whose job is now in `OgreBotAPI.Roster`.

**Note A** (3 rows below): arguments swapped - old `[search, mode, rank]`, new `[mode, search, rank]`. The first two arguments are swapped.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:CheckMemberLevel` | does nothing | `OgreBotAPI.Roster:CheckMemberLevel` `[fw,onlyNonMembers=FALSE]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. gained a for-who; argument 0 *was* the bool and is now the for-who. |
| `OgreBotAPI:ClassInfo_ChangeValue` | reads NULL | `OgreBotAPI.Roster:SetClassValue` `[fw,member,value]` | ✏️ Renamed |  |
| `OgreBotAPI.ClassInfo_GetValue` | reads NULL | `${ISXOgreEQ2.Class.Is[fighter]}   (any archetype, class or subclass name; this session only)` | ➡️ Lives somewhere else |  |
| `OgreBotAPI.CountGroupBy` | reads NULL | `OgreBotAPI.Roster.CountGroupBy` | ➡️ Moved |  |
| `OgreBotAPI.CountRaidBy` | reads NULL | `OgreBotAPI.Roster.CountRaidBy` | ➡️ Moved |  |
| `OgreBotAPI:Disband` | does nothing | `OgreBotAPI.Roster:Disband` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI:FlagNextPerson` | does nothing | `OgreBotAPI.Roster:FlagNextPerson` `[fw,mark=1]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it.<br>Not taken any more: `_Via`. |
| `OgreBotAPI:FlagToon` | does nothing | `OgreBotAPI.Roster:Flag` `[fw,n=1]` | ✏️ Renamed |  |
| `OgreBotAPI:FlagToonNextPerson` | does nothing | `OgreBotAPI.Roster:FlagNextPerson` `[fw,mark=1]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. gained a for-who; argument 0 *was* the mark. |
| `OgreBotAPI.Get_Archetype` | reads NULL | `OgreBotAPI.Roster.ArchetypeOf` `[class]` | ✏️ Renamed |  |
| `OgreBotAPI.Get_BaseClass` | reads NULL | `OgreBotAPI.Roster.BaseClassOf` `[class]` | ✏️ Renamed |  |
| `OgreBotAPI.Get_Role` | reads NULL | `OgreBotAPI.Roster.RoleOf` `[class]` | ✏️ Renamed |  |
| `OgreBotAPI:GetFlag` | works | — | ✅ Works as is |  |
| `OgreBotAPI.GetGroupIDBy` | reads NULL | `OgreBotAPI.Roster.GroupIDBy` | ✏️ Renamed | arguments swapped - old `[search, mode, rank]`, new `[mode, search, rank]`. An omitted mode now means All, not Class. |
| `OgreBotAPI.GetGroupNameBy` | reads NULL | `OgreBotAPI.Roster.GroupNameBy` | ⚠️ Argument order changed | Note A |
| `OgreBotAPI.GetRaidIDBy` | reads NULL | `OgreBotAPI.Roster.RaidIDBy` | ⚠️ Argument order changed | Note A |
| `OgreBotAPI.GetRaidNameBy` | reads NULL | `OgreBotAPI.Roster.RaidNameBy` | ⚠️ Argument order changed | Note A |
| `OgreBotAPI.GroupInZone` | reads NULL | `OgreBotAPI.Roster.InZone` `[within=0]` | ✏️ Renamed |  |
| `OgreBotAPI.GuildFlagLocation` | reads NULL | `OgreBotAPI.Roster.GuildFlagLocation` | ➡️ Moved |  |
| `OgreBotAPI.InEQ2Chars` | reads NULL | `OgreBotAPI.Roster.InEQ2Chars` `[speaker,fullAccountOnly=FALSE]` | ➡️ Moved |  |
| `OgreBotAPI.InICGroup` | reads NULL | — | ⛔ Removed | Ask the group: ${OgreBotAPI.Comms.GroupQuery[${Me.Name},-question,"LavishScript[\${ISXOgreEQ2.IC.Running}]"]} returns an id; wait on .Done[id], then .Result[id] is JSON - "anyYes" = someone in the group is running IC, "yesWho" = who. |
| `OgreBotAPI:Invite` | does nothing | `OgreBotAPI.Roster:Invite` `[fw,who=me]` | ➡️ Moved | Not taken any more: `_RaidInvite`. |
| `OgreBotAPI.IsGroupLeader` | reads NULL | `OgreBotAPI.Roster.IsGroupLeader` | ➡️ Moved |  |
| `OgreBotAPI:MakeLeader` | does nothing | `OgreBotAPI.Roster:MakeLeader` `[fw,leader=me]` | ➡️ Moved |  |
| `OgreBotAPI:MarkToon` | does nothing | `OgreBotAPI.Roster:Mark` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:Mentor` | does nothing | `OgreBotAPI.Roster:Mentor` `[fw,name=me]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. |
| `OgreBotAPI.SortGroupByIDBy` | reads NULL | `OgreBotAPI.Roster.SortGroupByID` | ⚠️ Argument order changed | arguments swapped - old `[search, mode, ...]`, new `[mode, search, ...]`. The first two arguments are swapped. |
| `OgreBotAPI.SortRaidByIDBy` | reads NULL | `OgreBotAPI.Roster.SortRaidByID` | ⚠️ Argument order changed | arguments swapped - old `[search, mode, ...]`, new `[mode, search, ...]`. The first two arguments are swapped. |
| `OgreBotAPI:SpewFlags` | does nothing | `OgreBotAPI.Roster:SpewFlags` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI.ToonFlagged` | reads NULL | `OgreBotAPI.Roster.Flagged` `[n=1]` | ✏️ Renamed |  |
| `OgreBotAPI:ToonMarked` | reads NULL | `OgreBotAPI.Roster:SpewMarked` `[fw,where]` | ✏️ Renamed |  |
| `OgreBotAPI:UnflagAll` | does nothing | `OgreBotAPI.Roster:UnflagAll` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI:UnflagToon` | does nothing | `OgreBotAPI.Roster:Unflag` `[fw,n=1]` | ✏️ Renamed |  |
| `OgreBotAPI:UnmarkToon` | does nothing | `OgreBotAPI.Roster:Unmark` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:Unmentor` | does nothing | `OgreBotAPI.Roster:Unmentor` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI:UseFlag` | works | — | ✅ Works as is |  |

## OgreBotAPI.Session

Old names whose job is now in `OgreBotAPI.Session`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI.AtCharacterSelect` | reads NULL | `OgreBotAPI.Session.AtCharacterSelect` | ➡️ Moved |  |
| `OgreBotAPI.CurrentCharacter` | reads NULL | `OgreBotAPI.Session.CharacterName` | ✏️ Renamed |  |
| `OgreBotAPI.Get_ReviveLocation` | reads NULL | `OgreBotAPI.Session.ReviveLocation` | ✏️ Renamed |  |
| `OgreBotAPI:ImmRes` | does nothing | `OgreBotAPI.Session:ImmRes` `[fw,howManyDead=2]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. |
| `OgreBotAPI:LoginAtCharacterSelect` | does nothing | `OgreBotAPI.Session:LoginAtCharacterSelect` `[fw,charName]` | ➡️ Moved |  |
| `OgreBotAPI:LogToonIn` | does nothing | `OgreBotAPI.Session:LogToonIn` `[forToon,toon]` | ➡️ Moved |  |
| `OgreBotAPI:PlayAtCharacterSelect` | does nothing | `OgreBotAPI.Session:PlayAtCharacterSelect` `[fw]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. gained a for-who. It runs where `${Me}` does not exist, so it is deliberately not gated on the character existing. |
| `OgreBotAPI:Question` | reads NULL | `OgreBotAPI.Session:CollectShiny` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:Res` | does nothing | `OgreBotAPI.Session:Res` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI:Resource` | does nothing | `OgreBotAPI.Session:Harvest` `[fw]` | ✏️ Renamed | renamed to `Session:Harvest` - it collects a harvest node in range. |
| `OgreBotAPI:ResStone` | does nothing | `OgreBotAPI.Session:ResStone` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI:Revive` | does nothing | `OgreBotAPI.Session:Revive` `[fw,option=0,exact=FALSE]` | ➡️ Moved |  |
| `OgreBotAPI:StopRes` | does nothing | `OgreBotAPI.Session:StopRes` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI:UpdateCharacterDetails` | does nothing | `OgreBotAPI.Session:UpdateCharacterDetails` `[fw]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. gained a for-who. |

## OgreBotAPI.Travel

Old names whose job is now in `OgreBotAPI.Travel`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:FastTravel` | does nothing | `OgreBotAPI.Travel:Fast` `[fw,toWhere,flag...]` | ✏️ Renamed |  |
| `OgreBotAPI:PortalToGuildHall` | does nothing | `OgreBotAPI.Travel:ToGuildHall` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:SpewZoneDoorOptions` | does nothing | `OgreBotAPI.Travel:SpewZoneDoorOptions` `[fw]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. |
| `OgreBotAPI:Travel` | does nothing | `OgreBotAPI.Travel:Travel` `[fw,toWhere,exact=FALSE,mzo=LAST_ENTRY]` | ➡️ Moved |  |
| `OgreBotAPI.Travel_Get_ZoneDoorValue` | reads NULL | `OgreBotAPI.Travel.ZoneDoorValue` `[option]` | ✏️ Renamed |  |
| `OgreBotAPI:TravelBell` | does nothing | `OgreBotAPI.Travel:Bell` `[fw,toWhere,exact=FALSE,mzo=LAST_ENTRY]` | ✏️ Renamed |  |
| `OgreBotAPI:TravelDruid` | does nothing | `OgreBotAPI.Travel:Druid` `[fw,toWhere,exact=FALSE,mzo=LAST_ENTRY]` | ✏️ Renamed |  |
| `OgreBotAPI:TravelSpires` | does nothing | `OgreBotAPI.Travel:Spires` `[fw,toWhere,exact=FALSE,mzo=LAST_ENTRY]` | ✏️ Renamed |  |
| `OgreBotAPI:ZoneDoor` | does nothing | `OgreBotAPI.Travel:ZoneDoor` `[door=1]` | ➡️ Moved |  |
| `OgreBotAPI:ZoneDoorForWho` | does nothing | `OgreBotAPI.Travel:ZoneDoorFor` `[fw,door=1]` | ✏️ Renamed |  |

## OgreBotAPI.Util

Old names whose job is now in `OgreBotAPI.Util`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI.ArraySearch` | reads NULL | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI.ArraySearch` was a stub that did nothing, and it was removed 2026-10-22. Classic's took a LavishScript array by reference, which a new-bot member cannot receive. Search the array in your script. |
| `OgreBotAPI.Between` | reads NULL | `OgreBotAPI.Util.Between` `[v=0,lo=0,hi=0]` | ➡️ Moved |  |
| `OgreBotAPI.BetweenFloat` | reads NULL | `OgreBotAPI.Util.BetweenFloat` `[v=0,lo=0,hi=0]` | ➡️ Moved |  |
| `OgreBotAPI:CheckResearch` | does nothing | `OgreBotAPI.Util:CheckResearch` `[fw,forceReport=FALSE]` | ➡️ Moved |  |
| `OgreBotAPI.Clean` | reads NULL | `OgreBotAPI.Util.Clean` `[s]` | ➡️ Moved |  |
| `OgreBotAPI.CleanNameWithSpaces` | reads NULL | `OgreBotAPI.Util.Clean` `[s]` | ✏️ Renamed |  |
| `OgreBotAPI.ConvertSecondsToHMS` | reads NULL | `OgreBotAPI.Util.SecondsToHMS` `[n=0]` | ✏️ Renamed |  |
| `OgreBotAPI.ConvertSlotArrayToSlot` | reads NULL | `OgreBotAPI.Util.SlotArrayToSlot` `[n=0]` | ✏️ Renamed |  |
| `OgreBotAPI.FileExists` | reads NULL | `OgreBotAPI.Util.FileExists` `[path]` | ➡️ Moved |  |
| `OgreBotAPI.Get_Hours` | reads NULL | `OgreBotAPI.Util.Hours` `[n=0]` | ✏️ Renamed |  |
| `OgreBotAPI.Get_Minutes` | reads NULL | `OgreBotAPI.Util.Minutes` `[n=0]` | ✏️ Renamed |  |
| `OgreBotAPI.Get_Seconds` | reads NULL | `OgreBotAPI.Util.Seconds` `[n=0]` | ✏️ Renamed |  |
| `OgreBotAPI.IndexMatch` | reads NULL | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI.IndexMatch` was a stub that did nothing, and it was removed 2026-10-22. Classic's took a LavishScript index by reference, which a new-bot member cannot receive. Search the index in your script. |
| `OgreBotAPI.IndexSearch` | reads NULL | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI.IndexSearch` was a stub that did nothing, and it was removed 2026-10-22. Classic's took a LavishScript array by reference, which a new-bot member cannot receive. Search the array in your script. |
| `OgreBotAPI.IndexSearchJSON` | reads NULL | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI.IndexSearchJSON` was a stub that did nothing, and it was removed 2026-10-22. Classic's took a LavishScript jsonvalue array by reference, which a new-bot member cannot receive. Search the array in your script. |
| `OgreBotAPI.MD5` | reads NULL | `OgreBotAPI.Util.MD5` `[s]` | ➡️ Moved |  |
| `OgreBotAPI:OnScreenTimer` | does nothing | `OgreBotAPI.Util:OnScreenTimer` `[fw,...]` | ➡️ Moved | Not taken any more: `_Slot`, `_Message`, `_MinUpdateTimer`, `_ExtraTimer`, `_ExtraTimerMessage`. |
| `OgreBotAPI:OnScreenTimerReset` | does nothing | `OgreBotAPI.Util:OnScreenTimerReset` `[fw,slot=1]` | ➡️ Moved |  |
| `OgreBotAPI.PE_ThisMember` | reads NULL | `OgreBotAPI.Util.IEquals` `[a,b]` | ✏️ Renamed |  |
| `OgreBotAPI.RemoveColourCode` | reads NULL | `OgreBotAPI.Util.StripColourCodes` `[s]` | ✏️ Renamed |  |
| `OgreBotAPI.RemoveZoneNumber` | reads NULL | `OgreBotAPI.Util.StripZoneNumber` `[s=${Zone.Name}]` | ✏️ Renamed |  |
| `OgreBotAPI.RemoveZoneNumberOnly` | reads NULL | `OgreBotAPI.Util.StripZoneNumberOnly` `[s=${Zone.Name}]` | ✏️ Renamed |  |
| `OgreBotAPI:Research_Material_Check` | does nothing | `OgreBotAPI.Util:CheckResearchMaterials` `[fw,...]` | ✏️ Renamed |  |
| `OgreBotAPI.RomanToInt` | reads NULL | `OgreBotAPI.Util.RomanToInt` `[s]` | ➡️ Moved |  |
| `OgreBotAPI.RoundNumToNearestValue` | reads NULL | `OgreBotAPI.Util.RoundToNearest` `[value=0,step=1,incBy=0]` | ✏️ Renamed |  |
| `OgreBotAPI.To_Float` | reads NULL | `OgreBotAPI.Util.ToFloat` `[s]` | ✏️ Renamed |  |
| `OgreBotAPI.To_Int` | reads NULL | `OgreBotAPI.Util.ToInt` `[s]` | ✏️ Renamed |  |
| `OgreBotAPI.To_Number` | reads NULL | `OgreBotAPI.Util.ToNumber` `[s]` | ✏️ Renamed |  |

## OgreBotAPI.Vars

Old names whose job is now in `OgreBotAPI.Vars`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:Clear_InternalVariable` | does nothing | `OgreBotAPI.Vars:ClearInternal` `[fw,name]` | ✏️ Renamed |  |
| `OgreBotAPI:Clear_InternalVariables` | does nothing | `OgreBotAPI.Vars:ClearAllInternal` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:Clear_Variable` | does nothing | `OgreBotAPI.Vars:Clear` `[fw,name]` | ✏️ Renamed |  |
| `OgreBotAPI:Clear_Variables` | does nothing | `OgreBotAPI.Vars:ClearAll` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI.Get_InternalVariable` | reads NULL | `OgreBotAPI.Vars.GetInternal` `[name]` | ✏️ Renamed |  |
| `OgreBotAPI.Get_InternalVariableExists` | reads NULL | `OgreBotAPI.Vars.InternalExists` `[name]` | ✏️ Renamed |  |
| `OgreBotAPI.Get_Variable` | reads NULL | `OgreBotAPI.Vars.Get` `[name]` | ✏️ Renamed |  |
| `OgreBotAPI.Get_Variable_Bool` | reads NULL | `OgreBotAPI.Vars.Bool` `[name]` | ✏️ Renamed |  |
| `OgreBotAPI.Get_VariableExists` | reads NULL | `OgreBotAPI.Vars.Exists` `[name]` | ✏️ Renamed |  |
| `OgreBotAPI.InternalVariables` | reads NULL | `OgreBotAPI.Vars.GetInternal` `[name]` | ✏️ Renamed |  |
| `OgreBotAPI:Set_InternalVariable` | does nothing | `OgreBotAPI.Vars:SetInternal` `[fw,name,value]` | ✏️ Renamed |  |
| `OgreBotAPI:Set_Variable` | does nothing | `OgreBotAPI.Vars:Set` `[fw,name,value]` | ✏️ Renamed |  |
| `OgreBotAPI.Variables` | reads NULL | `OgreBotAPI.Vars.Get` `[name]` | ✏️ Renamed |  |

## OgreBotAPI.Windows

Old names whose job is now in `OgreBotAPI.Windows`.

**Note A** (3 rows below): The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:AcceptNoChoiceReward` | does nothing | `OgreBotAPI.Windows:AcceptNoChoiceReward` `[fw,windowId]` | ⚠️ Arguments changed | Note A |
| `OgreBotAPI:AcceptReward` | does nothing | `OgreBotAPI.Windows:AcceptReward` `[fw,num\|name=0,windowId=0]` | ➡️ Moved |  |
| `OgreBotAPI:ChoiceWindow` | does nothing | `OgreBotAPI.Windows:Choice` `[fw,option=1]` | ✏️ Renamed |  |
| `OgreBotAPI:CloseAllExamine` | does nothing | `OgreBotAPI.Windows:CloseExamine` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:CloseExamine` | does nothing | `OgreBotAPI.Windows:CloseExamine` `[fw]` | ⚠️ Arguments changed | Note A |
| `OgreBotAPI:CloseExamineWindow` | does nothing | `OgreBotAPI.Windows:CloseExamine` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:CloseWindow` | does nothing | `OgreBotAPI.Windows:Close` `[fw,name]` | ⚠️ Arguments changed | The arguments are different: Classic took `(string _ForWho="all")`, the new call takes `[fw,name]`. |
| `OgreBotAPI:DungeonMakerCancel` | does nothing | `OgreBotAPI.Windows:DungeonMakerCancel` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI:F2PWindow_Check` | does nothing | `OgreBotAPI.Windows:F2PWindowCheck` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI.Get_RewardID` | reads NULL | `OgreBotAPI.Windows.RewardID` `[num\|name,windowId]` | ✏️ Renamed |  |
| `OgreBotAPI.Get_RewardLinkID` | reads NULL | `OgreBotAPI.Windows.RewardLinkID` `[num\|name,windowId]` | ✏️ Renamed |  |
| `OgreBotAPI.Get_RewardName` | reads NULL | `OgreBotAPI.Windows.RewardName` `[num\|name,windowId]` | ✏️ Renamed |  |
| `OgreBotAPI:InputTextWindow_Accept` | does nothing | `OgreBotAPI.Windows:InputTextAccept` `[fw,...]` | ✏️ Renamed |  |
| `OgreBotAPI:InputTextWindow_AddText` | does nothing | `OgreBotAPI.Windows:InputTextAdd` `[fw,text]` | ✏️ Renamed | `[fw, text]`. Same page/child/visible gate as `:InputTextAccept` - a no-op when the input box is not up. |
| `OgreBotAPI:InputTextWindow_ClearText` | does nothing | `OgreBotAPI.Windows:InputTextClear` `[fw]` | ✏️ Renamed | `[fw]`. |
| `OgreBotAPI.IsCastingWindowVisible` | reads NULL | `OgreBotAPI.Windows.CastingWindowVisible` | ✏️ Renamed |  |
| `OgreBotAPI:OK_Button` | does nothing | `OgreBotAPI.Windows:OK` `[fw,...]` | ✏️ Renamed |  |
| `OgreBotAPI:ProvingGrounds_Exit` | does nothing | `OgreBotAPI.Windows:ProvingGroundsExit` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:ProvingGrounds_Scoreboard_Close` | does nothing | `OgreBotAPI.Windows:ProvingGroundsScoreboardClose` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:ReplyDialog` | does nothing | `OgreBotAPI.Windows:Reply` `[fw,number\|text=1]` | ✏️ Renamed |  |
| `OgreBotAPI.ReplyDialog_ReplyExists` | reads NULL | `OgreBotAPI.Windows.ReplyExists` `[text]` | ⚠️ Arguments changed | SIGNATURE CHANGED - drop the for-who (a member answers for the session reading it): the reply text (Classic `_Choice`) is the one argument, matched as CONTAINS in any case (Classic's default); `_ExactMatch` is gone. Still the 1-based reply number of the open reply dialog, 0 = none. Example: `${OgreBotAPI.ReplyDialog_ReplyExists["all","Curio"]}` -&gt; `${OgreBotAPI.Windows.ReplyExists["Curio"]}`. |
| `OgreBotAPI:ReplyDialogClose` | does nothing | `OgreBotAPI.Windows:ReplyClose` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI.RewardWindow_Get_WindowID` | reads NULL | `OgreBotAPI.Windows.RewardWindowID` | ✏️ Renamed |  |
| `OgreBotAPI:RewardWindow_Spew_WindowIDs` | does nothing | `OgreBotAPI.Windows:SpewRewardWindowIDs` `[fw]` | ⚠️ Arguments changed | Note A |
| `OgreBotAPI:Select_Window` | does nothing | `OgreBotAPI.Windows:Select` `[fw,option]` | ⚠️ Arguments changed | The arguments are different: Classic took `(string _ForWho=all, ... Args)`, the new call takes `[fw,option]`. |
| `OgreBotAPI:Select_Window_Cancel` | does nothing | `OgreBotAPI.Windows:SelectCancel` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI.Select_Window_GetOption` | reads NULL | `OgreBotAPI.Windows.SelectOption` `[n]` | ⚠️ Arguments changed | The arguments are different: Classic took `(... Args)`, the new call takes `[n]`. |
| `OgreBotAPI:Select_Window_Spew` | does nothing | `OgreBotAPI.Windows:SelectSpew` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:ShowOgreConsole` | does nothing | `OgreBotAPI.Windows:ShowConsole` `[fw,on=TRUE]` | ✏️ Renamed |  |
| `OgreBotAPI:ToggleConsoleWindow` | does nothing | `OgreBotAPI.Windows:ToggleConsole` `[fw,value=toggle]` | ✏️ Renamed |  |
| `OgreBotAPI:ToggleMainWindow` | does nothing | `OgreBotAPI.Windows:ToggleMain` `[fw]` | ✏️ Renamed |  |

## OgreBotAPI.Zone

Old names whose job is now in `OgreBotAPI.Zone`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:Champions_Zone_Resetter` | does nothing | `OgreBotAPI.Zone:ChampionsResetter` `[fw,...]` | ✏️ Renamed |  |
| `OgreBotAPI:ChangeZoneTo` | does nothing | `OgreBotAPI.Zone:ChangeZoneTo` `[fw,toWho]` | ➡️ Moved |  |
| `OgreBotAPI:CheckICPartyStatus` | does nothing | — | ⛔ Removed | Nothing to call - delete the line. To ask whether the group is running IC: Ask the group: ${OgreBotAPI.Comms.GroupQuery[${Me.Name},-question,"LavishScript[\${ISXOgreEQ2.IC.Running}]"]} returns an id; wait on .Done[id], then .Result[id] is JSON - "anyYes" = someone in the group is running IC, "yesWho" = who. |
| `OgreBotAPI.CityRestrictions` | reads NULL | `OgreBotAPI.Zone.CityRestrictions` | ➡️ Moved |  |
| `OgreBotAPI.CleanZoneName` | reads NULL | `OgreBotAPI.Zone.CleanName` `[name=${Zone.Name}]` | ✏️ Renamed |  |
| `OgreBotAPI.InBattleGround` | reads NULL | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI.Zone.InBattleGround` was a stub that did nothing, and it was removed 2026-10-22. |
| `OgreBotAPI.InGuildHallZone` | reads NULL | `OgreBotAPI.Zone.InGuildHall` | ✏️ Renamed |  |
| `OgreBotAPI.InHouseAccessZone` | reads NULL | `OgreBotAPI.Zone.InHouseAccess` | ✏️ Renamed |  |
| `OgreBotAPI.InHouseZone` | reads NULL | `OgreBotAPI.Zone.InHouse` | ✏️ Renamed |  |
| `OgreBotAPI.InInstance` | reads NULL | `OgreBotAPI.Zone.InInstance` | ➡️ Moved |  |
| `OgreBotAPI:ResetZone` | does nothing | `OgreBotAPI.Zone:ResetZone` `[fw,...]` | ➡️ Moved |  |
| `OgreBotAPI:Select_Zone_Version` | does nothing | `OgreBotAPI.Zone:SelectVersion` `[fw,version=OK]` | ✏️ Renamed |  |
| `OgreBotAPI:ShareQuestsForZone` | does nothing | `OgreBotAPI.Zone:ShareQuestsForZone` `[fw,...]` | ➡️ Moved |  |
| `OgreBotAPI:SpecialZoneSpecific` | does nothing | `OgreBotAPI.Zone:SpecialZoneSpecific` `[fw,...]` | ➡️ Moved |  |
| `OgreBotAPI:ToggleZoneReuse` | does nothing | `OgreBotAPI.Zone:ToggleZoneReuse` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI:Zone` | does nothing | `OgreBotAPI.Zone:Zone` `[fw,zone,...]` | ➡️ Moved |  |
| `OgreBotAPI.ZoneName` | reads NULL | `OgreBotAPI.Zone.Name` | ✏️ Renamed |  |
| `OgreBotAPI.ZoneReset_Get_ZoneData` | reads NULL | `OgreBotAPI.Zone.ResetZoneData` `[zone,field]` | ⚠️ Arguments changed | Takes the zone and the key instead of a collection to fill: ${OgreBotAPI.Zone.ResetZoneData[&lt;zone&gt;]} is TRUE when the zone is in the Zone Reuse list, and ${OgreBotAPI.Zone.ResetZoneData[&lt;zone&gt;,&lt;key&gt;]} gives one key - ZoneName, IsSet, Resettable, TimeLeft (seconds) or TextTimeLeft. Run OgreBotAPI.Zone:ResetUpdateInfo first; Zone.ResetReady says when the list is in. |
| `OgreBotAPI.ZoneReset_IsReady` | reads NULL | `OgreBotAPI.Zone.ResetReady` | ✏️ Renamed |  |
| `OgreBotAPI.ZoneReset_IsUpdating` | reads NULL | `OgreBotAPI.Zone.ResetUpdating` | ✏️ Renamed |  |
| `OgreBotAPI:ZoneReset_UpdateInfo` | does nothing | `OgreBotAPI.Zone:ResetUpdateInfo` `[fw]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. |
| `OgreBotAPI:ZoneResetAll` | does nothing | `OgreBotAPI.Zone:ResetAll` `[fw,allowRaid=FALSE]` | ✏️ Renamed |  |

## Not in a group

Old names with no home in a group: not ported yet, done somewhere else, or a line in a data file now.

**Note A** (18 rows below): Classic-internal state (a cache, a timer, a handle). Not script-facing, and the new engine owns the equivalent state privately.

**Note B** (7 rows below): a fight-, item- or zone-specific one-off.

**Note C** (7 rows below): a `_Report` variant that echoed what the plain verb did. The new surface has one verb per action; the roll-call verbs it once pointed to (`Comms:ReportListIrc` / `:ReportSpew`) were stubs and were removed 2026-10-22.

**Note D** (5 rows below): no new-bot equivalent on the OgreBotAPI surface.

**Note E** (4 rows below): Rule 9: every cast goes through the one cast chokepoint. The new bot exposes `Abilities:Cast` and its variants (`:CastNoChecks`, `:CastOnNPC`, `:CastOnPlayer`, the `*Relay` forms) plus the cast stack; the Classic delay/no-export/type variants were not carried as separate verbs.

**Note F** (3 rows below): SmartLoot per-player assignment. `OgreBotAPI.Loot` carries the ported loot surface (`:LootAll`, `:SetAutoLootMode`, `:Decide`, `:Config`, `.WindowExists`); the assignment table was not carried.

**Note G** (3 rows below): client/session lifecycle. The new bot drives this from the TaskRunner and the auto-login engine rather than from the API surface; `Bot:CampToDesktop` and `Session:PlayAtCharacterSelect` are the two that were ported.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:AfterProfileLoad` | does nothing | — | ⛔ Not ported yet | Note A |
| `OgreBotAPI:Aliases_ShowAllBuiltInAliases` | does nothing | — | ⛔ Not ported yet | Classic's verb only set a display flag on one combobox; the new bot has no such flag by design. The 'Display Aliases' button is a different feature and still works. |
| `OgreBotAPI.bBuyingFromMerchantConfirmation` | reads NULL | — | ⛔ Not ported yet | Note A |
| `OgreBotAPI.bCacheEquipmentAdornmentNames` | reads NULL | — | ⛔ Not ported yet | Note A |
| `OgreBotAPI.bDebugMode` | reads NULL | `${OgreBotAPI.Debug.DebugPrefix}` | ➡️ Lives somewhere else |  |
| `OgreBotAPI.bInternal` | reads NULL | — | ⛔ Not ported yet | Note A |
| `OgreBotAPI.bNoCollision` | reads NULL | — | ⛔ Not ported yet | Note A |
| `OgreBotAPI.bSetUpFor_HOs_Current_HeroicSurge` | reads NULL | — | ⛔ Not ported yet | Note A |
| `OgreBotAPI.bSetUpFor_HOs_Obtained_Current_HeroicSurge` | reads NULL | — | ⛔ Not ported yet | Note A |
| `OgreBotAPI:CastAbilityNoExportUntilCast` | does nothing | — | ⛔ Not ported yet | Note E |
| `OgreBotAPI:CastAbilityType` | does nothing | — | ⛔ Not ported yet | Note E |
| `OgreBotAPI:CastHQEar` | does nothing | — | ⛔ Not ported yet | Note B |
| `OgreBotAPI.CastStackAllowHOIcons` | reads NULL | — | ⛔ Not ported yet | Note A |
| `OgreBotAPI.CastStackDisableHOIcons` | reads NULL | — | ⛔ Not ported yet | Note A |
| `OgreBotAPI:Change_PoisonAutoConsume` | does nothing | — | ⛔ Not ported yet | Classic toggled its own auto-consume checkboxes here. On the new bot a setting is written through `OgreBotAPI.Options:Set[<setting_id>, <value>]` and the consumable ACTIONS live on `OgreBotAPI.Consumables` / `.Inventory`. |
| `OgreBotAPI:DestroyItemByID_NoChecks` | does nothing | — | ⛔ Not ported yet | Note D |
| `OgreBotAPI:Dispell` | does nothing | encounter action `dispell` | 📄 In a data file now |  |
| `OgreBotAPI:DispellNPCWithAny` | does nothing | encounter action `dispell` | 📄 In a data file now |  |
| `OgreBotAPI:DispellNPCWithItem` | does nothing | encounter action `dispell` | 📄 In a data file now |  |
| `OgreBotAPI:DispellNPCWithSpell` | does nothing | encounter action `dispell` | 📄 In a data file now |  |
| `OgreBotAPI:FastTravel_Report` | does nothing | — | ⛔ Not ported yet | Note C |
| `OgreBotAPI:FastTravelOld` | does nothing | — | ⛔ Not ported yet | Note C |
| `call OgreBotAPI.FindAdornment_ReturnSlot` | does nothing | — | ⛔ Not ported yet | The two Classic consumers: (`"Lazirah's Star" TRUE`) is ALREADY absorbed - StarEquipped = HasAdornment("Lazirah's Star"); object_TabInfo_Other.Find_FieldMedic has no port. |
| `call OgreBotAPI.FindAdornments_ReturnJSON` | does nothing | — | ⛔ Not ported yet | Its single Classic caller is Find_FieldMedic counting Field Medic runes - unported (see FindAdornment_ReturnSlot). |
| `OgreBotAPI:Fix_Broken_Shit` | does nothing | — | ⛔ Not ported yet | Note B |
| `OgreBotAPI:FixCastAfterZoneBug` | does nothing | — | ⛔ Not ported yet | Note B |
| `OgreBotAPI:ForceAcceptQuest` | does nothing | the automatic quest-offer reaction | ➡️ Lives somewhere else |  |
| `call OgreBotAPI.Generate_CacheEquipmentAdornmentNames` | does nothing | `${OgreBotAPI.CastStack:ExamineItems}   (re-arms the engine's rebuild after a gear change)` | ➡️ Lives somewhere else | ExamineItems also re-examines uncached cast-stack items, not just the adorn cache. There is no bool 'cache built' return to wait on. |
| `OgreBotAPI:Get_MissionTimerInfo` | does nothing | — | ⛔ Not ported yet | Note B |
| `OgreBotAPI.Get_NumAdornmentsOfColour` | reads NULL | — | ⛔ Not ported yet | Note D |
| `OgreBotAPI:Get_Poisons` | does nothing | — | ⛔ Not ported yet | Note D |
| `OgreBotAPI.HardCodedAbilityEffectRadius` | reads NULL | — | ⛔ Not ported yet | Note A |
| `OgreBotAPI.HardCodedAbilityMaxRange` | reads NULL | — | ⛔ Not ported yet | Note A |
| `call OgreBotAPI.Interrupt_Mode` | does nothing | — | ⛔ Not ported yet | Note E |
| `OgreBotAPI.IsItemTimeUntilReadyZero` | reads NULL | — | ⛔ Not ported yet | Note D |
| `OgreBotAPI:ItemDebug` | does nothing | — | ⛔ Not ported yet | Note D |
| `OgreBotAPI.jvCacheEquipmentAdornmentNames` | reads NULL | — | ⛔ Not ported yet | Note A |
| `OgreBotAPI.LandFlyingMountActive` | reads NULL | — | ⛔ Not ported yet | Note A |
| `OgreBotAPI:Loot_SmartAssign_Add` | does nothing | — | ⛔ Not ported yet | Note F |
| `OgreBotAPI:Loot_SmartAssign_Update` | does nothing | — | ⛔ Not ported yet | Note F |
| `OgreBotAPI:Mount` | does nothing | — | ⛔ Not ported yet | Mount -&gt; f_SummonMount is ONE `/summon_mount`, i.e. a TOGGLE (iss:10988), which is how the console schema described it. Consumables:MountUp is FORCE-ON (sit/toggle/stand/mount) and is already `-Force_MountOn`. |
| `OgreBotAPI:Myzer1` | does nothing | — | ⛔ Not ported yet | the new bot's equivalents are its own instrumentation - the buffered log sink and `Log <path>` - not an OgreBotAPI verb. Nothing to convert. |
| `OgreBotAPI:Myzer2` | does nothing | — | ⛔ Not ported yet | the new bot's equivalents are its own instrumentation - the buffered log sink and `Log <path>` - not an OgreBotAPI verb. Nothing to convert. |
| `OgreBotAPI:NoTanking` | does nothing | `OgreBotAPI.Options:Set + OgreBotAPI.Abilities:Cast` | ➡️ Lives somewhere else | the cast is ability-by-NAME (`"Subtle Strikes"`), which is Rule 10 territory now - resolve the id off the export catalog when converting. |
| `OgreBotAPI.ogre_campspot_me` | reads NULL | — | ⛔ Not ported yet | Engine-only in Classic too (both sites are). |
| `OgreBotAPI:Output_InGame_MovementKeys` | does nothing | — | ⛔ Not ported yet | prints Classic's movement key bindings. The new surface SETS them (`Movement:SetForwardKey` / `:SetBackwardKey` / `:SetFlyUpKey` / `:SetFlyDownKey`) but does not dump them. |
| `OgreBotAPI:Populate_ExportList` | does nothing | — | ⛔ Not ported yet |  |
| `OgreBotAPI.PulseCircleMovement_CurrentSpot` | reads NULL | — | ⛔ Not ported yet | Note A |
| `OgreBotAPI.PulseCircleMovement_TimerRecentlyMoved` | reads NULL | — | ⛔ Not ported yet | Note A |
| `OgreBotAPI:Reload_DevBot` | does nothing | — | ⛔ Not ported yet | Note G |
| `OgreBotAPI:ReloadExport` | does nothing | — | ⛔ Not ported yet | Note G |
| `OgreBotAPI:ReloadOgreIRC` | does nothing | `${OgreIRCHub:Reload}  /  ${OgreIRCHub:Connect}` | ➡️ Lives somewhere else |  |
| `OgreBotAPI:Report_Back` | does nothing | — | ⛔ Not ported yet | Note C |
| `OgreBotAPI:Report_ClearList` | does nothing | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI.Comms:ReportClear` was a stub that did nothing, and it was removed 2026-10-22. |
| `OgreBotAPI.Report_Group_GetKey` | reads NULL | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI.Comms.ReportKey` was a stub that did nothing, and it was removed 2026-10-22. |
| `OgreBotAPI.Report_Group_GetValue` | reads NULL | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI.Comms.ReportValue` was a stub that did nothing, and it was removed 2026-10-22. |
| `OgreBotAPI:Report_SpewList` | does nothing | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI.Comms:ReportSpew` was a stub that did nothing, and it was removed 2026-10-22. |
| `OgreBotAPI:ReportForList_IRC` | does nothing | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI.Comms:ReportListIrc` was a stub that did nothing, and it was removed 2026-10-22. |
| `OgreBotAPI:Reporting` | does nothing | — | ⛔ Removed | Not ported: the new bot's `OgreBotAPI.Comms:Reporting` was a stub that did nothing, and it was removed 2026-10-22. |
| `call OgreBotAPI.Set_FirstPersonView` | does nothing | `OgreBotAPI.Client:SetCameraPitch["<forwho>",<pitch>,TRUE]   /   encounter {"do":"camera","op":"setPitch","pitch":<n>}` | ➡️ Lives somewhere else | Client:SetCameraPitch's endInFirstPerson DEFAULTS FALSE (pass TRUE); the encounter `camera setPitch` op defaults firstPerson TRUE. Pitch range -75..75, 0 = centre, out of range refused. A flow, not a wait - there is no TRUE/FALSE return to `call` on. |
| `call OgreBotAPI.Set_LookDown` | does nothing | `OgreBotAPI.Client:SetCameraPitch["<forwho>",<pitch>,TRUE]   /   encounter {"do":"camera","op":"setPitch","pitch":<n>}` | ➡️ Lives somewhere else | Classic's arg is a HOLD DURATION, not an angle - choose a pitch; do not carry the 30 across. |
| `call OgreBotAPI.Set_LookUp` | does nothing | `OgreBotAPI.Client:SetCameraPitch["<forwho>",<pitch>,TRUE]` | ➡️ Lives somewhere else | Classic's arg is a hold duration, not an angle. |
| `OgreBotAPI:SetQuestion` | does nothing | — | ⛔ Not ported yet | Classic toggled its own auto-consume checkboxes here. On the new bot a setting is written through `OgreBotAPI.Options:Set[<setting_id>, <value>]` and the consumable ACTIONS live on `OgreBotAPI.Consumables` / `.Inventory`. |
| `OgreBotAPI:SmartLoot_LOL_AssignPlayer_Item` | does nothing | — | ⛔ Not ported yet | Note F |
| `OgreBotAPI.SpecialDebugMode` | reads NULL | — | ⛔ Not ported yet | Note A |
| `OgreBotAPI:SpendDeityPoints` | does nothing | — | ⛔ Not ported yet | Note B |
| `OgreBotAPI:SpendDietyPoints` | does nothing | — | ⛔ Not ported yet | DEAD ON OLDBOT TOO, and the console verb is DELETED. SpendDietyPoints (iss:11671) is a for-who gate followed by a COMMENTED-OUT QueueCommand - the one line that would do anything. |
| `OgreBotAPI:Test_ExportList` | does nothing | — | ⛔ Not ported yet |  |
| `OgreBotAPI.Timer_Exit` | reads NULL | — | ⛔ Not ported yet | Note A |
| `OgreBotAPI:Travel_Report` | does nothing | — | ⛔ Not ported yet | Note C |
| `OgreBotAPI:TravelBell_Report` | does nothing | — | ⛔ Not ported yet | Note C |
| `OgreBotAPI:TravelDruid_Report` | does nothing | — | ⛔ Not ported yet | Note C |
| `OgreBotAPI:TravelSpires_Report` | does nothing | — | ⛔ Not ported yet | Note C |
| `OgreBotAPI:Update_Guk_Shinies` | does nothing | — | ⛔ Not ported yet | Note B |
| `OgreBotAPI:Update_PoP_Shinies` | does nothing | — | ⛔ Not ported yet | Note B |
| `OgreBotAPI:VampiricRequiem_AbilityCancel` | does nothing | — | ⛔ Not ported yet | Note E |
| `call OgreBotAPI.WaitForCasting` | does nothing | — | ⛔ Not ported yet | no door is needed and none was built: `${Me.CastingSpell}` is a plain ISXEQ2 read, so a converted script writes the wait itself. 8 consumer call sites, all `call GetInfoOb.WaitForCasting` / `call OgreBotAPI.WaitForCasting`. |
| `OgreBotAPI.WeaponSlotSubTypes` | reads NULL | — | ⛔ Not ported yet | Note A |
| `OgreBotAPI:ZoneInto` | does nothing | — | ⛔ Not ported yet | Note G |

## Not in the new bot yet

If your script needs one of these, leave it out for now and tell us - this list is what still needs work.

- `OgreBotAPI:AfterProfileLoad` - not ported yet
- `OgreBotAPI:Aliases_ShowAllBuiltInAliases` - not ported yet
- `OgreBotAPI:AscensionEmbargo_Add_DoNotCombo` - not ported yet
- `OgreBotAPI:AscensionEmbargo_Change_Disable_Status` - not ported yet
- `OgreBotAPI:AscensionEmbargo_Remove_DoNotCombo` - not ported yet
- `OgreBotAPI:AutoHunt_AddPath` - not ported yet
- `OgreBotAPI:AutoHunt_AddPoint` - not ported yet
- `OgreBotAPI:AutoHunt_ClearPoints` - not ported yet
- `OgreBotAPI:AutoHunt_RemovePoint` - not ported yet
- `OgreBotAPI.bBuyingFromMerchantConfirmation` - not ported yet
- `OgreBotAPI.bCacheEquipmentAdornmentNames` - not ported yet
- `OgreBotAPI.bInternal` - not ported yet
- `OgreBotAPI.bNoCollision` - not ported yet
- `OgreBotAPI.bSetUpFor_HOs_Current_HeroicSurge` - not ported yet
- `OgreBotAPI.bSetUpFor_HOs_Obtained_Current_HeroicSurge` - not ported yet
- `OgreBotAPI:CastAbilityNoExportUntilCast` - not ported yet
- `OgreBotAPI:CastAbilityType` - not ported yet
- `OgreBotAPI:CastHQEar` - not ported yet
- `OgreBotAPI.CastStackAllowHOIcons` - not ported yet
- `OgreBotAPI.CastStackDisableHOIcons` - not ported yet
- `OgreBotAPI:Change_PoisonAutoConsume` - not ported yet
- `OgreBotAPI:DestroyItemByID_NoChecks` - not ported yet
- `OgreBotAPI:DisplayMyAscensionCombos` - not ported yet
- `OgreBotAPI:FastTravel_Report` - not ported yet
- `OgreBotAPI:FastTravelOld` - not ported yet
- `call OgreBotAPI.FindAdornment_ReturnSlot` - not ported yet
- `call OgreBotAPI.FindAdornments_ReturnJSON` - not ported yet
- `OgreBotAPI:Fix_Broken_Shit` - not ported yet
- `OgreBotAPI:FixCastAfterZoneBug` - not ported yet
- `OgreBotAPI:GenerateMyAscensionCombos` - not ported yet
- `OgreBotAPI.Get_AbilityVia` - not ported yet
- `OgreBotAPI.Get_AbilityVia_ref` - not ported yet
- `OgreBotAPI:Get_MissionTimerInfo` - not ported yet
- `OgreBotAPI.Get_NumAdornmentsOfColour` - not ported yet
- `OgreBotAPI:Get_Poisons` - not ported yet
- `OgreBotAPI.GetDeityPoints` - exists, does nothing yet
- `OgreBotAPI:GuidedAscension` - not ported yet
- `OgreBotAPI:HandleLootWindow` - not ported yet
- `OgreBotAPI.HardCodedAbilityEffectRadius` - not ported yet
- `OgreBotAPI.HardCodedAbilityMaxRange` - not ported yet
- `call OgreBotAPI.Interrupt_Mode` - not ported yet
- `OgreBotAPI.IsItemTimeUntilReadyZero` - not ported yet
- `OgreBotAPI:ItemDebug` - not ported yet
- `OgreBotAPI.jvCacheEquipmentAdornmentNames` - not ported yet
- `OgreBotAPI.LandFlyingMountActive` - not ported yet
- `OgreBotAPI:Loot_SmartAssign_Add` - not ported yet
- `OgreBotAPI:Loot_SmartAssign_Update` - not ported yet
- `OgreBotAPI:Mount` - not ported yet
- `OgreBotAPI:Myzer1` - not ported yet
- `OgreBotAPI:Myzer2` - not ported yet
- `OgreBotAPI.ogre_campspot_me` - not ported yet
- `OgreBotAPI:OLD_ChangeOgreBotUIOption` - not ported yet
- `OgreBotAPI:Output_InGame_MovementKeys` - not ported yet
- `OgreBotAPI:Populate_ExportList` - not ported yet
- `OgreBotAPI:PopulatePCOptionLists` - not ported yet
- `OgreBotAPI.PulseCircleMovement_CurrentSpot` - not ported yet
- `OgreBotAPI.PulseCircleMovement_TimerRecentlyMoved` - not ported yet
- `OgreBotAPI:Reload_DevBot` - not ported yet
- `OgreBotAPI:ReloadExport` - not ported yet
- `OgreBotAPI:Report_Back` - not ported yet
- `OgreBotAPI.RoomID` - not ported yet
- `OgreBotAPI:SetQuestion` - not ported yet
- `OgreBotAPI:SetRelayGroup` - not ported yet
- `OgreBotAPI:SetRelayGroup_Relay` - not ported yet
- `OgreBotAPI:SetRelayGroupToDefault` - not ported yet
- `OgreBotAPI:SetRelayGroupToDefault_Relay` - not ported yet
- `OgreBotAPI:SmartLoot_LOL_AssignPlayer_Item` - not ported yet
- `OgreBotAPI.SpecialDebugMode` - not ported yet
- `OgreBotAPI:SpendDeityPoints` - not ported yet
- `OgreBotAPI:SpendDietyPoints` - not ported yet
- `OgreBotAPI:Test_ExportList` - not ported yet
- `OgreBotAPI.Timer_Exit` - not ported yet
- `OgreBotAPI:Travel_Report` - not ported yet
- `OgreBotAPI:TravelBell_Report` - not ported yet
- `OgreBotAPI:TravelDruid_Report` - not ported yet
- `OgreBotAPI:TravelSpires_Report` - not ported yet
- `OgreBotAPI:Update_Guk_Shinies` - not ported yet
- `OgreBotAPI:Update_PoP_Shinies` - not ported yet
- `OgreBotAPI:VampiricRequiem_AbilityCancel` - not ported yet
- `call OgreBotAPI.WaitForCasting` - not ported yet
- `OgreBotAPI.WeaponSlotSubTypes` - not ported yet
- `OgreBotAPI:ZoneInto` - not ported yet
