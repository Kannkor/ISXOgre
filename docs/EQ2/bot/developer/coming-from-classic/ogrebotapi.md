# OgreBotAPI

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../index.md).
</div>

Every name Classic's *OgreBotAPI Reference* page listed, and what it is in the new bot. The flat `OgreBotAPI:Name` list became groups (`OgreBotAPI.Movement`, `OgreBotAPI.Cures`, …): each section below is one group. Use your browser's find (Ctrl+F) with the old name.

> **:warning: An old call does nothing now - it does not give an error**
>
> The new bot does not keep the old names. A call to an old method silently does nothing and a read of an old member gives `NULL`. Find your name below and write what the row says instead.

## At a glance

| What happened | Names |
|---|---|
| ⚠️ Arguments changed | 53 |
| ⚠️ Argument order changed | 6 |
| ✏️ Renamed | 326 |
| ➡️ Moved | 115 |
| ➡️ Lives somewhere else | 7 |
| 📄 In a data file now | 4 |
| ⛔ Exists, does nothing yet | 67 |
| ⛔ Not ported yet | 83 |
| ⛔ Removed | 2 |
| ✅ Works as is | 25 |
| **Total** | **688** |

The camp-spot calls are on the [Camp spot](campspot.md) page, the `Ask` calls on [Ask query system](ask.md) and the `…Preferred` calls on [Preferred group members](preferred.md).

## Worked examples

One real Classic line per kind of change, and the line that replaces it.

### ✏️ Renamed: `OgreBotAPI:ChangeOgreBotUIOption`

```
; before (Classic)
OgreBotAPI:ChangeOgreBotUIOption["all","checkbox_debug_casting",TRUE]
; after (new bot)
OgreBotAPI.Options:Set["all","checkbox_debug_casting",TRUE]
```

### ➡️ Moved: `OgreBotAPI:Pause`

```
; before (Classic)
OgreBotAPI:Pause
; after (new bot)
OgreBotAPI.Bot:Pause
```

## OgreBotAPI.Abilities

Old names whose job is now in `OgreBotAPI.Abilities`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:AbilityEmbargo_AddRotateTimer` | does nothing | `OgreBotAPI.Abilities:AddEmbargo` `[fw,id,durationSec]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. does NOT take a for-who. `[abilityId, durationSeconds]`. Note its sibling `:ClearEmbargo` is `[forwho, abilityName]` - different arg 0, different key type. |
| `OgreBotAPI:AbilityEmbargo_ResetAbilityEmbargo` | does nothing | `OgreBotAPI.Abilities:ClearEmbargo` | ✏️ Renamed |  |
| `OgreBotAPI:AbilityEmbargo_ResetAllAbilityEmbargos` | does nothing | `OgreBotAPI.Abilities:ClearAllEmbargos` | ✏️ Renamed |  |
| `OgreBotAPI.AbilityReady` | reads NULL | `OgreBotAPI.Abilities.Ready` | ✏️ Renamed |  |
| `OgreBotAPI:AbilityTracker_Add` | does nothing | `OgreBotAPI.Abilities:TrackerAdd` | ✏️ Renamed |  |
| `OgreBotAPI:ApplyVerbForWho` | does nothing | `OgreBotAPI.Abilities:ApplyVerbFor` | ✏️ Renamed |  |
| `OgreBotAPI:ApplyVerbIDForWho` | does nothing | `OgreBotAPI.Abilities:ApplyVerbIDFor` | ✏️ Renamed |  |
| `OgreBotAPI:ApplyVerbQueuedForWho` | does nothing | `OgreBotAPI.Abilities:ApplyVerbQueuedFor` | ✏️ Renamed |  |
| `OgreBotAPI.CancelCasting` | reads NULL | `OgreBotAPI.Abilities:CancelCasting` | ➡️ Moved |  |
| `OgreBotAPI:CancelCasting_OLD` | does nothing (stub) | `OgreBotAPI.Abilities:CancelCastingOld` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI.CancelCurrentCast` | reads NULL | `OgreBotAPI.Abilities:SetCancelCurrentCast` | ✏️ Renamed |  |
| `OgreBotAPI:CancelGroupWaterBreathing` | does nothing | `OgreBotAPI.Abilities:CancelGroupWaterBreathing` | ➡️ Moved |  |
| `call OgreBotAPI.CancelInvis` | does nothing | `OgreBotAPI.Abilities:CancelInvis` | ➡️ Moved |  |
| `OgreBotAPI:CancelMaintained` | does nothing | `OgreBotAPI.Abilities:CancelMaintained` | ➡️ Moved | does NOT take a for-who. Argument 0 is an ability name, exactly as in Classic. `OgreBotAPI.Abilities:CancelMaintainedFor["all","Sprint"]` is the gated twin. Doc 21 lists this verb as having gained a for-who; the implementation says otherwise and the implementation is what runs. |
| `OgreBotAPI:CancelMaintainedForWho` | does nothing | `OgreBotAPI.Abilities:CancelMaintainedFor` | ✏️ Renamed | the gated twin, renamed to `:CancelMaintainedFor`. For-who at arg 0, ability names from arg 1. |
| `OgreBotAPI:Cast_Interrupt` | does nothing | `OgreBotAPI.Abilities:CastInterrupt` `[fw,mobNameOrId,calledFrom]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it.<br>Not taken any more: `_CalledFrom`. |
| `OgreBotAPI:CastAbility` | does nothing | `OgreBotAPI.Abilities:Cast` | ✏️ Renamed |  |
| `OgreBotAPI:CastAbility_Relay` | does nothing | `OgreBotAPI.Abilities:CastRelay` | ✏️ Renamed |  |
| `OgreBotAPI:CastAbility_Via` | does nothing | `OgreBotAPI.Abilities:CastVia` | ✏️ Renamed |  |
| `OgreBotAPI:CastAbilityInSeconds` | does nothing | `OgreBotAPI.Abilities:CastInSeconds` | ✏️ Renamed | `[fw, ability, delay, calledFrom]` - positionally identical to Classic. A BARE delay is SECONDS: the scheduler's global default is milliseconds, and this verb overrides it because its name states the unit, so `[...,25]` is 25 seconds exactly as Classic meant it. An explicit unit still wins (`"500ms"`, `"2m"`), and a bare decimal is legal (Classic took a `float`). `calledFrom` rides through to the cast log's "called from:" label - pass it, it is how you find where a cast came from. Ability may be an id or a NAME (names resolve off the export catalog, no server call). |
| `OgreBotAPI:CastAbilityInSeconds_Relay` | does nothing | `OgreBotAPI.Abilities:CastInSeconds` | ✏️ Renamed | see `CastAbilityInSeconds` for the arguments - and note the bare-delay-is-SECONDS rule. |
| `OgreBotAPI:CastAbilityNoChecks` | does nothing | `OgreBotAPI.Abilities:CastNoChecks` | ✏️ Renamed |  |
| `OgreBotAPI:CastAbilityNoExport` | does nothing | `OgreBotAPI.Abilities:CastNoExport` | ✏️ Renamed |  |
| `OgreBotAPI:CastAbilityNoExport_Relay` | does nothing | `OgreBotAPI.Abilities:CastNoExportRelay` | ✏️ Renamed |  |
| `OgreBotAPI:CastAbilityOnNPC` | does nothing | `OgreBotAPI.Abilities:CastOnNPC` | ✏️ Renamed |  |
| `OgreBotAPI:CastAbilityOnPlayer` | does nothing | `OgreBotAPI.Abilities:CastOnPlayer` | ✏️ Renamed |  |
| `OgreBotAPI:CastAbilityOnPlayer_Relay` | does nothing | `OgreBotAPI.Abilities:CastOnPlayerRelay` | ✏️ Renamed |  |
| `OgreBotAPI:CastAbilityOnPlayerInSeconds` | does nothing | `OgreBotAPI.Abilities:CastOnPlayerInSeconds` `[fw,ability,player,seconds,calledFrom]` | ⚠️ Arguments changed | The arguments are different: Classic took `(string _ForWho, string AbilityName, string sTarget=${Me.Name}, float _Seconds)`, the new call takes `[fw,ability,player,seconds,calledFrom]`. the command must be ONE QUOTED argument - LavishScript ends the outer call at the first `]` otherwise. Unlike `:CastInSeconds`, `Util:DelayedAction` keeps the scheduler's default: a BARE number there is MILLISECONDS, so write `"10s"`. |
| `OgreBotAPI:CastAbilityOnPlayerNoChecks` | does nothing | `OgreBotAPI.Abilities:CastOnPlayerNoChecks` `[fw,ability,player,calledFrom]` | ✏️ Renamed |  |
| `OgreBotAPI:CastBulwarkImmediately` | does nothing | `OgreBotAPI.Abilities:CastBulwark` | ✏️ Renamed |  |
| `OgreBotAPI:CastedCastOnTheMove` | does nothing | `OgreBotAPI.Abilities:AnnounceCasted` | ✏️ Renamed |  |
| `OgreBotAPI:CastGroupWaterBreathing` | does nothing | `OgreBotAPI.Abilities:CastGroupWaterBreathing` | ➡️ Moved |  |
| `OgreBotAPI:CastHOIconID` | does nothing | `OgreBotAPI.Abilities:CastHOIcon` | ✏️ Renamed |  |
| `OgreBotAPI:CastingCastOnTheMove` | does nothing | `OgreBotAPI.Abilities:AnnounceCasting` | ✏️ Renamed |  |
| `OgreBotAPI:CastRescue` | does nothing | `OgreBotAPI.Abilities:CastRescue` `[fw,...opts]` | ➡️ Moved |  |
| `OgreBotAPI:Disable_Dispells` | does nothing | `OgreBotAPI.Abilities:SetDispellsEnabled` | ✏️ Renamed |  |
| `OgreBotAPI:Disable_Interrupts` | does nothing | `OgreBotAPI.Abilities:SetInterruptsEnabled` | ✏️ Renamed |  |
| `OgreBotAPI:Disable_Stuns` | does nothing | `OgreBotAPI.Abilities:SetStunsEnabled` | ⚠️ Arguments changed | the OFF half. You must pass `FALSE` after the for-who: `OgreBotAPI.Abilities:SetStunsEnabled["all",FALSE]`. A bare `[FALSE]` puts FALSE in the for-who slot and addresses the call to nobody. Pass FALSE as the value argument. |
| `OgreBotAPI:Enable_Dispells` | does nothing | `OgreBotAPI.Abilities:SetDispellsEnabled` | ✏️ Renamed |  |
| `OgreBotAPI:Enable_Interrupts` | does nothing | `OgreBotAPI.Abilities:SetInterruptsEnabled` | ✏️ Renamed |  |
| `OgreBotAPI:Enable_Stuns` | does nothing | `OgreBotAPI.Abilities:SetStunsEnabled` | ⚠️ Arguments changed | the ON half of a collapsed polarity pair. `OgreBotAPI.Abilities:SetStunsEnabled["all",TRUE]` (TRUE is the default, so `["all"]` also works). Pass TRUE as the value argument. |
| `OgreBotAPI.Get_AbilityInfo` | reads NULL | `OgreBotAPI.Abilities.Info` | ✏️ Renamed |  |
| `OgreBotAPI.Get_AbilityInfo_RawData` | reads NULL | `OgreBotAPI.Abilities.InfoRaw` | ✏️ Renamed |  |
| `OgreBotAPI.Get_AbilityShortName` | reads NULL | `OgreBotAPI.Abilities.ShortName` | ✏️ Renamed |  |
| `OgreBotAPI.Get_AbilityTypeID` | reads NULL | `OgreBotAPI.Abilities.TypeID` | ✏️ Renamed |  |
| `OgreBotAPI.Get_AbilityTypeID_Ref` | reads NULL | `OgreBotAPI.Abilities.TypeIDRef` | ✏️ Renamed |  |
| `OgreBotAPI.Get_AbilityVia` | reads NULL | — | ⛔ Not ported yet |  |
| `OgreBotAPI.Get_AbilityVia_ref` | reads NULL | — | ⛔ Not ported yet | as Get_AbilityVia |
| `OgreBotAPI.Get_HOIconAbility` | reads NULL | `OgreBotAPI.Abilities.HOIconAbility` | ✏️ Renamed |  |
| `OgreBotAPI.Get_InterruptID` | reads NULL | `OgreBotAPI.Abilities.InterruptID` | ✏️ Renamed |  |
| `OgreBotAPI.Get_RotationData` | does nothing (stub) | `OgreBotAPI.Abilities.RotationData` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI.GetAbilityID` | reads NULL | `OgreBotAPI.Abilities.ID` | ✏️ Renamed |  |
| `OgreBotAPI.HaveMaintained` | reads NULL | `OgreBotAPI.Abilities.HaveMaintained` | ➡️ Moved |  |
| `OgreBotAPI:ItemEmbargo_AddRotateTimer` | does nothing | `OgreBotAPI.Abilities:AddEmbargo` `[fw,id,durationSec]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. same verb as `AbilityEmbargo_AddRotateTimer` - they shared one id store and are one verb now. `[id, durationSeconds]`, no for-who. |
| `OgreBotAPI:NoCasting` | does nothing | `OgreBotAPI.Abilities:NoCasting` | ➡️ Moved |  |
| `OgreBotAPI:Rebuff` | does nothing | `OgreBotAPI.Abilities:Rebuff` | ➡️ Moved |  |
| `OgreBotAPI:ResetFor_Dispells` | does nothing | `OgreBotAPI.Abilities:SetUpForDispells` | ⚠️ Arguments changed | the OFF half of `SetUpFor_Dispells`: `OgreBotAPI.Abilities:SetUpForDispells["all",FALSE]`. Not the same toggle as `Enable_/Disable_Dispells`, which is the master checkbox. Pass FALSE as the value argument. |
| `OgreBotAPI:ResolveBuffCheck` | does nothing (stub) | `OgreBotAPI.Abilities:ResolveBuffCheck` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI.ScrollOf_Get_MaintainedDuration` | reads NULL | `OgreBotAPI.Abilities.ScrollMaintainedDuration` | ✏️ Renamed |  |
| `OgreBotAPI:Set_DisableAllAOEs` | does nothing | `OgreBotAPI.Abilities:SetAOEsDisabled` | ✏️ Renamed |  |
| `OgreBotAPI:Set_VampiricRequiem_Cancelling_Active` | does nothing (stub) | `OgreBotAPI.Abilities:SetVampiricRequiemCancelling` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:SetUpFor_Dispells` | does nothing | `OgreBotAPI.Abilities:SetUpForDispells` | ✏️ Renamed |  |
| `OgreBotAPI:Spew_Get_AbilityVia` | does nothing (stub) | `OgreBotAPI.Abilities:SpewAbilityVia` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:SpewAbility` | does nothing (stub) | `OgreBotAPI.Abilities:SpewAbility` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |

## OgreBotAPI.Actors

Old names whose job is now in `OgreBotAPI.Actors`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:Actor_Click` | does nothing | `OgreBotAPI.Actors:Click` `[fw,nameOrId,...]` | ✏️ Renamed |  |
| `OgreBotAPI:Actor_ClickQueued` | does nothing | `OgreBotAPI.Actors:ClickQueued` `[fw,nameOrId,...]` | ✏️ Renamed | Not taken any more: `_WaitTime`. |
| `OgreBotAPI:AltarOfTheAncients` | does nothing | `OgreBotAPI.Actors:ClickQueued` `[fw,nameOrId,...]` | ✏️ Renamed |  |
| `OgreBotAPI:ApplyVerb` | does nothing | `OgreBotAPI.Actors:ApplyVerb` `[fw,actor,verb]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. |
| `OgreBotAPI:ApplyVerbID` | does nothing | `OgreBotAPI.Actors:ApplyVerbID` `[fw,actorId,verb]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. |
| `OgreBotAPI:ApplyVerbIDQueuedForWho` | does nothing | `OgreBotAPI.Actors:ApplyVerbIDQueued` `[fw,actorId,verb,waitDs=40]` | ✏️ Renamed |  |
| `OgreBotAPI.CursorActor_Tooltip_Text` | does nothing (stub) | `OgreBotAPI.Actors.CursorTooltipText` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI.CursorActor_Tooltip_Visible` | does nothing (stub) | `OgreBotAPI.Actors.CursorTooltipVisible` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI.Get_CurrentImmunityRune` | reads NULL | `OgreBotAPI.Actors.CurrentImmunityRune` | ✏️ Renamed |  |
| `OgreBotAPI.GetActorCountByName` | reads NULL | `OgreBotAPI.Actors.CountByName` `[name,...]` | ✏️ Renamed |  |
| `OgreBotAPI.GetActorCountByType` | reads NULL | `OgreBotAPI.Actors.CountByType` `[-distance F,-Type S]` | ⚠️ Arguments changed | The arguments are different: Classic took `(... Args)`, the new call takes `[-distance F,-Type S]`. |
| `OgreBotAPI.GetMobID` | reads NULL | `OgreBotAPI.Actors.MobID` `[name]` | ✏️ Renamed |  |
| `OgreBotAPI:HailNPC` | does nothing | `OgreBotAPI.Actors:Hail` `[fw,nameOrId]` | ✏️ Renamed |  |
| `OgreBotAPI.IsAPC` | reads NULL | `OgreBotAPI.Actors.IsPC` `[nameOrId]` | ✏️ Renamed |  |
| `OgreBotAPI:NPC_CastMonitoring` | does nothing (stub) | `OgreBotAPI.Actors:SetCastMonitoring` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI.NPCsWithinRange` | does nothing (stub) | `OgreBotAPI.Actors.NPCsWithin` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
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
| `OgreBotAPI:Assist` | does nothing | `OgreBotAPI.Assist:Anchor` `[fw, who]` | ⚠️ Argument order changed | The for-who moved from argument 2 to argument 1 (first). put the for-who at slot 1, behind the person being assisted. The new form is contract-shaped: `OgreBotAPI.Assist:Anchor["<forwho>","<who to assist>"]`. |
| `OgreBotAPI:AssistForWho` | does nothing | `OgreBotAPI.Assist:Anchor` `[fw, who]` | ✏️ Renamed |  |
| `OgreBotAPI.GetAssistID` | reads NULL | `OgreBotAPI.Assist.TargetID` | ✏️ Renamed |  |
| `OgreBotAPI.InControlOfAssisting` | reads NULL | `OgreBotAPI.Assist.InControl` | ✏️ Renamed |  |
| `OgreBotAPI.IsAssisting` | reads NULL | `OgreBotAPI.Assist.IsAssisting` | ➡️ Moved |  |
| `OgreBotAPI:NoTarget` | works | — | ✅ Works as is |  |
| `OgreBotAPI:Prepare_TankSwapping` | does nothing (stub) | `OgreBotAPI:Prepare_TankSwapping` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:ResetFor_Intercept` | works | — | ✅ Works as is |  |
| `OgreBotAPI:SetUpFor_Intercept` | works | — | ✅ Works as is |  |
| `OgreBotAPI:Target` | works | — | ✅ Works as is |  |
| `OgreBotAPI:UpdateNPCTarget` | works | — | ✅ Works as is |  |
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
| `OgreBotAPI:AutoTarget_AddActor` | does nothing | `OgreBotAPI.AutoTarget:AddActor` `[fw, name, minHP, checkCollision, aggroOnGroupOnly, maxHP, aggroOnNonFighterOnly, aggroOnNotMe]` | ✏️ Renamed |  |
| `OgreBotAPI:AutoTarget_Clear` | does nothing | `OgreBotAPI.AutoTarget:Clear` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:AutoTarget_ClearActors` | does nothing | `OgreBotAPI.AutoTarget:Clear` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:AutoTarget_Disable` | does nothing | `OgreBotAPI.AutoTarget:Suppress` `[fw, reason]` | ✏️ Renamed | suppression is keyed: `:Suppress["all","YOUR_KEY"]`, released by the same key. It is not a boolean. |
| `OgreBotAPI.AutoTarget_Disabled` | reads NULL | `OgreBotAPI.AutoTarget.Suppressed` `[key]` | ✏️ Renamed |  |
| `OgreBotAPI:AutoTarget_Enable` | does nothing | `OgreBotAPI.AutoTarget:Release` `[fw, reason]` | ✏️ Renamed | releases a keyed suppression: `:Release["all","YOUR_KEY"]`. |
| `OgreBotAPI.AutoTarget_Enabled` | reads NULL | `OgreBotAPI.AutoTarget.Enabled` | ✏️ Renamed |  |
| `OgreBotAPI:AutoTarget_RemoveActor` | does nothing | `OgreBotAPI.AutoTarget:RemoveActor` `[fw, name]` | ✏️ Renamed |  |
| `OgreBotAPI:AutoTarget_SetRescanTime` | does nothing | `OgreBotAPI.AutoTarget:SetRescanTime` `[fw, n]` | ✏️ Renamed |  |
| `OgreBotAPI:AutoTarget_SetScanHeight` | does nothing | `OgreBotAPI.AutoTarget:SetScanHeight` `[fw, n]` | ✏️ Renamed |  |
| `OgreBotAPI:AutoTarget_SetScanRadius` | does nothing | `OgreBotAPI.AutoTarget:SetScanRadius` `[fw, n]` | ✏️ Renamed |  |

