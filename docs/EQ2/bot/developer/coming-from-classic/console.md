<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../index.md).
</div>

# Console commands (OgreConsole)

What changed between the Classic console (V1) and the new console (V2) for every command you type after `oc !c` or `oc !ci`, or put on an MCP button.

> **:warning: Two rules for every console line**
>
> 1. **The for-who comes first** on every command that targets someone. A command that had none in Classic gets `auto` - the For Who window decides, as it always did. A line that starts `oc !c -cfw <who> -Command` already says who, and still works.
> 2. **An unknown command is not silent here** - each session that receives it prints *Unknown command entered*. A command with its arguments in the wrong order, though, still runs.

## At a glance

| What happened | Names |
|---|---|
| ⚠️ Arguments changed | 39 |
| ⚠️ Argument order changed | 10 |
| ✏️ Renamed | 13 |
| ➡️ Lives somewhere else | 1 |
| 📄 In a data file now | 18 |
| ⛔ Removed | 38 |
| ✅ Works as is | 435 |
| **Total** | **554** |

435 of the 554 Classic commands are typed exactly as before (126 of those are other names - aliases - for a command, and keep working).

## 1. Commands you must change

Every Classic console command that does not work as typed any more. Sorted by what to do.

### ⚠️ Arguments changed (39)

#### ⚠️ Arguments changed: `-ZoneDoor`

```
; before (Classic)
oc !c -ZoneDoor "${UserInput}"
; after (new bot)
oc !c -ZoneDoor auto "${UserInput}"
```

