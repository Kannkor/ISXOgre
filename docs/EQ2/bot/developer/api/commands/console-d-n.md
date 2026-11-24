<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# Console commands: D-N

## `-DeleteQuest`

`-DeleteQuest <who> <value>`

Deletes a quest.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string |  | Quest name |

Runs: `OgreBotAPI.Quest:Delete`

```text
oc !c -DeleteQuest igw:${Me.Name} "A Lost Shipment"
```

## `-DestroyItem`

`-DestroyItem <who> <itemname> <charges>`

Destroys item if it has no charges or charges are at Charges. Default of 0.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `itemname` | string | `DoesNotExist` | Itemname |
| `charges` | string | `0` | Charges |

Runs: `OgreBotAPI.Inventory:DestroyItem`

```text
oc !c -DestroyItem igw:${Me.Name} "Rusty Dagger" 0
```

## `-DestroyItem_NoChecks`

`-DestroyItem_NoChecks <who> <itemname>`

Destroys the carried item (bags, not bank) with that name without checking its charges, through the bot's one destroy door, which re-checks the name and refuses a bag. Nothing happens when you carry no such item.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `itemname` | string | `DoesNotExist` |  |

Runs: `OgreBotAPI.Inventory:DestroyItemNoChecks`

```text
oc !c -DestroyItem_NoChecks igw:${Me.Name} "Rusty Dagger"
```

## `-Disable_Dispells`

`-Disable_Dispells <who>`

Ticks the No Dispels setting, so the bot stops casting dispels.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Abilities:SetDispellsEnabled`

```text
oc !c -Disable_Dispells igw:${Me.Name}
```

## `-Disable_Interrupts`

`-Disable_Interrupts <who>`

Ticks the No Interrupts setting, and on a Rogue also turns Daring Advance off in the cast stack and cancels it.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Abilities:SetInterruptsEnabled`

```text
oc !c -Disable_Interrupts igw:${Me.Name}
```

## `-Disband`

`-Disband <who>`

Disband your group.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Roster:Disband`

```text
oc !c -Disband ${Me.Name}
```

## `-DispellNPCWithAny`

`-DispellNPCWithAny <who> <npcnameorid>`

Queues a dispel on the NPC (name or actor id) using your class dispel ability first and an Energy Inverter clicky if there is none, as soon as the cast bar is free. Every call queues another one, and a blank NPC prints a console line instead.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `npcnameorid` | string | `DoesNotExist` |  |

Runs: `OgreBotAPI.Abilities:DispellNPC`

```text
oc !c -DispellNPCWithAny igw:${Me.Name} ${Target.ID}
```

## `-DispellNPCWithItem`

`-DispellNPCWithItem <who> <npcnameorid>`

Queues a dispel on the NPC (name or actor id) using a fighter's Energy Inverter clicky, used as soon as the cast bar is free, and every call queues another one. A blank NPC prints a console line instead.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `npcnameorid` | string | `DoesNotExist` |  |

Runs: `OgreBotAPI.Abilities:DispellNPC`

```text
oc !c -DispellNPCWithItem igw:${Me.Name} ${Target.ID}
```

## `-DispellNPCWithSpell`

`-DispellNPCWithSpell <who> <npcnameorid>`

Dispel a buff off an NPC using your class dispel ability (no item fallback - use -DispellNPCWithAny for that).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `npcnameorid` | string | `DoesNotExist` |  |

Runs: `OgreBotAPI.Abilities:DispellNPC`

```text
oc !c -DispellNPCWithSpell igw:${Me.Name} ${Target.ID}
```

## `-DisplayEtherealMissionInfo`

`-DisplayEtherealMissionInfo <who>`

Show which zones are hot right now, when they rotate, and what is next. Legacy name - use -DisplayHotZoneInfo.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Quest:ShowMissionInfo`

```text
oc !c -DisplayEtherealMissionInfo ${Me.Name}
```

## `-DisplayHotZoneInfo`

