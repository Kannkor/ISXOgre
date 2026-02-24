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

!!! tip
    For a complete breakdown of targeting options including class-specific filters, raid targeting, and the `igw:` prefix system, see the [Cross-Session Commands](cross-session-commands.md) page.

---

## Methods - Categorized

### Movement & Positioning

| Method | Description |
|--------|-------------|
| `KWL(string _ForWho, float _X, float _Y, float _Z, uint _RoomID=0)` | Kill, Walk, Loot - Move to location and engage |
| `KWL_CCS(string _ForWho, float _X, float _Y, float _Z, uint _RoomID=0)` | KWL with Clear Camp Spot |
| `KWL_CRCS(string _ForWho, float _X, float _Y, float _Z, uint _RoomID=0)` | KWL with Clear and Reset Camp Spot |
| `KWL_ClearRCS(string _ForWho)` | Clear and reset camp spot |
| `KWL_Safe(string _ForWho, float _X, float _Y, float _Z, uint _RoomID=0)` | Safe version of KWL with checks |
| `KWNL(string _ForWho, string _NamedLocation)` | KWL to a named location |
| `KW(string _ForWho, string _NameOrID)` | Kill, Walk to actor |
| `KW_CCS(string _ForWho, string _NameOrID)` | KW with Clear Camp Spot |
| `Come2Me(string _MoveTo="${Me.Name}", string _ForWho="all", float _Precision=3)` | Move group to player |
| `Move2Area(float _XPos, float _YPos, string _ForWho, float _Precision=3)` | Move to area |
| `ChangeCampSpot(float _X, float _Y, float _Z)` | Change camp spot location |
| `ChangeCampSpotWho(string _ForWho, float _X, float _Y, float _Z)` | Change camp spot for specific players |
| `FaceActor(string _ForWho, string _ActorNameID)` | Face towards an actor |
| `FaceLoc(string _ForWho, float _X, float _Y, float _Z)` | Face towards a location |
| `FaceAngle(string _ForWho, int _Angle)` | Face a specific angle |
| `SetCS_PositionNPC(string _ForWho, string _NameOrID, float _Distance=3, bool _SkipIfAggro=FALSE)` | Set camp spot positions relative to NPC |
| `SetCS_BehindNPC(string _ForWho, string _NameOrID, float _Distance=3, bool _SkipIfAggro=FALSE)` | Set camp spot behind NPC |
| `SetCS_InFrontNPC(string _ForWho, string _NameOrID, float _Distance=3, bool _SkipIfAggro=FALSE)` | Set camp spot in front of NPC |
| `SetCS_NPC(int _Angle, string _NameOrID, float _Distance=3, bool _SkipIfAggro=FALSE, bool _KWL=TRUE)` | Set camp spot at angle from NPC |
| `PulseCircleMovement(point3f _Loc, ... Args)` | Circular movement pattern around location |
| `Waypoint(string _ForWho, float _X, float _Y, float _Z)` | Set waypoint |
| `Jump(string _ForWho)` | Jump command |
| `JumpKW(string _ForWho, int _Wait1=2, int _Wait2=8)` | Jump during KW |
| `Crouch(string _ForWho)` | Crouch toggle |
| `AutoRun(string _ForWho)` | Toggle autorun |
| `FlyUp(string _ForWho)` | Fly upward |
| `FlyDown(string _ForWho)` | Fly downward |
| `FlyStop(string _ForWho)` | Stop flying |
| `LandFlyingMount(string _ForWho)` | Land a flying mount |
| `Stand(string _ForWho)` | Stand up (cancel feign death) |

### Combat Control

| Method | Description |
|--------|-------------|
| `CastAbility(string _ForWho, string AbilityName, string CalledFrom="OgreBotAPI")` | Cast an ability |
| `CastAbilityOnPlayer(string _ForWho, string AbilityName, string sTarget)` | Cast ability on specific player |
| `CastAbilityOnNPC(string _ForWho, string AbilityName, string _MobNameID, string _CalledFrom)` | Cast ability on NPC |
| `CastAbilityInSeconds(string _ForWho, string AbilityName, float _Seconds, string CalledFrom)` | Cast ability after delay |
| `CastAbilityNoChecks(string _ForWho, string AbilityName, string CalledFrom)` | Cast without readiness checks |
| `CastAbilityNoExport(string _ForWho, string _Ability, string _CastFrom)` | Cast without triggering export |
| `CastAbilityType(string _ForWho, string AbilityType, string CalledFrom, ... Args)` | Cast by ability type |
| `CastRescue(string _ForWho, string CalledFrom, ... Args)` | Cast rescue ability |
| `CastHOIconID(string _ForWho, int _IconID, string CalledFrom)` | Cast ability by HO icon ID |
| `CastBulwarkImmediately(string _ForWho)` | Cast bulwark immediately |
| `Cast_Interrupt(string _ForWho, string _MobNameID, string _CalledFrom, ... Args)` | Cast interrupt on target |
| `UseItem(string _ForWho, string AbilityName)` | Use an item ability |
| `UseItemOnPlayer(string _ForWho, string AbilityName, string sTarget)` | Use item on player |
| `CancelCasting(string _ForWho, ... Args)` | Cancel current casting |
| `CancelCurrentCast(string _ForWho, bool _TorF=TRUE)` | Cancel current cast |
| `CancelMaintained(... Args)` | Cancel maintained spell |
| `CancelMaintainedForWho(string _ForWho, ... Args)` | Cancel maintained for specific players |
| `Pull(string _ForWho, bool _Named=FALSE)` | Pull mob |
| `PetAttack(string _ForWho)` | Pet attack command |
| `PetAssist(string _ForWho)` | Pet assist command |
| `PetOff(string _ForWho)` | Pet passive/off |
| `PetGetLost(string _ForWho)` | Dismiss pet |
| `Evac(string _ForWho)` | Evacuate |
| `Res(string _ForWho)` | Resurrect group |
| `StopRes(string _ForWho)` | Stop resurrection attempts |
| `ImmRes(int _HowMany=2)` | Immediate resurrect |
| `Revive(string _ForWho, string _Option=0, bool _ExactMatch=FALSE)` | Revive at location |
| `Assist(string _AssistWho, string _ForWho)` | Assist another player |
| `AssistForWho(string _ForWho, string _AssistWho)` | Set assist target |
| `Target(string _ForWho, string _Target)` | Target an actor |
| `NoTarget(string _ForWho)` | Clear target |
| `TargetAndDoubleClickActor(string _ForWho, int64 _ActorID)` | Target and interact with actor |