| You typed | Today | Type instead | What changed | Notes |
|---|---|---|---|---|
| `-AbilityEmbargo` | runs, arguments mean something else | `-AbilityEmbargo` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-AbilityEmbargo <abilityid> <duration> [<args...>]`<br>**New:** `-AbilityEmbargo <fw> <abilityid> <duration> [<args...>]`<br>… |
| `-AbilityRotate` | runs, arguments mean something else | `-AbilityEmbargo` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-AbilityRotate <abilityid> <duration> [<args...>]`<br>**New:** `-AbilityRotate <fw> <abilityid> <duration> [<args...>]`<br>… |
| `-Apply_Verb` | runs, arguments mean something else | `-ApplyVerb` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-Apply_Verb <actorname> <verb>`<br>**New:** `-Apply_Verb <fw> <actorname> <verb>`<br>Quoting one argument is still fine ("${UserInput}" stays one argument); only the command and its arguments inside ONE pair of quotes breaks the line. |
| `-ApplyTempAdorn` | Unknown command | `-TempAdorns` | ⚠️ Arguments changed | Write `-TempAdorns <fw> <profile>`. Make the profile first in the Temp Adornments window (`ogre tempadorns`): put the adornments you want on Primary and Chest, save it, and name it on the line. An MCP button is converted for you.<br>**Old:** `-ApplyTempAdorn <fw> [adorn] [slot] - the Umbra adornments, on the primary and / or the chest`<br>**New:** `-TempAdorns <fw> <profile> [overwrite] - a saved profile: each gear piece it names gets its adornment` |
| `-ApplyTempAdorns` | Unknown command | `-TempAdorns` | ⚠️ Arguments changed | Write `-TempAdorns <fw> <profile>`. Make the profile first in the Temp Adornments window (`ogre tempadorns`): put the adornments you want on Primary and Chest, save it, and name it on the line. An MCP button is converted for you.<br>**Old:** `-ApplyTempAdorns <fw> [adorn] [slot] - the Umbra adornments, on the primary and / or the chest`<br>**New:** `-TempAdorns <fw> <profile> [overwrite] - a saved profile: each gear piece it names gets its adornment` |
| `-ApplyVerb` | runs, arguments mean something else | `-ApplyVerb` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-ApplyVerb <actorname> <verb>`<br>**New:** `-ApplyVerb <fw> <actorname> <verb>`<br>Quoting one argument is still fine ("${UserInput}" stays one argument); only the command and its arguments inside ONE pair of quotes breaks the line. |
| `-AutoItemCure` | runs, arguments mean something else | `-AutoItemCure` | ⚠️ Arguments changed | Keep one cure type (or none). The new command has no argument for the exclusive / DirectTarget / Curse flags.<br>**Old:** `-AutoItemCure <fw> [<flag> ...]`<br>**New:** `-AutoItemCure <fw> [<type>]` |
| `-Cancel_Maintained` | runs, arguments mean something else | `-CancelMaintained` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-Cancel_Maintained <ability> [<more abilities...>]`<br>**New:** `-Cancel_Maintained <fw> <abilityname> [<args...>]`<br>Classic's `-CancelMaintainedForWho` and `-Cancel_MaintainedForWho` (already for-who first) are now other names for this same command. |
| `-CancelMaintained` | runs, arguments mean something else | `-CancelMaintained` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-CancelMaintained <ability> [<more abilities...>]`<br>**New:** `-CancelMaintained <fw> <abilityname> [<args...>]`<br>Classic's `-CancelMaintainedForWho` and `-Cancel_MaintainedForWho` (already for-who first) are now other names for this same command. |
| `-ccs` | runs, arguments mean something else | `-ChangeCampSpot` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-ccs <x> <y> <z> (or one x,y,z token)`<br>**New:** `-ccs <fw> <x> <y> <z>`<br>… |
| `-Change_CampSpot` | runs, arguments mean something else | `-ChangeCampSpot` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-Change_CampSpot <x> <y> <z> (or one x,y,z token)`<br>**New:** `-Change_CampSpot <fw> <x> <y> <z>`<br>… |
| `-ChangeCampSpot` | runs, arguments mean something else | `-ChangeCampSpot` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-ChangeCampSpot <x> <y> <z> (or one x,y,z token)`<br>**New:** `-ChangeCampSpot <fw> <x> <y> <z>`<br>… |
| `-CheckMemberLevel` | runs, arguments mean something else | `-CheckMemberLevel` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-CheckMemberLevel <onlyShowNonMembers>`<br>**New:** `-CheckMemberLevel <fw> <value>`<br>`<value>` defaults to FALSE. |
| `-CompareQuest` | runs, arguments mean something else | `-CompareQuest` | ⚠️ Arguments changed | Drop the step-line arguments; send it from the box whose step is the reference. The answers come back to the asker.<br>**Old:** `-CompareQuest <fw> <questname> <step lines...>`<br>**New:** `-CompareQuest <fw> <questname>`<br>GROUP-scoped by default (comms is local-box). |
| `-Door` | runs, arguments mean something else | `-ZoneDoor` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-Door <dooroption>`<br>**New:** `-Door <fw> <dooroption>`<br>`<dooroption>` defaults to 1. Classic's `-ZoneDoorForWho`, `-DoorForWho`, `-DoorXForWho` and `-ZoneDoorOptionForWho` (already for-who first) are now other names for this same command. |
| `-DoorX` | runs, arguments mean something else | `-ZoneDoor` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-DoorX <dooroption>`<br>**New:** `-DoorX <fw> <dooroption>`<br>`<dooroption>` defaults to 1. Classic's `-ZoneDoorForWho`, `-DoorForWho`, `-DoorXForWho` and `-ZoneDoorOptionForWho` (already for-who first) are now other names for this same command. |
| `-EndScript` | runs, arguments mean something else | `-EndScript` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-EndScript <scriptname>`<br>**New:** `-EndScript <fw> <scriptname>`<br>It runs `OgreBotAPI.Bot:EndScript`. |
| `-Group` | runs, arguments mean something else | `-Raid` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-Group <chat>`<br>**New:** `-Group <fw> <chat>`<br>Classic's always sent the chat line to every session (its InjectChat_ForAll); the new command takes a for-who first, like every other, and runs `OgreBotAPI.Comms:InjectChat`. |
| `-ImmRes` | runs, arguments mean something else | `-ImmRes` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-ImmRes <howmany>`<br>**New:** `-ImmRes <fw> <howmany>`<br>`<howmany>` defaults to 2. |
| `-ItemEmbargo` | runs, arguments mean something else | `-ItemEmbargo` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-ItemEmbargo <abilityid> <duration> [<args...>]`<br>**New:** `-ItemEmbargo <fw> <abilityid> <duration> [<args...>]`<br>… |
| `-ItemRotate` | runs, arguments mean something else | `-ItemEmbargo` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-ItemRotate <abilityid> <duration> [<args...>]`<br>**New:** `-ItemRotate <fw> <abilityid> <duration> [<args...>]`<br>… |
| `-Mentor` | runs, arguments mean something else | `-Mentor` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-Mentor <mentorwho>`<br>**New:** `-Mentor <fw> <mentorwho>`<br>`<mentorwho>` defaults to `${Me.Name}`. |
| `-Move2Area` | runs, arguments mean something else | `-Move2Area` | ⚠️ Arguments changed | Move the for-who to the front and give three coordinates (x y z).<br>**Old:** `-Move2Area <X> <Z> <fw> <precision>`<br>**New:** `-Move2Area <fw> <x> <y> <z> <precision>`<br>V1's two coordinates were X and Z - a ground move. V2 takes x y z so ${Me.Loc} pastes straight in, and IGNORES y: put any number there. |
| `-Move2AreaNoTarget` | runs, arguments mean something else | `-MoveToAreaNoTarget` | ⚠️ Arguments changed | Move the for-who to the front and give three coordinates (x y z).<br>**Old:** `-Move2AreaNoTarget <X> <Z> <fw> <precision>`<br>**New:** `-Move2AreaNoTarget <fw> <x> <y> <z> <precision>`<br>V1's two coordinates were X and Z - a ground move. V2 takes x y z so ${Me.Loc} pastes straight in, and IGNORES y: put any number there. The V2 row runs OgreBotAPI.Movement:Move2AreaNoTarget: it moves with or without a target, as V1 did. |
| `-MoveToArea` | runs, arguments mean something else | `-Move2Area` | ⚠️ Arguments changed | Move the for-who to the front and give three coordinates (x y z).<br>**Old:** `-MoveToArea <X> <Z> <fw> <precision>`<br>**New:** `-MoveToArea <fw> <x> <y> <z> <precision>`<br>V1's two coordinates were X and Z - a ground move. V2 takes x y z so ${Me.Loc} pastes straight in, and IGNORES y: put any number there. |
| `-MoveToAreaNoTarget` | runs, arguments mean something else | `-MoveToAreaNoTarget` | ⚠️ Arguments changed | Move the for-who to the front and give three coordinates (x y z).<br>**Old:** `-MoveToAreaNoTarget <X> <Z> <fw> <precision>`<br>**New:** `-MoveToAreaNoTarget <fw> <x> <y> <z> <precision>`<br>V1's two coordinates were X and Z - a ground move. V2 takes x y z so ${Me.Loc} pastes straight in, and IGNORES y: put any number there. The V2 row runs OgreBotAPI.Movement:Move2AreaNoTarget: it moves with or without a target, as V1 did. |
| `-OgreBotAPI` | runs, arguments mean something else | `-OgreBotAPI` | ⚠️ Arguments changed | The method now receives the for-who first, as every new-bot OgreBotAPI method expects; the method name must be one the new OgreBotAPI registers (see the API conversion guide - most Classic flat names moved).<br>**Old:** `-OgreBotAPI <fw> <OldMethod> <args...> -> OgreBotAPI:<OldMethod>[<args...>]`<br>**New:** `-OgreBotAPI <fw> <method> <args...> -> OgreBotAPI:<method>[<fw>,<args...>]` |
| `-OgreConsole_Show` | runs, arguments mean something else | `-OgreConsole_Show` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-OgreConsole_Show <show>`<br>**New:** `-OgreConsole_Show <fw> <value>`<br>Classic's called OgreConsole:ShowOgreConsole on each session that read the line. `<value>` defaults to TRUE; the new command runs `OgreBotAPI.Windows:ShowConsole`. |
| `-Poison_AutoConsume` | works | `-Poison_AutoConsume` | ⚠️ Arguments changed | Name the poison as the third argument - Cerebral Caustic Poison, or Cerebral Hemotoxin on an assassin or brigand. The classic row picked it from your class when it was left blank; the new row fills a blank name with your configured stat potion instead.<br>**Old:** `-Poison_AutoConsume <fw> <value> [poison]`<br>**New:** `-Poison_AutoConsume <fw> <value> <poison>`<br>Not carried: the class default name, and the class check (any class acts on the poison it is given). |
| `-Poison_Replenish` | works | `-Poison_Replenish` | ⚠️ Arguments changed | Name the poison as the second argument - Cerebral Caustic Poison, or Cerebral Hemotoxin on an assassin or brigand. The classic row picked it from your class when it was left blank; the new row pulls your configured stat potion instead.<br>**Old:** `-Poison_Replenish <fw> [poison]`<br>**New:** `-Poison_Replenish <fw> <poison>`<br>Not carried: the class default name, and the class check (any class pulls the poison it is given). |
| `-Raid` | runs, arguments mean something else | `-Raid` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-Raid <chat>`<br>**New:** `-Raid <fw> <chat>`<br>… |
| `-Run` | runs, arguments mean something else | `-Run` | ⚠️ Arguments changed | Nothing to retype; check the intent - V2 does what the name says.<br>**Old:** `-Run <fw> - flipped the current mode (a -Run sent to a box already running made it walk). New: -Run <fw> - sets run; a box already there is left alone` |
| `-SetUpFor` | runs, arguments mean something else | `-SetUpFor` | ⚠️ Arguments changed | Pass the named mob's exact name, or nothing to auto-detect. A module phrase that is not the mob's name (e.g. 'Master' for The Djinn Master, 'reset') no longer matches - it logs "no encounter owns mob".<br>**Old:** `-SetUpFor <fw> <words after "Set up for">`<br>**New:** `-SetUpFor <fw> [<named mob name>] [<restart>]`<br>`restart` FALSE leaves a setup that is already running alone. |
| `-SpewStat` | runs, arguments mean something else | `-SpewStat` | ⚠️ Arguments changed | Write the type as its own flag: `-SpewStat <fw> -item Foo oc` instead of `-SpewStat <fw> item_Foo oc`.<br>**Old:** `-SpewStat <fw> <prefix_value> <where>`<br>**New:** `-SpewStat <fw> <-type> <value> <where>`<br>The old mashed form is still READ: an old type is mapped to its new one and `where` is taken from the old slot, so most old lines still work. deity_* tokens are dropped, and a token it cannot map errors loudly. |
| `-SpewStats` | runs, arguments mean something else | `-SpewStat` | ⚠️ Arguments changed | Write the type as its own flag: `-SpewStat <fw> -item Foo oc` instead of `-SpewStat <fw> item_Foo oc`.<br>**Old:** `-SpewStats <fw> <prefix_value> <where>`<br>**New:** `-SpewStats <fw> <-type> <value> <where>`<br>The old mashed form is still READ: an old type is mapped to its new one and `where` is taken from the old slot, so most old lines still work. deity_* tokens are dropped, and a token it cannot map errors loudly. |
| `-Unpack` | runs, arguments mean something else | `-Unpack` | ⚠️ Arguments changed | Write the reward choice as `-pick <choice>`: `-Unpack <fw> "<item>" -pick <number \| name \| lowest>`. A line with no choice needs no change.<br>**Old:** `-Unpack <fw> <item> <choice>`<br>**New:** `-Unpack <fw> <item> [-qty <N> \| -all] [-pick <number \| name \| lowest>]`<br>… |
| `-Walk` | runs, arguments mean something else | `-Walk` | ⚠️ Arguments changed | Nothing to retype; check the intent - V2 does what the name says.<br>**Old:** `-Walk <fw> - flipped the current mode (a -Walk sent to a box already walking made it run). New: -Walk <fw> - sets walk; a box already there is left alone` |
| `-ZoneDoor` | runs, arguments mean something else | `-ZoneDoor` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-ZoneDoor <dooroption>`<br>**New:** `-ZoneDoor <fw> <dooroption>`<br>`<dooroption>` defaults to 1. Classic's `-ZoneDoorForWho`, `-DoorForWho`, `-DoorXForWho` and `-ZoneDoorOptionForWho` (already for-who first) are now other names for this same command. |
| `-ZoneDoorOption` | runs, arguments mean something else | `-ZoneDoor` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-ZoneDoorOption <dooroption>`<br>**New:** `-ZoneDoorOption <fw> <dooroption>`<br>`<dooroption>` defaults to 1. Classic's `-ZoneDoorForWho`, `-DoorForWho`, `-DoorXForWho` and `-ZoneDoorOptionForWho` (already for-who first) are now other names for this same command. |

