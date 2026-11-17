# Console commands: S-Z

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## `-Scribe_Empyral`

`-Scribe_Empyral <who> <namefilter>`

Also: `-Scribe`

Scribes Empyral books in your inventory.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `namefilter` | string | `Empyral` | Only scribe scribeable items whose name contains this. "*" = everything scribeable. |

Runs: `OgreBotAPI:Scribe_Empyral`

```text
oc !c -Scribe_Empyral igw:${Me.Name} Empyral
```

## `-ScrollOf`

`-ScrollOf <who> <name> <value> <usebest>`

Uses a Scroll Of ___. Example: Scroll of Prowess. For best success use 'Thaumic Scroll of _____'.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `name` | string | `Prowess` | Scroll Name. Shortform of Prowess or Pain or Power or PowerLink is acceptable |
| `value` | int64 | `0` | If duration less than this cancel it first. Leave blank or 0 to disable |
| `usebest` | string | `FALSE` |  |

Runs: `OgreBotAPI.Consumables:ScrollOf`

```text
oc !c -ScrollOf ${Me.Name} Prowess 0 TRUE
```

## `-Select_Window_AP`

`-Select_Window_AP <who> <args>`

Picks an option in the select window on screen by number or exact text (-substring matches part of it), then clicks OK. -test selects without OK, -reportonly only reports the option number, -spew lists the options, and with no select window open it prints a line and does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `args` | rest |  |  |

Runs: `OgreBotAPI.Windows:Select`

```text
oc !c -Select_Window_AP ${Me.Name} -substring Heroic
```

## `-Select_Window_Spew_AP`

`-Select_Window_Spew_AP <who>`

Lists the options of the select window on screen to the console, numbered from 1.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Windows:SelectSpew`

```text
oc !c -Select_Window_Spew_AP ${Me.Name}
```

## `-Select_Zone_Version`

`-Select_Zone_Version <who>`

Presses OK in the select zone version window. Designed specifically for BoL Heroics.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Zone:SelectVersion`

```text
oc !c -Select_Zone_Version igw:${Me.Name}
```

## `-SellToMerchant`

`-SellToMerchant <who> <itemname> <value>`

Sells the quantity (default 1) of the named item from your inventory to the merchant window that is already open. No item, no merchant window, or an item not in its sell list each get one line.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `itemname` | string |  |  |
| `value` | string | `1` |  |

Runs: `OgreBotAPI.Merchant:Sell`

```text
oc !c -SellToMerchant ${Me.Name} "Rusty Dagger" 1
```

## `-Set_Allow_HOICon`

`-Set_Allow_HOICon <who> <variablename>`

Adds an HO icon id to the allow list: while that list has any entry, the cast stack casts only those Heroic Opportunity abilities whose icon is on it. Abilities with no HO icon are not affected, and left blank it adds icon 0.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `variablename` | int64 |  |  |

Runs: `OgreBotAPI.HOs:AllowIcon`

```text
oc !c -Set_Allow_HOICon ${Me.Name} 12
```

## `-Set_CameraPitch`

`-Set_CameraPitch <who> <pitch>`

Also: `-SetCameraPitch`

Pitches the camera from -75 to 75 (0 is level), switching to third person to do it. Out-of-range values are refused, and a request while one is still running is dropped.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `pitch` | string | `0` |  |

Runs: `OgreBotAPI.Client:SetCameraPitch`

```text
oc !c -Set_CameraPitch ${Me.Name} 30
```

## `-Set_CampSpotJump_Handle`

`-Set_CampSpotJump_Handle <who> <start> <jump> <end> <completed> <args>`

Walk a short route and jump once on the way: start, jump, end, completed (blank = end). Flags: -JumpDistance N, -MaxTimer seconds, -Attempts N, -RetryDelay seconds, -AboveY N, -RunMode walk\|run.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `start` | string |  |  |
| `jump` | string |  |  |
| `end` | string |  |  |
| `completed` | string |  |  |
| `args` | rest |  |  |

Runs: `OgreBotAPI.Movement:JumpRoute`

```text
oc !c -Set_CampSpotJump_Handle ${Me.Name} 100,20,300 110,20,310 120,22,320 125,22,325 -JumpDistance 3
```

## `-Set_Disable_HOICon`

`-Set_Disable_HOICon <who> <variablename>`

Adds an HO icon id to the disable list, so the cast stack never casts a Heroic Opportunity ability with that icon. Left blank it adds icon 0.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `variablename` | int64 |  |  |