`-DisplayHotZoneInfo <who>`

Also: `-HotZones`, `-DisplayHotZonesInfo`

Show which zones are hot right now, when they rotate, and what is next. Only the expansions ticked on the Hot Zones tab are listed.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Quest:ShowMissionInfo`

```text
oc !c -DisplayHotZoneInfo ${Me.Name}
```

## `-DoHO_Reset`

`-DoHO_Reset <who>`

Clears the HO run record (target, completion count and options) without changing whether DoHO is enabled or its timeout.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.HOs:DoReset`

```text
oc !c -DoHO_Reset igw:${Me.Name}
```

## `-DoHO_Set_Enable`

`-DoHO_Set_Enable <who> <torf> <args>`

TRUE (default) elects this session as the group's HO'er with the options given (-Force, -NoEnable, -NoHoAbilities, -DelayStart, -TimeOut), and FALSE ends the HO run and puts the HO options back. A word that is not TRUE or FALSE changes nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `torf` | string | `TRUE` |  |
| `args` | rest |  |  |

Runs: `OgreBotAPI.HOs:DoSetEnabled`

```text
oc !c -DoHO_Set_Enable ${Me.Name} FALSE
```

## `-DoHO_Setup`

`-DoHO_Setup <who> <args>`

Makes this session the group's HO'er: the others stand down, and it runs Heroic Opportunities until -NumHOsToComplete are done (default 1) or -TimeOut passes (default 25 seconds), then everyone's HO options are put back. Further options are -TargetID, -LeaveWheelOpen, -LeaveStartOpen, -NoModifyOptions and -AllowCastStack.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `args` | rest |  |  |

Runs: `OgreBotAPI.HOs:DoSetup`

```text
oc !c -DoHO_Setup ${Me.Name} -TargetID ${Target.ID} -NumHOsToComplete 2
```

## `-DoNotMove`

`-DoNotMove <who>`

Also: `-NoMove`

Pauses follow and stops the current move. The leader is kept: LetsGo or a new follow resumes it, and the camp spot still pulls the character back.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Movement:StopFollow`

```text
oc !c -DoNotMove igw:${Me.Name}
```

## `-DoVDebuff`

`-DoVDebuff <who> <npcnameorid> <allowmovement>`

Also: `-raiddebuff`

Auto rebuffing of DoV Raid Debuffs.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `npcnameorid` | string |  | NPC Name or ID |
| `allowmovement` | string |  | Allow Moving |

Runs: `OgreBotAPI:DoVDebuff`

```text
oc !c -DoVDebuff igw:${Me.Name} ${Target.ID} TRUE
```

## `-DoVDebuff_Half`

`-DoVDebuff_Half <who> <npcnameorid> <archetype> <odd> <allowmovement>`

Half of the toons cast DoV Raid Debuff.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `npcnameorid` | string |  | NPC Name or ID |
| `archetype` | string | `auto` | Archtype. Valid options are: Fighter or scout or priest or mage |
| `odd` | string | `TRUE` | Odd |
| `allowmovement` | string |  | Allow Moving |

Runs: `OgreBotAPI:DoVDebuff_Half`

```text
oc !c -DoVDebuff_Half igw:${Me.Name} ${Target.ID} auto TRUE FALSE
```

## `-Drink_Alcohol`

`-Drink_Alcohol <who> <value>`

Drinks the item in your main bags with that name using the game's drink_alcohol command. Nothing happens when no such item is there.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string |  | The drink's name, as it is in your bags |

Runs: `OgreBotAPI.Consumables:DrinkAlcohol`

```text
oc !c -Drink_Alcohol ${Me.Name} "Halas Ale"
```

## `-DungeonMakerCancel`

`-DungeonMakerCancel <who>`

Also: `-DungeonMaker_Cancel`

Cancels the rating window for DM

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Windows:DungeonMakerCancel`

```text
oc !c -DungeonMakerCancel igw:${Me.Name}
```

## `-Enable_Dispells`

