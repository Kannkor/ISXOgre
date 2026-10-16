# Other Classic objects

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../index.md).
</div>

The Classic objects scripts used that Classic's docs never had a page for (`GetInfoOb`, `ClassInfo`, `TabConfig`, `Ob_AutoTarget`, …), and what each name is in the new bot. None of these objects exists in the new bot.

> **:warning: An old call does nothing now - it does not give an error**
>
> The new bot does not keep the old names. A call to an old method silently does nothing and a read of an old member gives `NULL`. Find your name below and write what the row says instead.

## At a glance

| What happened | Names |
|---|---|
| ⚠️ Arguments changed | 70 |
| ✏️ Renamed | 90 |
| ➡️ Moved | 6 |
| ➡️ Lives somewhere else | 160 |
| 📄 In a data file now | 26 |
| ⛔ Exists, does nothing yet | 3 |
| ⛔ Not ported yet | 197 |
| ⛔ Removed | 50 |
| **Total** | **602** |

## Worked examples

One real Classic line per kind of change, and the line that replaces it.

### ⚠️ Arguments changed: `call Obj_OgreUtilities.NavToLoc`

```
; before (Classic)
call Obj_OgreUtilities.NavToLoc "-665.449280,79.212479,102.971169"
; after (new bot)
OgreBotAPI.Movement:NavTo[all,-665.449280,79.212479,102.971169]
```

### ✏️ Renamed: `GetInfoOb.GetBaseClass`

```
; before (Classic)
sBaseClass:Set["${GetInfoOb.GetBaseClass[${Me.Raid[${iCounter}].Class}]}"]
; after (new bot)
sBaseClass:Set["${OgreBotAPI.Roster.BaseClassOf[${Me.Raid[${iCounter}].Class}]}"]
```

### ➡️ Moved: `GetInfoOb.Alias`

```
; before (Classic)
sTarget:Set["${GetInfoOb.Alias["${sTarget}"]}"]
; after (new bot)
sTarget:Set["${OgreBotAPI.ForWho.Alias["${sTarget}"]}"]
```

### 📄 In a data file now: `call Obj_OgreUtilities.HandleWaitForCombat`

```
; before (Classic)
call Obj_OgreUtilities.HandleWaitForCombat -TimeOutIfNoProgress 30
; after (new bot)
{ "do": "waitForCombat", "noProgressMs": 30000 }
```

## Obj_OgreUtilities

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `Obj_OgreUtilities:AcceptQuest` | does nothing | `OgreBotAPI.Quest:Accept` | ⚠️ Arguments changed | For-who is new as argument 0; questName (argument 1) is accepted and ignored. |
| `Obj_OgreUtilities.Alignment` | reads NULL | — | ⛔ Not ported yet | Classic: Good / Evil / None / Unknown from the bind location (Me.GetGameData[Self.BindLocation]). 0 calls. New: no BindLocation or alignment read anywhere in ISXOgreEQ2 (searched). |
| `Obj_OgreUtilities.AnyGroupMembersDead` | reads NULL | — | ⛔ Not ported yet | Classic: is any group member (me included) dead. New: no script-facing read (searched Roster / Combat / Zone regs,). The IC reads it privately: the path's dead-member hold and the named step's after-fight res run. |
| `Obj_OgreUtilities.CallingScriptName` | reads NULL | — | ⛔ Not ported yet | Classic: internal - the script that created the object, passed to OgreNavLib / ZoneReset. No script on the new bot owns these engines. |
| `call Obj_OgreUtilities.CallToGH` | does nothing | `OgreBotAPI.Movement:CallGH` | ⚠️ Arguments changed | For-who is new as argument 0. No _OnlyIfAvailableNow, no wait, no result. The fallback state machine is Movement:GetToGH; in an IC file, `recover` op callGH. |
| `call Obj_OgreUtilities.CastAbilityID` | does nothing | `OgreBotAPI.Abilities:Cast` | ⚠️ Arguments changed | For-who is argument 0, the id argument 1. Nothing waits for the cast; in a data file wait on `not selfCasting`. |
| `call Obj_OgreUtilities.CastEvac` | does nothing | `OgreBotAPI.Movement:Evac` | ⚠️ Arguments changed | For-who is argument 0, `totem` argument 1. It does not wait for the zone and has no _ref: failures are said in the log. In an IC file the `recover` op evac runs the group ladder. |
| `call Obj_OgreUtilities.CheckEvacTotems` | does nothing | — | ⛔ Not ported yet | Classic: an evac class or a scout needs nothing; otherwise make sure a Totem of Escape is at hand, withdrawing 100 from the 'Poison, Potion, & Totem Depot'. 0 calls. New: Movement:Evac with `totem` USES a totem in the bags but nothing stocks them. |
| `call Obj_OgreUtilities.CheckIfGroupInSameZone` | does nothing | `OgreBotAPI.Roster.InZone` | ⚠️ Arguments changed | A member, not a waiting function: it answers once; loop on it yourself, or in an IC file use `zoneOut`, which waits for the group in the new zone. |
| `Obj_OgreUtilities.CleanName` | reads NULL | `OgreBotAPI.Util.Clean` | ✏️ Renamed |  |
| `call Obj_OgreUtilities.ClearQuestWindow` | does nothing | — | ⛔ Not ported yet | Classic: untick the active-quest HUD entries. 0 calls. No equivalent found. |
| `call Obj_OgreUtilities.Close_Depot` | does nothing | — | ⛔ Not ported yet | Classic: click the container window's Close until it is gone. Part of Handle_Depot; no equivalent door. |
| `call Obj_OgreUtilities.ConverseWithScrollMerchant` | does nothing | — | ⛔ Not ported yet | Classic: hail the scroll merchant and run HandleConversation, writing errors / times into a persistentref. 0 calls. No equivalent found. |
| `Obj_OgreUtilities.ConvertSecondsToHMS` | reads NULL | `OgreBotAPI.Util.SecondsToHMS` | ✏️ Renamed |  |
| `Obj_OgreUtilities:DeleteQuest` | does nothing | `OgreBotAPI.Quest:Delete` | ⚠️ Arguments changed | For-who is new as argument 0; _Silent is gone. |
| `Obj_OgreUtilities:DeleteQuestActual` | does nothing | `OgreBotAPI.Quest:Delete` | ⚠️ Arguments changed | For-who is new as argument 0; the quest name is argument 1; _Silent is gone. |
| `Obj_OgreUtilities:Depot_Button` | does nothing | — | ⛔ Not ported yet | Classic: press the container's Deposit All. Part of Handle_Depot; only DepotTransfer presses it on the new bot. |
| `Obj_OgreUtilities.Depot_Visible` | reads NULL | — | ⛔ Not ported yet | Classic: is the container window up. Part of Handle_Depot; no script-facing read on the new bot. |
| `Obj_OgreUtilities.DepotNames` | reads NULL | — | ⛔ Not ported yet | Classic: the four harvest-depot names Handle_Depot looks for. Internal to Handle_Depot (see it). |
| `call Obj_OgreUtilities.DoConversation` | does nothing | `OgreBotAPI.Comms:ConversationBubble` | ⚠️ Arguments changed | For-who is argument 0 and ONE reply per call (argument 1, default 1) - no list, no waits. In a data file: `actorInteract` op dialog `choices`. |
| `call Obj_OgreUtilities.DoHail` | does nothing | `OgreBotAPI.Actors:Hail` | ⚠️ Arguments changed | For-who is new as argument 0; the name is resolved partially (targetwho::Resolve), and with nothing found it hails the nearest NoKill NPC within 10 m. |
| `call Obj_OgreUtilities.DoHailID` | does nothing | `OgreBotAPI.Actors:Hail` | ⚠️ Arguments changed | For-who is new as argument 0. |
| `call Obj_OgreUtilities.DoTarget` | does nothing | `OgreBotAPI:Target` | ⚠️ Arguments changed | For-who is new as argument 0; no range limit; nothing is returned. |
| `Obj_OgreUtilities:EQ2_onQuestOffered` | does nothing | automatic (no call) | ➡️ Lives somewhere else | Nothing to call: the new bot accepts new-quest offers by itself (setting checkbox_settings_donotacceptquests turns it off). |
| `Obj_OgreUtilities:EQ2_onRewardWindowAppeared` | does nothing | automatic (no call) | ➡️ Lives somewhere else | Nothing to call: the new bot accepts no-choice reward windows by itself. |
| `Obj_OgreUtilities.EscapeTotemName` | reads NULL | — | ⛔ Not ported yet | Classic: the item name "Totem of Escape" used by CheckEvacTotems / CastEvac. New: the name is a constant inside Movement:Evac; not settable. |
| `call Obj_OgreUtilities.FastTravel` | does nothing | `OgreBotAPI.Travel:Fast` | ⚠️ Arguments changed | For-who is new as argument 0; _ExactMatch TRUE becomes the flag -em. |
| `Obj_OgreUtilities.Get_Hours` | reads NULL | `OgreBotAPI.Util.Hours` | ✏️ Renamed |  |
| `Obj_OgreUtilities.Get_Minutes` | reads NULL | `OgreBotAPI.Util.Minutes` | ✏️ Renamed |  |
| `Obj_OgreUtilities.Get_Seconds` | reads NULL | `OgreBotAPI.Util.Seconds` | ✏️ Renamed |  |
| `Obj_OgreUtilities.Get_ZoneName` | reads NULL | — | ⛔ Not ported yet | Classic: "GUILDHALL" in a guild hall, otherwise the zone name without its number. 0 calls. No single member: OgreBotAPI.Zone.InGuildHall and OgreBotAPI.Zone.Name (number stripped, :3294) are the two halves. |
| `Obj_OgreUtilities.GetAscensionClass` | reads NULL | `ISXOgreEQ2.Class.AscensionClass` | ➡️ Moved |  |
| `call Obj_OgreUtilities.GetInGameQuestStep` | does nothing | — | ⛔ Not ported yet | Classic: makes the quest current in the journal and returns its first unchecked step (text, index, counts, zone) in a collection. New: no journal step reader. |
| `call Obj_OgreUtilities.GetIntoCorrectZone` | does nothing | — | ⛔ Not ported yet | Classic: CORRECTZONE / GUILDHALL / else CallToGH, then CheckEvacTotems + GetIntoZoneFromGH. Incomplete in Classic itself: WhereAreWe never returns CORRECTZONE (that case is commented out, :1927-1929) and GetIntoZoneFromGH is not defined in this objectdef. 0 calls. |
| `call Obj_OgreUtilities.GHToHouse` | does nothing | — | ⛔ Not ported yet | Classic: double-click 'Portal to Housing', filter the house list by name, enter, wait for zoning. 0 calls. New: no 'go to a house' door; the housing-portal clicks exist only inside DepotTransfer's transfer flow and GetToGH's guild-hall tab. |
| `Obj_OgreUtilities.GroupInCombat` | reads NULL | — | ⛔ Not ported yet | Classic: any group member (not me) in combat mode; 3 calls. New: no script-facing or data-file read of group combat - OgreBotAPI.Combat.InCombat is ME only; the `inCombat` condition is me only too. |
| `Obj_OgreUtilities.GroupWithinDistance` | reads NULL | `OgreBotAPI.Position.FarthestGroupDistance` | ⚠️ Arguments changed | Returns a number, not TRUE/FALSE. It counts every group member (a mercenary too), where Classic skipped non-PCs. In a data file: the `groupDistance` condition. |
| `call Obj_OgreUtilities.Handle_Depot` | does nothing | — | ⛔ Not ported yet | Classic: for every harvest depot within 12 m, open it and press Deposit All. 0 calls. New: nothing deposits bag harvests into a nearby depot. DepotTransfer clicks the same Deposit All button, but only inside its house &lt;-&gt; guild-hall depot transfer. |
| `call Obj_OgreUtilities.HandleCampSpotToLoc` | does nothing | `campSpot` | 📄 In a data file now | Two steps: {"do":"campSpot","op":"setLoc","loc":[x,y,z],"sendTo":"igw:{{me}}"} then {"wait":"atCampSpot","limitMs":...,"onTimeout":...}. |
| `call Obj_OgreUtilities.HandleCampSpotToPort` | does nothing | — | ⛔ Not ported yet | Classic: camp the group onto a teleport spot and wait until the camp spot is suddenly far (we were ported), then clear it; one call, in an Archive file. New: nothing walks the group INTO a teleport loc. The IC `teleporter` step is the clicked kind only - every toon clicks an actor. |
| `call Obj_OgreUtilities.HandleClickActor` | does nothing | `OgreBotAPI.Actors:Click` | ⚠️ Arguments changed | For-who is new as argument 0. No distance limit and no wait for the cast; use OgreBotAPI.Actors:ClickQueued if you need the cast-bar wait. |
| `call Obj_OgreUtilities.HandleClickActor_Special` | does nothing | `OgreBotAPI:Special` | ⚠️ Arguments changed | For-who is new as argument 0; no distance limit, no cast wait. |
| `call Obj_OgreUtilities.HandleConversation` | does nothing | — | ⛔ Not ported yet | Classic: walks a hard-coded list of class-trainer conversation lines (Chosooth, Najena, Miragul...) for ConverseWithScrollMerchant. 0 external calls. No equivalent; the generic form is `actorInteract` op dialog. |
| `call Obj_OgreUtilities.HandleConversationByText` | does nothing | `actorInteract` | 📄 In a data file now | The match is 'contains', not 'equals'. No script door clicks a reply by text (Comms:ConversationBubble takes a number). |
| `call Obj_OgreUtilities.HandleWaitForCampSpot` | does nothing | `atCampSpot` | 📄 In a data file now | A wait needs limitMs and onTimeout - Classic had no limit. The leading _Delay is a separate {"wait":"ms"} step. |
| `call Obj_OgreUtilities.HandleWaitForCombat` | does nothing | `waitForCombat` | 📄 In a data file now | -Wait (deciseconds) -&gt; settleMs (x100); -SkipIfNoMobsRange -&gt; settleWithin; -TimeOutIfNoProgress (seconds) -&gt; noProgressMs (x1000). -NPCName / -ExitOnNPCAggroName / -ClearTarget have no keys: a named's fight is the `named` step's, and a stale target is dropped by the step itself. |
| `call Obj_OgreUtilities.HandleWaitForCombat_old` | does nothing | — | ⛔ Not ported yet | Classic: the superseded positional version of HandleWaitForCombat; 0 calls in Classic itself. |
| `call Obj_OgreUtilities.HandleWaitForCombatOrPower` | does nothing | — | ⛔ Not ported yet | Classic: hold while in combat AND power &gt; 1% - i.e. leave a fight when out of power; 3 calls. New: `waitForCombat` has no power exit. A `wait` on `or` of `not inCombat` and `myStat` {stat: power, compare: "&lt;=", value: 1} expresses the exit, but nothing drops the far target the way Classic did. |
| `call Obj_OgreUtilities.HandleWaitForCombatUntilNPCSpawns` | does nothing | `actorPresent` | 📄 In a data file now | The 'drop a target beyond N' leg has no twin in a wait; waitForCombat drops a stale target on its own ( rule 6). |
| `call Obj_OgreUtilities.HandleWaitForCombatWithNPC` | does nothing | `named` | 📄 In a data file now | For a plain 'until nothing hates us' hold use the `waitForCombat` step. |
| `call Obj_OgreUtilities.HandleWaitForGroupDistance` | does nothing | `groupDistance` | 📄 In a data file now | A wait needs limitMs and onTimeout - Classic blocked forever. The farthest-member read counts every group member, not only PCs. |
| `call Obj_OgreUtilities.HandleWaitForNPCToSpawn` | does nothing | `actorPresent` | 📄 In a data file now | The IC `named` step already waits for its named to spawn. |
| `call Obj_OgreUtilities.HandleWaitForZoning` | does nothing | `zoneOut` | 📄 In a data file now |  |
| `call Obj_OgreUtilities.HandleWaitTime` | does nothing | `ms` | 📄 In a data file now | {"wait":"ms","limitMs":&lt;deciseconds x 100&gt;,"onTimeout":"proceed"}. |
| `call Obj_OgreUtilities.HandleZoneDoor` | does nothing | `OgreBotAPI.Travel:ZoneDoorFor` | ⚠️ Arguments changed | For-who is new as argument 0, the option argument 1. In a data file: the `zoneDoorWindow` action (op choose). |
| `Obj_OgreUtilities.HaveAbilityID` | reads NULL | `hasAbility` | 📄 In a data file now |  |
| `Obj_OgreUtilities.IndexMatch` | does nothing (stub) | `OgreBotAPI.IndexMatch` *(does nothing yet)* | ⛔ Exists, does nothing yet |  |
| `Obj_OgreUtilities.InGuildHallZone` | reads NULL | `OgreBotAPI.Zone.InGuildHall` | ✏️ Renamed | Slightly wider than this list (it also knows guildhall_drunder, guildhall_skyshrinecapital and the catch-all). |
| `Obj_OgreUtilities:Initialize_Depot` | does nothing | — | ⛔ Not ported yet | Classic: fills DepotNames. Internal to Handle_Depot (see it). |
| `Obj_OgreUtilities.InternalVersion` | reads NULL | — | ⛔ Not ported yet | Classic: the backing string "1.001" returned by Version (75-78). There is no utilities object on the new bot to have a version; see Version for the adapter's. |
| `Obj_OgreUtilities.InZoneName` | reads NULL | `zone` | 📄 In a data file now | In a script: ${OgreBotAPI.Zone.Name} is the zone name with the number stripped - compare it yourself. |
| `Obj_OgreUtilities.InZoneShortName` | reads NULL | — | ⛔ Not ported yet | ISXEQ2's own ${Zone.ShortName} is still there for a script. |
| `Obj_OgreUtilities.IsAnyoneDead` | reads NULL | — | ⛔ Not ported yet | Classic: any group member (me included) is dead; 5 calls in. New: no script-facing read (see AnyGroupMembersDead); the IC's path / named holds read it privately. |
| `Obj_OgreUtilities.IsGroupDead` | reads NULL | `onWipe` | 📄 In a data file now | Nothing to test in the file: author the recovery as the `onWipe` list (and `afterWipe`). No script-facing 'group is dead' member exists. |
| `Obj_OgreUtilities.IsGroupDeadOrNoRes` | reads NULL | — | ⛔ Not ported yet | Classic: someone is dead AND (everyone is dead OR no living priest); 2 calls in/:661. New: no script-facing or data-file read; the IC wipe watch tests 'everyone dead' only. |
| `Obj_OgreUtilities.ItemCount` | does nothing (stub) | `OgreBotAPI.Inventory.Count` *(does nothing yet)* | ⛔ Exists, does nothing yet | Do NOT use OgreBotAPI.Loot.ItemCount: it is SmartLoot's count of distinct capped item names, not a bag count. The data-file condition `hasItem` answers only 'is it in my bags' ( cond_hasItem). |
| `Obj_OgreUtilities:Jump` | does nothing | `OgreBotAPI.Movement:Jump` | ⚠️ Arguments changed | For-who is new as argument 0. |
| `call Obj_OgreUtilities.LoginToon` | does nothing | `ogre login` | ➡️ Lives somewhere else | It does not wait; the login runs in the adapter. |
| `call Obj_OgreUtilities.NavTo` | does nothing | `OgreBotAPI.Movement:NavTo` | ⚠️ Arguments changed | For-who is argument 0; no _HowClose and no wait (see NavToLoc). |
| `call Obj_OgreUtilities.NavToLoc` | does nothing | `OgreBotAPI.Movement:NavTo` | ⚠️ Arguments changed | For-who is argument 0, then X, Y, Z as three arguments. It returns at once - there is no precision and no wait; read ${ISXOgreEQ2.Nav.NavActive} or, in a data file, use `movement` op navTo and wait on `moveFinished`. In an IC file the `path` step navs the group itself. |
| `call Obj_OgreUtilities.NavToLocation` | does nothing | — | ⛔ Not ported yet | Navigating to the region's coordinates works: OgreBotAPI.Movement:NavTo (see NavToLoc). |
| `Obj_OgreUtilities.NearLoc` | reads NULL | `nearSpot` | 📄 In a data file now | {"nearSpot":{"spots":[[x,y,z]],"within":10}}. No script-facing member; in a script, ISXEQ2's ${Math.Distance[${Me.Loc},x,y,z]} still answers it. |
| `Obj_OgreUtilities.NPCCount` | reads NULL | `count` | 📄 In a data file now |  |
| `Obj_OgreUtilities.NPCHatedCount` | reads NULL | `count` | 📄 In a data file now | {"count":{"of":"actors","find":{"query":"Distance &lt;= 30 && (Type == \"NPC\" \|\| Type == \"NamedNPC\") && Target.ID &gt; 0"},"compare":"&gt;","value":0}}. No script-facing member counts this. |
| `Obj_OgreUtilities.Obj_OgreResources` | reads NULL | — | ⛔ Not ported yet | Classic: an Object_OgreResources. 0 references in instance or raid files. No equivalent found in ISXOgreEQ2 (searched the registrations). |
| `Obj_OgreUtilities.Obj_Travel` | reads NULL | `OgreBotAPI.Travel:Fast` | ➡️ Lives somewhere else | The rest of Object_Travel maps onto the same sub-object (Travel, Bell, Druid, Spires, ToGuildHall, ZoneDoor...). |
| `Obj_OgreUtilities.OgreNavChecks` | reads NULL | — | ⛔ Not ported yet | Classic: OgreNavLib's movement checks; content toggles them, e.g. Obj_OgreUtilities.OgreNavChecks:Set_Check_Group[FALSE,1000]. New: the OgreNavLib layer is a stub; the new nav has its own tunables through ISXOgreEQ2.Nav:Set, not these checks. |
| `Obj_OgreUtilities.OgreNavEntry` | reads NULL | — | ⛔ Not ported yet | Classic: the OgreNavLib request object that NavToLocation / NavToLoc fill. The OgreNavLib layer is not ported: `ogre navlib` is a stub word, 'NOT PORTED YET'. Point-to-point nav is OgreBotAPI.Movement:NavTo (see NavToLoc). |
| `Obj_OgreUtilities.OnCorrectCharacter` | reads NULL | — | ⛔ Not ported yet | Classic: CleanName[Me.Name] equals the toon. 0 calls. No member; compare ${OgreBotAPI.Util.Clean[${Me.Name}]} yourself (see CleanName). |
| `call Obj_OgreUtilities.OnQuestStep` | does nothing | — | ⛔ Not ported yet | Classic: is quest X on a step whose text matches (-ExactMatch, -StepIndex, -CurrentZoneOnly, extra -StepText) - reads the journal via GetInGameQuestStep; 19 calls, e.g.. New: no quest-step reader. The Quest sub-object has Have / ActorHas / DeityPoints / SkipShinies; the only journal reads are the current quest's NAME and completed-quest lookups for travel. |
| `call Obj_OgreUtilities.Open_Depot` | does nothing | — | ⛔ Not ported yet | Classic: DoubleClick a depot by id and wait for the window. Part of Handle_Depot. (A plain double-click by id is OgreBotAPI.Actors:Click.) |
| `call Obj_OgreUtilities.PreCombatBuff` | does nothing | `named` | 📄 In a data file now | Only before a named pull: keys prebuffMs (_Seconds x 1000) and preCastTagMs (_TagDuration x 1000) on the `named` step. There is no standalone buff-up step. |
| `Obj_OgreUtilities.QuestIt` | reads NULL | — | ⛔ Not ported yet | Classic: internal iterator over Quests. Not script-facing. |
| `Obj_OgreUtilities.Quests` | reads NULL | — | ⛔ Not ported yet | Classic: internal index filled by UpdateQuestInformation for DeleteQuest. Quest:Delete does its own lookup. |
| `Obj_OgreUtilities.RemoveZoneNumber` | reads NULL | `OgreBotAPI.Util.StripZoneNumberOnly` | ✏️ Renamed | Util.StripZoneNumber also removes colour codes first; the utilities version did not. |
| `call Obj_OgreUtilities.ResetCameraAngle` | does nothing | `OgreBotAPI.Client:ResetCamera` | ⚠️ Arguments changed | For-who is new as argument 0. It does not change the point of view. |
| `call Obj_OgreUtilities.Revive` | does nothing | `OgreBotAPI.Session:Revive` | ⚠️ Arguments changed | For-who is new as argument 0. Row 0 / select_junction 0 has no twin - blank or 0 presses the default Revive button. |
| `Obj_OgreUtilities:Set_EQ2_onQuestOffered` | does nothing | `OgreBotAPI.Options:Set` | ➡️ Lives somewhere else | Nothing to attach: the new bot accepts new-quest offers by itself. To turn that off, set checkbox_settings_donotacceptquests to TRUE with OgreBotAPI.Options:Set.<br>Polarity flips: Set_EQ2_onQuestOffered[TRUE] (accept) is checkbox_settings_donotacceptquests = FALSE. |
| `Obj_OgreUtilities:Set_EQ2_onRewardWindowAppeared` | does nothing | automatic (no call) | ➡️ Lives somewhere else | Nothing to call: the new bot accepts no-choice reward windows by itself. |
| `call Obj_OgreUtilities.Set_FirstPersonView` | does nothing | — | ⛔ Not ported yet | Classic: NEXTPOVSETTINGS until first person. 0 calls. New: no standalone 'go first person' door; first person is only the endInFirstPerson argument of Client:SetCameraPitch and the camera action's firstPerson key. |
| `call Obj_OgreUtilities.Set_LookDown` | does nothing | `OgreBotAPI.Client:SetCameraPitch` | ⚠️ Arguments changed | A pitch angle, not a hold time. |
| `call Obj_OgreUtilities.Set_LookUp` | does nothing | `OgreBotAPI.Client:SetCameraPitch` | ⚠️ Arguments changed | The argument is a pitch angle (-75..75, 0 centre), not a hold time. Whether the look/zoom key binds come back is open. |
| `call Obj_OgreUtilities.Set_ZoomIn` | does nothing | — | ⛔ Not ported yet | Classic: EMPTY body. Nothing to port. |
| `call Obj_OgreUtilities.Set_ZoomOut` | does nothing | — | ⛔ Not ported yet | Classic: hold the zoom-out key for _Value deciseconds. 0 calls. New: no zoom verb. |
| `call Obj_OgreUtilities.Set_ZoomOut_MouseWheel` | does nothing | — | ⛔ Not ported yet | Classic: press MouseWheelDown _Value times. 0 calls. No zoom verb on the new bot. |
| `Obj_OgreUtilities.Timer_HandleWaitForCombatw` | reads NULL | — | ⛔ Not ported yet | Classic: HandleWaitForCombat's no-progress timer. Internal; the clock is the `waitForCombat` step's noProgressMs. |
| `Obj_OgreUtilities.Timer_PreCombatBuff` | reads NULL | — | ⛔ Not ported yet | Classic: PreCombatBuff's own timer. Internal; the buff-up's clock is the `named` step's prebuffMs (see PreCombatBuff). |
| `Obj_OgreUtilities:UpdateQuestInformation` | does nothing | — | ⛔ Not ported yet | Classic: internal step of DeleteQuest - QuestJournalWindow:GetActiveQuests into Quests. Nothing to call on the new bot: Quest:Delete finds the quest itself. |
| `Obj_OgreUtilities.Version` | reads NULL | `ISXOgreEQ2.Version` | ➡️ Lives somewhere else | This is the whole extension's version, not a utilities version. |
| `call Obj_OgreUtilities.WaitForActorClick` | does nothing | `OgreBotAPI.Actors:ClickQueued` | ⚠️ Arguments changed | The caller no longer waits; the click is queued. In a data file: `actorInteract` with awaitCastBar. |
| `call Obj_OgreUtilities.WaitForCasting` | does nothing | `selfCasting` | 📄 In a data file now | {"wait":{"not":{"selfCasting":{}}},"limitMs":...,"onTimeout":...}. |
| `call Obj_OgreUtilities.WaitForGroupPower` | does nothing | — | ⛔ Not ported yet | Classic: wait until every group member's power &gt;= _PowerPercent. 0 calls. New: `myStat` is my own only; no group power read in the condition table (2660-2712) or the Roster regs. |
| `call Obj_OgreUtilities.WaitForGroupToZone` | does nothing | `zoneOut` | 📄 In a data file now | The health &gt; 90% leg is not part of zoneOut. |
| `call Obj_OgreUtilities.WaitForLootWindow` | does nothing | `waitForLoot` | 📄 In a data file now |  |
| `call Obj_OgreUtilities.WaitForPower` | does nothing | `myStat` | 📄 In a data file now |  |
| `call Obj_OgreUtilities.WaitForScript` | does nothing | — | ⛔ Not ported yet | Classic: wait up to 5 s for a script to start, then while it runs. 0 calls. |
| `call Obj_OgreUtilities.WaitForZoning` | does nothing | `zoneOut` | 📄 In a data file now | The door pick alone is OgreBotAPI.Travel:ZoneDoorFor. |
| `call Obj_OgreUtilities.WaitWhileGroupMembersDead` | does nothing | `path` | 📄 In a data file now | There is no standalone 'wait while dead' step; it is part of `path` and `named`. |
| `Obj_OgreUtilities.WhereAreWe` | reads NULL | — | ⛔ Not ported yet | Classic: GUILDHALL for any guild-hall short name, otherwise Zone.ShortName. 0 external calls. No single member; OgreBotAPI.Zone.InGuildHall answers the guild-hall half, and ISXEQ2's ${Zone.ShortName} the rest. |
| `Obj_OgreUtilities:ZoneReset_PopulateInternalMemory` | does nothing | — | ⛔ Not ported yet | Classic: Obj_ZoneReset:PopulateInternalMemory, loading the zone-reuse timers; called only by Classic's. New: the Zone sub-object's reset reads are STUBS returning FALSE - ResetZoneData / ResetReady / ResetUpdating / ResetInfoAvailable. The zone resetter is `ogre zone`. |
| `Obj_OgreUtilities.ZoneTeleporterWindowVisible` | reads NULL | `zoneDoorWindow` | 📄 In a data file now |  |