### ⚠️ Argument order changed (10)

#### ⚠️ Argument order changed: `-assist`

```
; before (Classic)
oc !ci -assist ${Me.Name} igw:${Me.Name}
; after (new bot)
oc !ci -assist igw:${Me.Name} ${Me.Name}
```

| You typed | Today | Type instead | What changed | Notes |
|---|---|---|---|---|
| `-ass` | runs, arguments in the wrong places | `-assist` | ⚠️ Argument order changed | Move the for-who to the first argument.<br>**Old:** `-ass <assistwho> <fw>`<br>**New:** `-ass <fw> <assistwho>` |
| `-assist` | runs, arguments in the wrong places | `-assist` | ⚠️ Argument order changed | Move the for-who to the first argument.<br>**Old:** `-assist <assistwho> <fw>`<br>**New:** `-assist <fw> <assistwho>` |
| `-Come2Me` | runs, arguments in the wrong places | `-Come2Me` | ⚠️ Argument order changed | Move the for-who to the first argument.<br>**Old:** `-Come2Me <moveto> <fw> <precision>`<br>**New:** `-Come2Me <fw> <moveto> <precision>` |
| `-ComeTome` | runs, arguments in the wrong places | `-Come2Me` | ⚠️ Argument order changed | Move the for-who to the first argument.<br>**Old:** `-ComeTome <moveto> <fw> <precision>`<br>**New:** `-ComeTome <fw> <moveto> <precision>` |
| `-LATL` | runs, arguments in the wrong places | `-LoadAutoTargetList` | ⚠️ Argument order changed | Move the for-who to the first argument.<br>**Old:** `-LATL <list> <fw>`<br>**New:** `-LATL <fw> <list>` |
| `-LoadAutoTargetList` | runs, arguments in the wrong places | `-LoadAutoTargetList` | ⚠️ Argument order changed | Move the for-who to the first argument.<br>**Old:** `-LoadAutoTargetList <list> <fw>`<br>**New:** `-LoadAutoTargetList <fw> <list>` |
| `-LoadAutoTargetListForWho` | runs, arguments in the wrong places | `-LoadAutoTargetList` | ⚠️ Argument order changed | Move the for-who to the first argument.<br>**Old:** `-LoadAutoTargetListForWho <list> <fw>`<br>**New:** `-LoadAutoTargetListForWho <fw> <list>` |
| `-LoadProfile` | runs, arguments in the wrong places | `-LoadProfile` | ⚠️ Argument order changed | Move the for-who to the first argument.<br>**Old:** `-LoadProfile <profilename> <fw>`<br>**New:** `-LoadProfile <fw> <profilename>` |
| `-Profile` | runs, arguments in the wrong places | `-LoadProfile` | ⚠️ Argument order changed | Move the for-who to the first argument.<br>**Old:** `-Profile <profilename> <fw>`<br>**New:** `-Profile <fw> <profilename>` |
| `-ProfileForWho` | runs, arguments in the wrong places | `-LoadProfile` | ⚠️ Argument order changed | Move the for-who to the first argument.<br>**Old:** `-ProfileForWho <profilename> <fw>`<br>**New:** `-ProfileForWho <fw> <profilename>` |

### ✏️ Renamed (13)

#### ✏️ Renamed: `-ApplyVerbForWho`

```
; before (Classic)
oc !ci -ApplyVerbForWho igw:${Me.Name} "boss_01_knight_light" "Touch"
; after (new bot)
oc !ci -ApplyVerb igw:${Me.Name} "boss_01_knight_light" "Touch"
```

| You typed | Today | Type instead | What changed | Notes |
|---|---|---|---|---|
| `-Apply_VerbForWho` | Unknown command | `-ApplyVerb` | ✏️ Renamed | The ForWho row is gone; write `-ApplyVerb` with the same arguments - the for-who stays first. An MCP button is converted for you. |
| `-ApplyVerbForWho` | Unknown command | `-ApplyVerb` | ✏️ Renamed | The ForWho row is gone; write `-ApplyVerb` with the same arguments - the for-who stays first. An MCP button is converted for you. |
| `-ApplyVerbIDForWho` | Unknown command | `-ApplyVerbID` | ✏️ Renamed | The ForWho row is gone; write `-ApplyVerbID` with the same arguments - the for-who stays first. An MCP button is converted for you. |
| `-ApplyVerbIDQueuedForWho` | Unknown command | `-ApplyVerbIDQueued` | ✏️ Renamed | The ForWho row is gone; write `-ApplyVerbIDQueued` with the same arguments - the for-who stays first. An MCP button is converted for you. |
| `-ApplyVerbQueuedForWho` | Unknown command | `-ApplyVerbQueued` | ✏️ Renamed | The ForWho row is gone; write `-ApplyVerbQueued` with the same arguments - the for-who stays first. An MCP button is converted for you. |
| `-OgreCraft_AddRecipesFromQuest` | Unknown command | `-OgreCraft_StartQuest` | ✏️ Renamed | Replace the verb name; the arguments are the same (`<fw>`).<br>It does MORE than V1: V1 only QUEUED the quest's recipes (with a 6/3 quantity guess); V2 is a flow that crafts the current quest's pending recipe steps, one of each per pass, until none is pending. The for-who now filters; V1 ran it on every session that heard the line. |
| `-Opt_Num` | Unknown command | `-ConversationBubble` | ✏️ Renamed | -Opt_Num was the same reply click as -ConversationBubble and is gone. Write `-ConversationBubble <fw> <num>`; V1 had no for-who, so put `auto` first (the For Who window).<br>**Old:** `-Opt_Num <num>`<br>**New:** `-ConversationBubble <fw> <num> (row -ConversationBubble)`<br>`<num>` defaults to 1. |
| `-OptNum` | Unknown command | `-ConversationBubble` | ✏️ Renamed | -Opt_Num was the same reply click as -ConversationBubble and is gone. Write `-ConversationBubble <fw> <num>`; V1 had no for-who, so put `auto` first (the For Who window).<br>**Old:** `-OptNum <num>`<br>**New:** `-ConversationBubble <fw> <num> (row -ConversationBubble)`<br>`<num>` defaults to 1. |
| `-PoP_TempAdorns` | Unknown command | `-TempAdorns` | ✏️ Renamed | Write `-TempAdorns` with the same arguments: `-TempAdorns <fw> cboc` (or pot / hp, or a profile you saved). Name the profile - the old default cboc is not assumed. An MCP button is converted for you.<br>**Old:** `-PoP_TempAdorns <fw> <cboc\|pot\|hp> <overwrite>`<br>**New:** `-TempAdorns <fw> <profile> <overwrite> - cboc / pot / hp are the ready-made profiles CBOC / Pot / HP (the old hardcoded lists)` |
| `-Set_VampiricRequiem_Cancelling_Active` | Unknown command | `-CancelOnCast` | ✏️ Renamed | Write `-CancelOnCast <fw> <ability>` naming the trigger ability (for the old verb: Vampiric Requiem), and configure what it cancels in the Cancel On Cast tab.<br>The V1 wait-N-seconds delay is dropped. |
| `-Unpack_EmpyralStones` | Unknown command | `-Unpack` | ✏️ Renamed | Use `-Unpack <fw> "Empyral Stones" -all -pick lowest` (or `-pick "<stone name>"` for one kind).<br>**Old:** `-Unpack_EmpyralStones <fw> [Lowest \| <stone name>]`<br>**New:** `-Unpack <fw> "Empyral Stones" -all -pick lowest` |
| `-Unpack_PlanarStones` | Unknown command | `-Unpack` | ✏️ Renamed | Use `-Unpack <fw> "Planar Stones" -all -pick lowest` (or `-pick "<stone name>"` for one kind).<br>**Old:** `-Unpack_PlanarStones <fw> [Lowest \| <stone name>]`<br>**New:** `-Unpack <fw> "Planar Stones" -all -pick lowest` |
| `-Unpack_Quantity` | Unknown command | `-Unpack` | ✏️ Renamed | Use `-Unpack <fw> "<item>" -qty <N>` (add `-pick <choice>` when the window offers a choice). Name the item - the old "examine" default (the item in the open examine window) is gone.<br>**Old:** `-Unpack_Quantity <fw> <item> <N> <choice>`<br>**New:** `-Unpack <fw> <item> -qty <N> -pick <choice>` |