`-Enable_Dispells <who>`

Unticks the No Dispels setting, so the bot casts dispels again.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Abilities:SetDispellsEnabled`

```text
oc !c -Enable_Dispells igw:${Me.Name}
```

## `-Enable_Interrupts`

`-Enable_Interrupts <who>`

Unticks the No Interrupts setting and turns Daring Advance on in the cast stack.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Abilities:SetInterruptsEnabled`

```text
oc !c -Enable_Interrupts igw:${Me.Name}
```

## `-End_Bot`

`-End_Bot <who>`

Also: `-EndBot`

Ends Ogrebot.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Bot:End`

```text
oc !c -End_Bot all
```

## `-EndScriptOB`

`-EndScriptOB <who> <scriptname>`

Also: `-EndScriptRequiresOgreBot`, `-esob`

Ends a script ForWho.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `scriptname` | string | `Nothing` | ScriptName |

Runs: `OgreBotAPI.Bot:EndScript`

```text
oc !c -EndScriptOB igw:${Me.Name} MyScript
```

## `-EquipCharm`

`-EquipCharm <who> <value>`

Equips charms based on what is selected in the 'Equipment Info' tab in Ogrebot. Note: It ONLY equips into Charm slot 1.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | int64 | `1` | Which charm option. Example: 1 |

Runs: `OgreBotAPI.Inventory:EquipCharm`

```text
oc !c -EquipCharm igw:${Me.Name} 1
```

## `-evac`

`-evac <who> <mode>`

Anyone with an evacuate ability will use it. With mode `totem`, a toon with no class evac (or one not ready) uses a Totem of Escape if it has one ready.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `mode` | string |  | Blank for the class evac only; `totem` also allows a Totem of Escape when there is no class evac ready (per toon). |

Runs: `OgreBotAPI.Movement:Evac`

```text
oc !c -evac igw:${Me.Name} totem
```

## `-ExamineAllOfItem`

`-ExamineAllOfItem <who> <args>`

Examines stacks of items. Parameter 2+ = Item Names

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `args` | rest |  |  |

Runs: `OgreBotAPI.Inventory:ExamineAll`

```text
oc !c -ExamineAllOfItem igw:${Me.Name} Shard
```

## `-ExamineInventoryItem`

`-ExamineInventoryItem <who> <value>`

Opens the examine window for the item in your main bags with exactly that name. Nothing happens when no such item is there.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string |  |  |

Runs: `OgreBotAPI.Inventory:Examine`

```text
oc !c -ExamineInventoryItem ${Me.Name} "Ethereal Shard"
```

## `-ExecuteEvent_AP`

`-ExecuteEvent_AP <who> <eventname> <args>`

Fires the named LavishScript event on this session, passing the remaining arguments joined by commas.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `eventname` | string | `DoesNotExist` |  |
| `args` | rest |  |  |

Runs: `OgreBotAPI.Comms:ExecuteEvent`

```text
oc !c -ExecuteEvent_AP igw:${Me.Name} MyScript_Phase 2
```

## `-ExitClient`

`-ExitClient <who> <seconds>`

Shows a message box warning that the game client will exit in the given number of seconds (30 by default), then closes the client without camping out. Clicking OK on the box before the time is up cancels it.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `seconds` | string | `30` |  |

Runs: `OgreBotAPI.Bot:ExitClient`

```text
oc !c -ExitClient ${Me.Name} 30
```

## `-F2PWindow_Check`

`-F2PWindow_Check <who>`

Closes the All-Access (F2P) upsell window once if it is showing, with a console note. Does nothing when the window is not up.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Windows:F2PWindowCheck`

```text
oc !c -F2PWindow_Check all
```

## `-F2PWindow_SetOptions`

`-F2PWindow_SetOptions <who>`