Runs: `OgreBotAPI.HOs:DisableIcon`

```text
oc !c -Set_Disable_HOICon ${Me.Name} 24
```

## `-Set_DisableAllAOEs_AllParams`

`-Set_DisableAllAOEs_AllParams <who> <args>`

TRUE (default) stops AE casting: it ticks the ignore PBAE, encounter nuke and counter-ability boxes, casts your single-target focus ability and cancels your class's AE-proccing buffs, while FALSE unticks the boxes and cancels the focus. -allowcounters keeps counter abilities and buffs, -AllowEncounters leaves the encounter nuke box alone, and -verbose announces each change.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `args` | rest |  |  |

Runs: `OgreBotAPI.Abilities:SetAOEsDisabled`

```text
oc !c -Set_DisableAllAOEs_AllParams igw:${Me.Name} TRUE -allowcounters
```

## `-set_Internalvariable`

`-set_Internalvariable <who> <variablename> <variablevalue>`

Stores the value under the name in the bot's internal variable store on this session, read back with ${OgreBotAPI.Vars.GetInternal[name]}. A blank name does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `variablename` | string |  |  |
| `variablevalue` | string |  |  |

Runs: `OgreBotAPI.Vars:SetInternal`

```text
oc !c -set_Internalvariable ${Me.Name} PullCount 3
```

## `-set_variable`

`-set_variable <who> <variablename> <variablevalue>`

Stores the value under the name in the script variable store on this session, read back with ${OgreBotAPI.Vars.Get[name]}. A blank name does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `variablename` | string |  |  |
| `variablevalue` | string |  |  |

Runs: `OgreBotAPI.Vars:Set`

```text
oc !c -set_variable igw:${Me.Name} Phase 2
```

## `-SetAccessLevel`

`-SetAccessLevel <who> <value> <silent>`

Set this session's access level (0 up to your account's level).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string | `0` |  |
| `silent` | string | `FALSE` |  |

Runs: `OgreBotAPI.Access:SetLevel`

```text
oc !c -SetAccessLevel ${Me.Name} 0
```

## `-SetAutoLootMode`

`-SetAutoLootMode <who> <value>`

Sets this character's own auto-loot mode through the game's /setautolootmode: 0 none, 1 auto greed, 2 auto decline. A blank value sends 0.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string |  | 0 (none), 1 (greed) or 2 (decline), or AN, AG or AD |

Runs: `OgreBotAPI.Loot:SetAutoLootMode`

```text
oc !c -SetAutoLootMode igw:${Me.Name} 1
```

## `-SetCS_BehindNPC`

`-SetCS_BehindNPC <who> <nameorid> <distance> <skipifaggro>`

Moves your camp spot to a point behind an NPC, distance away from it. A blank NPC means your NPC target, and skipifaggro TRUE leaves the camp spot alone while you hold that NPC's aggro.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `nameorid` | string |  | The NPC to position on (a name or an actor id) - leave blank for your NPC target: your target, or your target's target |
| `distance` | string | `3` |  |
| `skipifaggro` | string | `FALSE` |  |

Runs: `OgreBotAPI.CampSpot:SetLocBehindActor`

```text
oc !c -SetCS_BehindNPC igw:${Me.Name} ${Target.ID} 4 FALSE
```

## `-SetCS_InFrontNPC`

`-SetCS_InFrontNPC <who> <nameorid> <distance> <skipifaggro>`

Moves your camp spot to a point in front of an NPC, distance away from it. A blank NPC means your NPC target, and skipifaggro TRUE leaves the camp spot alone while you hold that NPC's aggro.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `fighter` | Who to target - leave blank to use the For Who window. |
| `nameorid` | string |  | The NPC to position on (a name or an actor id) - leave blank for your NPC target: your target, or your target's target |
| `distance` | string | `3` |  |
| `skipifaggro` | string | `FALSE` |  |

Runs: `OgreBotAPI.CampSpot:SetLocInFrontOfActor`

```text
oc !c -SetCS_InFrontNPC ${Me.Name} ${Target.ID} 3 TRUE
```

## `-SetCS_NPC`

`-SetCS_NPC <who> <angle> <nameorid> <distance> <skipifaggro>`

Moves your camp spot to a point at an angle around an NPC, measured from the way it faces: angle 0 is the -SetCS_BehindNPC side and 180 the -SetCS_InFrontNPC side. Unlike those two, the distance also adds the NPC's body size, so the same distance lands further out.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `angle` | string | `0` |  |
| `nameorid` | string |  | The NPC to position on (a name or an actor id) - leave blank for your NPC target: your target, or your target's target |
| `distance` | string | `3` |  |
| `skipifaggro` | string | `FALSE` |  |