## TabConfig

**Note A** (84 rows below): Read an OgreBot setting with `${ISXOgreEQ2.OgreBot.Value["<control id>"]}`. Only names that start `checkbox_`, `combobox_`, `textentry_`, `slider_` or `listbox_` are settings - the other `TabConfig` names were Classic methods, and reading them this way gives empty text. A setting that is not there also reads as empty text, which counts as FALSE, so say the default yourself. The value is text (`"TRUE"`), not true/false.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `TabConfig.AbilityResearch` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.AbilityResearchSettings` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.AbilityRotation` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.AbilityTracker` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig:After_Initialization` | does nothing | — | ⛔ Not ported yet | Note A |
| `TabConfig.Aliases` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.Announce` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.Ascension` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.AscensionEmbargoList` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.AscensionList` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.Assassin` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.Assist` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.AutoHunt` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.AutoHunt_Path` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.AutoTarget` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.BaseSetName` | reads NULL | — | ⛔ Not ported yet | Note A |
| `TabConfig.BaseSetRef` | reads NULL | — | ⛔ Not ported yet | Note A |
| `TabConfig.Brigand` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.CastStack` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.Channeler` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.ChatEvents` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.CodexSettings` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.Coercer` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.Conjuror` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.ConsumeItems` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.Crowd_Control` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.Crowd_Control_Settings` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.Debug` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.Defiler` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.DespawnEvents` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.Dirge` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.DoNotSave` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.EquipmentInfo` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig:GUI_Discord` | does nothing | — | ⛔ Not ported yet | Note A |
| `TabConfig:GUI_Forums` | does nothing | — | ⛔ Not ported yet | Note A |
| `TabConfig:GUI_Helper` | does nothing | — | ⛔ Not ported yet | Note A |
| `TabConfig:GUI_LastClickedTab` | does nothing | — | ⛔ Not ported yet | Note A |
| `TabConfig:GUI_TabClicked` | does nothing | — | ⛔ Not ported yet | Note A |
| `TabConfig:GUI_Wiki` | does nothing | — | ⛔ Not ported yet | Note A |
| `TabConfig.HOExcludes` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.HUDs` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig:InitSetup` | does nothing | — | ⛔ Not ported yet | Note A |
| `TabConfig.Inquisitor` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.ItemRotation` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.Items` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.LastClickedTabName` | reads NULL | — | ⛔ Not ported yet | Note A |
| `TabConfig.LavishSettingsConfigName` | reads NULL | — | ⛔ Not ported yet | Note A |
| `TabConfig.Load` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.LoadExecute` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.Loot` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.LootDistribution` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.Mystic` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.Necromancer` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.OgreConsole` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.OnZoneExecute` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.OSA` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.Other` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.Overseer` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.OverseerBuyMissions` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.PackPony` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.Postcast` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.Precast` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.ProfileParts` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.ProfilePartsSettings` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.Ranger` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.Ref` | reads NULL | — | ⛔ Not ported yet | Note A |
| `TabConfig.RelayGroups` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.RelayGroupsExecute` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig:SetBaseSetName` | does nothing | — | ⛔ Not ported yet | Note A |
| `TabConfig:SetLavishSettingsConfigName` | does nothing | — | ⛔ Not ported yet | Note A |
| `TabConfig.Settings` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.Setup` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.SetupInvis` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig:SetupSubObjects` | does nothing | — | ⛔ Not ported yet | Note A |
| `TabConfig.SpawnEvents` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.TabColSetRefs` | reads NULL | — | ⛔ Not ported yet | Note A |
| `TabConfig.TabName_HelpURL` | reads NULL | — | ⛔ Not ported yet | Note A |
| `TabConfig.Tags` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.Tags_AddNew` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.Troubador` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.UnloadExecute` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.VampiricRequiem` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.VampiricRequiemOptions` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |
| `TabConfig.Warlock` | reads NULL | `${ISXOgreEQ2.OgreBot.Value["<control id>"]}` | ➡️ Lives somewhere else | Note A |