Turns on the watcher that closes the All Access upsell window (Settings tab: Close F2P upsell window).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI:F2PWindow_SetOptions`

```text
oc !c -F2PWindow_SetOptions all
```

## `-FaceActor`

`-FaceActor <who> <actornameid>`

Turns you to face the actor with exactly that name, or that actor ID. Nothing happens when it is not found.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `actornameid` | string | `0` |  |

Runs: `OgreBotAPI.Movement:FaceActor`

```text
oc !c -FaceActor igw:${Me.Name} ${Target.ID}
```

## `-FaceAngle`

`-FaceAngle <who> <angle>`

Turns you to face the heading angle. A missing angle is refused with a console error.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `angle` | string |  |  |

Runs: `OgreBotAPI.Movement:FaceAngle`

```text
oc !c -FaceAngle igw:${Me.Name} 90
```

## `-FaceLoc`

`-FaceLoc <who> <x> <y> <z>`

Turns you to face the x and z location; y is ignored (a heading is flat) and kept so a location pastes in as x y z. A missing x or z is refused with a console error.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `x` | string |  | X, or the name of a point of interest in this zone |
| `y` | string |  | Y - ignored (a heading is flat); kept so a location pastes in as x y z |
| `z` | string |  | Z |

Runs: `OgreBotAPI.Movement:FaceLoc`

```text
oc !c -FaceLoc igw:${Me.Name} 120 15 -340
```

## `-FastTravel`

`-FastTravel <who> <towhere> <args>`

Also: `-TravelFast`

Fast Travel.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `towhere` | string | `NoWhere!` | Travel to where |
| `args` | rest | `FALSE.` | Exact Match |

Runs: `OgreBotAPI.Travel:Fast`

```text
oc !c -FastTravel igw:${Me.Name} Antonica FALSE
```

## `-FlagToon`

`-FlagToon <who> <value>`

Assigns a Flag designation to characters.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string | `1` | Flag # from 1 to 24 |

Runs: `OgreBotAPI.Roster:Flag`

```text
oc !c -FlagToon ${Me.Name} 3
```

## `-FlyDown`

`-FlyDown <who>`

Also: `-FlyDownForWho`

Presses the fly down [or swim down] button. Note: This is NOT a toggle.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Movement:FlyDown`

```text
oc !c -FlyDown igw:${Me.Name}
```

## `-FlyStop`

`-FlyStop <who>`

Also: `-FlyStopForWho`

Stops flying [up and down]. Note: This is NOT a toggle.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Movement:FlyStop`

```text
oc !c -FlyStop igw:${Me.Name}
```

## `-FlyUp`

`-FlyUp <who>`

Also: `-FlyUpForWho`

Presses the fly up [or swim up] button. Note: This is NOT a toggle.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Movement:FlyUp`

```text
oc !c -FlyUp igw:${Me.Name}
```

## `-FoodDrink_AutoConsume`

`-FoodDrink_AutoConsume <who> <value>`

Modifies Food and Drink AutoConsume based on Parameter 2 input.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string | `TRUE` | Value. Options are: TRUE. FALSE. TOGGLE. REPORT |

Runs: `OgreBotAPI.Inventory:AutoConsumeFoodDrink`

```text
oc !c -FoodDrink_AutoConsume igw:${Me.Name} TRUE
```

## `-FoodDrink_Replenish`

`-FoodDrink_Replenish <who>`

Replenishes food and drink from inventory and depot.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Consumables:ReplenishFoodDrink`

```text
oc !c -FoodDrink_Replenish igw:${Me.Name}
```

## `-Force_MountOff`

`-Force_MountOff <who>`

Will dismount you. The down half of Force_MountOn.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Consumables:MountDown`

```text
oc !c -Force_MountOff igw:${Me.Name}
```

## `-Force_MountOn`

`-Force_MountOn <who>`

Will cancel and recast your mount.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Consumables:MountUp`

```text
oc !c -Force_MountOn igw:${Me.Name}
```

## `-ForceAliasUpdate`

`-ForceAliasUpdate <who>`

Drops the cached alias answers on the matched toons, so the next *alias is worked out against the group and raid as they are now.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.ForWho:ForceUpdate`