### Combat Settings

| Method | Description |
|--------|-------------|
| `Pause(string _ForWho)` | Pause combat |
| `Resume(string _ForWho)` | Resume combat |
| `NoCasting(string _ForWho, bool _TorF=TRUE)` | Disable/enable casting |
| `Enable_Cures(string _ForWho)` | Enable curing |
| `Disable_Cures(string _ForWho)` | Disable curing |
| `Enable_Dispells(string _ForWho)` | Enable dispelling |
| `Disable_Dispells(string _ForWho)` | Disable dispelling |
| `Enable_Stuns(string _ForWho)` | Enable stuns |
| `Disable_Stuns(string _ForWho)` | Disable stuns |
| `Enable_Interrupts(string _ForWho)` | Enable interrupts |
| `Disable_Interrupts(string _ForWho)` | Disable interrupts |
| `Set_DisableAllAOEs(string _ForWho, bool _DisableAEs=TRUE, ... Args)` | Disable AOE abilities |
| `SetNoDefensive(string _ForWho, bool _Value=TRUE)` | Disable defensive abilities |
| `AddNoOffensiveOn(string _ForWho, string _MobName, bool _ExactMatchOnly=FALSE)` | Add mob to no-offensive list |
| `RemoveNoOffensiveOn(string _ForWho, string _MobName)` | Remove from no-offensive list |
| `ClearNoOffensiveOn(string _ForWho)` | Clear no-offensive list |
| `SetNoReqBowAbilities(string _ForWho, bool _Value=TRUE)` | Set no-ranged requirements |
| `JoustOut(string _ForWho)` | Joust out of range |
| `JoustIn(string _ForWho)` | Joust into range |
| `JoustOff(string _ForWho="Casters")` | Disable jousting |
| `JoustOn(string _ForWho="Melee")` | Enable jousting |
| `NoMove(string _ForWho)` | Disable movement |
| `ForceFollow(string _ForWho)` | Force follow |
| `LetsGo(string _ForWho)` | Start following/movement |
| `HoldUp(string _ForWho)` | Stop and hold |
| `Update_Turbo(string _ForWho, int _Turbo=300, bool _bIgnoreLimits=FALSE)` | Update turbo/speed setting |
| `Rebuff(string _ForWho)` | Trigger rebuff |
| `LoadProfile(string _ForWho, string sProfileName, string _LoadOnlyTab="")` | Load a bot profile |

### Heroic Opportunity (HO)

| Method | Description |
|--------|-------------|
| `HO_Start(string _ForWho, ... Args)` | Start a Heroic Opportunity |
| `HO_Starter(string _ForWho)` | HO starter ability |
| `HO_Starter_Advance(string _ForWho)` | Advance HO starter |
| `HO_Advance(string _ForWho)` | Advance HO wheel |
| `HO_Wheel_Advance(string _ForWho)` | Advance HO wheel specifically |
| `HO_Cancel_Starter(string _ForWho, string _CalledFrom)` | Cancel HO starter |
| `DoHO_Reset(string _ForWho)` | Reset HO system |
| `DoHO_Setup(string _ForWho, ... Args)` | Setup HO parameters |
| `DoHO_Set_Enable(string _ForWho, bool _TorF, ... Args)` | Enable/disable HO |
| `Set_Allow_HOICon(string _ForWho, int _VariableName)` | Allow specific HO icon |
| `Clear_Allow_HOICon(string _ForWho, int _VariableName)` | Clear allowed HO icon |
| `Clear_Allow_HOICons(string _ForWho)` | Clear all allowed HO icons |
| `Set_Disable_HOICon(string _ForWho, int _VariableName)` | Disable specific HO icon |
| `Clear_Disable_HOICon(string _ForWho, int _VariableName)` | Clear disabled HO icon |
| `Clear_Disable_HOICons(string _ForWho)` | Clear all disabled HO icons |

### Cures & Curses

| Method | Description |
|--------|-------------|
| `Cursed(string _ForWho, string _Toon, ... Args)` | Handle cursed player |
| `AutoCurse(string _ForWho, string _Toon, ... Args)` | Auto-cure curses |
| `AutoCure(string _ForWho, string _Toon, ... Args)` | Auto-cure ailments |
| `AutoItemCure(string _ForWho, ... Args)` | Auto-cure using items |
| `AutoGroupCure(string _ForWho, string _Toon, ... Args)` | Auto group cure |
| `GroupCure(string _ForWho)` | Cast group cure |
| `CancelDetrimental(string _ForWho, int _BackDropID, int _MainID)` | Cancel detrimental effect |
| `Dispell(string _ForWho, string _Value)` | Dispell target |
| `DispellNPCWithSpell(string _ForWho, string _NPCNameOrID)` | Dispell NPC with spell |
| `DispellNPCWithItem(string _ForWho, string _NPCNameOrID)` | Dispell NPC with item |
| `DispellNPCWithAny(string _ForWho, string _NPCNameOrID)` | Dispell NPC with any method |

### Auto-Target System

| Method | Description |
|--------|-------------|
| `AutoTarget_AddActor(string _ForWho, string _ActorName, int _HP=0, bool _CheckCollision=FALSE, bool _AggroOnGroupOnly=TRUE, int _MaxHP=0, bool _AggroOnNonFighterOnly=FALSE, bool _AggroOnNotMe=FALSE)` | Add actor to auto-target list |
| `AutoTarget_RemoveActor(string _ForWho, string _ActorName)` | Remove actor from list |
| `AutoTarget_ClearActors(string _ForWho)` | Clear auto-target actors |
| `AutoTarget_Clear(string _ForWho)` | Clear entire auto-target system |
| `AutoTarget_Enable(string _ForWho, string _Key="")` | Enable auto-targeting |
| `AutoTarget_Disable(string _ForWho, string _Key="")` | Disable auto-targeting |
| `AutoTarget_SetScanRadius(string _ForWho, int _Value=50)` | Set scan radius |
| `AutoTarget_SetScanHeight(string _ForWho, int _Value=5)` | Set scan height |
| `AutoTarget_SetRescanTime(string _ForWho, int _Value=50)` | Set rescan interval |

### Variables & Internal State

