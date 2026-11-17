# Console commands: O-R

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## `-ofol---`

`-ofol--- <who>`

Also: `-OFolDecDistance`, `-ofol--`

Decreases the distance of OgreFollow.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Movement:FollowDistanceDown`

```text
oc !c -ofol--- igw:${Me.Name}
```

## `-OFolIncDistance`

`-OFolIncDistance <who>`

Also: `-ofol++`, `-ofol-++`

Widens the toon's OgreFollow distances by 2: the minimum and maximum follow distance, and the back-off distance when one is set. Use -ofol--- to narrow them again.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Movement:FollowDistanceUp`

```text
oc !c -OFolIncDistance igw:${Me.Name}
```

## `-OgreBotAPI`

`-OgreBotAPI <who> <apicall> <args>`

Call a flat OgreBotAPI verb: the for-who is passed FIRST (every flat verb gates on it), then the rest as ONE argument.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `apicall` | string |  |  |
| `args` | rest |  |  |

Runs: `OgreBotAPI:${apicall}`

```text
oc !c -OgreBotAPI igw:${Me.Name} NoTarget
```

## `-OgreBotToggleConsoleWindow`

`-OgreBotToggleConsoleWindow <who> <value>`

Toggles the OgreConsole window.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string | `TOGGLE` | Value |

Runs: `OgreBotAPI.Windows:ToggleConsole`

```text
oc !c -OgreBotToggleConsoleWindow ${Me.Name} TOGGLE
```

## `-OgreCommandOB_AP`

`-OgreCommandOB_AP <who> <scriptname> <args>`

NOTE: Uses all parameters. Can not stack this command. Does an OgreCommand ForWho. Parameter 3+ = Parameters.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `scriptname` | string |  | command name |
| `args` | rest |  |  |

Runs: `OgreBotAPI.Bot:OgreCommand`

```text
oc !c -OgreCommandOB_AP igw:${Me.Name} tempadorns
```

## `-OgreConsole_Show`

`-OgreConsole_Show <who> <value>`

Opens the OgreConsole window when value is TRUE or blank; any other value, such as FALSE, closes it. It works before the character is in the world.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who acts - leave blank to use the For Who window. |
| `value` | string | `TRUE` |  |

Runs: `OgreBotAPI.Windows:ShowConsole`

```text
oc !c -OgreConsole_Show all TRUE
```

## `-OgreCraft_AddLastScribedRecipe`

`-OgreCraft_AddLastScribedRecipe <who> <iquantity>`

Queue the recipe you scribed most recently.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `iquantity` | string | `1` | Quantity |

Runs: `OgreBotAPI.Craft:AddLastScribedRecipe`

```text
oc !c -OgreCraft_AddLastScribedRecipe ${Me.Name} 5
```

## `-OgreCraft_AddRecipe`

`-OgreCraft_AddRecipe <who> <iquantity> <recipename>`

Add a recipe to the craft queue: its name (the rest of the line - names have spaces), its ID, or lastknownrecipe (the recipe you scribed last).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `iquantity` | int64 | `1` | How many to craft |
| `recipename` | string |  | Recipe name (quote a name with spaces), recipe ID, or lastknownrecipe |

Runs: `OgreBotAPI.Craft:AddRecipe`

```text
oc !c -OgreCraft_AddRecipe ${Me.Name} 10 lastknownrecipe
```

## `-OgreCraft_CompleteNavigation`

`-OgreCraft_CompleteNavigation <who>`

Scripters: tell a waiting craft that your script moved it (it re-checks the distance).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Craft:CompleteNavigation`

```text
oc !c -OgreCraft_CompleteNavigation ${Me.Name}
```

## `-OgreCraft_CraftQueue`

`-OgreCraft_CraftQueue <who>`

Start crafting the queue.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Craft:Start`

```text
oc !c -OgreCraft_CraftQueue ${Me.Name}
```

## `-OgreCraft_DeferNavigation`

`-OgreCraft_DeferNavigation <who>`

Scripters: hand a waiting craft walk back to craft (it moves itself).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Craft:DeferNavigation`

```text
oc !c -OgreCraft_DeferNavigation ${Me.Name}
```

## `-OgreCraft_ScribeRecipe`

`-OgreCraft_ScribeRecipe <who> <recipename>`

Scribe scribeable scrolls in your bags (blank/all = every one).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `recipename` | string | `all` | Scroll name (quote a name with spaces) OR all |

Runs: `OgreBotAPI.Craft:ScribeRecipe`

```text
oc !c -OgreCraft_ScribeRecipe ${Me.Name} all
```

## `-OgreCraft_StartLLL`

`-OgreCraft_StartLLL <who>`

Start Low Level Leveling - the Low Level Leveling tab settings.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Craft:StartLLL`