## OgreBotAPI.Bot

Old names whose job is now in `OgreBotAPI.Bot`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:CampToDesktop` | does nothing | `OgreBotAPI.Bot:CampToDesktop` `[fw]` | ➡️ Moved | Not taken any more: `_LoginOnly`. |
| `OgreBotAPI:DisplayAvailableSetups` | does nothing (stub) | `OgreBotAPI.Bot:ListSetups` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:End_Bot` | does nothing | `OgreBotAPI.Bot:End` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:ExitClient` | does nothing | `OgreBotAPI.Bot:ExitClient` `[fw,seconds=30]` | ➡️ Moved |  |
| `OgreBotAPI:FlushQueued` | does nothing (stub) | `OgreBotAPI.Bot:FlushQueued` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI.Get_ScriptBaseName` | reads NULL | `OgreBotAPI.Bot.ScriptBaseName` `[path,removeExtension=TRUE]` | ✏️ Renamed |  |
| `OgreBotAPI.Get_Turbo` | does nothing (stub) | `OgreBotAPI.Bot.Turbo` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:Initialize` | does nothing | `OgreBotAPI.Bot:Initialize` `[fw,...]` | ➡️ Moved |  |
| `OgreBotAPI:OnDeactivate` | does nothing | `OgreBotAPI.Bot:OnDeactivate` `[...]` | ➡️ Moved |  |
| `OgreBotAPI:Pause` | does nothing | `OgreBotAPI.Bot:Pause` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI.Paused` | reads NULL | `OgreBotAPI.Bot.Paused` | ➡️ Moved |  |
| `OgreBotAPI.QueuedCommands` | does nothing (stub) | `OgreBotAPI.Bot.QueuedCommands` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:Reload_Bot` | does nothing | `OgreBotAPI.Bot:Reload` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:Resume` | does nothing | `OgreBotAPI.Bot:Resume` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI:SetUpFor` | does nothing | `OgreBotAPI.Bot:SetUpFor` `[fw,what]` | ➡️ Moved |  |
| `OgreBotAPI.SourceAvailable` | does nothing (stub) | `OgreBotAPI.Bot.SourceAvailable` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:Update_Turbo` | does nothing (stub) | `OgreBotAPI.Bot:SetTurbo` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |

## OgreBotAPI.CastStack