```text
oc !c -ForceAliasUpdate all
```

## `-forcefollow`

`-forcefollow <who>`

Also: `-ffollow`

Does a Force follow as per what is set in OgreBot setup tab.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Movement:ForceFollow`

```text
oc !c -forcefollow igw:${Me.Name}
```

## `-GetFlag`

`-GetFlag <who>`

Gets a flag from a guild strategist.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI:GetFlag`

```text
oc !c -GetFlag igw:${Me.Name}
```

## `-GetToConcentration`

`-GetToConcentration <who> <value>`

Cancels your maintained buffs that cost concentration, last slot first, one buff for each point your used concentration is above the value (default 4).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string | `4` |  |

Runs: `OgreBotAPI.Movement:GetToConcentration`

```text
oc !c -GetToConcentration igw:${Me.Name} 4
```

## `-GetToGH`

`-GetToGH <who>`

Gets you to GH. Using call to GH or call to home or fast travel.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Movement:GetToGH`

```text
oc !c -GetToGH igw:${Me.Name}
```

## `-GroupCure`

`-GroupCure <who>`

Asks the matched toons for an immediate group cure: within the next 2 seconds they cast their class group cure if at least one group member is afflicted.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Cures:RequestGroup`

```text
oc !c -GroupCure igw:${Me.Name}
```

## `-Hail`

`-Hail <who> <mobnameid>`

Also: `-HailNPC`

Will hail based on parameters.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `mobnameid` | string | `0` | NPC Name or ID. \${Target.ID} is fine to use for your target |

Runs: `OgreBotAPI.Actors:Hail`

```text
oc !c -Hail ${Me.Name} ${Target.ID}
```

## `-Heartstone_RekindleBond`

`-Heartstone_RekindleBond <who>`

Will use the Heartstone to rekindle your bond.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Consumables:RekindleHeartstone`

```text
oc !c -Heartstone_RekindleBond ${Me.Name}
```

## `-HO_Cancel_Starter`

`-HO_Cancel_Starter <who>`

Cancels the open Heroic Opportunity starter selection. Nothing happens when no HO starter is showing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.HOs:CancelStarter`

```text
oc !c -HO_Cancel_Starter ${Me.Name}
```

## `-HO_Start`

`-HO_Start <who> <args>`

Casts your archetype's Heroic Opportunity starter ability to open an HO, unless one is already up or one was just started. -ActorID &lt;id> casts it on that actor, and -SkipTimer ignores the just-started wait.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `args` | rest |  |  |

Runs: `OgreBotAPI.HOs:Start`

```text
oc !c -HO_Start ${Me.Name} -ActorID ${Target.ID}
```

## `-HO_Starter_Advance`

`-HO_Starter_Advance <who>`

Also: `-HO_Starter`

Casts the abilities that match your archetype's offered starter icons, advancing the Heroic Opportunity starter chain.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.HOs:Starter`

```text
oc !c -HO_Starter_Advance igw:${Me.Name}
```

## `-HO_Wheel_Advance`

`-HO_Wheel_Advance <who>`

Also: `-HO_Advance`

Casts the abilities that match your archetype's icons on the Heroic Opportunity wheel, advancing it toward completion.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.HOs:Advance`

```text
oc !c -HO_Wheel_Advance igw:${Me.Name}
```

## `-holdup`

`-holdup <who>`