### ➡️ Lives somewhere else (1)

| You typed | Today | Type instead | What changed | Notes |
|---|---|---|---|---|
| `-Ask` | Unknown command | `OgreBotAPI.Comms.GroupQuery` | ➡️ Lives somewhere else | IC file: the `groupQuery` step - counts, allYes / anyYes / allNo / anyNo, per-member flags, raw answers, ready-made for-who lists. Script: the same engine - ${OgreBotAPI.Comms.GroupQuery[&lt;fw&gt;, -question, &lt;question&gt;, ...]} starts it and reads as its id; then ${OgreBotAPI.Comms.GroupQuery.Done[id]} / .Result[id] (JSON, the same names), or the event OgreEvent_GroupQueryDone(id, json). |

### 📄 In a data file now (18)

**Note A** (9 rows below): Nothing to type: the fight is coded in the zone's encounter file. An encounter author emits a cross-session signal with `broadcast` and receives it with a trigger `on: <event>`. A hand or button sender uses `-ExecuteEvent_AP <fw> <event> <args>` while that zone's encounter is loaded.

| You typed | Today | Type instead | What changed | Notes |
|---|---|---|---|---|
| `-GOAotA1` | Unknown command | `broadcast` | 📄 In a data file now | Note A |
| `-ROAOMCG` | Unknown command | `broadcast` | 📄 In a data file now | Note A |
| `-ROASEC` | Unknown command | `broadcast` | 📄 In a data file now | Note A |
| `-ROBSBFC` | Unknown command | `broadcast` | 📄 In a data file now | Note A |
| `-RODMPI` | Unknown command | `broadcast` | 📄 In a data file now | Nothing to type: the fight is coded in the zone's encounter file. An encounter author emits a cross-session signal with `broadcast` and receives it with a trigger `on: <event>`. A hand or button sender uses `-ExecuteEvent_AP <fw> <event> <args>` while that zone's encounter is loaded. Button form: `-ExecuteEvent_AP <fw> DjinnMaster_PlayInstruments <toon> <order>`. |
| `-RODMPS` | Unknown command | `campSpot` | 📄 In a data file now | Nothing to type: the portal handling is in the encounter file for The Djinn Master in The Fabled Djinn Master's Prism - spawn triggers + `campSpot`. |
| `-RODrinalDispell` | Unknown command | `broadcast` | 📄 In a data file now | Note A |
| `-RODrinalPos` | Unknown command | `campSpot` | 📄 In a data file now | Tank positioning for Drinal is in the Harrow's End [Raid] encounter file for Drinal. |
| `-ROKoolbhCloudOfVile` | Unknown command | `broadcast` | 📄 In a data file now | Note A |
| `-ROKraletusCureCalled` | Unknown command | `broadcast` | 📄 In a data file now | Note A |
| `-ROOSSSAC` | Unknown command | `broadcast` | 📄 In a data file now | Note A |
| `-ROPC` | Unknown command | `castAbility` | 📄 In a data file now | Nothing to type for the Council: it is coded. A new pre-cure is authored in that fight's encounter file.<br>The Mutagenic Outcast file also names -ROPC in its `_status` (the raid leader's precure); that site was not re-checked here. |
| `-ROSGDDispell` | Unknown command | `dispel` | 📄 In a data file now | Nothing to type: the dispel is coded in the Siren's Grotto - Dissension [Raid] encounter file for Diviner Gelerin. |
| `-ROSGPRDispell` | Unknown command | `dispel` | 📄 In a data file now | Nothing to type: the dispel is coded in the Siren's Grotto - Dissension [Raid] encounter file for Diviner Gelerin. |
| `-ROSGPRTCS` | Unknown command | `broadcast` | 📄 In a data file now | Nothing to type: the fight is coded in the zone's encounter file. An encounter author emits a cross-session signal with `broadcast` and receives it with a trigger `on: <event>`. A hand or button sender uses `-ExecuteEvent_AP <fw> <event> <args>` while that zone's encounter is loaded. Here the sender is the operator: `-ExecuteEvent_AP <fw> SGPsyllon_TankSpot`. |
| `-ROSGTDispell` | Unknown command | `dispel` | 📄 In a data file now | Nothing to type: the dispel is coded in the Siren's Grotto - Dissension [Raid] encounter file for Overlord Talan. |
| `-ROSGTFDispell` | Unknown command | `dispel` | 📄 In a data file now | Nothing to type: the dispel is coded in the Siren's Grotto - Dissension [Raid] encounter file for Overlord Talan. |
| `-ROTOVI` | Unknown command | `broadcast` | 📄 In a data file now | Note A |

### ⛔ Removed (38)