Old names whose job is now in `OgreBotAPI.CastStack`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:AbilityTag_AddRotateTagTimer` | does nothing | `OgreBotAPI.CastStack:HoldTag` `[fw,tag,duration,type,-m]` | ⚠️ Arguments changed | The arguments are different: Classic took `(string _ForWho, string _TagName, uint _Duration, ... Args)`, the new call takes `[fw,tag,duration,type,-m]`. |
| `OgreBotAPI.AbilityTag_GetTagAllowTimeRemaining` | reads NULL | `OgreBotAPI.CastStack.TagAllowRemaining` `[tag]` | ✏️ Renamed | was a stub returning FALSE, read as "expired". |
| `OgreBotAPI.AbilityTag_GetTagEmbargoTimeRemaining` | reads NULL | `OgreBotAPI.CastStack.TagEmbargoRemaining` `[tag]` | ✏️ Renamed | was a stub returning FALSE, read as "expired". It answers the clock, not liveness - a tag coupled to a maintained buff reports 0 and is still active. |
| `OgreBotAPI:AbilityTag_ResetAbilityTagAllow` | does nothing | `OgreBotAPI.CastStack:ClearAllow` `[fw,tag]` | ✏️ Renamed |  |
| `OgreBotAPI:AbilityTag_ResetAbilityTagEmbargo` | does nothing | `OgreBotAPI.CastStack:ClearEmbargo` `[fw,tag]` | ✏️ Renamed |  |
| `OgreBotAPI:AbilityTag_ResetAllAbilityTagAllows` | does nothing | `OgreBotAPI.CastStack:ClearAllAllows` | ✏️ Renamed |  |
| `OgreBotAPI:AbilityTag_ResetAllAbilityTagEmbargos` | does nothing | `OgreBotAPI.CastStack:ClearAllEmbargos` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:ChangeCastStackListBoxItem` | does nothing | `OgreBotAPI.CastStack:SetEntry` `[fw,ability,TRUE\|FALSE\|toggle]` | ✏️ Renamed | Not taken any more: `_SilentMode`. |
| `OgreBotAPI:ChangeCastStackListBoxItemByTag` | does nothing | `OgreBotAPI.CastStack:SetEntryByTag` `[fw,tag,TRUE\|FALSE\|toggle]` | ✏️ Renamed | Not taken any more: `_Partial`, `_SilentMode`. |

## OgreBotAPI.Client

Old names whose job is now in `OgreBotAPI.Client`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:ChangeRadarYAxis` | does nothing | `OgreBotAPI.Client:SetRadarYAxis` `[fw,value]` | ✏️ Renamed |  |
| `OgreBotAPI:ResetCameraAngle` | does nothing | `OgreBotAPI.Client:ResetCamera` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:Set_CameraPitch` | does nothing | `OgreBotAPI.Client:SetCameraPitch` `[fw,pitch]` | ✏️ Renamed |  |
| `OgreBotAPI:SetMousePosition` | does nothing | `OgreBotAPI.Client:SetMousePosition` `[fw,x,y]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. |
| `OgreBotAPI:SetMousePosition_Middle` | does nothing | `OgreBotAPI.Client:SetMousePositionMiddle` `[fw]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. |

## OgreBotAPI.Combat

Old names whose job is now in `OgreBotAPI.Combat`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:AddNoOffensiveOn` | does nothing | `OgreBotAPI.Combat:AddNoOffensive` `[fw,mobName,exactOnly=FALSE]` | ✏️ Renamed |  |
| `OgreBotAPI.bNoReqBowAbilities` | reads NULL | `OgreBotAPI.Combat.NoReqBowAbilities` | ✏️ Renamed |  |
| `OgreBotAPI.CheckNoDefensiveOn` | reads NULL | `OgreBotAPI.Combat.NoDefensive` | ✏️ Renamed |  |
| `OgreBotAPI.CheckNoOffensiveOn` | reads NULL | `OgreBotAPI.Combat.NoOffensive` | ✏️ Renamed |  |
| `OgreBotAPI.CheckNoReqBowAbilities` | reads NULL | `OgreBotAPI.Combat.NoReqBowAbilities` | ✏️ Renamed |  |
| `OgreBotAPI:ClearNoOffensiveOn` | does nothing | `OgreBotAPI.Combat:ClearNoOffensive` `[fw,...]` | ✏️ Renamed |  |
| `OgreBotAPI:Countdown` | does nothing | `OgreBotAPI.Combat:Countdown` `[fw,seconds,...]` | ➡️ Moved |  |
| `OgreBotAPI.InCombat` | reads NULL | `OgreBotAPI.Combat.InCombat` | ➡️ Moved |  |
| `OgreBotAPI.IsReady` | reads NULL | `OgreBotAPI.Combat.IsReady` | ➡️ Moved |  |
| `OgreBotAPI.MaybeAnotherTime_CheckNoOffensive` | reads NULL | `OgreBotAPI.Combat.MaybeAnotherTime` | ✏️ Renamed |  |
| `OgreBotAPI.NoOffensiveOn` | reads NULL | `OgreBotAPI.Combat.NoOffensive` | ✏️ Renamed |  |
| `OgreBotAPI:SetNoDefensive` | does nothing | `OgreBotAPI.Combat:SetNoDefensive` `[fw,on,reason]` | ⚠️ Arguments changed | The arguments are different: Classic took `(string _ForWho=all, bool _Value=TRUE)`, the new call takes `[fw,on,reason]`. |
| `OgreBotAPI:SetNoReqBowAbilities` | does nothing | `OgreBotAPI.Combat:SetNoReqBowAbilities` `[fw,on]` | ➡️ Moved |  |
| `OgreBotAPI.ThreatFighterIgnoreList` | reads NULL | `OgreBotAPI.Combat:ThreatIgnoreList` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:ThreatFighterIgnoreList_Add` | does nothing | `OgreBotAPI.Combat:ThreatIgnoreAdd` `[fw,name]` | ⚠️ Arguments changed | The arguments are different: Classic took `(string _ForWho="all", ... Args)`, the new call takes `[fw,name]`. |
| `OgreBotAPI:ThreatFighterIgnoreList_Clear` | does nothing | `OgreBotAPI.Combat:ThreatIgnoreClear` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:ThreatFighterIgnoreList_List` | does nothing | `OgreBotAPI.Combat:ThreatIgnoreList` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:ThreatFighterIgnoreList_Remove` | does nothing | `OgreBotAPI.Combat:ThreatIgnoreRemove` `[fw,name...]` | ✏️ Renamed |  |
| `OgreBotAPI.Zoning` | reads NULL | `OgreBotAPI.Combat.Zoning` | ➡️ Moved |  |

## OgreBotAPI.Comms

Old names whose job is now in `OgreBotAPI.Comms`.

**Note A** (3 rows below): Nothing is broken today - there is exactly ONE group, so nothing can leave it and nothing can become unreachable. `oc` cannot substitute: it rides a FIXED group (`"relayGroup": "ogre_everquest2"`, one per game), so a session that moved to another group cannot be called back by a broadcast confined to the one it left. If fleet partitioning is ever wanted, mutable groups and cross-group addressing must land TOGETHER. See the 'Relay groups - PARKED' entry in.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:Announce_AddEntry` | does nothing (stub) | `OgreBotAPI.Comms:AddAnnounce` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:ConversationBubble` | does nothing | `OgreBotAPI.Comms:ConversationBubble` `[fw,...]` | ➡️ Moved |  |
| `OgreBotAPI:ConversationBubbleSpew` | does nothing (stub) | `OgreBotAPI.Comms:SpewConversationBubbles` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:ExecuteEvent` | does nothing | `OgreBotAPI.Comms:ExecuteEvent` `[fw,name,...]` | ➡️ Moved |  |
| `OgreBotAPI:ExecuteEvent_JSON` | does nothing | `OgreBotAPI.Comms:ExecuteEventJSON` `[fw,name,json]` | ⚠️ Arguments changed | The arguments are different: Classic took `(string _ForWho="all", string _EventName, ... Args)`, the new call takes `[fw,name,json]`. |
| `OgreBotAPI:InjectChat` | does nothing | `OgreBotAPI.Comms:InjectChat` `[fw,chat]` | ➡️ Moved |  |
| `OgreBotAPI:Message` | does nothing | `OgreBotAPI.Comms:Message` `[fw,text]` | ⚠️ Arguments changed | moved to `OgreBotAPI.Comms:Message` - renders on THIS session only. Classic's positional `noise, NoiseToPlay` became FLAGS after the text (2026-10-16): `-sound ding` (Classic `TRUE` / `Default`) or `-sound alarm` (Classic `Loud`) - both PLAY (ding.wav / chatalarm.wav, Ogre/Common/OgreSounds) - and `-tab <name>` (repeatable) also shows the line in that OgreConsole tab. A leftover positional `TRUE` is just ignored (no sound). SIGNATURE CHANGED - drop the positional noise / NoiseToPlay pair; for a sound put `"-sound","ding"` (Classic TRUE / Default) or `"-sound","alarm"` (Classic Loud) after the text. `"-tab","<name>"` also shows the line in that OgreConsole tab. |
| `OgreBotAPI:Message_NT` | does nothing | `OgreBotAPI.Comms:Message` `[fw,text]` | ⚠️ Arguments changed | identical to `Message` - the "no timestamp" distinction stopped existing when the stamp was removed. Classic's positional `noise, NoiseToPlay` became FLAGS after the text (2026-10-16): `-sound ding` (Classic `TRUE` / `Default`) or `-sound alarm` (Classic `Loud`) - both PLAY (ding.wav / chatalarm.wav, Ogre/Common/OgreSounds) - and `-tab <name>` (repeatable) also shows the line in that OgreConsole tab. A leftover positional `TRUE` is just ignored (no sound). SIGNATURE CHANGED - drop the positional noise / NoiseToPlay pair; for a sound put `"-sound","ding"` (Classic TRUE / Default) or `"-sound","alarm"` (Classic Loud) after the text. `"-tab","<name>"` also shows the line in that OgreConsole tab. |
| `OgreBotAPI:Message_Relay` | does nothing | `OgreBotAPI.Comms:Broadcast` `[fw,text]` | ⚠️ Arguments changed | renamed to `:Broadcast`. `:Message` renders locally; `:Broadcast` reaches the fleet. Classic's positional `noise, NoiseToPlay` became FLAGS after the text (2026-10-16): `-sound ding` (Classic `TRUE` / `Default`) or `-sound alarm` (Classic `Loud`) - both PLAY (ding.wav / chatalarm.wav, Ogre/Common/OgreSounds) - and `-tab <name>` (repeatable) also shows the line in that OgreConsole tab. A leftover positional `TRUE` is just ignored (no sound). SIGNATURE CHANGED - drop the positional noise / NoiseToPlay pair; for a sound put `"-sound","ding"` (Classic TRUE / Default) or `"-sound","alarm"` (Classic Loud) after the text. `"-tab","<name>"` also shows the line in that OgreConsole tab. |
| `OgreBotAPI:OgreIRC_AuthIfInRaid` | does nothing | `OgreBotAPI.Comms:IrcAuthIfInRaid` `[fw,name]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it.<br>Not taken any more: `ToonName`. |
| `OgreBotAPI:OptNum` | does nothing | `OgreBotAPI.Comms:ConversationBubble` `[fw,...]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. |
| `OgreBotAPI:Pushover` | does nothing | `OgreBotAPI.Comms:Pushover` `[fw,message...,-title t,-priority n]` | ➡️ Moved |  |
| `OgreBotAPI:Report_ClearList` | does nothing (stub) | `OgreBotAPI.Comms:ReportClear` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI.Report_Group_GetKey` | does nothing (stub) | `OgreBotAPI.Comms.ReportKey` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI.Report_Group_GetValue` | does nothing (stub) | `OgreBotAPI.Comms.ReportValue` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:Report_SpewList` | does nothing (stub) | `OgreBotAPI.Comms:ReportSpew` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:ReportForList_IRC` | does nothing (stub) | `OgreBotAPI.Comms:ReportListIrc` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:Reporting` | does nothing (stub) | `OgreBotAPI.Comms:Reporting` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:Send_Tell` | does nothing | `OgreBotAPI.Comms:SendTell` `[speaker,...]` | ✏️ Renamed | Not taken any more: `Message`. |
| `OgreBotAPI:SetRelayGroup` | does nothing (stub) | `OgreBotAPI.Comms:SetRelayGroup` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
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
| `OgreBotAPI:ScrollOf` | does nothing | `OgreBotAPI.Consumables:ScrollOf` `[fw,name]` | ➡️ Moved | Not taken any more: `_CancelIfDurationLessThan`, `_UseBest`. |
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
| `OgreBotAPI.DetrimentalInfo` | reads NULL | `OgreBotAPI.Cures.Detrimental` `[main,back,actorId,field]` | ✏️ Renamed |  |
| `OgreBotAPI.DetrimentalInfo_ref` | reads NULL | `OgreBotAPI.Cures.Detrimental` `[main,back,actorId,field]` | ⚠️ Arguments changed | The arguments are different: Classic took `(weakref _IconIDs, int64 _ActorID=${Me.ID}, string _Return="exists")`, the new call takes `[main,back,actorId,field]`. Watch the icon pair order. Classic's `Object_IconIDs` declares the BACKDROP icon FIRST: `variable Object_IconIDs X=A B` means main=B, backdrop=A. The new call takes `[main,back,actorId,field]`, so `X=815 33803` becomes `Detrimental[33803,815,<actorId>]`. Copying the numbers left-to-right compiles, runs, and asks about a detriment nobody has. If the script's own comment names the icons the other way round, Classic read them backdrop-first anyway - convert what Classic actually checked, and say so in your report. |
| `OgreBotAPI.DetrimentalInfo_ref_String` | reads NULL | `OgreBotAPI.Cures.DetrimentalText` `[main,back,actorId,field]` | ⚠️ Arguments changed | The arguments are different: Classic took `(weakref _IconIDs, int64 _ActorID=${Me.ID}, string _Return="exists")`, the new call takes `[main,back,actorId,field]`. Watch the icon pair order. Classic's `Object_IconIDs` declares the BACKDROP icon FIRST: `variable Object_IconIDs X=A B` means main=B, backdrop=A. The new call takes `[main,back,actorId,field]`, so `X=815 33803` becomes `Detrimental[33803,815,<actorId>]`. Copying the numbers left-to-right compiles, runs, and asks about a detriment nobody has. If the script's own comment names the icons the other way round, Classic read them backdrop-first anyway - convert what Classic actually checked, and say so in your report. |
| `OgreBotAPI.DetrimentalInfo_String` | reads NULL | `OgreBotAPI.Cures.DetrimentalText` `[main,back,actorId,field]` | ✏️ Renamed |  |
| `OgreBotAPI:Disable_Cures` | does nothing | `OgreBotAPI.Cures:SetEnabled` `[fw,on=TRUE]` | ✏️ Renamed |  |
| `OgreBotAPI:Enable_Cures` | does nothing | `OgreBotAPI.Cures:SetEnabled` `[fw,on=TRUE]` | ✏️ Renamed |  |
| `OgreBotAPI:Get_CurePotions` | does nothing | `OgreBotAPI.Cures:ReplenishPotions` `[fw,all\|arcane\|elemental\|noxious\|trauma]` | ✏️ Renamed | as Get_FoodDrink - the new verb acts, it does not return the name |
| `OgreBotAPI.Get_CursedID` | reads NULL | `OgreBotAPI.Cures.CursedID` `[-archetype X\|-uncurable\|-uncurableonly\|-GroupOnly]` | ⚠️ Arguments changed | The arguments are different: Classic took `(... Args)`, the new call takes `[-archetype X\|-uncurable\|-uncurableonly\|-GroupOnly]`. |
| `OgreBotAPI.Get_CursedID_ArchetypeCheck` | reads NULL | `OgreBotAPI.Cures.CursedID` `[-archetype X\|-uncurable\|-uncurableonly\|-GroupOnly]` | ✏️ Renamed | was a stub returning FALSE. Use `.CursedID` with the `-archetype` option, which is what this was meant to do. pass the -archetype option<br>Not taken any more: `_ActorID`. |
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

**Note A** (3 rows below): The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI.bDebugLoading` | reads NULL | `OgreBotAPI.Debug.DebugLoading` | ✏️ Renamed |  |
| `OgreBotAPI.CheckVersion` | reads NULL | `OgreBotAPI.Debug.CheckVersion` `[fw,compareTo]` | ➡️ Moved |  |
| `OgreBotAPI.DebugMessage` | reads NULL | `OgreBotAPI.Debug.DebugPrefix` | ✏️ Renamed |  |
| `OgreBotAPI:Echo` | does nothing | `OgreBotAPI.Debug:Echo` `[fw,text]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it.<br>Not taken any more: `_Message2`. |
| `OgreBotAPI.Get_DebugLoading` | reads NULL | `OgreBotAPI.Debug.DebugLoading` | ✏️ Renamed |  |
| `OgreBotAPI:Get_Faction` | does nothing | `OgreBotAPI.Debug:BroadcastStat` `[fw,type,value]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. Classic's second argument was a spewstat OBJECT to fill; the new verb emits the rows itself. The READ half, `Debug.SpewStat`, is a STUB. |
| `OgreBotAPI:SetDebugLoading` | does nothing | `OgreBotAPI.Debug:SetDebugLoading` `[fw,on=TRUE]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. gained a for-who; argument 0 *was* the bool. |
| `OgreBotAPI:SetDebugMode` | does nothing | `OgreBotAPI.Debug:SetDebugMode` `[fw,on=TRUE]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. gained a for-who; argument 0 *was* the bool. |
| `OgreBotAPI:Spew_BoZ_Research` | does nothing | `OgreBotAPI.Debug:SpewResearchWindow` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:Spew_InternalVariables` | does nothing | `OgreBotAPI.Debug:SpewInternalVariables` `[fw]` | ⚠️ Arguments changed | Note A |
| `OgreBotAPI:Spew_Variables` | does nothing | `OgreBotAPI.Debug:SpewVariables` `[fw]` | ⚠️ Arguments changed | Note A |
| `OgreBotAPI.SpewStat` | reads NULL | `OgreBotAPI.Debug:BroadcastStat` `[fw,type,value]` | ⚠️ Arguments changed | Note A |
| `OgreBotAPI:SpewSubscriptionStatus` | does nothing | `OgreBotAPI.Debug:SpewSubscriptionStatus` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI.Version` | reads NULL | `OgreBotAPI.Debug.Version` | ➡️ Moved |  |