| Method | Description |
|--------|-------------|
| `Set_Variable(string _ForWho, string _VariableName, string _VariableValue)` | Set a custom variable |
| `Get_Variable(string _VariableName)` | Get custom variable value (member) |
| `Clear_Variable(string _ForWho, string _VariableName)` | Clear a variable |
| `Clear_Variables(string _ForWho)` | Clear all variables |
| `Set_InternalVariable(string _ForWho, string _VariableName, string _VariableValue)` | Set internal variable |
| `Get_InternalVariable(string _VariableName)` | Get internal variable (member) |
| `Clear_InternalVariable(string _ForWho, string _VariableName)` | Clear internal variable |
| `Clear_InternalVariables(string _ForWho)` | Clear all internal variables |
| `Spew_Variables()` | Debug output all variables |
| `Spew_InternalVariables()` | Debug output internal variables |

### Zone & Travel

| Method | Description |
|--------|-------------|
| `Zone(string _ForWho)` | Zone through door |
| `ZoneDoor(string _DoorOption=1)` | Zone through specific door |
| `ZoneDoorForWho(string _ForWho, string _DoorOption=1)` | Zone door for specific players |
| `ZoneInto(string _ForWho, string _ZoneName, string _ActorName, int _DoorOption=0)` | Zone into specific zone |
| `Travel(string _ForWho, string _ToWhere, bool _ExactMatch=FALSE, string _MultipleZoneOption)` | Travel to location |
| `FastTravel(string _ForWho, string _ToWhere, ... Params)` | Fast travel |
| `TravelBell(string _ForWho, string _ToWhere, bool _ExactMatch=FALSE, string _MultipleZoneOption)` | Use travel bell |
| `TravelDruid(string _ForWho, string _ToWhere, bool _ExactMatch=FALSE, string _MultipleZoneOption)` | Use druid ring |
| `TravelSpires(string _ForWho, string _ToWhere, bool _ExactMatch=FALSE, string _MultipleZoneOption)` | Use wizard spires |
| `GetToGH(string _ForWho)` | Get to guild hall |
| `CallGH(string _ForWho)` | Call to guild hall |
| `GetFlag(string _ForWho)` | Get guild rally flag |
| `UseFlag(string _ForWho)` | Use guild rally flag |
| `PortalToGuildHall(string _ForWho)` | Portal to guild hall |
| `CoV(string _ForWho, string _TravelOption, string _ToonOption, bool _AllowSameZone)` | Chroma of Valor travel |
| `ToggleZoneReuse(string _ForWho)` | Toggle zone reuse |
| `ResetZone(string _ForWho, string _ZoneName)` | Reset a zone |
| `ZoneResetAll(string _ForWho)` | Reset all zones |

### Actor Interaction

| Method | Description |
|--------|-------------|
| `Actor_Click(string _ForWho, string _NameOrID, bool _ExactName=FALSE)` | Click on actor |
| `Actor_ClickQueued(string _ForWho, string _NameOrID, bool _ExactName=FALSE, int _WaitTime=40)` | Queued actor click |
| `HailNPC(string _ForWho, string _NameOrID)` | Hail an NPC |
| `ApplyVerb(string _ActorName, string _Verb)` | Apply verb to actor |
| `ApplyVerbID(int64 _ActorID, string _Verb)` | Apply verb by actor ID |
| `ApplyVerbForWho(string _ForWho, string _ActorName, string _Verb)` | Apply verb for specific players |
| `ApplyVerbIDForWho(string _ForWho, int64 _ActorID, string _Verb)` | Apply verb by ID for specific players |
| `ApplyVerbQueuedForWho(string _ForWho, string _ActorName, string _Verb)` | Queued verb application |
| `ApplyVerbIDQueuedForWho(string _ForWho, int64 _ActorID, string _Verb)` | Queued verb by ID |

### Merchant & Economy

| Method | Description |
|--------|-------------|
| `BuyFromMerchant(string _ForWho, string _ItemName, int _Value=1)` | Buy from merchant |
| `SellToMerchant(string _ForWho, string _ItemName, int _Value=1)` | Sell to merchant |
| `OpenAndBuyFromMerchant(string _ForWho, string _MerchantName, string _ItemName, int _Value=1)` | Open merchant and buy |
| `OpenAndBuyFromMerchantXTimes(string _ForWho, string _MerchantName, string _ItemName, int _Value=1, int _HowManyTimes=1)` | Buy multiple times |
| `RepairGear(string _ForWho, bool _Force=FALSE)` | Repair gear |

### Quests & Dialogs

| Method | Description |
|--------|-------------|
| `AcceptQuest(string _ForWho, string _QuestName)` | Accept a quest |
| `ForceAcceptQuest(string _ForWho, string _QuestName)` | Force accept quest |
| `DeleteQuest(string _ForWho, string _QuestName)` | Delete a quest |
| `ShareQuest(string _ForWho, string _QuestName)` | Share a quest |
| `ShareMission(string _ForWho, string _QuestName)` | Share mission |
| `ShareAllMissions(string _ForWho)` | Share all missions |
| `ShareQuestsForZone(string _ForWho, string _ZoneName)` | Share quests for zone |
| `CompareQuestUpdate(string _ForWho, string _QuestName, ... _QuestInfo)` | Compare quest progress |
| `ChoiceWindow(string _ForWho, int _Choice=1)` | Click choice window option |
| `OK_Button(string _ForWho)` | Click OK button |
| `ReplyDialog(string _ForWho, string _Choice=1)` | Reply to dialog |
| `ReplyDialogClose(string _ForWho)` | Close reply dialog |
| `ConversationBubble(string _ForWho, int _DoorOption=1)` | Click conversation bubble |
| `Select_Window(string _ForWho, ... Args)` | Select window option |
| `Select_Window_Cancel(string _ForWho)` | Cancel select window |
| `Select_Window_Spew(string _ForWho)` | Debug select window |
| `Select_Zone_Version(string _ForWho, string _Option)` | Select zone version |
| `AcceptReward(string _ForWho, string _Selection=0, int64 _WindowID=0)` | Accept quest reward |
| `AcceptNoChoiceReward(int64 _WindowID=0)` | Accept reward with no choice |

### Items & Inventory