Pauses follow and stops the current move. The leader is kept: LetsGo or a new follow resumes it, and the camp spot still pulls the character back.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Movement:StopFollow`

```text
oc !c -holdup igw:${Me.Name}
```

## `-ImmRes`

`-ImmRes <who> <howmany>`

Uses Cleric AA Immaculate Revival if X people are dead. Will always cast if a priest or fighter is dead.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who acts - leave blank to use the For Who window. |
| `howmany` | string | `2` | How many dead to cast |

Runs: `OgreBotAPI.Session:ImmRes`

```text
oc !c -ImmRes igw:${Me.Name} 2
```

## `-InjectChat`

`-InjectChat <who> <chat>`

Injects a phrase as if it was said in raid chat.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `chat` | string | `Nothing` | Chat text |

Runs: `OgreBotAPI.Comms:InjectChat`

```text
oc !c -InjectChat igw:${Me.Name} "Set up for ${Target.Name}"
```

## `-InputTextWindow_Accept`

`-InputTextWindow_Accept <who>`

Clicks the accept button of the text-entry popup on screen. Nothing happens when that popup is not showing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Windows:InputTextAccept`

```text
oc !c -InputTextWindow_Accept igw:${Me.Name}
```

## `-InputTextWindow_AddText`

`-InputTextWindow_AddText <who> <value>`

Appends the text to the input box of the text-entry popup on screen. Nothing happens when that popup is not showing or the text is blank.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string |  |  |

Runs: `OgreBotAPI.Windows:InputTextAdd`

```text
oc !c -InputTextWindow_AddText igw:${Me.Name} opensesame
```

## `-InputTextWindow_ClearText`

`-InputTextWindow_ClearText <who>`

Empties the input box of the text-entry popup on screen. Nothing happens when that popup is not showing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Windows:InputTextClear`

```text
oc !c -InputTextWindow_ClearText igw:${Me.Name}
```

## `-Invite`

`-Invite <who> <invitewho>`

The matched toons send a group invite to invitewho (default: you), and an alias resolves to the toon it names. A player already in their group or raid is skipped, a name that is not a plain character name is refused with a console line, and raidinvite is not read.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `invitewho` | string |  |  |

Runs: `OgreBotAPI.Roster:Invite`

```text
oc !c -Invite ${Me.Name} ${Target.Name} FALSE
```

## `-Inviter`

`-Inviter <who> <args>`

Send 1-second-spaced group/raid invites to a curated list of toons.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `args` | rest |  | Space/comma-separated list of toon names to invite (plus any per-name flags). |

Runs: `OgreBotAPI.Roster:Inviter`

```text
oc !c -Inviter ${Me.Name} ${Target.Name}
```

## `-ItemEmbargo`

`-ItemEmbargo <who> <abilityid> <duration> <args>`

Also: `-ItemRotate`

Embargo an item for N seconds on the toons the for-who names (an item rotation): their cast stack skips that item until the time is up, while their Enable Item Embargo box (Settings) is ticked.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who embargoes - leave blank to use the For Who window; `all` = every session that hears it. |
| `abilityid` | string |  | The item's LinkID, as the item's LinkID member reads it (it can be negative). The unsigned form a guild bank or Census link writes is the same item. |
| `duration` | string |  |  |
| `args` | rest |  |  |

Runs: `OgreBotAPI.Inventory:AddEmbargo`

```text
oc !c -ItemEmbargo all 987654321 30
```

## `-joustin`

`-joustin <who>`

Also: `-joust-in`, `-jst-in`

Joust In. When campspot is turned on you will joust In (if permitted).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Movement:JoustIn`

```text
oc !c -joustin igw:${Me.Name}
```

## `-joustoff`

`-joustoff <who>`

Also: `-joust-off`, `-jst-off`

Joust Off. Tells certain classes or people they are not permitted to joust in.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto+Caster` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Movement:JoustOff`

```text
oc !c -joustoff igw:${Me.Name}
```

## `-jouston`

`-jouston <who>`

Also: `-joust-on`, `-jst-on`

Joust On. Reverses the effects of Joust Off. DOES NOT JOUST IN. Tells certain classes or people they are permitted to joust in.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto+Melee` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Movement:JoustOn`

```text
oc !c -jouston igw:${Me.Name}
```

## `-joustout`

`-joustout <who>`

Also: `-joust-out`, `-jst-out`

