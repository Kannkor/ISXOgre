# Camp spot

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../index.md).
</div>

Everything Classic's *CampSpot System Reference* and *CampSpot Jump* pages described - the `Ogre_CampSpot` object, the movement locks, the `OgreBotAPI` camp-spot calls, the camp-spot console commands and `Obj_CampSpotJump` - and what each one is in the new bot.

> **:warning: An old camp-spot call does nothing now - it does not give an error**
>
> `Ogre_CampSpot` does not exist in the new bot. Every `Ogre_CampSpot:` call silently does nothing and every `${Ogre_CampSpot.…}` read gives `NULL`. The camp spot now lives in `OgreBotAPI.CampSpot` (and the movement locks in `OgreBotAPI.Movement`).

## At a glance

| What happened | Names |
|---|---|
| ⚠️ Arguments changed | 20 |
| ✏️ Renamed | 52 |
| ➡️ Moved | 11 |
| ➡️ Lives somewhere else | 9 |
| 📄 In a data file now | 2 |
| ⛔ Removed | 7 |
| ✅ Works as is | 34 |
| **Total** | **135** |

## The big change: these calls need a for-who now

Most `Ogre_CampSpot:` calls had **no** for-who - they acted on the session that ran them. Every `OgreBotAPI.CampSpot` call takes the for-who **first**. To keep the old behaviour, use `all` - a script's own call only runs on the session running it, so `all` means that session. If Classic's call already started with a for-who (`["all", …]`), keep it.

## Worked examples

One real Classic line per kind of change, and the line that replaces it.

### ⚠️ Arguments changed: `Ogre_CampSpot:Set_CCS`

```
; before (Classic)
Ogre_CampSpot:Set_CCS[12.505716,75.479492,-426.626892]
; after (new bot)
OgreBotAPI.CampSpot:SetLoc[all,12.505716,75.479492,-426.626892]
```

The Classic object call only ever moved this session's own camp spot, so the new for-who is `all` - the call only runs on the session running the script, so `all` is that session.

### ✏️ Renamed: `Ogre_CampSpot.Get_CampSpot`

```
; before (Classic)
if ${Math.Distance[${Ogre_CampSpot.Get_CampSpot},${This.RaidSpot}]} < ${Math.Distance[${Ogre_CampSpot.Get_CampSpot},${This.RaidJoustSpot}]}
; after (new bot)
if ${Math.Distance[${OgreBotAPI.CampSpot.EffectiveLoc},${This.RaidSpot}]} < ${Math.Distance[${OgreBotAPI.CampSpot.EffectiveLoc},${This.RaidJoustSpot}]}
```

EffectiveLoc is the spot the toon actually walks to (the relative offset applied), which is what Get_CampSpot returned. With no camp spot set it reads empty text.

### ➡️ Moved: `Ogre_CampSpot:ClearRelative`

```
; before (Classic)
Ogre_CampSpot:ClearRelative["all"]
; after (new bot)
OgreBotAPI.CampSpot:ClearRelative["all"]
```

Same name and arguments; only the object in front changed.

### 📄 In a data file now: `Obj_CampSpotJump.bActive`

```
; before (Classic)
if ${Obj_CampSpotJump.bActive}
; after (new bot)
{ "when": [ { "jumpRoute": { "is": "running" } } ] }
```

## The Ogre_CampSpot object