```text
oc !c -OgreCraft_StartLLL ${Me.Name}
```

## `-OgreCraft_StartQuest`

`-OgreCraft_StartQuest <who>`

Craft the current quest’s recipe steps - one of each per pass, re-reading the quest, until none is pending.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Craft:StartQuest`

```text
oc !c -OgreCraft_StartQuest ${Me.Name}
```

## `-OgreCraft_StartTinker`

`-OgreCraft_StartTinker <who>`

Start Auto Tinkering - the Auto Tinkering tab settings.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Craft:StartTinker`

```text
oc !c -OgreCraft_StartTinker ${Me.Name}
```

## `-OgreCraft_StartWrits`

`-OgreCraft_StartWrits <who>`

Start crafting writs (rush orders) - the Writs tab settings.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Craft:StartWrits`

```text
oc !c -OgreCraft_StartWrits ${Me.Name}
```

## `-OgreCraft_Stop`

`-OgreCraft_Stop <who>`

Stop the crafting run (queue, writs, quest, Low Level Leveling or Auto Tinkering). With nothing running it says so and drops a pause.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Craft:Stop`

```text
oc !c -OgreCraft_Stop ${Me.Name}
```

## `-ogrefollow`

`-ogrefollow <who> <whotofollow> <mindistance> <maxdistance> <breakonfollow> <backoffdistance>`

Also: `-ofollow`, `-ofol`

Ogre Follow Default.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `whotofollow` | string | `${Me.Name}` | Who to follow |
| `mindistance` | float | `8` | Min Distance |
| `maxdistance` | float | `200` | Max Distance |
| `breakonfollow` | bool | `FALSE` | Break on follow |
| `backoffdistance` | float | `0` | Back off distance - back up while closer than this to the one you follow (0 = off) |

Runs: `OgreBotAPI.Movement:Follow`

```text
oc !c -ogrefollow igw:${Me.Name} ${Me.Name} 8 200 FALSE 0
```

## `-OgreZoneForceReset`

`-OgreZoneForceReset <who> <zonename>`

FORCE resets one zone lockout. SPENDS ONE OF YOUR LIMITED RESET CHARGES and cannot be undone.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `zonename` | string |  | Exact zone name as the Zone Reuse window shows it. |

Runs: `OgreBotAPI.Zone:ForceReset`

```text
oc !c -OgreZoneForceReset ${Me.Name} "${Zone.Name}"
```

## `-OK_Button`

`-OK_Button <who>`

Presses OK to a pop up that has OK.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Windows:OK`

```text
oc !c -OK_Button igw:${Me.Name}
```

## `-OpenAndBuyFromMerchant`

`-OpenAndBuyFromMerchant <who> <merchantname> <itemname> <value>`

Opens the nearest merchant whose name contains the merchant name (when no merchant window is open), then buys the quantity of the item and accepts the purchase confirmation. Runs in the action queue, and prints a console line when the window never opens or the merchant does not sell the item.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `merchantname` | string |  |  |
| `itemname` | string |  |  |
| `value` | string | `1` |  |

Runs: `OgreBotAPI.Merchant:OpenAndBuy`

```text
oc !c -OpenAndBuyFromMerchant ${Me.Name} ${Target.Name} "Bundle of Arrows" 1
```

## `-OpenAndBuyFromMerchantXTimes`

`-OpenAndBuyFromMerchantXTimes <who> <merchantname> <itemname> <value> <timestobuy>`

Same as -OpenAndBuyFromMerchant, repeated timestobuy times. A blank merchant or item name, or a count below 1, is refused with a console line.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `merchantname` | string |  |  |
| `itemname` | string |  |  |
| `value` | string | `1` |  |
| `timestobuy` | string | `1` |  |

Runs: `OgreBotAPI.Merchant:OpenAndBuyXTimes`

```text
oc !c -OpenAndBuyFromMerchantXTimes ${Me.Name} ${Target.Name} "Bundle of Arrows" 1 5
```

## `-Overseer_AddAgentsToCollection`

`-Overseer_AddAgentsToCollection <who> <destroy>`

Adds Agents to your overseer collection. Destroys if duplicates.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `destroy` | string | `TRUE` | Destroy if duplicate. TRUE or FALSE |

Runs: `OgreBotAPI.Overseer:AddAgents`

```text
oc !c -Overseer_AddAgentsToCollection ${Me.Name} TRUE
```

## `-Overseer_AutoAddOverseerQuests`

`-Overseer_AutoAddOverseerQuests <who>`

Uses the Overseer mission scrolls in your bags to add their quests to your Overseer quest list.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Overseer:AutoAddQuests`