| You typed | Today | Type instead | What changed | Notes |
|---|---|---|---|---|
| `-Aliases_ShowAllBuiltInAliases` | Unknown command | — | ⛔ Removed | Classic's set whether its alias list also showed the built-in aliases - a display option in its own window. The new bot has no such list; delete the line. |
| `-AscensionEmbargo_Add_DoNotCombo` | Unknown command | — | ⛔ Removed | Classic's added an entry to the ascension do-not-combo list. Ascension combos are not in the new bot; delete the line. |
| `-AscensionEmbargo_Change_Disable_Status` | Unknown command | — | ⛔ Removed | Classic's changed whether an entry of the ascension do-not-combo list was disabled. Ascension combos are not in the new bot; delete the line. |
| `-AscensionEmbargo_Remove_DoNotCombo` | Unknown command | — | ⛔ Removed | Classic's removed an entry from the ascension do-not-combo list. Ascension combos are not in the new bot; delete the line. |
| `-cfw` | as the first thing on a line (`-cfw <who> -Verb ...`): works, for that line only. On a line by itself: does nothing - the lasting default it set is gone | — | ⛔ Removed | As the FIRST thing after `oc !c` / `oc !ci` (`oc !ci -cfw igw:${Me.Name} -letsgo`) it still works: the new console reads it as that one line's for-who, and the verb's empty for-who takes it (the tool skips that form). Only `-cfw <who>` on a line by itself is gone - it set a lasting default for later lines. Put the for-who on each of those later verbs instead (it is argument 1).<br>Classic's `-cfw <who>` on a line by itself set a lasting default: every later `auto` for-who used it. |
| `-ChangeRadarYAxis` | Unknown command | — | ⛔ Removed | Classic's toggled the radar's Y axis. Delete the line - the new bot has nothing in its place. |
| `-ConsumeDeityBaubles` | Unknown command | — | ⛔ Removed | Classic's did nothing: its one line, the call to Obj_Deity.ConsumeDeityBaubles, is commented out. Nothing replaces it; delete the line. |
| `-cs-jo` | Unknown command | — | ⛔ Removed | Write the two steps it did: `-campspot <who> <min> <max>` then `-joustoff <joustoff>` (Classic: -cs-jo &lt;who&gt; &lt;joustoff&gt; &lt;min&gt; &lt;max&gt;; defaults auto, auto+casters, 2, 200). An MCP button is split for you.<br>**Old:** `-cs-jo <fw> <joustoff> <min> <max>`<br>**New:** `-campspot <fw> <min> <max> -joustoff <joustoff>` |
| `-cs-jo-ji` | Unknown command | — | ⛔ Removed | Write the three steps it did: `-campspot <who> <min> <max>`, `-joustoff <joustoff>`, `-joustin <joustin>` (Classic: -cs-jo-ji &lt;who&gt; &lt;joustoff&gt; &lt;min&gt; &lt;max&gt; &lt;joustin&gt;; defaults auto, auto+casters, 2, 200, auto). An MCP button is split for you.<br>**Old:** `-cs-jo-ji <fw> <joustoff> <min> <max> <joustin>`<br>**New:** `-campspot <fw> <min> <max> -joustoff <joustoff> -joustin <joustin>` |
| `-cs-set-cs-jo-ji-opt` | Unknown command | — | ⛔ Removed | Write the three steps it did: `-campspot <who> <min> <max>`, `-joustoff <joustoff>`, `-joustin <joustin>` (Classic: -cs-set-cs-jo-ji-opt &lt;who&gt; &lt;joustoff&gt; &lt;min&gt; &lt;max&gt; &lt;joustin&gt;, the same as -cs-jo-ji; defaults auto, auto+casters, 2, 200, auto). An MCP button is split for you.<br>**Old:** `-cs-set-cs-jo-ji-opt <fw> <joustoff> <min> <max> <joustin>`<br>**New:** `-campspot <fw> <min> <max> -joustoff <joustoff> -joustin <joustin>` |
| `-Deity_Spend` | Unknown command | — | ⛔ Removed | Classic's was meant to spend deity points, but its only working line is commented out, so it did nothing on Classic either. Delete the line. |
| `-DeitySpend` | Unknown command | — | ⛔ Removed | Classic's was meant to spend deity points, but its only working line is commented out, so it did nothing on Classic either. Delete the line. |
| `-DevBot` | Unknown command | — | ⛔ Removed | Classic's started the developer copy of the bot (`ogre dev`). The new bot has no developer copy; delete the line. |
| `-Fix_Broken_Shit` | Unknown command | — | ⛔ Removed | Run the parts it bundled: `ogre end console` / `ogre console` / `ogre end irc` / `ogre irc`.<br>Classic's restarted the console and IRC in one go. |
| `-GuidedAscension` | Unknown command | — | ⛔ Removed | Classic's used the 'Guided Ascension' item when ascension vitality was below a threshold. Delete the line - the new bot has nothing in its place. |
| `-HQEar` | Unknown command | — | ⛔ Removed | Classic's cast the HQ ear. The HQ Ear feature is not in the new bot; delete the line. |
| `-HQEar_Recheck` | Unknown command | — | ⛔ Removed | Classic's rechecked the HQ ear. The HQ Ear feature is not in the new bot; delete the line. |
| `-HQEar_ReEquipOriginalEar` | Unknown command | — | ⛔ Removed | Classic's re-equipped the original ear. The HQ Ear feature is not in the new bot; delete the line. |
| `-HQEar_ReportStuckEar` | Unknown command | — | ⛔ Removed | Classic's reported a stuck HQ ear. The HQ Ear feature is not in the new bot; delete the line. |
| `-Mount` | Unknown command | — | ⛔ Removed | Use `-Force_MountOn <fw>` or `-Force_MountOff <fw>`.<br>Classic's was a toggle - one `/summon_mount`, so it mounted you or took you off the mount. |
| `-OgreACommandOB_AP` | Unknown command | — | ⛔ Removed | Not the same verb as -OgreCommandOB_AP (`ogre <cmd>`), which is live. |
| `-Reload_DevBot` | Unknown command | — | ⛔ Removed | Classic's reloaded the developer copy of the bot (`ogre dev`). The new bot has no developer copy; delete the line. |
| `-ReloadOgreConsole` | Unknown command | — | ⛔ Removed | Close and reopen the panel: `ogre end console`, then `ogre console`.<br>Classic's was meant to close and reopen the console, but a typo stopped the close half from ever running. |
| `-Report_Back` | Unknown command | — | ⛔ Removed | Ask with groupQuery instead - the IC step `groupQuery`, or from a script ${OgreBotAPI.Comms.GroupQuery[&lt;fw&gt;, -question, ...]}: -item -&gt; question `itemCount`; -ScriptRunning and -CommandForMe -&gt; a LavishScript[...] question; -resolve_of_slot -&gt; loot distribution's own `lootBid`.<br>Classic callers: the instance helpers' EveryoneHaveItem, the loot resolve auction, now loot distribution's `lootBid`, and OgreAutoQuest with its nav scripts, not ported. |
| `-ReportForList_IRC` | Unknown command | — | ⛔ Removed | Classic's was an IRC roll call - who answered (that is, who is actually running the bot), ordered by actor id - with one user, Trakanon's Toxic Life rotation. The roll call is not in the new bot; delete the line. |
| `-Reporting` | Unknown command | — | ⛔ Removed | Any replacement has to answer "who is actually going to act", not "who is in my group". |
| `-ResolveBuffCheck` | Unknown command | — | ⛔ Removed | V1 sits inside a /* Need to remove this */ block, so V1 itself already answered "Unknown command"; its method Command_ResolveBuffCheck called OgreBotAPI:ResolveBuffCheck. |
| `-RODFCJ` | Unknown command | — | ⛔ Removed | No encounter verb replaces it. |
| `-RODMIR` | Unknown command | — | ⛔ Removed | Classic's ran the instrument item runner in The Fabled Djinn Master's Prism, placing each instrument by clicking the centre of the screen. The fight's encounter file does not do that part; delete the line. |
| `-RODTFP` | Unknown command | — | ⛔ Removed | Removed on purpose. The Fitzpitzle countdown belongs in its encounter file, which waits for the two spells' ability ids.<br>Classic's showed an on-screen countdown for Fitzpitzle's AE in the Deathtoll raid, read off the target's cast bar by name; the raid script sent it. |
| `-RoR_Epic_ChangeInCastStack` | Unknown command | — | ⛔ Removed | Classic's turned the RoR epic abilities on or off in the cast stack. Delete the line - the new bot has nothing in its place. |
| `-RunWalk` | Unknown command | — | ⛔ Removed | Use `-Run <fw>` or `-Walk <fw>`, which SET the mode through OgreBotAPI.Movement:SetRunMode and never flip. Decide which one the old line meant.<br>-Run and -Walk keep their V1 spelling but no longer toggle - see their own entries. |
| `-SetQuestion` | Unknown command | — | ⛔ Removed | The effect is one option write: `-ChangeOgreBotUIOption <fw> checkbox_loot_donotlootshinies <TRUE\|FALSE>`. Note the polarity: SetQuestion TRUE set do-NOT-loot-shinies TRUE.<br>Classic's did only that: its one live line wrote the option (`ChangeOgreBotUIOption[fw, checkbox_loot_donotlootshinies, value]`) and returned. |
| `-Test` | Unknown command | — | ⛔ Removed | Classic's ran your own test script (`timedcommand 0 run test`). Delete the line - the new bot has nothing in its place. |
| `-test1` | Unknown command | — | ⛔ Removed | Classic's was a test command: it read a for-who, two arguments and the rest of the line, and only echoed them. Delete the line. |
| `-test2` | Unknown command | — | ⛔ Removed | Classic's was the twin of -test1 (echo only). Delete the line. |
| `-Update_Turbo` | Unknown command | — | ⛔ Removed | Classic's changed LavishScript's turbo setting. That is a LavishScript setting, not the bot's; delete the line. |
| `-VampiricRequiem_AbilityCancel` | Unknown command | — | ⛔ Removed | The generic version is the Cancel On Cast tab: it cancels when the configured trigger is cast; to trigger it by hand use `-CancelOnCast <fw> <ability>`.<br>Classic's cancelled Vampiric Requiem by hand, through its own Vampiric Requiem handler. |

## 2. Every other command, A to Z

These 435 commands are typed exactly as in Classic. An alias is another name for a command; it keeps working.