Runs: `OgreBotAPI.CampSpot:SetLocAtAngleFromActor`

```text
oc !c -SetCS_NPC igw:${Me.Name} 90 ${Target.ID} 5 FALSE
```

## `-SetCS_PositionNPC`

`-SetCS_PositionNPC <who> <nameorid> <distance> <skipifaggro>`

Moves your camp spot next to an NPC by role: fighters take a spot in front of it, everyone else a spot behind it, distance away. A blank NPC means your NPC target, and skipifaggro TRUE leaves the camp spot alone while you hold that NPC's aggro.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `nameorid` | string |  | The NPC to position on (a name or an actor id) - leave blank for your NPC target: your target, or your target's target |
| `distance` | string | `3` |  |
| `skipifaggro` | string | `FALSE` |  |

Runs: `OgreBotAPI.CampSpot:SetLocByRole`

```text
oc !c -SetCS_PositionNPC igw:${Me.Name} ${Target.ID} 3 FALSE
```

## `-SetNoDefensive`

`-SetNoDefensive <who> <trueorfalse>`

TRUE (default) turns on the no-defensive switch, which stops the bot casting beneficial abilities. FALSE turns it off, clearing every reason anything set it for.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `trueorfalse` | bool | `TRUE` |  |

Runs: `OgreBotAPI.Combat:SetNoDefensive`

```text
oc !c -SetNoDefensive igw:${Me.Name} TRUE
```

## `-SetNoOffensive`

`-SetNoOffensive <who> <value> <reason>`

Toggle the global no-offensive latch (stops ALL offensive - casts and auto-attack). TRUE = on, FALSE = off; optional reason key.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - blank uses the For Who window. |
| `value` | string | `TRUE` | TRUE to stop offensive, FALSE to allow. |
| `reason` | string |  | Optional reason key (blank = 'manual'). FALSE + blank clears all reasons. |

Runs: `OgreBotAPI.Combat:SetNoOffensive`

```text
oc !c -SetNoOffensive igw:${Me.Name} TRUE mezzed
```

## `-SetNoReqBowAbilities`

`-SetNoReqBowAbilities <who> <value>`

Sets the no-bow-abilities flag (default TRUE), read back with ${OgreBotAPI.Combat.NoReqBowAbilities}. A word that is not TRUE or FALSE leaves it unchanged.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string | `TRUE` |  |

Runs: `OgreBotAPI.Combat:SetNoReqBowAbilities`

```text
oc !c -SetNoReqBowAbilities igw:${Me.Name} TRUE
```

## `-SetUpFor`

`-SetUpFor <who> <chat> <restart>`

Sets up for an encounter: the named mob given, or with it blank the nearest or engaged named in this zone.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `chat` | string |  | Name of the mob to set up for, for example Dagrin. Blank uses the nearest or engaged named in this zone. |
| `restart` | bool | `TRUE` | TRUE: a setup already running starts again from the top, like pressing the setup button. FALSE: a setup already running is left alone (how the Instance Controller calls it). |

Runs: `OgreBotAPI.Bot:SetUpFor`

```text
oc !c -SetUpFor igw:${Me.Name} "${Target.Name}" TRUE
```

## `-ShareAllMissions`

`-ShareAllMissions <who>`

Shares all mission quests. Only shares if everyone in group is nearby.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Quest:ShareAllMissions`

```text
oc !c -ShareAllMissions ${Me.Name}
```

## `-ShareMission`

`-ShareMission <who> <value>`

Shares a mission quest. Only shares if everyone in group is nearby.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string |  | Quest name |

Runs: `OgreBotAPI.Quest:ShareMission`

```text
oc !c -ShareMission ${Me.Name} "Zone Mission"
```

## `-ShareQuest`

`-ShareQuest <who> <value>`

Shares a quest. This has very limited checks.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string |  | Quest name |

Runs: `OgreBotAPI.Quest:ShareQuest`

```text
oc !c -ShareQuest ${Me.Name} "A Lost Shipment"
```

## `-ShareQuestsForZone`

`-ShareQuestsForZone <who> <value>`

Toon will share any quests for their current zone. You can specify a name to have them share instead of group leader. Use ${Me.Name} for the character pressing the MCP button.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string |  |  |

Runs: `OgreBotAPI.Zone:ShareQuestsForZone`

```text
oc !c -ShareQuestsForZone igw:${Me.Name} ${Me.Name}
```

## `-ShowAvailableSetups`

`-ShowAvailableSetups <who>`

Also: `-Show_Available_Set_ups`

Prints the encounter coding for the current zone in the console, one line per fight.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Encounter:List`