```text
oc !c -Overseer_AutoAddOverseerQuests ${Me.Name}
```

## `-Overseer_BuyMissions`

`-Overseer_BuyMissions <who> <args>`

Also: `-BuyOverseerMissions`

Buys Overseer missions from the merchant you are standing at (or a nearby Administrator Agent), then scribes them. Each character uses its own Overseer tab options unless you pass flags.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `args` | rest |  | Optional overrides: -s &lt;season 1-7> -c &lt;Any\|Blue\|Yellow\|Purple\|Green> -n &lt;different recipes> -a &lt;of each, max 20> -noscribe -destroy -replenishonly |

Runs: `OgreBotAPI.Overseer:BuyMissions`

```text
oc !c -Overseer_BuyMissions igw:${Me.Name}
```

## `-Overseer_CheckQuests`

`-Overseer_CheckQuests <who>`

Runs Overseer scan.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Overseer:CheckQuests`

```text
oc !c -Overseer_CheckQuests ${Me.Name}
```

## `-PackPony`

`-PackPony <who> <forcecheck>`

Checks your packpony based off Ogrebot packpony tab. ** Ogre keeps track of when it was run last. TRUE makes it run again no matter what.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `forcecheck` | string | `FALSE` | Force it to run |

Runs: `OgreBotAPI.Inventory:CheckPackPony`

```text
oc !c -PackPony igw:${Me.Name} TRUE
```

## `-Path`

`-Path <who> <name>`

Walks a saved path of the zone you are in, point by point. It runs while OgreBot is paused, and waits through a fight or a death. A point that does not resolve stops it before anything moves.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `name` | string |  | The path's name, in any case. IE: autohuntpath1 |

Runs: `OgreBotAPI.Paths:Start`

```text
oc !c -Path igw:${Me.Name} autohuntpath1
```

## `-PathStop`

`-PathStop <who>`

Stops the path being walked. The toon stands where it is.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Paths:Stop`

```text
oc !c -PathStop igw:${Me.Name}
```

## `-pause`

`-pause <who>`

Pauses all the bots.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Bot:Pause`

```text
oc !c -pause igw:${Me.Name}
```

## `-PetAssist`

`-PetAssist <who>`

Sends the game's pet autoassist command, so the pet assists its owner.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Pet:Assist`

```text
oc !c -PetAssist igw:${Me.Name}
```

## `-petattack`

`-petattack <who>`

Also: `-PetOn`, `-pet_on`, `-pet-on`, `-pet-attack`, `-pet_attack`

Everyone does a pet attack command.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Pet:Attack`

```text
oc !c -petattack igw:${Me.Name}
```

## `-PetGetLost`

`-PetGetLost <who>`

Sends the game's pet get lost command, dismissing the toon's pet.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Pet:GetLost`

```text
oc !c -PetGetLost igw:${Me.Name}
```

## `-PetOff`

`-PetOff <who>`

Also: `-pet_off`, `-pet-off`

Everyone does a pet back off command.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Pet:Off`

```text
oc !c -PetOff igw:${Me.Name}
```

## `-POI_Add`

`-POI_Add <name> <x> <y> <z> <sender>`

Saves a named point of interest in the zone you are in, where you stand or at x y z. The name then works with -TravelMesh and wherever a location does. Only the box that sends the line saves it, and every box on this PC can use it.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | string |  | The name. It cannot be empty, hold a comma or read as a number. IE: "Quest giver" |
| `x` | string |  | X, or leave blank for where you stand |
| `y` | string |  | Y |
| `z` | string |  | Z |
| `sender` | string | `${Me.Name}` | The box that saves it. Leave this out: it is the box that sent the line. |

Runs: `OgreBotAPI.POI:Add`

```text
oc !c -POI_Add "Quest giver"
```

## `-Poison_AutoConsume`

`-Poison_AutoConsume <who> <value> <potion>`

Modifies Poison AutoConsume based on Parameter 2 input.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string | `TRUE` | Value. Options are: TRUE. FALSE. TOGGLE. REPORT |
| `potion` | string |  | Poison name: Cerebral Caustic Poison, or Cerebral Hemotoxin for an assassin or brigand. Left blank, the configured stat potion is used instead. |

Runs: `OgreBotAPI.Inventory:AutoConsumeStatPotions`

```text
oc !c -Poison_AutoConsume igw:${Me.Name} TRUE "Cerebral Caustic Poison"
```

## `-Poison_Replenish`

`-Poison_Replenish <who> <potion>`

Replenishes Poison from the depot.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `potion` | string |  | Poison name: Cerebral Caustic Poison, or Cerebral Hemotoxin for an assassin or brigand. Left blank, the configured stat potion is pulled instead. |

Runs: `OgreBotAPI.Consumables:ReplenishStatPotions`

```text
oc !c -Poison_Replenish igw:${Me.Name} "Cerebral Caustic Poison"
```

## `-PortalToGuildHall`

`-PortalToGuildHall <who>`

Also: `-ToGuild`

Relays to use Magic Door to Guild Hall

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Travel:ToGuildHall`