## GetInfoOb

**Note A** (8 rows below): arguments swapped - the Classic `*By_` members take (search, mode, ...); Roster's take (mode, search, ...). A rename-only edit compiles and searches for a Class literally named "Fighter".

**Note B** (7 rows below): The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it.

**Note C** (3 rows below): The arguments are different: Classic took `(persistentref DotToCheck)`, the new call takes `[main,back,actorId,field]`. takes a `persistentref` (a LavishScript reference passed by name). Watch the pair order - Classic's `Object_IconIDs` declares BACKDROP FIRST, so `=A B` means main=B, back=A. Reading it left-to-right compiles, runs, and asks about a detriment nobody has.

**Note D** (3 rows below): The new surface returns values instead: `${OgreBotAPI.Roster.SortGroupByID[...]}` / `.GroupIDBy` / `.GroupNameBy` / `.RaidIDBy` / `.RaidNameBy` and the four `*Preferred` forms. Mind the argument order - Roster takes (mode, search, ...), Classic took (search, mode, ...).

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `GetInfoOb.ActorToID` | reads NULL | `OgreBotAPI.Actors.MobID` `[name]` | ✏️ Renamed | Not taken any more: `IsNPC`. |
| `GetInfoOb.Alias` | reads NULL | `OgreBotAPI.ForWho.Alias` `[name]` | ➡️ Moved |  |
| `GetInfoOb.Archetype` | reads NULL | `OgreBotAPI.Roster.ArchetypeOf` `[class]` | ✏️ Renamed | Not taken any more: `IncludeMe`. |
| `GetInfoOb.AscensionVitalityRemaining` | reads NULL | — | ⛔ Not ported yet |  |
| `GetInfoOb:CancelEffect` | does nothing | `OgreBotAPI.Cures:CancelDetrimental` `[fw,mainId,backdropId]` | ⚠️ Arguments changed | Note B |
| `GetInfoOb:CancelEffect_ref` | does nothing | `OgreBotAPI.Cures:CancelDetrimental` `[fw,mainId,backdropId]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. takes a `persistentref` (a LavishScript reference passed by name). |
| `GetInfoOb.CheckMobDetriment` | reads NULL | `OgreBotAPI.Cures.Detrimental` `[main,back,actorId,field]` | ⚠️ Arguments changed | The arguments are different: Classic took `(string _MobName, persistentref _IDs)`, the new call takes `[main,back,actorId,field]`. the new reader is keyed on the DETRIMENT ICON PAIR, not on a name: `${OgreBotAPI.Cures.Detrimental[<main>,<back>,<actorId>,"<field>"]}` (field defaults to "exists"; "CurrentIncrements" and "Duration" are the other common ones). Watch the pair order - Classic's `Object_IconIDs` declares BACKDROP FIRST, so `=A B` means main=B, back=A. Reading it left-to-right compiles, runs, and asks about a detriment nobody has. |
| `GetInfoOb.CheckMobDetriment_Increment` | reads NULL | `OgreBotAPI.Cures.Detrimental` `[main,back,actorId,field]` | ⚠️ Arguments changed | The arguments are different: Classic took `(string _MobName, persistentref _IDs)`, the new call takes `[main,back,actorId,field]`. pass `"CurrentIncrements"`. the new reader is keyed on the DETRIMENT ICON PAIR, not on a name: `${OgreBotAPI.Cures.Detrimental[<main>,<back>,<actorId>,"<field>"]}` (field defaults to "exists"; "CurrentIncrements" and "Duration" are the other common ones). Watch the pair order - Classic's `Object_IconIDs` declares BACKDROP FIRST, so `=A B` means main=B, back=A. Reading it left-to-right compiles, runs, and asks about a detriment nobody has. |
| `GetInfoOb.Class` | reads NULL | `OgreBotAPI.Roster.NearestOfClass` | ✏️ Renamed | Faithful: scope auto-detects (raid if in one, else group); a match is the member's SUBCLASS or its class TIER, so `"warrior"` finds a berserker; self answers first with no distance test; distance must be &gt; 0 (Classic's guard against members reading 0 while zoning) and &lt;= range. Deliberate superset: ARCHETYPE also matches, so `"fighter"` finds any of them - Classic's hand-written switch only knew subclass\|tier. |
| `GetInfoOb.Clean` | reads NULL | `OgreBotAPI.Util.Clean` `[s]` | ➡️ Moved |  |
| `GetInfoOb.CleanNameWithSpaces` | reads NULL | `OgreBotAPI.Util.Clean` `[s]` | ✏️ Renamed |  |
| `GetInfoOb.CleanNameWithUnderscores` | reads NULL | — | ⛔ Not ported yet | the underscore variant of CleanName. `Util.Clean` is the ported one; the underscore form has no twin. |
| `GetInfoOb.CommandForMe` | reads NULL | `OgreBotAPI.ForWho.Me` | ✏️ Renamed |  |
| `GetInfoOb.CommandForMe_Check` | reads NULL | `OgreBotAPI.ForWho.Me` | ✏️ Renamed |  |
| `GetInfoOb.CommandForMe_Eval_Me` | reads NULL | `OgreBotAPI.ForWho.Me` | ✏️ Renamed |  |
| `GetInfoOb.CountGroupBy_` | reads NULL | `OgreBotAPI.Roster.CountGroupBy` | ✏️ Renamed | Note A |
| `GetInfoOb.CountRaidBy_` | reads NULL | `OgreBotAPI.Roster.CountRaidBy` | ✏️ Renamed | Note A |
| `GetInfoOb.CurableDisable` | reads NULL | — | ⛔ Not ported yet | takes a `persistentref` (a LavishScript reference passed by name). |
| `GetInfoOb.CureCurseNotRecentlyCast` | reads NULL | — | ⛔ Not ported yet | Classic's per-target cure throttle, read out of its own cure queue. The new engine owns request de-duplication internally (see the Obj_Cure* objects), so there is no throttle to consult. |
| `GetInfoOb.CurrentIncrements` | reads NULL | `OgreBotAPI.Cures.Detrimental` `[main,back,actorId,field]` | ⚠️ Arguments changed | The arguments are different: Classic took `(string DotToCheck)`, the new call takes `[main,back,actorId,field]`. Classic looked the detriment up by NAME; the new reader is keyed on the DETRIMENT ICON PAIR, not on a name: `${OgreBotAPI.Cures.Detrimental[<main>,<back>,<actorId>,"<field>"]}` (field defaults to "exists"; "CurrentIncrements" and "Duration" are the other common ones). Watch the pair order - Classic's `Object_IconIDs` declares BACKDROP FIRST, so `=A B` means main=B, back=A. Reading it left-to-right compiles, runs, and asks about a detriment nobody has. |
| `GetInfoOb.CurrentIncrements_ID` | reads NULL | `OgreBotAPI.Cures.Detrimental` `[main,back,actorId,field]` | ⚠️ Arguments changed | The arguments are different: Classic took `(int _BackDropID=0, int _MainID=0)`, the new call takes `[main,back,actorId,field]`. pass `"CurrentIncrements"` as the field. the new reader is keyed on the DETRIMENT ICON PAIR, not on a name: `${OgreBotAPI.Cures.Detrimental[<main>,<back>,<actorId>,"<field>"]}` (field defaults to "exists"; "CurrentIncrements" and "Duration" are the other common ones). Watch the pair order - Classic's `Object_IconIDs` declares BACKDROP FIRST, so `=A B` means main=B, back=A. Reading it left-to-right compiles, runs, and asks about a detriment nobody has. |
| `GetInfoOb.CurrentIncrements_ref` | reads NULL | `OgreBotAPI.Cures.Detrimental` `[main,back,actorId,field]` | ⚠️ Arguments changed | Note C |
| `GetInfoOb.CursesInGroup` | reads NULL | `OgreBotAPI.Cures.GroupCurses` | ✏️ Renamed |  |
| `GetInfoOb.DetrimentalInfo` | reads NULL | `OgreBotAPI.Cures.Detrimental` `[main,back,actorId,field]` | ✏️ Renamed |  |
| `GetInfoOb.DetrimentalInfo_ref` | reads NULL | `OgreBotAPI.Cures.Detrimental` `[main,back,actorId,field]` | ⚠️ Arguments changed | The arguments are different: Classic took `(persistentref DotToCheck, int64 _ActorID=${Me.ID}, string _Return="exists")`, the new call takes `[main,back,actorId,field]`. |
| `GetInfoOb.DotDuration` | reads NULL | `OgreBotAPI.Cures.Detrimental` `[main,back,actorId,field]` | ⚠️ Arguments changed | The arguments are different: Classic took `(string DotToCheck)`, the new call takes `[main,back,actorId,field]`. pass `"Duration"` as the field. the new reader is keyed on the DETRIMENT ICON PAIR, not on a name: `${OgreBotAPI.Cures.Detrimental[<main>,<back>,<actorId>,"<field>"]}` (field defaults to "exists"; "CurrentIncrements" and "Duration" are the other common ones). Watch the pair order - Classic's `Object_IconIDs` declares BACKDROP FIRST, so `=A B` means main=B, back=A. Reading it left-to-right compiles, runs, and asks about a detriment nobody has. |
| `GetInfoOb.DotDuration_ref` | reads NULL | `OgreBotAPI.Cures.Detrimental` `[main,back,actorId,field]` | ⚠️ Arguments changed | Note C |
| `GetInfoOb.Dotted` | reads NULL | `OgreBotAPI.Cures.Detrimental` `[main,back,actorId,field]` | ⚠️ Arguments changed | The arguments are different: Classic took `(string DotToCheck)`, the new call takes `[main,back,actorId,field]`. the default field "exists" is this question. the new reader is keyed on the DETRIMENT ICON PAIR, not on a name: `${OgreBotAPI.Cures.Detrimental[<main>,<back>,<actorId>,"<field>"]}` (field defaults to "exists"; "CurrentIncrements" and "Duration" are the other common ones). Watch the pair order - Classic's `Object_IconIDs` declares BACKDROP FIRST, so `=A B` means main=B, back=A. Reading it left-to-right compiles, runs, and asks about a detriment nobody has. |
| `GetInfoOb.Dotted_ref` | reads NULL | `OgreBotAPI.Cures.Detrimental` `[main,back,actorId,field]` | ⚠️ Arguments changed | Note C |
| `GetInfoOb.DottedDescription_ref` | reads NULL | `OgreBotAPI.Cures.DetrimentalText` `[main,back,actorId,field]` | ⚠️ Arguments changed | The arguments are different: Classic took `(persistentref DotToCheck)`, the new call takes `[main,back,actorId,field]`. takes a `persistentref` (a LavishScript reference passed by name). The id-keyed `.DetrimentalText` is the working form. |
| `GetInfoOb.DottedExamine_ref` | reads NULL | — | ⛔ Not ported yet | opened the EXAMINE window for a detriment, which is a window action rather than a detriment read - `Cures.Detrimental` / `.DetrimentalText` answer about the detriment, not about examining it. No twin, and it took a persistentref besides. |
| `GetInfoOb.DottedName_ref` | reads NULL | `OgreBotAPI.Cures.DetrimentalText` `[main,back,actorId,field]` | ⚠️ Arguments changed | The arguments are different: Classic took `(persistentref DotToCheck)`, the new call takes `[main,back,actorId,field]`. takes a `persistentref` (a LavishScript reference passed by name). The id-keyed `.DetrimentalText` is the working form. |
| `GetInfoOb.EquipOrInven` | reads NULL | — | ⛔ Not ported yet | answers whether an item is equipped or in a bag. The Inventory surface exposes slot and adornment reads but no equipped-vs-bagged lookup. |
| `GetInfoOb.Evaluate_Num` | reads NULL | — | ⛔ Not ported yet | a generic numeric comparator (v1 &lt;op&gt; v2). Nothing to port - write the comparison inline; `Util.Between` / `.BetweenFloat` cover the range case. |
| `GetInfoOb.FlaggedToon` | reads NULL | `OgreBotAPI.Roster.Flagged` `[n=1]` | ✏️ Renamed |  |
| `GetInfoOb:FlagToon` | does nothing | `OgreBotAPI.Roster:Flag` `[fw,n=1]` | ⚠️ Arguments changed | Note B |
| `GetInfoOb:Get_GroupIDs` | does nothing | `OgreBotAPI.Roster.SortGroupByID` | ✏️ Renamed | Classic handed back a collection to iterate; the new surface is INDEXED - ask for rank n rather than filling a container. `ExcludeToon` has no argument twin: filter it caller-side. |
| `GetInfoOb:Get_GroupNames` | does nothing | — | ⛔ Not ported yet | Note D |
| `GetInfoOb:Get_RaidIDs` | does nothing | — | ⛔ Not ported yet | Note D |
| `GetInfoOb:Get_RaidNames` | does nothing | — | ⛔ Not ported yet | Note D |
| `GetInfoOb.GetAscensionScrolls` | reads NULL | — | ⛔ Not ported yet |  |
| `GetInfoOb.GetBaseClass` | reads NULL | `OgreBotAPI.Roster.BaseClassOf` `[class]` | ✏️ Renamed |  |
| `GetInfoOb.GetClass` | reads NULL | `OgreBotAPI.Roster.BaseClassOf` `[class]` | ✏️ Renamed |  |
| `GetInfoOb.GetGroupIDBy_` | reads NULL | `OgreBotAPI.Roster.GroupIDBy` | ✏️ Renamed | Note A |
| `GetInfoOb.GetGroupInformation` | reads NULL | `OgreBotAPI.Roster.GroupNameBy` | ✏️ Renamed | Roster takes (mode, search, rank); Classic took (search, member). `.GroupIDBy` is the id twin. |
| `GetInfoOb.GetGroupNameBy_` | reads NULL | `OgreBotAPI.Roster.GroupNameBy` | ✏️ Renamed | Note A |
| `GetInfoOb.GetMobID` | reads NULL | `OgreBotAPI.Actors.MobID` `[name]` | ✏️ Renamed |  |
| `GetInfoOb.GetRaidIDBy_` | reads NULL | `OgreBotAPI.Roster.RaidIDBy` | ✏️ Renamed | Note A |
| `GetInfoOb.GetRaidNameBy_` | reads NULL | `OgreBotAPI.Roster.RaidNameBy` | ✏️ Renamed | Note A |
| `GetInfoOb.GetRole` | reads NULL | `OgreBotAPI.Roster.RoleOf` `[class]` | ✏️ Renamed |  |
| `GetInfoOb.GroupInZone` | reads NULL | `OgreBotAPI.Roster.InZone` `[within=0]` | ✏️ Renamed |  |
| `GetInfoOb.InAInstance` | reads NULL | `OgreBotAPI.Zone.InInstance` | ✏️ Renamed |  |
| `GetInfoOb.InGame` | reads NULL | — | ⛔ Not ported yet | Classic's 'is the character in world' guard. The new bot gates the whole adapter on `${ISXEQ2.IsReady}` and exposes character state as `Session.AtCharacterSelect`; there is no InGame member, so ask the game. |
| `GetInfoOb.InGuildHallZone` | reads NULL | `OgreBotAPI.Zone.InGuildHall` | ✏️ Renamed |  |
| `GetInfoOb.InHouseAccessZone` | reads NULL | `OgreBotAPI.Zone.InHouseAccess` | ✏️ Renamed |  |
| `GetInfoOb.InHouseZone` | reads NULL | `OgreBotAPI.Zone.InHouse` | ✏️ Renamed |  |
| `GetInfoOb.IsAssisting` | reads NULL | `OgreBotAPI.Assist.IsAssisting` | ➡️ Moved |  |
| `GetInfoOb:MarkToon` | does nothing | `OgreBotAPI.Roster:Mark` `[fw]` | ⚠️ Arguments changed | Note B |
| `GetInfoOb.NewCharacterLoaded` | reads NULL | — | ⛔ Not ported yet | Classic polled for a character swap. The new bot's character-load seam is the `EQ2_FinishedZoning` event, not a polled member - so this is an event to subscribe to, not a read to convert. |
| `GetInfoOb:PopulatePCOptionLists` | does nothing | — | ⛔ Not ported yet |  |
| `GetInfoOb:PopulatePCOptionLists_AddToUI` | does nothing | — | ⛔ Not ported yet |  |
| `GetInfoOb.RemoveZoneNumber` | reads NULL | `OgreBotAPI.Util.StripZoneNumber` `[s]` | ✏️ Renamed |  |
| `GetInfoOb.SortGroupByIDBy_` | reads NULL | `OgreBotAPI.Roster.SortGroupByID` | ✏️ Renamed | Note A |
| `GetInfoOb.SortRaidByIDBy_` | reads NULL | `OgreBotAPI.Roster.SortRaidByID` | ✏️ Renamed | Note A |
| `GetInfoOb:SpewFlags` | does nothing | `OgreBotAPI.Roster:SpewFlags` `[fw]` | ⚠️ Arguments changed | Note B |
| `GetInfoOb:ToonFlagged` | does nothing | `OgreBotAPI.Roster.Flagged` `[n=1]` | ✏️ Renamed | Not taken any more: `_Where`. |
| `GetInfoOb.ToonMarked` | reads NULL | `OgreBotAPI.Roster.Marked` | ✏️ Renamed |  |
| `GetInfoOb.Trim` | reads NULL | — | ⛔ Not ported yet | a string trim. `Util` carries the conversions LavishScript lacks but has no Trim; LavishScript's own string members cover it. |
| `GetInfoOb:TroubadorPoWMythCloakProc` | does nothing | — | ⛔ Not ported yet | a class-and-item-specific proc tracker. Fight/class one-offs are not API on the new bot - they belong in an encounter module or a method hatch. |
| `GetInfoOb.TroubadorPoWMythCloakProcOn` | reads NULL | — | ⛔ Not ported yet | state for the Troubador proc tracker - a class one-off, not API. See TroubadorPoWMythCloakProc. |
| `GetInfoOb.TroubadorPowMythCloakProcTimer` | reads NULL | — | ⛔ Not ported yet | state for the Troubador proc tracker - a class one-off, not API. See TroubadorPoWMythCloakProc. |
| `GetInfoOb:UnflagAll` | does nothing | `OgreBotAPI.Roster:UnflagAll` `[fw]` | ⚠️ Arguments changed | Note B |
| `GetInfoOb:UnflagToon` | does nothing | `OgreBotAPI.Roster:Unflag` `[fw,n=1]` | ⚠️ Arguments changed | Note B |
| `GetInfoOb:UnmarkToon` | does nothing | `OgreBotAPI.Roster:Unmark` `[fw]` | ⚠️ Arguments changed | Note B |
| `GetInfoOb.UplinkName` | reads NULL | `OgreBotAPI.Comms.UplinkName` | ➡️ Moved |  |
| `call GetInfoOb.WaitForCasting` | does nothing | — | ⛔ Not ported yet | a blocking wait on 'am I still casting'. Rule 9 routes casts through the one chokepoint, which owns its own sequencing - the new surface has no wait-for-cast helper. `Abilities.CancelCurrentCast` reads the current cast. |

## ClassInfo

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `ClassInfo.Archetype` | reads NULL | `OgreBotAPI.Roster.ArchetypeOf` `[class]` | ✏️ Renamed | pass `${Me.ID}`. `${ISXOgreEQ2.Class.Archetype}` is the direct read. |
| `ClassInfo.ChangeValue` | reads NULL | `${ISXOgreEQ2.Class:ChangeValue[<member>,<value>]}` | ➡️ Lives somewhere else |  |
| `ClassInfo:Clear` | does nothing | — | ⛔ Not ported yet | internal reset of Classic's own class cache; the new bot has no such cache to clear |
| `ClassInfo.GroupWaterBreathingAbility` | reads NULL | `${ISXOgreEQ2.Class.WaterBreathingAbility}` | ➡️ Lives somewhere else |  |
| `ClassInfo.HasEpic2` | reads NULL | `${ISXOgreEQ2.Class.HasEpic2}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsAnimalist` | reads NULL | `${ISXOgreEQ2.Class.Is["animalist"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsAssassin` | reads NULL | `${ISXOgreEQ2.Class.Is["assassin"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsBard` | reads NULL | `${ISXOgreEQ2.Class.Is["bard"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsBeastlord` | reads NULL | `${ISXOgreEQ2.Class.Is["beastlord"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsBerserker` | reads NULL | `${ISXOgreEQ2.Class.Is["berserker"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsBrawler` | reads NULL | `${ISXOgreEQ2.Class.Is["brawler"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsBrigand` | reads NULL | `${ISXOgreEQ2.Class.Is["brigand"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsBruiser` | reads NULL | `${ISXOgreEQ2.Class.Is["bruiser"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsChanneler` | reads NULL | `${ISXOgreEQ2.Class.Is["channeler"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsCleric` | reads NULL | `${ISXOgreEQ2.Class.Is["cleric"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsCoercer` | reads NULL | `${ISXOgreEQ2.Class.Is["coercer"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsConjuror` | reads NULL | `${ISXOgreEQ2.Class.Is["conjuror"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsCrusader` | reads NULL | `${ISXOgreEQ2.Class.Is["crusader"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsDefiler` | reads NULL | `${ISXOgreEQ2.Class.Is["defiler"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsDirge` | reads NULL | `${ISXOgreEQ2.Class.Is["dirge"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsDruid` | reads NULL | `${ISXOgreEQ2.Class.Is["druid"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsElementalist` | reads NULL | `${ISXOgreEQ2.Class.Is["elementalist"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsEnchanter` | reads NULL | `${ISXOgreEQ2.Class.Is["enchanter"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsEtherealist` | reads NULL | `${ISXOgreEQ2.Class.Is["etherealist"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsFighter` | reads NULL | `${ISXOgreEQ2.Class.Is["fighter"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsFury` | reads NULL | `${ISXOgreEQ2.Class.Is["fury"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsGeomancer` | reads NULL | `${ISXOgreEQ2.Class.Is["geomancer"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsGuardian` | reads NULL | `${ISXOgreEQ2.Class.Is["guardian"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsIllusionist` | reads NULL | `${ISXOgreEQ2.Class.Is["illusionist"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsInquisitor` | reads NULL | `${ISXOgreEQ2.Class.Is["inquisitor"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsMage` | reads NULL | `${ISXOgreEQ2.Class.Is["mage"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsMonk` | reads NULL | `${ISXOgreEQ2.Class.Is["monk"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsMystic` | reads NULL | `${ISXOgreEQ2.Class.Is["mystic"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsNecromancer` | reads NULL | `${ISXOgreEQ2.Class.Is["necromancer"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsPaladin` | reads NULL | `${ISXOgreEQ2.Class.Is["paladin"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsPredator` | reads NULL | `${ISXOgreEQ2.Class.Is["predator"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsPriest` | reads NULL | `${ISXOgreEQ2.Class.Is["priest"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsRanger` | reads NULL | `${ISXOgreEQ2.Class.Is["ranger"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsRogue` | reads NULL | `${ISXOgreEQ2.Class.Is["rogue"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsScout` | reads NULL | `${ISXOgreEQ2.Class.Is["scout"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsShadowknight` | reads NULL | `${ISXOgreEQ2.Class.Is["shadowknight"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsShaman` | reads NULL | `${ISXOgreEQ2.Class.Is["shaman"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsShaper` | reads NULL | `${ISXOgreEQ2.Class.Is["shaper"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsSorcerer` | reads NULL | `${ISXOgreEQ2.Class.Is["sorcerer"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsSummoner` | reads NULL | `${ISXOgreEQ2.Class.Is["summoner"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsSwashbuckler` | reads NULL | `${ISXOgreEQ2.Class.Is["swashbuckler"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsTemplar` | reads NULL | `${ISXOgreEQ2.Class.Is["templar"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsThaumaturgist` | reads NULL | `${ISXOgreEQ2.Class.Is["thaumaturgist"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsTroubador` | reads NULL | `${ISXOgreEQ2.Class.Is["troubador"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsWarden` | reads NULL | `${ISXOgreEQ2.Class.Is["warden"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsWarlock` | reads NULL | `${ISXOgreEQ2.Class.Is["warlock"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsWarrior` | reads NULL | `${ISXOgreEQ2.Class.Is["warrior"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.IsWizard` | reads NULL | `${ISXOgreEQ2.Class.Is["wizard"]}` | ➡️ Lives somewhere else |  |
| `ClassInfo.Name` | reads NULL | `${ISXOgreEQ2.Class.Subclass}` | ➡️ Lives somewhere else |  |
| `ClassInfo.OnBGServer` | reads NULL | `${ISXOgreEQ2.Class.OnBGServer}` | ➡️ Lives somewhere else |  |
| `ClassInfo.OnKaladimServer` | reads NULL | `${ISXOgreEQ2.Class.OnKaladimServer}` | ➡️ Lives somewhere else |  |
| `ClassInfo.OnTLEServer` | reads NULL | `${ISXOgreEQ2.Class.OnTLEServer}` | ➡️ Lives somewhere else |  |
| `ClassInfo.OnVarsoonServer` | reads NULL | `${ISXOgreEQ2.Class.OnVarsoonServer}` | ➡️ Lives somewhere else |  |
| `ClassInfo.RangerEpic2AbilityID` | reads NULL | — | ⛔ Not ported yet | a hard-coded constant in Classic's class table, not an API read |
| `ClassInfo:Update` | does nothing | `${ISXOgreEQ2.Class:Update}` | ➡️ Lives somewhere else |  |
| `ClassInfo:UpdateAscensionClass` | does nothing | `${ISXOgreEQ2.Class.AscensionClass}` | ➡️ Lives somewhere else |  |
| `ClassInfo:UpdateServer` | does nothing | `${ISXOgreEQ2.Class:UpdateServer}` | ➡️ Lives somewhere else |  |

## Classic framework

**Note A** (4 rows below): Delete the line - it is a typo that never worked.<br>A typo - the name never existed in Classic, so the line never did anything. Delete it.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `ChangeCastStackListBoxItem` | not defined - the new bot does not load Classic's framework, so the name does not exist | `OgreBotAPI.CastStack:SetEntry` | ⚠️ Arguments changed | Call OgreBotAPI.CastStack:SetEntry[&lt;forwho&gt;,"&lt;ability&gt;",TRUE\|FALSE\|toggle] (the for-who is new and comes first; the silent flag is gone). In fight files use `castStack` `op` "set".<br>OgreBot's worker that turned one cast-stack entry on, off or toggled (with special keywords such as Ascension or IsStun), optionally silently; raid modules running inside OgreBot called it directly. |
| `ChangeCastStackListBoxItemByTag` | not defined - the new bot does not load Classic's framework, so the name does not exist | `OgreBotAPI.CastStack:SetEntryByTag` | ⚠️ Arguments changed | Call OgreBotAPI.CastStack:SetEntryByTag[&lt;forwho&gt;,"&lt;tag&gt;",TRUE\|FALSE\|toggle]; in fight files use `castStack` with `match` "tag".<br>OgreBot's worker that turned on, off or toggled every cast-stack entry carrying a tag (exact or partial match). |
| `Items` | not defined - the new bot does not load Classic's framework, so the name does not exist | — | ⛔ Not ported yet | Not ported - there is no replacement yet. Nothing in content used it; if two toons fire the purse together, take it out of all but one cast stack.<br>OgreBot's internal spacer for Ahrmatal's Ringmail Purse: when one group member used it, the others held theirs for 30 seconds so only one purse fired at a time. |
| `LetsGo` | not defined - the new bot does not load Classic's framework, so the name does not exist | `OgreBotAPI.CampSpot:Release` | ⚠️ Arguments changed | Call OgreBotAPI.CampSpot:Release with `all` as the for-who first; in IC and fight files use `campSpot` `op` "release".<br>OgreBot's worker behind 'let's go': cleared the no-offensive/no-defensive holds, the threat ignore list, the assist overrides, follow pause and no-move, stood up from feign death, cleared every campspot, the HO icon lists and the bow-ability block. |
| `Mentor` | not defined - the new bot does not load Classic's framework, so the name does not exist | `OgreBotAPI.Roster:Mentor` | ⚠️ Arguments changed | Call OgreBotAPI.Roster:Mentor[&lt;forwho&gt;,&lt;name&gt;].<br>OgreBot's worker that mentored a group member when you out-levelled them and neither of you was already mentored. |
| `Obj_CreateInstance_Helpers` | not defined - the new bot does not load Classic's framework, so the name does not exist | — | ⛔ Removed | The loader object of the Instance_Helpers script, used to create an Obj_OgreIH object inside an instance file when the source was not installed. |
| `Obj_CreateOgreUtilities` | not defined - the new bot does not load Classic's framework, so the name does not exist | — | ⛔ Removed | Delete the call: there is no helper object to create; use OgreBotAPI / ISXOgreEQ2 directly.<br>The loader object of the OgreUtilities helper script, used to create an Obj_OgreUtilities object inside another script when the source was not installed. |
| `Obj_Kord.Initialise_IC` | not defined - the new bot does not load Classic's framework, so the name does not exist | — | ⛔ Removed | Note A |
| `Obj_OgreUtilities.OgreMapControllerOb` | not defined - the new bot does not load Classic's framework, so the name does not exist | — | ⛔ Removed | Delete the line. Zone maps load by themselves in the new bot.<br>Nothing real: Obj_OgreUtilities never had this member. The name belongs to a separate global LavishNav map loader; one archived script echoed whether the member existed while debugging. |
| `Obj_OgreUtilities.OgreNavLib` | not defined - the new bot does not load Classic's framework, so the name does not exist | automatic (no call) | ➡️ Lives somewhere else | Delete these lines: the new bot loads the current zone's navmesh by itself. To walk somewhere use OgreBotAPI.Movement:NavTo (or a `path` step with `using` "nav").<br>The OgreNav navigation library object inside Obj_OgreUtilities; content used it only to point it at a zone's map folder and load that map (ChangeLoadingPath, LoadMap, Set_AutoLoadMapOnZone). |
| `Obj_Pushover` | not defined - the new bot does not load Classic's framework, so the name does not exist | `OgreBotAPI.Comms:Pushover` | ➡️ Lives somewhere else | Drop the exists check and call OgreBotAPI.Comms:Pushover directly - it is always there, and it drops the message itself (with one log line) when Pushover is not set up.<br>LostSync's Pushover object - scripts checked ${Obj_Pushover(exists)} before sending. |
| `Obj_Pushover.PushoverSendMsg` | not defined - the new bot does not load Classic's framework, so the name does not exist | `OgreBotAPI.Comms:Pushover` | ⚠️ Arguments changed | Write OgreBotAPI.Comms:Pushover[all,"&lt;message&gt;",-title,"&lt;title&gt;",-priority,&lt;n&gt;]. The sound is accepted but ignored (the log says so). The new bot already pushes tells and SmartLoot assignments by itself.<br>Sent a Pushover notification: PushoverSendMsg "&lt;title&gt;" "&lt;message&gt;" "&lt;sound&gt;" &lt;priority&gt;. |
| `Obj_SpewStats` | not defined - the new bot does not load Classic's framework, so the name does not exist | `OgreBotAPI.Debug.SpewStat` *(does nothing yet)* | ⛔ Exists, does nothing yet | To report a stat to chat use OgreBotAPI.Debug:BroadcastStat (or the console `-SpewStat`). Reading a stat back into a script (OgreBotAPI.Debug.SpewStat) exists but does not work yet, so a script that needs your potency has no working read today.<br>OgreBot's stat reporter: read your stats, currencies, factions, skills and recipe counts from the game windows, either returned to the script (GetSpewStat, e.g. potency) or sent to chat. |
| `Object_Timer` | not defined - the new bot does not load Classic's framework, so the name does not exist | `timer` | 📄 In a data file now | In fight and IC files use the `timer` action and the `timerLeft` / `timerExpired` conditions. In a hand-written script use ISXOgreEQ2.Scheduler: :FireEvent[delayMs,event,...,-key &lt;k&gt;] to fire an event later, .Remaining[&lt;key&gt;] for the time left.<br>A countdown object scripts declared (`variable Object_Timer Timer_X`): set it for some milliseconds/seconds, read TimeLeft / SecondsLeft, and optionally fire a named event when it ran out. |
| `ogre bookcase` | not defined - the new bot does not load Classic's framework, so the name does not exist | — | ⛔ Removed | Delete the line - there is no replacement.<br>Classic's bookcase tool. |
| `ogre craft2int` | not defined - the new bot does not load Classic's framework, so the name does not exist | — | ⛔ Removed | Delete the line. To craft, use `ogre craft`.<br>Classic's internal craft2 loader. |
| `ogre ica` | not defined - the new bot does not load Classic's framework, so the name does not exist | — | ⛔ Removed | Delete the line - there is no replacement.<br>Classic's instance-controller assistant. |
| `ogre instance_helpers` | not defined - the new bot does not load Classic's framework, so the name does not exist | — | ⛔ Removed | Delete the line - the instance controller runs instance files itself.<br>Started Classic's instance-helper script. |
| `ogre meshuiint` | not defined - the new bot does not load Classic's framework, so the name does not exist | — | ⛔ Not ported yet | Not ported yet - a new tool covering the mesh UI and travel is planned.<br>Classic's internal mesh UI tool (`int` = internal). |
| `ogre navtest` | not defined - the new bot does not load Classic's framework, so the name does not exist | — | ⛔ Removed | Delete the line - there is no replacement.<br>Classic's navigation test window. |
| `ogre travelint` | not defined - the new bot does not load Classic's framework, so the name does not exist | — | ⛔ Not ported yet | Not ported yet - a new tool covering the mesh UI and travel is planned.<br>Classic's internal travel tool (`int` = internal). |
| `ogre utilities` | not defined - the new bot does not load Classic's framework, so the name does not exist | — | ⛔ Removed | Delete the line - there is no replacement.<br>Classic's utilities window. |
| `Ogre_Instance_Controller_Assister` | not defined - the new bot does not load Classic's framework, so the name does not exist | — | ⛔ Removed | Delete the line - there is no replacement.<br>Classic's instance-controller assistant (the `ogre ica` window). |
| `OgreBackwardKey` | not defined - the new bot does not load Classic's framework, so the name does not exist | — | ⛔ Not ported yet | There is no script-readable key bind in the new bot. Do not hold keys: to step somewhere, move to a location with OgreBotAPI.Movement:ToLoc (or NavTo), or in a fight file use `movement` `op` "navTo" or a `campSpot`.<br>The key your client uses to walk backward (default s), which fight scripts held for a moment to back away. |
| `OgreBotAPI:NotTarget` | not defined - the new bot does not load Classic's framework, so the name does not exist | — | ⛔ Removed | Note A |
| `OgreBotHUDs` | not defined - the new bot does not load Classic's framework, so the name does not exist | `onScreenTimer` | 📄 In a data file now | For the countdown slots use the `onScreenTimer` action in the fight file (`slot` 1-10, `time`, `message`, `minUpdate`; `op` "clear" to remove), or OgreBotAPI.Util:OnScreenTimer from a script. The HUD panels themselves are ISXOgreEQ2.HUDs (Open, :Close, :Set).<br>OgreBot's on-screen overlays: NPC, group, raid and nearest-player HUDs, plus ten raid-module countdown slots (RM.RO[1..10]) that fight scripts filled with a message and a timer. |
| `OgreBotScriptName` | not defined - the new bot does not load Classic's framework, so the name does not exist | `ISXOgreEQ2.OgreBot.IsReady` | ➡️ Lives somewhere else | There is no OgreBot script any more. To ask whether the bot is up, read ${ISXOgreEQ2.OgreBot.IsReady}; to wait while it is paused, read ${OgreBotAPI.Bot.Paused}; call OgreBotAPI methods directly instead of queueing commands into the bot.<br>The file name of the running OgreBot script, so other scripts could check that OgreBot was running (`Script[${OgreBotScriptName}](exists)`) or queue commands into it. |
| `OgreConsole.bUplink` | not defined - the new bot does not load Classic's framework, so the name does not exist | `!${LavishScript.Executable.Right[14].Equal["EverQuest2.exe"]}` | ➡️ Lives somewhere else | Test "not the game" with plain LavishScript: !${LavishScript.Executable.Right[14].Equal["EverQuest2.exe"]} is TRUE outside the game. Do not test for InnerSpace.exe - people rename it (e.g. Steam.exe).<br>TRUE when the script ran outside the game (in the InnerSpace uplink). |
| `OgreConsole:SendToIRC` | not defined - the new bot does not load Classic's framework, so the name does not exist | irc &lt;text&gt; | ➡️ Lives somewhere else | Use the `irc` command: `irc <text>` says the text in the IRC channel (it needs the IRC hub in the uplink, as before).<br>Sent a line of text to the IRC channel. |
| `OgreCrouchKey` | not defined - the new bot does not load Classic's framework, so the name does not exist | `OgreBotAPI.Movement:Crouch` | ➡️ Lives somewhere else | Call OgreBotAPI.Movement:Crouch[&lt;forwho&gt;] (or OgreBotAPI.Movement:Stand to get up from feign death).<br>The key your client uses to crouch (default Z), which scripts pressed to crouch or to stand up. |
| `OgreFlyDownKey` | not defined - the new bot does not load Classic's framework, so the name does not exist | `OgreBotAPI.Movement:FlyDown` | ➡️ Lives somewhere else | Call OgreBotAPI.Movement:FlyDown[&lt;forwho&gt;] to start sinking and OgreBotAPI.Movement:FlyStop[&lt;forwho&gt;] to stop.<br>The key your client uses to fly or swim down (default End), which scripts held and released. |
| `OgreFlyUpKey` | not defined - the new bot does not load Classic's framework, so the name does not exist | `OgreBotAPI.Movement:FlyUp` | ➡️ Lives somewhere else | Call OgreBotAPI.Movement:FlyUp[&lt;forwho&gt;] to start rising and OgreBotAPI.Movement:FlyStop[&lt;forwho&gt;] to stop.<br>The key your client uses to fly or swim up (default Home), which scripts held and released. |
| `OgreForwardKey` | not defined - the new bot does not load Classic's framework, so the name does not exist | — | ⛔ Not ported yet | There is no script-readable key bind in the new bot. Do not hold keys: to step somewhere, move to a location with OgreBotAPI.Movement:ToLoc (or NavTo), or in a fight file use `movement` `op` "navTo" or a `campSpot`.<br>The key your client uses to walk forward (default w), which fight scripts held for a moment to step forward. |
| `OgreIH` | not defined - the new bot does not load Classic's framework, so the name does not exist | — | ⛔ Removed | Note A |
| `OgreJumpKey` | not defined - the new bot does not load Classic's framework, so the name does not exist | `OgreBotAPI.Movement:Jump` | ➡️ Lives somewhere else | Call OgreBotAPI.Movement:Jump[&lt;forwho&gt;]; it presses your jump key from the Key Binds tab. In fight files use `movement` `op` "jump".<br>The key your client uses to jump (default Space), so scripts could `press ${OgreJumpKey}`. |
| `OgreLookDownKey` | not defined - the new bot does not load Classic's framework, so the name does not exist | `OgreBotAPI.Client:SetCameraPitch` | ➡️ Lives somewhere else | Set the camera angle directly: OgreBotAPI.Client:SetCameraPitch[&lt;forwho&gt;,&lt;pitch&gt;] (-75..75, 0 = level); in fight files use `camera` `op` "setPitch".<br>The key your client uses to tilt the camera down (default Page Down); scripts held it to look at the ground before clicking the middle of the screen. |
| `OgreLookUpKey` | not defined - the new bot does not load Classic's framework, so the name does not exist | `OgreBotAPI.Client:SetCameraPitch` | ➡️ Lives somewhere else | Set the camera angle directly: OgreBotAPI.Client:SetCameraPitch[&lt;forwho&gt;,&lt;pitch&gt;]; in fight files use `camera` `op` "setPitch".<br>The key your client uses to tilt the camera up (default Page Up), which scripts held and released. |
| `OgreMapControllerOb` | not defined - the new bot does not load Classic's framework, so the name does not exist | — | ⛔ Removed | Delete the line - the new bot loads each zone's navmesh by itself when you zone in.<br>Classic's nav-map controller (`OgreMapControllerOb:LoadMap` loaded the zone's map). |
| `OgreRelayGroup` | not defined - the new bot does not load Classic's framework, so the name does not exist | `ISXOgreEQ2.Auth.RelayGroup` | ✏️ Renamed | Read ${ISXOgreEQ2.Auth.RelayGroup}. To send a command to your sessions, prefer the console's `oc !c` / `oc !ci` with a for-who instead of a raw relay.<br>The name of the relay group every OgreBot session joins (default ogre_everquest2), used as `relay ${OgreRelayGroup} ...` to reach all your sessions. |
| `OgreUtilities` | not defined - the new bot does not load Classic's framework, so the name does not exist | — | ⛔ Removed | Note A |
| `OgreZoomOutKey` | not defined - the new bot does not load Classic's framework, so the name does not exist | — | ⛔ Not ported yet | Not ported - there is no camera-zoom verb yet; the key is set in the Key Binds tab but scripts cannot read it.<br>The key your client uses to zoom the camera out (default Num -), which one fight script held on every toon. |
| `ReplyDialog` | not defined - the new bot does not load Classic's framework, so the name does not exist | `OgreBotAPI.Windows:Reply` | ⚠️ Arguments changed | Call OgreBotAPI.Windows:Reply[&lt;forwho&gt;,&lt;text or number&gt;]; in IC and fight files use `replyDialog`. (Lines that read ${ReplyDialog...} are ISXEQ2's own window object, not this function, and are unaffected.)<br>OgreBot's worker that chose a numbered reply in an NPC conversation window. |
| `Revive` | not defined - the new bot does not load Classic's framework, so the name does not exist | `OgreBotAPI.Session:Revive` | ⚠️ Arguments changed | Call OgreBotAPI.Session:Revive with the for-who first; in IC files use a `recover` step with `op` "revive".<br>OgreBot's worker that, when dead, picked a respawn row on the death window and clicked Respawn (it already printed that scripts should use OgreBotAPI:Revive instead). |

## ProfileConfig

**Note A** (28 rows below): LavishSettings / profile-file plumbing: set refs, config-file paths, the tab-text lookup tables, the import list. Never script-facing - Classic's own options window drove it.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `ProfileConfig.AllowAbilityConversions` | reads NULL | — | ⛔ Not ported yet | Note A |
| `ProfileConfig.BaseSetName` | reads NULL | — | ⛔ Not ported yet | Note A |
| `ProfileConfig:BaseSetNameList` | does nothing | — | ⛔ Not ported yet | Note A |
| `ProfileConfig.BaseSetRef` | reads NULL | — | ⛔ Not ported yet | Note A |
| `ProfileConfig:ChangeToProfileBox` | does nothing | `${ISXOgreEQ2.OgreBot:Save} / :LoadProfile / :CreateProfile / :DeleteProfile` | ➡️ Lives somewhere else |  |
| `ProfileConfig.CheckCopingOldServerProfile` | reads NULL | — | ⛔ Not ported yet | Note A |
| `ProfileConfig:Clear` | does nothing | — | ⛔ Not ported yet | Note A |
| `ProfileConfig.ConfigFileLocation` | reads NULL | — | ⛔ Not ported yet | Note A |
| `ProfileConfig.CurrentSetRef` | reads NULL | — | ⛔ Not ported yet | Note A |
| `ProfileConfig.DefaultProfileName` | reads NULL | — | ⛔ Not ported yet | Note A |
| `ProfileConfig:DeleteProfile` | does nothing | `${ISXOgreEQ2.OgreBot:Save} / :LoadProfile / :CreateProfile / :DeleteProfile` | ➡️ Lives somewhere else |  |
| `ProfileConfig.Exists_TabTextToValueTable` | reads NULL | — | ⛔ Not ported yet | Note A |
| `ProfileConfig.fp_ImportProfileFileLocation` | reads NULL | — | ⛔ Not ported yet | Note A |
| `ProfileConfig.Get_ProfilePartsActiveForTab` | reads NULL | — | ⛔ Not ported yet | Note A |
| `ProfileConfig.Get_ProfilePartsCustomFile` | reads NULL | — | ⛔ Not ported yet | Note A |
| `ProfileConfig.Get_ProfilePartsCustomFileFromCurrentSettings` | reads NULL | — | ⛔ Not ported yet | Note A |
| `ProfileConfig.Get_ReuseableSS` | reads NULL | — | ⛔ Not ported yet | Note A |
| `ProfileConfig.Get_ReuseableSSPP` | reads NULL | — | ⛔ Not ported yet | Note A |
| `ProfileConfig.Get_TabTextToValueTable` | reads NULL | — | ⛔ Not ported yet | Note A |
| `ProfileConfig:ImportFile` | does nothing | `${ISXOgreEQ2.OgreBot:Save} / :LoadProfile / :CreateProfile / :DeleteProfile` | ➡️ Lives somewhere else |  |
| `ProfileConfig.LavishSettingsConfigName` | reads NULL | — | ⛔ Not ported yet | Note A |
| `ProfileConfig:LoadConfigFile` | does nothing | `${ISXOgreEQ2.OgreBot:Save} / :LoadProfile / :CreateProfile / :DeleteProfile` | ➡️ Lives somewhere else |  |
| `ProfileConfig:LoadDefaultBaseSetName` | does nothing | `${ISXOgreEQ2.OgreBot:Save} / :LoadProfile / :CreateProfile / :DeleteProfile` | ➡️ Lives somewhere else |  |
| `ProfileConfig:LoadDefaultBaseSetNameList` | does nothing | `${ISXOgreEQ2.OgreBot:Save} / :LoadProfile / :CreateProfile / :DeleteProfile` | ➡️ Lives somewhere else |  |
| `ProfileConfig:LoadDefaultProfile` | does nothing | `${ISXOgreEQ2.OgreBot:Save} / :LoadProfile / :CreateProfile / :DeleteProfile` | ➡️ Lives somewhere else |  |
| `ProfileConfig:LoadProfile` | does nothing | `OgreBotAPI.Options:LoadProfile` `[fw, name, tabOnly]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. |
| `ProfileConfig:LoadProfileForWho` | does nothing | `OgreBotAPI.Options:LoadProfile` `[fw, name, tabOnly]` | ⚠️ Arguments changed | The arguments are different: Classic took `(string ForWho, string sProfileName=Use_UI)`, the new call takes `[fw, name, tabOnly]`. |
| `ProfileConfig:LoadProfileParts` | does nothing | `${ISXOgreEQ2.OgreBot:Save} / :LoadProfile / :CreateProfile / :DeleteProfile` | ➡️ Lives somewhere else |  |
| `ProfileConfig.Ref` | reads NULL | — | ⛔ Not ported yet | Note A |
| `ProfileConfig:RefreshImportProfileList` | does nothing | `${ISXOgreEQ2.OgreBot:Save} / :LoadProfile / :CreateProfile / :DeleteProfile` | ➡️ Lives somewhere else |  |
| `ProfileConfig.ReuseableSS` | reads NULL | — | ⛔ Not ported yet | Note A |
| `ProfileConfig.ReuseableSSPP` | reads NULL | — | ⛔ Not ported yet | Note A |
| `ProfileConfig:SaveDefaultBaseSetName` | does nothing | `${ISXOgreEQ2.OgreBot:Save} / :LoadProfile / :CreateProfile / :DeleteProfile` | ➡️ Lives somewhere else |  |
| `ProfileConfig:SaveProfile` | does nothing | `${ISXOgreEQ2.OgreBot:Save} / :LoadProfile / :CreateProfile / :DeleteProfile` | ➡️ Lives somewhere else |  |
| `ProfileConfig:SaveProfileParts` | does nothing | `${ISXOgreEQ2.OgreBot:Save} / :LoadProfile / :CreateProfile / :DeleteProfile` | ➡️ Lives somewhere else |  |
| `ProfileConfig:SaveSingleProfile` | does nothing | `${ISXOgreEQ2.OgreBot:Save} / :LoadProfile / :CreateProfile / :DeleteProfile` | ➡️ Lives somewhere else |  |
| `ProfileConfig:SetBaseSetName` | does nothing | — | ⛔ Not ported yet | Note A |
| `ProfileConfig:SetConfigFileLocation` | does nothing | — | ⛔ Not ported yet | Note A |
| `ProfileConfig:SetCurrentSetRefToBaseSetRef` | does nothing | — | ⛔ Not ported yet | Note A |
| `ProfileConfig:SetLavishSettingsConfigName` | does nothing | — | ⛔ Not ported yet | Note A |
| `ProfileConfig.SingleProfileName` | reads NULL | — | ⛔ Not ported yet | Note A |
| `ProfileConfig.TabManager` | reads NULL | — | ⛔ Not ported yet | Note A |
| `ProfileConfig.TabTextToValueTable` | reads NULL | — | ⛔ Not ported yet | Note A |

## Ob_AutoTarget

**Note A** (12 rows below): the new type returns a whole entry as JSON - `${OgreBotAPI.AutoTarget.Entry[n]}` (1-based) - instead of one member per field. Read the entry and take the field out of the JSON. `.JSON` gives the whole working list at once.

**Note B** (5 rows below): The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it.

**Note C** (4 rows below): UI/listbox plumbing for Classic's own AutoTarget tab. The new panel drives the engine directly, so there is nothing script-facing to port.

**Note D** (3 rows below): Classic indexed by its own entry _ID / UI listbox position; the new member is a 1-based index into the working list

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `Ob_AutoTarget.ActorName` | reads NULL | `OgreBotAPI.AutoTarget.EntryName` `[n]` | ✏️ Renamed | Note D |
| `Ob_AutoTarget.ActorNameOrderedItem` | reads NULL | `OgreBotAPI.AutoTarget.EntryName` `[n]` | ✏️ Renamed | Note D |
| `Ob_AutoTarget:AddActor` | does nothing | `OgreBotAPI.AutoTarget:AddActor` `[fw, name, minHP, checkCollision, aggroOnGroupOnly, maxHP, aggroOnNonFighterOnly, aggroOnNotMe]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. insert a for-who at the front; every other argument keeps its position |
| `Ob_AutoTarget:AddActorFromUI` | does nothing | — | ⛔ Not ported yet | Note C |
| `Ob_AutoTarget:AddAddsThenNamed` | does nothing | — | ⛔ Not ported yet | a Classic list-building convenience that ordered adds before the named. No new-bot equivalent - build the list with :AddActor in the order you want. |
| `Ob_AutoTarget:AddListBoxItem` | does nothing | — | ⛔ Not ported yet | Note C |
| `Ob_AutoTarget:AddNamed` | does nothing | — | ⛔ Not ported yet | as AddAddsThenNamed - a list-building convenience with no new-bot twin |
| `Ob_AutoTarget.AggroOnGroupOnly` | reads NULL | `OgreBotAPI.AutoTarget.Entry` `[n]` | ✏️ Renamed | Note A |
| `Ob_AutoTarget.AggroOnGroupOnlyOrderedItem` | reads NULL | `OgreBotAPI.AutoTarget.Entry` `[n]` | ✏️ Renamed | Note A |
| `Ob_AutoTarget.AggroOnNonFighterOnly` | reads NULL | `OgreBotAPI.AutoTarget.Entry` `[n]` | ✏️ Renamed | Note A |
| `Ob_AutoTarget.AggroOnNonFighterOnlyOrderedItem` | reads NULL | `OgreBotAPI.AutoTarget.Entry` `[n]` | ✏️ Renamed | Note A |
| `Ob_AutoTarget.AggroOnNotMe` | reads NULL | `OgreBotAPI.AutoTarget.Entry` `[n]` | ✏️ Renamed | Note A |
| `Ob_AutoTarget.AggroOnNotMeOrderedItem` | reads NULL | `OgreBotAPI.AutoTarget.Entry` `[n]` | ✏️ Renamed | Note A |
| `Ob_AutoTarget.CheckCollision` | reads NULL | `OgreBotAPI.AutoTarget.Entry` `[n]` | ✏️ Renamed | Note A |
| `Ob_AutoTarget.CheckCollisionOrderedItem` | reads NULL | `OgreBotAPI.AutoTarget.Entry` `[n]` | ✏️ Renamed | Note A |
| `Ob_AutoTarget:Clear` | does nothing | `OgreBotAPI.AutoTarget:Clear` `[fw]` | ⚠️ Arguments changed | Note B |
| `Ob_AutoTarget:ClearSavedLists` | does nothing | — | ⛔ Not ported yet | bulk on-disk catalogue management. :DeleteSaved removes ONE saved list; there is no delete-everything verb. |
| `Ob_AutoTarget:DeleteList` | does nothing | `OgreBotAPI.AutoTarget:DeleteSaved` `[fw, name]` | ⚠️ Arguments changed | Note B |
| `Ob_AutoTarget.Enable_Status` | reads NULL | — | ⛔ Not ported yet | an internal Object_Enable_Status sub-object, not script-facing. The master switch is .Enabled / :SetEnabled and the keyed pause is .Suppressed / :Suppress / :Release. |
| `Ob_AutoTarget.HasActor` | reads NULL | `OgreBotAPI.AutoTarget.HasActor` `[name]` | ➡️ Moved |  |
| `Ob_AutoTarget.Items` | reads NULL | `OgreBotAPI.AutoTarget.Count` | ✏️ Renamed |  |
| `Ob_AutoTarget:LoadListFromSaveList` | does nothing | `OgreBotAPI.AutoTarget:LoadSaved` `[fw, name]` | ⚠️ Arguments changed | Note B |
| `Ob_AutoTarget:LoadListFromSaveListForWho` | does nothing | `OgreBotAPI.AutoTarget:LoadSaved` `[fw, name]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it.<br>Not taken any more: `_CommandForMe`. |
| `Ob_AutoTarget:LoadSavedLists` | does nothing | — | ⛔ Not ported yet | Classic pre-loaded the saved-list catalogue into memory. The new engine reads the catalogue on demand (.SavedCount / .SavedName / :LoadSaved), so there is nothing to pre-load. |
| `Ob_AutoTarget:LoadZoneFileIntoMemory` | does nothing | — | ⛔ Not ported yet | as LoadSavedLists - the per-zone file is read on demand |
| `Ob_AutoTarget.MaxHPToTarget` | reads NULL | `OgreBotAPI.AutoTarget.Entry` `[n]` | ✏️ Renamed | Note A |
| `Ob_AutoTarget.MaxHPToTargetOrderedItem` | reads NULL | `OgreBotAPI.AutoTarget.Entry` `[n]` | ✏️ Renamed | Note A |
| `Ob_AutoTarget.MinHPToTarget` | reads NULL | `OgreBotAPI.AutoTarget.Entry` `[n]` | ✏️ Renamed | Note A |
| `Ob_AutoTarget.MinHPToTargetOrderedItem` | reads NULL | `OgreBotAPI.AutoTarget.Entry` `[n]` | ✏️ Renamed | Note A |
| `Ob_AutoTarget.Ob_AutoTargetList` | reads NULL | `OgreBotAPI.AutoTarget.JSON` | ✏️ Renamed |  |
| `Ob_AutoTarget.OrderedItem` | reads NULL | `OgreBotAPI.AutoTarget.EntryName` `[n]` | ✏️ Renamed | Note D |
| `Ob_AutoTarget:PopulateUI` | does nothing | — | ⛔ Not ported yet | Note C |
| `Ob_AutoTarget:RemoveActor` | does nothing | `OgreBotAPI.AutoTarget:RemoveActor` `[fw, name]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. removes EVERY match, case-insensitive |
| `Ob_AutoTarget:RemoveFromUI` | does nothing | — | ⛔ Not ported yet | Note C |
| `Ob_AutoTarget:Reset` | does nothing | `OgreBotAPI.AutoTarget:Clear` `[fw]` | ⚠️ Arguments changed | Note B |
| `Ob_AutoTarget:SaveList` | does nothing | `OgreBotAPI.AutoTarget:Save` `[fw, name]` | ⚠️ Arguments changed | Note B |
| `Ob_AutoTarget.set_OgreAutoTarget` | reads NULL | — | ⛔ Not ported yet | a LavishSettings settingsetref - Classic's on-disk store handle. Internal; the new engine owns its own persistence. |
| `Ob_AutoTarget:Spew` | does nothing | — | ⛔ Not ported yet | a METHOD that printed the working list to console. The new surface has no spew verb; read `.JSON` (or walk `.Entry[n]`) and print it yourself. A read, not a rename. |

## Obj_Collection

**Note A** (32 rows below): Classic's collection-JOURNAL scraper (open the journal, walk entries, click Location/Missing). There is no new-bot equivalent. `${ISXOgreEQ2.Collection}` exists but is a different thing - the `ogre cm` collection-manager DRIVER (`.Running` / `.Status` / `:Run` / `:Stop`) - and it is NOT reachable from `OgreBotAPI`. REMOVED: "We only need 2 things" - `ogre cm` (the depot: only usable pieces, pull them out and add them) and `ogre cm 1` / `-inventory` (add the shinies in your bags), both in ${ISXOgreEQ2.Collection}; "The other collection stuff is stuff we do not need at this time." The journal scraper, shiny data files, no-trade list and report window are not needed.

**Note B** (3 rows below): Not needed in the new bot. To add collection pieces, use `ogre cm` (from the depot) or `ogre cm 1` (the shinies in your bags).

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `Obj_Collection.bDisplayResults` | reads NULL | — | ⛔ Removed | Note A |
| `Obj_Collection.bReportNoTradeIndex` | reads NULL | — | ⛔ Removed | Note A |
| `Obj_Collection.Category` | reads NULL | — | ⛔ Removed | Note A |
| `Obj_Collection.Category2` | reads NULL | — | ⛔ Removed | Note A |
| `call Obj_Collection.CloseJournal` | does nothing | — | ⛔ Removed | Note A |
| `Obj_Collection:CloseUI` | does nothing | — | ⛔ Removed | Note A |
| `Obj_Collection.CountDown` | reads NULL | — | ⛔ Removed | Note A |
| `Obj_Collection.Debug` | reads NULL | — | ⛔ Removed | Note A |
| `Obj_Collection:Get_Location_Click` | does nothing | — | ⛔ Removed | Note A |
| `Obj_Collection:Get_Missing_Click` | does nothing | — | ⛔ Removed | Note A |
| `Obj_Collection.Get_Scroll_Amount` | reads NULL | — | ⛔ Removed | Note A |
| `call Obj_Collection.Get_Total` | does nothing | — | ⛔ Removed | Note A |
| `Obj_Collection.Lavish_CharData` | reads NULL | — | ⛔ Removed | Note A |
| `call Obj_Collection.Load_Shiny_Data` | does nothing | — | ⛔ Removed | Note A |
| `Obj_Collection.NoTradeIndex` | reads NULL | — | ⛔ Removed | Note A |
| `Obj_Collection.Obj_Pork_LavishSetting` | reads NULL | — | ⛔ Removed | Note A |
| `call Obj_Collection.OpenJournal` | does nothing | — | ⛔ Removed | Note B |
| `call Obj_Collection.ParseJournal` | does nothing | — | ⛔ Removed | Note B |
| `call Obj_Collection.ProcessNoTrade_Collection` | does nothing | — | ⛔ Removed | Note A |
| `call Obj_Collection.ProcessNoTradeIndex` | does nothing | — | ⛔ Removed | Note A |
| `Obj_Collection.ref_Index` | reads NULL | — | ⛔ Removed | Note A |
| `call Obj_Collection.Remove_Completed` | does nothing | — | ⛔ Removed | Note A |
| `call Obj_Collection.Scan_Journal_Complete` | does nothing | — | ⛔ Removed | Note B |
| `call Obj_Collection.Scan_Journal_Got` | does nothing | — | ⛔ Removed | Note A |
| `call Obj_Collection.Scroll_Down` | does nothing | — | ⛔ Removed | Note A |
| `call Obj_Collection.SelectJournalTab` | does nothing | — | ⛔ Removed | Note A |
| `Obj_Collection:Set_Shiny_Collection` | does nothing | — | ⛔ Removed | Note A |
| `call Obj_Collection.SetCollectionTabOptions` | does nothing | — | ⛔ Removed | Note A |
| `call Obj_Collection.SetInternalOptions` | does nothing | — | ⛔ Removed | Note A |
| `Obj_Collection.TotalCollectionAmount` | reads NULL | — | ⛔ Removed | Note A |
| `Obj_Collection.TotalItemAmount` | reads NULL | — | ⛔ Removed | Note A |
| `Obj_Collection.UICategory` | reads NULL | — | ⛔ Removed | Note A |
| `Obj_Collection.UIIcon` | reads NULL | — | ⛔ Removed | Note A |
| `Obj_Collection.UIName` | reads NULL | — | ⛔ Removed | Note A |
| `Obj_Collection.UIStatus` | reads NULL | — | ⛔ Removed | Note A |

## SpellOb

**Note A** (11 rows below): the ability export does not carry this field (it has 46; this is not one of them), so there is nothing to read it from. `${OgreBotAPI.Abilities.InfoRaw[<nameOrId>]}` dumps the whole record if you want to confirm what IS there.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `SpellOb.AbilityExists` | reads NULL | `OgreBotAPI.Abilities.ID` | ✏️ Renamed | resolve by id, not by name (Rule 10) |
| `SpellOb.AbilityName` | reads NULL | `OgreBotAPI.Abilities.ShortName` | ✏️ Renamed | the catalog answers by id; Rule 10 forbids resolving an ability by NAME without per-site approval |
| `SpellOb.AllowRaid` | reads NULL | `OgreBotAPI.Abilities.Info` | ✏️ Renamed | pass `"AllowRaid"` as the field: `${OgreBotAPI.Abilities.Info[<nameOrId>,"AllowRaid"]}` |
| `SpellOb.BLAdvantage` | reads NULL | — | ⛔ Not ported yet | Note A |
| `SpellOb.BLPrimal` | reads NULL | — | ⛔ Not ported yet | Note A |
| `SpellOb.BLPrimalMinSavLevel` | reads NULL | — | ⛔ Not ported yet | Note A |
| `SpellOb.CastingTime` | reads NULL | `OgreBotAPI.Abilities.Info` | ✏️ Renamed | pass `"CastingTime"` as the field: `${OgreBotAPI.Abilities.Info[<nameOrId>,"CastingTime"]}` |
| `SpellOb.ConcentrationCost` | reads NULL | `OgreBotAPI.Abilities.Info` | ✏️ Renamed | pass `"ConcentrationCost"` as the field: `${OgreBotAPI.Abilities.Info[<nameOrId>,"ConcentrationCost"]}` |
| `SpellOb.ConvertToInt64` | reads NULL | `OgreBotAPI.Util.ToInt` `[s]` | ✏️ Renamed |  |
| `SpellOb.DamageType` | reads NULL | — | ⛔ Not ported yet | Note A |
| `SpellOb.DamageTypeGroup` | reads NULL | — | ⛔ Not ported yet | Note A |
| `SpellOb.DescRestrictions` | reads NULL | — | ⛔ Not ported yet | Note A |
| `SpellOb.EffectRadius` | reads NULL | `OgreBotAPI.Abilities.Info` | ✏️ Renamed | pass `"EffectRadius"` as the field: `${OgreBotAPI.Abilities.Info[<nameOrId>,"EffectRadius"]}` |
| `SpellOb.FeralAdvantage` | reads NULL | — | ⛔ Not ported yet | Note A |
| `SpellOb.FeralPrimal` | reads NULL | — | ⛔ Not ported yet | Note A |
| `SpellOb.GetAbilityExFullName` | reads NULL | `OgreBotAPI.Abilities.Info` | ✏️ Renamed |  |
| `SpellOb.GetAbilityFullName` | reads NULL | `OgreBotAPI.Abilities.Info` | ✏️ Renamed |  |
| `SpellOb.GetAbilityNameNum` | reads NULL | `OgreBotAPI.Abilities.Info` | ✏️ Renamed |  |
| `SpellOb.GetAbilityShortName` | reads NULL | `OgreBotAPI.Abilities.ShortName` | ✏️ Renamed |  |
| `SpellOb.ID` | reads NULL | `OgreBotAPI.Abilities.Info` | ✏️ Renamed | pass `"ID"` as the field: `${OgreBotAPI.Abilities.Info[<nameOrId>,"ID"]}` |
| `SpellOb.IsAStun` | reads NULL | — | ⛔ Not ported yet | Note A |
| `SpellOb.MaxRange` | reads NULL | `OgreBotAPI.Abilities.Info` | ✏️ Renamed | pass `"MaxRange"` as the field: `${OgreBotAPI.Abilities.Info[<nameOrId>,"MaxRange"]}` |
| `SpellOb.MinRange` | reads NULL | `OgreBotAPI.Abilities.Info` | ✏️ Renamed | pass `"MinRange"` as the field: `${OgreBotAPI.Abilities.Info[<nameOrId>,"MinRange"]}` |
| `SpellOb.Name` | reads NULL | `OgreBotAPI.Abilities.Info` | ✏️ Renamed | pass `"Name"` as the field: `${OgreBotAPI.Abilities.Info[<nameOrId>,"Name"]}` |
| `SpellOb.PowerCost` | reads NULL | `OgreBotAPI.Abilities.Info` | ✏️ Renamed | pass `"PowerCost"` as the field: `${OgreBotAPI.Abilities.Info[<nameOrId>,"PowerCost"]}` |
| `SpellOb.RecastTime` | reads NULL | `OgreBotAPI.Abilities.Info` | ✏️ Renamed | pass `"RecastTime"` as the field: `${OgreBotAPI.Abilities.Info[<nameOrId>,"RecastTime"]}` |
| `SpellOb.RecoveryTime` | reads NULL | `OgreBotAPI.Abilities.Info` | ✏️ Renamed | pass `"RecoveryTime"` as the field: `${OgreBotAPI.Abilities.Info[<nameOrId>,"RecoveryTime"]}` |
| `SpellOb.SpellBookType` | reads NULL | `OgreBotAPI.Abilities.Info` | ✏️ Renamed | pass `"SpellBookType"` as the field: `${OgreBotAPI.Abilities.Info[<nameOrId>,"SpellBookType"]}` |
| `SpellOb.SpiritualAdvantage` | reads NULL | — | ⛔ Not ported yet | Note A |
| `SpellOb.SpiritualPrimal` | reads NULL | — | ⛔ Not ported yet | Note A |
| `SpellOb.TargetType` | reads NULL | `OgreBotAPI.Abilities.Info` | ✏️ Renamed | pass `"TargetType"` as the field: `${OgreBotAPI.Abilities.Info[<nameOrId>,"TargetType"]}` |
| `SpellOb.VerifyID` | reads NULL | `OgreBotAPI.Abilities.ID` | ✏️ Renamed |  |

## g_RaidOb

**Note A** (19 rows below): a dispatch shim into ONE raid module's method (the body forwards to e.g. `RO_Doomfire_TheMoltenCaldera_Raid.Chancellor:Joust`). Fight-specific behaviour is not API on the new bot: it lives in the encounter module itself, or in a method hatch on `OgreEncounterAPI` when the vocabulary cannot express it.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `g_RaidOb:AotA1` | does nothing | — | ⛔ Not ported yet | Note A |
| `g_RaidOb:DMIR` | does nothing | — | ⛔ Not ported yet | Note A |
| `g_RaidOb:DMPI` | does nothing | — | ⛔ Not ported yet | Note A |
| `g_RaidOb:DMPS` | does nothing | — | ⛔ Not ported yet | Note A |
| `g_RaidOb:ROAOMCG` | does nothing | — | ⛔ Not ported yet | Note A |
| `g_RaidOb:ROASEC` | does nothing | — | ⛔ Not ported yet | Note A |
| `g_RaidOb:ROBSBFC` | does nothing | — | ⛔ Not ported yet | Note A |
| `g_RaidOb:RODFCJ` | does nothing | — | ⛔ Not ported yet | Note A |
| `g_RaidOb:RODTFP` | does nothing | — | ⛔ Not ported yet | Note A |
| `g_RaidOb:ROKoolbhCloudOfVile` | does nothing | — | ⛔ Not ported yet | Note A |
| `g_RaidOb:ROKraletusCureCalled` | does nothing | — | ⛔ Not ported yet | Note A |
| `g_RaidOb:ROOSSCOBEPM` | does nothing | — | ⛔ Not ported yet | Note A |
| `g_RaidOb:ROOSSSAC` | does nothing | — | ⛔ Not ported yet | Note A |
| `g_RaidOb:ROPC` | does nothing | — | ⛔ Not ported yet | 2 consumer sites, both `g_RaidOb:ROPC` in Chaos Descending raids. |
| `g_RaidOb:ROSGPRTCS` | does nothing | — | ⛔ Not ported yet | Note A |
| `g_RaidOb:ROTOVI` | does nothing | — | ⛔ Not ported yet | Note A |
| `g_RaidOb:SGDD` | does nothing | — | ⛔ Not ported yet | Note A |
| `g_RaidOb:SGPRD` | does nothing | — | ⛔ Not ported yet | Note A |
| `g_RaidOb:SGTD` | does nothing | — | ⛔ Not ported yet | Note A |
| `g_RaidOb:SGTFD` | does nothing | — | ⛔ Not ported yet | Note A |

## Obj_CureCurseCalled

**Note A** (3 rows below): Classic's cure-request QUEUE internals. The new bot replaced the whole mechanism: a script asks for a cure through the request verbs (`Cures:Request` / `:RequestCurse` / `:RequestGroup` / `:RequestGroupWatch`) and the engine owns the queue, the de-duplication and the casting. There is no queue object to poke, by design.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `Obj_CureCurseCalled:Add` | does nothing | `OgreBotAPI.Cures:RequestCurse` `[fw,victim]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. `[fw, victim]`; the engine queues and casts, you no longer add to a list<br>Not taken any more: `_HardTarget`. |
| `Obj_CureCurseCalled:AutoAdd` | does nothing | `OgreBotAPI.Cures:RequestCurse` `[fw,victim]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it.<br>Not taken any more: `_HardTarget`. |
| `Obj_CureCurseCalled:AutoAddID` | does nothing | `OgreBotAPI.Cures:RequestCurse` `[fw,victim]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it.<br>Not taken any more: `_HardTarget`. |
| `Obj_CureCurseCalled:AutoRemove` | does nothing | — | ⛔ Not ported yet | Note A |
| `Obj_CureCurseCalled.bEmpty` | reads NULL | — | ⛔ Not ported yet | Note A |
| `Obj_CureCurseCalled.CastCureCurse` | reads NULL | `OgreBotAPI.Cures.CurseCalled` | ✏️ Renamed | Classic's member also ACTED when read (queued the cast, returned TRUE to cancel the current spell); the new bot separates request from serve, so `.CurseCalled` only READS. A bare read asks about ME; pass a victim, or "any" for the fleet-wide read. Classic's `call` WAITED inline - adapter methods never yield, so express the wait in the caller (Sequence/WaitUntil on the curse clearing). |
| `call Obj_CureCurseCalled.CastCureCurseHardTarget` | does nothing | — | ⛔ Not ported yet | Classic cast the cure itself from this object. On the new bot a cure is REQUESTED, not cast directly - `Cures:RequestCurse[fw,victim]` puts it on the fleet channel and the cast goes through the one cast chokepoint (Rule 9). Casting a specific ability yourself is `Abilities:Cast`. |
| `Obj_CureCurseCalled.Get_GroupCursedMember` | reads NULL | `OgreBotAPI.Cures.CursedID` `[-archetype X\|-uncurable\|-uncurableonly\|-GroupOnly]` | ✏️ Renamed | the Classic member took an INDEX (_Num) to walk cursed members. `.CursedID` returns the top-priority one; for the whole set read `.RaidCursedIDs` (JSON) and index that. |
| `Obj_CureCurseCalled.GetID_CursedMember` | reads NULL | `OgreBotAPI.Cures.CursedID` `[-archetype X\|-uncurable\|-uncurableonly\|-GroupOnly]` | ⚠️ Arguments changed | The arguments are different: Classic took ``, the new call takes `[-archetype X\|-uncurable\|-uncurableonly\|-GroupOnly]`. |
| `Obj_CureCurseCalled.GetID_GroupCursedMember` | reads NULL | `OgreBotAPI.Cures.CursedID` `[-archetype X\|-uncurable\|-uncurableonly\|-GroupOnly]` | ⚠️ Arguments changed | The arguments are different: Classic took ``, the new call takes `[-archetype X\|-uncurable\|-uncurableonly\|-GroupOnly]`. pass the `-GroupOnly` option to restrict it to the group |
| `Obj_CureCurseCalled.GetID_RaidCursedMember` | reads NULL | `OgreBotAPI.Cures.CursedID` `[-archetype X\|-uncurable\|-uncurableonly\|-GroupOnly]` | ⚠️ Arguments changed | The arguments are different: Classic took ``, the new call takes `[-archetype X\|-uncurable\|-uncurableonly\|-GroupOnly]`. raid scope is the default when you are in a raid; `-GroupOnly` narrows it |
| `Obj_CureCurseCalled.GroupCurseCount` | reads NULL | `OgreBotAPI.Cures.GroupCurses` | ✏️ Renamed |  |
| `Obj_CureCurseCalled.ic_CursedToons` | reads NULL | `OgreBotAPI.Cures.RaidCursedIDs` | ✏️ Renamed | JSON array of ids, not a collection you index by name |
| `Obj_CureCurseCalled:Remove` | does nothing | — | ⛔ Not ported yet | Note A |

## Obj_CureCalled

**Note A** (6 rows below): Classic's cure-request QUEUE internals. The new bot replaced the whole mechanism: a script asks for a cure through the request verbs (`Cures:Request` / `:RequestCurse` / `:RequestGroup` / `:RequestGroupWatch`) and the engine owns the queue, the de-duplication and the casting. There is no queue object to poke, by design.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `Obj_CureCalled:AutoAdd` | does nothing | `OgreBotAPI.Cures:Request` `[fw,victim,kinds...]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. for a CURSE use `Cures:RequestCurse` - a curse is its own channel, not one of the four basic cure kinds |
| `Obj_CureCalled.bCasted` | reads NULL | — | ⛔ Not ported yet | Note A |
| `Obj_CureCalled.bKeep` | reads NULL | — | ⛔ Not ported yet | Note A |
| `Obj_CureCalled.bValidCureAbility` | reads NULL | — | ⛔ Not ported yet | internal validity flag for the cached cure ability |
| `call Obj_CureCalled.CastCure` | does nothing | `OgreBotAPI.Cures:Request["<forwho>","<victim>"{,kinds...}]   (ask; the engine serves)` | ➡️ Lives somewhere else |  |
| `call Obj_CureCalled.CastCure_Actual` | does nothing | `OgreBotAPI.Cures:Request["<forwho>","<victim>"{,kinds...}]   /   to fire a specific ability yourself: OgreBotAPI.Abilities:Cast` | ➡️ Lives somewhere else |  |
| `Obj_CureCalled.CureAbility` | reads NULL | — | ⛔ Not ported yet |  |
| `Obj_CureCalled.icc_Entries` | reads NULL | — | ⛔ Not ported yet | the consumer sites read `.Used` (is anything queued) and call `:Clear`. The read is `Cures.CurseCalled`. There is deliberately NO clear verb: entries retire themselves when the victim is cured or the 8s deadline passes, so clearing by hand would fight the engine. |
| `Obj_CureCalled.RecentlyCastOn` | reads NULL | — | ⛔ Not ported yet | Note A |
| `Obj_CureCalled:RemoveByCustomFlag` | does nothing | — | ⛔ Not ported yet | Note A |
| `Obj_CureCalled:RemoveByToon` | does nothing | — | ⛔ Not ported yet | Note A |
| `Obj_CureCalled:Set_CureAbility` | does nothing | — | ⛔ Not ported yet | Classic picked and cached the cure ability here. The new engine resolves the cure itself when it services a request. |
| `Obj_CureCalled.Timer_RecentlyCast` | reads NULL | — | ⛔ Not ported yet | Note A |

## Obj_CurseCalled

**Note A** (6 rows below): Classic's cure-request QUEUE internals. The new bot replaced the whole mechanism: a script asks for a cure through the request verbs (`Cures:Request` / `:RequestCurse` / `:RequestGroup` / `:RequestGroupWatch`) and the engine owns the queue, the de-duplication and the casting. There is no queue object to poke, by design.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `Obj_CurseCalled:AutoAdd` | does nothing | `OgreBotAPI.Cures:Request` `[fw,victim,kinds...]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. for a CURSE use `Cures:RequestCurse` - a curse is its own channel, not one of the four basic cure kinds |
| `Obj_CurseCalled.bCasted` | reads NULL | — | ⛔ Not ported yet | Note A |
| `Obj_CurseCalled.bKeep` | reads NULL | — | ⛔ Not ported yet | Note A |
| `Obj_CurseCalled.bValidCureAbility` | reads NULL | — | ⛔ Not ported yet | internal validity flag for the cached cure ability |
| `call Obj_CurseCalled.CastCure` | does nothing | `OgreBotAPI.Cures:RequestCurse["<forwho>","<victim>"]   (ask; the engine serves)` | ➡️ Lives somewhere else | The read 'is a curse cure called right now?' is Cures.CurseCalled (see Obj_CureCurseCalled.CastCureCurse). |
| `call Obj_CurseCalled.CastCure_Actual` | does nothing | `OgreBotAPI.Cures:RequestCurse["<forwho>","<victim>"]   /   to fire a specific ability yourself: OgreBotAPI.Abilities:Cast` | ➡️ Lives somewhere else |  |
| `Obj_CurseCalled.CureAbility` | reads NULL | — | ⛔ Not ported yet |  |
| `Obj_CurseCalled.icc_Entries` | reads NULL | — | ⛔ Not ported yet | the consumer sites read `.Used` (is anything queued) and call `:Clear`. The read is `Cures.CurseCalled`. There is deliberately NO clear verb: entries retire themselves when the victim is cured or the 8s deadline passes, so clearing by hand would fight the engine. |
| `Obj_CurseCalled.RecentlyCastOn` | reads NULL | — | ⛔ Not ported yet | Note A |
| `Obj_CurseCalled:RemoveByCustomFlag` | does nothing | — | ⛔ Not ported yet | Note A |
| `Obj_CurseCalled:RemoveByToon` | does nothing | — | ⛔ Not ported yet | Note A |
| `Obj_CurseCalled:Set_CureAbility` | does nothing | — | ⛔ Not ported yet | Classic picked and cached the cure ability here. The new engine resolves the cure itself when it services a request. |
| `Obj_CurseCalled.Timer_RecentlyCast` | reads NULL | — | ⛔ Not ported yet | Note A |

## GroupCureOb

**Note A** (4 rows below): a per-kind count of afflicted group members. The new Cures surface counts curses and answers per-detriment questions via `.Detrimental[main,back,id,field]`, but has no per-cure-kind group tally.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `GroupCureOb.Arcane` | reads NULL | — | ⛔ Not ported yet | Note A |
| `GroupCureOb.Elemental` | reads NULL | — | ⛔ Not ported yet | Note A |
| `GroupCureOb.GroupCureAvailable` | reads NULL | — | ⛔ Not ported yet | the 3 consumer sites all do `AbilityID:Set[${GroupCureOb.GroupCureAvailable}]` and then cast it - that whole shape becomes one `:RequestGroup`. Note also that a hard-coded ability-NAME table is Rule-10 territory now; the export catalog is the name source. |
| `GroupCureOb.Noxious` | reads NULL | — | ⛔ Not ported yet | Note A |
| `GroupCureOb.NumOfPCsAfflicted` | reads NULL | — | ⛔ Not ported yet | a count of PCs carrying ANY curable detriment. The new surface counts CURSES (.GroupCurses/.RaidCurses) and exposes per-detriment reads (.Detrimental), but has no all-afflicted tally. |
| `GroupCureOb.NumOfPCsCursed` | reads NULL | `OgreBotAPI.Cures.GroupCurses` | ✏️ Renamed | `.RaidCurses` is the raid-wide twin |
| `GroupCureOb.Trauma` | reads NULL | — | ⛔ Not ported yet | Note A |

## Abilities

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `Abilities.Ability` | reads NULL | `OgreBotAPI.Abilities.ID` | ✏️ Renamed |  |
| `Abilities.AddIndex` | reads NULL | `OgreBotAPI.Abilities.ID` | ✏️ Renamed |  |
| `Abilities.GetIndexBy` | reads NULL | `OgreBotAPI.Abilities.ID` | ✏️ Renamed |  |
| `Abilities.GetIndexByID` | reads NULL | `OgreBotAPI.Abilities.ID` | ✏️ Renamed |  |
| `Abilities.GetIndexByName` | reads NULL | `OgreBotAPI.Abilities.ID` | ✏️ Renamed |  |

## OgreBotDebug

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotDebug.bIncludeMSTime` | reads NULL | — | ⛔ Not ported yet | a Classic formatting flag on its own echo helper; the new `Debug:Echo` owns its formatting |
| `OgreBotDebug:Echo` | does nothing | `OgreBotAPI.Debug:Echo` `[fw,text]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it.<br>Not taken any more: `Message`. |
| `OgreBotDebug:EchoIf` | does nothing | — | ⛔ Not ported yet | no conditional-echo verb; gate the call yourself and use Debug:Echo |
| `OgreBotDebug.Prefix` | reads NULL | `OgreBotAPI.Debug.DebugPrefix` | ✏️ Renamed |  |

## OgreBotInternals

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotInternals.bInternal` | reads NULL | — | ⛔ Not ported yet | internal build flag |
| `OgreBotInternals.Is_InternalVersion` | reads NULL | — | ⛔ Not ported yet | asks whether this is an internal build. No new-bot equivalent is exposed; `Debug.Version` / `.CheckVersion` are the version reads (and `.CheckVersion` is a STUB). |

## Not in the new bot yet

If your script needs one of these, leave it out for now and tell us - this list is what still needs work.

- `Ob_AutoTarget:AddActorFromUI` - not ported yet
- `Ob_AutoTarget:AddAddsThenNamed` - not ported yet
- `Ob_AutoTarget:AddListBoxItem` - not ported yet
- `Ob_AutoTarget:AddNamed` - not ported yet
- `TabConfig:After_Initialization` - not ported yet
- `Obj_OgreUtilities.Alignment` - not ported yet
- `ProfileConfig.AllowAbilityConversions` - not ported yet
- `Obj_OgreUtilities.AnyGroupMembersDead` - not ported yet
- `g_RaidOb:AotA1` - not ported yet
- `GroupCureOb.Arcane` - not ported yet
- `GetInfoOb.AscensionVitalityRemaining` - not ported yet
- `Obj_CureCurseCalled:AutoRemove` - not ported yet
- `TabConfig.BaseSetName` - not ported yet
- `ProfileConfig.BaseSetName` - not ported yet
- `ProfileConfig:BaseSetNameList` - not ported yet
- `TabConfig.BaseSetRef` - not ported yet
- `ProfileConfig.BaseSetRef` - not ported yet
- `Obj_CureCalled.bCasted` - not ported yet
- `Obj_CurseCalled.bCasted` - not ported yet
- `Obj_CureCurseCalled.bEmpty` - not ported yet
- `OgreBotDebug.bIncludeMSTime` - not ported yet
- `OgreBotInternals.bInternal` - not ported yet
- `Obj_CureCalled.bKeep` - not ported yet
- `Obj_CurseCalled.bKeep` - not ported yet
- `SpellOb.BLAdvantage` - not ported yet
- `SpellOb.BLPrimal` - not ported yet
- `SpellOb.BLPrimalMinSavLevel` - not ported yet
- `Obj_CureCalled.bValidCureAbility` - not ported yet
- `Obj_CurseCalled.bValidCureAbility` - not ported yet
- `Obj_OgreUtilities.CallingScriptName` - not ported yet
- `call Obj_CureCurseCalled.CastCureCurseHardTarget` - not ported yet
- `ProfileConfig.CheckCopingOldServerProfile` - not ported yet
- `call Obj_OgreUtilities.CheckEvacTotems` - not ported yet
- `GetInfoOb.CleanNameWithUnderscores` - not ported yet
- `ClassInfo:Clear` - not ported yet
- `ProfileConfig:Clear` - not ported yet
- `call Obj_OgreUtilities.ClearQuestWindow` - not ported yet
- `Ob_AutoTarget:ClearSavedLists` - not ported yet
- `call Obj_OgreUtilities.Close_Depot` - not ported yet
- `ProfileConfig.ConfigFileLocation` - not ported yet
- `call Obj_OgreUtilities.ConverseWithScrollMerchant` - not ported yet
- `GetInfoOb.CurableDisable` - not ported yet
- `Obj_CureCalled.CureAbility` - not ported yet
- `Obj_CurseCalled.CureAbility` - not ported yet
- `GetInfoOb.CureCurseNotRecentlyCast` - not ported yet
- `ProfileConfig.CurrentSetRef` - not ported yet
- `SpellOb.DamageType` - not ported yet
- `SpellOb.DamageTypeGroup` - not ported yet
- `ProfileConfig.DefaultProfileName` - not ported yet
- `Obj_OgreUtilities:Depot_Button` - not ported yet
- `Obj_OgreUtilities.Depot_Visible` - not ported yet
- `Obj_OgreUtilities.DepotNames` - not ported yet
- `SpellOb.DescRestrictions` - not ported yet
- `g_RaidOb:DMIR` - not ported yet
- `g_RaidOb:DMPI` - not ported yet
- `g_RaidOb:DMPS` - not ported yet
- `GetInfoOb.DottedExamine_ref` - not ported yet
- `OgreBotDebug:EchoIf` - not ported yet
- `GroupCureOb.Elemental` - not ported yet
- `Ob_AutoTarget.Enable_Status` - not ported yet
- `GetInfoOb.EquipOrInven` - not ported yet
- `Obj_OgreUtilities.EscapeTotemName` - not ported yet
- `GetInfoOb.Evaluate_Num` - not ported yet
- `ProfileConfig.Exists_TabTextToValueTable` - not ported yet
- `SpellOb.FeralAdvantage` - not ported yet
- `SpellOb.FeralPrimal` - not ported yet
- `ProfileConfig.fp_ImportProfileFileLocation` - not ported yet
- `GetInfoOb:Get_GroupNames` - not ported yet
- `ProfileConfig.Get_ProfilePartsActiveForTab` - not ported yet
- `ProfileConfig.Get_ProfilePartsCustomFile` - not ported yet
- `ProfileConfig.Get_ProfilePartsCustomFileFromCurrentSettings` - not ported yet
- `GetInfoOb:Get_RaidIDs` - not ported yet
- `GetInfoOb:Get_RaidNames` - not ported yet
- `ProfileConfig.Get_ReuseableSS` - not ported yet
- `ProfileConfig.Get_ReuseableSSPP` - not ported yet
- `ProfileConfig.Get_TabTextToValueTable` - not ported yet
- `Obj_OgreUtilities.Get_ZoneName` - not ported yet
- `GetInfoOb.GetAscensionScrolls` - not ported yet
- `call Obj_OgreUtilities.GetInGameQuestStep` - not ported yet
- `call Obj_OgreUtilities.GetIntoCorrectZone` - not ported yet
- `call Obj_OgreUtilities.GHToHouse` - not ported yet
- `GroupCureOb.GroupCureAvailable` - not ported yet
- `Obj_OgreUtilities.GroupInCombat` - not ported yet
- `TabConfig:GUI_Discord` - not ported yet
- `TabConfig:GUI_Forums` - not ported yet
- `TabConfig:GUI_Helper` - not ported yet
- `TabConfig:GUI_LastClickedTab` - not ported yet
- `TabConfig:GUI_TabClicked` - not ported yet
- `TabConfig:GUI_Wiki` - not ported yet
- `call Obj_OgreUtilities.Handle_Depot` - not ported yet
- `call Obj_OgreUtilities.HandleCampSpotToPort` - not ported yet
- `call Obj_OgreUtilities.HandleConversation` - not ported yet
- `call Obj_OgreUtilities.HandleWaitForCombat_old` - not ported yet
- `call Obj_OgreUtilities.HandleWaitForCombatOrPower` - not ported yet
- `Obj_CureCalled.icc_Entries` - not ported yet
- `Obj_CurseCalled.icc_Entries` - not ported yet
- `Obj_OgreUtilities.IndexMatch` - exists, does nothing yet
- `GetInfoOb.InGame` - not ported yet
- `Obj_OgreUtilities:Initialize_Depot` - not ported yet
- `TabConfig:InitSetup` - not ported yet
- `Obj_OgreUtilities.InternalVersion` - not ported yet
- `Obj_OgreUtilities.InZoneShortName` - not ported yet
- `OgreBotInternals.Is_InternalVersion` - not ported yet
- `Obj_OgreUtilities.IsAnyoneDead` - not ported yet
- `SpellOb.IsAStun` - not ported yet
- `Obj_OgreUtilities.IsGroupDeadOrNoRes` - not ported yet
- `Obj_OgreUtilities.ItemCount` - exists, does nothing yet
- `Items` - not ported yet
- `TabConfig.LastClickedTabName` - not ported yet
- `TabConfig.LavishSettingsConfigName` - not ported yet
- `ProfileConfig.LavishSettingsConfigName` - not ported yet
- `Ob_AutoTarget:LoadSavedLists` - not ported yet
- `Ob_AutoTarget:LoadZoneFileIntoMemory` - not ported yet
- `call Obj_OgreUtilities.NavToLocation` - not ported yet
- `GetInfoOb.NewCharacterLoaded` - not ported yet
- `GroupCureOb.Noxious` - not ported yet
- `GroupCureOb.NumOfPCsAfflicted` - not ported yet
- `Obj_OgreUtilities.Obj_OgreResources` - not ported yet
- `Obj_SpewStats` - exists, does nothing yet
- `ogre meshuiint` - not ported yet
- `ogre travelint` - not ported yet
- `OgreBackwardKey` - not ported yet
- `OgreForwardKey` - not ported yet
- `Obj_OgreUtilities.OgreNavChecks` - not ported yet
- `Obj_OgreUtilities.OgreNavEntry` - not ported yet
- `OgreZoomOutKey` - not ported yet
- `Obj_OgreUtilities.OnCorrectCharacter` - not ported yet
- `call Obj_OgreUtilities.OnQuestStep` - not ported yet
- `call Obj_OgreUtilities.Open_Depot` - not ported yet
- `GetInfoOb:PopulatePCOptionLists` - not ported yet
- `GetInfoOb:PopulatePCOptionLists_AddToUI` - not ported yet
- `Ob_AutoTarget:PopulateUI` - not ported yet
- `Obj_OgreUtilities.QuestIt` - not ported yet
- `Obj_OgreUtilities.Quests` - not ported yet
- `ClassInfo.RangerEpic2AbilityID` - not ported yet
- `Obj_CureCalled.RecentlyCastOn` - not ported yet
- `Obj_CurseCalled.RecentlyCastOn` - not ported yet
- `TabConfig.Ref` - not ported yet
- `ProfileConfig.Ref` - not ported yet
- `Obj_CureCurseCalled:Remove` - not ported yet
- `Obj_CureCalled:RemoveByCustomFlag` - not ported yet
- `Obj_CurseCalled:RemoveByCustomFlag` - not ported yet
- `Obj_CureCalled:RemoveByToon` - not ported yet
- `Obj_CurseCalled:RemoveByToon` - not ported yet
- `Ob_AutoTarget:RemoveFromUI` - not ported yet
- `ProfileConfig.ReuseableSS` - not ported yet
- `ProfileConfig.ReuseableSSPP` - not ported yet
- `g_RaidOb:ROAOMCG` - not ported yet
- `g_RaidOb:ROASEC` - not ported yet
- `g_RaidOb:ROBSBFC` - not ported yet
- `g_RaidOb:RODFCJ` - not ported yet
- `g_RaidOb:RODTFP` - not ported yet
- `g_RaidOb:ROKoolbhCloudOfVile` - not ported yet
- `g_RaidOb:ROKraletusCureCalled` - not ported yet
- `g_RaidOb:ROOSSCOBEPM` - not ported yet
- `g_RaidOb:ROOSSSAC` - not ported yet
- `g_RaidOb:ROPC` - not ported yet
- `g_RaidOb:ROSGPRTCS` - not ported yet
- `g_RaidOb:ROTOVI` - not ported yet
- `Obj_CureCalled:Set_CureAbility` - not ported yet
- `Obj_CurseCalled:Set_CureAbility` - not ported yet
- `call Obj_OgreUtilities.Set_FirstPersonView` - not ported yet
- `Ob_AutoTarget.set_OgreAutoTarget` - not ported yet
- `call Obj_OgreUtilities.Set_ZoomIn` - not ported yet
- `call Obj_OgreUtilities.Set_ZoomOut` - not ported yet
- `call Obj_OgreUtilities.Set_ZoomOut_MouseWheel` - not ported yet
- `TabConfig:SetBaseSetName` - not ported yet
- `ProfileConfig:SetBaseSetName` - not ported yet
- `ProfileConfig:SetConfigFileLocation` - not ported yet
- `ProfileConfig:SetCurrentSetRefToBaseSetRef` - not ported yet
- `TabConfig:SetLavishSettingsConfigName` - not ported yet
- `ProfileConfig:SetLavishSettingsConfigName` - not ported yet
- `TabConfig:SetupSubObjects` - not ported yet
- `g_RaidOb:SGDD` - not ported yet
- `g_RaidOb:SGPRD` - not ported yet
- `g_RaidOb:SGTD` - not ported yet
- `g_RaidOb:SGTFD` - not ported yet
- `ProfileConfig.SingleProfileName` - not ported yet
- `Ob_AutoTarget:Spew` - not ported yet
- `SpellOb.SpiritualAdvantage` - not ported yet
- `SpellOb.SpiritualPrimal` - not ported yet
- `TabConfig.TabColSetRefs` - not ported yet
- `ProfileConfig.TabManager` - not ported yet
- `TabConfig.TabName_HelpURL` - not ported yet
- `ProfileConfig.TabTextToValueTable` - not ported yet
- `Obj_OgreUtilities.Timer_HandleWaitForCombatw` - not ported yet
- `Obj_OgreUtilities.Timer_PreCombatBuff` - not ported yet
- `Obj_CureCalled.Timer_RecentlyCast` - not ported yet
- `Obj_CurseCalled.Timer_RecentlyCast` - not ported yet
- `GroupCureOb.Trauma` - not ported yet
- `GetInfoOb.Trim` - not ported yet
- `GetInfoOb:TroubadorPoWMythCloakProc` - not ported yet
- `GetInfoOb.TroubadorPoWMythCloakProcOn` - not ported yet
- `GetInfoOb.TroubadorPowMythCloakProcTimer` - not ported yet
- `Obj_OgreUtilities:UpdateQuestInformation` - not ported yet
- `call GetInfoOb.WaitForCasting` - not ported yet
- `call Obj_OgreUtilities.WaitForGroupPower` - not ported yet
- `call Obj_OgreUtilities.WaitForScript` - not ported yet
- `Obj_OgreUtilities.WhereAreWe` - not ported yet
- `Obj_OgreUtilities:ZoneReset_PopulateInternalMemory` - not ported yet