| Method | Description |
|--------|-------------|
| `DestroyItem(string _ForWho, string _ItemName, uint _Charges=0)` | Destroy item with checks |
| `DestroyItem_NoChecks(string _ForWho, string _ItemName)` | Destroy item without checks |
| `DestroyItemByID_NoChecks(string _ForWho, int64 _ItemID)` | Destroy item by ID |
| `ExamineInventoryItem(string _ForWho, string _ItemName)` | Examine item |
| `ExamineAllOfItem(string _ForWho, ... _Items)` | Examine all of item type |
| `CloseExamine()` | Close examine window |
| `CloseExamineWindow(string _ForWho)` | Close examine window for all |
| `CloseAllExamine(string _ForWho)` | Close all examine windows |
| `Drink_Alcohol(string _ForWho, string _ItemName)` | Drink alcohol item |
| `Unpack(string _ForWho, string _ItemName, string _UnpackOption)` | Unpack item |
| `Unpack_Quantity(string _ForWho, string _ItemName, uint Quantity, string _UnpackOption)` | Unpack quantity |
| `Unpack_EmpyralStones(string _ForWho, string _Option)` | Unpack Empyral stones |
| `Unpack_PlanarStones(string _ForWho, string _Option)` | Unpack Planar stones |
| `Unpack_Familiars(string _ForWho)` | Unpack familiar crates |
| `Consume_Familiars(string _ForWho)` | Consume familiars for XP |
| `Unpack_Consume_Familiars(string _ForWho)` | Unpack and consume familiars |
| `Consume_Status_Tokens(string _ForWho, uint _Amount)` | Consume status tokens |
| `Consume_Status_Ingots(string _ForWho, uint _Amount)` | Consume status ingots |
| `ConsumeItems_ProcessList(string _ForWho, ... Args)` | Process consume item list |
| `ConsumeDeityBaubles(string _ForWho)` | Consume deity baubles |

### Equipment & Adornments

| Method | Description |
|--------|-------------|
| `EquipCharm(string _ForWho, int _Value=1)` | Equip charm |
| `ChangeBeltAdorn(string _ForWho, string _AdornType, bool _Unequip=TRUE, bool _SkipAdornMoving=FALSE)` | Change belt adornment |
| `ApplyTempAdorn(string _ForWho, string _Adorn, string _Slot)` | Apply temporary adornment |
| `PoP_TempAdorns(string _ForWho, string _AdornmentType, bool _Overwrite)` | Apply PoP temp adorns |
| `CheckGear(string _ForWho, string _ReportIfValueEqualOrLess)` | Check gear condition |

### Mount & Familiar

| Method | Description |
|--------|-------------|
| `Mount(string _ForWho)` | Toggle mount |
| `Force_MountOn(string _ForWho)` | Force mount on |
| `Force_MountOff(string _ForWho)` | Force mount off |
| `CheckMountTraining(string _ForWho, bool _ForceCheck=FALSE)` | Check mount training |
| `Check_Familiar(string _ForWho)` | Check familiar |
| `Summon_Familiar(string _ForWho)` | Summon familiar |

### Communication & Events

| Method | Description |
|--------|-------------|
| `Message(string _ForWho, string _Message, bool _Noise=FALSE, string NoiseToPlay)` | Send message |
| `Message_Relay(string _ForWho, string _Message, bool _Noise=FALSE, string NoiseToPlay)` | Relay message |
| `Message_NT(string _ForWho, string _Message, bool _Noise=FALSE, string NoiseToPlay)` | Message no-throttle |
| `TTS(string _ForWho, string _Message)` | Text-to-speech |
| `Countdown(string _ForWho, int _Time=10)` | Countdown timer |
| `OnScreenTimer(string _ForWho, float _Time, int _Slot, string _Message, int _MinUpdateTimer, float _ExtraTimer, string _ExtraTimerMessage)` | On-screen timer |
| `OnScreenTimerReset(string _ForWho, int _Slot)` | Reset on-screen timer |
| `Announce_AddEntry(string _ForWho, string _Ability, string _AnnounceTo, string _AnnounceText)` | Add announcement |
| `ChatEvent_AddEntry(string _ForWho, string _Text, bool _OC, bool _Ding, string _Code)` | Add chat event |
| `ChatEvent_RemoveEntry(string _ForWho, string _Text)` | Remove chat event |
| `SpawnEvent_AddEntry(string _ForWho, string _Text, bool _OC, bool _Ding, string _Code)` | Add spawn event |
| `SpawnEvent_RemoveEntry(string _ForWho, string _Text)` | Remove spawn event |
| `DespawnEvent_AddEntry(string _ForWho, string _Text, bool _OC, bool _Ding, string _Code)` | Add despawn event |
| `DespawnEvent_RemoveEntry(string _ForWho, string _Text)` | Remove despawn event |
| `ExecuteEvent(string _ForWho, string _EventName, ... Args)` | Execute custom event |
| `ExecuteEvent_JSON(string _ForWho, string _EventName, ... Args)` | Execute event with JSON |
| `InjectChat(string _ForWho, string _Chat)` | Inject chat command |
| `Send_Tell(string Speaker, string _Target, string Message)` | Send tell message |
| `Invite(string _ForWho, string _WhoToInvite, bool _RaidInvite=FALSE)` | Invite to group/raid |

### Group/Raid Management

| Method | Description |
|--------|-------------|
| `Mentor(string _Value)` | Mentor to player |
| `Unmentor(string _ForWho)` | Remove mentoring |
| `Disband(string _ForWho)` | Leave group |
| `MakeLeader(string _ForWho, string _Leader)` | Make group leader |
| `FlagToon(string _ForWho, int _Value=1)` | Flag toon for tracking |
| `UnflagToon(string _ForWho, int _Value=1)` | Unflag toon |
| `UnflagAll(string _ForWho)` | Unflag all toons |
| `SpewFlags(string _ForWho)` | Debug output flags |
| `FlagToonNextPerson(int _Mark=1)` | Flag next person |
| `MarkToon(string _ForWho)` | Mark toon |
| `UnmarkToon(string _ForWho)` | Unmark toon |
| `SetRelayGroup(string _ForWho, string _Value)` | Set relay group |
| `SetRelayGroupToDefault(string _ForWho)` | Reset relay group |
| `Spew_RelayGroup(string _ForWho)` | Debug relay group |

### UI Control

| Method | Description |
|--------|-------------|
| `ChangeOgreBotUIOption(string _ForWho, ... Args)` | Change OgreBot UI option |
| `ChangeCastStackListBoxItem(string _ForWho, string _Object, string _Value, bool _SilentMode=FALSE)` | Change cast stack listbox |
| `ChangeCastStackListBoxItemByTag(string _ForWho, string _Object, string _Value, string _Partial, bool _SilentMode)` | Change by tag |
| `UplinkOptionChange(string _ForWho, ... Args)` | Change uplink option |
| `ToggleMainWindow(string _ForWho)` | Toggle main window |
| `ToggleConsoleWindow(string _ForWho, string _Value)` | Toggle console |
| `ShowOgreConsole(string _ForWho, bool _Value)` | Show/hide OgreConsole |
| `CloseWindow(string _ForWho)` | Close window |
| `InputTextWindow_AddText(string _ForWho, string _Text)` | Add text to input window |
| `InputTextWindow_ClearText(string _ForWho)` | Clear input window |
| `InputTextWindow_Accept(string _ForWho)` | Accept input window |
| `ResetCameraAngle(string _ForWho)` | Reset camera |
| `Set_CameraPitch(string _ForWho, int _Pitch)` | Set camera pitch |
| `SetMousePosition(float _X, float _Y)` | Set mouse position |
| `SetMousePosition_Middle()` | Center mouse |

