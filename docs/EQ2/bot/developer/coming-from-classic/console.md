# Console commands (OgreConsole)

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../index.md).
</div>

What changed between the Classic console (V1) and the new console (V2) for every command you type after `oc !c` or `oc !ci`, or put on an MCP button.

> **:warning: Two rules for every console line**
>
> 1. **The for-who comes first** on every command that targets someone. A command that had none in Classic gets `auto` - the For Who window decides, as it always did. A line that starts `oc !c -cfw <who> -Command` already says who, and still works.
> 2. **An unknown command is not silent here** - each session that receives it prints *Unknown command entered*. A command with its arguments in the wrong order, though, still runs.

## At a glance

| What happened | Names |
|---|---|
| ⚠️ Arguments changed | 35 |
| ⚠️ Argument order changed | 10 |
| ✏️ Renamed | 4 |
| ➡️ Lives somewhere else | 1 |
| 📄 In a data file now | 18 |
| ⛔ Removed | 38 |
| ✅ Works as is | 448 |
| **Total** | **554** |

448 of the 554 Classic commands are typed exactly as before (127 of those are other names - aliases - for a command, and keep working).

## 1. Commands you must change

Every Classic console command that does not work as typed any more. Sorted by what to do.

### ⚠️ Arguments changed (35)

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
| `-Apply_Verb` | runs, arguments mean something else | `-ApplyVerb` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-Apply_Verb <actorname> <verb>`<br>**New:** `-Apply_Verb <fw> <actorname> <verb>`<br>V2 params: who, actorname, verb. Quoting one argument is still fine ("${UserInput}" stays one argument); only the command and its arguments inside ONE pair of quotes breaks the line. |
| `-ApplyVerb` | runs, arguments mean something else | `-ApplyVerb` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-ApplyVerb <actorname> <verb>`<br>**New:** `-ApplyVerb <fw> <actorname> <verb>`<br>V2 params: who, actorname, verb. Quoting one argument is still fine ("${UserInput}" stays one argument); only the command and its arguments inside ONE pair of quotes breaks the line. |
| `-AutoItemCure` | runs, arguments mean something else | `-AutoItemCure` | ⚠️ Arguments changed | Keep one cure type (or none). The exclusive / DirectTarget / Curse flags have no V2 argument.<br>**Old:** `-AutoItemCure <fw> [<flag> ...]`<br>**New:** `-AutoItemCure <fw> [<type>]` |
| `-Cancel_Maintained` | runs, arguments mean something else | `-CancelMaintained` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-Cancel_Maintained <ability> [<more abilities...>]`<br>**New:** `-Cancel_Maintained <fw> <abilityname> [<args...>]`<br>V2 params: who, abilityname, args (rest). The V1 -CancelMaintainedForWho twin is now an alias of the same row. |
| `-CancelMaintained` | runs, arguments mean something else | `-CancelMaintained` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-CancelMaintained <ability> [<more abilities...>]`<br>**New:** `-CancelMaintained <fw> <abilityname> [<args...>]`<br>V2 params: who, abilityname, args (rest). The V1 -CancelMaintainedForWho twin is now an alias of the same row. |
| `-ccs` | runs, arguments mean something else | `-ChangeCampSpot` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-ccs <x> <y> <z> (or one x,y,z token)`<br>**New:** `-ccs <fw> <x> <y> <z>`<br>… |
| `-Change_CampSpot` | runs, arguments mean something else | `-ChangeCampSpot` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-Change_CampSpot <x> <y> <z> (or one x,y,z token)`<br>**New:** `-Change_CampSpot <fw> <x> <y> <z>`<br>… |
| `-ChangeCampSpot` | runs, arguments mean something else | `-ChangeCampSpot` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-ChangeCampSpot <x> <y> <z> (or one x,y,z token)`<br>**New:** `-ChangeCampSpot <fw> <x> <y> <z>`<br>… |
| `-CheckMemberLevel` | runs, arguments mean something else | `-CheckMemberLevel` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-CheckMemberLevel <onlyShowNonMembers>`<br>**New:** `-CheckMemberLevel <fw> <value>`<br>V2 params: who, value (default FALSE). |
| `-CompareQuest` | runs, arguments mean something else | `-CompareQuest` | ⚠️ Arguments changed | Drop the step-line arguments; send it from the box whose step is the reference. The answers come back to the asker.<br>**Old:** `-CompareQuest <fw> <questname> <step lines...>`<br>**New:** `-CompareQuest <fw> <questname>`<br>GROUP-scoped by default (comms is local-box). |
| `-cs-set-cs-jo-ji-opt` | runs, arguments mean something else | `-cs-jo-ji` | ⚠️ Arguments changed | Move &lt;joustin&gt; from last to third. To keep V1's joust half, add `-joustoff <joustoff>` and `-joustin <joustin>` lines - the row no longer does it.<br>**Old:** `-cs-set-cs-jo-ji-opt <fw> <joustoff> <min> <max> <joustin>`<br>**New:** `-cs-set-cs-jo-ji-opt <fw> <joustoff> <joustin> <min> <max>`<br>BEHAVIOUR CHANGE UNDER THE SAME NAME: V2 executes ONLY OgreBotAPI.CampSpot:SetHere[who, mindistance, maxdistance]; the `joustoff` and `joustin` params are accepted and never used, so nobody is jousted off or in. |
| `-Door` | runs, arguments mean something else | `-ZoneDoor` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-Door <dooroption>`<br>**New:** `-Door <fw> <dooroption>`<br>V2 params: who, dooroption (default 1). The V1 -...ForWho twins (already for-who first) are now aliases of the same row. |
| `-DoorX` | runs, arguments mean something else | `-ZoneDoor` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-DoorX <dooroption>`<br>**New:** `-DoorX <fw> <dooroption>`<br>V2 params: who, dooroption (default 1). The V1 -...ForWho twins (already for-who first) are now aliases of the same row. |
| `-EndScript` | runs, arguments mean something else | `-EndScript` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-EndScript <scriptname>`<br>**New:** `-EndScript <fw> <scriptname>`<br>V2 params: who, scriptname -&gt; OgreBotAPI.Bot:EndScript. NOT in (it lists -EndScript under 'no ForWho'), so no caller was converted by that pass. |
| `-Group` | runs, arguments mean something else | `-Raid` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-Group <chat>`<br>**New:** `-Group <fw> <chat>`<br>V1 hard-coded the for-who to All (InjectChat_ForAll). V2 params: who, chat -&gt; OgreBotAPI.Comms:InjectChat. Guide Resolutions: "-Raid / -Group - standard ForWho (drop the hard-coded All)". |
| `-ImmRes` | runs, arguments mean something else | `-ImmRes` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-ImmRes <howmany>`<br>**New:** `-ImmRes <fw> <howmany>`<br>V2 params: who, howmany (default 2). |
| `-ItemEmbargo` | runs, arguments mean something else | `-ItemEmbargo` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-ItemEmbargo <abilityid> <duration> [<args...>]`<br>**New:** `-ItemEmbargo <fw> <abilityid> <duration> [<args...>]`<br>… |
| `-ItemRotate` | runs, arguments mean something else | `-ItemEmbargo` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-ItemRotate <abilityid> <duration> [<args...>]`<br>**New:** `-ItemRotate <fw> <abilityid> <duration> [<args...>]`<br>… |
| `-Mentor` | runs, arguments mean something else | `-Mentor` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-Mentor <mentorwho>`<br>**New:** `-Mentor <fw> <mentorwho>`<br>V2 params: who, mentorwho (default ${Me.Name}). |
| `-Move2Area` | runs, arguments mean something else | `-Move2Area` | ⚠️ Arguments changed | Move the for-who to the front and give three coordinates (x y z).<br>**Old:** `-Move2Area <X> <Z> <fw> <precision>`<br>**New:** `-Move2Area <fw> <x> <y> <z> <precision>`<br>V1's two coordinates were X and Z - a ground move (AreaToMoveTo(_XPos,_ZPos),). V2 takes x y z so ${Me.Loc} pastes straight in, and IGNORES y: put any number there. |
| `-Move2AreaNoTarget` | runs, arguments mean something else | `-MoveToAreaNoTarget` | ⚠️ Arguments changed | Move the for-who to the front and give three coordinates (x y z).<br>**Old:** `-Move2AreaNoTarget <X> <Z> <fw> <precision>`<br>**New:** `-Move2AreaNoTarget <fw> <x> <y> <z> <precision>`<br>V1's two coordinates were X and Z - a ground move (AreaToMoveTo(_XPos,_ZPos),). V2 takes x y z so ${Me.Loc} pastes straight in, and IGNORES y: put any number there. The V2 row runs OgreBotAPI.Movement:Move2AreaNoTarget: it moves with or without a target, as V1 did. |
| `-MoveToArea` | runs, arguments mean something else | `-Move2Area` | ⚠️ Arguments changed | Move the for-who to the front and give three coordinates (x y z).<br>**Old:** `-MoveToArea <X> <Z> <fw> <precision>`<br>**New:** `-MoveToArea <fw> <x> <y> <z> <precision>`<br>V1's two coordinates were X and Z - a ground move (AreaToMoveTo(_XPos,_ZPos),). V2 takes x y z so ${Me.Loc} pastes straight in, and IGNORES y: put any number there. |
| `-MoveToAreaNoTarget` | runs, arguments mean something else | `-MoveToAreaNoTarget` | ⚠️ Arguments changed | Move the for-who to the front and give three coordinates (x y z).<br>**Old:** `-MoveToAreaNoTarget <X> <Z> <fw> <precision>`<br>**New:** `-MoveToAreaNoTarget <fw> <x> <y> <z> <precision>`<br>V1's two coordinates were X and Z - a ground move (AreaToMoveTo(_XPos,_ZPos),). V2 takes x y z so ${Me.Loc} pastes straight in, and IGNORES y: put any number there. The V2 row runs OgreBotAPI.Movement:Move2AreaNoTarget: it moves with or without a target, as V1 did. |
| `-OgreBotAPI` | runs, arguments mean something else | `-OgreBotAPI` | ⚠️ Arguments changed | The method now receives the for-who first, as every new-bot OgreBotAPI method expects; the method name must be one the new OgreBotAPI registers (see the API conversion guide - most Classic flat names moved).<br>**Old:** `-OgreBotAPI <fw> <OldMethod> <args...> -> OgreBotAPI:<OldMethod>[<args...>]`<br>**New:** `-OgreBotAPI <fw> <method> <args...> -> OgreBotAPI:<method>[<fw>,<args...>]` |
| `-OgreConsole_Show` | runs, arguments mean something else | `-OgreConsole_Show` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-OgreConsole_Show <show>`<br>**New:** `-OgreConsole_Show <fw> <value>`<br>V1 called OgreConsole:ShowOgreConsole locally. V2 params: who, value (default TRUE) -&gt; OgreBotAPI.Windows:ShowConsole. |
| `-Raid` | runs, arguments mean something else | `-Raid` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-Raid <chat>`<br>**New:** `-Raid <fw> <chat>`<br>… |
| `-Run` | runs, arguments mean something else | `-Run` | ⚠️ Arguments changed | Nothing to retype; check the intent - V2 does what the name says.<br>**Old:** `-Run <fw> - flipped the current mode (a -Run sent to a box already running made it walk). New: -Run <fw> - sets run; a box already there is left alone` |
| `-SetUpFor` | runs, arguments mean something else | `-SetUpFor` | ⚠️ Arguments changed | Pass the named mob's exact name, or nothing to auto-detect. A module phrase that is not the mob's name (e.g. 'Master' for The Djinn Master, 'reset') no longer matches - it logs "no encounter owns mob".<br>**Old:** `-SetUpFor <fw> <words after "Set up for">`<br>**New:** `-SetUpFor <fw> [<named mob name>] [<restart>]`<br>restart FALSE leaves a setup that is already running alone. |
| `-SpewStat` | runs, arguments mean something else | `-SpewStat` | ⚠️ Arguments changed | Write the type as its own flag: `-SpewStat <fw> -item Foo oc` instead of `-SpewStat <fw> item_Foo oc`.<br>**Old:** `-SpewStat <fw> <prefix_value> <where>`<br>**New:** `-SpewStat <fw> <-type> <value> <where>`<br>The old mashed form is still READ: maps an unknown type through MapLegacyToken and takes `where` from the old slot, so most old lines still work. deity_* tokens are dropped, and a token it cannot map errors loudly. |
| `-SpewStats` | runs, arguments mean something else | `-SpewStat` | ⚠️ Arguments changed | Write the type as its own flag: `-SpewStat <fw> -item Foo oc` instead of `-SpewStat <fw> item_Foo oc`.<br>**Old:** `-SpewStats <fw> <prefix_value> <where>`<br>**New:** `-SpewStats <fw> <-type> <value> <where>`<br>The old mashed form is still READ: maps an unknown type through MapLegacyToken and takes `where` from the old slot, so most old lines still work. deity_* tokens are dropped, and a token it cannot map errors loudly. |
| `-Walk` | runs, arguments mean something else | `-Walk` | ⚠️ Arguments changed | Nothing to retype; check the intent - V2 does what the name says.<br>**Old:** `-Walk <fw> - flipped the current mode (a -Walk sent to a box already walking made it run). New: -Walk <fw> - sets walk; a box already there is left alone` |
| `-ZoneDoor` | runs, arguments mean something else | `-ZoneDoor` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-ZoneDoor <dooroption>`<br>**New:** `-ZoneDoor <fw> <dooroption>`<br>V2 params: who, dooroption (default 1). The V1 -...ForWho twins (already for-who first) are now aliases of the same row. |
| `-ZoneDoorOption` | runs, arguments mean something else | `-ZoneDoor` | ⚠️ Arguments changed | Insert the for-who as the first argument. V1 had NO for-who: every session that heard the line acted. V2 reads argument 1 as the for-who, so an unconverted line's value lands in the for-who slot and the real argument falls back to its default - silently. Write `auto` there; that is what the MCP migration writes.<br>**Old:** `-ZoneDoorOption <dooroption>`<br>**New:** `-ZoneDoorOption <fw> <dooroption>`<br>V2 params: who, dooroption (default 1). The V1 -...ForWho twins (already for-who first) are now aliases of the same row. |

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

### ✏️ Renamed (4)

#### ✏️ Renamed: `-OptNum`

```
; before (Classic)
oc !c -OptNum 1
; after (new bot)
oc !c -ConversationBubble auto 1
```

| You typed | Today | Type instead | What changed | Notes |
|---|---|---|---|---|
| `-OgreCraft_AddRecipesFromQuest` | Unknown command | `-OgreCraft_StartQuest` | ✏️ Renamed | Replace the verb name; the arguments are the same (`<fw>`).<br>It does MORE than V1: V1 only QUEUED the quest's recipes (with a 6/3 quantity guess); V2 is a flow that crafts the current quest's pending recipe steps, one of each per pass, until none is pending. The for-who now filters; V1 ran it on every session that heard the line. |
| `-Opt_Num` | Unknown command | `-ConversationBubble` | ✏️ Renamed | -Opt_Num was the same reply click as -ConversationBubble and is gone. Write `-ConversationBubble <fw> <num>`; V1 had no for-who, so put `auto` first (the For Who window).<br>**Old:** `-Opt_Num <num>`<br>**New:** `-ConversationBubble <fw> <num> (row -ConversationBubble)`<br>V2 params: who, num (default 1). |
| `-OptNum` | Unknown command | `-ConversationBubble` | ✏️ Renamed | -Opt_Num was the same reply click as -ConversationBubble and is gone. Write `-ConversationBubble <fw> <num>`; V1 had no for-who, so put `auto` first (the For Who window).<br>**Old:** `-OptNum <num>`<br>**New:** `-ConversationBubble <fw> <num> (row -ConversationBubble)`<br>V2 params: who, num (default 1). |
| `-Set_VampiricRequiem_Cancelling_Active` | Unknown command | `-CancelOnCast` | ✏️ Renamed | Write `-CancelOnCast <fw> <ability>` naming the trigger ability (for the old verb: Vampiric Requiem), and configure what it cancels in the Cancel On Cast tab. |

### ➡️ Lives somewhere else (1)

| You typed | Today | Type instead | What changed | Notes |
|---|---|---|---|---|
| `-Ask` | Unknown command | `ISXOgreEQ2.Comms:Query` | ➡️ Lives somewhere else | IC file: the `groupQuery` step - counts, allYes / anyYes / allNo / anyNo, per-member flags, raw answers, ready-made for-who lists. Script: the same engine - ${ISXOgreEQ2.Comms.GroupQuery[&lt;fw&gt;, -question, &lt;question&gt;, ...]} starts it and reads as its id; then ${ISXOgreEQ2.Comms.GroupQuery.Done[id]} / .Result[id] (JSON, the same names), or the event OgreEvent_GroupQueryDone(id, json). |

### 📄 In a data file now (18)

**Note A** (9 rows below): Nothing to type: the fight is coded in the zone's encounter file. An encounter author emits a cross-session signal with `broadcast` and receives it with a trigger `on: <event>`. A hand or button sender uses `-ExecuteEvent_AP <fw> <event> <args>` while that zone's encounter is loaded.

| You typed | Today | Type instead | What changed | Notes |
|---|---|---|---|---|
| `-GOAotA1` | Unknown command | `broadcast` | 📄 In a data file now | Note A |
| `-ROAOMCG` | Unknown command | `broadcast` | 📄 In a data file now | Note A |
| `-ROASEC` | Unknown command | `broadcast` | 📄 In a data file now | Note A |
| `-ROBSBFC` | Unknown command | `broadcast` | 📄 In a data file now | Note A |
| `-RODMPI` | Unknown command | `broadcast` | 📄 In a data file now | Nothing to type: the fight is coded in the zone's encounter file. An encounter author emits a cross-session signal with `broadcast` and receives it with a trigger `on: <event>`. A hand or button sender uses `-ExecuteEvent_AP <fw> <event> <args>` while that zone's encounter is loaded. Button form: `-ExecuteEvent_AP <fw> DjinnMaster_PlayInstruments <toon> <order>`. |
| `-RODMPS` | Unknown command | `campSpot` | 📄 In a data file now | Nothing to type: the portal handling is in The Djinn (spawn triggers + `campSpot`). |
| `-RODrinalDispell` | Unknown command | `broadcast` | 📄 In a data file now | Note A |
| `-RODrinalPos` | Unknown command | `campSpot` | 📄 In a data file now | Tank positioning for Drinal is in Ogre/EQ2/Encounters/default/Chains of Eternity/Harrow's End [Raid]/. |
| `-ROKoolbhCloudOfVile` | Unknown command | `broadcast` | 📄 In a data file now | Note A |
| `-ROKraletusCureCalled` | Unknown command | `broadcast` | 📄 In a data file now | Note A |
| `-ROOSSSAC` | Unknown command | `broadcast` | 📄 In a data file now | Note A |
| `-ROPC` | Unknown command | `castAbility` | 📄 In a data file now | Nothing to type for the Council: it is coded. A new pre-cure is authored in that fight's encounter file.<br>The Mutagenic Outcast file also names -ROPC in its `_status` (the raid leader's precure); that site was not re-checked here. |
| `-ROSGDDispell` | Unknown command | `dispel` | 📄 In a data file now | Nothing to type: the dispel is coded in Ogre/EQ2/Encounters/default/Chains of Eternity/Siren's Grotto - Dissension [Raid]/Diviner. |
| `-ROSGPRDispell` | Unknown command | `dispel` | 📄 In a data file now | Nothing to type: the dispel is coded in Ogre/EQ2/Encounters/default/Chains of Eternity/Siren's Grotto - Dissension [Raid]/Diviner. |
| `-ROSGPRTCS` | Unknown command | `broadcast` | 📄 In a data file now | Nothing to type: the fight is coded in the zone's encounter file. An encounter author emits a cross-session signal with `broadcast` and receives it with a trigger `on: <event>`. A hand or button sender uses `-ExecuteEvent_AP <fw> <event> <args>` while that zone's encounter is loaded. Here the sender is the operator: `-ExecuteEvent_AP <fw> SGPsyllon_TankSpot`. |
| `-ROSGTDispell` | Unknown command | `dispel` | 📄 In a data file now | Nothing to type: the dispel is coded in Ogre/EQ2/Encounters/default/Chains of Eternity/Siren's Grotto - Dissension [Raid]/Overlord. |
| `-ROSGTFDispell` | Unknown command | `dispel` | 📄 In a data file now | Nothing to type: the dispel is coded in Ogre/EQ2/Encounters/default/Chains of Eternity/Siren's Grotto - Dissension [Raid]/Overlord. |
| `-ROTOVI` | Unknown command | `broadcast` | 📄 In a data file now | Note A |

### ⛔ Removed (38)

| You typed | Today | Type instead | What changed | Notes |
|---|---|---|---|---|
| `-Aliases_ShowAllBuiltInAliases` | Unknown command | — | ⛔ Removed | V1 -&gt; Command_Aliases_ShowAllBuiltInAliases :2421 - set a combobox display flag. |
| `-AscensionEmbargo_Add_DoNotCombo` | Unknown command | — | ⛔ Removed | V1 -&gt; Command_AscensionEmbargo_Add_DoNotCombo :3086. |
| `-AscensionEmbargo_Change_Disable_Status` | Unknown command | — | ⛔ Removed | V1 -&gt; Command_AscensionEmbargo_Change_Disable_Status :3055. |
| `-AscensionEmbargo_Remove_DoNotCombo` | Unknown command | — | ⛔ Removed | V1 -&gt; Command_AscensionEmbargo_Remove_DoNotCombo :3075. |
| `-cfw` | as the first thing on a line (`-cfw <who> -Verb ...`): works, for that line only. On a line by itself: does nothing - the lasting default it set is gone | — | ⛔ Removed | As the FIRST thing after `oc !c` / `oc !ci` (`oc !ci -cfw igw:${Me.Name} -letsgo`) it still works: the new console reads it as that one line's for-who, and the verb's empty for-who takes it (the tool skips that form). Only `-cfw <who>` on a line by itself is gone - it set a lasting default for later lines. Put the for-who on each of those later verbs instead (it is argument 1).<br>V1 -&gt; Command_Set_CustomCFW :1440 wrote This.Default_CFW - a PERSISTENT default that every later `auto` for-who resolved to (Get_CommandForWho :1449). |
| `-ChangeRadarYAxis` | Unknown command | — | ⛔ Removed | V1 -&gt; method ChangeRadarYAxis :5075 -&gt; OgreBotAPI:ChangeRadarYAxis :5085 (toggle the radar Y axis). The V2 row ran OgreBotAPI.Client:SetRadarYAxis, a stub that did nothing; both were removed 2026-10-22. |
| `-cs-jo` | Unknown command | — | ⛔ Removed | Write the two steps it did: `-campspot <who> <min> <max>` then `-joustoff <joustoff>` (Classic: -cs-jo &lt;who&gt; &lt;joustoff&gt; &lt;min&gt; &lt;max&gt;; defaults auto, auto+casters, 2, 200). An MCP button is split for you.<br>**Old:** `-cs-jo <fw> <joustoff> <min> <max>`<br>**New:** `-campspot <fw> <min> <max> -joustoff <joustoff>` |
| `-cs-jo-ji` | Unknown command | — | ⛔ Removed | Write the three steps it did: `-campspot <who> <min> <max>`, `-joustoff <joustoff>`, `-joustin <joustin>` (Classic: -cs-jo-ji &lt;who&gt; &lt;joustoff&gt; &lt;min&gt; &lt;max&gt; &lt;joustin&gt;; defaults auto, auto+casters, 2, 200, auto). An MCP button is split for you.<br>**Old:** `-cs-jo-ji <fw> <joustoff> <min> <max> <joustin>`<br>**New:** `-campspot <fw> <min> <max> -joustoff <joustoff> -joustin <joustin>` |
| `-Deity_Spend` | Unknown command | — | ⛔ Removed | V1 label. V1 -&gt; Command_Deity_Spend -&gt; OgreBotAPI:SpendDietyPoints, whose only working line (the QueueCommand) is commented out - a no-op on Classic too. |
| `-DeitySpend` | Unknown command | — | ⛔ Removed | V1 label (shares the -Deity_Spend body). V1 -&gt; Command_Deity_Spend -&gt; OgreBotAPI:SpendDietyPoints, whose only working line (the QueueCommand) is commented out - a no-op on Classic too. |
| `-DevBot` | Unknown command | — | ⛔ Removed | V1 -&gt; method DevBot :4916 = `timedcommand 0 ogre dev` (started). |
| `-Fix_Broken_Shit` | Unknown command | — | ⛔ Removed | Run the parts it bundled: `ogre end console` / `ogre console` / `ogre end irc` / `ogre irc`.<br>V1 -&gt; Command_Fix_Broken_Shit :4899 -&gt; OgreBotAPI:Fix_Broken_Shit - a macro for console + IRC restarts. |
| `-GuidedAscension` | Unknown command | — | ⛔ Removed | V1 -&gt; Command_GuidedAscension :3489 -&gt; OgreBotAPI:GuidedAscension[fw, amount=3000000] (use the 'Guided Ascension' item below an ascension-vitality threshold). |
| `-HQEar` | Unknown command | — | ⛔ Removed | V1 -&gt; Command_HQEar :3421 -&gt; OgreBotAPI:CastHQEar. |
| `-HQEar_Recheck` | Unknown command | — | ⛔ Removed | V1 -&gt; Command_HQEar_Recheck :2683 -&gt; OgreBotAPI:HQEar_Recheck. |
| `-HQEar_ReEquipOriginalEar` | Unknown command | — | ⛔ Removed | V1 -&gt; Command_HQEar_ReEquipOriginalEar :2393. |
| `-HQEar_ReportStuckEar` | Unknown command | — | ⛔ Removed | V1 -&gt; Command_HQEar_ReportStuckEar :2381. |
| `-Mount` | Unknown command | — | ⛔ Removed | Use `-Force_MountOn <fw>` or `-Force_MountOff <fw>`.<br>V1 -&gt; method Mount :6838 -&gt; OgreBotAPI:Mount -&gt; f_SummonMount = `EQ2Execute /summon_mount` with its already-mounted guard commented out, i.e. a mount TOGGLE. |
| `-OgreACommandOB_AP` | Unknown command | — | ⛔ Removed | Not the same verb as -OgreCommandOB_AP (`ogre <cmd>`), which is live. |
| `-Reload_DevBot` | Unknown command | — | ⛔ Removed | V1 -&gt; Command_Reload_DevBot :3769 -&gt; OgreBotAPI:Reload_DevBot (target `ogre dev`). |
| `-ReloadOgreConsole` | Unknown command | — | ⛔ Removed | Close and reopen the panel: `ogre end console`, then `ogre console`.<br>V1 -&gt; Command_ReloadOgreConsole :4907 = `timedcommand 5 ogre console` + `timedcommnad 1 ogre end console` (typo: the close half never ran). |
| `-Report_Back` | Unknown command | — | ⛔ Removed | Ask with groupQuery instead - the IC step `groupQuery`, or from a script ${ISXOgreEQ2.Comms.GroupQuery[&lt;fw&gt;, -question, ...]}: -item -&gt; question `itemCount`; -ScriptRunning and -CommandForMe -&gt; a LavishScript[...] question; -resolve_of_slot -&gt; loot distribution's own `lootBid`.<br>Classic callers: (EveryoneHaveItem),/654 (the resolve auction - replaced by lootBid), + + (OgreAutoQuest - not ported). |
| `-ReportForList_IRC` | Unknown command | — | ⛔ Removed | V1 -&gt; Command_ReportForList_IRC :3322 -&gt; OgreBotAPI:ReportForList_IRC (the roll-call emitter). It was an IRC roll call - who ANSWERED (i.e. is actually running the bot), ordered by actor id - with one consumer, Trakanon's Toxic Life rotation. |
| `-Reporting` | Unknown command | — | ⛔ Removed | Any replacement has to answer "who is actually going to act", not "who is in my group" - see the -Reporting verdict in. |
| `-ResolveBuffCheck` | Unknown command | — | ⛔ Removed | V1 sits inside a /* Need to remove this */ block (810-814), so V1 itself already answered "Unknown command"; its method Command_ResolveBuffCheck :3839 called OgreBotAPI:ResolveBuffCheck. |
| `-RODFCJ` | Unknown command | — | ⛔ Removed | No encounter verb replaces it. |
| `-RODMIR` | Unknown command | — | ⛔ Removed | V1 -&gt; Command_RODMIR :4715 -&gt; g_RaidOb:DMIR -&gt; Master:PlaceItem - the instrument item runner. |
| `-RODTFP` | Unknown command | — | ⛔ Removed | Removed on purpose. The Fitzpitzle countdown belongs in its encounter file (Ogre/EQ2/Encounters/default/Tears of Veeshan/The Fabled), which waits for the two spells' ability ids.<br>V1 -&gt; Command_RODTFP :4791 -&gt; g_RaidOb:RODTFP[ae] -&gt; Fitzpitzle:AE - fed by (`irc !c me -RODTFP <Target.Casting.Label>`), an on-screen AE countdown read off the target's cast bar BY NAME. REMOVED 2026-10-14 - the console verb is not coming back; the fight lives in the encounter file, whose `_status` carries the ability-id capture as a deferred to-do. |
| `-RoR_Epic_ChangeInCastStack` | Unknown command | — | ⛔ Removed | V1 -&gt; Command_RoR_Epic_ChangeInCastStack :1593 -&gt; OgreBotAPI:RoR_Epic_ChangeInCastStack[fw, enabled] (enable/disable the RoR epic abilities in the cast stack). |
| `-RunWalk` | Unknown command | — | ⛔ Removed | Use `-Run <fw>` or `-Walk <fw>`, which SET the mode through OgreBotAPI.Movement:SetRunMode and never flip. Decide which one the old line meant.<br>-Run and -Walk keep their V1 spelling but no longer toggle - see their own entries. |
| `-SetQuestion` | Unknown command | — | ⛔ Removed | The effect is one option write: `-ChangeOgreBotUIOption <fw> checkbox_loot_donotlootshinies <TRUE\|FALSE>`. Note the polarity: SetQuestion TRUE set do-NOT-loot-shinies TRUE.<br>V1 -&gt; Command_SetQuestion :3735 -&gt; OgreBotAPI:SetQuestion, whose live line is `ChangeOgreBotUIOption[fw, checkbox_loot_donotlootshinies, value]` followed by `return`. |
| `-Test` | Unknown command | — | ⛔ Removed | V1 -&gt; method Test :4928 = `timedcommand 0 run test` (whatever is). |
| `-test1` | Unknown command | — | ⛔ Removed | V1 -&gt; Command_Test1 :2748 parses a for-who, two args and a tail and only `echo`es them - an arg-parsing scratch harness. |
| `-test2` | Unknown command | — | ⛔ Removed | V1 -&gt; Command_Test2 :2771, the twin of -test1 (echo only). |
| `-Unpack_EmpyralStones` | Unknown command | — | ⛔ Removed | Use `-Unpack <fw> <itemname> <unpackoption>` naming the container.<br>V1 -&gt; Command_Unpack_EmpyralStones :2726 -&gt; OgreBotAPI:Unpack_EmpyralStones[fw, option=Lowest]. |
| `-Unpack_PlanarStones` | Unknown command | — | ⛔ Removed | Use `-Unpack <fw> <itemname> <unpackoption>` naming the container.<br>V1 -&gt; Command_Unpack_PlanarStones :2737 -&gt; OgreBotAPI:Unpack_PlanarStones[fw, option=Lowest]. |
| `-Update_Turbo` | Unknown command | — | ⛔ Removed | V1 -&gt; Command_Update_Turbo :2238 -&gt; OgreBotAPI:Update_Turbo[fw, 300] (LavishScript turbo). |
| `-VampiricRequiem_AbilityCancel` | Unknown command | — | ⛔ Removed | The generic version is the Cancel On Cast tab: it cancels when the configured trigger is cast; to trigger it by hand use `-CancelOnCast <fw> <ability>`.<br>V1 -&gt; Command_VampiricRequiem_AbilityCancel :1694 -&gt; OgreBotAPI:VampiricRequiem_AbilityCancel -&gt; run TabConfig.VampiricRequiem.Handle_Cancel now. |

## 2. Every other command, A to Z

These 448 commands are typed exactly as in Classic. An alias is another name for a command; it keeps working.

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
| `-Apply_VerbForWho` |  |
| `-ApplyTempAdorn` |  |
| `-ApplyTempAdorns` | An alias of `-ApplyTempAdorn` - it works as typed. |
| `-ApplyVerbForWho` | An alias of `-Apply_VerbForWho` - it works as typed. |
| `-ApplyVerbIDForWho` |  |
| `-ApplyVerbIDQueuedForWho` |  |
| `-ApplyVerbQueuedForWho` |  |
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
| `-ccsb` |  |
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
| `-ChangeBeltAdorn` |  |
| `-ChangeCampSpotBy` | An alias of `-ccsb` - it works as typed. |
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
| `-ConsumeDeityBaubles` |  |
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
| `-cs-set-ccs-by` | An alias of `-ccsb` - it works as typed. |
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
| `-Poison_AutoConsume` |  |
| `-Poison_Replenish` |  |
| `-PoP_TempAdorns` |  |
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
| `-Unpack` |  |
| `-Unpack_Consume_Familiars` |  |
| `-Unpack_Familiars` |  |
| `-Unpack_Quantity` |  |
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
