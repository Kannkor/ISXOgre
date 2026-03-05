# OgreBotAPI Reference

The `OgreBotAPI` is the primary interface for interacting with OgreBot from Instance Controller scripts and other automation. It provides methods, members, and functions for controlling bot behavior, casting abilities, movement, UI manipulation, and more.

This reference covers every available method, member, and function on the `OgreBotAPI` object. Use it as a comprehensive lookup when writing encounter modules, instance controllers, or any OgreBot automation script.

---

## Usage Pattern

```lavishscript
OgreBotAPI:MethodName["param1", param2, ...]
${OgreBotAPI.MemberName[param1]}
```

## The _ForWho Parameter

Most methods accept a `_ForWho` parameter that controls which characters execute the command:

| Target | Description |
|--------|-------------|
| `"all"` | All characters in the group |
| `"${Me.Name}"` | Only the current character |
| `"fighter"` / `"healer"` / `"scout"` / `"mage"` | By archetype |
| `"notfighter"` | Everyone except fighters |
| `"igw:CharName"` | Everyone in group with the specified character |
| `"is1"` | Only session 1 |

> **:bulb: Tip**
>
> For a complete breakdown of targeting options including class-specific filters, raid targeting, and the `igw:` prefix system, see the `_ForWho` examples throughout this page.

---

## Methods - Categorized

### Movement & Positioning