```text
oc !c -ShowAvailableSetups ${Me.Name}
```

## `-ShowWikiForQuest`

`-ShowWikiForQuest <who> <questname>`

Opens wiki for a quest.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `is1` | Who to target - leave blank to use the For Who window. |
| `questname` | string |  | Questname. If blank uses your currently active quest |

Runs: `OgreBotAPI.Quest:ShowWiki`

```text
oc !c -ShowWikiForQuest ${Me.Name} "A Lost Shipment"
```

## `-SmartLoot_ReloadDataFromFile`

`-SmartLoot_ReloadDataFromFile <who>`

Re-reads the smart loot data (item loot limits and each character's loot counts) from file on the matched toons. While loot hand-outs are still in progress, the character counts wait until they finish.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Loot:Reload`

```text
oc !c -SmartLoot_ReloadDataFromFile all
```

## `-Special`

`-Special <who>`

Also: `-SpecialForWho`

Clicks the nearest special.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI:Special`

```text
oc !c -Special igw:${Me.Name}
```

## `-SpecialZoneSpecific`

`-SpecialZoneSpecific <who>`

Also: `-SpecialZS`

Clicks the nearest special that is specifically coded for that zone. If one doesn't exist - clicks the nearest special.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Zone:SpecialZoneSpecific`

```text
oc !c -SpecialZoneSpecific igw:${Me.Name}
```

## `-Spew_BoZ_Research`

`-Spew_BoZ_Research <who>`

Opens the research window if it is not up, waits for it to fill, broadcasts every row as label -> status, then closes the window. It is queued behind other actions, and prints a console line when the window has no rows.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Debug:SpewResearchWindow`

```text
oc !c -Spew_BoZ_Research ${Me.Name}
```

## `-Spew_MissionTimerInfo_AP`

`-Spew_MissionTimerInfo_AP <who> <args>`

Queues a read of the quest journal's Mission Timers tab and posts one OgreConsole line per mission whose name contains any of your search words, with its reset time and whether it is completed. With no search word it prints only a note asking for one.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `args` | rest |  |  |

Runs: `OgreBotAPI.Quest:SpewMissionTimers`

```text
oc !c -Spew_MissionTimerInfo_AP igw:${Me.Name} Weekly
```

## `-Spew_RelayGroup`

`-Spew_RelayGroup <who>`

Also: `-RelayGroups_Spew`

Sends this session's relay group name to every session in this PC's relay group, shown in OgreConsole.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Comms:SpewRelayGroup`

```text
oc !c -Spew_RelayGroup all
```

## `-SpewFlags`

`-SpewFlags <who>`

Posts one OgreConsole line per flag this character holds, as '&lt;name> Flagged &lt;number>', and nothing when it holds none. A marked character also lists flag 24, because the mark is kept as flag 24.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Roster:SpewFlags`

```text
oc !c -SpewFlags igw:${Me.Name}
```

## `-SpewStat`

`-SpewStat <who> <type> <value> <where>`

Also: `-SpewStats`

Displays a specific stat for all your toons.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to report - blank uses the For Who window. |
| `type` | string | `-stat` | What kind of stat to report. |
| `value` | string |  | The stat key / item name / ability name or id (blank for -marked). |
| `where` | string | `oc` | Where to report. |

Runs: `OgreBotAPI.Debug:BroadcastStat`

```text
oc !c -SpewStat all -stat potency oc
```

## `-SpewSubscriptionStatus`

`-SpewSubscriptionStatus <who>`

Also: `-SubscriptionStatus`, `-SubStatus`

Reads the All-Access button's tooltip in the marketplace window and broadcasts it with a verdict: Good, Need to claim, Need more time, Not a member or Unknown. It opens no window, so it reports Unknown until the marketplace page has been shown.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Debug:SpewSubscriptionStatus`

```text
oc !c -SpewSubscriptionStatus all
```

## `-stand`

`-stand <who>`

If you are FD you will stand up.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Movement:Stand`

```text
oc !c -stand igw:${Me.Name}
```

## `-StatPotions_AutoConsume`

`-StatPotions_AutoConsume <who> <value> <potion>`

Modifies stat potions AutoConsume based on Parameter 2 input.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string | `TRUE` | Value. Options are: TRUE. FALSE. TOGGLE. REPORT |
| `potion` | string |  | Optional. Potion name. Leave blank for the configured stat potion (Planar Elixir of intellect). |

Runs: `OgreBotAPI.Inventory:AutoConsumeStatPotions`

```text
oc !c -StatPotions_AutoConsume igw:${Me.Name} TOGGLE
```

## `-StatPotions_Replenish`

`-StatPotions_Replenish <who> <potion>`

Replenishes stat potions from the depot.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `potion` | string |  | Optional. Potion name. Leave blank for the configured stat potion (Planar Elixir of intellect). |

Runs: `OgreBotAPI.Consumables:ReplenishStatPotions`

```text
oc !c -StatPotions_Replenish igw:${Me.Name}
```

## `-StopRes`

`-StopRes <who>`

Turns ressing off: checks Disable CS_Res, so the Cast Stack's Res entries are skipped.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Session:StopRes`

```text
oc !c -StopRes igw:${Me.Name}
```

## `-Summon_Familiar`

`-Summon_Familiar <who>`

Summons your familiar.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Consumables:SummonFamiliar`

```text
oc !c -Summon_Familiar igw:${Me.Name}
```

## `-Target`

`-Target <who> <targetwho>`

Targets an actor once. Takes part of a name; me targets yourself.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `targetwho` | string | `${Me.Name}` | Target Name |

Runs: `OgreBotAPI:Target`

```text
oc !c -Target igw:${Me.Name} ${Group[1].Name}
```

## `-targetlock`

`-targetlock <who> <target>`

Also: `-TargetLock`

Lock targeting to one target (a priority override above auto-target/assist) until cleared. Numeric = actor ID; 'clear'/'0'/'off' releases.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `target` | string | `0` | Target name or actor ID; 'clear'/'0'/'off' to release the lock. |

Runs: `OgreBotAPI:TargetLock`

```text
oc !c -targetlock igw:${Me.Name} ${Target.ID}
```

## `-Tell`

`-Tell <who> <target> <message>`

The toons named by the first argument (a for-who; left out, the For Who window) send an in-game /tell of message to target. A missing target or message is refused with one console line, and a target or message that contains NULL is not sent - a line on IRC says so instead.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who sends the tell - leave blank to use the For Who window. |
| `target` | string |  | The toon to send the tell to |
| `message` | string |  | The message (quote it when it has spaces) |

Runs: `OgreBotAPI.Comms:SendTell`

```text
oc !c -Tell ${Me.Name} ${Group[1].Name} "Ready when you are"
```

## `-TempAdorns`

`-TempAdorns <who> <profile>`

Applies a saved temp-adornment profile: each gear piece it names gets its temporary adornment, even one that still has it. `ogre tempadorns` opens the window that makes and saves profiles (CBOC, Pot and HP come ready-made).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `profile` | string |  | The profile to apply - its name as saved in the Temp Adornments window (`ogre tempadorns list` prints them) |

Runs: `OgreBotAPI.TempAdorns:Apply`

```text
oc !c -TempAdorns igw:${Me.Name} CBOC FALSE
```

## `-ThreatFighterIgnoreList_Add`

`-ThreatFighterIgnoreList_Add <who> <args>`

Adds one or more player names to the threat fighter ignore list: a fighter on it is not counted as a fighter tanking when the bot checks its while-a-fighter-is-tanking limits on force-target and threat-position-increase abilities.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `args` | rest |  |  |

Runs: `OgreBotAPI.Combat:ThreatIgnoreAdd`

```text
oc !c -ThreatFighterIgnoreList_Add igw:${Me.Name} ${Group[1].Name}
```

## `-ThreatFighterIgnoreList_Clear`

`-ThreatFighterIgnoreList_Clear <who>`

Empties the threat fighter ignore list.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Combat:ThreatIgnoreClear`

```text
oc !c -ThreatFighterIgnoreList_Clear igw:${Me.Name}
```

## `-ThreatFighterIgnoreList_Remove`

`-ThreatFighterIgnoreList_Remove <who> <args>`

Removes one or more player names from the threat fighter ignore list.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `args` | rest |  |  |

Runs: `OgreBotAPI.Combat:ThreatIgnoreRemove`

```text
oc !c -ThreatFighterIgnoreList_Remove igw:${Me.Name} ${Group[1].Name}
```

## `-Timer`

`-Timer <who> <time> <slot> <message> <minupdatetimer>`

Also: `-OnScreenTimer`

Puts a raid timer on-screen. Enter no parameters to see an example!

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `time` | string | `30` | Duration in seconds |
| `slot` | string | `1` | Slot number. Valid options: 1-10 |
| `message` | string | `Timer:` | Message. The timer will be at the end of this message |
| `minupdatetimer` | string | `1` |  |

Runs: `OgreBotAPI.Util:OnScreenTimer`

```text
oc !c -Timer all 60 2 Burn: 1
```

## `-ToggleMainWindow`

`-ToggleMainWindow <who>`

Also: `-Main`

Toggles the main window. Same as pressing Show Main or Hide Main.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Windows:ToggleMain`

```text
oc !c -ToggleMainWindow igw:${Me.Name}
```

## `-ToggleZoneReset`

`-ToggleZoneReset <who>`

Loads the Zone Reuse window and reads its table, so the zone reset timers are known and ${OgreBotAPI.Zone.ResetZoneData} can answer. Despite the name it is not a toggle: the window ends closed.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Zone:ResetUpdateInfo`

```text
oc !c -ToggleZoneReset igw:${Me.Name}
```

## `-ToonMarked`

`-ToonMarked <who> <where>`

Reports who is marked.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `where` | string | `oc` |  |

Runs: `OgreBotAPI.Roster:SpewMarked`

```text
oc !c -ToonMarked igw:${Me.Name} oc
```

## `-Travel`

`-Travel <who> <value> <exactmatch> <multiplezoneoption>`

Also: `-TravelMap`

Clicks a location on the Travel map. IE: When you click a bell. Commas do not work. Use text before or after it. Such as 'the Scourge Wastes'.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string |  | Name of where you want to go. IE: Qeynos |
| `exactmatch` | string | `FALSE` | Exact match |
| `multiplezoneoption` | string | `LAST_ENTRY` | If multiple zones which zone to go to |

Runs: `OgreBotAPI.Travel:Travel`

```text
oc !c -Travel igw:${Me.Name} Qeynos FALSE LAST_ENTRY
```

## `-TravelBell`

`-TravelBell <who> <value> <exactmatch> <multiplezoneoption>`

Attempts to click on a bell and clicks a location on the Travel map. Commas do not work. Use text before or after it. Such as 'the Scourge Wastes'.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string |  | Name of where you want to go. IE: Qeynos |
| `exactmatch` | string | `FALSE` | Exact match |
| `multiplezoneoption` | string | `LAST_ENTRY` | If multiple zones which zone to go to |

Runs: `OgreBotAPI.Travel:Bell`

```text
oc !c -TravelBell igw:${Me.Name} Qeynos FALSE LAST_ENTRY
```

## `-TravelDruid`

`-TravelDruid <who> <value> <exactmatch> <multiplezoneoption>`

Attempts to click on a Druid bush and clicks a location on the Travel map. Commas do not work. Use text before or after it. Such as 'the Scourge Wastes'.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string |  | Name of where you want to go. IE: Qeynos |
| `exactmatch` | string | `FALSE` | Exact match |
| `multiplezoneoption` | string | `LAST_ENTRY` | If multiple zones which zone to go to |

Runs: `OgreBotAPI.Travel:Druid`

```text
oc !c -TravelDruid igw:${Me.Name} Antonica FALSE LAST_ENTRY
```

## `-TravelMesh`

`-TravelMesh <who> <destination> <poi>`

Plans a route from the zone you are in to the destination zone and travels it, hop by hop. Quote a destination of more than one word: "Qeynos Harbor". The optional point of interest is a named spot inside the destination zone to finish at.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `destination` | string |  | Zone to travel to. IE: Antonica |
| `poi` | string |  | Optional point of interest in the destination zone. IE: "Druid Rings" |

Runs: `OgreBotAPI.Travel:Mesh`

```text
oc !c -TravelMesh igw:${Me.Name} Antonica "Druid Rings"
```

## `-TravelMeshFeatures`

`-TravelMeshFeatures <who> <flag> <value>`

With no flag: prints the account travel features known for this character and scans any that are unanswered. With a flag and TRUE or FALSE: sets that feature by hand, and it is never re-scanned.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `flag` | string |  | Optional feature flag to set. IE: roc_friends_and_family |
| `value` | string |  | TRUE or FALSE - only with a flag |

Runs: `OgreBotAPI.Travel:MeshFeatures`

```text
oc !c -TravelMeshFeatures ${Me.Name} roc_friends_and_family TRUE
```

## `-TravelMeshGroup`

`-TravelMeshGroup <who> <destination> <poi>`

Sends your whole group to the destination zone. Every member plans their own route from wherever they are, with staggered starts. Run it on ONE character - it tells the rest of the group itself.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `destination` | string |  | Zone to travel to. IE: Antonica |
| `poi` | string |  | Optional point of interest in the destination zone. IE: "Druid Rings" |

Runs: `OgreBotAPI.Travel:MeshGroup`

```text
oc !c -TravelMeshGroup ${Me.Name} Antonica
```

## `-TravelMeshPreview`

`-TravelMeshPreview <who> <destination>`

Prints the route the travel mesh would take to the destination zone, one line per hop. Moves nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `destination` | string |  | Zone to plan a route to. IE: Antonica |

Runs: `OgreBotAPI.Travel:MeshPreview`

```text
oc !c -TravelMeshPreview ${Me.Name} Antonica
```

## `-TravelMeshStop`

`-TravelMeshStop <who>`

Stops the travel mesh route in progress.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Travel:MeshStop`

```text
oc !c -TravelMeshStop igw:${Me.Name}
```

## `-TravelSpires`

`-TravelSpires <who> <value> <exactmatch> <multiplezoneoption>`

Also: `-TravelSpire`

Attempts to click on a Spire and clicks a location on the Travel map. Commas do not work. Use text before or after it. Such as 'the Scourge Wastes'.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string |  | Name of where you want to go. IE: Qeynos |
| `exactmatch` | bool | `FALSE` | Exact match |
| `multiplezoneoption` | string | `LAST_ENTRY` | If multiple zones which zone to go to |

Runs: `OgreBotAPI.Travel:Spires`

```text
oc !c -TravelSpires igw:${Me.Name} Antonica FALSE LAST_ENTRY
```

## `-TTS`

`-TTS <who> <message>`

Speaks the message aloud through InnerSpace text-to-speech on this PC. A blank message does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `message` | string |  |  |

Runs: `OgreBotAPI.Comms:TTS`

```text
oc !c -TTS ${Me.Name} "Named is up"
```

## `-UnflagAll`

`-UnflagAll <who>`

Removes all Flags designation from characters.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Roster:UnflagAll`

```text
oc !c -UnflagAll igw:${Me.Name}
```

## `-UnflagToon`

`-UnflagToon <who> <value>`

Removes a Flag designation from characters.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string | `1` | Flag # from 1 to 24 |

Runs: `OgreBotAPI.Roster:Unflag`

```text
oc !c -UnflagToon ${Me.Name} 3
```

## `-UnmarkToon`

`-UnmarkToon <who>`

Removes the mark (flag 24) from each selected character.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Roster:Unmark`

```text
oc !c -UnmarkToon ${Me.Name}
```

## `-Unmentor`

`-Unmentor <who>`

Tells [Bots] to unmentor.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Roster:Unmentor`

```text
oc !c -Unmentor igw:${Me.Name}
```

## `-Unpack`

`-Unpack <who> <itemname> <args>`

Unpack an item in your bags. After the item, in any order: -qty N unpacks N of them, -all keeps going until none is left, and -pick &lt;number \| name \| lowest> says which reward to take when the window offers a choice (lowest = the one you have fewest of in your bags). A reward window that is already open is waited out first, up to 10 seconds.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `itemname` | string |  | The item to unpack, by its full name. Put it in quotes when it has spaces. |
| `args` | rest |  | Optional: -qty &lt;N> or -all, and -pick &lt;number \| name \| lowest> |

Runs: `OgreBotAPI.Inventory:Unpack`

```text
oc !c -Unpack ${Me.Name} "Overseer Reward Crate" -all
```

## `-Unpack_Consume_Familiars`

`-Unpack_Consume_Familiars <who>`

Unpacks and adds Familiars to collection if possible otherwise consumes for experience.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Inventory:UnpackConsumeFamiliars`

```text
oc !c -Unpack_Consume_Familiars igw:${Me.Name}
```

## `-Unpack_Familiars`

`-Unpack_Familiars <who>`

Unpacks Familiars.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Inventory:UnpackFamiliars`

```text
oc !c -Unpack_Familiars igw:${Me.Name}
```

## `-UpgradeItem`

`-UpgradeItem <who>`

Upgrades a piece of gear: put the old item in bag 1 slot 1 and the new one in bag 1 slot 2. The old item's adornments are moved onto the new one, the old item goes to the end of bag 1, and the new one is equipped. Both must be for the same slot, and the new one must have no adornments yet.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Inventory:UpgradeItem`

```text
oc !c -UpgradeItem ${Me.Name}
```

## `-UplinkOptionChange`

`-UplinkOptionChange <who> <object> <value> <silent>`

Also: `-UplinkOption`, `-Uplinkoption_change`, `-UO`

Changes an OgreBot option in the loaded profile: object is the control id, value the new value. The change is unsaved until the profile is saved. Note: TRUE is not the same as true.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `object` | string |  |  |
| `value` | string | `TRUE` |  |
| `silent` | bool | `FALSE` |  |

Runs: `OgreBotAPI.Options:Set`

```text
oc !c -UplinkOptionChange all checkbox_autotarget_enabled TRUE FALSE
```

## `-UplinkOptionSilent`

`-UplinkOptionSilent <who> <args>`

Also: `-UOS`

Same as -UplinkOptionChange, but never announces the change. Param 1 = For who; the rest are (control id, value) pairs.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `args` | rest |  |  |

Runs: `OgreBotAPI.Options:Set`

```text
oc !c -UplinkOptionSilent all checkbox_autotarget_enabled FALSE
```

## `-UseFlag`

`-UseFlag <who>`

Uses a flag from a guild strategist.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI:UseFlag`

```text
oc !c -UseFlag igw:${Me.Name}
```

## `-UseItem`

`-UseItem <who> <abilityname>`

Also: `-Use_Item`

Tells [Bots] to Use a specific [Item]. Note - Item names must be exact.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `abilityname` | string | `Nothing` | Item to be used |

Runs: `OgreBotAPI.Inventory:Use`

```text
oc !c -UseItem igw:${Me.Name} "Totem of the Otter"
```

## `-UseItemOnPlayer`

`-UseItemOnPlayer <who> <abilityname> <onplayer>`

Also: `-useitemon`, `-Use_Item_On_Player`

Tells [Bots] to Use a specific [Item]. Note - Item names must be exact.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `abilityname` | string | `Nothing` | Item to be used |
| `onplayer` | string | `${Me.Name}` | Use item on this player |

Runs: `OgreBotAPI.Inventory:UseOnPlayer`

```text
oc !c -UseItemOnPlayer igw:${Me.Name} "Totem of the Otter" ${Group[1].Name}
```

## `-Walk`

`-Walk <who>`

Sets walking. Presses the run toggle only if the character is running.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Movement:SetRunMode`

```text
oc !c -Walk igw:${Me.Name}
```

## `-WarnBeforeSave`

`-WarnBeforeSave <who>`

Marks that the Instance Controller has run on these characters, so the OgreBot window warns before saving the profile (cleared when a profile is loaded).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Options:WarnBeforeSave`

```text
oc !c -WarnBeforeSave igw:${Me.Name}
```

## `-Waypoint`

`-Waypoint <who> <x> <y> <z>`

Sets the game's waypoint (the in-game /waypoint trail) to the x y z location. All three numbers are required; if one is missing it prints an error and does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `x` | string |  | X, or the name of a point of interest in this zone |
| `y` | string |  |  |
| `z` | string |  |  |

Runs: `OgreBotAPI.Movement:Waypoint`

```text
oc !c -Waypoint ${Me.Name} 125.5 -10.2 340.8
```

## `-Zone`

`-Zone <who>`

Will attempt to zone you.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Zone:Zone`

```text
oc !c -Zone igw:${Me.Name}
```

## `-ZoneDoor`

`-ZoneDoor <who> <dooroption>`

Also: `-Door`, `-DoorX`, `-ZoneDoorOption`, `-ZoneDoorForWho`, `-DoorForWho`, `-DoorXForWho`, `-ZoneDoorOptionForWho`

When zoning and you have the option to select which zone this will select the one you use as a parameter.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who acts - leave blank to use the For Who window. |
| `dooroption` | string | `1` | option to choose |

Runs: `OgreBotAPI.Travel:ZoneDoorFor`

```text
oc !c -ZoneDoor igw:${Me.Name} 1
```

## `-ZoneResetAll`

`-ZoneResetAll <who> <ballowraid>`

Also: `-resetzoneall`

Resets every resettable zone. WARNING: There is no confirmation of any sort. It resets every single zone available.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `ballowraid` | string | `FALSE` |  |

Runs: `OgreBotAPI.Zone:ResetAll`

```text
oc !c -ZoneResetAll igw:${Me.Name} FALSE
```