| You typed | Notes |
|---|---|
| `-AbilityEmbargo_ResetAbilityEmbargo` |  |
| `-AbilityEmbargo_ResetAllAbilityEmbargos` |  |
| `-AbilityTag` | An alias of `-AbilityTagEmbargo` - it works as typed. |
| `-AbilityTag_ResetAbilityTagAllow` |  |
| `-AbilityTag_ResetAbilityTagEmbargo` |  |
| `-AbilityTag_ResetAllAbilityTagAllows` |  |
| `-AbilityTag_ResetAllAbilityTagEmbargos` |  |
| `-AbilityTagEmbargo` |  |
| `-AbilityTagRotate` | An alias of `-AbilityTagEmbargo` - it works as typed. |
| `-AbilityTracker_Add` |  |
| `-AcceptQuest` |  |
| `-AcceptReward` |  |
| `-Actor_Click` |  |
| `-Actor_ClickQueued` |  |
| `-AddNoOffensiveOn` |  |
| `-AIIR` | An alias of `-AuthIfInRaid` - it works as typed. |
| `-Alias_AddEntry` |  |
| `-Alias_ChangeEntry` | An alias of `-Alias_ChangeEntryFor` - it works as typed. |
| `-Alias_ChangeEntryAlias` |  |
| `-Alias_ChangeEntryFor` |  |
| `-Alias_RemoveEntry` |  |
| `-AltarOfTheAncients` |  |
| `-ArcannaseEffigyOfRebirth` |  |
| `-AReward` | An alias of `-AcceptReward` - it works as typed. |
| `-AssistForWho` |  |
| `-AT_Add` | An alias of `-AutoTarget_AddActor` - it works as typed. |
| `-AT_Clear` | An alias of `-AutoTarget_ClearActors` - it works as typed. |
| `-AT_Disable` | An alias of `-AutoTarget_Disable` - it works as typed. |
| `-AT_Enable` | An alias of `-AutoTarget_Enable` - it works as typed. |
| `-AT_Height` | An alias of `-AutoTarget_SetScanHeight` - it works as typed. |
| `-AT_Rescan` | An alias of `-AutoTarget_SetRescanTime` - it works as typed. |
| `-AT_Scan` | An alias of `-AutoTarget_SetScanRadius` - it works as typed. |
| `-ATOCST` | An alias of `-AutoTargetOCSToggle` - it works as typed. |
| `-ATT` | An alias of `-AutoTargetToggle` - it works as typed. |
| `-Auth` |  |
| `-AuthIfInRaid` |  |
| `-authlist` |  |
| `-AutoConsumeTemporaryFamiliarExperience` |  |
| `-AutoConsumeTemporaryMountTrainingReduction` |  |
| `-AutoConsumeTemporaryResearchReduction` |  |
| `-AutoCure` |  |
| `-AutoCurse` |  |
| `-AutoGroupCure` |  |
| `-AutoRun` |  |
| `-AutoTarget_AddActor` |  |
| `-AutoTarget_Clear` |  |
| `-AutoTarget_ClearActors` |  |
| `-AutoTarget_Disable` |  |
| `-AutoTarget_Enable` |  |
| `-AutoTarget_SetRescanTime` |  |
| `-AutoTarget_SetScanHeight` |  |
| `-AutoTarget_SetScanRadius` |  |
| `-AutoTargetOCSToggle` |  |
| `-AutoTargetToggle` |  |
| `-BuyFromMerchant` |  |
| `-CallGH` |  |
| `-CallToGH` | An alias of `-CallGH` - it works as typed. |
| `-Camp` | An alias of `-CampToDesktop` - it works as typed. |
| `-campspot` |  |
| `-CampToDesktop` |  |
| `-Cancel_Casting` | An alias of `-CancelCasting` - it works as typed. |
| `-Cancel_MaintainedForWho` | An alias of `-CancelMaintained` - it works as typed. |
| `-cancelcast` | An alias of `-CastAbility` - it works as typed. |
| `-CancelCasting` |  |
| `-cancelcastnoexport` |  |
| `-cancelcaston` | An alias of `-CastAbilityOnPlayer` - it works as typed. |
| `-CancelDetrimental` |  |
| `-CancelGroupWaterBreathing` |  |
| `-CancelMaintainedForWho` | An alias of `-CancelMaintained` - it works as typed. |
| `-cast` | An alias of `-CastAbility` - it works as typed. |
| `-cast_ability` | An alias of `-CastAbility` - it works as typed. |
| `-cast_ability_on_player` | An alias of `-CastAbilityOnPlayer` - it works as typed. |
| `-cast_abilitynoexport` | An alias of `-cancelcastnoexport` - it works as typed. |
| `-Cast_Interrupt` |  |
| `-CastAbility` |  |
| `-CastAbilityInSeconds` |  |
| `-CastAbilityNoChecks` |  |
| `-CastAbilitynoexport` | An alias of `-cancelcastnoexport` - it works as typed. |
| `-CastAbilityOnNPC` |  |
| `-CastAbilityOnPlayer` |  |
| `-CastAbilityOnPlayerInSeconds` |  |
| `-CastAbilityOnPlayerNoChecks` |  |
| `-CastBulwarkImmediately` |  |
| `-CastGroupWaterBreathing` |  |
| `-CastHOIconID` |  |
| `-CastInterrupt` | An alias of `-Cast_Interrupt` - it works as typed. |
| `-castnoexport` | An alias of `-cancelcastnoexport` - it works as typed. |
| `-caston` | An alias of `-CastAbilityOnPlayer` - it works as typed. |
| `-castonmob` | An alias of `-CastAbilityOnNPC` - it works as typed. |
| `-castonnpc` | An alias of `-CastAbilityOnNPC` - it works as typed. |
| `-CastRescue_AP` |  |
| `-ccaston` | An alias of `-CastAbilityOnPlayer` - it works as typed. |
| `-CCastStack` | An alias of `-ChangeCastStackListBoxItem` - it works as typed. |
| `-CCastStackByTag` | An alias of `-ChangeCastStackListBoxItemByTag` - it works as typed. |
| `-ccsb` | An alias of `-CS_Set_ChangeCampSpotBy` - it works as typed. |
| `-ccsbfw` | An alias of `-CS_Set_ChangeCampSpotBy` - it works as typed. |
| `-ccsbw` | An alias of `-CS_Set_ChangeCampSpotBy` - it works as typed. |
| `-ccsbyforwho` | An alias of `-CS_Set_ChangeCampSpotBy` - it works as typed. |
| `-ccsfw` | An alias of `-ChangeCampSpot` - it works as typed. |
| `-ccst` | An alias of `-CastAbility` - it works as typed. |
| `-CCStack` | An alias of `-ChangeCastStackListBoxItem` - it works as typed. |
| `-CCStackByTag` | An alias of `-ChangeCastStackListBoxItemByTag` - it works as typed. |
| `-ccstnoexport` | An alias of `-cancelcastnoexport` - it works as typed. |
| `-ccsw` | An alias of `-ChangeCampSpot` - it works as typed. |
| `-Champions_Zone_Resetter` |  |
| `-Change_Campspot_Who` | An alias of `-ChangeCampSpot` - it works as typed. |
| `-ChangeBeltAdorn` | Nothing to change - unless the line passes a fourth argument (skip moving adornments): drop it. The old rune is always moved back to the bag slot the new one came from.<br>**Old:** `-ChangeBeltAdorn <fw> <value> [unequip] [skipadornmoving]`<br>**New:** `-ChangeBeltAdorn <fw> <value> [unequip]` |
| `-ChangeCampSpotBy` | An alias of `-CS_Set_ChangeCampSpotBy` - it works as typed. |
| `-ChangeCampSpotWho` | An alias of `-ChangeCampSpot` - it works as typed. |
| `-ChangeCastStack` | An alias of `-ChangeCastStackListBoxItem` - it works as typed. |
| `-ChangeCastStackByTag` | An alias of `-ChangeCastStackListBoxItemByTag` - it works as typed. |
| `-ChangeCastStackListBoxItem` |  |
| `-ChangeCastStackListBoxItemByTag` |  |
| `-ChangeLootOptions` |  |
| `-ChangeOgreBotUIOption` |  |
| `-ChangeZoneTo` |  |
| `-CheckGear` |  |
| `-CheckKunarkAscendingRequirements` |  |
| `-CheckMercenaryTraining` |  |
| `-CheckMountTraining` |  |
| `-CheckResearch` |  |
| `-CheckVersion` |  |
| `-ChoiceWindow` |  |
| `-ClassInfo_ChangeValue` |  |
| `-Clear_Allow_HOICon` |  |
| `-Clear_Allow_HOICons` |  |
| `-Clear_Disable_HOICon` |  |
| `-Clear_Disable_HOICons` |  |
| `-clear_Internalvariable` |  |
| `-clear_Internalvariables` |  |
| `-clear_variable` |  |
| `-clear_variables` |  |
| `-ClearNoOffensiveOn` |  |
| `-CloseExamineWindow` |  |
| `-CloseWindow` |  |
| `-ClsWdn` | An alias of `-CloseWindow` - it works as typed. |
| `-Consume_Familiars` |  |
| `-Consume_Status_Ignots` | An alias of `-Consume_Status_Ingots` - it works as typed. |
| `-Consume_Status_Ingots` |  |
| `-Consume_Status_Tokens` |  |
| `-ConsumeItems_ProcessList_AP` |  |
| `-ConsumeKrono` | An alias of `-RedeemKrono` - it works as typed. |
| `-Conversation_Bubble` | An alias of `-ConversationBubble` - it works as typed. |
| `-ConversationBubble` |  |
| `-countdown` |  |
| `-CoV` |  |
| `-Crouch` |  |
| `-cs` | An alias of `-campspot` - it works as typed. |
| `-cs-circle` | An alias of `-CS_Set_Formation_Circle` - it works as typed. |
| `-cs-monkey` | An alias of `-CS_Set_Formation_MonkeyInMiddle` - it works as typed. |
| `-cs-monkeyRaid` | An alias of `-CS_Set_Formation_MonkeyInMiddleRaid` - it works as typed. |
| `-cs-set-ccs-by` | An alias of `-CS_Set_ChangeCampSpotBy` - it works as typed. |
| `-cs-set-cs` | An alias of `-campspot` - it works as typed. |
| `-CS_ClearAll` |  |
| `-CS_ClearCampSpot` |  |
| `-CS_ClearRelative` |  |
| `-CS_Set_ChangeCampSpot` |  |
| `-CS_Set_ChangeCampSpotBy` |  |
| `-CS_Set_ChangeRelativeCampSpotBy` |  |
| `-CS_Set_Formation_Circle` |  |
| `-CS_Set_Formation_MonkeyInMiddle` |  |
| `-CS_Set_Formation_MonkeyInMiddleRaid` |  |
| `-CS_Set_HowClose` |  |
| `-CS_Set_HowFar` |  |
| `-CS_Set_Relative` |  |
| `-CurePotions_Replenish` |  |
| `-DeleteQuest` |  |
| `-DestroyItem` |  |
| `-DestroyItem_NoChecks` |  |
| `-Disable_Dispells` |  |
| `-Disable_Interrupts` |  |
| `-Disband` |  |
| `-Dispell` |  |
| `-DispellNPCWithAny` |  |
| `-DispellNPCWithItem` |  |
| `-DispellNPCWithSpell` |  |
| `-DisplayEtherealMissionInfo` |  |
| `-DoHO_Reset` |  |
| `-DoHO_Set_Enable` |  |
| `-DoHO_Setup` |  |
| `-DoNotMove` |  |
| `-DoorForWho` | An alias of `-ZoneDoor` - it works as typed. |
| `-DoorXForWho` | An alias of `-ZoneDoor` - it works as typed. |
| `-DoVDebuff` |  |
| `-DoVDebuff_Half` |  |
| `-Drink_Alcohol` |  |
| `-DungeonMaker_Cancel` | An alias of `-DungeonMakerCancel` - it works as typed. |
| `-DungeonMakerCancel` |  |
| `-Enable_Dispells` |  |
| `-Enable_Interrupts` |  |
| `-End_Bot` |  |
| `-endargs` |  |
| `-EndBot` | An alias of `-End_Bot` - it works as typed. |
| `-EndScriptOB` |  |
| `-EndScriptRequiresOgreBot` | An alias of `-EndScriptOB` - it works as typed. |
| `-EquipCharm` |  |
| `-esob` | An alias of `-EndScriptOB` - it works as typed. |
| `-evac` |  |
| `-ExamineAllOfItem` |  |
| `-ExamineInventoryItem` |  |
| `-ExecuteEvent_AP` |  |
| `-ExecuteEvent_JSON_AP` |  |
| `-ExitClient` |  |
| `-F2PWindow_Check` |  |
| `-F2PWindow_SetOptions` |  |
| `-FaceActor` |  |
| `-FaceAngle` |  |
| `-FaceLoc` |  |
| `-FastTravel` |  |
| `-ffollow` | An alias of `-forcefollow` - it works as typed. |
| `-FlagToon` |  |
| `-FlyDown` |  |
| `-FlyDownForWho` | An alias of `-FlyDown` - it works as typed. |
| `-FlyStop` |  |
| `-FlyStopForWho` | An alias of `-FlyStop` - it works as typed. |
| `-FlyUp` |  |
| `-FlyUpForWho` | An alias of `-FlyUp` - it works as typed. |
| `-FoodDrink_AutoConsume` |  |
| `-FoodDrink_Replenish` |  |
| `-Force_MountOn` |  |
| `-ForceAliasUpdate` |  |
| `-forcefollow` |  |
| `-FullRebuff` | An alias of `-Rebuff` - it works as typed. |
| `-Gear` | An alias of `-CheckGear` - it works as typed. |
| `-GetFlag` |  |
| `-GetToConcentration` |  |
| `-GetToGH` |  |
| `-GroupCure` |  |
| `-Hail` |  |
| `-HailNPC` | An alias of `-Hail` - it works as typed. |
| `-Heartstone_RekindleBond` |  |
| `-HO_Advance` | An alias of `-HO_Wheel_Advance` - it works as typed. |
| `-HO_Cancel_Starter` |  |
| `-HO_Start` |  |
| `-HO_Starter` | An alias of `-HO_Starter_Advance` - it works as typed. |
| `-HO_Starter_Advance` |  |
| `-HO_Wheel_Advance` |  |
| `-holdup` |  |
| `-InjectChat` |  |
| `-InputTextWindow_Accept` |  |
| `-InputTextWindow_AddText` |  |
| `-InputTextWindow_ClearText` |  |
| `-Invite` |  |
| `-joust-in` | An alias of `-joustin` - it works as typed. |
| `-joust-off` | An alias of `-joustoff` - it works as typed. |
| `-joust-on` | An alias of `-jouston` - it works as typed. |
| `-joust-out` | An alias of `-joustout` - it works as typed. |
| `-joustin` |  |
| `-joustoff` |  |
| `-jouston` |  |
| `-joustout` |  |
| `-jst-in` | An alias of `-joustin` - it works as typed. |
| `-jst-off` | An alias of `-joustoff` - it works as typed. |
| `-jst-on` | An alias of `-jouston` - it works as typed. |
| `-jst-out` | An alias of `-joustout` - it works as typed. |
| `-Jump` |  |
| `-KillSession` |  |
| `-Krono` | An alias of `-RedeemKrono` - it works as typed. |
| `-LandFlyingMount` |  |
| `-LaunchAutoLogin` |  |
| `-letsgo` |  |
| `-List_AutoLoginProfiles` |  |
| `-List_Sessions` |  |
| `-LoadBot` |  |
| `-LoadCharacter` |  |
| `-LoginAtCharacterSelect` |  |
| `-LogToonIn` |  |
| `-LootAll` |  |
| `-Main` | An alias of `-ToggleMainWindow` - it works as typed. |
| `-MakeLeader` |  |
| `-MarkToon` |  |
| `-Mercenary_AddMercenaries` |  |
| `-NoMove` | An alias of `-DoNotMove` - it works as typed. |
| `-NoTarget` |  |
| `-ofol` | An alias of `-ogrefollow` - it works as typed. |
| `-ofol++` | An alias of `-OFolIncDistance` - it works as typed. |
| `-ofol-++` | An alias of `-OFolIncDistance` - it works as typed. |
| `-ofol--` | An alias of `-ofol---` - it works as typed. |
| `-ofol---` |  |
| `-OFolDecDistance` | An alias of `-ofol---` - it works as typed. |
| `-OFolIncDistance` |  |
| `-ofollow` | An alias of `-ogrefollow` - it works as typed. |
| `-OgreBotToggleConsoleWindow` |  |
| `-OgreCommandOB_AP` |  |
| `-OgreConsole_ShowRequiresOgreBot` |  |
| `-OgreCraft_AddLastScribedRecipe` |  |
| `-OgreCraft_AddRecipe` |  |
| `-OgreCraft_CraftQueue` |  |
| `-OgreCraft_ScribeRecipe` |  |
| `-ogrefollow` |  |
| `-OgreZoneForceReset` |  |
| `-OK_Button` |  |
| `-OnScreenTimer` | An alias of `-Timer` - it works as typed. |
| `-OpenAndBuyFromMerchant` |  |
| `-OpenAndBuyFromMerchantXTimes` |  |
| `-OSExecute` |  |
| `-Overseer_AddAgentsToCollection` |  |
| `-Overseer_AutoAddOverseerQuests` |  |
| `-Overseer_CheckQuests` |  |
| `-PackPony` |  |
| `-pause` |  |
| `-pet-attack` | An alias of `-petattack` - it works as typed. |
| `-pet-off` | An alias of `-PetOff` - it works as typed. |
| `-pet-on` | An alias of `-petattack` - it works as typed. |
| `-pet_attack` | An alias of `-petattack` - it works as typed. |
| `-pet_off` | An alias of `-PetOff` - it works as typed. |
| `-pet_on` | An alias of `-petattack` - it works as typed. |
| `-PetAssist` |  |
| `-petattack` |  |
| `-PetGetLost` |  |
| `-PetOff` |  |
| `-PetOn` | An alias of `-petattack` - it works as typed. |
| `-PortalToGuildHall` |  |
| `-ProvingGrounds_Exit` |  |
| `-ProvingGrounds_Scoreboard_Close` |  |
| `-Pull` |  |
| `-Pushover` |  |
| `-Question` |  |
| `-RaidInvite` |  |
| `-RawCommandOB_AP` |  |
| `-RawCommandRequiresOgreBot_AllParams` | An alias of `-RawCommandOB_AP` - it works as typed. |
| `-Rebuff` |  |
| `-RedeemKrono` |  |
| `-RelayGroups_Spew` | An alias of `-Spew_RelayGroup` - it works as typed. |
| `-Reload_Bot` |  |
| `-ReloadBot` | An alias of `-Reload_Bot` - it works as typed. |
| `-ReloadOgreIRC` |  |
| `-RemoveNoOffensiveOn` |  |
| `-Repair` | An alias of `-RepairGear` - it works as typed. |
| `-RepairGear` |  |
| `-ReplyDialog` |  |
| `-ReplyDialogClose` |  |
| `-Res` |  |
| `-Research_Material_Check` |  |
| `-ResetActorsLooted` |  |
| `-resetauth` |  |
| `-ResetCameraAngle` |  |
| `-ResetZone` |  |
| `-resetzoneall` | An alias of `-ZoneResetAll` - it works as typed. |
| `-Resource` |  |
| `-ResStone` |  |
| `-resume` |  |
| `-Revive` |  |
| `-rsob` | An alias of `-RunScriptOB` - it works as typed. |
| `-RunScriptOB` |  |
| `-RunScriptOB_AP` |  |
| `-RunScriptRequiresOgreBot` | An alias of `-RunScriptOB` - it works as typed. |
| `-Scribe_Empyral` |  |
| `-ScrollOf` |  |
| `-Select_Window_AP` |  |
| `-Select_Window_Spew_AP` |  |
| `-Select_Zone_Version` |  |
| `-SellToMerchant` |  |
| `-Set_Allow_HOICon` |  |
| `-Set_CameraPitch` |  |
| `-Set_CampSpotJump_Handle` |  |
| `-Set_Disable_HOICon` |  |
| `-Set_DisableAllAOEs_AllParams` |  |
| `-set_Internalvariable` |  |
| `-set_variable` |  |
| `-SetAutoLootMode` |  |
| `-SetCameraPitch` | An alias of `-Set_CameraPitch` - it works as typed. |
| `-SetCS_BehindNPC` |  |
| `-SetCS_InFrontNPC` |  |
| `-SetCS_NPC` |  |
| `-SetCS_PositionNPC` |  |
| `-SetNoDefensive` |  |
| `-SetNoReqBowAbilities` |  |
| `-ShareAllMissions` |  |
| `-ShareMission` |  |
| `-ShareQuest` |  |
| `-ShareQuestsForZone` |  |
| `-Show_Available_Set_ups` | An alias of `-ShowAvailableSetups` - it works as typed. |
| `-ShowAvailableSetups` |  |
| `-ShowWikiForQuest` |  |
| `-SmartLoot_ReloadDataFromFile` |  |
| `-Special` |  |
| `-SpecialForWho` | An alias of `-Special` - it works as typed. |
| `-SpecialZoneSpecific` |  |
| `-SpecialZS` | An alias of `-SpecialZoneSpecific` - it works as typed. |
| `-Spew_BoZ_Research` |  |
| `-Spew_MissionTimerInfo_AP` |  |
| `-Spew_RelayGroup` |  |
| `-SpewFlags` |  |
| `-SpewSubscriptionStatus` |  |
| `-stand` |  |
| `-StatPotions_AutoConsume` |  |
| `-StatPotions_Replenish` |  |
| `-StopRes` |  |
| `-SubscriptionStatus` | An alias of `-SpewSubscriptionStatus` - it works as typed. |
| `-SubStatus` | An alias of `-SpewSubscriptionStatus` - it works as typed. |
| `-Summon_Familiar` |  |
| `-Target` |  |
| `-Tell` |  |
| `-TestPull1` | An alias of `-Pull` - it works as typed. |
| `-ThreatFighterIgnoreList_Add` |  |
| `-ThreatFighterIgnoreList_Clear` |  |
| `-ThreatFighterIgnoreList_Remove` |  |
| `-Timer` |  |
| `-ToggleMainWindow` |  |
| `-ToggleZoneReset` |  |
| `-ToGuild` | An alias of `-PortalToGuildHall` - it works as typed. |
| `-ToonMarked` |  |
| `-Travel` |  |
| `-TravelBell` |  |
| `-TravelDruid` |  |
| `-TravelFast` | An alias of `-FastTravel` - it works as typed. |
| `-TravelMap` | An alias of `-Travel` - it works as typed. |
| `-TravelSpire` | An alias of `-TravelSpires` - it works as typed. |
| `-TravelSpires` |  |
| `-TTS` |  |
| `-unauth` |  |
| `-UnflagAll` |  |
| `-UnflagToon` |  |
| `-UnmarkToon` |  |
| `-Unmentor` |  |
| `-Unpack_Consume_Familiars` |  |
| `-Unpack_Familiars` |  |
| `-UO` | An alias of `-UplinkOptionChange` - it works as typed. |
| `-UOS` | An alias of `-UplinkOptionSilent` - it works as typed. |
| `-UplinkOption` | An alias of `-UplinkOptionChange` - it works as typed. |
| `-Uplinkoption_change` | An alias of `-UplinkOptionChange` - it works as typed. |
| `-UplinkOptionChange` |  |
| `-UplinkOptionSilent` |  |
| `-Use_Item` | An alias of `-UseItem` - it works as typed. |
| `-Use_Item_On_Player` | An alias of `-UseItemOnPlayer` - it works as typed. |
| `-UseFlag` |  |
| `-UseItem` |  |
| `-useitemon` | An alias of `-UseItemOnPlayer` - it works as typed. |
| `-UseItemOnPlayer` |  |
| `-Waypoint` |  |
| `-Zone` |  |
| `-ZoneDoorForWho` | An alias of `-ZoneDoor` - it works as typed. |
| `-ZoneDoorOptionForWho` | An alias of `-ZoneDoor` - it works as typed. |
| `-ZoneResetAll` |  |