| Method | Description | Example |
|--------|-------------|---------|
| `Come2Me(string _MoveTo="${Me.Name}", string _ForWho="all", float _Precision=3)` | Move group to player | `OgreBotAPI:Come2Me["${Me.Name}", "all"]` |
| `Move2Area(float _XPos, float _YPos, string _ForWho, float _Precision=3)` | Move to area | `OgreBotAPI:Move2Area[100.5, -50.3, "all"]` |
| `ChangeCampSpot(float _X, float _Y, float _Z)` | Change camp spot location | `OgreBotAPI:ChangeCampSpot[100.5, 25.0, -50.3]` |
| `ChangeCampSpotWho(string _ForWho, float _X, float _Y, float _Z)` | Change camp spot for specific players | `OgreBotAPI:ChangeCampSpotWho["fighter", 100.5, 25.0, -50.3]` |
| `FaceActor(string _ForWho, string _ActorNameID)` | Face towards an actor | `OgreBotAPI:FaceActor["all", "Boss Name"]` |
| `FaceLoc(string _ForWho, float _X, float _Y, float _Z)` | Face towards a location | `OgreBotAPI:FaceLoc["all", 100.5, 25.0, -50.3]` |
| `FaceAngle(string _ForWho, int _Angle)` | Face a specific angle | `OgreBotAPI:FaceAngle["all", 180]` |
| `SetCS_PositionNPC(string _ForWho, string _NameOrID, float _Distance=3, bool _SkipIfAggro=FALSE)` | Set camp spot positions relative to NPC | `OgreBotAPI:SetCS_PositionNPC["all", "Boss Name", 5]` |
| `SetCS_BehindNPC(string _ForWho, string _NameOrID, float _Distance=3, bool _SkipIfAggro=FALSE)` | Set camp spot behind NPC | `OgreBotAPI:SetCS_BehindNPC["notfighter", "Boss Name", 5]` |
| `SetCS_InFrontNPC(string _ForWho, string _NameOrID, float _Distance=3, bool _SkipIfAggro=FALSE)` | Set camp spot in front of NPC | `OgreBotAPI:SetCS_InFrontNPC["fighter", "Boss Name", 3]` |
| `SetCS_NPC(int _Angle, string _NameOrID, float _Distance=3, bool _SkipIfAggro=FALSE)` | Set camp spot at angle from NPC | `OgreBotAPI:SetCS_NPC[90, "Boss Name", 5]` |
| `PulseCircleMovement(point3f _Loc, ... Args)` | Circular movement pattern around location ([Args](#pulsecirclemovement-args)) | `OgreBotAPI:PulseCircleMovement["100.0,25.0,-50.0", "-spots", 8, "-distance", 4.5]` |
| `Waypoint(string _ForWho, float _X, float _Y, float _Z)` | Set waypoint | `OgreBotAPI:Waypoint["all", 100.5, 25.0, -50.3]` |
| `Jump(string _ForWho)` | Jump command | `OgreBotAPI:Jump["all"]` |
| `Crouch(string _ForWho)` | Crouch toggle | `OgreBotAPI:Crouch["all"]` |
| `AutoRun(string _ForWho)` | Toggle autorun | `OgreBotAPI:AutoRun["all"]` |
| `FlyUp(string _ForWho)` | Fly upward | `OgreBotAPI:FlyUp["all"]` |
| `FlyDown(string _ForWho)` | Fly downward | `OgreBotAPI:FlyDown["all"]` |
| `FlyStop(string _ForWho)` | Stop flying | `OgreBotAPI:FlyStop["all"]` |
| `LandFlyingMount(string _ForWho)` | Land a flying mount | `OgreBotAPI:LandFlyingMount["all"]` |
| `Stand(string _ForWho)` | Stand up (cancel feign death) | `OgreBotAPI:Stand["all"]` |
| `Move2AreaNoTarget(float _XPos, float _YPos, string _ForWho, float _Precision=3)` | Move to area without changing target | `OgreBotAPI:Move2AreaNoTarget[100.5, -50.3, "all"]` |
| `SetCS_NPC_ForWho(string _ForWho, int _Angle, string _NameOrID, float _Distance=3, bool _SkipIfAggro=FALSE)` | Set camp spot at angle from NPC for specific players | `OgreBotAPI:SetCS_NPC_ForWho["fighter", 90, "Boss Name", 5]` |
| `CampSpot(string _ForWho, float _MinDistance=2, float _MaxDistance=200)` | Update camp spot min/max distances | `OgreBotAPI:CampSpot["all", 2, 200]` |
| `CCS(string _ForWho, float _X, float _Y, float _Z, uint _RoomID=0)` | Change camp spot with RoomID | `OgreBotAPI:CCS["all", 100.5, 25.0, -50.3, 0]` |
| `CRCS(string _ForWho, float _X, float _Y, float _Z, uint _RoomID=0)` | Change relative camp spot | `OgreBotAPI:CRCS["all", 5.0, 0.0, 3.0, 0]` |
| `ClearRCS(string _ForWho)` | Clear relative camp spot | `OgreBotAPI:ClearRCS["all"]` |
| `EQ2Loc_Add(float _X, float _Y, float _Z, string _Label, uint _RoomID=0)` | Add a named EQ2 location marker | `OgreBotAPI:EQ2Loc_Add[100.5, 25.0, -50.3, "BossSpot", 0]` |
| `EQ2Loc_P(string _Label)` | Print/display a named EQ2 location | `OgreBotAPI:EQ2Loc_P["BossSpot"]` |
| `EQ2Loc_Delete(string _Label)` | Delete a named EQ2 location | `OgreBotAPI:EQ2Loc_Delete["BossSpot"]` |
| `OFolIncDistance(string _ForWho)` | Increase follow distance | `OgreBotAPI:OFolIncDistance["all"]` |
| `OFolDecDistance(string _ForWho)` | Decrease follow distance | `OgreBotAPI:OFolDecDistance["all"]` |
| `Set_CampSpotJump_Handle(string _ForWho, point3f _Start, point3f _Jump, point3f _End, point3f _Completed, ... Args)` | Set campspot jump waypoints ([Args](#set_campspotjump_handle-args)) | `OgreBotAPI:Set_CampSpotJump_Handle["all", "0,0,0", "5,5,5", "10,0,10", "10,0,10"]` |

### Combat Control

| Method | Description | Example |
|--------|-------------|---------|
| `CastAbility(string _ForWho, string AbilityName, string CalledFrom="OgreBotAPI")` | Cast an ability | `OgreBotAPI:CastAbility["all", "Divine Arbitration"]` |
| `CastAbilityOnPlayer(string _ForWho, string AbilityName, string sTarget)` | Cast ability on specific player | `OgreBotAPI:CastAbilityOnPlayer["healer", "Heal", "TankName"]` |
| `CastAbilityOnNPC(string _ForWho, string AbilityName, string _MobNameID, string _CalledFrom)` | Cast ability on NPC | `OgreBotAPI:CastAbilityOnNPC["all", "Taunt", "Boss Name", "IC"]` |
| `CastAbilityInSeconds(string _ForWho, string AbilityName, float _Seconds, string CalledFrom)` | Cast ability after delay | `OgreBotAPI:CastAbilityInSeconds["all", "Ward", 5.0, "IC"]` |
| `CastAbilityNoChecks(string _ForWho, string AbilityName, string CalledFrom)` | Cast without readiness checks | `OgreBotAPI:CastAbilityNoChecks["all", "Emergency Heal", "IC"]` |
| `CastAbilityNoExport(string _ForWho, string _Ability, string _CastFrom)` | Cast without triggering export | `OgreBotAPI:CastAbilityNoExport["all", "Buff", "IC"]` |
| `CastAbilityNoExportUntilCast(string _ForWho, string _Ability, string _CastFrom)` | Cast without export until casting starts | `OgreBotAPI:CastAbilityNoExportUntilCast["all", "Buff", "IC"]` |
| `CastAbilityOnPlayerInSeconds(string _ForWho, string AbilityName, string sTarget, float _Seconds)` | Cast ability on player after delay | `OgreBotAPI:CastAbilityOnPlayerInSeconds["healer", "Heal", "TankName", 3.0]` |
| `CastAbilityOnPlayerNoChecks(string _ForWho, string AbilityName, string OnPlayer, string CalledFrom)` | Cast on player without readiness checks | `OgreBotAPI:CastAbilityOnPlayerNoChecks["healer", "Emergency Heal", "TankName", "IC"]` |
| `CastAbilityType(string _ForWho, string AbilityType, string CalledFrom, ... Args)` | Cast by ability type ([Args](#castabilitytype-args)) | `OgreBotAPI:CastAbilityType["healer", "cure", "IC", "-NPCRequired"]` |
| `CastRescue(string _ForWho, string CalledFrom, ... Args)` | Cast rescue ability ([Args](#castrescue-args)) | `OgreBotAPI:CastRescue["fighter", "IC", "-NPCRequired"]` |
| `CastHOIconID(string _ForWho, int _IconID, string CalledFrom)` | Cast ability by HO icon ID | `OgreBotAPI:CastHOIconID["all", 1234, "IC"]` |
| `CastBulwarkImmediately(string _ForWho)` | Cast bulwark immediately | `OgreBotAPI:CastBulwarkImmediately["fighter"]` |
| `Cast_Interrupt(string _ForWho, string _MobNameID, string _CalledFrom, ... Args)` | Cast interrupt on target ([Args](#cast_interrupt-args)) | `OgreBotAPI:Cast_Interrupt["all", "Boss Name", "IC"]` |
| `UseItem(string _ForWho, string AbilityName)` | Use an item ability | `OgreBotAPI:UseItem["all", "Totem of the Otter"]` |
| `UseItemOnPlayer(string _ForWho, string AbilityName, string sTarget)` | Use item on player | `OgreBotAPI:UseItemOnPlayer["all", "Cure Potion", "TankName"]` |
| `CancelCasting(string _ForWho, ... Args)` | Cancel current casting ([Args](#cancelcasting-args)) | `OgreBotAPI:CancelCasting["all"]` |
| `CancelCurrentCast(string _ForWho, bool _TorF=TRUE)` | Cancel current cast | `OgreBotAPI:CancelCurrentCast["all", TRUE]` |
| `CancelMaintained(... Args)` | Cancel maintained spell ([Args](#cancelmaintained-args)) | `OgreBotAPI:CancelMaintained["Buff A", "Buff B"]` |
| `CancelMaintainedForWho(string _ForWho, ... Args)` | Cancel maintained for specific players ([Args](#cancelmaintainedforwho-args)) | `OgreBotAPI:CancelMaintainedForWho["all", "Buff A", "Buff B"]` |
| `Pull(string _ForWho, bool _Named=FALSE)` | Pull mob | `OgreBotAPI:Pull["fighter", TRUE]` |
| `PetAttack(string _ForWho)` | Pet attack command | `OgreBotAPI:PetAttack["all"]` |
| `PetAssist(string _ForWho)` | Pet assist command | `OgreBotAPI:PetAssist["all"]` |
| `PetOff(string _ForWho)` | Pet passive/off | `OgreBotAPI:PetOff["all"]` |
| `PetGetLost(string _ForWho)` | Dismiss pet | `OgreBotAPI:PetGetLost["all"]` |
| `Evac(string _ForWho)` | Evacuate | `OgreBotAPI:Evac["all"]` |
| `Res(string _ForWho)` | Resurrect group | `OgreBotAPI:Res["healer"]` |
| `StopRes(string _ForWho)` | Stop resurrection attempts | `OgreBotAPI:StopRes["all"]` |
| `ImmRes(int _HowMany=2)` | Immediate resurrect | `OgreBotAPI:ImmRes[2]` |
| `Revive(string _ForWho, string _Option=0, bool _ExactMatch=FALSE)` | Revive at location | `OgreBotAPI:Revive["all"]` |
| `Assist(string _AssistWho, string _ForWho)` | Assist another player | `OgreBotAPI:Assist["TankName", "all"]` |
| `AssistForWho(string _ForWho, string _AssistWho)` | Set assist target | `OgreBotAPI:AssistForWho["all", "TankName"]` |
| `Target(string _ForWho, string _Target)` | Target an actor | `OgreBotAPI:Target["all", "Boss Name"]` |
| `NoTarget(string _ForWho)` | Clear target | `OgreBotAPI:NoTarget["all"]` |
| `TargetAndDoubleClickActor(string _ForWho, int64 _ActorID)` | Target and interact with actor | `OgreBotAPI:TargetAndDoubleClickActor["all", ${Actor[namednpc,"NPC Name"].ID}]` |

### Combat Settings

| Method | Description | Example |
|--------|-------------|---------|
| `Pause(string _ForWho)` | Pause combat | `OgreBotAPI:Pause["all"]` |
| `Resume(string _ForWho)` | Resume combat | `OgreBotAPI:Resume["all"]` |
| `NoCasting(string _ForWho, bool _TorF=TRUE)` | Disable/enable casting | `OgreBotAPI:NoCasting["all", TRUE]` |
| `Enable_Cures(string _ForWho)` | Enable curing | `OgreBotAPI:Enable_Cures["all"]` |
| `Disable_Cures(string _ForWho)` | Disable curing | `OgreBotAPI:Disable_Cures["all"]` |
| `Enable_Dispells(string _ForWho)` | Enable dispelling | `OgreBotAPI:Enable_Dispells["all"]` |
| `Disable_Dispells(string _ForWho)` | Disable dispelling | `OgreBotAPI:Disable_Dispells["all"]` |
| `Enable_Stuns(string _ForWho)` | Enable stuns | `OgreBotAPI:Enable_Stuns["all"]` |
| `Disable_Stuns(string _ForWho)` | Disable stuns | `OgreBotAPI:Disable_Stuns["all"]` |
| `Enable_Interrupts(string _ForWho)` | Enable interrupts | `OgreBotAPI:Enable_Interrupts["all"]` |
| `Disable_Interrupts(string _ForWho)` | Disable interrupts | `OgreBotAPI:Disable_Interrupts["all"]` |
| `Set_DisableAllAOEs(string _ForWho, bool _DisableAEs=TRUE, ... Args)` | Disable AOE abilities ([Args](#set_disableallaoes-args)) | `OgreBotAPI:Set_DisableAllAOEs["all", TRUE, "-allowcounters"]` |
| `SetNoDefensive(string _ForWho, bool _Value=TRUE)` | Disable defensive abilities | `OgreBotAPI:SetNoDefensive["all", TRUE]` |
| `AddNoOffensiveOn(string _ForWho, string _MobName, bool _ExactMatchOnly=FALSE)` | Add mob to no-offensive list | `OgreBotAPI:AddNoOffensiveOn["all", "Friendly NPC"]` |
| `RemoveNoOffensiveOn(string _ForWho, string _MobName)` | Remove from no-offensive list | `OgreBotAPI:RemoveNoOffensiveOn["all", "Friendly NPC"]` |
| `ClearNoOffensiveOn(string _ForWho)` | Clear no-offensive list | `OgreBotAPI:ClearNoOffensiveOn["all"]` |
| `SetNoReqBowAbilities(string _ForWho, bool _Value=TRUE)` | Set no-ranged requirements | `OgreBotAPI:SetNoReqBowAbilities["all", TRUE]` |
| `JoustOut(string _ForWho)` | Joust out of range | `OgreBotAPI:JoustOut["all"]` |
| `JoustIn(string _ForWho)` | Joust into range | `OgreBotAPI:JoustIn["all"]` |
| `JoustOff(string _ForWho="Casters")` | Disable jousting | `OgreBotAPI:JoustOff["Casters"]` |
| `JoustOn(string _ForWho="Melee")` | Enable jousting | `OgreBotAPI:JoustOn["Melee"]` |
| `NoMove(string _ForWho)` | Disable movement | `OgreBotAPI:NoMove["all"]` |
| `ForceFollow(string _ForWho)` | Force follow | `OgreBotAPI:ForceFollow["all"]` |
| `LetsGo(string _ForWho)` | Start following/movement | `OgreBotAPI:LetsGo["all"]` |
| `HoldUp(string _ForWho)` | Stop and hold | `OgreBotAPI:HoldUp["all"]` |
| `Update_Turbo(string _ForWho, int _Turbo=300, bool _bIgnoreLimits=FALSE)` | Update turbo/speed setting | `OgreBotAPI:Update_Turbo["all", 300]` |
| `Rebuff(string _ForWho)` | Trigger rebuff | `OgreBotAPI:Rebuff["all"]` |
| `LoadProfile(string _ForWho, string sProfileName, string _LoadOnlyTab="")` | Load a bot profile | `OgreBotAPI:LoadProfile["all", "MyProfile"]` |
| `NPC_CastMonitoring(string _ForWho, ... Args)` | Enable NPC cast monitoring ([Args](#npc_castmonitoring-args)) | `OgreBotAPI:NPC_CastMonitoring["all", "-radius", 40, "Boss Name"]` |
| `VampiricRequiem_AbilityCancel(string _ForWho, ... Args)` | Cancel Vampiric Requiem abilities | `OgreBotAPI:VampiricRequiem_AbilityCancel["all"]` |
| `Set_VampiricRequiem_Cancelling_Active(string _ForWho, int _Time=10)` | Set Vampiric Requiem cancel duration | `OgreBotAPI:Set_VampiricRequiem_Cancelling_Active["all", 10]` |
| `ScrollOf(string _ForWho, string _ScrollName="Prowess", int _CancelIfDurationLessThan=0, bool _UseBest=FALSE)` | Use a Scroll ability | `OgreBotAPI:ScrollOf["all", "Prowess"]` |
| `ResolveBuffCheck(string _ForWho)` | Check and apply resolve buffs | `OgreBotAPI:ResolveBuffCheck["all"]` |
| `Heartstone_RekindleBond(string _ForWho)` | Use Heartstone to rekindle bond | `OgreBotAPI:Heartstone_RekindleBond["all"]` |
| `AbilityTracker_Add(string _ForWho, string _AbilityName)` | Add ability to the ability tracker | `OgreBotAPI:AbilityTracker_Add["all", "Ability Name"]` |

### Heroic Opportunity (HO)

| Method | Description | Example |
|--------|-------------|---------|
| `HO_Start(string _ForWho, ... Args)` | Start a Heroic Opportunity ([Args](#ho_start-args)) | `OgreBotAPI:HO_Start["all"]` |
| `HO_Starter(string _ForWho)` | HO starter ability | `OgreBotAPI:HO_Starter["fighter"]` |
| `HO_Starter_Advance(string _ForWho)` | Advance HO starter | `OgreBotAPI:HO_Starter_Advance["all"]` |
| `HO_Advance(string _ForWho)` | Advance HO wheel | `OgreBotAPI:HO_Advance["all"]` |
| `HO_Wheel_Advance(string _ForWho)` | Advance HO wheel specifically | `OgreBotAPI:HO_Wheel_Advance["all"]` |
| `HO_Cancel_Starter(string _ForWho, string _CalledFrom)` | Cancel HO starter | `OgreBotAPI:HO_Cancel_Starter["all", "IC"]` |
| `DoHO_Reset(string _ForWho)` | Reset HO system | `OgreBotAPI:DoHO_Reset["all"]` |
| `DoHO_Setup(string _ForWho, ... Args)` | Setup HO parameters ([Args](#doho_setup-args)) | `OgreBotAPI:DoHO_Setup["all"]` |
| `DoHO_Set_Enable(string _ForWho, bool _TorF, ... Args)` | Enable/disable HO ([Args](#doho_set_enable-args)) | `OgreBotAPI:DoHO_Set_Enable["all", TRUE]` |
| `Set_Allow_HOICon(string _ForWho, int _VariableName)` | Allow specific HO icon | `OgreBotAPI:Set_Allow_HOICon["all", 1234]` |
| `Clear_Allow_HOICon(string _ForWho, int _VariableName)` | Clear allowed HO icon | `OgreBotAPI:Clear_Allow_HOICon["all", 1234]` |
| `Clear_Allow_HOICons(string _ForWho)` | Clear all allowed HO icons | `OgreBotAPI:Clear_Allow_HOICons["all"]` |
| `Set_Disable_HOICon(string _ForWho, int _VariableName)` | Disable specific HO icon | `OgreBotAPI:Set_Disable_HOICon["all", 1234]` |
| `Clear_Disable_HOICon(string _ForWho, int _VariableName)` | Clear disabled HO icon | `OgreBotAPI:Clear_Disable_HOICon["all", 1234]` |
| `Clear_Disable_HOICons(string _ForWho)` | Clear all disabled HO icons | `OgreBotAPI:Clear_Disable_HOICons["all"]` |

### Cures & Curses

| Method | Description | Example |
|--------|-------------|---------|
| `Cursed(string _ForWho, string _Toon, ... Args)` | Handle cursed player ([Args](#cure-method-args)) | `OgreBotAPI:Cursed["healer", "TankName"]` |
| `AutoCurse(string _ForWho, string _Toon, ... Args)` | Auto-cure curses ([Args](#cure-method-args)) | `OgreBotAPI:AutoCurse["healer", "TankName"]` |
| `AutoCure(string _ForWho, string _Toon, ... Args)` | Auto-cure ailments ([Args](#cure-method-args)) | `OgreBotAPI:AutoCure["healer", "TankName"]` |
| `AutoItemCure(string _ForWho, ... Args)` | Auto-cure using items ([Args](#cure-method-args)) | `OgreBotAPI:AutoItemCure["all"]` |
| `AutoGroupCure(string _ForWho, string _Toon, ... Args)` | Auto group cure ([Args](#cure-method-args)) | `OgreBotAPI:AutoGroupCure["healer", "TankName"]` |
| `GroupCure(string _ForWho)` | Cast group cure | `OgreBotAPI:GroupCure["healer"]` |
| `CancelDetrimental(string _ForWho, int _BackDropID, int _MainID)` | Cancel detrimental effect | `OgreBotAPI:CancelDetrimental["all", 110, 55]` |
| `Dispell(string _ForWho, string _Value)` | Dispell target | `OgreBotAPI:Dispell["all", "Boss Name"]` |
| `DispellNPCWithSpell(string _ForWho, string _NPCNameOrID)` | Dispell NPC with spell | `OgreBotAPI:DispellNPCWithSpell["all", "Boss Name"]` |
| `DispellNPCWithItem(string _ForWho, string _NPCNameOrID)` | Dispell NPC with item | `OgreBotAPI:DispellNPCWithItem["all", "Boss Name"]` |
| `DispellNPCWithAny(string _ForWho, string _NPCNameOrID)` | Dispell NPC with any method | `OgreBotAPI:DispellNPCWithAny["all", "Boss Name"]` |

### Auto-Target System

| Method | Description | Example |
|--------|-------------|---------|
| `AutoTarget_AddActor(string _ForWho, string _ActorName, int _HP=0, bool _CheckCollision=FALSE, bool _AggroOnGroupOnly=TRUE, int _MaxHP=0, bool _AggroOnNonFighterOnly=FALSE, bool _AggroOnNotMe=FALSE)` | Add actor to auto-target list | `OgreBotAPI:AutoTarget_AddActor["all", "Add Name", 75]` |
| `AutoTarget_RemoveActor(string _ForWho, string _ActorName)` | Remove actor from list | `OgreBotAPI:AutoTarget_RemoveActor["all", "Add Name"]` |
| `AutoTarget_ClearActors(string _ForWho)` | Clear auto-target actors | `OgreBotAPI:AutoTarget_ClearActors["all"]` |
| `AutoTarget_Clear(string _ForWho)` | Clear entire auto-target system | `OgreBotAPI:AutoTarget_Clear["all"]` |
| `AutoTarget_Enable(string _ForWho, string _Key="")` | Enable auto-targeting | `OgreBotAPI:AutoTarget_Enable["all"]` |
| `AutoTarget_Disable(string _ForWho, string _Key="")` | Disable auto-targeting | `OgreBotAPI:AutoTarget_Disable["all"]` |
| `AutoTarget_SetScanRadius(string _ForWho, int _Value=50)` | Set scan radius | `OgreBotAPI:AutoTarget_SetScanRadius["all", 75]` |
| `AutoTarget_SetScanHeight(string _ForWho, int _Value=5)` | Set scan height | `OgreBotAPI:AutoTarget_SetScanHeight["all", 10]` |
| `AutoTarget_SetRescanTime(string _ForWho, int _Value=50)` | Set rescan interval | `OgreBotAPI:AutoTarget_SetRescanTime["all", 30]` |

### Variables & Internal State

| Method | Description | Example |
|--------|-------------|---------|
| `Set_Variable(string _ForWho, string _VariableName, string _VariableValue)` | Set a custom variable | `OgreBotAPI:Set_Variable["all", "phase", "2"]` |
| `Get_Variable(string _VariableName)` | Get custom variable value (member) | `${OgreBotAPI.Get_Variable["phase"]}` |
| `Clear_Variable(string _ForWho, string _VariableName)` | Clear a variable | `OgreBotAPI:Clear_Variable["all", "phase"]` |
| `Clear_Variables(string _ForWho)` | Clear all variables | `OgreBotAPI:Clear_Variables["all"]` |
| `Set_InternalVariable(string _ForWho, string _VariableName, string _VariableValue)` | Set internal variable | `OgreBotAPI:Set_InternalVariable["all", "myVar", "value"]` |
| `Get_InternalVariable(string _VariableName)` | Get internal variable (member) | `${OgreBotAPI.Get_InternalVariable["myVar"]}` |
| `Clear_InternalVariable(string _ForWho, string _VariableName)` | Clear internal variable | `OgreBotAPI:Clear_InternalVariable["all", "myVar"]` |
| `Clear_InternalVariables(string _ForWho)` | Clear all internal variables | `OgreBotAPI:Clear_InternalVariables["all"]` |
| `Spew_Variables()` | Debug output all variables | `OgreBotAPI:Spew_Variables` |
| `Spew_InternalVariables()` | Debug output internal variables | `OgreBotAPI:Spew_InternalVariables` |

### Zone & Travel

| Method | Description | Example |
|--------|-------------|---------|
| `Zone(string _ForWho)` | Zone through door | `OgreBotAPI:Zone["all"]` |
| `ZoneDoor(string _DoorOption=1)` | Zone through specific door | `OgreBotAPI:ZoneDoor[1]` |
| `ZoneDoorForWho(string _ForWho, string _DoorOption=1)` | Zone door for specific players | `OgreBotAPI:ZoneDoorForWho["all", 1]` |
| `ZoneInto(string _ForWho, string _ZoneName, string _ActorName, int _DoorOption=0)` | Zone into specific zone | `OgreBotAPI:ZoneInto["all", "Zone Name", "Door NPC"]` |
| `Travel(string _ForWho, string _ToWhere, bool _ExactMatch=FALSE, string _MultipleZoneOption)` | Travel to location | `OgreBotAPI:Travel["all", "Qeynos Harbor"]` |
| `FastTravel(string _ForWho, string _ToWhere, ... Params)` | Fast travel | `OgreBotAPI:FastTravel["all", "Qeynos Harbor"]` |
| `TravelBell(string _ForWho, string _ToWhere, bool _ExactMatch=FALSE, string _MultipleZoneOption)` | Use travel bell | `OgreBotAPI:TravelBell["all", "Qeynos Harbor"]` |
| `TravelDruid(string _ForWho, string _ToWhere, bool _ExactMatch=FALSE, string _MultipleZoneOption)` | Use druid ring | `OgreBotAPI:TravelDruid["all", "Darklight Wood"]` |
| `TravelSpires(string _ForWho, string _ToWhere, bool _ExactMatch=FALSE, string _MultipleZoneOption)` | Use wizard spires | `OgreBotAPI:TravelSpires["all", "Enchanted Lands"]` |
| `GetToGH(string _ForWho)` | Get to guild hall | `OgreBotAPI:GetToGH["all"]` |
| `CallGH(string _ForWho)` | Call to guild hall | `OgreBotAPI:CallGH["all"]` |
| `GetFlag(string _ForWho)` | Get guild rally flag | `OgreBotAPI:GetFlag["all"]` |
| `UseFlag(string _ForWho)` | Use guild rally flag | `OgreBotAPI:UseFlag["all"]` |
| `PortalToGuildHall(string _ForWho)` | Portal to guild hall | `OgreBotAPI:PortalToGuildHall["all"]` |
| `CoV(string _ForWho, string _TravelOption, string _ToonOption, bool _AllowSameZone)` | Chroma of Valor travel | `OgreBotAPI:CoV["all", "Option1", "all", FALSE]` |
| `ToggleZoneReuse(string _ForWho)` | Toggle zone reuse | `OgreBotAPI:ToggleZoneReuse["all"]` |
| `ResetZone(string _ForWho, string _ZoneName)` | Reset a zone | `OgreBotAPI:ResetZone["all", "Zone Name"]` |
| `ZoneResetAll(string _ForWho)` | Reset all zones | `OgreBotAPI:ZoneResetAll["all"]` |

### Actor Interaction

| Method | Description | Example |
|--------|-------------|---------|
| `Actor_Click(string _ForWho, string _NameOrID, bool _ExactName=FALSE)` | Click on actor | `OgreBotAPI:Actor_Click["all", "NPC Name"]` |
| `Actor_ClickQueued(string _ForWho, string _NameOrID, bool _ExactName=FALSE, int _WaitTime=40)` | Queued actor click | `OgreBotAPI:Actor_ClickQueued["all", "NPC Name", FALSE, 40]` |
| `HailNPC(string _ForWho, string _NameOrID)` | Hail an NPC | `OgreBotAPI:HailNPC["all", "NPC Name"]` |
| `ApplyVerb(string _ActorName, string _Verb)` | Apply verb to actor | `OgreBotAPI:ApplyVerb["Door Name", "open"]` |
| `ApplyVerbID(int64 _ActorID, string _Verb)` | Apply verb by actor ID | `OgreBotAPI:ApplyVerbID[${Actor["Door Name"].ID}, "open"]` |
| `ApplyVerbForWho(string _ForWho, string _ActorName, string _Verb)` | Apply verb for specific players | `OgreBotAPI:ApplyVerbForWho["all", "Door Name", "open"]` |
| `ApplyVerbIDForWho(string _ForWho, int64 _ActorID, string _Verb)` | Apply verb by ID for specific players | `OgreBotAPI:ApplyVerbIDForWho["all", ${Actor["Door"].ID}, "open"]` |
| `ApplyVerbQueuedForWho(string _ForWho, string _ActorName, string _Verb)` | Queued verb application | `OgreBotAPI:ApplyVerbQueuedForWho["all", "NPC Name", "use"]` |
| `ApplyVerbIDQueuedForWho(string _ForWho, int64 _ActorID, string _Verb)` | Queued verb by ID | `OgreBotAPI:ApplyVerbIDQueuedForWho["all", ${Actor["NPC"].ID}, "use"]` |

### Merchant & Economy

| Method | Description | Example |
|--------|-------------|---------|
| `BuyFromMerchant(string _ForWho, string _ItemName, int _Value=1)` | Buy from merchant | `OgreBotAPI:BuyFromMerchant["all", "Healing Potion", 5]` |
| `SellToMerchant(string _ForWho, string _ItemName, int _Value=1)` | Sell to merchant | `OgreBotAPI:SellToMerchant["all", "Junk Item"]` |
| `OpenAndBuyFromMerchant(string _ForWho, string _MerchantName, string _ItemName, int _Value=1)` | Open merchant and buy | `OgreBotAPI:OpenAndBuyFromMerchant["all", "Merchant Name", "Item", 1]` |
| `OpenAndBuyFromMerchantXTimes(string _ForWho, string _MerchantName, string _ItemName, int _Value=1, int _HowManyTimes=1)` | Buy multiple times | `OgreBotAPI:OpenAndBuyFromMerchantXTimes["all", "Merchant", "Item", 1, 5]` |
| `RepairGear(string _ForWho, bool _Force=FALSE)` | Repair gear | `OgreBotAPI:RepairGear["all"]` |

### Quests & Dialogs

| Method | Description | Example |
|--------|-------------|---------|
| `AcceptQuest(string _ForWho, string _QuestName)` | Accept a quest | `OgreBotAPI:AcceptQuest["all", "Quest Name"]` |
| `ForceAcceptQuest(string _ForWho, string _QuestName)` | Force accept quest | `OgreBotAPI:ForceAcceptQuest["all", "Quest Name"]` |
| `DeleteQuest(string _ForWho, string _QuestName)` | Delete a quest | `OgreBotAPI:DeleteQuest["all", "Quest Name"]` |
| `ShareQuest(string _ForWho, string _QuestName)` | Share a quest | `OgreBotAPI:ShareQuest["all", "Quest Name"]` |
| `ShareMission(string _ForWho, string _QuestName)` | Share mission | `OgreBotAPI:ShareMission["all", "Mission Name"]` |
| `ShareAllMissions(string _ForWho)` | Share all missions | `OgreBotAPI:ShareAllMissions["all"]` |
| `ShareQuestsForZone(string _ForWho, string _ZoneName)` | Share quests for zone | `OgreBotAPI:ShareQuestsForZone["all", "Zone Name"]` |
| `CompareQuestUpdate(string _ForWho, string _QuestName, ... _QuestInfo)` | Compare quest progress | `OgreBotAPI:CompareQuestUpdate["all", "Quest Name"]` |
| `ChoiceWindow(string _ForWho, int _Choice=1)` | Click choice window option | `OgreBotAPI:ChoiceWindow["all", 2]` |
| `OK_Button(string _ForWho)` | Click OK button | `OgreBotAPI:OK_Button["all"]` |
| `ReplyDialog(string _ForWho, string _Choice=1)` | Reply to dialog | `OgreBotAPI:ReplyDialog["all", "1"]` |
| `ReplyDialogClose(string _ForWho)` | Close reply dialog | `OgreBotAPI:ReplyDialogClose["all"]` |
| `ConversationBubble(string _ForWho, int _DoorOption=1)` | Click conversation bubble | `OgreBotAPI:ConversationBubble["all", 1]` |
| `ConversationBubbleSpew(string _ForWho)` | Debug output conversation bubble options | `OgreBotAPI:ConversationBubbleSpew["all"]` |
| `Select_Window(string _ForWho, ... Args)` | Select window option ([Args](#select_window-args)) | `OgreBotAPI:Select_Window["all", "-substring", "Accept"]` |
| `Select_Window_Cancel(string _ForWho)` | Cancel select window | `OgreBotAPI:Select_Window_Cancel["all"]` |
| `Select_Window_Spew(string _ForWho)` | Debug select window | `OgreBotAPI:Select_Window_Spew["all"]` |
| `Select_Zone_Version(string _ForWho, string _Option)` | Select zone version | `OgreBotAPI:Select_Zone_Version["all", "Heroic"]` |
| `AcceptReward(string _ForWho, string _Selection=0, int64 _WindowID=0)` | Accept quest reward | `OgreBotAPI:AcceptReward["all"]` |
| `AcceptNoChoiceReward(int64 _WindowID=0)` | Accept reward with no choice | `OgreBotAPI:AcceptNoChoiceReward` |

### Items & Inventory

| Method | Description | Example |
|--------|-------------|---------|
| `DestroyItem(string _ForWho, string _ItemName, uint _Charges=0)` | Destroy item with checks | `OgreBotAPI:DestroyItem["all", "Junk Item"]` |
| `DestroyItem_NoChecks(string _ForWho, string _ItemName)` | Destroy item without checks | `OgreBotAPI:DestroyItem_NoChecks["all", "Junk Item"]` |
| `DestroyItemByID_NoChecks(string _ForWho, int64 _ItemID)` | Destroy item by ID | `OgreBotAPI:DestroyItemByID_NoChecks["all", 123456789]` |
| `ExamineInventoryItem(string _ForWho, string _ItemName)` | Examine item | `OgreBotAPI:ExamineInventoryItem["all", "Item Name"]` |
| `ExamineAllOfItem(string _ForWho, ... _Items)` | Examine all of item type | `OgreBotAPI:ExamineAllOfItem["all", "Item Name"]` |
| `CloseExamine()` | Close examine window | `OgreBotAPI:CloseExamine` |
| `CloseExamineWindow(string _ForWho)` | Close examine window for all | `OgreBotAPI:CloseExamineWindow["all"]` |
| `CloseAllExamine(string _ForWho)` | Close all examine windows | `OgreBotAPI:CloseAllExamine["all"]` |
| `Drink_Alcohol(string _ForWho, string _ItemName)` | Drink alcohol item | `OgreBotAPI:Drink_Alcohol["all", "Ale"]` |
| `Unpack(string _ForWho, string _ItemName, string _UnpackOption)` | Unpack item | `OgreBotAPI:Unpack["all", "Crate", "option1"]` |
| `Unpack_Quantity(string _ForWho, string _ItemName, uint Quantity, string _UnpackOption)` | Unpack quantity | `OgreBotAPI:Unpack_Quantity["all", "Crate", 5, "option1"]` |
| `Unpack_EmpyralStones(string _ForWho, string _Option)` | Unpack Empyral stones | `OgreBotAPI:Unpack_EmpyralStones["all", "option1"]` |
| `Unpack_PlanarStones(string _ForWho, string _Option)` | Unpack Planar stones | `OgreBotAPI:Unpack_PlanarStones["all", "option1"]` |
| `Unpack_Familiars(string _ForWho)` | Unpack familiar crates | `OgreBotAPI:Unpack_Familiars["all"]` |
| `Consume_Familiars(string _ForWho)` | Consume familiars for XP | `OgreBotAPI:Consume_Familiars["all"]` |
| `Unpack_Consume_Familiars(string _ForWho)` | Unpack and consume familiars | `OgreBotAPI:Unpack_Consume_Familiars["all"]` |
| `Consume_Status_Tokens(string _ForWho, uint _Amount)` | Consume status tokens | `OgreBotAPI:Consume_Status_Tokens["all", 100]` |
| `Consume_Status_Ingots(string _ForWho, uint _Amount)` | Consume status ingots | `OgreBotAPI:Consume_Status_Ingots["all", 100]` |
| `ConsumeItems_ProcessList(string _ForWho, ... Args)` | Process consume item list ([Args](#consumeitems_processlist-args)) | `OgreBotAPI:ConsumeItems_ProcessList["all", "-all", "-fc"]` |
| `ConsumeDeityBaubles(string _ForWho)` | Consume deity baubles | `OgreBotAPI:ConsumeDeityBaubles["all"]` |

### Equipment & Adornments

| Method | Description | Example |
|--------|-------------|---------|
| `EquipCharm(string _ForWho, int _Value=1)` | Equip charm | `OgreBotAPI:EquipCharm["all", 1]` |
| `ChangeBeltAdorn(string _ForWho, string _AdornType, bool _Unequip=TRUE, bool _SkipAdornMoving=FALSE)` | Change belt adornment | `OgreBotAPI:ChangeBeltAdorn["all", "War Rune"]` |
| `ApplyTempAdorn(string _ForWho, string _Adorn, string _Slot)` | Apply temporary adornment | `OgreBotAPI:ApplyTempAdorn["all", "Adorn Name", "Primary"]` |
| `PoP_TempAdorns(string _ForWho, string _AdornmentType, bool _Overwrite)` | Apply PoP temp adorns | `OgreBotAPI:PoP_TempAdorns["all", "Type", TRUE]` |
| `CheckGear(string _ForWho, string _ReportIfValueEqualOrLess)` | Check gear condition | `OgreBotAPI:CheckGear["all", "50"]` |
| `Scribe_Empyral(string _ForWho)` | Scribe Empyral spells from inventory | `OgreBotAPI:Scribe_Empyral["all"]` |

### Mount & Familiar

| Method | Description | Example |
|--------|-------------|---------|
| `Mount(string _ForWho)` | Toggle mount | `OgreBotAPI:Mount["all"]` |
| `Force_MountOn(string _ForWho)` | Force mount on | `OgreBotAPI:Force_MountOn["all"]` |
| `Force_MountOff(string _ForWho)` | Force mount off | `OgreBotAPI:Force_MountOff["all"]` |
| `CheckMountTraining(string _ForWho, bool _ForceCheck=FALSE)` | Check mount training | `OgreBotAPI:CheckMountTraining["all"]` |
| `Check_Familiar(string _ForWho)` | Check familiar | `OgreBotAPI:Check_Familiar["all"]` |
| `Summon_Familiar(string _ForWho)` | Summon familiar | `OgreBotAPI:Summon_Familiar["all"]` |

### Communication & Events

| Method | Description | Example |
|--------|-------------|---------|
| `Message(string _ForWho, string _Message, bool _Noise=FALSE, string NoiseToPlay)` | Send message | `OgreBotAPI:Message["all", "Phase 2 starting!"]` |
| `Message_Relay(string _ForWho, string _Message, bool _Noise=FALSE, string NoiseToPlay)` | Relay message | `OgreBotAPI:Message_Relay["all", "Move now!"]` |
| `Message_NT(string _ForWho, string _Message, bool _Noise=FALSE, string NoiseToPlay)` | Message no-throttle | `OgreBotAPI:Message_NT["all", "Urgent message"]` |
| `TTS(string _ForWho, string _Message)` | Text-to-speech | `OgreBotAPI:TTS["all", "Joust out now"]` |
| `Countdown(string _ForWho, int _Time=10)` | Countdown timer | `OgreBotAPI:Countdown["all", 10]` |
| `OnScreenTimer(string _ForWho, float _Time, int _Slot, string _Message, int _MinUpdateTimer, float _ExtraTimer, string _ExtraTimerMessage)` | On-screen timer | `OgreBotAPI:OnScreenTimer["all", 30.0, 1, "Timer"]` |
| `OnScreenTimerReset(string _ForWho, int _Slot)` | Reset on-screen timer | `OgreBotAPI:OnScreenTimerReset["all", 1]` |
| `Announce_AddEntry(string _ForWho, string _Ability, string _AnnounceTo, string _AnnounceText)` | Add announcement | `OgreBotAPI:Announce_AddEntry["all", "Ability", "group", "Casting!"]` |
| `ChatEvent_AddEntry(string _ForWho, string _Text, bool _OC, bool _Ding, string _Code)` | Add chat event | `OgreBotAPI:ChatEvent_AddEntry["all", "trigger text", TRUE, TRUE, "code"]` |
| `ChatEvent_RemoveEntry(string _ForWho, string _Text)` | Remove chat event | `OgreBotAPI:ChatEvent_RemoveEntry["all", "trigger text"]` |
| `SpawnEvent_AddEntry(string _ForWho, string _Text, bool _OC, bool _Ding, string _Code)` | Add spawn event | `OgreBotAPI:SpawnEvent_AddEntry["all", "Add Name", TRUE, TRUE, "code"]` |
| `SpawnEvent_RemoveEntry(string _ForWho, string _Text)` | Remove spawn event | `OgreBotAPI:SpawnEvent_RemoveEntry["all", "Add Name"]` |
| `DespawnEvent_AddEntry(string _ForWho, string _Text, bool _OC, bool _Ding, string _Code)` | Add despawn event | `OgreBotAPI:DespawnEvent_AddEntry["all", "NPC Name", TRUE, TRUE, "code"]` |
| `DespawnEvent_RemoveEntry(string _ForWho, string _Text)` | Remove despawn event | `OgreBotAPI:DespawnEvent_RemoveEntry["all", "NPC Name"]` |
| `ExecuteEvent(string _ForWho, string _EventName, ... Args)` | Execute custom event ([Args](#executeevent-args)) | `OgreBotAPI:ExecuteEvent["all", "MyEvent", "param1", "param2"]` |
| `ExecuteEvent_JSON(string _ForWho, string _EventName, ... Args)` | Execute event with JSON ([Args](#executeevent_json-args)) | `OgreBotAPI:ExecuteEvent_JSON["all", "MyEvent", "param1"]` |
| `InjectChat(string _ForWho, string _Chat)` | Inject chat command | `OgreBotAPI:InjectChat["all", "/say Hello"]` |
| `Send_Tell(string Speaker, string _Target, string Message)` | Send tell message | `OgreBotAPI:Send_Tell["${Me.Name}", "PlayerName", "Hello"]` |
| `Invite(string _ForWho, string _WhoToInvite, bool _RaidInvite=FALSE)` | Invite to group/raid | `OgreBotAPI:Invite["all", "PlayerName"]` |

### Group/Raid Management

| Method | Description | Example |
|--------|-------------|---------|
| `Mentor(string _Value)` | Mentor to player | `OgreBotAPI:Mentor["PlayerName"]` |
| `Unmentor(string _ForWho)` | Remove mentoring | `OgreBotAPI:Unmentor["all"]` |
| `Disband(string _ForWho)` | Leave group | `OgreBotAPI:Disband["all"]` |
| `MakeLeader(string _ForWho, string _Leader)` | Make group leader | `OgreBotAPI:MakeLeader["all", "PlayerName"]` |
| `FlagToon(string _ForWho, int _Value=1)` | Flag toon for tracking | `OgreBotAPI:FlagToon["fighter", 1]` |
| `UnflagToon(string _ForWho, int _Value=1)` | Unflag toon | `OgreBotAPI:UnflagToon["fighter", 1]` |
| `UnflagAll(string _ForWho)` | Unflag all toons | `OgreBotAPI:UnflagAll["all"]` |
| `SpewFlags(string _ForWho)` | Debug output flags | `OgreBotAPI:SpewFlags["all"]` |
| `FlagToonNextPerson(int _Mark=1)` | Flag next person | `OgreBotAPI:FlagToonNextPerson[1]` |
| `FlagNextPerson(int _Mark=1, string _Via="any", ... SearchForArray)` | Flag next matching person ([Args](#flagnextperson-args)) | `OgreBotAPI:FlagNextPerson[1, "archetype", "fighter"]` |
| `CheckMemberLevel(bool _OnlyShowNonMembers=FALSE)` | Check member subscription levels | `OgreBotAPI:CheckMemberLevel[FALSE]` |
| `MarkToon(string _ForWho)` | Mark toon | `OgreBotAPI:MarkToon["fighter"]` |
| `UnmarkToon(string _ForWho)` | Unmark toon | `OgreBotAPI:UnmarkToon["fighter"]` |
| `SetRelayGroup(string _ForWho, string _Value)` | Set relay group | `OgreBotAPI:SetRelayGroup["all", "MyGroup"]` |
| `SetRelayGroupToDefault(string _ForWho)` | Reset relay group | `OgreBotAPI:SetRelayGroupToDefault["all"]` |
| `Spew_RelayGroup(string _ForWho)` | Debug relay group | `OgreBotAPI:Spew_RelayGroup["all"]` |

### UI Control

| Method | Description | Example |
|--------|-------------|---------|
| `ChangeOgreBotUIOption(string _ForWho, ... Args)` | Change OgreBot UI option ([Args](#changeogrebotuioption--uplinkoptionchange-args)) | `OgreBotAPI:ChangeOgreBotUIOption["all", "silent", "DisableRoots", "TRUE"]` |
| `ChangeCastStackListBoxItem(string _ForWho, string _Object, string _Value, bool _SilentMode=FALSE)` | Change cast stack listbox | `OgreBotAPI:ChangeCastStackListBoxItem["all", "Ability", "TRUE"]` |
| `ChangeCastStackListBoxItemByTag(string _ForWho, string _Object, string _Value, string _Partial, bool _SilentMode)` | Change by tag | `OgreBotAPI:ChangeCastStackListBoxItemByTag["all", "Tag", "TRUE", "partial"]` |
| `UplinkOptionChange(string _ForWho, ... Args)` | Change uplink option ([Args](#changeogrebotuioption--uplinkoptionchange-args)) | `OgreBotAPI:UplinkOptionChange["all", "silent", "Option", "Value"]` |
| `ToggleMainWindow(string _ForWho)` | Toggle main window | `OgreBotAPI:ToggleMainWindow["all"]` |
| `ToggleConsoleWindow(string _ForWho, string _Value)` | Toggle console | `OgreBotAPI:ToggleConsoleWindow["all", "show"]` |
| `ShowOgreConsole(string _ForWho, bool _Value)` | Show/hide OgreConsole | `OgreBotAPI:ShowOgreConsole["all", TRUE]` |
| `CloseWindow(string _ForWho)` | Close window | `OgreBotAPI:CloseWindow["all"]` |
| `InputTextWindow_AddText(string _ForWho, string _Text)` | Add text to input window | `OgreBotAPI:InputTextWindow_AddText["all", "text"]` |
| `InputTextWindow_ClearText(string _ForWho)` | Clear input window | `OgreBotAPI:InputTextWindow_ClearText["all"]` |
| `InputTextWindow_Accept(string _ForWho)` | Accept input window | `OgreBotAPI:InputTextWindow_Accept["all"]` |
| `ResetCameraAngle(string _ForWho)` | Reset camera | `OgreBotAPI:ResetCameraAngle["all"]` |
| `Set_CameraPitch(string _ForWho, int _Pitch)` | Set camera pitch | `OgreBotAPI:Set_CameraPitch["all", 45]` |
| `SetMousePosition(float _X, float _Y)` | Set mouse position | `OgreBotAPI:SetMousePosition[500.0, 400.0]` |
| `SetMousePosition_Middle()` | Center mouse | `OgreBotAPI:SetMousePosition_Middle` |

### Loot System

| Method | Description | Example |
|--------|-------------|---------|
| `HandleLootWindow(string _ForWho, uint _LootWindowID)` | Handle loot window | `OgreBotAPI:HandleLootWindow["all", ${windowID}]` |
| `LootWindowLootAll(string _ForWho)` | Loot all from window | `OgreBotAPI:LootWindowLootAll["all"]` |
| `ChangeLootOptions(string _ForWho, ... Args)` | Change loot options ([Args](#changelootoptions-args)) | `OgreBotAPI:ChangeLootOptions["all", "FFA", "All", "AG"]` |
| `SetAutoLootMode(string _ForWho, int _Value, bool _Silent)` | Set auto-loot mode | `OgreBotAPI:SetAutoLootMode["all", 1, FALSE]` |
| `ResetActorsLooted(string _ForWho)` | Reset looted actors list | `OgreBotAPI:ResetActorsLooted["all"]` |
| `SmartLoot_ReloadDataFromFile(string _ForWho)` | Reload smart loot data | `OgreBotAPI:SmartLoot_ReloadDataFromFile["all"]` |
| `SmartLoot_LOL_AssignPlayer_Item(string _ForWho, string _LootWindowID, string _PlayerToAssignTo, string _ItemName)` | Assign loot to player | `OgreBotAPI:SmartLoot_LOL_AssignPlayer_Item["all", "1", "Player", "Item"]` |
| `SmartLoot_BuildToonItemsToBeZeroed(string _ForWho, ... Args)` | Build items to zero ([Args](#smartloot_buildtoonitemstobezeroed-args)) | `OgreBotAPI:SmartLoot_BuildToonItemsToBeZeroed["all", "PlayerA", "Item"]` |
| `SmartLoot_ProcessToonItemsToBeZeroed(string _ForWho)` | Process zeroed items | `OgreBotAPI:SmartLoot_ProcessToonItemsToBeZeroed["all"]` |
| `Loot_SmartAssign_Add()` | Add smart assign | `OgreBotAPI:Loot_SmartAssign_Add` |
| `Loot_SmartAssign_Update()` | Update smart assign | `OgreBotAPI:Loot_SmartAssign_Update` |

### Alias System

| Method | Description | Example |
|--------|-------------|---------|
| `Alias_AddEntry(string _ForWho, string _Alias, string _Value, _NoRaid=FALSE)` | Add alias | `OgreBotAPI:Alias_AddEntry["all", "mt", "TankName"]` |
| `Alias_RemoveEntry(string _ForWho, string _Text)` | Remove alias | `OgreBotAPI:Alias_RemoveEntry["all", "mt"]` |
| `Alias_ChangeEntry(string _ForWho, string _From, string _To, bool _SilentMode=FALSE)` | Change alias | `OgreBotAPI:Alias_ChangeEntry["all", "mt", "NewTank"]` |
| `Alias_ChangeEntryAlias(string _ForWho, string _From, string _To, bool _SilentMode)` | Change alias reference | `OgreBotAPI:Alias_ChangeEntryAlias["all", "mt", "ot"]` |
| `ForceAliasUpdate(string _ForWho)` | Force alias cache update | `OgreBotAPI:ForceAliasUpdate["all"]` |
| `Aliases_ShowAllBuiltInAliases(string _ForWho, bool _TorF=TRUE)` | Show/hide all built-in aliases | `OgreBotAPI:Aliases_ShowAllBuiltInAliases["all", TRUE]` |

### Ability Embargo/Rotation

| Method | Description | Example |
|--------|-------------|---------|
| `AbilityEmbargo_AddRotateTimer(int64 _AbilityID, uint _Duration, ... Args)` | Add ability rotation timer ([Args](#abilityembargo_addrotatetimer--itemembargo_addrotatetimer-args)) | `OgreBotAPI:AbilityEmbargo_AddRotateTimer[123456, 30, "-g", "PlayerName"]` |
| `AbilityEmbargo_ResetAllAbilityEmbargos(string _ForWho)` | Reset all ability embargos | `OgreBotAPI:AbilityEmbargo_ResetAllAbilityEmbargos["all"]` |
| `AbilityEmbargo_ResetAbilityEmbargo(string _ForWho, string _AbilityName)` | Reset specific embargo | `OgreBotAPI:AbilityEmbargo_ResetAbilityEmbargo["all", "Ability Name"]` |
| `ItemEmbargo_AddRotateTimer(int64 _AbilityID, uint _Duration, ... Args)` | Add item rotation timer ([Args](#abilityembargo_addrotatetimer--itemembargo_addrotatetimer-args)) | `OgreBotAPI:ItemEmbargo_AddRotateTimer[123456, 30, "-g", "PlayerName"]` |
| `AbilityTag_AddRotateTagTimer(string _ForWho, string _TagName, uint _Duration, ... Args)` | Add tag timer ([Args](#abilitytag_addrotatetagtimer-args)) | `OgreBotAPI:AbilityTag_AddRotateTagTimer["all", "MyTag", 30, "-g", "PlayerName"]` |
| `AbilityTag_ResetAllAbilityTagEmbargos(string _ForWho)` | Reset all tag embargos | `OgreBotAPI:AbilityTag_ResetAllAbilityTagEmbargos["all"]` |
| `AbilityTag_ResetAbilityTagEmbargo(string _ForWho, string _TagName)` | Reset tag embargo | `OgreBotAPI:AbilityTag_ResetAbilityTagEmbargo["all", "MyTag"]` |
| `AbilityTag_ResetAllAbilityTagAllows(string _ForWho)` | Reset all tag allows | `OgreBotAPI:AbilityTag_ResetAllAbilityTagAllows["all"]` |
| `AbilityTag_ResetAbilityTagAllow(string _ForWho, string _TagName)` | Reset tag allow | `OgreBotAPI:AbilityTag_ResetAbilityTagAllow["all", "MyTag"]` |

### Intercept System

| Method | Description | Example |
|--------|-------------|---------|
| `SetUpFor_Intercept(string _ForWho)` | Setup intercept | `OgreBotAPI:SetUpFor_Intercept["fighter"]` |
| `ResetFor_Intercept(string _ForWho)` | Reset intercept | `OgreBotAPI:ResetFor_Intercept["fighter"]` |
| `SetUpFor_Dispells(string _ForWho)` | Setup dispells | `OgreBotAPI:SetUpFor_Dispells["all"]` |
| `ResetFor_Dispells(string _ForWho)` | Reset dispells | `OgreBotAPI:ResetFor_Dispells["all"]` |

### Ascension & Deity

| Method | Description | Example |
|--------|-------------|---------|
| `AscensionEmbargo_Add_DoNotCombo(string _ForWho, string _sItemToAdd)` | Add to no-combo list | `OgreBotAPI:AscensionEmbargo_Add_DoNotCombo["all", "Ability Name"]` |
| `AscensionEmbargo_Remove_DoNotCombo(string _ForWho, string _sItemToAdd)` | Remove from no-combo | `OgreBotAPI:AscensionEmbargo_Remove_DoNotCombo["all", "Ability Name"]` |
| `AscensionEmbargo_Change_Disable_Status(string _ForWho, string _sItemToAdd, string ObjectValue, bool _SilentMode)` | Change disable status | `OgreBotAPI:AscensionEmbargo_Change_Disable_Status["all", "Ability", "TRUE"]` |
| `DisplayMyAscensionCombos()` | Display ascension combos | `OgreBotAPI:DisplayMyAscensionCombos` |
| `GenerateMyAscensionCombos()` | Generate ascension combos | `OgreBotAPI:GenerateMyAscensionCombos` |
| `GuidedAscension(string _ForWho, int64 _Amount)` | Use guided ascension | `OgreBotAPI:GuidedAscension["all", 100]` |
| `SpendDeityPoints(string _ForWho, string _SpendOn, int _Spend)` | Spend deity points | `OgreBotAPI:SpendDeityPoints["all", "Option", 10]` |
| `AltarOfTheAncients(string _ForWho)` | Use Altar of Ancients | `OgreBotAPI:AltarOfTheAncients["all"]` |
| `ArcannaseEffigyOfRebirth(string _ForWho)` | Use Arcannase Effigy | `OgreBotAPI:ArcannaseEffigyOfRebirth["all"]` |

### Research & Training

| Method | Description | Example |
|--------|-------------|---------|
| `CheckResearch(string _ForWho, bool _ForceReport=FALSE)` | Check research status | `OgreBotAPI:CheckResearch["all"]` |
| `Research_Material_Check(string _ForWho)` | Check research materials | `OgreBotAPI:Research_Material_Check["all"]` |
| `CheckMercenaryTraining(string _ForWho)` | Check mercenary training | `OgreBotAPI:CheckMercenaryTraining["all"]` |
| `AutoConsumeTemporaryFamiliarExperience(string _ForWho)` | Consume familiar XP items | `OgreBotAPI:AutoConsumeTemporaryFamiliarExperience["all"]` |
| `AutoConsumeTemporaryMountTrainingReduction(string _ForWho)` | Consume mount training items | `OgreBotAPI:AutoConsumeTemporaryMountTrainingReduction["all"]` |
| `AutoConsumeTemporaryResearchReduction(string _ForWho)` | Consume research reduction items | `OgreBotAPI:AutoConsumeTemporaryResearchReduction["all"]` |

### Bot Control

| Method | Description | Example |
|--------|-------------|---------|
| `Reload_Bot(string _ForWho)` | Reload bot | `OgreBotAPI:Reload_Bot["all"]` |
| `Reload_DevBot(string _ForWho)` | Reload dev bot | `OgreBotAPI:Reload_DevBot["all"]` |
| `End_Bot(string _ForWho)` | End bot script | `OgreBotAPI:End_Bot["all"]` |
| `ExitClient(string _ForWho, int _Seconds=30)` | Exit client | `OgreBotAPI:ExitClient["all", 30]` |
| `CampToDesktop(string _ForWho, bool _LoginOnly=FALSE)` | Camp to desktop | `OgreBotAPI:CampToDesktop["all"]` |
| `PlayAtCharacterSelect()` | Play at character select | `OgreBotAPI:PlayAtCharacterSelect` |
| `LoginAtCharacterSelect(string _ForWho, string _CharName)` | Login character | `OgreBotAPI:LoginAtCharacterSelect["all", "CharName"]` |
| `KronoWindowCheck()` | Check Krono window | `OgreBotAPI:KronoWindowCheck` |
| `RedeemKrono(string _ForWho)` | Redeem Krono | `OgreBotAPI:RedeemKrono["all"]` |
| `F2PWindow_Check(string _ForWho)` | Check F2P window | `OgreBotAPI:F2PWindow_Check["all"]` |
| `F2PWindow_SetOptions(string _ForWho, uint _Minutes)` | Set F2P options | `OgreBotAPI:F2PWindow_SetOptions["all", 60]` |
| `SetDebugLoading(bool _TorF=TRUE)` | Enable debug loading messages | `OgreBotAPI:SetDebugLoading[TRUE]` |
| `SetDeveloperLevel(string _ForWho, int _Value=0, bool _Silent=FALSE)` | Set developer level | `OgreBotAPI:SetDeveloperLevel["all", 0]` |
| `Set_CSP(string _ForWho, bool _Value=TRUE, bool _Silent=FALSE)` | Set CSP (campspot processing) status | `OgreBotAPI:Set_CSP["all", TRUE]` |
| `SpewSubscriptionStatus(string _ForWho)` | Display subscription status info | `OgreBotAPI:SpewSubscriptionStatus["all"]` |
| `LogToonIn(string _ForWho, string _ToWho)` | Log a toon into a different character | `OgreBotAPI:LogToonIn["${Me.Name}", "AltCharName"]` |
| `SetQuestion(string _ForWho, bool _Value=TRUE)` | Enable/disable question handling | `OgreBotAPI:SetQuestion["all", TRUE]` |

### Miscellaneous

| Method | Description | Example |
|--------|-------------|---------|
| `SetDebugMode(bool _TorF=TRUE)` | Enable debug mode | `OgreBotAPI:SetDebugMode[TRUE]` |
| `DebugMessage(string _Message, string _Message2)` | Output debug message | `OgreBotAPI:DebugMessage["Phase", "Started"]` |
| `Special(string _ForWho)` | Special command | `OgreBotAPI:Special["all"]` |
| `SpecialZoneSpecific(string _ForWho)` | Zone-specific special | `OgreBotAPI:SpecialZoneSpecific["all"]` |
| `RunWalk(string _ForWho)` | Toggle run/walk | `OgreBotAPI:RunWalk["all"]` |
| `ResStone(string _ForWho)` | Use resurrection stone | `OgreBotAPI:ResStone["all"]` |
| `DungeonMakerCancel(string _ForWho)` | Cancel dungeon maker | `OgreBotAPI:DungeonMakerCancel["all"]` |
| `CheckPackPony(string _ForWho, bool _ForceCheck=FALSE)` | Check pack pony | `OgreBotAPI:CheckPackPony["all"]` |
| `GetToConcentration(string _ForWho, int _Concentration)` | Reduce concentration | `OgreBotAPI:GetToConcentration["all", 3]` |
| `FixCastAfterZoneBug()` | Fix cast-after-zone bug | `OgreBotAPI:FixCastAfterZoneBug` |
| `FlushQueued()` | Flush queued commands | `OgreBotAPI:FlushQueued` |
| `ReloadExport()` | Reload ability export | `OgreBotAPI:ReloadExport` |
| `ReloadOgreIRC()` | Reload OgreIRC | `OgreBotAPI:ReloadOgreIRC` |
| `AfterProfileLoad()` | After profile load hook | `OgreBotAPI:AfterProfileLoad` |
| `SpewAbility(string AbilityName)` | Debug output ability details | `OgreBotAPI:SpewAbility["Ability Name"]` |
| `DisplayAvailableSetups()` | Display available setup configurations | `OgreBotAPI:DisplayAvailableSetups` |
| `SpewZoneDoorOptions()` | Debug output zone door options | `OgreBotAPI:SpewZoneDoorOptions` |
| `RewardWindow_Spew_WindowIDs()` | Debug output reward window IDs | `OgreBotAPI:RewardWindow_Spew_WindowIDs` |
| `ChangeRadarYAxis(string _ForWho, bool _Value)` | Toggle radar Y-axis display | `OgreBotAPI:ChangeRadarYAxis["all", TRUE]` |
| `ShowWikiForQuest(string _ForWho, string _QuestName)` | Open wiki page for quest | `OgreBotAPI:ShowWikiForQuest["${Me.Name}", "Quest Name"]` |
| `DisplayEtherealMissionInfo(string _ForWho)` | Display ethereal mission info | `OgreBotAPI:DisplayEtherealMissionInfo["all"]` |
| `DailyEtherealMissionReset()` | Reset daily ethereal mission | `OgreBotAPI:DailyEtherealMissionReset` |
| `Spew_MissionTimerInfo(string _ForWho, ... Searches)` | Display mission timer info (method) | `OgreBotAPI:Spew_MissionTimerInfo["all", "Mission Name"]` |
| `Get_MissionTimerInfo(string _Global_JSONValue, ... Searches)` | Get mission timer info as JSON | `OgreBotAPI:Get_MissionTimerInfo["myJSONVar", "Mission Name"]` |
| `Spew_BoZ_Research(string _ForWho)` | Display Ballads of Zimara research info | `OgreBotAPI:Spew_BoZ_Research["all"]` |

### Threat Management

| Method | Description | Example |
|--------|-------------|---------|
| `ThreatFighterIgnoreList_Add(string _ForWho, ... Args)` | Add fighters to threat ignore list (Args: fighter names) | `OgreBotAPI:ThreatFighterIgnoreList_Add["all", "Fighter1", "Fighter2"]` |
| `ThreatFighterIgnoreList_Remove(string _ForWho, ... Args)` | Remove fighters from threat ignore list (Args: fighter names) | `OgreBotAPI:ThreatFighterIgnoreList_Remove["all", "Fighter1"]` |
| `ThreatFighterIgnoreList_Clear(string _ForWho)` | Clear entire threat ignore list | `OgreBotAPI:ThreatFighterIgnoreList_Clear["all"]` |
| `ThreatFighterIgnoreList_List(string _ForWho)` | Debug output threat ignore list | `OgreBotAPI:ThreatFighterIgnoreList_List["all"]` |

### Overseer System

| Method | Description | Example |
|--------|-------------|---------|
| `Overseer_SpewMissionsInInventory(string _ForWho)` | Display overseer missions in inventory | `OgreBotAPI:Overseer_SpewMissionsInInventory["all"]` |
| `Overseer_AutoAddOverseerQuests(string _ForWho)` | Automatically add overseer quests | `OgreBotAPI:Overseer_AutoAddOverseerQuests["all"]` |
| `Overseer_AddAgentsToCollection(string _ForWho, bool _Destroy=TRUE)` | Add overseer agents to collection | `OgreBotAPI:Overseer_AddAgentsToCollection["all", TRUE]` |
| `Overseer_CheckQuests(string _ForWho)` | Check overseer quest status | `OgreBotAPI:Overseer_CheckQuests["all"]` |
| `Mercenary_AddMercenaries(string _ForWho)` | Add mercenaries | `OgreBotAPI:Mercenary_AddMercenaries["all"]` |

### AutoHunt System

| Method | Description | Example |
|--------|-------------|---------|
| `AutoHunt_ScanRadius(string _ForWho, int _Value)` | Set auto-hunt scan radius | `OgreBotAPI:AutoHunt_ScanRadius["all", 50]` |
| `AutoHunt_CheckHP(string _ForWho, int _Value)` | Set HP threshold for auto-hunt | `OgreBotAPI:AutoHunt_CheckHP["all", 80]` |
| `AutoHunt_CheckMana(string _ForWho, int _Value)` | Set mana threshold for auto-hunt | `OgreBotAPI:AutoHunt_CheckMana["all", 30]` |
| `AutoHunt_AddPath(string _Value)` | Add auto-hunt path | `OgreBotAPI:AutoHunt_AddPath["PathName"]` |
| `AutoHunt_AddPoint(string _Value)` | Add waypoint to auto-hunt path | `OgreBotAPI:AutoHunt_AddPoint["100.5,25.0,-50.3"]` |
| `AutoHunt_RemovePoint(string _Value)` | Remove waypoint from auto-hunt path | `OgreBotAPI:AutoHunt_RemovePoint["100.5,25.0,-50.3"]` |
| `AutoHunt_ClearPoints()` | Clear all auto-hunt waypoints | `OgreBotAPI:AutoHunt_ClearPoints` |

### Food, Drink & Potions

| Method | Description | Example |
|--------|-------------|---------|
| `Get_FoodDrink(string _ForWho)` | Display current food/drink info | `OgreBotAPI:Get_FoodDrink["all"]` |
| `Change_FoodDrinkAutoConsume(string _ForWho, string _Value)` | Change food/drink auto-consume setting | `OgreBotAPI:Change_FoodDrinkAutoConsume["all", "TRUE"]` |
| `Change_StatPotionsAutoConsume(string _ForWho, string _Value, string _PotionName)` | Change stat potion auto-consume | `OgreBotAPI:Change_StatPotionsAutoConsume["all", "TRUE", "Potion Name"]` |
| `Get_CurePotions(string _ForWho, string _Value)` | Display cure potion info | `OgreBotAPI:Get_CurePotions["all", "info"]` |
| `Get_StatPotions(string _ForWho, string _Value)` | Display stat potion info | `OgreBotAPI:Get_StatPotions["all", "info"]` |
| `Change_PoisonAutoConsume(string _ForWho, string _Value, string Poison)` | Change poison auto-consume setting | `OgreBotAPI:Change_PoisonAutoConsume["all", "TRUE", "Poison Name"]` |
| `Get_Poisons(string _ForWho, string _Value)` | Display poison info | `OgreBotAPI:Get_Poisons["all", "info"]` |

### DoV Raid Debuff

| Method | Description | Example |
|--------|-------------|---------|
| `DoVDebuff(string _ForWho, string _sMobName, string _AllowMoving)` | Apply DoV raid debuff | `OgreBotAPI:DoVDebuff["all", "Boss Name"]` |
| `DoVDebuff_Half(string _ForWho, string _sMobName, string _Archetype="auto", bool _Odd=TRUE, string _AllowMoving)` | Apply DoV raid debuff (half group) | `OgreBotAPI:DoVDebuff_Half["all", "Boss Name", "auto", TRUE]` |

### HQ Ear

| Method | Description | Example |
|--------|-------------|---------|
| `HQEar_ReportStuckEar(string _ForWho, string _ToWhere="OC")` | Report stuck HQ ear | `OgreBotAPI:HQEar_ReportStuckEar["all", "OC"]` |
| `HQEar_ReEquipOriginalEar(string _ForWho)` | Re-equip original ear item | `OgreBotAPI:HQEar_ReEquipOriginalEar["all"]` |
| `HQEar_Recheck(string _ForWho)` | Recheck HQ ear status | `OgreBotAPI:HQEar_Recheck["all"]` |

### Proving Grounds

| Method | Description | Example |
|--------|-------------|---------|
| `ProvingGrounds_Scoreboard_Close(string _ForWho)` | Close proving grounds scoreboard | `OgreBotAPI:ProvingGrounds_Scoreboard_Close["all"]` |
| `ProvingGrounds_Exit(string _ForWho)` | Exit proving grounds | `OgreBotAPI:ProvingGrounds_Exit["all"]` |

---

## Members (Properties)

Members return values and are accessed via `${OgreBotAPI.MemberName[params]}`.

### Status & Checks

| Member | Return | Description | Example |
|--------|--------|-------------|---------|
| `IsReady()` | bool | Is OgreBotAPI ready | `${OgreBotAPI.IsReady}` |
| `Version()` | string | API version | `${OgreBotAPI.Version}` |
| `Paused()` | bool | Is bot paused | `${OgreBotAPI.Paused}` |
| `InCombat()` | bool | Is in combat | `${OgreBotAPI.InCombat}` |
| `InInstance()` | bool | Is in instance | `${OgreBotAPI.InInstance}` |
| `InGuildHallZone()` | bool | Is in guild hall | `${OgreBotAPI.InGuildHallZone}` |
| `InHouseZone()` | bool | Is in house zone | `${OgreBotAPI.InHouseZone}` |
| `InHouseAccessZone()` | bool | Is in house access zone | `${OgreBotAPI.InHouseAccessZone}` |
| `InBattleGround()` | bool | Is in battleground | `${OgreBotAPI.InBattleGround}` |
| `Zoning()` | bool | Is currently zoning | `${OgreBotAPI.Zoning}` |
| `AtCharacterSelect()` | bool | At character select screen | `${OgreBotAPI.AtCharacterSelect}` |
| `ValidKillTarget()` | bool | Has valid kill target | `${OgreBotAPI.ValidKillTarget}` |
| `CancelCurrentCast()` | bool | Is cancel cast active | `${OgreBotAPI.CancelCurrentCast}` |
| `QueuedCommands()` | bool | Has queued commands | `${OgreBotAPI.QueuedCommands}` |
| `IsGroupLeader()` | bool | Is group leader (TRUE if solo or group leader) | `${OgreBotAPI.IsGroupLeader}` |
| `SourceAvailable()` | bool | Is source code available | `${OgreBotAPI.SourceAvailable}` |
| `InICGroup()` | bool | Is in an Instance Controller group | `${OgreBotAPI.InICGroup}` |

### Combat Information

| Member | Return | Description | Example |
|--------|--------|-------------|---------|
| `GetAssistID()` | int64 | Current assist target ID | `${OgreBotAPI.GetAssistID}` |
| `IsAssisting()` | bool | Is currently assisting | `${OgreBotAPI.IsAssisting}` |
| `InControlOfAssisting()` | bool | Is in control of assist | `${OgreBotAPI.InControlOfAssisting}` |
| `NPCsWithinRange(string AbilityName)` | int | NPCs in ability range | `${OgreBotAPI.NPCsWithinRange["Ability Name"]}` |
| `Get_InterruptID(int64 _ActorID)` | int64 | Get interrupt ability ID | `${OgreBotAPI.Get_InterruptID[${Target.ID}]}` |

### Group/Raid Information

| Member | Return | Description | Example |
|--------|--------|-------------|---------|
| `GroupInZone(float _Within=0)` | bool | Is group in zone | `${OgreBotAPI.GroupInZone}` |
| `NumGroupWithCurses()` | int | Group members with curses | `${OgreBotAPI.NumGroupWithCurses}` |
| `NumRaidWithCurses()` | int | Raid members with curses | `${OgreBotAPI.NumRaidWithCurses}` |
| `Get_GroupCurseCount()` | int | Group curse count | `${OgreBotAPI.Get_GroupCurseCount}` |
| `Get_RaidCurseCount()` | int | Raid curse count | `${OgreBotAPI.Get_RaidCurseCount}` |
| `Get_GroupUncurableCurseCount()` | int | Uncurable curse count | `${OgreBotAPI.Get_GroupUncurableCurseCount}` |
| `Get_CursedID(... Args)` | int64 | Get cursed player ID ([Args](#get_cursedid-args)) | `${OgreBotAPI.Get_CursedID["-archetype", "fighter", "-GroupOnly"]}` |
| `Get_Uncurable(string _Type, ... Args)` | int64 | Get uncurable effect ([Args](#get_uncurable-args)) | `${OgreBotAPI.Get_Uncurable["Cursed", "-GroupOnly"]}` |
| `Get_GroupUncurableCurseCount()` | int | Group uncurable curse count | `${OgreBotAPI.Get_GroupUncurableCurseCount}` |
| `Get_RaidUncurableCurseCount()` | int | Raid uncurable curse count | `${OgreBotAPI.Get_RaidUncurableCurseCount}` |
| `Count_CursesInGroup()` | int | Count curses in group | `${OgreBotAPI.Count_CursesInGroup}` |
| `Get_RaidCurableOrUncurableCurses_JSON()` | jsonvalue | Raid curses as JSON (curable + uncurable) | `${OgreBotAPI.Get_RaidCurableOrUncurableCurses_JSON}` |
| `Get_RaidUncurableCurses_JSON()` | jsonvalue | Raid uncurable curses as JSON | `${OgreBotAPI.Get_RaidUncurableCurses_JSON}` |
| `Get_GroupUncurableCurses_JSON()` | jsonvalue | Group uncurable curses as JSON | `${OgreBotAPI.Get_GroupUncurableCurses_JSON}` |
| `GetFarthestGroupDistance()` | float | Distance to farthest group member | `${OgreBotAPI.GetFarthestGroupDistance}` |

### Heroic Opportunity

| Member | Return | Description | Example |
|--------|--------|-------------|---------|
| `HO_Visible()` | bool | Is HO visible | `${OgreBotAPI.HO_Visible}` |
| `HO_Starter_Visible()` | bool | Is HO starter visible | `${OgreBotAPI.HO_Starter_Visible}` |
| `HO_Wheel_Visible()` | bool | Is HO wheel visible | `${OgreBotAPI.HO_Wheel_Visible}` |
| `HO_Wheel_Name()` | string | Current HO wheel name | `${OgreBotAPI.HO_Wheel_Name}` |
| `HO_Starter_Class()` | string | HO starter class | `${OgreBotAPI.HO_Starter_Class}` |
| `HO_Class_Available(string _ForWho)` | bool | Is HO class available | `${OgreBotAPI.HO_Class_Available["fighter"]}` |
| `HO_Wheel_Class_Available(string _ForWho)` | bool | Is wheel class available | `${OgreBotAPI.HO_Wheel_Class_Available["fighter"]}` |
| `HO_Starter_Class_Available(string _ForWho)` | bool | Is starter class available | `${OgreBotAPI.HO_Starter_Class_Available["fighter"]}` |
| `HO_TargetID()` | int64 | HO target ID | `${OgreBotAPI.HO_TargetID}` |
| `DoHO_Get_Enabled()` | bool | Is DoHO enabled | `${OgreBotAPI.DoHO_Get_Enabled}` |
| `DoHO_Get_Primed()` | bool | Is DoHO primed | `${OgreBotAPI.DoHO_Get_Primed}` |
| `DoHo_Get_TargetID()` | int64 | DoHO target ID | `${OgreBotAPI.DoHo_Get_TargetID}` |
| `DoHO_Get_HOerID()` | int64 | DoHO caster ID | `${OgreBotAPI.DoHO_Get_HOerID}` |
| `Get_HOIconAbility(string _HOIconID, ... _Options)` | int64 | Get ability by HO icon | `${OgreBotAPI.Get_HOIconAbility[1234]}` |

### Variables

| Member | Return | Description | Example |
|--------|--------|-------------|---------|
| `Get_Variable(string _VariableName)` | string | Get variable value | `${OgreBotAPI.Get_Variable["phase"]}` |
| `Get_Variable_Bool(string _VariableName)` | bool | Get variable as bool | `${OgreBotAPI.Get_Variable_Bool["isActive"]}` |
| `Get_VariableExists(string _VariableName)` | bool | Does variable exist | `${OgreBotAPI.Get_VariableExists["phase"]}` |
| `Get_InternalVariable(string _VariableName)` | string | Get internal variable | `${OgreBotAPI.Get_InternalVariable["myVar"]}` |
| `Get_InternalVariableExists(string _VariableName)` | bool | Does internal var exist | `${OgreBotAPI.Get_InternalVariableExists["myVar"]}` |

### Actor/Target Information

| Member | Return | Description | Example |
|--------|--------|-------------|---------|
| `GetMobID(string _MobNameID)` | int64 | Get mob ID from name/ID | `${OgreBotAPI.GetMobID["Boss Name"]}` |
| `GetActorCountByName(string _ActorName, ... Args)` | int | Count actors by name ([Args](#getactorcountbyname-args)) | `${OgreBotAPI.GetActorCountByName["Add Name", "-partial", "-distance", 30]}` |
| `GetFarthestActorFrom(string _FindActorName, string _FromActorNameID, float _MinDistance)` | int64 | Get farthest actor | `${OgreBotAPI.GetFarthestActorFrom["Add", "${Me.Name}", 5]}` |
| `GameDistanceToActor(string _NameOrID)` | float | Distance to actor | `${OgreBotAPI.GameDistanceToActor["Boss Name"]}` |
| `GetActorModelSize(int64 _ActorID)` | float | Actor model size | `${OgreBotAPI.GetActorModelSize[${Target.ID}]}` |
| `GetMyModelSize()` | float | My model size | `${OgreBotAPI.GetMyModelSize}` |
| `ActorHasQuest(int64 _ActorID)` | bool | Actor has quest | `${OgreBotAPI.ActorHasQuest[${Target.ID}]}` |
| `GetActorCountByType(... Args)` | int | Count actors by type ([Args](#getactorcountbytype-args)) | `${OgreBotAPI.GetActorCountByType["-Type", "NamedNPC", "-distance", 30]}` |

### Ability Information

| Member | Return | Description | Example |
|--------|--------|-------------|---------|
| `GetAbilityID(string AbilityName)` | int64 | Get ability ID | `${OgreBotAPI.GetAbilityID["Divine Arbitration"]}` |
| `Get_AbilityInfo(string _AbilityNameID, string _Member)` | string | Get ability info | `${OgreBotAPI.Get_AbilityInfo["Ability Name", "Range"]}` |
| `Get_AbilityInfo_RawData(string _AbilityName, string _Member)` | string | Get raw ability data | `${OgreBotAPI.Get_AbilityInfo_RawData["Ability Name", "Range"]}` |
| `Get_AbilityShortName(string _AbilityName)` | string | Get short ability name | `${OgreBotAPI.Get_AbilityShortName["Long Ability Name"]}` |
| `Get_AbilityTypeID(string AbilityType, ... Args)` | int64 | Get ability type ID ([Args](#get_abilitytypeid-args)) | `${OgreBotAPI.Get_AbilityTypeID["cure", "-NPCRequired"]}` |
| `Get_AbilityVia(... Args)` | int64 | Get ability via params ([Args](#get_abilityvia-args)) | `${OgreBotAPI.Get_AbilityVia["IsInterrupt", "equal", "TRUE", "-NPCRequired"]}` |
| `AbilityReady(string _ForWho, string AbilityName, int64 _ActorID)` | bool | Is ability ready | `${OgreBotAPI.AbilityReady["${Me.Name}", "Ability", ${Target.ID}]}` |
| `CheckNoReqBowAbilities()` | bool | Check no-bow-req setting | `${OgreBotAPI.CheckNoReqBowAbilities}` |

### Equipment Information

| Member | Return | Description | Example |
|--------|--------|-------------|---------|
| `Get_EquipmentModifierValue(string _Slot, string _Modifier)` | string | Get equipment modifier | `${OgreBotAPI.Get_EquipmentModifierValue["Primary", "DPS"]}` |
| `EquipmentSlotAvailable(string _Slot)` | bool | Is slot available | `${OgreBotAPI.EquipmentSlotAvailable["Primary"]}` |
| `EquipmentSlotNumAvailable(int _Slot)` | bool | Is slot num available | `${OgreBotAPI.EquipmentSlotNumAvailable[0]}` |
| `ConvertSlotArrayToSlot(int _SlotArray)` | int | Convert slot array | `${OgreBotAPI.ConvertSlotArrayToSlot[0]}` |
| `RoR_Epic_Available()` | bool | Is RoR epic available | `${OgreBotAPI.RoR_Epic_Available}` |
| `RoR_Epic_Ready()` | bool | Is RoR epic ready | `${OgreBotAPI.RoR_Epic_Ready}` |
| `RoR_Epic_AbilityID()` | int64 | RoR epic ability ID | `${OgreBotAPI.RoR_Epic_AbilityID}` |

### Adornment Information

| Member | Return | Description | Example |
|--------|--------|-------------|---------|
| `Get_AdornmentColour(string _IconID)` | string | Get adorn color | `${OgreBotAPI.Get_AdornmentColour["1234"]}` |
| `IsAdornmentColour(string _IconID, string _Colour)` | bool | Check adorn color | `${OgreBotAPI.IsAdornmentColour["1234", "Red"]}` |
| `Get_NumAdornmentsOfColour(string _Slot, string _Colour)` | int | Count adorns by color | `${OgreBotAPI.Get_NumAdornmentsOfColour["Primary", "Red"]}` |
| `ConvertAdornToSlot(string _AdornHash, int _Slot)` | string | Convert adorn to slot | `${OgreBotAPI.ConvertAdornToSlot["hash", 0]}` |
| `ConvertAdornToRemoveSlot(string _AdornHash)` | string | Convert for removal | `${OgreBotAPI.ConvertAdornToRemoveSlot["hash"]}` |

### Zone Information

| Member | Return | Description | Example |
|--------|--------|-------------|---------|
| `ZoneName(string _Input)` | string | Clean zone name | `${OgreBotAPI.ZoneName["${Zone.Name}"]}` |
| `CleanZoneName(string _ZoneName)` | string | Sanitized zone name | `${OgreBotAPI.CleanZoneName["${Zone.Name}"]}` |
| `RemoveZoneNumber(string _Input)` | string | Remove zone number | `${OgreBotAPI.RemoveZoneNumber["${Zone.Name}"]}` |
| `RemoveZoneNumberOnly(string _Input)` | string | Remove only number | `${OgreBotAPI.RemoveZoneNumberOnly["${Zone.Name}"]}` |
| `RoomID()` | string | Current room ID | `${OgreBotAPI.RoomID}` |
| `Travel_Get_ZoneDoorValue(string _DoorOption)` | int | Get zone door value | `${OgreBotAPI.Travel_Get_ZoneDoorValue["option1"]}` |
| `GuildFlagLocation()` | string | Guild flag location | `${OgreBotAPI.GuildFlagLocation}` |
| `RemoveColourCode(string _Input)` | string | Remove colour codes from string | `${OgreBotAPI.RemoveColourCode["${Zone.Name}"]}` |

### Zone Reset Information

| Member | Return | Description | Example |
|--------|--------|-------------|---------|
| `ZoneReset_IsReady()` | bool | Is zone reset data ready | `${OgreBotAPI.ZoneReset_IsReady}` |
| `ZoneReset_IsUpdating()` | bool | Is zone reset data updating | `${OgreBotAPI.ZoneReset_IsUpdating}` |
| `ZoneReset_FullZoneInformationAvailable()` | bool | Is full zone reset info available | `${OgreBotAPI.ZoneReset_FullZoneInformationAvailable}` |

### Flags & Markers

| Member | Return | Description | Example |
|--------|--------|-------------|---------|
| `ToonMarked()` | bool | Is toon marked | `${OgreBotAPI.ToonMarked}` |
| `ToonFlagged(int _Value)` | bool | Is toon flagged | `${OgreBotAPI.ToonFlagged[1]}` |

### Loot Information

| Member | Return | Description | Example |
|--------|--------|-------------|---------|
| `LootWindowExists()` | bool | Does loot window exist | `${OgreBotAPI.LootWindowExists}` |
| `Get_LootWindowID()` | int64 | Get loot window ID | `${OgreBotAPI.Get_LootWindowID}` |
| `RewardWindow_Get_WindowID()` | uint | Get reward window ID | `${OgreBotAPI.RewardWindow_Get_WindowID}` |
| `Get_RewardName(string _Selection, int64 _WindowID)` | string | Get reward name | `${OgreBotAPI.Get_RewardName["0", ${windowID}]}` |
| `Get_RewardID(string _Selection, int64 _WindowID)` | int | Get reward ID | `${OgreBotAPI.Get_RewardID["0", ${windowID}]}` |
| `Get_RewardLinkID(string _Selection, int64 _WindowID)` | string | Get reward link ID | `${OgreBotAPI.Get_RewardLinkID["0", ${windowID}]}` |

### Detrimental Effects

| Member | Return | Description |
|--------|--------|-------------|
| `DetrimentalInfo(int _MainID, int _BackDropID, uint _ActorID, string _Return)` | string | Get detrimental info |
| `DetrimentalInfo_ref(persistentref DotToCheck, uint _ActorID, string _Return)` | string | Get detrimental by icon ref |
| `DetrimentalInfo_String(int _MainID, int _BackDropID, int64 _ActorID, string _Return)` | string | Get detrimental info as string | `${OgreBotAPI.DetrimentalInfo_String[55, 110, ${Me.ID}, "exists"]}` |
| `DetrimentalInfo_ref_String(weakref _IconIDs, int64 _ActorID, string _Return)` | string | Get detrimental string by icon ref | `${OgreBotAPI.DetrimentalInfo_ref_String[CurseIconID, ${Me.ID}, "exists"]}` |

#### DetrimentalInfo Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `_MainID` | int | Main icon ID of the detriment |
| `_BackDropID` | int | Backdrop icon ID of the detriment |
| `_ActorID` | uint | Actor to check (default: `${Me.ID}`) |
| `_Return` | string | What info to return (default: `"exists"`) |

#### Available _Return Values

**For Self (`${Me.ID}`):**

| Value | Returns | Description |
|-------|---------|-------------|
| `exists` | 1 or 0 | Whether detriment exists (default) |
| `CurrentIncrements` | int | Stack count of the detriment |
| `Duration` | float | Time remaining in seconds |
| `MaxDuration` | float | Maximum duration |
| `ID` | int | Effect ID |
| `cancel` | 1 | Cancels the detriment |

**For Other Actors (NPCs, group members):**

| Value | Returns | Description |
|-------|---------|-------------|
| `exists` | 1 or 0 | Whether effect exists (default) |
| `CurrentIncrements` | int | Stack count |
| `ID` | int | Effect ID |

#### DetrimentalInfo Usage Examples

```lavishscript
; Check if detriment exists (MainIconID=55, BackdropIconID=110)
if ${OgreBotAPI.DetrimentalInfo[55, 110, ${Me.ID}, "exists"]}
{
    echo "I have the detriment!"
}

; Get current stack count
variable int stacks
stacks:Set[${OgreBotAPI.DetrimentalInfo[55, 110, ${Me.ID}, "CurrentIncrements"]}]
if ${stacks} >= 3
{
    echo "Stacks at ${stacks}, need to joust!"
}

; Check duration remaining
if ${OgreBotAPI.DetrimentalInfo[55, 110, ${Me.ID}, "Duration"]} < 5
{
    echo "Detriment about to expire!"
}

; Cancel the detriment
noop ${OgreBotAPI.DetrimentalInfo[55, 110, ${Me.ID}, "cancel"]}

; Check detriment on an NPC
if ${OgreBotAPI.DetrimentalInfo[55, 110, ${Actor[${AssistTarget}].ID}, "exists"]}
{
    echo "Target has the debuff with ${OgreBotAPI.DetrimentalInfo[55, 110, ${Actor[${AssistTarget}].ID}, "CurrentIncrements"]} stacks"
}
```

#### Using with persistentref (Icon ID Object)

For cleaner code when checking the same detriment repeatedly:

```lavishscript
; Define icon ID reference
variable persistentref CurseIconID
CurseIconID:SetReference["OgreGenericIconID"]
CurseIconID.MainID:Set[55]
CurseIconID.BackDropID:Set[110]

; Use DetrimentalInfo_ref for cleaner checks
if ${GetInfoOb.DetrimentalInfo_ref[CurseIconID]}
{
    echo "Curse detected!"
    echo "Stacks: ${GetInfoOb.DetrimentalInfo_ref[CurseIconID, ${Me.ID}, "CurrentIncrements"]}"
    echo "Duration: ${GetInfoOb.DetrimentalInfo_ref[CurseIconID, ${Me.ID}, "Duration"]}"
}
```

#### Cross-Session Detrimental Command

```lavishscript
; Cancel a specific detriment across all group members
oc !ci -CancelDetrimental igw:${Me.Name} 110 55
; Note: CancelDetrimental params are BackDropID, MainID (reversed order)
```

### Quests

| Member | Return | Description | Example |
|--------|--------|-------------|---------|
| `HaveQuest(string _QuestName)` | bool | Do I have quest | `${OgreBotAPI.HaveQuest["Quest Name"]}` |
| `ReplyDialog_ReplyExists(string _ForWho, string _Choice, bool _ExactMatch)` | int | Does reply exist | `${OgreBotAPI.ReplyDialog_ReplyExists["all", "1", FALSE]}` |
| `Select_Window_GetOption(... Args)` | int | Get select window option ([Args](#select_window-args)) | `${OgreBotAPI.Select_Window_GetOption["-substring", "Accept"]}` |

### Utility

| Member | Return | Description | Example |
|--------|--------|-------------|---------|
| `CommandForMe(string _ForWho)` | bool | Is command for me | `${OgreBotAPI.CommandForMe["fighter"]}` |
| `Between(int64 _ValueToCompare, int64 _Value1, int64 _Value2)` | bool | Is value between | `${OgreBotAPI.Between[50, 25, 75]}` |
| `BetweenFloat(float _ValueToCompare, float _Value1, float _Value2)` | bool | Float between | `${OgreBotAPI.BetweenFloat[50.5, 25.0, 75.0]}` |
| `To_Int(string _Value)` | int64 | Convert to int | `${OgreBotAPI.To_Int["123"]}` |
| `To_Float(string _Value)` | float | Convert to float | `${OgreBotAPI.To_Float["12.5"]}` |
| `To_Number(string _Value)` | string | Convert to number string | `${OgreBotAPI.To_Number["abc123"]}` |
| `Get_Archetype(string _Value)` | string | Get archetype | `${OgreBotAPI.Get_Archetype["Berserker"]}` |
| `Get_Role(string _Value)` | string | Get role | `${OgreBotAPI.Get_Role["Berserker"]}` |
| `Get_BaseClass(string _Value)` | string | Get base class | `${OgreBotAPI.Get_BaseClass["Berserker"]}` |
| `Get_Turbo()` | int | Get turbo value | `${OgreBotAPI.Get_Turbo}` |
| `Get_Alias(string _Alias)` | string | Get alias value | `${OgreBotAPI.Get_Alias["mt"]}` |
| `Get_Alias2(string _Alias)` | string | Get alias value (alt) | `${OgreBotAPI.Get_Alias2["mt"]}` |
| `Get_ScriptBaseName(string _Path, bool _RemoveExtension)` | string | Get script basename | `${OgreBotAPI.Get_ScriptBaseName["path/script.iss", TRUE]}` |
| `FileExists(string _Path)` | bool | Does file exist | `${OgreBotAPI.FileExists["Scripts/MyScript.iss"]}` |
| `MD5(string _Input)` | string | MD5 hash | `${OgreBotAPI.MD5["input string"]}` |
| `Clean(string _Input)` | string | Clean string | `${OgreBotAPI.Clean["dirty string"]}` |
| `CleanNameWithSpaces(string _Input)` | string | Clean name with spaces | `${OgreBotAPI.CleanNameWithSpaces["Name With Spaces"]}` |
| `ItemCount(string _ItemName)` | int | Count items | `${OgreBotAPI.ItemCount["Item Name"]}` |
| `CurrentCharacter()` | string | Current character name | `${OgreBotAPI.CurrentCharacter}` |
| `UplinkName()` | string | Uplink session name | `${OgreBotAPI.UplinkName}` |
| `IsCastingWindowVisible()` | bool | Is casting window visible | `${OgreBotAPI.IsCastingWindowVisible}` |
| `CursorActor_Tooltip_Visible()` | bool | Is cursor tooltip visible | `${OgreBotAPI.CursorActor_Tooltip_Visible}` |
| `CursorActor_Tooltip_Text()` | string | Cursor tooltip text | `${OgreBotAPI.CursorActor_Tooltip_Text}` |
| `PointAtAngle(int _Angle, string _NameOrID, float _Distance)` | point3f | Point at angle from actor | `${OgreBotAPI.PointAtAngle[180, "Boss Name", 5]}` |
| `PointAtAngleNoSize(int _Angle, string _NameOrID, float _Distance)` | point3f | Point ignoring size | `${OgreBotAPI.PointAtAngleNoSize[180, "Boss Name", 5]}` |
| `Get_Seconds(int64 _Seconds)` | int64 | Get seconds component | `${OgreBotAPI.Get_Seconds[3661]}` |
| `Get_Minutes(int64 _Seconds)` | int64 | Get minutes component | `${OgreBotAPI.Get_Minutes[3661]}` |
| `Get_Hours(int64 _Seconds)` | int64 | Get hours component | `${OgreBotAPI.Get_Hours[3661]}` |
| `ConvertSecondsToHMS(int64 _Seconds)` | string | Convert to H:M:S | `${OgreBotAPI.ConvertSecondsToHMS[3661]}` |
| `SpewStat(string _Command, bool _AddLabel)` | string | Spew stat info | `${OgreBotAPI.SpewStat["stat", TRUE]}` |
| `Get_DeityPoints(string _Value)` | int | Get deity points | `${OgreBotAPI.Get_DeityPoints["available"]}` |
| `RomanToInt(string _sRoman)` | int | Convert Roman numeral to integer | `${OgreBotAPI.RomanToInt["IV"]}` |
| `RoundNumToNearestValue(int _Health, int _Divider=1, int _IncrementBy=0)` | int | Round number to nearest value | `${OgreBotAPI.RoundNumToNearestValue[73, 5, 0]}` |
| `IsItemTimeUntilReadyZero(int64 _LinkID, string _EquipmentOrInventory="Inventory")` | bool | Is item ready (cooldown expired) | `${OgreBotAPI.IsItemTimeUntilReadyZero[123456, "Inventory"]}` |
| `Get_APIPackPonyRunning()` | bool | Is API pack pony running | `${OgreBotAPI.Get_APIPackPonyRunning}` |
| `Get_PackPonyRunning()` | bool | Is pack pony running | `${OgreBotAPI.Get_PackPonyRunning}` |
| `Get_RotationData()` | jsonvalue | Get current rotation data as JSON | `${OgreBotAPI.Get_RotationData}` |

### CSP & Developer

| Member | Return | Description | Example |
|--------|--------|-------------|---------|
| `Get_CSP()` | bool | Get CSP status | `${OgreBotAPI.Get_CSP}` |
| `NG()` | bool | No gravity status | `${OgreBotAPI.NG}` |
| `InTesting()` | bool | In testing mode | `${OgreBotAPI.InTesting}` |
| `Get_DebugLoading()` | bool | Debug loading enabled | `${OgreBotAPI.Get_DebugLoading}` |
| `IsAPC(string _Type)` | bool | Is actor a PC | `${OgreBotAPI.IsAPC["type"]}` |
| `ERE(int _EqualOrAbove)` | bool | Elite raid status | `${OgreBotAPI.ERE[1]}` |
| `HaveSickness()` | bool | Has resurrection sickness | `${OgreBotAPI.HaveSickness}` |
| `NPCUnkillableBug()` | bool | NPC unkillable bug check | `${OgreBotAPI.NPCUnkillableBug}` |
| `CityRestrictions()` | bool | City restrictions apply | `${OgreBotAPI.CityRestrictions}` |
| `UnauthPCsNearMe(float _Distance)` | bool | Unauthorized PCs nearby | `${OgreBotAPI.UnauthPCsNearMe[50.0]}` |
| `CheckNoOffensiveOn()` | bool | No-offensive list check | `${OgreBotAPI.CheckNoOffensiveOn}` |
| `CheckNoDefensiveOn()` | bool | No-defensive check | `${OgreBotAPI.CheckNoDefensiveOn}` |
| `Get_CSP()` | bool | Get CSP (campspot processing) status | `${OgreBotAPI.Get_CSP}` |
| `ClassInfo_GetValue(string _ForWho, string _Member)` | bool | Get class info value | `${OgreBotAPI.ClassInfo_GetValue["all", "Archetype"]}` |
| `InEQ2Chars(string _Speaker, bool _FullAccountInfoOnly=FALSE)` | bool | Is speaker in EQ2 character list | `${OgreBotAPI.InEQ2Chars["PlayerName"]}` |
| `Get_ReviveLocation(string _Option, bool _ExactMatch=FALSE)` | int | Get revive location option index | `${OgreBotAPI.Get_ReviveLocation["option", FALSE]}` |

### Ability Embargo

| Member | Return | Description | Example |
|--------|--------|-------------|---------|
| `AbilityTag_GetTagEmbargoTimeRemaining(string _TagName)` | float | Tag embargo time left | `${OgreBotAPI.AbilityTag_GetTagEmbargoTimeRemaining["MyTag"]}` |
| `AbilityTag_GetTagAllowTimeRemaining(string _TagName)` | float | Tag allow time left | `${OgreBotAPI.AbilityTag_GetTagAllowTimeRemaining["MyTag"]}` |

### Auto-Target

| Member | Return | Description | Example |
|--------|--------|-------------|---------|
| `AutoTarget_Enabled()` | bool | Is auto-target enabled | `${OgreBotAPI.AutoTarget_Enabled}` |
| `AutoTarget_Disabled(string _Key)` | bool | Is auto-target disabled | `${OgreBotAPI.AutoTarget_Disabled["key"]}` |

### Maintained Spells

| Member | Return | Description | Example |
|--------|--------|-------------|---------|
| `HaveMaintained(... Args)` | bool | Have maintained spell ([Args](#havemaintained-args)) | `${OgreBotAPI.HaveMaintained["-exact", "Buff Name"]}` |
| `ScrollOf_Get_MaintainedDuration(string _ScrollName)` | int | Get scroll duration | `${OgreBotAPI.ScrollOf_Get_MaintainedDuration["Scroll Name"]}` |

### Water Breathing

| Member | Return | Description | Example |
|--------|--------|-------------|---------|
| `CastGroupWaterBreathing(string _ForWho)` | method | Cast group water breathing | `OgreBotAPI:CastGroupWaterBreathing["all"]` |
| `CancelGroupWaterBreathing(string _ForWho)` | method | Cancel water breathing | `OgreBotAPI:CancelGroupWaterBreathing["all"]` |

---

## Functions

Functions are called with `call OgreBotAPI.FunctionName params` and can return values.

| Function | Return | Description | Example |
|----------|--------|-------------|---------|
| `HO_Start(... Args)` | bool | Start HO ([Args](#ho_start-args)) | `call OgreBotAPI.HO_Start` |
| `HO_Starter()` | bool | Cast HO starter | `call OgreBotAPI.HO_Starter` |
| `HO_Advance()` | bool | Advance HO | `call OgreBotAPI.HO_Advance` |
| `Cast_Interrupt(string _MobNameID, int64 _AbilityID, string _CalledFrom)` | - | Cast interrupt | `call OgreBotAPI.Cast_Interrupt "Boss Name" 0 "IC"` |
| `CastAbilityOnNPC(string _ForWho, string AbilityName, string _MobNameID, string _CalledFrom)` | - | Cast on NPC | `call OgreBotAPI.CastAbilityOnNPC "all" "Taunt" "Boss" "IC"` |
| `CastRescue(string CalledFrom, ... Args)` | - | Cast rescue ([Args](#castrescue-args)) | `call OgreBotAPI.CastRescue "IC" "-NPCRequired"` |
| `ZoneInto(string _ZoneName, string _ActorName, int _DoorOption)` | - | Zone into | `call OgreBotAPI.ZoneInto "Zone Name" "Door NPC" 0` |
| `GetToGH()` | - | Get to guild hall | `call OgreBotAPI.GetToGH` |
| `HouseWindowToGH()` | - | House window to GH | `call OgreBotAPI.HouseWindowToGH` |
| `AcceptReward(string _Selection, int64 _WindowID)` | - | Accept reward | `call OgreBotAPI.AcceptReward "0" 0` |
| `Question()` | - | Handle question | `call OgreBotAPI.Question` |
| `Resource()` | - | Handle resource | `call OgreBotAPI.Resource` |
| `DestroyItem(string _ItemName, uint _Charges)` | - | Destroy item | `call OgreBotAPI.DestroyItem "Item Name" 0` |
| `DestroyItem_NoChecks(string _ItemName)` | - | Destroy no checks | `call OgreBotAPI.DestroyItem_NoChecks "Item Name"` |
| `DestroyItemByID_NoChecks(int64 _ItemID)` | - | Destroy by ID | `call OgreBotAPI.DestroyItemByID_NoChecks 123456789` |
| `Consume_Status_Ingots(uint _Amount)` | - | Consume ingots | `call OgreBotAPI.Consume_Status_Ingots 100` |
| `Actor_ClickQueued(string _NameOrID, bool _ExactName, int _WaitTime)` | - | Click actor queued | `call OgreBotAPI.Actor_ClickQueued "NPC Name" FALSE 40` |
| `HailNPC(string _NameOrID)` | - | Hail NPC | `call OgreBotAPI.HailNPC "NPC Name"` |
| `ReloadExport()` | - | Reload export | `call OgreBotAPI.ReloadExport` |
| `Summon_Familiar()` | - | Summon familiar | `call OgreBotAPI.Summon_Familiar` |
| `Research_Material_Check(string _ForWho)` | int | Check research mats | `call OgreBotAPI.Research_Material_Check "all"` |
| `Champions_Zone_Resetter(string _ZoneName)` | - | Reset champions zone | `call OgreBotAPI.Champions_Zone_Resetter "Zone Name"` |
| `Select_Window(string _ForWho, ... Args)` | int | Select window ([Args](#select_window-args)) | `call OgreBotAPI.Select_Window "all" "-substring" "Accept"` |
| `AutoConsumeTemporaryFamiliarExperience()` | - | Consume familiar XP | `call OgreBotAPI.AutoConsumeTemporaryFamiliarExperience` |
| `AutoConsumeTemporaryMountTrainingReduction()` | - | Consume mount training | `call OgreBotAPI.AutoConsumeTemporaryMountTrainingReduction` |
| `AutoConsumeTemporaryResearchReduction()` | - | Consume research | `call OgreBotAPI.AutoConsumeTemporaryResearchReduction` |
| `CheckResearch(bool _ForceReport)` | - | Check research | `call OgreBotAPI.CheckResearch FALSE` |
| `ResetCameraAngle()` | - | Reset camera | `call OgreBotAPI.ResetCameraAngle` |
| `Set_CameraPitch(int _Pitch)` | - | Set pitch | `call OgreBotAPI.Set_CameraPitch 45` |
| `Set_FirstPersonView()` | bool | Set first person | `call OgreBotAPI.Set_FirstPersonView` |
| `Set_LookDown(uint _Value)` | bool | Look down | `call OgreBotAPI.Set_LookDown 30` |
| `Set_LookUp(uint _Value)` | bool | Look up | `call OgreBotAPI.Set_LookUp 30` |
| `CheckKunarkAscendingRequirements()` | - | Check KA requirements | `call OgreBotAPI.CheckKunarkAscendingRequirements` |
| `ApplyVerbIDQueuedForWho(int64 _ActorID, string _Verb)` | - | Apply verb queued | `call OgreBotAPI.ApplyVerbIDQueuedForWho ${Actor["NPC"].ID} "use"` |
| `ApplyVerbQueuedForWho(string _ActorName, string _Verb)` | - | Apply verb queued | `call OgreBotAPI.ApplyVerbQueuedForWho "NPC Name" "use"` |
| `ToggleZoneReuse()` | - | Toggle zone reuse | `call OgreBotAPI.ToggleZoneReuse` |
| `ResetZone(string _ZoneName)` | - | Reset zone | `call OgreBotAPI.ResetZone "Zone Name"` |
| `ConvertAdornToSlot(string _AdornHash)` | string | Convert adorn slot | `call OgreBotAPI.ConvertAdornToSlot "hash"` |
| `CancelInvis()` | - | Cancel invisibility | `call OgreBotAPI.CancelInvis` |
| `LoginAtCharacterSelect(string _CharName)` | - | Login character | `call OgreBotAPI.LoginAtCharacterSelect "CharName"` |
| `TargetAndDoubleClickActor(int64 _ActorID)` | - | Target and click | `call OgreBotAPI.TargetAndDoubleClickActor ${Actor["NPC"].ID}` |
| `Spew_MissionTimerInfo(... Searches)` | - | Spew mission info | `call OgreBotAPI.Spew_MissionTimerInfo` |
| `LandFlyingMount()` | - | Land mount | `call OgreBotAPI.LandFlyingMount` |
| `ExitClient(int _Seconds)` | - | Exit client | `call OgreBotAPI.ExitClient 30` |
| `OpenAndBuyFromMerchant(...)` | - | Buy from merchant | `call OgreBotAPI.OpenAndBuyFromMerchant "Merchant" "Item" 1` |
| `CloseAllExamine()` | - | Close all examine | `call OgreBotAPI.CloseAllExamine` |
| `ExamineAllOfItem(... _Items)` | - | Examine items | `call OgreBotAPI.ExamineAllOfItem "Item Name"` |
| `Consume_Status_Tokens(uint _Amount)` | - | Consume tokens | `call OgreBotAPI.Consume_Status_Tokens 100` |
| `WaitForCasting(uint _TimeToWaitForCasting=50)` | - | Wait for casting to complete | `call OgreBotAPI.WaitForCasting 50` |
| `Interrupt_Mode()` | - | Run interrupt mode | `call OgreBotAPI.Interrupt_Mode` |

---

## Args Reference

Methods, members, and functions that accept `... Args` support optional flags. See [Variadic Parameters](../../innerspace/advanced-lavishscript.md) for how `... Args` works in LavishScript. Below is a detailed reference for each.

### PulseCircleMovement Args

Moves the group (or self) in a circular pattern around a location. Each call advances to the next position around the circle.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `-setspot` | int | `0` | Force a specific spot number instead of auto-incrementing |
| `-spots` | int | `4` | Number of positions around the circle (e.g., 4 = every 90°, 8 = every 45°) |
| `-distance` | float | `3` | Radius of the circle from `_Loc` |
| `-Group` | *(flag)* | `FALSE` | Apply campspot change to the whole group (`igw:`) |
| `-SpotChangeWait` | int | `2` | Cooldown between spot changes in **seconds** |
| `-SpotChangeWaitMS` | int | `2000` | Cooldown between spot changes in **milliseconds** |
| `-ClearWait` | *(flag)* | — | Resets the movement timer to 0, allowing immediate movement |
| `-Return` | *(flag)* | — | Immediately returns without doing anything |
| `-RelativeCampspot` | *(flag)* | `FALSE` | Uses relative campspot instead of absolute |
| `-Debug` | *(flag)* | `FALSE` | Echoes debug output |
| `-YChange` | float | `0` | Vertical offset added to the Y coordinate |

**Example:**

```lavishscript
; 8 positions, 4.5m radius, 1-second rotation, +1 Y offset, debug on
OgreBotAPI:PulseCircleMovement["${This.PuzzleSolutionLoc}", "-spots", 8, "-distance", 4.5, "-Debug", "-SpotChangeWait", 1, "-YChange", 1]
```

### Set_DisableAllAOEs Args

Disables (or enables) all AOE abilities, with optional flags.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `-verbose` | *(flag)* | silent | Changes UI option changes from silent to verbose (echoes output) |
| `-allowcounters` | *(flag)* | `FALSE` | When TRUE, counter abilities (e.g., Aggressive Defense, Porcupine, Ancestral Palisade) are NOT cancelled even when disabling all AoEs |

**Example:**

```lavishscript
OgreBotAPI:Set_DisableAllAOEs["all", TRUE, "-allowcounters"]
```

### CastAbilityType Args

Casts an ability by type (e.g., cure, interrupt). Args control targeting.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `-NPCRequired` | *(flag)* | — | Sets the target to the current NPC target |
| `-TargetID` / `-ActorID` | int64 | `0` | Sets a specific actor ID to target |

**Example:**

```lavishscript
OgreBotAPI:CastAbilityType["healer", "cure", "IC", "-NPCRequired"]
```

### CastRescue Args

Casts a rescue/threat-increase ability. Args control targeting and fallback behavior.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `-NPCRequired` | *(flag)* | — | Sets the target to the current NPC target |
| `-TargetID` / `-ActorID` | int64 | `0` | Sets a specific actor ID to target |
| `-NoForceTargets` | *(flag)* | `FALSE` | If no threat-increase ability is found, do NOT fall back to ForceTarget abilities |

**Example:**

```lavishscript
OgreBotAPI:CastRescue["fighter", "IC", "-NPCRequired"]
```

### Cast_Interrupt Args

Note: `Cast_Interrupt` declares `... Args` in its signature but **does not process any flags** from them. Args are unused.

### CancelCasting Args

Cancels current casting, with optional conditions and follow-up actions.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `-HOAbility` | *(flag)* | `FALSE` | Only cancel if the current spell is a Heroic Opportunity ability |
| `-HOAbilityUI` | *(flag)* | `FALSE` | Only cancel if the current spell is an HO ability AND the HO UI setting says to cancel it |
| `-CastHOAbilityIconID` | int | — | After cancelling, queue an HO icon ability cast with this icon ID |
| `-CastTime` | float | `0` | Only cancel if remaining cast time is greater than this value (seconds) |
| `-CastAbility` | string | — | After cancelling, queue casting this ability by name |
| `-CastAbilityOnPlayer` | string string | — | After cancelling, queue casting ability on player (consumes TWO args: ability name, player name) |
| *(any other value)* | string | — | Added to a "do not cancel" list — if the current spell matches any of these names, casting is NOT cancelled |

**Example:**

```lavishscript
; Cancel casting unless it's "Divine Arbitration", then cast "Heal" on tank
OgreBotAPI:CancelCasting["all", "Divine Arbitration", "-CastAbilityOnPlayer", "Heal", "TankName"]
```

### CancelMaintained Args

Each arg is treated as an ability name to cancel. No flags.

```lavishscript
OgreBotAPI:CancelMaintained["Buff A", "Buff B", "Buff C"]
```

### CancelMaintainedForWho Args

Same as CancelMaintained — each arg is an ability name to cancel.

```lavishscript
OgreBotAPI:CancelMaintainedForWho["all", "Buff A", "Buff B"]
```

### Get_AbilityTypeID Args

Gets the ability ID for a given ability type. Args control targeting.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `-NPCRequired` | *(flag)* | — | Sets the target to the current NPC target |
| `-TargetID` / `-ActorID` | int64 | `0` | Sets a specific actor ID to validate abilities against |

**Example:**

```lavishscript
${OgreBotAPI.Get_AbilityTypeID["cure", "-ActorID", "${Target.ID}"]}
```

### Get_AbilityVia Args

Finds an ability matching specified attribute filters. This is the most complex Args handler — it supports flag-based options AND attribute search triplets.

**Flags:**

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `-NPCRequired` | *(flag)* | — | Sets the target to the current NPC target |
| `-TargetID` / `-ActorID` | int64 | `0` | Sets a specific actor ID to validate abilities against |
| `-SkipActorChecks` | *(flag)* | `FALSE` | Skips actor-related validation checks |
| `-SkipAbilityAvailable` | *(flag)* | `FALSE` | Skips IsReady and TimeUntilReady checks on abilities |
| `-ignore` | string | — | Adds a member name to the ignore set, excluding it from GUI checks |
| `-IgnoreGUI` | *(flag)* | `FALSE` | Ignores GUI settings when filtering abilities |
| `-HonorGUI` | *(flag)* | `FALSE` | Strictly honors GUI settings — if a checkbox disables something, exclude it |
| `-offensive` | *(flag)* | `FALSE` | Restricts results to offensive abilities only |
| `SortByReuse` | *(flag)* | `FALSE` | When multiple abilities match, sort by shortest reuse time instead of casting time |

**Attribute Triplets:** Any arg matching a known ability export attribute is treated as a search filter consuming THREE args: `AttributeName`, `Operator`, `Value`. Operators: `equal`, `=`, `==`, `<`, `<=`, `>`, `>=`.

**Example:**

```lavishscript
${OgreBotAPI.Get_AbilityVia["IsInterrupt", "equal", "TRUE", "-NPCRequired"]}
```

### HO_Start Args

Starts a Heroic Opportunity. The method queues the function, which delegates to `Obj_HeroicOpportunity.HO_Start`.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `-SkipTimer` | *(flag)* | `FALSE` | Skips the recently-processed timer check, allowing immediate HO start |
| `-TargetID` / `-ActorID` | int64 | `0` | Specifies a target actor ID to start the HO on |

**Example:**

```lavishscript
OgreBotAPI:HO_Start["all", "-TargetID", "${Target.ID}", "-SkipTimer"]
```

### DoHO_Setup Args

Sets up the DoHO (automated Heroic Opportunity) system. Processes its own flags, then forwards all Args to `DoHO_Set_Enable` as well.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `-LeaveWheelOpen` | *(flag)* | `FALSE` | Does not modify wheel-advancement options for other archetypes |
| `-LeaveStartOpen` | *(flag)* | `FALSE` | Does not modify starter-advancement options for other archetypes |
| `-TimeOut` | int (seconds) | `25` | Timeout for the HO sequence |
| `-NotSoloHO` | *(flag)* | solo | Marks as group HO instead of solo (not fully implemented) |
| `-NoModifyOptions` | *(flag)* | modify | Prevents modifying HO UI options for the group |
| `-AllowCastStack` | *(flag)* | disabled | Allows cast stack to remain active during HO |
| `-TargetID` | int64 | `0` | Target actor ID for the HO |
| `-NumHOsToComplete` | int | `1` | Number of HOs to complete before the task is done |
| `-Force` | *(flag)* | `FALSE` | *(Forwarded to Set_Enable)* — Forces enable even if state unchanged |
| `-PrimeOnly` / `-NoEnable` / `-NoStart` | *(flag)* | `FALSE` | *(Forwarded to Set_Enable)* — Primes infrastructure without enabling |
| `-DelayStart` | int | `1` | *(Forwarded to Set_Enable)* — Delay before starting the HO |

**Example:**

```lavishscript
OgreBotAPI:DoHO_Setup["all", "-TargetID", "${Target.ID}", "-TimeOut", 30, "-NumHOsToComplete", 2]
```

### DoHO_Set_Enable Args

Enables or disables the DoHO system.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `-Force` | *(flag)* | `FALSE` | Forces enable/disable even if current state matches the requested state |
| `-PrimeOnly` / `-NoEnable` / `-NoStart` | *(flag)* | `FALSE` | Primes HO infrastructure but does not enable start/starter/wheel checkboxes |
| `-NoHoAbilities` | *(flag)* | `FALSE` | Prevents disabling HO abilities for same-archetype group members |
| `-TimeOut` | int (seconds) | `25` (minimum) | Overrides the timeout timer (cannot go below 25 seconds) |
| `-DelayStart` | int | `1` | Delay before starting the HO process |

**Example:**

```lavishscript
OgreBotAPI:DoHO_Set_Enable["all", TRUE, "-Force", "-TimeOut", 30]
```

### Get_CursedID Args

Finds a group/raid member with a curse detriment and returns their ID.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `-archetype` | string | *(no restriction)* | Limits search to a specific archetype. Can be specified multiple times for multiple archetypes |
| `-uncurable` | *(flag)* | `FALSE` | Include both curable AND uncurable curses in the search |
| `-uncurableonly` | *(flag)* | `FALSE` | Only return uncurable curses |
| `-GroupOnly` | *(flag)* | `FALSE` | Only check the group, not the raid |

**Example:**

```lavishscript
${OgreBotAPI.Get_CursedID["-archetype", "fighter", "-archetype", "priest", "-GroupOnly"]}
```

### Get_Uncurable Args

Finds a group/raid member with an uncurable condition.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `-GroupOnly` | *(flag)* | `FALSE` | Only check the group, not the raid |

**Example:**

```lavishscript
${OgreBotAPI.Get_Uncurable["Cursed", "-GroupOnly"]}
```

### Cure Method Args

`Cursed`, `AutoCurse`, `AutoCure`, `AutoGroupCure`, and `AutoItemCure` all forward Args to `Object_CureCalled_Entry:Initialize`, which processes cure type keywords and options. Note: `Cursed` and `AutoCurse` automatically prepend `"Curse"` before the Args.

**Cure Type Keywords (each increments the corresponding detriment counter):**

| Keyword | Aliases | Description |
|---------|---------|-------------|
| `any` | — | Marks all detriment types (arcane, elemental, noxious, trauma) |
| `Curse` | — | Marks as curse detriment (auto-prepended by `Cursed`/`AutoCurse`) |
| `arcane` | `a` | Marks as arcane detriment |
| `elemental` | `e` | Marks as elemental detriment |
| `Noxious` | `n` | Marks as noxious detriment |
| `Trauma` | `t` | Marks as trauma detriment |
| `arcaneX` | `aX` | Next arg = count to add for arcane |
| `elementalX` | `eX` | Next arg = count to add for elemental |
| `NoxiousX` | `nX` | Next arg = count to add for noxious |
| `TraumaX` | `tX` | Next arg = count to add for trauma |

**Option Keywords:**

| Keyword | Type | Default | Description |
|---------|------|---------|-------------|
| `exclusive` / `only` | *(flag)* | `FALSE` | Only this cure entry is valid — skip others |
| `DirectTarget` | *(flag)* | `FALSE` | Directly target the player for curing |
| `AutoRemove` | int (seconds) | `8` | Auto-remove this cure entry after N seconds |
| `AutoRemoveMS` | int (ms) | `8000` | Auto-remove after N milliseconds |
| `CustomFlag` | string | — | Adds a custom flag string for script-specific logic |

If no Args are provided, defaults to `any` (all detriment types).

**Example:**

```lavishscript
; Cure arcane and noxious on TankName
OgreBotAPI:AutoCure["healer", "TankName", "arcane", "Noxious"]

; Cure 3 elemental detriments, exclusive, with 10s auto-remove
OgreBotAPI:AutoCure["healer", "TankName", "elementalX", 3, "exclusive", "AutoRemove", 10]
```

### GetActorCountByName Args

Counts actors matching a name, with optional filters.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `-partial` / `-substring` | *(flag)* | exact match | Use substring matching instead of exact match |
| `-distance` | float | `999` | Maximum distance filter — only count actors within this range |
| `-Type` | string | *(no filter)* | Filter by actor type (e.g., `"NPC"`, `"Special"`) |

**Example:**

```lavishscript
${OgreBotAPI.GetActorCountByName["Add Name", "-partial", "-distance", 30]}
```

### HaveMaintained Args

Checks if any maintained spell matches the given ability names. Uses a **mode toggle** pattern.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `TRUE` / `-exact` / `-e` | *(flag)* | — | Sets matching mode to exact for subsequent names |
| `FALSE` / `-partial` / `-p` | *(flag)* | exact match | Sets matching mode to substring for subsequent names |
| *(any other value)* | string | — | An ability name to search for using the current match mode |

Mode toggles can be mixed between names to change matching behavior per name.

**Example:**

```lavishscript
${OgreBotAPI.HaveMaintained["-exact", "Spell A", "-partial", "Buff"]}
```

### Select_Window Args

Selects an option in a Select Window dialog. Used by the method, function, and `Select_Window_GetOption` member.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `-substring` | *(flag)* | exact match | Use substring matching when searching option text |
| `-ReportOnly` | *(flag)* | `FALSE` | Only return the option index, don't click it. **Auto-appended by `Select_Window_GetOption`.** |
| `-Spew` | *(flag)* | `FALSE` | Dump all option text to debug (also enables ReportOnly) |
| `-test` | *(flag)* | `FALSE` | Select the option but do NOT click the OK button |
| `-Debug` | *(flag)* | `FALSE` | Echo debug info about the Args |
| *(any other value)* | string | — | The search text — either a numeric option index or text to match against option labels |

**Example:**

```lavishscript
OgreBotAPI:Select_Window["all", "-substring", "Accept"]
```

### ConsumeItems_ProcessList Args

Passes Args through to the internal consume items handler.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `-fc` / `-forcecombat` | *(flag)* | `FALSE` | Force item consumption even out of combat |
| `-all` | *(flag)* | `FALSE` | Process the entire consume items list instead of stopping early |
| `-st` / `-skiptimers` | *(flag)* | `FALSE` | Skip ready-to-cast timer checks |

**Example:**

```lavishscript
OgreBotAPI:ConsumeItems_ProcessList["all", "-all", "-fc"]
```

### ExecuteEvent Args

Dispatches a LavishScript event by name via `Event[name]:Execute`. All Args are passed directly as positional parameters to whatever event handler is attached. No flags — the meaning of each arg is defined by the specific event handler.

**Example:**

```lavishscript
OgreBotAPI:ExecuteEvent["all", "MyEvent", "param1", "param2"]
```

### ExecuteEvent_JSON Args

Functionally identical to `ExecuteEvent` — dispatches a LavishScript event and passes all Args as positional parameters. Intended for events that receive JSON-encoded strings as arguments.

### ChangeLootOptions Args

Changes group loot settings. Most flags are **group leader only** unless noted.

**Loot Method:**

| Flag | Aliases | Description |
|------|---------|-------------|
| `LO` | `LOL`, `Leader`, `LeaderOnly`, `LeaderOnlyLoot` | Leader Only Loot |
| `FFA` | `Free`, `FreeForAll` | Free For All |
| `Lotto` | — | Lotto |
| `NBG` | `Need`, `NeedBeforeGreed` | Need Before Greed |
| `RR` | `Round`, `Robin`, `RoundRobin` | Round Robin |

**Item Rarity Threshold:**

| Flag | Aliases | Description |
|------|---------|-------------|
| `All` | — | All items |
| `T` | `T+`, `Treasured`, `Treasured+` | Treasured and above |
| `L` | `L+`, `Legendary`, `Legendary+` | Legendary and above |
| `F` | `F+`, `Fabled`, `Fabled+` | Fabled and above |

**Access Control:**

| Flag | Aliases | Description |
|------|---------|-------------|
| `YL` | `YellLeader`, `YellLeaderOnly` | Yell access: Leader Only |
| `YA` | `YellAll` | Yell access: All |
| `ELL` | `EncLockLeader`, `EncLockLeaderOnly` | Encounter lock: Leader Only |
| `ELA` | `EncLockAll` | Encounter lock: All |

**Auto Loot (works for both leader and non-leader):**

| Flag | Aliases | Description |
|------|---------|-------------|
| `AN` | `AutoNone` | Auto loot: None |
| `AG` | `AutoGreed` | Auto loot: Greed |
| `AD` | `AutoDecline` | Auto loot: Decline |
| `AS` | `AutoSplit` | Enable auto split coin |
| `NAS` | `NoAutoSplit` | Disable auto split coin |
| `AL` | `AutoLock` | Enable auto lock encounters |
| `NAL` | `NoAutoLock` | Disable auto lock encounters |

**Example:**

```lavishscript
OgreBotAPI:ChangeLootOptions["all", "FFA", "All", "AG"]
```

### SmartLoot_BuildToonItemsToBeZeroed Args

Args are consumed as sequential pairs: `ToonName`, `ItemName`, `ToonName`, `ItemName`, etc. No flags.

**Example:**

```lavishscript
OgreBotAPI:SmartLoot_BuildToonItemsToBeZeroed["all", "PlayerA", "Item One", "PlayerB", "Item Two"]
```

### AbilityEmbargo_AddRotateTimer / ItemEmbargo_AddRotateTimer Args

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `-g` | string | — | Group member name — if this member is NOT in the group, the timer is not added (conditional guard) |

**Example:**

```lavishscript
OgreBotAPI:AbilityEmbargo_AddRotateTimer[123456, 30, "-g", "PlayerName"]
```

### AbilityTag_AddRotateTagTimer Args

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `-g` | string | — | Group member name — if not in the group, the timer is not added |
| `-m` | string | — | Maintained ability name to monitor for triggered ability tracking |
| `-MBuffer` | int | `1` | Buffer time for determining how long to assume the maintained is active (used with `-m`) |

**Example:**

```lavishscript
OgreBotAPI:AbilityTag_AddRotateTagTimer["all", "MyTag", 30, "-g", "PlayerName", "-m", "Buff Name"]
```

### ChangeOgreBotUIOption / UplinkOptionChange Args

Both methods delegate to the same internal handler. Args are processed as flag/value sequences.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `silent` | *(flag)* | `FALSE` | Suppress relay messages when changing UI options |
| `loud` / `verbose` | *(flag)* | — | Re-enable relay messages |
| *(any other value)* | string pair | — | Treated as a UI element name + value pair. Element names are resolved as `OBUI_<name>`. Values: checkboxes accept `TRUE`/`FALSE`/`Toggle`, text entries accept strings, comboboxes accept option text |

**Example:**

```lavishscript
OgreBotAPI:ChangeOgreBotUIOption["all", "silent", "DisableRoots", "TRUE"]
```

### Report_Back Args

Reports back variable values from group members.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `-Invisible` / `-Silent` | *(flag)* | visible | Uses invisible cross-session command (`!ci` instead of `!c`) |
| `-SendToWho` | string | `irw:${Me.Name}` | Target for where to send the report back variable |
| `-SendToWhere` | string | `oc` | Transport mechanism (`oc`, `irc`, etc.) |
| `-ToIRC` | *(flag)* | — | Shorthand to set SendToWhere to `irc` |
| `-item` | string | — | Checks if named item exists in inventory, returns `TRUE`/`FALSE` |
| `-AdditionalInfo` | string | — | Adds additional info for secondary matching (e.g., weapon subtype) |
| `-resolve_of_slot` | string int64 | — | Consumes TWO args: slot name and LinkID. Gets resolve value for equipment in that slot |
| `-ReportBackVariable` | string | `${Me.Name}` | Variable name used in the set_variable command. `**ME**` is replaced with `${Me.Name}` |

**Example:**

```lavishscript
OgreBotAPI:Report_Back["all", "-Silent", "-item", "Cure Potion"]
```

### Set_CampSpotJump_Handle Args

Sets up campspot jump waypoints for automated jump-based movement patterns. The jump system moves players through a series of points: Start → Jump → End → Completed.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `-JumpDistance` | float | `2` | Distance threshold to trigger jump |
| `-MaxTimer` | int | `10` | Maximum seconds before timeout |

**Example:**

```lavishscript
OgreBotAPI:Set_CampSpotJump_Handle["all", "100,25,-50", "105,30,-50", "110,25,-50", "110,25,-50", "-JumpDistance", 3, "-MaxTimer", 15]
```

### NPC_CastMonitoring Args

Enables NPC cast monitoring with optional scan radius and mob names to monitor.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `-radius` | int | `30` | Scan radius for NPC detection |
| *(default)* | string | — | Each non-flag arg is an NPC name to monitor |

Calling with no Args enables monitoring using the UI checkbox setting. Calling with Args enables monitoring AND adds the specified NPCs to the monitor list.

**Example:**

```lavishscript
; Monitor specific NPCs with custom radius
OgreBotAPI:NPC_CastMonitoring["all", "-radius", 40, "Boss Name", "Add Name"]

; Enable monitoring using UI settings only
OgreBotAPI:NPC_CastMonitoring["all"]
```

### FlagNextPerson Args

Flags the next matching person in rotation. The `_Via` parameter controls matching: `any` (default), `archetype`, or `baseclass`.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `-GroupOnly` | *(flag)* | — | Only search within group (not raid) |
| `-Debug` | *(flag)* | — | Use visible cross-session command for debugging |
| *(default)* | string | — | Each non-flag arg is a search term to match against |

**Example:**

```lavishscript
; Flag next fighter in group
OgreBotAPI:FlagNextPerson[1, "archetype", "fighter", "-GroupOnly"]

; Flag next person matching any criteria
OgreBotAPI:FlagNextPerson[1, "any"]
```

### GetActorCountByType Args

Counts actors matching a specific type within a distance.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `-distance` | float | `999` | Maximum distance to search |
| `-Type` | string | `"Special"` | Actor type to match (e.g., `NPC`, `NamedNPC`, `PC`) |

**Example:**

```lavishscript
; Count named NPCs within 30 meters
variable int count
count:Set[${OgreBotAPI.GetActorCountByType["-Type", "NamedNPC", "-distance", 30]}]
```

---

## Usage Examples

### Basic Movement

```lavishscript
; Move group behind NPC for positioning
OgreBotAPI:SetCS_BehindNPC["notfighter", "Boss Name", 5]
OgreBotAPI:SetCS_InFrontNPC["fighter", "Boss Name", 3]
```

### Combat Control

```lavishscript
; Cast ability on all characters
OgreBotAPI:CastAbility["all", "Divine Arbitration"]

; Cast ability on specific player
OgreBotAPI:CastAbilityOnPlayer["healer", "Heal", "${Tank.Name}"]

; Disable AOEs during burn phase
OgreBotAPI:Set_DisableAllAOEs["all", TRUE]
```

### Auto-Target Setup

```lavishscript
; Setup auto-target for adds that spawn
OgreBotAPI:AutoTarget_AddActor["all", "Add Name", 75, FALSE, TRUE]
OgreBotAPI:AutoTarget_AddActor["all", "Add Name", 50, FALSE, TRUE]
OgreBotAPI:AutoTarget_AddActor["all", "Add Name", 25, FALSE, TRUE]

; Clear when done
OgreBotAPI:AutoTarget_Clear["all"]
```

### Quest Handling

```lavishscript
; Accept a quest
OgreBotAPI:AcceptQuest["all", "Quest Name"]

; Handle dialog choices
OgreBotAPI:ReplyDialog["all", "1"]
OgreBotAPI:ChoiceWindow["all", 2]
```

### Variables for State Tracking

```lavishscript
; Set a variable
OgreBotAPI:Set_Variable["all", "phase", "2"]

; Check variable
if ${OgreBotAPI.Get_Variable["phase"].Equal["2"]}
{
    ; Do phase 2 stuff
}
```

### Checking Status

```lavishscript
if ${OgreBotAPI.InCombat}
{
    ; Combat logic
}

if ${OgreBotAPI.ValidKillTarget}
{
    ; Has valid target
}

variable int64 assistID = ${OgreBotAPI.GetAssistID}
```

---

## Common Patterns in Instance Controllers

### Standard Zone Setup

```lavishscript
call Obj_OgreIH.Set_VariousOptions
call Obj_OgreIH.Set_PriestAscension FALSE
Obj_OgreIH:Set_NoMove
```

### Named NPC Fight Pattern

```lavishscript
function:bool Named1(string _NamedNPC="Boss Name")
{
    variable point3f KillSpot="100.0,25.0,-50.0"

    Obj_OgreIH:SetCampSpot
    Obj_OgreIH:KWL_CCS["${KillSpot}"]
    wait 20

    call Obj_OgreUtilities.PreCombatBuff 5
    call Obj_OgreIH.PortKillAllw "${_NamedNPC}"

    wait 20
    call Obj_OgreUtilities.HandleWaitForCombatWithNPC "${_NamedNPC}"
    wait 10
    call Obj_OgreUtilities.WaitWhileGroupMembersDead

    if ${Actor[namednpc,"${_NamedNPC}"].ID(exists)}
    {
        Obj_OgreIH:Message_FailedToKill["${_NamedNPC}"]
        return FALSE
    }

    return TRUE
}
```

---

## Related Objects

The OgreBotAPI works alongside these helper objects:

- `Obj_OgreIH` - Instance Helper with common instance controller functions
- `Obj_OgreUtilities` - Utility functions
- `Ob_AutoTarget` - Auto-targeting system
- `Ogre_CampSpot` - Camp spot management (see [CampSpot Reference](camp-spot.md))
- `Ogre_Instance_Controller` - Instance controller core

---

## Important Notes

> **:memo: _ForWho Parameter**
>
> Most methods support targeting specific characters. Use `"all"` for everyone, archetype names for groups, or specific character names. Use `"igw:${Me.Name}"` to target all characters in your group.

> **:memo: Async Operations**
>
> Many methods queue commands. Use `wait` or check status members to ensure completion.

> **:warning: Error Handling**
>
> Check return values and use existence checks before accessing actor/object members. Always validate with `(exists)` before accessing `.ID`, `.Name`, or other members.

> **:bulb: Performance**
>
> Use appropriate throttling -- do not spam methods every frame. The bot has built-in pulse timing.

> **:warning: Do NOT use relay groups**
>
> Relay group commands (`relay ${OgreRelayGroup} OgreBotAtom ...`) are deprecated/legacy. Always use the OgreBot cross-session `oc !c` or `oc !ci` commands instead for sending commands to other sessions.

---

## Related Documentation

- [CampSpot System](camp-spot.md) - Detailed positioning and movement reference
- [Coding Practices](coding-practices.md) - Variable naming conventions and code style