## OgreBotAPI.Events

Old names whose job is now in `OgreBotAPI.Events`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:ChatEvent_AddEntry` | does nothing (stub) | `OgreBotAPI.Events:AddChatEntry` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:ChatEvent_RemoveEntry` | does nothing (stub) | `OgreBotAPI.Events:RemoveChatEntry` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:DespawnEvent_AddEntry` | does nothing (stub) | `OgreBotAPI.Events:AddDespawnEntry` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:DespawnEvent_RemoveEntry` | does nothing | `OgreBotAPI.Events:RemoveDespawnEntry` `[fw,text=all]` | ✏️ Renamed |  |
| `OgreBotAPI:OgreEvent_AskReply` | does nothing | IC file: the `groupQuery` step (ic-actions/09-groupQuery.md) - counts, allYes / anyYes / allNo / anyNo, per-member flags, raw answers, ready-made for-who lists. Script: the same engine - ${ISXOgreEQ2.Comms.GroupQuery[&lt;fw&gt;, -question, &lt;question&gt;, ...]} starts it and reads as its id; then ${ISXOgreEQ2.Comms.GroupQuery.Done[id]} / .Result[id] (JSON, the same names), or the event OgreEvent_GroupQueryDone(id, json). | ➡️ Lives somewhere else |  |
| `OgreBotAPI:SpawnEvent_AddEntry` | does nothing (stub) | `OgreBotAPI.Events:AddSpawnEntry` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:SpawnEvent_RemoveEntry` | does nothing (stub) | `OgreBotAPI.Events:RemoveSpawnEntry` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |

## OgreBotAPI.ForWho

Old names whose job is now in `OgreBotAPI.ForWho`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:Alias_AddEntry` | does nothing | `OgreBotAPI.ForWho:AddAlias` `[fw,alias,value,noRaid=FALSE]` | ✏️ Renamed |  |
| `OgreBotAPI:Alias_ChangeEntry` | does nothing | `OgreBotAPI.ForWho:ChangeAlias` `[fw,from,to]` | ✏️ Renamed | Not taken any more: `_SilentMode`. |
| `OgreBotAPI:Alias_ChangeEntryAlias` | does nothing | `OgreBotAPI.ForWho:RenameAlias` `[fw,from,to]` | ✏️ Renamed | Not taken any more: `_SilentMode`. |
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
| `OgreBotAPI:DoHO_Set_Enable` | does nothing | `OgreBotAPI.HOs:DoSetEnabled` `[fw,on]` | ✏️ Renamed |  |
| `OgreBotAPI:DoHO_Setup` | does nothing | `OgreBotAPI.HOs:DoSetup` `[fw,...]` | ✏️ Renamed |  |
| `OgreBotAPI:HO_Advance` | does nothing | `OgreBotAPI.HOs:Advance` `[fw,...]` | ✏️ Renamed |  |
| `OgreBotAPI:HO_Cancel_Starter` | does nothing | `OgreBotAPI.HOs:CancelStarter` `[fw]` | ✏️ Renamed | Not taken any more: `_CalledFrom`. |
| `OgreBotAPI.HO_Class_Available` | reads NULL | `OgreBotAPI.HOs.WheelClassAvailable` `[class]` | ✏️ Renamed |  |
| `OgreBotAPI:HO_Start` | does nothing | `OgreBotAPI.HOs:Start` `[fw,...]` | ✏️ Renamed |  |
| `OgreBotAPI:HO_Starter` | does nothing | `OgreBotAPI.HOs:Starter` `[fw,...]` | ✏️ Renamed |  |
| `OgreBotAPI:HO_Starter_Advance` | does nothing | `OgreBotAPI.HOs:Advance` `[fw,...]` | ✏️ Renamed |  |
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
| `OgreBotAPI:ConsumeItems_ProcessList` | does nothing | `OgreBotAPI.Inventory:ConsumeList` `[fw,-fc,-all,-st]` | ⚠️ Arguments changed | The arguments are different: Classic took `(string _ForWho="all", ... Args)`, the new call takes `[fw,-fc,-all,-st]`. |
| `OgreBotAPI.ConvertAdornToRemoveSlot` | reads NULL | `OgreBotAPI.Inventory.AdornToRemoveSlot` `[adorn]` | ✏️ Renamed |  |
| `OgreBotAPI.ConvertAdornToSlot` | reads NULL | `OgreBotAPI.Inventory.AdornToSlot` `[adorn]` | ✏️ Renamed |  |
| `OgreBotAPI:DestroyItem` | does nothing | `OgreBotAPI.Inventory:DestroyItem` `[fw,itemName]` | ➡️ Moved | Not taken any more: `_Charges`. |
| `OgreBotAPI:DestroyItem_NoChecks` | does nothing | `OgreBotAPI.Inventory:DestroyItem` `[fw,itemName]` | ✏️ Renamed |  |
| `OgreBotAPI:EquipCharm` | does nothing | `OgreBotAPI.Inventory:EquipCharm` `[fw,...]` | ➡️ Moved |  |
| `OgreBotAPI.EquipmentSlotAvailable` | does nothing (stub) | `OgreBotAPI.Inventory.SlotAvailable` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI.EquipmentSlotNumAvailable` | does nothing (stub) | `OgreBotAPI.Inventory.SlotNumAvailable` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:ExamineAllOfItem` | does nothing | `OgreBotAPI.Inventory:ExamineAll` `[fw,item...]` | ✏️ Renamed |  |
| `OgreBotAPI:ExamineInventoryItem` | does nothing | `OgreBotAPI.Inventory:Examine` `[fw,item]` | ✏️ Renamed |  |
| `OgreBotAPI.Get_AdornmentColour` | reads NULL | `OgreBotAPI.Inventory.AdornmentColour` `[iconId]` | ✏️ Renamed |  |
| `OgreBotAPI.Get_APIPackPonyRunning` | reads NULL | `OgreBotAPI.Inventory.PackPonyRunning` | ✏️ Renamed |  |
| `OgreBotAPI.Get_EquipmentModifierValue` | reads NULL | `OgreBotAPI.Inventory.SlotModifier` `[slot,modifier]` | ✏️ Renamed |  |
| `OgreBotAPI.Get_PackPonyRunning` | works | — | ✅ Works as is |  |
| `OgreBotAPI.Get_SlotNum_EQ2UIPageSlotNames` | reads NULL | `OgreBotAPI.Inventory.SlotUIName` `[n]` | ✏️ Renamed |  |
| `OgreBotAPI.Get_SlotNum_To_SlotNames` | reads NULL | `OgreBotAPI.Inventory.SlotName` `[n]` | ✏️ Renamed |  |
| `OgreBotAPI:Initialize_AdornmentInfo` | does nothing | `OgreBotAPI.Inventory:InitAdornmentInfo` `[fw]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. |
| `OgreBotAPI.IsAdornmentColour` | reads NULL | `OgreBotAPI.Inventory.IsAdornmentColour` `[iconId,colour]` | ➡️ Moved |  |
| `OgreBotAPI.ItemCount` | reads NULL | `OgreBotAPI.Inventory.Count` `[itemName,exact\|contains]` | ⚠️ Arguments changed | Write OgreBotAPI.Inventory.Count[&lt;name&gt;,contains] - Classic matched a PART of the name (=-); `exact` (the default) needs the whole name. Both count every stack in the bags and the Harvest Bag. |
| `OgreBotAPI:KronoWindowCheck` | does nothing (stub) | `OgreBotAPI.Inventory:KronoWindowCheck` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:Overseer_SpewMissionsInInventory` | does nothing (stub) | `OgreBotAPI.Inventory:SpewOverseerMissions` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:PoP_TempAdorns` | does nothing | `OgreBotAPI.Inventory:PoPTempAdorns` `[fw,...]` | ✏️ Renamed | Not taken any more: `_Overwrite`. |
| `OgreBotAPI:RedeemKrono` | does nothing | `OgreBotAPI.Inventory:RedeemKrono` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI.Slot_SlotNames` | reads NULL | `OgreBotAPI.Inventory.SlotName` `[n]` | ✏️ Renamed |  |
| `OgreBotAPI.SlotNum_EQ2UIPageSlotNames` | reads NULL | `OgreBotAPI.Inventory.SlotUIName` `[n]` | ✏️ Renamed |  |
| `OgreBotAPI.SlotNum_SlotNames` | reads NULL | `OgreBotAPI.Inventory.SlotName` `[n]` | ✏️ Renamed |  |
| `OgreBotAPI:Spew_SlotNum_To_SlotNames` | does nothing | `OgreBotAPI.Inventory:SpewSlotNames` `[fw]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. |
| `OgreBotAPI:Unpack` | does nothing | `OgreBotAPI.Inventory:Unpack` `[fw,...]` | ➡️ Moved | Not taken any more: `_UnpackOption`. |
| `OgreBotAPI:Unpack_Consume_Familiars` | does nothing | `OgreBotAPI.Inventory:UnpackConsumeFamiliars` `[fw,...]` | ✏️ Renamed |  |
| `OgreBotAPI:Unpack_EmpyralStones` | does nothing (stub) | `OgreBotAPI.Inventory:UnpackEmpyralStones` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:Unpack_Familiars` | does nothing | `OgreBotAPI.Inventory:UnpackFamiliars` `[fw,...]` | ✏️ Renamed |  |
| `OgreBotAPI:Unpack_PlanarStones` | does nothing (stub) | `OgreBotAPI.Inventory:UnpackPlanarStones` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:Unpack_Quantity` | does nothing | `OgreBotAPI.Inventory:UnpackQuantity` `[fw,...]` | ✏️ Renamed | Not taken any more: `Quantity`, `_UnpackOption`. |
| `OgreBotAPI:UseItem` | does nothing | `OgreBotAPI.Inventory:Use` `[fw,item,...]` | ✏️ Renamed |  |
| `OgreBotAPI:UseItem_Relay` | does nothing | `OgreBotAPI.Inventory:UseRelay` `[fw,item,...]` | ✏️ Renamed |  |
| `OgreBotAPI:UseItemOnPlayer` | does nothing | `OgreBotAPI.Inventory:UseOnPlayer` `[fw,item,player,...]` | ✏️ Renamed |  |
| `OgreBotAPI:UseItemOnPlayer_Relay` | does nothing | `OgreBotAPI.Inventory:UseOnPlayerRelay` `[fw,item,player,...]` | ✏️ Renamed |  |

## OgreBotAPI.Loot

Old names whose job is now in `OgreBotAPI.Loot`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:ChangeLootOptions` | does nothing | `OgreBotAPI.Loot:SetOptions` | ✏️ Renamed | NOT `Loot:SetAutoLootMode` - that is only this toon's auto-loot dropdown. A family nobody names is left alone, so you can set the method without disturbing rarity. |
| `OgreBotAPI.Get_LootWindowID` | reads NULL | `OgreBotAPI.Loot.WindowID` | ✏️ Renamed |  |
| `OgreBotAPI:HandleLootWindow` | does nothing | — | ⛔ Not ported yet |  |
| `OgreBotAPI.LootWindowExists` | reads NULL | `OgreBotAPI.Loot.WindowExists` | ✏️ Renamed |  |
| `OgreBotAPI:LootWindowLootAll` | does nothing | `OgreBotAPI.Loot:LootAll` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:ResetActorsLooted` | does nothing | `OgreBotAPI.Loot:ResetLootedActors` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:SetAutoLootMode` | does nothing | `OgreBotAPI.Loot:SetAutoLootMode` `[fw,n]` | ➡️ Moved | Not taken any more: `_Silent`. |
| `OgreBotAPI:SmartLoot_BuildToonItemsToBeZeroed` | does nothing | `OgreBotAPI.Loot:BuildToonItemsToBeZeroed` | ✏️ Renamed |  |
| `OgreBotAPI:SmartLoot_ProcessToonItemsToBeZeroed` | does nothing | `OgreBotAPI.Loot:ProcessToonItemsToBeZeroed` | ✏️ Renamed |  |
| `OgreBotAPI:SmartLoot_ReloadDataFromFile` | does nothing | `OgreBotAPI.Loot:Reload` | ✏️ Renamed |  |

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
| `OgreBotAPI:AutoRun` | does nothing | `OgreBotAPI.Movement:AutoRun` | ➡️ Moved |  |
| `OgreBotAPI:CallGH` | does nothing | `OgreBotAPI.Movement:CallGH` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI:Come2Me` | does nothing | `OgreBotAPI.Movement:Come2Me` | ➡️ Moved |  |
| `OgreBotAPI:Crouch` | does nothing | `OgreBotAPI.Movement:Crouch` | ➡️ Moved |  |
| `OgreBotAPI:Evac` | does nothing | `OgreBotAPI.Movement:Evac` | ➡️ Moved |  |
| `OgreBotAPI:FaceActor` | does nothing | `OgreBotAPI.Movement:FaceActor` | ➡️ Moved |  |
| `OgreBotAPI:FaceAngle` | does nothing | `OgreBotAPI.Movement:FaceAngle` | ➡️ Moved |  |
| `OgreBotAPI:FaceLoc` | does nothing | `OgreBotAPI.Movement:FaceLoc` | ➡️ Moved |  |
| `OgreBotAPI:FlyDown` | does nothing | `OgreBotAPI.Movement:FlyDown` | ➡️ Moved |  |
| `OgreBotAPI:FlyStop` | does nothing | `OgreBotAPI.Movement:FlyStop` | ➡️ Moved |  |
| `OgreBotAPI:FlyUp` | does nothing | `OgreBotAPI.Movement:FlyUp` | ➡️ Moved |  |
| `OgreBotAPI:ForceFollow` | does nothing | `OgreBotAPI.Movement:ForceFollow` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI.GettingToGH` | reads NULL | `OgreBotAPI.Movement.GettingToGH` | ➡️ Moved |  |
| `OgreBotAPI:GetToConcentration` | does nothing | `OgreBotAPI.Movement:GetToConcentration` | ➡️ Moved |  |
| `OgreBotAPI:GetToGH` | does nothing | `OgreBotAPI.Movement:GetToGH` | ➡️ Moved |  |
| `OgreBotAPI:HoldUp` | does nothing | `OgreBotAPI.Movement:HoldUp` | ➡️ Moved |  |
| `call OgreBotAPI.HouseWindowToGH` | does nothing | `OgreBotAPI.Movement:GetToGH` | ✏️ Renamed | the house-window leg is one route inside the ported driver, not a separate verb |
| `OgreBotAPI:JoustIn` | does nothing | `OgreBotAPI.Movement:JoustIn` | ➡️ Moved |  |
| `OgreBotAPI:JoustOff` | does nothing | `OgreBotAPI.Movement:JoustOff` | ➡️ Moved |  |
| `OgreBotAPI:JoustOn` | does nothing | `OgreBotAPI.Movement:JoustOn` | ➡️ Moved |  |
| `OgreBotAPI:JoustOut` | does nothing | `OgreBotAPI.Movement:JoustOut` | ➡️ Moved |  |
| `OgreBotAPI:Jump` | does nothing | `OgreBotAPI.Movement:Jump` | ➡️ Moved |  |
| `OgreBotAPI:LandFlyingMount` | does nothing | `OgreBotAPI.Movement:LandFlyingMount` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI:Move2Area` | does nothing | `OgreBotAPI.Movement:Move2Area` `[fw,x,y,z,precision]` | ⚠️ Arguments changed | **Old:** `OgreBotAPI:Move2Area[x,z,who,precision] (Classic's second number is the Z). New: OgreBotAPI.Movement:Move2Area[who,x,y,z,precision] - the for-who comes first and y is new but ignored (a ground move: pass ${Me.Y} or 0). Only toons that have a target move, as in Classic` |
| `OgreBotAPI:Move2AreaNoTarget` | does nothing | `OgreBotAPI.Movement:Move2AreaNoTarget` `[fw,x,y,z,precision]` | ⚠️ Arguments changed | **Old:** `OgreBotAPI:Move2AreaNoTarget[x,z,who,precision] (Classic's second number is the Z). New: OgreBotAPI.Movement:Move2AreaNoTarget[who,x,y,z,precision] - the for-who comes first and y is new but ignored (a ground move: pass ${Me.Y} or 0). Moves with or without a target, as in Classic` |
| `OgreBotAPI:NoMove` | does nothing | `OgreBotAPI.Movement:StopFollow` | ✏️ Renamed |  |
| `OgreBotAPI:OFolDecDistance` | does nothing | `OgreBotAPI.Movement:FollowDistanceDown` | ✏️ Renamed |  |
| `OgreBotAPI:OFolIncDistance` | does nothing | `OgreBotAPI.Movement:FollowDistanceUp` | ✏️ Renamed |  |
| `OgreBotAPI:Pull` | does nothing | `OgreBotAPI.Movement:Pull` | ➡️ Moved |  |
| `OgreBotAPI:Remove_Prepare_TankSwapping` | does nothing (stub) | `OgreBotAPI:Remove_Prepare_TankSwapping` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:RemoveNoOffensiveOn` | works | — | ✅ Works as is |  |
| `OgreBotAPI:RunWalk` | does nothing | `OgreBotAPI.Movement:SetRunMode` | ⚠️ Arguments changed | SIGNATURE CHANGED - add TRUE (run) or FALSE (walk) after the for-who; there is no toggle. |
| `OgreBotAPI:Set_CampSpotJump_Handle` | does nothing | `OgreBotAPI.Movement:JumpRoute` | ✏️ Renamed | Same arguments in the same order; each option is its own argument. The jump distance and max time Classic kept on Obj_CampSpotJump (Set_JumpDistance / Set_MaxTimer) are per-route options now - see the Obj_CampSpotJump rows. |
| `OgreBotAPI:Stand` | does nothing | `OgreBotAPI.Movement:Stand` | ➡️ Moved |  |
| `OgreBotAPI:Waypoint` | does nothing | `OgreBotAPI.Movement:Waypoint` | ➡️ Moved |  |

## OgreBotAPI.OneOff

Old names whose job is now in `OgreBotAPI.OneOff`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:ArcannaseEffigyOfRebirth` | works | — | ✅ Works as is |  |
| `OgreBotAPI:C4M` | does nothing (stub) | `OgreBotAPI:C4M` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:DoVDebuff` | works | — | ✅ Works as is |  |
| `OgreBotAPI:DoVDebuff_Half` | works | — | ✅ Works as is |  |
| `OgreBotAPI:GO_CryptofDalnir_WizardsDen_EventHeroic_King` | does nothing (stub) | `OgreBotAPI:GO_CryptofDalnir_WizardsDen_EventHeroic_King` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:HQEar_Recheck` | does nothing (stub) | `OgreBotAPI:HQEar_Recheck` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:HQEar_ReEquipOriginalEar` | does nothing (stub) | `OgreBotAPI:HQEar_ReEquipOriginalEar` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:HQEar_ReportStuckEar` | does nothing (stub) | `OgreBotAPI:HQEar_ReportStuckEar` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI.NPCUnkillableBug` | works | — | ✅ Works as is |  |
| `OgreBotAPI:RO_FSD_BB_Brutas_DoNotNeedColdWater` | does nothing (stub) | `OgreBotAPI:RO_FSD_BB_Brutas_DoNotNeedColdWater` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:RO_FSD_BB_Brutas_DoNotNeedColdWater_Relay` | works | — | ✅ Works as is |  |
| `OgreBotAPI:RO_FSD_BB_Brutas_NeedColdWater` | does nothing (stub) | `OgreBotAPI:RO_FSD_BB_Brutas_NeedColdWater` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:RO_FSD_BB_Brutas_NeedColdWater_Relay` | works | — | ✅ Works as is |  |
| `OgreBotAPI.RoR_Epic_AbilityID` | does nothing (stub) | `OgreBotAPI.RoR_Epic_AbilityID` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI.RoR_Epic_Available` | does nothing (stub) | `OgreBotAPI.RoR_Epic_Available` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:RoR_Epic_ChangeInCastStack` | does nothing (stub) | `OgreBotAPI:RoR_Epic_ChangeInCastStack` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI.RoR_Epic_Ready` | does nothing (stub) | `OgreBotAPI.RoR_Epic_Ready` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:Scribe_Empyral` | works | — | ✅ Works as is |  |
| `OgreBotAPI:Special` | works | — | ✅ Works as is |  |
| `OgreBotAPI:Test` | works | — | ✅ Works as is |  |
| `OgreBotAPI:TestAll` | works | — | ✅ Works as is |  |

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
| `OgreBotAPI:AcceptQuest` | does nothing | `OgreBotAPI.Quest:Accept` `[fw,questName]` | ✏️ Renamed |  |
| `OgreBotAPI.ActorHasQuest` | reads NULL | `OgreBotAPI.Quest.ActorHas` `[actorId]` | ✏️ Renamed |  |
| `OgreBotAPI:CheckKunarkAscendingRequirements` | does nothing | `OgreBotAPI.Quest:CheckKunarkAscending` `[fw,...]` | ✏️ Renamed |  |
| `OgreBotAPI:CheckToShareQuest` | does nothing | `OgreBotAPI.Quest:CheckToShare` `[fw,...]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. |
| `OgreBotAPI:CompareQuestUpdate` | does nothing | `OgreBotAPI.Quest:CompareUpdate` `[fw,...]` | ✏️ Renamed |  |
| `OgreBotAPI:DailyEtherealMissionReset` | does nothing (stub) | `OgreBotAPI.Quest:DailyMissionReset` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:DeleteQuest` | does nothing | `OgreBotAPI.Quest:Delete` `[fw,name]` | ✏️ Renamed |  |
| `OgreBotAPI:DisplayEtherealMissionInfo` | does nothing | `OgreBotAPI.Quest:ShowMissionInfo` `[fw,...]` | ✏️ Renamed |  |
| `OgreBotAPI.GetDeityPoints` | does nothing (stub) | `OgreBotAPI.Quest.DeityPoints` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI.HaveQuest` | reads NULL | `OgreBotAPI.Quest.Have` `[name]` | ✏️ Renamed |  |
| `OgreBotAPI.LootQuestion` | reads NULL | `OgreBotAPI.Quest.SkipShinies` | ✏️ Renamed |  |
| `OgreBotAPI:ShareAllMissions` | does nothing | `OgreBotAPI.Quest:ShareAllMissions` `[fw,...]` | ➡️ Moved |  |
| `OgreBotAPI:ShareMission` | does nothing | `OgreBotAPI.Quest:ShareMission` `[fw,...]` | ➡️ Moved |  |
| `OgreBotAPI:ShareQuest` | does nothing | `OgreBotAPI.Quest:ShareQuest` `[fw,...]` | ➡️ Moved |  |
| `OgreBotAPI:ShareQuestWhenAble` | does nothing (stub) | `OgreBotAPI.Quest:ShareQuestWhenAble` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:ShowWikiForQuest` | does nothing | `OgreBotAPI.Quest:ShowWiki` `[fw,name]` | ✏️ Renamed |  |
| `OgreBotAPI:Spew_MissionTimerInfo` | does nothing | `OgreBotAPI.Quest:SpewMissionTimers` `[fw,...searches]` | ✏️ Renamed |  |

## OgreBotAPI.Roster

Old names whose job is now in `OgreBotAPI.Roster`.

**Note A** (3 rows below): arguments swapped - old `[search, mode, rank]`, new `[mode, search, rank]`. The first two arguments are swapped.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:CheckMemberLevel` | does nothing | `OgreBotAPI.Roster:CheckMemberLevel` `[fw,onlyNonMembers=FALSE]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. gained a for-who; argument 0 *was* the bool and is now the for-who. |
| `OgreBotAPI.ClassInfo_ChangeValue` | reads NULL | `OgreBotAPI.Roster:SetClassValue` `[fw,member,value]` | ✏️ Renamed |  |
| `OgreBotAPI.ClassInfo_GetValue` | does nothing (stub) | `OgreBotAPI.Roster.ClassValue` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
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
| `OgreBotAPI.InEQ2Chars` | does nothing (stub) | `OgreBotAPI.Roster.InEQ2Chars` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI.InICGroup` | reads NULL | — | ⛔ Removed | Ask the group: ${ISXOgreEQ2.Comms.GroupQuery[${Me.Name},-question,"LavishScript[\${ISXOgreEQ2.IC.Running}]"]} returns an id; wait on .Done[id], then .Result[id] is JSON - "anyYes" = someone in the group is running IC, "yesWho" = who. |
| `OgreBotAPI:Invite` | does nothing | `OgreBotAPI.Roster:Invite` `[fw,who=me]` | ➡️ Moved | Not taken any more: `_RaidInvite`. |
| `OgreBotAPI.IsGroupLeader` | reads NULL | `OgreBotAPI.Roster.IsGroupLeader` | ➡️ Moved |  |
| `OgreBotAPI:MakeLeader` | does nothing | `OgreBotAPI.Roster:MakeLeader` `[fw,leader=me]` | ➡️ Moved |  |
| `OgreBotAPI:MarkToon` | does nothing | `OgreBotAPI.Roster:Mark` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:Mentor` | does nothing | `OgreBotAPI.Roster:Mentor` `[fw,name]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. |
| `OgreBotAPI.SortGroupByIDBy` | reads NULL | `OgreBotAPI.Roster.SortGroupByID` | ⚠️ Argument order changed | arguments swapped - old `[search, mode, ...]`, new `[mode, search, ...]`. The first two arguments are swapped. |
| `OgreBotAPI.SortRaidByIDBy` | reads NULL | `OgreBotAPI.Roster.SortRaidByID` | ⚠️ Argument order changed | arguments swapped - old `[search, mode, ...]`, new `[mode, search, ...]`. The first two arguments are swapped. |
| `OgreBotAPI:SpewFlags` | does nothing | `OgreBotAPI.Roster:SpewFlags` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI.ToonFlagged` | reads NULL | `OgreBotAPI.Roster.Flagged` `[n=1]` | ✏️ Renamed |  |
| `OgreBotAPI.ToonMarked` | reads NULL | `OgreBotAPI.Roster:SpewMarked` `[fw,where]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. |
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
| `OgreBotAPI.Question` | reads NULL | `OgreBotAPI.Session:CollectShiny` `[fw]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. |
| `OgreBotAPI:Res` | does nothing | `OgreBotAPI.Session:Res` | ➡️ Moved |  |
| `OgreBotAPI:Resource` | does nothing | `OgreBotAPI.Session:Harvest` `[fw]` | ✏️ Renamed | renamed to `Session:Harvest` - it collects a harvest node in range. |
| `OgreBotAPI:ResStone` | does nothing | `OgreBotAPI.Session:ResStone` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI:Revive` | does nothing | `OgreBotAPI.Session:Revive` | ➡️ Moved |  |
| `OgreBotAPI:StopRes` | does nothing | `OgreBotAPI.Session:StopRes` | ➡️ Moved |  |
| `OgreBotAPI:UpdateCharacterDetails` | does nothing | `OgreBotAPI.Session:UpdateCharacterDetails` `[fw]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. gained a for-who. |

## OgreBotAPI.Travel

Old names whose job is now in `OgreBotAPI.Travel`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:FastTravel` | does nothing | `OgreBotAPI.Travel:Fast` | ✏️ Renamed |  |
| `OgreBotAPI:PortalToGuildHall` | does nothing | `OgreBotAPI.Travel:ToGuildHall` | ✏️ Renamed |  |
| `OgreBotAPI:SpewZoneDoorOptions` | does nothing | `OgreBotAPI.Travel:SpewZoneDoorOptions` | ➡️ Moved |  |
| `OgreBotAPI:Travel` | does nothing | `OgreBotAPI.Travel:Travel` | ➡️ Moved |  |
| `OgreBotAPI.Travel_Get_ZoneDoorValue` | reads NULL | `OgreBotAPI.Travel.ZoneDoorValue` | ✏️ Renamed |  |
| `OgreBotAPI:TravelBell` | does nothing | `OgreBotAPI.Travel:Bell` | ✏️ Renamed |  |
| `OgreBotAPI:TravelDruid` | does nothing | `OgreBotAPI.Travel:Druid` | ✏️ Renamed |  |
| `OgreBotAPI:TravelSpires` | does nothing | `OgreBotAPI.Travel:Spires` | ✏️ Renamed |  |
| `OgreBotAPI:ZoneDoor` | does nothing | `OgreBotAPI.Travel:ZoneDoor` | ➡️ Moved |  |
| `OgreBotAPI:ZoneDoorForWho` | does nothing | `OgreBotAPI.Travel:ZoneDoorFor` | ✏️ Renamed |  |

## OgreBotAPI.Util

Old names whose job is now in `OgreBotAPI.Util`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI.ArraySearch` | works | — | ✅ Works as is |  |
| `OgreBotAPI.Between` | reads NULL | `OgreBotAPI.Util.Between` `[v,lo,hi]` | ➡️ Moved |  |
| `OgreBotAPI.BetweenFloat` | reads NULL | `OgreBotAPI.Util.BetweenFloat` `[v,lo,hi]` | ➡️ Moved |  |
| `OgreBotAPI:CheckResearch` | does nothing | `OgreBotAPI.Util:CheckResearch` `[fw,forceReport=FALSE]` | ➡️ Moved |  |
| `OgreBotAPI.Clean` | reads NULL | `OgreBotAPI.Util.Clean` `[s]` | ➡️ Moved |  |
| `OgreBotAPI.CleanNameWithSpaces` | reads NULL | `OgreBotAPI.Util.Clean` `[s]` | ✏️ Renamed |  |
| `OgreBotAPI.ConvertSecondsToHMS` | reads NULL | `OgreBotAPI.Util.SecondsToHMS` `[n]` | ✏️ Renamed |  |
| `OgreBotAPI.ConvertSlotArrayToSlot` | reads NULL | `OgreBotAPI.Util.SlotArrayToSlot` `[n]` | ✏️ Renamed |  |
| `OgreBotAPI.FileExists` | reads NULL | `OgreBotAPI.Util.FileExists` `[path]` | ➡️ Moved |  |
| `OgreBotAPI.Get_Hours` | reads NULL | `OgreBotAPI.Util.Hours` `[n]` | ✏️ Renamed |  |
| `OgreBotAPI.Get_Minutes` | reads NULL | `OgreBotAPI.Util.Minutes` `[n]` | ✏️ Renamed |  |
| `OgreBotAPI.Get_Seconds` | reads NULL | `OgreBotAPI.Util.Seconds` `[n]` | ✏️ Renamed |  |
| `OgreBotAPI.IndexMatch` | works | — | ✅ Works as is |  |
| `OgreBotAPI.IndexSearch` | works | — | ✅ Works as is |  |
| `OgreBotAPI.IndexSearchJSON` | works | — | ✅ Works as is |  |
| `OgreBotAPI.MD5` | reads NULL | `OgreBotAPI.Util.MD5` `[s]` | ➡️ Moved |  |
| `OgreBotAPI:OnScreenTimer` | does nothing | `OgreBotAPI.Util:OnScreenTimer` `[fw,...]` | ➡️ Moved | Not taken any more: `_Slot`, `_Message`, `_MinUpdateTimer`, `_ExtraTimer`, `_ExtraTimerMessage`. |
| `OgreBotAPI:OnScreenTimerReset` | does nothing | `OgreBotAPI.Util:OnScreenTimerReset` `[fw]` | ➡️ Moved | Not taken any more: `_Slot`. |
| `OgreBotAPI.PE_ThisMember` | reads NULL | `OgreBotAPI.Util.IEquals` `[a,b]` | ✏️ Renamed |  |
| `OgreBotAPI.RemoveColourCode` | reads NULL | `OgreBotAPI.Util.StripColourCodes` `[s]` | ✏️ Renamed |  |
| `OgreBotAPI.RemoveZoneNumber` | reads NULL | `OgreBotAPI.Util.StripZoneNumber` `[s]` | ✏️ Renamed |  |
| `OgreBotAPI.RemoveZoneNumberOnly` | reads NULL | `OgreBotAPI.Util.StripZoneNumberOnly` `[s]` | ✏️ Renamed |  |
| `OgreBotAPI:Research_Material_Check` | does nothing | `OgreBotAPI.Util:CheckResearchMaterials` `[fw,...]` | ✏️ Renamed |  |
| `OgreBotAPI.RomanToInt` | reads NULL | `OgreBotAPI.Util.RomanToInt` `[s]` | ➡️ Moved |  |
| `OgreBotAPI.RoundNumToNearestValue` | reads NULL | `OgreBotAPI.Util.RoundToNearest` `[value,step]` | ✏️ Renamed | Not taken any more: `_IncrementBy`. |
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

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:AcceptNoChoiceReward` | does nothing (stub) | `OgreBotAPI.Windows:AcceptNoChoiceReward` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:AcceptReward` | does nothing | `OgreBotAPI.Windows:AcceptReward` `[fw,num\|name,windowId]` | ➡️ Moved |  |
| `OgreBotAPI:ChoiceWindow` | does nothing | `OgreBotAPI.Windows:Choice` `[fw,option]` | ✏️ Renamed |  |
| `OgreBotAPI:CloseAllExamine` | does nothing | `OgreBotAPI.Windows:CloseExamine` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:CloseExamine` | does nothing | `OgreBotAPI.Windows:CloseExamine` `[fw]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. |
| `OgreBotAPI:CloseExamineWindow` | does nothing | `OgreBotAPI.Windows:CloseExamine` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:CloseWindow` | does nothing | `OgreBotAPI.Windows:Close` `[fw,name]` | ⚠️ Arguments changed | The arguments are different: Classic took `(string _ForWho="all")`, the new call takes `[fw,name]`. |
| `OgreBotAPI:DungeonMakerCancel` | does nothing | `OgreBotAPI.Windows:DungeonMakerCancel` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI:F2PWindow_Check` | does nothing | `OgreBotAPI.Windows:F2PWindowCheck` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI.Get_RewardID` | does nothing (stub) | `OgreBotAPI.Windows.RewardID` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI.Get_RewardLinkID` | does nothing (stub) | `OgreBotAPI.Windows.RewardLinkID` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI.Get_RewardName` | does nothing (stub) | `OgreBotAPI.Windows.RewardName` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:InputTextWindow_Accept` | does nothing | `OgreBotAPI.Windows:InputTextAccept` `[fw,...]` | ✏️ Renamed |  |
| `OgreBotAPI:InputTextWindow_AddText` | does nothing | `OgreBotAPI.Windows:InputTextAdd` `[fw,text]` | ✏️ Renamed | `[fw, text]`. Same page/child/visible gate as `:InputTextAccept` - a no-op when the input box is not up. |
| `OgreBotAPI:InputTextWindow_ClearText` | does nothing | `OgreBotAPI.Windows:InputTextClear` `[fw]` | ✏️ Renamed | `[fw]`. |
| `OgreBotAPI.IsCastingWindowVisible` | reads NULL | `OgreBotAPI.Windows.CastingWindowVisible` | ✏️ Renamed |  |
| `OgreBotAPI:OK_Button` | does nothing | `OgreBotAPI.Windows:OK` `[fw,...]` | ✏️ Renamed |  |
| `OgreBotAPI:ProvingGrounds_Exit` | does nothing | `OgreBotAPI.Windows:ProvingGroundsExit` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:ProvingGrounds_Scoreboard_Close` | does nothing | `OgreBotAPI.Windows:ProvingGroundsScoreboardClose` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:ReplyDialog` | does nothing | `OgreBotAPI.Windows:Reply` `[fw,text]` | ✏️ Renamed |  |
| `OgreBotAPI.ReplyDialog_ReplyExists` | does nothing (stub) | `OgreBotAPI.Windows.ReplyExists` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:ReplyDialogClose` | does nothing | `OgreBotAPI.Windows:ReplyClose` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI.RewardWindow_Get_WindowID` | does nothing (stub) | `OgreBotAPI.Windows.RewardWindowID` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:RewardWindow_Spew_WindowIDs` | does nothing (stub) | `OgreBotAPI.Windows:SpewRewardWindowIDs` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:Select_Window` | does nothing | `OgreBotAPI.Windows:Select` `[fw,option]` | ⚠️ Arguments changed | The arguments are different: Classic took `(string _ForWho=all, ... Args)`, the new call takes `[fw,option]`. |
| `OgreBotAPI:Select_Window_Cancel` | does nothing | `OgreBotAPI.Windows:SelectCancel` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI.Select_Window_GetOption` | reads NULL | `OgreBotAPI.Windows.SelectOption` `[n]` | ⚠️ Arguments changed | The arguments are different: Classic took `(... Args)`, the new call takes `[n]`. |
| `OgreBotAPI:Select_Window_Spew` | does nothing | `OgreBotAPI.Windows:SelectSpew` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:ShowOgreConsole` | does nothing | `OgreBotAPI.Windows:ShowConsole` `[fw]` | ✏️ Renamed | Not taken any more: `_Value`. |
| `OgreBotAPI:ToggleConsoleWindow` | does nothing | `OgreBotAPI.Windows:ToggleConsole` `[fw]` | ✏️ Renamed | Not taken any more: `_Value`. |
| `OgreBotAPI:ToggleMainWindow` | does nothing | `OgreBotAPI.Windows:ToggleMain` `[fw]` | ✏️ Renamed |  |

## OgreBotAPI.Zone

Old names whose job is now in `OgreBotAPI.Zone`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:Champions_Zone_Resetter` | does nothing | `OgreBotAPI.Zone:ChampionsResetter` `[fw,...]` | ✏️ Renamed |  |
| `OgreBotAPI:ChangeZoneTo` | does nothing | `OgreBotAPI.Zone:ChangeZoneTo` `[fw,toWho]` | ➡️ Moved |  |
| `OgreBotAPI:CheckICPartyStatus` | does nothing | — | ⛔ Removed | Nothing to call - delete the line. To ask whether the group is running IC: Ask the group: ${ISXOgreEQ2.Comms.GroupQuery[${Me.Name},-question,"LavishScript[\${ISXOgreEQ2.IC.Running}]"]} returns an id; wait on .Done[id], then .Result[id] is JSON - "anyYes" = someone in the group is running IC, "yesWho" = who. |
| `OgreBotAPI.CityRestrictions` | does nothing (stub) | `OgreBotAPI.Zone.CityRestrictions` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI.CleanZoneName` | reads NULL | `OgreBotAPI.Zone.CleanName` `[name]` | ✏️ Renamed |  |
| `OgreBotAPI.InBattleGround` | does nothing (stub) | `OgreBotAPI.Zone.InBattleGround` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI.InGuildHallZone` | reads NULL | `OgreBotAPI.Zone.InGuildHall` | ✏️ Renamed |  |
| `OgreBotAPI.InHouseAccessZone` | reads NULL | `OgreBotAPI.Zone.InHouseAccess` | ✏️ Renamed |  |
| `OgreBotAPI.InHouseZone` | reads NULL | `OgreBotAPI.Zone.InHouse` | ✏️ Renamed |  |
| `OgreBotAPI.InInstance` | reads NULL | `OgreBotAPI.Zone.InInstance` | ➡️ Moved |  |
| `OgreBotAPI:ResetZone` | does nothing | `OgreBotAPI.Zone:ResetZone` `[fw,...]` | ➡️ Moved |  |
| `OgreBotAPI:Select_Zone_Version` | does nothing | `OgreBotAPI.Zone:SelectVersion` `[fw,version]` | ✏️ Renamed |  |
| `OgreBotAPI:ShareQuestsForZone` | does nothing | `OgreBotAPI.Zone:ShareQuestsForZone` `[fw,...]` | ➡️ Moved |  |
| `OgreBotAPI:SpecialZoneSpecific` | does nothing | `OgreBotAPI.Zone:SpecialZoneSpecific` `[fw,...]` | ➡️ Moved |  |
| `OgreBotAPI:ToggleZoneReuse` | does nothing | `OgreBotAPI.Zone:ToggleZoneReuse` `[fw]` | ➡️ Moved |  |
| `OgreBotAPI:Zone` | does nothing | `OgreBotAPI.Zone:Zone` `[fw,zone,...]` | ➡️ Moved |  |
| `OgreBotAPI.ZoneName` | reads NULL | `OgreBotAPI.Zone.Name` | ✏️ Renamed |  |
| `OgreBotAPI.ZoneReset_FullZoneInformationAvailable` | reads NULL | `OgreBotAPI.Zone.ResetInfoAvailable` | ✏️ Renamed |  |
| `OgreBotAPI.ZoneReset_Get_ZoneData` | does nothing (stub) | `OgreBotAPI.Zone.ResetZoneData` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI.ZoneReset_IsReady` | does nothing (stub) | `OgreBotAPI.Zone.ResetReady` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI.ZoneReset_IsUpdating` | does nothing (stub) | `OgreBotAPI.Zone.ResetUpdating` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:ZoneReset_UpdateInfo` | does nothing (stub) | `OgreBotAPI.Zone:ResetUpdateInfo` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `OgreBotAPI:ZoneResetAll` | does nothing | `OgreBotAPI.Zone:ResetAll` `[fw]` | ✏️ Renamed | Not taken any more: `_bAllowRaid`. |

## Not in a group

Old names with no home in a group: not ported yet, done somewhere else, or a line in a data file now.

**Note A** (18 rows below): Classic-internal state (a cache, a timer, a handle). Not script-facing, and the new engine owns the equivalent state privately.

**Note B** (7 rows below): a fight-, item- or zone-specific one-off.

**Note C** (7 rows below): a `_Report` variant that echoed what the plain verb did. The new surface has one verb per action; fleet reporting is `Comms:ReportListIrc` / `:ReportSpew` / `.ReportKey` / `.ReportValue`.

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
| `OgreBotAPI.bDebugMode` | reads NULL | — | ⛔ Not ported yet | the debug-mode FLAG has no read member; `Debug:SetDebugMode` writes it and `Debug:DebugEcho` is gated on it, but nothing exposes the boolean. |
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
| `OgreBotAPI:NoTanking` | does nothing | — | ⛔ Not ported yet | the cast is ability-by-NAME (`"Subtle Strikes"`), which is Rule 10 territory now - resolve the id off the export catalog when converting. |
| `OgreBotAPI.ogre_campspot_me` | reads NULL | — | ⛔ Not ported yet | Engine-only in Classic too (both sites are). |
| `OgreBotAPI:Output_InGame_MovementKeys` | does nothing | — | ⛔ Not ported yet | prints Classic's movement key bindings. The new surface SETS them (`Movement:SetForwardKey` / `:SetBackwardKey` / `:SetFlyUpKey` / `:SetFlyDownKey`) but does not dump them. |
| `OgreBotAPI:Populate_ExportList` | does nothing | — | ⛔ Not ported yet |  |
| `OgreBotAPI:PulseCircleMovement` | does nothing | — | ⛔ Not ported yet | `:SetLocAtAngleFromActor` places the camp spot at one angle/distance from an actor; `:SetLocBehindActor` / `:SetLocInFrontOfActor` / `:SetLocByRole` are the fixed-bearing forms. A converted encounter drives the rotation itself and calls one of these per spot. |
| `OgreBotAPI.PulseCircleMovement_CurrentSpot` | reads NULL | — | ⛔ Not ported yet | Note A |
| `OgreBotAPI.PulseCircleMovement_TimerRecentlyMoved` | reads NULL | — | ⛔ Not ported yet | Note A |
| `OgreBotAPI:Reload_DevBot` | does nothing | — | ⛔ Not ported yet | Note G |
| `OgreBotAPI:ReloadExport` | does nothing | — | ⛔ Not ported yet | Note G |
| `OgreBotAPI:ReloadOgreIRC` | does nothing | `${OgreIRCHub:Reload}  /  ${OgreIRCHub:Connect}` | ➡️ Lives somewhere else |  |
| `OgreBotAPI:Report_Back` | does nothing | — | ⛔ Not ported yet | Note C |
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

- `OgreBotAPI:AcceptNoChoiceReward` - exists, does nothing yet
- `OgreBotAPI:AfterProfileLoad` - not ported yet
- `OgreBotAPI:Aliases_ShowAllBuiltInAliases` - not ported yet
- `OgreBotAPI:Announce_AddEntry` - exists, does nothing yet
- `OgreBotAPI:AscensionEmbargo_Add_DoNotCombo` - not ported yet
- `OgreBotAPI:AscensionEmbargo_Change_Disable_Status` - not ported yet
- `OgreBotAPI:AscensionEmbargo_Remove_DoNotCombo` - not ported yet
- `OgreBotAPI:AutoHunt_AddPath` - not ported yet
- `OgreBotAPI:AutoHunt_AddPoint` - not ported yet
- `OgreBotAPI:AutoHunt_ClearPoints` - not ported yet
- `OgreBotAPI:AutoHunt_RemovePoint` - not ported yet
- `OgreBotAPI.bBuyingFromMerchantConfirmation` - not ported yet
- `OgreBotAPI.bCacheEquipmentAdornmentNames` - not ported yet
- `OgreBotAPI.bDebugMode` - not ported yet
- `OgreBotAPI.bInternal` - not ported yet
- `OgreBotAPI.bNoCollision` - not ported yet
- `OgreBotAPI.bSetUpFor_HOs_Current_HeroicSurge` - not ported yet
- `OgreBotAPI.bSetUpFor_HOs_Obtained_Current_HeroicSurge` - not ported yet
- `OgreBotAPI:C4M` - exists, does nothing yet
- `OgreBotAPI:CancelCasting_OLD` - exists, does nothing yet
- `OgreBotAPI:CastAbilityNoExportUntilCast` - not ported yet
- `OgreBotAPI:CastAbilityType` - not ported yet
- `OgreBotAPI:CastHQEar` - not ported yet
- `OgreBotAPI.CastStackAllowHOIcons` - not ported yet
- `OgreBotAPI.CastStackDisableHOIcons` - not ported yet
- `OgreBotAPI:Change_PoisonAutoConsume` - not ported yet
- `OgreBotAPI:ChatEvent_AddEntry` - exists, does nothing yet
- `OgreBotAPI:ChatEvent_RemoveEntry` - exists, does nothing yet
- `OgreBotAPI.CityRestrictions` - exists, does nothing yet
- `OgreBotAPI.ClassInfo_GetValue` - exists, does nothing yet
- `OgreBotAPI:ConversationBubbleSpew` - exists, does nothing yet
- `OgreBotAPI.CursorActor_Tooltip_Text` - exists, does nothing yet
- `OgreBotAPI.CursorActor_Tooltip_Visible` - exists, does nothing yet
- `OgreBotAPI:DailyEtherealMissionReset` - exists, does nothing yet
- `OgreBotAPI:DespawnEvent_AddEntry` - exists, does nothing yet
- `OgreBotAPI:DestroyItemByID_NoChecks` - not ported yet
- `OgreBotAPI:DisplayAvailableSetups` - exists, does nothing yet
- `OgreBotAPI:DisplayMyAscensionCombos` - not ported yet
- `OgreBotAPI.EquipmentSlotAvailable` - exists, does nothing yet
- `OgreBotAPI.EquipmentSlotNumAvailable` - exists, does nothing yet
- `OgreBotAPI:FastTravel_Report` - not ported yet
- `OgreBotAPI:FastTravelOld` - not ported yet
- `call OgreBotAPI.FindAdornment_ReturnSlot` - not ported yet
- `call OgreBotAPI.FindAdornments_ReturnJSON` - not ported yet
- `OgreBotAPI:Fix_Broken_Shit` - not ported yet
- `OgreBotAPI:FixCastAfterZoneBug` - not ported yet
- `OgreBotAPI:FlushQueued` - exists, does nothing yet
- `OgreBotAPI:GenerateMyAscensionCombos` - not ported yet
- `OgreBotAPI.Get_AbilityVia` - not ported yet
- `OgreBotAPI.Get_AbilityVia_ref` - not ported yet
- `OgreBotAPI:Get_MissionTimerInfo` - not ported yet
- `OgreBotAPI.Get_NumAdornmentsOfColour` - not ported yet
- `OgreBotAPI:Get_Poisons` - not ported yet
- `OgreBotAPI.Get_RewardID` - exists, does nothing yet
- `OgreBotAPI.Get_RewardLinkID` - exists, does nothing yet
- `OgreBotAPI.Get_RewardName` - exists, does nothing yet
- `OgreBotAPI.Get_RotationData` - exists, does nothing yet
- `OgreBotAPI.Get_Turbo` - exists, does nothing yet
- `OgreBotAPI.GetDeityPoints` - exists, does nothing yet
- `OgreBotAPI:GO_CryptofDalnir_WizardsDen_EventHeroic_King` - exists, does nothing yet
- `OgreBotAPI:GuidedAscension` - not ported yet
- `OgreBotAPI:HandleLootWindow` - not ported yet
- `OgreBotAPI.HardCodedAbilityEffectRadius` - not ported yet
- `OgreBotAPI.HardCodedAbilityMaxRange` - not ported yet
- `OgreBotAPI:HQEar_Recheck` - exists, does nothing yet
- `OgreBotAPI:HQEar_ReEquipOriginalEar` - exists, does nothing yet
- `OgreBotAPI:HQEar_ReportStuckEar` - exists, does nothing yet
- `OgreBotAPI.InBattleGround` - exists, does nothing yet
- `OgreBotAPI.InEQ2Chars` - exists, does nothing yet
- `call OgreBotAPI.Interrupt_Mode` - not ported yet
- `OgreBotAPI.IsItemTimeUntilReadyZero` - not ported yet
- `OgreBotAPI:ItemDebug` - not ported yet
- `OgreBotAPI.jvCacheEquipmentAdornmentNames` - not ported yet
- `OgreBotAPI:KronoWindowCheck` - exists, does nothing yet
- `OgreBotAPI.LandFlyingMountActive` - not ported yet
- `OgreBotAPI:Loot_SmartAssign_Add` - not ported yet
- `OgreBotAPI:Loot_SmartAssign_Update` - not ported yet
- `OgreBotAPI:Mount` - not ported yet
- `OgreBotAPI:Myzer1` - not ported yet
- `OgreBotAPI:Myzer2` - not ported yet
- `OgreBotAPI:NoTanking` - not ported yet
- `OgreBotAPI:NPC_CastMonitoring` - exists, does nothing yet
- `OgreBotAPI.NPCsWithinRange` - exists, does nothing yet
- `OgreBotAPI.ogre_campspot_me` - not ported yet
- `OgreBotAPI:OLD_ChangeOgreBotUIOption` - not ported yet
- `OgreBotAPI:Output_InGame_MovementKeys` - not ported yet
- `OgreBotAPI:Overseer_SpewMissionsInInventory` - exists, does nothing yet
- `OgreBotAPI:Populate_ExportList` - not ported yet
- `OgreBotAPI:PopulatePCOptionLists` - not ported yet
- `OgreBotAPI:Prepare_TankSwapping` - exists, does nothing yet
- `OgreBotAPI:PulseCircleMovement` - not ported yet
- `OgreBotAPI.PulseCircleMovement_CurrentSpot` - not ported yet
- `OgreBotAPI.PulseCircleMovement_TimerRecentlyMoved` - not ported yet
- `OgreBotAPI.QueuedCommands` - exists, does nothing yet
- `OgreBotAPI:Reload_DevBot` - not ported yet
- `OgreBotAPI:ReloadExport` - not ported yet
- `OgreBotAPI:Remove_Prepare_TankSwapping` - exists, does nothing yet
- `OgreBotAPI.ReplyDialog_ReplyExists` - exists, does nothing yet
- `OgreBotAPI:Report_Back` - not ported yet
- `OgreBotAPI:Report_ClearList` - exists, does nothing yet
- `OgreBotAPI.Report_Group_GetKey` - exists, does nothing yet
- `OgreBotAPI.Report_Group_GetValue` - exists, does nothing yet
- `OgreBotAPI:Report_SpewList` - exists, does nothing yet
- `OgreBotAPI:ReportForList_IRC` - exists, does nothing yet
- `OgreBotAPI:Reporting` - exists, does nothing yet
- `OgreBotAPI:ResolveBuffCheck` - exists, does nothing yet
- `OgreBotAPI.RewardWindow_Get_WindowID` - exists, does nothing yet
- `OgreBotAPI:RewardWindow_Spew_WindowIDs` - exists, does nothing yet
- `OgreBotAPI:RO_FSD_BB_Brutas_DoNotNeedColdWater` - exists, does nothing yet
- `OgreBotAPI:RO_FSD_BB_Brutas_NeedColdWater` - exists, does nothing yet
- `OgreBotAPI.RoomID` - not ported yet
- `OgreBotAPI.RoR_Epic_AbilityID` - exists, does nothing yet
- `OgreBotAPI.RoR_Epic_Available` - exists, does nothing yet
- `OgreBotAPI:RoR_Epic_ChangeInCastStack` - exists, does nothing yet
- `OgreBotAPI.RoR_Epic_Ready` - exists, does nothing yet
- `OgreBotAPI:Set_VampiricRequiem_Cancelling_Active` - exists, does nothing yet
- `OgreBotAPI:SetQuestion` - not ported yet
- `OgreBotAPI:SetRelayGroup` - exists, does nothing yet
- `OgreBotAPI:SetRelayGroup_Relay` - not ported yet
- `OgreBotAPI:SetRelayGroupToDefault` - not ported yet
- `OgreBotAPI:SetRelayGroupToDefault_Relay` - not ported yet
- `OgreBotAPI:ShareQuestWhenAble` - exists, does nothing yet
- `OgreBotAPI:SmartLoot_LOL_AssignPlayer_Item` - not ported yet
- `OgreBotAPI.SourceAvailable` - exists, does nothing yet
- `OgreBotAPI:SpawnEvent_AddEntry` - exists, does nothing yet
- `OgreBotAPI:SpawnEvent_RemoveEntry` - exists, does nothing yet
- `OgreBotAPI.SpecialDebugMode` - not ported yet
- `OgreBotAPI:SpendDeityPoints` - not ported yet
- `OgreBotAPI:SpendDietyPoints` - not ported yet
- `OgreBotAPI:Spew_Get_AbilityVia` - exists, does nothing yet
- `OgreBotAPI:SpewAbility` - exists, does nothing yet
- `OgreBotAPI:Test_ExportList` - not ported yet
- `OgreBotAPI.Timer_Exit` - not ported yet
- `OgreBotAPI:Travel_Report` - not ported yet
- `OgreBotAPI:TravelBell_Report` - not ported yet
- `OgreBotAPI:TravelDruid_Report` - not ported yet
- `OgreBotAPI:TravelSpires_Report` - not ported yet
- `OgreBotAPI:Unpack_EmpyralStones` - exists, does nothing yet
- `OgreBotAPI:Unpack_PlanarStones` - exists, does nothing yet
- `OgreBotAPI:Update_Guk_Shinies` - not ported yet
- `OgreBotAPI:Update_PoP_Shinies` - not ported yet
- `OgreBotAPI:Update_Turbo` - exists, does nothing yet
- `OgreBotAPI:VampiricRequiem_AbilityCancel` - not ported yet
- `call OgreBotAPI.WaitForCasting` - not ported yet
- `OgreBotAPI.WeaponSlotSubTypes` - not ported yet
- `OgreBotAPI:ZoneInto` - not ported yet
- `OgreBotAPI.ZoneReset_Get_ZoneData` - exists, does nothing yet
- `OgreBotAPI.ZoneReset_IsReady` - exists, does nothing yet
- `OgreBotAPI.ZoneReset_IsUpdating` - exists, does nothing yet
- `OgreBotAPI:ZoneReset_UpdateInfo` - exists, does nothing yet