```text
oc !c -PortalToGuildHall igw:${Me.Name}
```

## `-ProvingGrounds_Exit`

`-ProvingGrounds_Exit <who>`

Exits Proving Grounds. If in a match will exit the match. If in the lobby will exit the lobby.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Windows:ProvingGroundsExit`

```text
oc !c -ProvingGrounds_Exit igw:${Me.Name}
```

## `-ProvingGrounds_Scoreboard_Close`

`-ProvingGrounds_Scoreboard_Close <who>`

Closes the Proving Grounds scoreboard.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Windows:ProvingGroundsScoreboardClose`

```text
oc !c -ProvingGrounds_Scoreboard_Close igw:${Me.Name}
```

## `-Pushover`

`-Pushover <who> <args>`

Sends a Pushover notification using the Pushover keys saved on this PC; every word that is not a flag becomes the message, and -title &lt;text> and -priority &lt;number> are read. -sound, -device, -retry and -expire are accepted but ignored with a console note, and nothing is sent when no message is given, the keys are not set up, or Pushover's disable-all box is ticked.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `is1` | Who to target - leave blank to use the For Who window. |
| `args` | rest |  |  |

Runs: `OgreBotAPI.Comms:Pushover`

```text
oc !c -Pushover ${Me.Name} -title Raid "Named is up"
```

## `-Question`

`-Question <who>`

Collects the nearest `?` shiny within 10 meters. The harvest-node twin is -Resource.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Session:CollectShiny`

```text
oc !c -Question ${Me.Name}
```

## `-RaidAuth`

`-RaidAuth <who>`

Authorizes everyone in your raid to each other on their IRC bridges, and nobody outside it. Your bridge asks once; each PC in the raid answers once with -AIIR. Anyone in the raid may ask.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. Several characters on one PC still ask only once. |

Runs: `OgreBotAPI.Comms:IrcRaidAuth`

```text
oc !c -RaidAuth ${Me.Name}
```

## `-RaidInvite`

`-RaidInvite <who> <invitewho>`

Meant to send a raid invite to invitewho, but today it sends a group invite exactly like -Invite, because the raidinvite TRUE it passes is never read. A player already in the group or raid is skipped.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `invitewho` | string |  |  |

Runs: `OgreBotAPI.Roster:RaidInvite`

```text
oc !c -RaidInvite ${Me.Name} ${Target.Name} TRUE
```

## `-RaidUnauth`

`-RaidUnauth <who>`

Every IRC bridge in your raid removes the nicks it authorized through Auth raid (or -AIIR) and says who. Nicks authorized by hand and the bridge's own nick stay.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. Several characters on one PC still ask only once. |

Runs: `OgreBotAPI.Comms:IrcRaidUnauth`

```text
oc !c -RaidUnauth ${Me.Name}
```

## `-RawCommandOB_AP`

`-RawCommandOB_AP <who> <args>`

Also: `-RawCommandRequiresOgreBot_AllParams`, `-RawCommand`

Runs the rest of the line as a console command on each matched toon, exactly as typed, and shows it in the OgreConsole. OgreBot does not need to be running.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `args` | rest |  |  |

Runs: `OgreBotAPI.Bot:RawCommand`

```text
oc !c -RawCommandOB_AP igw:${Me.Name} eq2execute pet getlost
```

## `-Rebuff`

`-Rebuff <who>`

Also: `-FullRebuff`

Tells [Bots] to cancel all buffs. Only cancels abilities in your spell book.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Abilities:Rebuff`

```text
oc !c -Rebuff igw:${Me.Name}
```

## `-RedeemKrono`

`-RedeemKrono <who>`

Also: `-ConsumeKrono`, `-Krono`

Redeems a Krono.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Inventory:RedeemKrono`

```text
oc !c -RedeemKrono ${Me.Name}
```

## `-Reload_Bot`

`-Reload_Bot <who>`

Also: `-ReloadBot`

Reloads Ogrebot.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Bot:Reload`

```text
oc !c -Reload_Bot all
```

## `-ReloadOgreIRC`