### Loot System

| Method | Description |
|--------|-------------|
| `HandleLootWindow(string _ForWho, uint _LootWindowID)` | Handle loot window |
| `LootWindowLootAll(string _ForWho)` | Loot all from window |
| `ChangeLootOptions(string _ForWho, ... Args)` | Change loot options |
| `SetAutoLootMode(string _ForWho, int _Value, bool _Silent)` | Set auto-loot mode |
| `ResetActorsLooted(string _ForWho)` | Reset looted actors list |
| `SmartLoot_ReloadDataFromFile(string _ForWho)` | Reload smart loot data |
| `SmartLoot_LOL_AssignPlayer_Item(string _ForWho, string _LootWindowID, string _PlayerToAssignTo, string _ItemName)` | Assign loot to player |
| `SmartLoot_BuildToonItemsToBeZeroed(string _ForWho, ... Args)` | Build items to zero |
| `SmartLoot_ProcessToonItemsToBeZeroed(string _ForWho)` | Process zeroed items |
| `Loot_SmartAssign_Add()` | Add smart assign |
| `Loot_SmartAssign_Update()` | Update smart assign |

### Alias System

| Method | Description |
|--------|-------------|
| `Alias_AddEntry(string _ForWho, string _Alias, string _Value, _NoRaid=FALSE)` | Add alias |
| `Alias_RemoveEntry(string _ForWho, string _Text)` | Remove alias |
| `Alias_ChangeEntry(string _ForWho, string _From, string _To, bool _SilentMode=FALSE)` | Change alias |
| `Alias_ChangeEntryAlias(string _ForWho, string _From, string _To, bool _SilentMode)` | Change alias reference |
| `ForceAliasUpdate(string _ForWho)` | Force alias cache update |

### Ability Embargo/Rotation

| Method | Description |
|--------|-------------|
| `AbilityEmbargo_AddRotateTimer(int64 _AbilityID, uint _Duration, ... Args)` | Add ability rotation timer |
| `AbilityEmbargo_ResetAllAbilityEmbargos(string _ForWho)` | Reset all ability embargos |
| `AbilityEmbargo_ResetAbilityEmbargo(string _ForWho, string _AbilityName)` | Reset specific embargo |
| `ItemEmbargo_AddRotateTimer(int64 _AbilityID, uint _Duration, ... Args)` | Add item rotation timer |
| `AbilityTag_AddRotateTagTimer(string _ForWho, string _TagName, uint _Duration, ... Args)` | Add tag timer |
| `AbilityTag_ResetAllAbilityTagEmbargos(string _ForWho)` | Reset all tag embargos |
| `AbilityTag_ResetAbilityTagEmbargo(string _ForWho, string _TagName)` | Reset tag embargo |
| `AbilityTag_ResetAllAbilityTagAllows(string _ForWho)` | Reset all tag allows |
| `AbilityTag_ResetAbilityTagAllow(string _ForWho, string _TagName)` | Reset tag allow |

### Intercept System

| Method | Description |
|--------|-------------|
| `SetUpFor_Intercept(string _ForWho)` | Setup intercept |
| `ResetFor_Intercept(string _ForWho)` | Reset intercept |
| `SetUpFor_Dispells(string _ForWho)` | Setup dispells |
| `ResetFor_Dispells(string _ForWho)` | Reset dispells |

### Ascension & Deity

| Method | Description |
|--------|-------------|
| `AscensionEmbargo_Add_DoNotCombo(string _ForWho, string _sItemToAdd)` | Add to no-combo list |
| `AscensionEmbargo_Remove_DoNotCombo(string _ForWho, string _sItemToAdd)` | Remove from no-combo |
| `AscensionEmbargo_Change_Disable_Status(string _ForWho, string _sItemToAdd, string ObjectValue, bool _SilentMode)` | Change disable status |
| `DisplayMyAscensionCombos()` | Display ascension combos |
| `GenerateMyAscensionCombos()` | Generate ascension combos |
| `GuidedAscension(string _ForWho, int64 _Amount)` | Use guided ascension |
| `SpendDeityPoints(string _ForWho, string _SpendOn, int _Spend)` | Spend deity points |
| `AltarOfTheAncients(string _ForWho)` | Use Altar of Ancients |
| `ArcannaseEffigyOfRebirth(string _ForWho)` | Use Arcannase Effigy |

### Research & Training

| Method | Description |
|--------|-------------|
| `CheckResearch(string _ForWho, bool _ForceReport=FALSE)` | Check research status |
| `Research_Material_Check(string _ForWho)` | Check research materials |
| `CheckMercenaryTraining(string _ForWho)` | Check mercenary training |
| `AutoConsumeTemporaryFamiliarExperience(string _ForWho)` | Consume familiar XP items |
| `AutoConsumeTemporaryMountTrainingReduction(string _ForWho)` | Consume mount training items |
| `AutoConsumeTemporaryResearchReduction(string _ForWho)` | Consume research reduction items |

### Bot Control

| Method | Description |
|--------|-------------|
| `Reload_Bot(string _ForWho)` | Reload bot |
| `Reload_DevBot(string _ForWho)` | Reload dev bot |
| `End_Bot(string _ForWho)` | End bot script |
| `ExitClient(string _ForWho, int _Seconds=30)` | Exit client |
| `CampToDesktop(string _ForWho, bool _LoginOnly=FALSE)` | Camp to desktop |
| `PlayAtCharacterSelect()` | Play at character select |
| `LoginAtCharacterSelect(string _ForWho, string _CharName)` | Login character |
| `KronoWindowCheck()` | Check Krono window |
| `RedeemKrono(string _ForWho)` | Redeem Krono |
| `F2PWindow_Check(string _ForWho)` | Check F2P window |
| `F2PWindow_SetOptions(string _ForWho, uint _Minutes)` | Set F2P options |