Joust Out. When campspot is turned on you will joust out.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Movement:JoustOut`

```text
oc !c -joustout igw:${Me.Name}
```

## `-Jump`

`-Jump <who>`

Presses the jump key once.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Movement:Jump`

```text
oc !c -Jump igw:${Me.Name}
```

## `-Kick`

`-Kick <who> <kickwho>`

Kicks a member out of the group.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who acts - leave blank to use the For Who window. |
| `kickwho` | string |  | The group member to kick |

Runs: `OgreBotAPI.Roster:Kick`

```text
oc !c -Kick ${Me.Name} ${Group[1].Name}
```

## `-LandFlyingMount`

`-LandFlyingMount <who>`

Holds the fly-down key until the toon has landed its flying mount, for up to 60 seconds, then releases the key. It runs as a queued action and does nothing outside the world.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Movement:LandFlyingMount`

```text
oc !c -LandFlyingMount igw:${Me.Name}
```

## `-letsgo`

`-letsgo <who>`

This button removes movement restrictions such as HoldUp and campspot.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.CampSpot:Release`

```text
oc !c -letsgo igw:${Me.Name}
```

## `-LoadAutoTargetList`

`-LoadAutoTargetList <who> <list>`

Also: `-LoadAutoTargetListForWho`, `-LATL`

Loads an AutoTarget List for a specific toon

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `list` | string |  | List to load |

Runs: `OgreBotAPI.AutoTarget:LoadSaved`

```text
oc !c -LoadAutoTargetList igw:${Me.Name} MyRaidList
```

## `-LoadBot`

`-LoadBot <who>`

Loads OgreBot (starts it if it is not running).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Bot:Load`

```text
oc !c -LoadBot igw:${Me.Name}
```

## `-LoadProfile`

`-LoadProfile <who> <profilename>`

Also: `-ProfileForWho`, `-Profile`

Loads a profile using the name you provide.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `profilename` | string |  | Profile Name |

Runs: `OgreBotAPI.Options:LoadProfile`

```text
oc !c -LoadProfile igw:${Me.Name} Raid
```

## `-LogToonIn`

`-LogToonIn <who> <name> <server> <class>`

Logs a character in on one box: from the login screen, from character select, or from the world on another character (it camps first). Name the box by its InnerSpace session or its character, and at character select or the login screen by the character it last played: oc !c -LogToonIn MyToon MyToon logs MyToon back in after a zone dropped it to character select.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | string |  | The box: its InnerSpace session name or its character's name (at character select, the character it last played). all and groups pick no box. |
| `name` | string |  | The character to log in. It needs a saved login on this PC. |
| `server` | string |  | The server, for a character saved on more than one. Blank uses its default. A short form works: ior, md. |
| `class` | string |  | The class to log in as, like ranger. Blank logs in whatever class it was. |

Runs: `OgreBotAPI.Session:LogToonIn`

```text
oc !c -LogToonIn ${Me.Name} ${Group[1].Name}
```

## `-LootAll`

`-LootAll <who>`

Clicks Loot All on the loot window of the matched toons. It does nothing on a toon with no loot window open.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Loot:LootAll`

```text
oc !c -LootAll ${Me.Name}
```

## `-MakeLeader`

`-MakeLeader <who> <name>`

Makes someone else the group leader.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `name` | string | `${Me.Name}` | Person to make group leader. Leave blank for youself |

Runs: `OgreBotAPI.Roster:MakeLeader`

```text
oc !c -MakeLeader ${Me.Name} ${Group[1].Name}
```

## `-MarkToon`

`-MarkToon <who>`

Marks each selected character (the same as setting flag 24).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Roster:Mark`

```text
oc !c -MarkToon ${Me.Name}
```

## `-Mentor`

`-Mentor <who> <mentorwho>`

Tells [Bots] to mentor a specific player.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who acts - leave blank to use the For Who window. |
| `mentorwho` | string | `${Me.Name}` | Toonname to mentor |

Runs: `OgreBotAPI.Roster:Mentor`

```text
oc !c -Mentor igw:${Me.Name} ${Me.Name}
```

## `-Mercenary_AddMercenaries`

`-Mercenary_AddMercenaries <who>`

Adds every Mercenary item in your bags, Overseer bag and harvest bag.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Consumables:AddMercenaries`