`-ReloadOgreIRC <who>`

Reloads the IRC config on the uplink and reconnects if already connected.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Comms:IrcReload`

```text
oc !c -ReloadOgreIRC all
```

## `-RemoveNoOffensiveOn`

`-RemoveNoOffensiveOn <who> <mobname>`

Removes a mob name from the no-offensive list.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `mobname` | string | `DoesNotExist` |  |

Runs: `OgreBotAPI.Combat:RemoveNoOffensive`

```text
oc !c -RemoveNoOffensiveOn igw:${Me.Name} "${Target.Name}"
```

## `-RepairGear`

`-RepairGear <who> <force>`

Also: `-Repair`

Uses a repairer or repair bot. Parameter 1 - Forwho. Parameter 2 - Force Repair. Default FALSE.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `force` | string | `FALSE` |  |

Runs: `OgreBotAPI.Merchant:Repair`

```text
oc !c -RepairGear igw:${Me.Name} FALSE
```

## `-ReplyDialog`

`-ReplyDialog <who> <choice>`

Makes a choice in the replydialog window

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `choice` | string | `1` | Choice |

Runs: `OgreBotAPI.Windows:Reply`

```text
oc !c -ReplyDialog igw:${Me.Name} 2
```

## `-ReplyDialogClose`

`-ReplyDialogClose <who>`

Closes the reply dialog (the NPC conversation window) if one is open. Does nothing when none is open.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Windows:ReplyClose`

```text
oc !c -ReplyDialogClose igw:${Me.Name}
```

## `-Res`

`-Res <who>`

Turns ressing back on: unchecks Disable CS_Res, so the Cast Stack's Res entries run again.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Session:Res`

```text
oc !c -Res igw:${Me.Name}
```

## `-Research_Material_Check`

`-Research_Material_Check <who>`

Examines each Research Material item in your bags (Advancement, Companion, Mount, Tradeskill, Upgrade and General) and picks the first research option it offers. A type that shows No Eligible Research is skipped with a console line.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Util:CheckResearchMaterials`

```text
oc !c -Research_Material_Check ${Me.Name}
```

## `-ResetActorsLooted`

`-ResetActorsLooted <who>`

Ogrebot only tries to loot each chest once. This will reset it.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Loot:ResetLootedActors`

```text
oc !c -ResetActorsLooted igw:${Me.Name}
```

## `-ResetCameraAngle`

`-ResetCameraAngle <who>`

Resets your Camera Angle.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Client:ResetCamera`

```text
oc !c -ResetCameraAngle igw:${Me.Name}
```

## `-ResetZone`

`-ResetZone <who> <zonename>`

Resets the reuse timer of the named zone, first loading the Zone Reuse window if the toon has no zone data yet. It runs as a short queued action; a blank zone name does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `zonename` | string |  |  |

Runs: `OgreBotAPI.Zone:ResetZone`

```text
oc !c -ResetZone igw:${Me.Name} "${Zone.Name}"
```

## `-Resource`

`-Resource <who>`

Clicks the nearest Resource.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Session:Harvest`

```text
oc !c -Resource ${Me.Name}
```

## `-ResStone`

`-ResStone <who>`

Priests cast their resurrection stone spell. Other classes do nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Session:ResStone`

```text
oc !c -ResStone igw:${Me.Name}
```

## `-resume`

`-resume <who>`

Resumes all the bots.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Bot:Resume`

```text
oc !c -resume igw:${Me.Name}
```

## `-Revive`

`-Revive <who> <option> <exactmatch>`

Presses Revive on the death window, or picks a revive point first.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `option` | string | `0` | Where to revive: 0 = the death window's default Revive button; a row number; or the revive point's name, e.g. Entrance (a point the window does not list = the last revive point it lists, said with the points it has) |
| `exactmatch` | string | `FALSE` | TRUE = the name must equal the revive point's name; FALSE = the point's name contains it |

Runs: `OgreBotAPI.Session:Revive`

```text
oc !c -Revive igw:${Me.Name} 0 FALSE
```

## `-Run`

`-Run <who>`

Sets running. Presses the run toggle only if the character is walking.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Movement:SetRunMode`

```text
oc !c -Run igw:${Me.Name}
```

## `-RunScriptOB`

`-RunScriptOB <who> <scriptname> <args>`

Also: `-RunScriptRequiresOgreBot`, `-rsob`

Runs a script ForWho. Parameter 3+ = Parameters.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `scriptname` | string |  | ScriptName |
| `args` | rest |  |  |

Runs: `OgreBotAPI.Bot:RunScript`

```text
oc !c -RunScriptOB igw:${Me.Name} MyScript arg1
```