Calls written `Ogre_CampSpot:…` (methods) and `${Ogre_CampSpot.…}` (members).

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `Ogre_CampSpot.AbsoluteCampSpotLoc` | reads NULL | `OgreBotAPI.CampSpot.AnchorLoc` | ✏️ Renamed | see `Get_AbsoluteCampSpot`. |
| `Ogre_CampSpot.AllowCampSpot` | reads NULL | `OgreBotAPI.Movement.AllowMovement` | ✏️ Renamed |  |
| `Ogre_CampSpot.AllowMovement` | reads NULL | `OgreBotAPI.Movement.AllowMovement` | ➡️ Moved |  |
| `Ogre_CampSpot.AtCampSpot` | reads NULL | `OgreBotAPI.CampSpot.AtCampSpot` | ➡️ Moved |  |
| `Ogre_CampSpot.bUse3D` | reads NULL | `OgreBotAPI.CampSpot.Use3D` | ✏️ Renamed |  |
| `Ogre_CampSpot:Clear` | does nothing | `OgreBotAPI.Movement:ClearBlocks` `[fw]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). `CampSpot:Release` (LetsGo) also clears them. |
| `Ogre_CampSpot:ClearAll` | does nothing | `OgreBotAPI.CampSpot:ClearAll` `[fw]` | ➡️ Moved |  |
| `Ogre_CampSpot:ClearCampSpot` | does nothing | `OgreBotAPI.CampSpot:ClearCampSpot` `[fw]` | ➡️ Moved |  |
| `Ogre_CampSpot:ClearRelative` | does nothing | `OgreBotAPI.CampSpot:ClearRelative` `[fw]` | ➡️ Moved |  |
| `Ogre_CampSpot.CSZoneName` | reads NULL | `OgreBotAPI.CampSpot.Zone` | ✏️ Renamed |  |
| `Ogre_CampSpot:Disable` | does nothing | `OgreBotAPI.Movement:Block` `[fw,reason]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. Renamed on purpose: Classic's `Disable` ADDS a block and `Enable` REMOVES one. Next to `CampSpot:Enable` / `:Disable` (which arm and disarm the LEASH) that polarity reads backwards, and it already cost this port a wrong mapping. The verbs now say what they do. `[fw, reason]` - the reason name is REQUIRED; an unnamed block could never be released. |
| `Ogre_CampSpot.Disabled` | reads NULL | `OgreBotAPI.Movement.Blocked` `[reason]` | ✏️ Renamed | `[reason]` asks about that hold; no argument asks whether ANY hold is active. |
| `Ogre_CampSpot.DistanceFromAbsoluteCampSpot` | reads NULL | `${Math.Distance[${ISXOgreEQ2.CampSpot.AnchorLoc},${Me.Loc}]}` | ➡️ Lives somewhere else |  |
| `Ogre_CampSpot.DistanceFromCampSpot` | reads NULL | `OgreBotAPI.CampSpot.DistanceTo` | ✏️ Renamed |  |
| `Ogre_CampSpot:Enable` | does nothing | `OgreBotAPI.Movement:Unblock` `[fw,reason]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. Renamed on purpose: Classic's `Disable` ADDS a block and `Enable` REMOVES one. Next to `CampSpot:Enable` / `:Disable` (which arm and disarm the LEASH) that polarity reads backwards, and it already cost this port a wrong mapping. The verbs now say what they do. `[fw, reason]` releases THAT hold only. |
| `Ogre_CampSpot.Get_AbsoluteCampSpot` | reads NULL | `OgreBotAPI.CampSpot.AnchorLoc` | ✏️ Renamed | `"x,y,z"` string, same shape as `.EffectiveLoc`, so it feeds `Math.Distance` directly; components are `.AnchorX/.AnchorY/.AnchorZ`. Empty string when no spot is set. |
| `Ogre_CampSpot.Get_CampSpot` | reads NULL | `OgreBotAPI.CampSpot.EffectiveLoc` | ✏️ Renamed | see `RelativeCampSpotLoc` - same value. |
| `Ogre_CampSpot.Get_HowClose` | reads NULL | `OgreBotAPI.CampSpot.HowClose` | ✏️ Renamed |  |
| `Ogre_CampSpot.Get_HowFar` | reads NULL | `OgreBotAPI.CampSpot.HowFar` | ✏️ Renamed |  |
| `Ogre_CampSpot.Get_RelativeCampSpot` | reads NULL | `OgreBotAPI.CampSpot.EffectiveLoc` | ✏️ Renamed | see `RelativeCampSpotLoc` - same value, third spelling. |
| `Ogre_CampSpot.Get_RelativeMods` | reads NULL | `OgreBotAPI.CampSpot.RelativeLoc` | ✏️ Renamed |  |
| `Ogre_CampSpot.Get_Use3D` | reads NULL | `OgreBotAPI.CampSpot.Use3D` | ✏️ Renamed |  |
| `Ogre_CampSpot.Get_X` | reads NULL | `OgreBotAPI.CampSpot.EffectiveX` | ✏️ Renamed |  |
| `Ogre_CampSpot.Get_Y` | reads NULL | `OgreBotAPI.CampSpot.EffectiveY` | ✏️ Renamed |  |
| `Ogre_CampSpot.Get_Z` | reads NULL | `OgreBotAPI.CampSpot.EffectiveZ` | ✏️ Renamed |  |
| `call Ogre_CampSpot.HandleWaitForCampSpot` | does nothing | encounter file: {"wait":"atCampSpot","limitMs":N,"onTimeout":"fail"\|"proceed"}   /   IC file: the `path` step (it waits for arrival itself)   /   hand-written script: poll ${OgreBotAPI.CampSpot.AtCampSpot} in your own bounded wait loop | ➡️ Lives somewhere else | Of the ~82 Classic call sites most sit in OgreBotRaidModules fight files (-&gt; encounter `wait atCampSpot`) and a few IC _ignore_scripts. Classic's loop also quit early once the toon was farther than HowFar from the spot (= not walking there) - the encounter `wait` has no such exit, so its limitMs is the bound. If you hand-roll the poll, bound it (feedback: polling loops must be bounded) and include !${Me.IsDead}. |
| `Ogre_CampSpot.HowClose` | reads NULL | `OgreBotAPI.CampSpot.HowClose` | ➡️ Moved |  |
| `Ogre_CampSpot.HowFar` | reads NULL | `OgreBotAPI.CampSpot.HowFar` | ➡️ Moved |  |
| `Ogre_CampSpot.RelativeCampSpotLoc` | reads NULL | `OgreBotAPI.CampSpot.EffectiveLoc` | ✏️ Renamed | components are `.EffectiveX/.EffectiveY/.EffectiveZ`. The RAW anchor is the separate `.AnchorLoc`; the two differ by exactly the sticky offset whenever a relative is in play. |
| `Ogre_CampSpot.RelativeLoc` | reads NULL | `OgreBotAPI.CampSpot.RelativeLoc` | ➡️ Moved |  |
| `Ogre_CampSpot.sc_ItemsAffectingMovement` | reads NULL | `OgreBotAPI.Movement.BlockReasons` | ✏️ Renamed |  |
| `Ogre_CampSpot:Set_CampSpot` | does nothing | `OgreBotAPI.CampSpot:SetHere` `[fw,howClose,howFar]` | ✏️ Renamed | do not convert this to :SetLoc - the arguments are bands, not a location |
| `Ogre_CampSpot:Set_CCS` | does nothing | `OgreBotAPI.CampSpot:SetLoc` `[fw,x,y,z]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. Set_CCS took NO for-who (`method Set_CCS(float LocX, float LocY, float LocZ)`) - it was local-only. The new verb takes a for-who first, so you must INSERT one: use `all`. The for-who is a gate on the session running the line, not a broadcast, so `all` acts on this session only - exactly what the old call did. 33 call sites use this form. |
| `Ogre_CampSpot:Set_ChangeCampSpot` | does nothing | `OgreBotAPI.CampSpot:SetLoc` `[fw,x,y,z]` | ✏️ Renamed |  |
| `Ogre_CampSpot:Set_ChangeCampSpotBy` | does nothing | `OgreBotAPI.CampSpot:NudgeBy` `[fw,dx,dy,dz]` | ✏️ Renamed |  |
| `Ogre_CampSpot:Set_ChangeRelativeCampSpotBy` | does nothing | `OgreBotAPI.CampSpot:NudgeRelativeBy` `[fw,dx,dy,dz]` | ✏️ Renamed |  |
| `Ogre_CampSpot:Set_CS` | does nothing | `OgreBotAPI.CampSpot:SetHere` `[fw,howClose,howFar]` | ✏️ Renamed |  |
| `Ogre_CampSpot:Set_Formation_Circle` | does nothing | `OgreBotAPI.CampSpot:SetFormation` `[fw,kind,dist,circleSpots]` | ✏️ Renamed | pass kind `circle`<br>Not taken any more: `_Z`, `_UseRelative`. |
| `Ogre_CampSpot:Set_Formation_MonkeyInMiddle` | does nothing | `OgreBotAPI.CampSpot:SetFormation` `[fw,kind,dist,circleSpots]` | ✏️ Renamed | pass kind `monkey`<br>Not taken any more: `_Z`, `_Middle`, `_UseRelative`. |
| `Ogre_CampSpot:Set_Formation_MonkeyInMiddleRaid` | does nothing | `OgreBotAPI.CampSpot:SetFormation` `[fw,kind,dist,circleSpots]` | ✏️ Renamed | pass kind `monkeyraid`<br>Not taken any more: `_Y`, `_Z`, `_CircleSpots`, `_UseRelative`. |
| `Ogre_CampSpot:Set_HowClose` | does nothing | `OgreBotAPI.CampSpot:SetHowClose` `[fw,v]` | ✏️ Renamed |  |
| `Ogre_CampSpot:Set_HowFar` | does nothing | `OgreBotAPI.CampSpot:SetHowFar` `[fw,v]` | ✏️ Renamed |  |
| `Ogre_CampSpot:Set_Relative` | does nothing | `OgreBotAPI.CampSpot:SetRelativeLoc` `[fw,x,y,z]` | ✏️ Renamed |  |
| `Ogre_CampSpot:Set_Use3D` | does nothing | `OgreBotAPI.CampSpot:SetUse3D` `[fw,0/1]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. |
| `Ogre_CampSpot.uAllowMovement` | reads NULL | `OgreBotAPI.Movement.BlockCount` | ✏️ Renamed |  |
| `Ogre_CampSpot.UsingRelative` | reads NULL | `OgreBotAPI.CampSpot.RelativeActive` | ✏️ Renamed | NOT `.UsingRelativeBy`, and this is the trap. `UsingRelativeBy` reports the MODE and is TRUE for a RelativeBy state with a 0,0,0 offset - where `.RelativeActive` is correctly FALSE. Pinned by CampSpotTests; confusing the two fails 4 checks. |
| `Ogre_CampSpot.UsingRelativeBy` | reads NULL | `OgreBotAPI.CampSpot.UsingRelativeBy` | ➡️ Moved |  |
| `Ogre_CampSpot.UsingRelativeByCS` | reads NULL | `${ISXOgreEQ2.CampSpot.RelativeX} / .RelativeY / .RelativeZ (any non-zero)` | ➡️ Lives somewhere else | use `.RelativeActive` unless you specifically need this half alone. |
| `Ogre_CampSpot.UsingRelativeCS` | reads NULL | `${Math.Distance[${ISXOgreEQ2.CampSpot.AnchorLoc},${ISXOgreEQ2.CampSpot.EffectiveLoc}]}` | ➡️ Lives somewhere else | non-zero == TRUE. For the plain "is a relative in effect" question use `.RelativeActive`. |
| `Ogre_CampSpot.ValidCampSpotOptions` | reads NULL | `OgreBotAPI.CampSpot.ValidOptions` | ✏️ Renamed | the inherited Object_Movement allowance is a SEPARATE term from the `Allow Camp Spot` config box - both are tested. Does NOT test whether the leash is armed (that is `.Enabled`) nor the annulus (that is `.AtCampSpot`). |
| `Ogre_CampSpot.ValidCampSpotOptionsCommon` | reads NULL | `OgreBotAPI.CampSpot.ValidOptionsCommon` | ✏️ Renamed | `.ValidOptions` = this AND the current zone matches the capture zone. |
| `Ogre_CampSpot.ValidStayAtCampSpotOptions` | reads NULL | `OgreBotAPI.CampSpot.Leashing` | ✏️ Renamed | Leashing is the bot's own answer, made on its pulse - true while it is actually walking you back. It is also false when the leash is switched off or you are in a different zone from where the spot was set, which Classic's test did not check. |

## Movement locks (Enable / Disable)

Classic kept the movement lock on `Obj_Movement`, reachable as `Obj_CampSpot` and through `Ogre_CampSpot` (those rows are in the table above). In the new bot it is `OgreBotAPI.Movement`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `Obj_CampSpot.AllowCampSpot` | reads NULL | `OgreBotAPI.Movement.AllowMovement` | ✏️ Renamed |  |
| `Obj_Movement.AllowCampSpot` | reads NULL | `OgreBotAPI.Movement.AllowMovement` | ✏️ Renamed |  |
| `Obj_CampSpot.AllowMovement` | reads NULL | `OgreBotAPI.Movement.AllowMovement` | ➡️ Moved |  |
| `Obj_Movement.AllowMovement` | reads NULL | `OgreBotAPI.Movement.AllowMovement` | ➡️ Moved |  |
| `Obj_CampSpot:Clear` | does nothing | `OgreBotAPI.Movement:ClearBlocks` `[fw]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). `CampSpot:Release` (LetsGo) also clears them. |
| `Obj_Movement:Clear` | does nothing | `OgreBotAPI.Movement:ClearBlocks` `[fw]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). `CampSpot:Release` (LetsGo) also clears them. |
| `Obj_CampSpot:Disable` | does nothing | `OgreBotAPI.Movement:Block` `[fw,reason]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. Renamed on purpose: Classic's `Disable` ADDS a block and `Enable` REMOVES one. Next to `CampSpot:Enable` / `:Disable` (which arm and disarm the LEASH) that polarity reads backwards, and it already cost this port a wrong mapping. The verbs now say what they do. `[fw, reason]` - the reason name is REQUIRED; an unnamed block could never be released. |
| `Obj_Movement:Disable` | does nothing | `OgreBotAPI.Movement:Block` `[fw,reason]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. Renamed on purpose: Classic's `Disable` ADDS a block and `Enable` REMOVES one. Next to `CampSpot:Enable` / `:Disable` (which arm and disarm the LEASH) that polarity reads backwards, and it already cost this port a wrong mapping. The verbs now say what they do. `[fw, reason]` - the reason name is REQUIRED; an unnamed block could never be released. |
| `Obj_CampSpot.Disabled` | reads NULL | `OgreBotAPI.Movement.Blocked` `[reason]` | ✏️ Renamed | `[reason]` asks about that hold; no argument asks whether ANY hold is active. |
| `Obj_Movement.Disabled` | reads NULL | `OgreBotAPI.Movement.Blocked` `[reason]` | ✏️ Renamed | `[reason]` asks about that hold; no argument asks whether ANY hold is active. |
| `Obj_CampSpot:Enable` | does nothing | `OgreBotAPI.Movement:Unblock` `[fw,reason]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. Renamed on purpose: Classic's `Disable` ADDS a block and `Enable` REMOVES one. Next to `CampSpot:Enable` / `:Disable` (which arm and disarm the LEASH) that polarity reads backwards, and it already cost this port a wrong mapping. The verbs now say what they do. `[fw, reason]` releases THAT hold only. |
| `Obj_Movement:Enable` | does nothing | `OgreBotAPI.Movement:Unblock` `[fw,reason]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. Renamed on purpose: Classic's `Disable` ADDS a block and `Enable` REMOVES one. Next to `CampSpot:Enable` / `:Disable` (which arm and disarm the LEASH) that polarity reads backwards, and it already cost this port a wrong mapping. The verbs now say what they do. `[fw, reason]` releases THAT hold only. |
| `Obj_CampSpot.sc_ItemsAffectingMovement` | reads NULL | `OgreBotAPI.Movement.BlockReasons` | ✏️ Renamed |  |
| `Obj_Movement.sc_ItemsAffectingMovement` | reads NULL | `OgreBotAPI.Movement.BlockReasons` | ✏️ Renamed |  |
| `Obj_CampSpot.uAllowMovement` | reads NULL | `OgreBotAPI.Movement.BlockCount` | ✏️ Renamed |  |
| `Obj_Movement.uAllowMovement` | reads NULL | `OgreBotAPI.Movement.BlockCount` | ✏️ Renamed |  |

## OgreBotAPI camp-spot calls

The flat `OgreBotAPI:` camp-spot calls. They moved into `OgreBotAPI.CampSpot`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:CampSpot` | does nothing | `OgreBotAPI.CampSpot:SetHere` `[fw,howClose,howFar]` | ✏️ Renamed |  |
| `OgreBotAPI:CCS` | does nothing | `OgreBotAPI.CampSpot:SetLoc` `[fw,x,y,z]` | ✏️ Renamed | Not taken any more: `_RoomID`. |
| `OgreBotAPI:ChangeCampSpot` | does nothing | `OgreBotAPI.CampSpot:SetLoc` `[fw,x,y,z]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. took coordinates at arg 0 with no for-who. The new form requires one: `OgreBotAPI.CampSpot:SetLoc["all",x,y,z]`. |
| `OgreBotAPI:ChangeCampSpotWho` | does nothing | `OgreBotAPI.CampSpot:SetLoc` `[fw,x,y,z]` | ✏️ Renamed |  |
| `OgreBotAPI:ClearRCS` | does nothing | `OgreBotAPI.CampSpot:ClearRelative` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:CRCS` | does nothing | `OgreBotAPI.CampSpot:SetRelativeLoc` `[fw,x,y,z]` | ✏️ Renamed | Not taken any more: `_RoomID`. |
| `OgreBotAPI:LetsGo` | does nothing | `OgreBotAPI.CampSpot:Release` `[fw]` | ✏️ Renamed |  |
| `OgreBotAPI:SetCS_BehindNPC` | does nothing | `OgreBotAPI.CampSpot:SetLocBehindActor` `[fw,nameOrId,dist,skipIfAggro]` | ✏️ Renamed |  |
| `OgreBotAPI:SetCS_InFrontNPC` | does nothing | `OgreBotAPI.CampSpot:SetLocInFrontOfActor` `[fw,nameOrId,dist,skipIfAggro]` | ✏️ Renamed |  |
| `OgreBotAPI:SetCS_NPC` | does nothing | `OgreBotAPI.CampSpot:SetLocAtAngleFromActor` `[fw,angle,nameOrId,dist,skipIfAggro,includeNpcSize=TRUE]` | ⚠️ Arguments changed | The for-who is now argument 0 - the Classic call had none (it acted on the session running it). Put `all` first: a script's own call only runs on the session running it, so that keeps it. was a dead stub; `:SetLocAtAngleFromActor` is the working port. |
| `OgreBotAPI:SetCS_NPC_ForWho` | does nothing | `OgreBotAPI.CampSpot:SetLocAtAngleFromActor` `[fw,angle,nameOrId,dist,skipIfAggro,includeNpcSize=TRUE]` | ✏️ Renamed | Angle 0 = behind the actor, 180 = in front (as Classic). The extra last argument (include the NPC's size in the distance) defaults to TRUE. |
| `OgreBotAPI:SetCS_PositionNPC` | does nothing | `OgreBotAPI.CampSpot:SetLocByRole` `[fw,nameOrId,dist,skipIfAggro]` | ✏️ Renamed |  |

## Camp-spot console commands

What you type after `oc !c` / `oc !ci`.

**Note A** (4 rows below): An alias of `-ChangeCampSpot` - it works as typed.

**Note B** (3 rows below): An alias of `-CS_Set_ChangeCampSpotBy` - it works as typed.

| You typed | Today | Type instead | What changed | Notes |
|---|---|---|---|---|
| `-campspot` | works | — | ✅ Works as is |  |
| `-ccs` | runs, arguments mean something else | `-ChangeCampSpot` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-ccs <x> <y> <z> (or one x,y,z token)`<br>**New:** `-ccs <fw> <x> <y> <z>`<br>… |
| `-ccsb` | works | — | ✅ Works as is |  |
| `-ccsbfw` | works | — | ✅ Works as is | Note B |
| `-ccsbw` | works | — | ✅ Works as is | Note B |
| `-ccsbyforwho` | works | — | ✅ Works as is | Note B |
| `-ccsfw` | works | — | ✅ Works as is | Note A |
| `-ccsw` | works | — | ✅ Works as is | Note A |
| `-Change_CampSpot` | runs, arguments mean something else | `-ChangeCampSpot` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-Change_CampSpot <x> <y> <z> (or one x,y,z token)`<br>**New:** `-Change_CampSpot <fw> <x> <y> <z>`<br>… |
| `-Change_Campspot_Who` | works | — | ✅ Works as is | Note A |
| `-ChangeCampSpot` | runs, arguments mean something else | `-ChangeCampSpot` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-ChangeCampSpot <x> <y> <z> (or one x,y,z token)`<br>**New:** `-ChangeCampSpot <fw> <x> <y> <z>`<br>… |
| `-ChangeCampSpotBy` | works | — | ✅ Works as is | An alias of `-ccsb` - it works as typed. |
| `-ChangeCampSpotWho` | works | — | ✅ Works as is | Note A |
| `-cs` | works | — | ✅ Works as is | An alias of `-campspot` - it works as typed. |
| `-cs-circle` | works | — | ✅ Works as is | An alias of `-CS_Set_Formation_Circle` - it works as typed. |
| `-cs-monkey` | works | — | ✅ Works as is | An alias of `-CS_Set_Formation_MonkeyInMiddle` - it works as typed. |
| `-cs-monkeyRaid` | works | — | ✅ Works as is | An alias of `-CS_Set_Formation_MonkeyInMiddleRaid` - it works as typed. |
| `-cs-set-ccs-by` | works | — | ✅ Works as is | An alias of `-ccsb` - it works as typed. |
| `-cs-set-cs` | works | — | ✅ Works as is | An alias of `-campspot` - it works as typed. |
| `-CS_ClearAll` | works | — | ✅ Works as is |  |
| `-CS_ClearCampSpot` | works | — | ✅ Works as is |  |
| `-CS_ClearRelative` | works | — | ✅ Works as is |  |
| `-CS_Set_ChangeCampSpot` | works | — | ✅ Works as is |  |
| `-CS_Set_ChangeCampSpotBy` | works | — | ✅ Works as is |  |
| `-CS_Set_ChangeRelativeCampSpotBy` | works | — | ✅ Works as is |  |
| `-CS_Set_Formation_Circle` | works | — | ✅ Works as is |  |
| `-CS_Set_Formation_MonkeyInMiddle` | works | — | ✅ Works as is |  |
| `-CS_Set_Formation_MonkeyInMiddleRaid` | works | — | ✅ Works as is |  |
| `-CS_Set_HowClose` | works | — | ✅ Works as is |  |
| `-CS_Set_HowFar` | works | — | ✅ Works as is |  |
| `-CS_Set_Relative` | works | — | ✅ Works as is |  |
| `-letsgo` | works | — | ✅ Works as is |  |
| `-Set_CampSpotJump_Handle` | works | — | ✅ Works as is |  |
| `-SetCS_BehindNPC` | works | — | ✅ Works as is |  |
| `-SetCS_InFrontNPC` | works | — | ✅ Works as is |  |
| `-SetCS_NPC` | works | — | ✅ Works as is |  |
| `-SetCS_PositionNPC` | works | — | ✅ Works as is |  |

## Camp spot jump (Obj_CampSpotJump)

Classic's jump-route helper. In the new bot the route runs inside the bot (`OgreBotAPI.Movement:JumpRoute`).

**Note A** (5 rows below): Nothing to convert: this was the old jump script's own bookkeeping. The new jump route (OgreBotAPI.Movement:JumpRoute) keeps it inside the bot, and no Classic script ever read it.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `Obj_CampSpotJump.Active` | reads NULL | `jumpRoute` | 📄 In a data file now | A script that must know when a route ends can attach to CampSpotJump_Completed instead. |
| `Obj_CampSpotJump.bActive` | reads NULL | `jumpRoute` | 📄 In a data file now | Reading it: `{"jumpRoute":{"is":"running"}}`. Writing FALSE (to stop a route) is OgreBotAPI.Movement:StopJumpRoute[&lt;forwho&gt;]. Scripts can also attach to CampSpotJump_Completed, which now fires when a route ends. |
| `Obj_CampSpotJump.bDebugMode` | reads NULL | — | ⛔ Removed | Classic - the jump script's own debug-echo switch (object scope). Not an API; the new route runner logs through the bot log. |
| `Obj_CampSpotJump:CampSpotJump_Completed` | does nothing | — | ⛔ Removed | Nothing to convert: an empty example method in the old jump script. The CampSpotJump_Completed EVENT itself does fire in the new bot - see its own row. |
| `Obj_CampSpotJump.CompletedPoint` | reads NULL | — | ⛔ Removed | Note A |
| `Obj_CampSpotJump.EndPoint` | reads NULL | — | ⛔ Removed | Note A |
| `CampSpotJump_Completed` | never fires | `CampSpotJump_Completed` | ⚠️ Arguments changed | It fires now, with 2 arguments: method MyHandler(string result, string why). A 0-parameter atom still attaches; it just ignores them. |
| `Obj_CampSpotJump:Handle` | does nothing | `OgreBotAPI.Movement:JumpRoute` | ⚠️ Arguments changed | The for-who is new as argument 0 (Classic's object acted on the session that called it, so use ${Me.Name}). Completed may be "". The loop half (`function Handle`) has no call: the runtime is always there, and the `ogre campspotjump` word is retired. JumpDistance / MaxTimer are no longer sticky object settings - pass them as flags on this call. |
| `Obj_CampSpotJump:HandleAdvanced` | does nothing | `OgreBotAPI.Movement:JumpRoute` | ⚠️ Arguments changed | The for-who is argument 0; each flag and each value is its own argument. An unknown flag refuses the whole route where Classic ignored it. |
| `Obj_CampSpotJump:Initalize` | does nothing | automatic (no call) | ➡️ Lives somewhere else | Nothing to call: the event is registered by the new bot. Attach your own atom to CampSpotJump_Completed. |
| `Obj_CampSpotJump.JumpDistance` | reads NULL | `OgreBotAPI.Movement:JumpRoute` | ➡️ Lives somewhere else | Per route, not sticky: pass `-JumpDistance`,`N` as two arguments after the four points on each JumpRoute call. |
| `Obj_CampSpotJump.JumpPoint` | reads NULL | — | ⛔ Removed | Note A |
| `Obj_CampSpotJump.MaxTimer` | reads NULL | `OgreBotAPI.Movement:JumpRoute` | ➡️ Lives somewhere else | Per route, not sticky: pass `-MaxTimer`,`N` on each JumpRoute call. |
| `Obj_CampSpotJump:Set_JumpDistance` | does nothing | `OgreBotAPI.Movement:JumpRoute` | ➡️ Lives somewhere else | Fold it into the route: OgreBotAPI.Movement:JumpRoute[&lt;fw&gt;,start,jump,end,"","-JumpDistance","1"]. |
| `Obj_CampSpotJump:Set_MaxTimer` | does nothing | `OgreBotAPI.Movement:JumpRoute` | ➡️ Lives somewhere else | Fold it into the route call as `-MaxTimer`,`N`. |
| `Obj_CampSpotJump.StartPoint` | reads NULL | — | ⛔ Removed | Note A |
| `Obj_CampSpotJump:Stop` | does nothing | `OgreBotAPI.Movement:StopJumpRoute` | ⚠️ Arguments changed | The for-who is new as argument 0. |
| `Obj_CampSpotJump.Timer_MaxTimer` | reads NULL | — | ⛔ Removed | Note A |