```text
oc !c -Mercenary_AddMercenaries ${Me.Name}
```

## `-Message`

`-Message <who> <text>`

Display a message on this session's console.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `text` | string |  | Message text to display. |

Runs: `OgreBotAPI.Comms:Message`

```text
oc !c -Message igw:${Me.Name} "Pulling in 5"
```

## `-Message_Relay`

`-Message_Relay <who> <text>`

Broadcast a message to every session's console across the fleet (including this one).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `text` | string |  | Message text to broadcast. |

Runs: `OgreBotAPI.Comms:Broadcast`

```text
oc !c -Message_Relay ${Me.Name} "Ready check"
```

## `-Move2Area`

`-Move2Area <who> <x> <y> <z> <precision>`

Also: `-MoveToArea`

Tells [Bots] to move to a specific area.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `x` | string | `${Me.X}` | X coordinate (paste ${Me.X}), or the name of a point of interest in this zone |
| `y` | float | `${Me.Y}` | Y/height - IGNORED (2D ground move); pass ${Me.Y} for game-order convenience |
| `z` | float | `${Me.Z}` | Z coordinate (paste ${Me.Z}) |
| `precision` | float | `3` | Arrival precision |

Runs: `OgreBotAPI.Movement:Move2Area`

```text
oc !c -Move2Area igw:${Me.Name} ${Me.X} ${Me.Y} ${Me.Z} 3
```

## `-MoveToAreaNoTarget`

`-MoveToAreaNoTarget <who> <x> <y> <z> <precision>`

Also: `-Move2AreaNoTarget`

Walks to the given X and Z (Y is ignored) and stops within the precision distance, whether or not the toon has a target. A toon on a campspot stays there until -joustout or -letsgo; nothing moves if X or Z is missing or OgreBot is not open.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `x` | string | `${Me.X}` | X coordinate (paste ${Me.X}), or the name of a point of interest in this zone |
| `y` | float | `${Me.Y}` | Y/height - IGNORED (2D ground move) |
| `z` | float | `${Me.Z}` | Z coordinate (paste ${Me.Z}) |
| `precision` | float | `3` | Arrival precision |

Runs: `OgreBotAPI.Movement:Move2AreaNoTarget`

```text
oc !c -MoveToAreaNoTarget igw:${Me.Name} ${Me.X} ${Me.Y} ${Me.Z} 3
```

## `-NavStop`

`-NavStop <who>`

Also: `-nav-stop`, `-nav_stop`

Stops the nav trip under way, unless it belongs to an encounter (`ogre nav stop` ends any trip).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who navs - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Movement:NavStop`

```text
oc !c -NavStop igw:${Me.Name}
```

## `-NavTo`

`-NavTo <who> <x> <y> <z> <fly>`

Also: `-nav-to`, `-nav_to`

Nav (the mesh router) to an x y z, or to a point of interest in this zone. Left blank, x y z are where the box that sends the line stands, so everyone comes to you. It waits while OgreBot is paused and stops when OgreBot closes. It leaves an encounter's trip alone.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who navs - leave blank to use the For Who window. |
| `x` | string | `${Me.X}` | X, or the name of a point of interest in this zone |
| `y` | float | `${Me.Y}` | Y |
| `z` | float | `${Me.Z}` | Z |
| `fly` | string | `nofly` | fly flies the trip; nofly walks it. |

Runs: `OgreBotAPI.Movement:NavTo`

```text
oc !c -NavTo igw:${Me.Name} 120.5 -14 380.25 nofly
```

## `-NoTarget`

`-NoTarget <who>`

Clears everyones target. Useful to stop come2me.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI:NoTarget`

```text
oc !c -NoTarget igw:${Me.Name}
```