### Miscellaneous

| Method | Description |
|--------|-------------|
| `SetDebugMode(bool _TorF=TRUE)` | Enable debug mode |
| `DebugMessage(string _Message, string _Message2)` | Output debug message |
| `Special(string _ForWho)` | Special command |
| `SpecialZoneSpecific(string _ForWho)` | Zone-specific special |
| `RunWalk(string _ForWho)` | Toggle run/walk |
| `ResStone(string _ForWho)` | Use resurrection stone |
| `DungeonMakerCancel(string _ForWho)` | Cancel dungeon maker |
| `CheckPackPony(string _ForWho, bool _ForceCheck=FALSE)` | Check pack pony |
| `GetToConcentration(string _ForWho, int _Concentration)` | Reduce concentration |
| `FixCastAfterZoneBug()` | Fix cast-after-zone bug |
| `FlushQueued()` | Flush queued commands |
| `ReloadExport()` | Reload ability export |
| `ReloadOgreIRC()` | Reload OgreIRC |
| `AfterProfileLoad()` | After profile load hook |

---

## Members (Properties)

Members return values and are accessed via `${OgreBotAPI.MemberName[params]}`.

### Status & Checks

| Member | Return | Description |
|--------|--------|-------------|
| `IsReady()` | bool | Is OgreBotAPI ready |
| `Version()` | string | API version |
| `Paused()` | bool | Is bot paused |
| `InCombat()` | bool | Is in combat |
| `InInstance()` | bool | Is in instance |
| `InGuildHallZone()` | bool | Is in guild hall |
| `InHouseZone()` | bool | Is in house zone |
| `InHouseAccessZone()` | bool | Is in house access zone |
| `InBattleGround()` | bool | Is in battleground |
| `Zoning()` | bool | Is currently zoning |
| `AtCharacterSelect()` | bool | At character select screen |
| `KWAble()` | bool | Can use KW commands |
| `ValidKillTarget()` | bool | Has valid kill target |
| `CancelCurrentCast()` | bool | Is cancel cast active |
| `QueuedCommands()` | bool | Has queued commands |

### Combat Information

| Member | Return | Description |
|--------|--------|-------------|
| `GetAssistID()` | int64 | Current assist target ID |
| `IsAssisting()` | bool | Is currently assisting |
| `InControlOfAssisting()` | bool | Is in control of assist |
| `NPCsWithinRange(string AbilityName)` | int | NPCs in ability range |
| `Get_InterruptID(int64 _ActorID)` | int64 | Get interrupt ability ID |

### Group/Raid Information

| Member | Return | Description |
|--------|--------|-------------|
| `GroupInZone(float _Within=0)` | bool | Is group in zone |
| `NumGroupWithCurses()` | int | Group members with curses |
| `NumRaidWithCurses()` | int | Raid members with curses |
| `Get_GroupCurseCount()` | int | Group curse count |
| `Get_RaidCurseCount()` | int | Raid curse count |
| `Get_GroupUncurableCurseCount()` | int | Uncurable curse count |
| `Get_CursedID(... Args)` | int64 | Get cursed player ID |
| `Get_Uncurable(string _Type, ... Args)` | int64 | Get uncurable effect |

### Heroic Opportunity

| Member | Return | Description |
|--------|--------|-------------|
| `HO_Visible()` | bool | Is HO visible |
| `HO_Starter_Visible()` | bool | Is HO starter visible |
| `HO_Wheel_Visible()` | bool | Is HO wheel visible |
| `HO_Wheel_Name()` | string | Current HO wheel name |
| `HO_Starter_Class()` | string | HO starter class |
| `HO_Class_Available(string _ForWho)` | bool | Is HO class available |
| `HO_Wheel_Class_Available(string _ForWho)` | bool | Is wheel class available |
| `HO_Starter_Class_Available(string _ForWho)` | bool | Is starter class available |
| `HO_TargetID()` | int64 | HO target ID |
| `DoHO_Get_Enabled()` | bool | Is DoHO enabled |
| `DoHO_Get_Primed()` | bool | Is DoHO primed |
| `DoHo_Get_TargetID()` | int64 | DoHO target ID |
| `DoHO_Get_HOerID()` | int64 | DoHO caster ID |
| `Get_HOIconAbility(string _HOIconID, ... _Options)` | int64 | Get ability by HO icon |

### Variables

| Member | Return | Description |
|--------|--------|-------------|
| `Get_Variable(string _VariableName)` | string | Get variable value |
| `Get_Variable_Bool(string _VariableName)` | bool | Get variable as bool |
| `Get_VariableExists(string _VariableName)` | bool | Does variable exist |
| `Get_InternalVariable(string _VariableName)` | string | Get internal variable |
| `Get_InternalVariableExists(string _VariableName)` | bool | Does internal var exist |

### Actor/Target Information

| Member | Return | Description |
|--------|--------|-------------|
| `GetMobID(string _MobNameID)` | int64 | Get mob ID from name/ID |
| `GetActorCountByName(string _ActorName, ... Args)` | int | Count actors by name |
| `GetFarthestActorFrom(string _FindActorName, string _FromActorNameID, float _MinDistance)` | int64 | Get farthest actor |
| `GameDistanceToActor(string _NameOrID)` | float | Distance to actor |
| `GetActorModelSize(int64 _ActorID)` | float | Actor model size |
| `GetMyModelSize()` | float | My model size |
| `ActorHasQuest(int64 _ActorID)` | bool | Actor has quest |

### Ability Information

| Member | Return | Description |
|--------|--------|-------------|
| `GetAbilityID(string AbilityName)` | int64 | Get ability ID |
| `Get_AbilityInfo(string _AbilityNameID, string _Member)` | string | Get ability info |
| `Get_AbilityInfo_RawData(string _AbilityName, string _Member)` | string | Get raw ability data |
| `Get_AbilityShortName(string _AbilityName)` | string | Get short ability name |
| `Get_AbilityTypeID(string AbilityType, ... Args)` | int64 | Get ability type ID |
| `Get_AbilityVia(... Args)` | int64 | Get ability via params |
| `AbilityReady(string _ForWho, string AbilityName, int64 _ActorID)` | bool | Is ability ready |
| `CheckNoReqBowAbilities()` | bool | Check no-bow-req setting |

### Equipment Information

| Member | Return | Description |
|--------|--------|-------------|
| `Get_EquipmentModifierValue(string _Slot, string _Modifier)` | string | Get equipment modifier |
| `EquipmentSlotAvailable(string _Slot)` | bool | Is slot available |
| `EquipmentSlotNumAvailable(int _Slot)` | bool | Is slot num available |
| `ConvertSlotArrayToSlot(int _SlotArray)` | int | Convert slot array |
| `RoR_Epic_Available()` | bool | Is RoR epic available |
| `RoR_Epic_Ready()` | bool | Is RoR epic ready |
| `RoR_Epic_AbilityID()` | int64 | RoR epic ability ID |

### Adornment Information

| Member | Return | Description |
|--------|--------|-------------|
| `Get_AdornmentColour(string _IconID)` | string | Get adorn color |
| `IsAdornmentColour(string _IconID, string _Colour)` | bool | Check adorn color |
| `Get_NumAdornmentsOfColour(string _Slot, string _Colour)` | int | Count adorns by color |
| `ConvertAdornToSlot(string _AdornHash, int _Slot)` | string | Convert adorn to slot |
| `ConvertAdornToRemoveSlot(string _AdornHash)` | string | Convert for removal |

### Zone Information

| Member | Return | Description |
|--------|--------|-------------|
| `ZoneName(string _Input)` | string | Clean zone name |
| `CleanZoneName(string _ZoneName)` | string | Sanitized zone name |
| `RemoveZoneNumber(string _Input)` | string | Remove zone number |
| `RemoveZoneNumberOnly(string _Input)` | string | Remove only number |
| `KWL_ZoneName()` | string | KWL zone name |
| `KWL_ZoneName_WithNum()` | string | KWL zone with number |
| `RoomID()` | string | Current room ID |
| `Travel_Get_ZoneDoorValue(string _DoorOption)` | int | Get zone door value |
| `GuildFlagLocation()` | string | Guild flag location |

### Flags & Markers

| Member | Return | Description |
|--------|--------|-------------|
| `ToonMarked()` | bool | Is toon marked |
| `ToonFlagged(int _Value)` | bool | Is toon flagged |

### Loot Information

| Member | Return | Description |
|--------|--------|-------------|
| `LootWindowExists()` | bool | Does loot window exist |
| `Get_LootWindowID()` | int64 | Get loot window ID |
| `RewardWindow_Get_WindowID()` | uint | Get reward window ID |
| `Get_RewardName(string _Selection, int64 _WindowID)` | string | Get reward name |
| `Get_RewardID(string _Selection, int64 _WindowID)` | int | Get reward ID |
| `Get_RewardLinkID(string _Selection, int64 _WindowID)` | string | Get reward link ID |

### Detrimental Effects

| Member | Return | Description |
|--------|--------|-------------|
| `DetrimentalInfo(int _MainID, int _BackDropID, uint _ActorID, string _Return)` | string | Get detrimental info |
| `DetrimentalInfo_ref(persistentref DotToCheck, uint _ActorID, string _Return)` | string | Get detrimental by icon ref |

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

| Member | Return | Description |
|--------|--------|-------------|
| `HaveQuest(string _QuestName)` | bool | Do I have quest |
| `ReplyDialog_ReplyExists(string _ForWho, string _Choice, bool _ExactMatch)` | int | Does reply exist |
| `Select_Window_GetOption(... Args)` | int | Get select window option |

### Utility

| Member | Return | Description |
|--------|--------|-------------|
| `CommandForMe(string _ForWho)` | bool | Is command for me |
| `Between(int64 _ValueToCompare, int64 _Value1, int64 _Value2)` | bool | Is value between |
| `BetweenFloat(float _ValueToCompare, float _Value1, float _Value2)` | bool | Float between |
| `To_Int(string _Value)` | int64 | Convert to int |
| `To_Float(string _Value)` | float | Convert to float |
| `To_Number(string _Value)` | string | Convert to number string |
| `Get_Archetype(string _Value)` | string | Get archetype |
| `Get_Role(string _Value)` | string | Get role |
| `Get_BaseClass(string _Value)` | string | Get base class |
| `Get_Turbo()` | int | Get turbo value |
| `Get_Alias(string _Alias)` | string | Get alias value |
| `Get_Alias2(string _Alias)` | string | Get alias value (alt) |
| `Get_ScriptBaseName(string _Path, bool _RemoveExtension)` | string | Get script basename |
| `FileExists(string _Path)` | bool | Does file exist |
| `MD5(string _Input)` | string | MD5 hash |
| `Clean(string _Input)` | string | Clean string |
| `CleanNameWithSpaces(string _Input)` | string | Clean name with spaces |
| `ItemCount(string _ItemName)` | int | Count items |
| `CurrentCharacter()` | string | Current character name |
| `UplinkName()` | string | Uplink session name |
| `IsCastingWindowVisible()` | bool | Is casting window visible |
| `CursorActor_Tooltip_Visible()` | bool | Is cursor tooltip visible |
| `CursorActor_Tooltip_Text()` | string | Cursor tooltip text |
| `PointAtAngle(int _Angle, string _NameOrID, float _Distance)` | point3f | Point at angle from actor |
| `PointAtAngleNoSize(int _Angle, string _NameOrID, float _Distance)` | point3f | Point ignoring size |
| `Get_Seconds(int64 _Seconds)` | int64 | Get seconds component |
| `Get_Minutes(int64 _Seconds)` | int64 | Get minutes component |
| `Get_Hours(int64 _Seconds)` | int64 | Get hours component |
| `ConvertSecondsToHMS(int64 _Seconds)` | string | Convert to H:M:S |
| `SpewStat(string _Command, bool _AddLabel)` | string | Spew stat info |
| `Get_DeityPoints(string _Value)` | int | Get deity points |

### CSP & Developer

| Member | Return | Description |
|--------|--------|-------------|
| `Get_CSP()` | bool | Get CSP status |
| `NG()` | bool | No gravity status |
| `InTesting()` | bool | In testing mode |
| `Get_DebugLoading()` | bool | Debug loading enabled |
| `IsAPC(string _Type)` | bool | Is actor a PC |
| `ERE(int _EqualOrAbove)` | bool | Elite raid status |
| `HaveSickness()` | bool | Has resurrection sickness |
| `NPCUnkillableBug()` | bool | NPC unkillable bug check |
| `CityRestrictions()` | bool | City restrictions apply |
| `UnauthPCsNearMe(float _Distance)` | bool | Unauthorized PCs nearby |
| `CheckNoOffensiveOn()` | bool | No-offensive list check |
| `CheckNoDefensiveOn()` | bool | No-defensive check |

### Ability Embargo

| Member | Return | Description |
|--------|--------|-------------|
| `AbilityTag_GetTagEmbargoTimeRemaining(string _TagName)` | float | Tag embargo time left |
| `AbilityTag_GetTagAllowTimeRemaining(string _TagName)` | float | Tag allow time left |

### Auto-Target

| Member | Return | Description |
|--------|--------|-------------|
| `AutoTarget_Enabled()` | bool | Is auto-target enabled |
| `AutoTarget_Disabled(string _Key)` | bool | Is auto-target disabled |

### Maintained Spells

| Member | Return | Description |
|--------|--------|-------------|
| `HaveMaintained(... Args)` | bool | Have maintained spell |
| `ScrollOf_Get_MaintainedDuration(string _ScrollName)` | int | Get scroll duration |

### Water Breathing

| Member | Return | Description |
|--------|--------|-------------|
| `CastGroupWaterBreathing(string _ForWho)` | method | Cast group water breathing |
| `CancelGroupWaterBreathing(string _ForWho)` | method | Cancel water breathing |

---

## Functions

Functions are called with `call OgreBotAPI.FunctionName params` and can return values.

| Function | Return | Description |
|----------|--------|-------------|
| `HO_Start(... Args)` | bool | Start HO |
| `HO_Starter()` | bool | Cast HO starter |
| `HO_Advance()` | bool | Advance HO |
| `Cast_Interrupt(string _MobNameID, int64 _AbilityID, string _CalledFrom)` | - | Cast interrupt |
| `CastAbilityOnNPC(string _ForWho, string AbilityName, string _MobNameID, string _CalledFrom)` | - | Cast on NPC |
| `CastRescue(string CalledFrom, ... Args)` | - | Cast rescue |
| `ZoneInto(string _ZoneName, string _ActorName, int _DoorOption)` | - | Zone into |
| `GetToGH()` | - | Get to guild hall |
| `HouseWindowToGH()` | - | House window to GH |
| `AcceptReward(string _Selection, int64 _WindowID)` | - | Accept reward |
| `JumpKW(int _Wait1, int _Wait2)` | - | Jump KW |
| `Question()` | - | Handle question |
| `Resource()` | - | Handle resource |
| `DestroyItem(string _ItemName, uint _Charges)` | - | Destroy item |
| `DestroyItem_NoChecks(string _ItemName)` | - | Destroy no checks |
| `DestroyItemByID_NoChecks(int64 _ItemID)` | - | Destroy by ID |
| `Consume_Status_Ingots(uint _Amount)` | - | Consume ingots |
| `Actor_ClickQueued(string _NameOrID, bool _ExactName, int _WaitTime)` | - | Click actor queued |
| `KWL_Safe(string _ForWho, float _X, float _Y, float _Z, uint _RoomID)` | bool | Safe KWL |
| `HailNPC(string _NameOrID)` | - | Hail NPC |
| `ReloadExport()` | - | Reload export |
| `Summon_Familiar()` | - | Summon familiar |
| `Research_Material_Check(string _ForWho)` | int | Check research mats |
| `Champions_Zone_Resetter(string _ZoneName)` | - | Reset champions zone |
| `Select_Window(string _ForWho, ... Args)` | int | Select window |
| `AutoConsumeTemporaryFamiliarExperience()` | - | Consume familiar XP |
| `AutoConsumeTemporaryMountTrainingReduction()` | - | Consume mount training |
| `AutoConsumeTemporaryResearchReduction()` | - | Consume research |
| `CheckResearch(bool _ForceReport)` | - | Check research |
| `ResetCameraAngle()` | - | Reset camera |
| `Set_CameraPitch(int _Pitch)` | - | Set pitch |
| `Set_FirstPersonView()` | bool | Set first person |
| `Set_LookDown(uint _Value)` | bool | Look down |
| `Set_LookUp(uint _Value)` | bool | Look up |
| `CheckKunarkAscendingRequirements()` | - | Check KA requirements |
| `ApplyVerbIDQueuedForWho(int64 _ActorID, string _Verb)` | - | Apply verb queued |
| `ApplyVerbQueuedForWho(string _ActorName, string _Verb)` | - | Apply verb queued |
| `ToggleZoneReuse()` | - | Toggle zone reuse |
| `ResetZone(string _ZoneName)` | - | Reset zone |
| `ConvertAdornToSlot(string _AdornHash)` | string | Convert adorn slot |
| `CancelInvis()` | - | Cancel invisibility |
| `LoginAtCharacterSelect(string _CharName)` | - | Login character |
| `TargetAndDoubleClickActor(int64 _ActorID)` | - | Target and click |
| `Spew_MissionTimerInfo(... Searches)` | - | Spew mission info |
| `LandFlyingMount()` | - | Land mount |
| `ExitClient(int _Seconds)` | - | Exit client |
| `OpenAndBuyFromMerchant(...)` | - | Buy from merchant |
| `CloseAllExamine()` | - | Close all examine |
| `ExamineAllOfItem(... _Items)` | - | Examine items |
| `Consume_Status_Tokens(uint _Amount)` | - | Consume tokens |

---

## Usage Examples

### Basic Movement

```lavishscript
; Move group to location and engage
OgreBotAPI:KWL["all", 100.5, 25.0, -50.3]

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

!!! note "_ForWho Parameter"
    Most methods support targeting specific characters. Use `"all"` for everyone, archetype names for groups, or specific character names. See [Cross-Session Commands](cross-session-commands.md) for the full targeting reference.

!!! note "Async Operations"
    Many methods queue commands. Use `wait` or check status members to ensure completion.

!!! warning "Error Handling"
    Check return values and use existence checks before accessing actor/object members. Always validate with `(exists)` before accessing `.ID`, `.Name`, or other members.

!!! tip "Performance"
    Use appropriate throttling -- do not spam methods every frame. The bot has built-in pulse timing.

!!! warning "Do NOT use relay groups"
    Relay group commands (`relay ${OgreRelayGroup} OgreBotAtom ...`) are deprecated/legacy. Always use the OgreBot cross-session `oc !c` or `oc !ci` commands instead for sending commands to other sessions. See [Cross-Session Commands](cross-session-commands.md) for details.

---

## Related Documentation

- [Cross-Session Commands](cross-session-commands.md) - How to send commands across all sessions
- [CampSpot System](camp-spot.md) - Detailed positioning and movement reference
- [Encounter Coding](encounter-coding.md) - How to write encounter modules using OgreBotAPI
- [Coding Practices](coding-practices.md) - Variable naming conventions and code style
