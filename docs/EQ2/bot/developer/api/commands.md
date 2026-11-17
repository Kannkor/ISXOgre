<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../index.md).
</div>

# Commands

What a user types: the `ogre` commands (the in-game Commands panel lists them all) and the console commands (`oc !c` / `oc !ci`).

A console command is sent as `oc !c <command> <who> ...` - typed in the console, put on an MCP button or run from a script. It goes to the sessions on this PC, this one included, and the [for-who](ogrebotapi/ForWho.md) in `<who>` picks which of them act: `igw:${Me.Name}` is your whole group, `igwbn:${Me.Name}` your group without you. Left out, or `auto`, it uses the For Who window. `oc !ci` does the same as `oc !c`.

## Console commands (ISXOgreX)

### `-auth`

`-auth <nick>`

IRC only: authorizes an IRC nick to send this hub commands.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `nick` | string |  | The IRC nick to authorize |

```text
irc !c -auth SomeNick
```

### `-authlist`

`-authlist`

IRC only: says which IRC nicks are authorized.

```text
irc !c -authlist
```

### `-KillSession`

`-KillSession <target>`

IRC only, authorized senders only: ends one InnerSpace session on this PC, or all of them.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `target` | string |  | The session name (is1, is2, ...) or all |

```text
irc !c -KillSession is3
```

### `-LaunchAutoLogin`

`-LaunchAutoLogin <profile>`

From IRC, authorised senders only: runs an auto-login profile.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `profile` | one |  | The auto-login profile to run. |

```text
irc !c -LaunchAutoLogin MyProfile
```

### `-List_AutoLoginProfiles`

`-List_AutoLoginProfiles`

From IRC, authorised senders only: lists the auto-login profiles. -details adds each row, -profile &lt;name> shows one.

```text
irc !c -List_AutoLoginProfiles
```

### `-List_Sessions`

`-List_Sessions`

IRC only, authorized senders only: lists this PC's InnerSpace sessions.

```text
irc !c -List_Sessions
```

### `-LoadCharacter`

`-LoadCharacter <toon>`

From IRC, authorised senders only: logs one toon in, using the first auto-login profile that holds it.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `toon` | one |  | The toon, or toon:isN to name the session. |

```text
irc !c -LoadCharacter MyToon
```

### `-unauth`

`-unauth <nick>`

IRC only: removes an IRC nick from the authorized list.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `nick` | string |  | The IRC nick to remove |

```text
irc !c -unauth SomeNick
```

### `-unauthall`

`-unauthall`

IRC only: clears the authorized list.

```text
irc !c -unauthall
```

## `ogre` commands

### `abilitydetails`

`ogre abilitydetails [name or id]`

Show every field your ability export holds for an ability, with a search

### `account`

`ogre account`

Show this session's account and access level

### `ae`

`ogre ae`

Also: `ogre abilityefficiency`

Score your abilities as damage / (cast + recovery) into a report file

### `afk`

`ogre afk [0|on|off]`

Also: `ogre antiafk`

Keep the session alive (bare = silent; 0 = noisy; off = stop)

### `analysis`

`ogre analysis [scan|monitor|taps|export|import|end]`

Also: `ogre anal`

Watch actors, record what changes and when, and diff two of them

### `assist`

`ogre assist`

Show who this toon is assisting right now, and why

### `atb`

`ogre atb`

Also: `ogre autotargetbalance`

Open OgreBot at the AutoTarget tab (Balance generator)

### `autologin`

`ogre autologin`

Open the auto-login config panel

### `bot`

`ogre bot [<toon>] [-s <server>] [-c <class>]`

Load OgreBot (logs &lt;toon> in first if given, on that server and as that class if given)

### `buycrate`

`ogre buycrate [-r|-h|-all]`

Buy this zone's heroic/raid crates (-r raid, -h heroic, -all)

### `buyfuel`

`ogre buyfuel [amount]`

Buy the EXAMINED fuel up to &lt;amount> in the guild fuel depot

### `buyoverseermissions`

`ogre buyoverseermissions [flags] | stop | status`

Also: `ogre bom`

Buy Overseer missions from the Administrator agent

### `camp`

`ogre camp [charselect]`

Camp out to login+exit ('charselect' stays at char select)

### `chatcmd`

`ogre chatcmd [off|status|debug [on|off]|reloadauth|test <chattype> <speaker> [message]]`

Run the commands your own characters send you in chat

### `cm`

`ogre cm [-small|-large]`

Also: `ogre collection`, `ogre collections`

Add collectibles from your collectible depot to your collections

### `codexinspect`

`ogre codexinspect <Name[,Name...]|reset>`

Inspect group/raid members and upload their gear to eq2codex.com

### `codextoon`

`ogre codextoon [status]`

Upload your own gear/stat snapshot to eq2codex.com

### `commandpacks`

`ogre commandpacks`

Also: `ogre packs`

Re-read the console's commands, including command packs (Scripts/OgreExternal)

### `commands`

`ogre commands`

Also: `ogre help`

Open the Commands panel: every ogre command, searchable and runnable

### `console`

`ogre console`

Also: `ogre oc`, `ogre ogreconsole`

Open the OgreConsole window

### `craft`

`ogre craft [status|start|writs|tinker|lll|stop|end|minimize|scan|add|set|shop|?]`

Also: `ogre craft2`

Open the crafting panel

### `craftgm`

`ogre craftgm [<range>] | scan [<range>] | start [<range>] | queue [<range>] | status | stop | end | close  [depot|nodepot]`

Open the Grandmaster crafting panel ((Master) scrolls -> (Grandmaster) crafts)

### `craftingmats`

`ogre craftingmats [-<expansion> -<category> ...] | ogre craftingmats plan|help|end`

Also: `ogre cmats`

Edit the crafting-mats lists; with flags, pull a craft's mats from the harvest depot

### `craftlite`

`ogre craftlite`

Also: `ogre cl`

Cast crafting reactions only (no panel, no queue)

### `dets`

`ogre dets [m|target] [-noinfo]`

Also: `ogre detrimentals`

Dump your detrimentals, with Name and Description (a server read each; -noinfo skips them)

### `effecttracker`

`ogre effecttracker [on|off|npc on|merge|status|end]`

Also: `ogre oet`

Capture what every detrimental and NPC effect says it does, into the shared zone dataset

### `encounter`

`ogre encounter [reload|debug comms|steps on|off|sequences]`

Encounter authoring: reload the json from disk, toggle the debug echoes, list live sequences

### `examine`

`ogre examine [on|off|reset]`

Examine each NEW detrimental signature once and report it

### `experiment`

`ogre experiment [-<stat> <n>]... | items | run <row> ...`

Also: `ogre experimentui`

Boost item stats on the tradeskill Experiment tab

### `export`

`ogre export [flags]`

Also: `ogre abilityexport`

Open the export panel (-start runs it now, -default uses defaults)

### `find`

`ogre find <name> [-rorr]`

Watch for named actors and waypoint them when they spawn

### `forwhogroups`

`ogre forwhogroups [list|panel|reload]`

Also: `ogre fwg`

Name a set of toons once, then select them all with one *Team:&lt;group> for-who token

### `getquest`

`ogre getquest [list|reload|status|off]`

Hail the configured NPC for this zone and pick up its quest (you must be standing next to them)

### `ghtohouse`

`ogre ghtohouse [flags]`

Move the guild-hall depots into your house ones (-all, -scroll, ...)

### `heartstone`

`ogre heartstone [on|off|now]`

Also: `ogre hs`

Rekindle a guild-hall Heartstone (always-on; arms itself at zone-in)

### `hideeffects`

`ogre hideeffects [panel|clear|end]`

Hide the listed junk effects on your character (plain `ogre hideeffects` runs it now)

### `hl`

`ogre hl [off|status|interval <ms>]`

Also: `ogre harvestlite`

Collect resource nodes already in reach (no walking)

### `housetogh`

`ogre housetogh [flags]`

Move your house depots into the guild-hall ones (-all, -harvest, ...)

### `ic`

`ogre ic [status|list|run|check|pause|end|options] | ogre ic -<option>[=off] ...`

Also: `ogre icx`, `ogre instancecontroller`

Open the instance controller - run zones from a queue (doc 28)

### `im`

`ogre im [-depot -sell -destroy -tse -end] | depot|sell|destroy|tse|restock|trade <args> | chain | status | stop | close`

Also: `ogre inventorymanager`

Inventory manager - the window is the session; runs depot/sell/destroy/tse/restock/trade

### `info`

`ogre config`

Also: `ogre options`, `ogre config`

Open Ogre Options (account, UI scale, theme, per-game options)

### `irc`

`ogre irc`

Also: `ogre ogreirc`

Connect to IRC (`ogre end irc` disconnects). `irc <message>` sends.

### `keys`

`ogre keys`

Also: `ogre keyboard`, `ogre kbd`

Dump the keyboard state (Shift stuck? run it while it happens and send the lines)

### `lag`

`ogre lag [report [s]|dump [s]|on|off|overhead|budget <ms> <ms>|minutes <1-60>|clear|close]`

Every frame of the last few minutes - what it cost and what ran in it; find and open the FPS dips

### `leveltransmuting`

`ogre leveltransmuting [on|off|status|end]`

Also: `ogre lt`

Buy transmuter's stones from Barnaby, then transmute them, for transmuting skill-ups

### `login`

`ogre login <toon> [-s <server>] [-c <class>]`

Log a character in (does not load OgreBot). 'ogre login -?' lists the server short forms

### `mbc`

`ogre mbc <from> <to>`

Also: `ogre movebagcontents`

Move a bag's contents into another bag (bags 1-6)

### `mcp`

`ogre mcp`

Also: `ogre ogremcp`

Open the Master Control Panel

### `merchant_craft`

`ogre mc [list | #<n>|<recipe> [count]]`

Also: `ogre mc`

Buy limited recipes from a merchant, then craft them

### `mesh`

`ogre mesh <destination>`

Also: `ogre ogretravelmesh`

Travel to a destination across the zone-network mesh

### `migrate`

`ogre migrate`

Review migration status and re-run any item

### `move`

`ogre move`

NOT PORTED YET - comes with the new movement and navigation

### `moveincombat`

`ogre moveincombat`

NOT PORTED YET - comes with the new movement and navigation

### `movent`

`ogre movent`

NOT PORTED YET - comes with the new movement and navigation

### `nav`

`ogre nav -loc \"x,y,z\" [flags]`

Also: `ogre navigate`

Walk somewhere over the baked navmesh (`ogre nav -help` for the flags)

### `navlib`

`ogre navlib`

NOT PORTED YET - comes with the new navigation

### `npccast`

`ogre npccast [monitor [target|named|all|off|copy]|status|zone|capture|reload|import|end]`

Also: `ogre npccastmonitoring`

Log what mobs cast (spell name + ability id) to copy or send; watch named mobs' casts - interrupt them or run your own commands

### `oau`

`ogre oau [minLevel]`

Also: `ogre abilityupgrades`, `ogre ogreabilityupgrades`

Report which Scroll Depot scrolls upgrade an ability you know

### `osa`

`ogre osa`

Open the On-Screen Assistant

### `overflow`

`ogre overflow`

Move overflow-window items into your bags

### `overseer`

`ogre overseer [status|stop]`

Run the daily Overseer missions

### `patch`

`ogre patch [status|revert-ext]`

Also: `ogre patcher`, `ogre update`

Check for and apply updates (status: the release you are on; revert-ext: undo a core self-update)

### `paths`

`ogre paths [<path>]`

This zone's points of interest and saved paths: add them, order them, walk them, import OgreBot Classic's

### `perf`

`ogre perf [seconds] [nothreads] | stop | status`

Also: `ogre fps`

Measure the frame rate and what uses each frame - run it while it lags and paste the report

### `persona`

`ogre persona [<class>]`

Change this character's class, or with no class open the window to say which profile file each class uses on this PC; one character's own setting is on OgreBot's Persona tab

### `potcb`

`ogre potcb [on|off|status|reset|interval <ms>|end]`

Also: `ogre cbpot`

Track Potency / Crit Bonus / Fervor during fights - min, max, average and time at cap

### `pulse`

`ogre pulse [report|on|off|reset|ceiling <us>|slice <section> <us>|jobtest on|off]`

Also: `ogre pulsebudget`

Tune the per-frame time slice each resumable section gets

### `pulseprof`

`ogre pulseprof [report [n] [reads]|reset|on|off|overhead|scans [n|reset|on|off]]`

Frame time and native reads per pulse subsystem

### `pushover`

`ogre pushover <message> [-title T] [-priority N] | status|reload`

Send a push notification through Pushover.net

### `quest`

`ogre quest [1]`

Also: `ogre questhelper`, `ogre qh`

Watch for quest NPCs and dialogs and do the clicking (1 = always take reply 1)

### `questcompare`

`ogre questcompare`

Also: `ogre qc`, `ogre compare`

Show whether your group is on the same step of a quest as you (`ogre end questcompare` closes it)

### `quiver`

`ogre quiver`

Refill your quiver/pouch from your bags, then the ammo depot

### `radar`

`ogre radar [on|off|<verb>]`

Also: `ogre r`

Show what is around you - nearby actors on a panel (`ogre end radar` to stop)

### `refine`

`ogre refine [start|stop|plan|raw|rare|bags|rewards]`

Refine the Raw/Rare resources in your carried bags

### `reloadbot`

`ogre reloadbot`

Reload OgreBot if it is running (does nothing if it is not)

### `replenishnames`

`ogre replenishnames [show|reload]`

Also: `ogre staples`

The fallback food/drink/potion names the *_Replenish depot verbs use - yours, in a file

### `safefall`

`ogre safefall [on|off|panel|end]`

Also: `ogre levelsafefall`

Level Safe Fall: fly up, drop, remount, repeat

### `sessions`

`ogre sessions [on|off]`

The uplink's session watch: on/off until the uplink restarts (the saved switch is in ogre config); bare: list every session it hears

### `smalldepottobigdepot`

`ogre smalldepottobigdepot [-type]`

Also: `ogre sd2bd`

Empty a guild-hall depot into its (Large) twin

### `smartloot`

`ogre smartloot`

Also: `ogre sl`

Open the SmartLoot quota editor

### `tags`

`ogre tags`

Also: `ogre tagtimers`

Open the Tag Timers window: every Embargo and Allow tag on this character

### `taskrunner`

`ogre taskrunner [-list <list>|run <list>|start|stop|end|status|panel|lists]`

Also: `ogre tr`, `ogre packpony`, `ogre pony`

Cycle characters through their scheduled chores

### `tempadorns`

`ogre tempadorns [<profile> | list | end]`

Pick the temporary adornment for each gear piece and save it as a profile; `ogre tempadorns <profile>` applies one

### `tour`

`ogre tour`

Open the new-user tour

### `trackshiny`

`ogre trackshiny [colour]`

Watch for a coloured shiny and waypoint it

### `trade`

`ogre trade [count]`

Also: `ogre tradeit`

Trade the EXAMINED item to your target (default 12 stacks)

### `travel`

`ogre travel [fast|spire|druid|bell|map|end]`

Also: `ogre travelhelper`

Open the Travel Helper: list a fast-travel, spire, druid-ring or bell map's destinations and send the group to one

### `travelsurvey`

`ogre travelsurvey [-r <radius>] [-all]`

Also: `ogre tsurvey`

Record every actor near you into the travel survey (for building the zone corpus)

### `version`

`ogre version`

Which OgreBot release you are on (the name the What's new page uses) and when the core was built

### `watcher`

`ogre watcher`

Open the Watcher window (Find Actor + Track Shiny)

### `windowreset`

`ogre windowreset`

Also: `ogre resetwindows`

Open Reset UI Windows - put windows back where they started

### `zone`

`ogre zone [force <name>|end]`

Also: `ogre reset`, `ogre zonereset`

Open the zone-reuse resetter (OldBot's `zone` / `reset`)

## Console commands (ISXOgreEQ2)

### `-AbilityEmbargo`

`-AbilityEmbargo <who> <abilityid> <duration> <args>`

Also: `-AbilityRotate`

Embargo an ability (its name or id) for N seconds on the toons the for-who names (an ability rotation: the caster tells the others not to cast it).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who embargoes - leave blank to use the For Who window; `all` = every session that hears it. |
| `abilityid` | string |  |  |
| `duration` | string |  |  |
| `args` | rest |  |  |

Runs: `OgreBotAPI.Abilities:AddEmbargo`

```text
oc !c -AbilityEmbargo all 1234567890 15
```

### `-AbilityEmbargo_ResetAbilityEmbargo`

`-AbilityEmbargo_ResetAbilityEmbargo <who> <value>`

Clears the embargo on one ability, given by name or id, on the matching characters. A name that cannot be found (including the default Unknown) does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string | `Unknown` |  |

Runs: `OgreBotAPI.Abilities:ClearEmbargo`

```text
oc !c -AbilityEmbargo_ResetAbilityEmbargo all 1234567890
```

### `-AbilityEmbargo_ResetAllAbilityEmbargos`

`-AbilityEmbargo_ResetAllAbilityEmbargos <who>`

Clears every ability embargo on the matching characters, so their cast stacks may cast those abilities again. Item embargos are not touched.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Abilities:ClearAllEmbargos`

```text
oc !c -AbilityEmbargo_ResetAllAbilityEmbargos all
```

### `-AbilityTag_ResetAbilityTagAllow`

`-AbilityTag_ResetAbilityTagAllow <who> <value>`

Clears one held allow tag, by name, on the matching characters. A blank tag does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string | `Unknown` |  |

Runs: `OgreBotAPI.CastStack:ClearAllow`

```text
oc !c -AbilityTag_ResetAbilityTagAllow all Stifle
```

### `-AbilityTag_ResetAbilityTagEmbargo`

`-AbilityTag_ResetAbilityTagEmbargo <who> <value>`

Also: `-AbilityEmbargo_ResetAbilityTagEmbargo`

Clears one held embargo tag, by name, on the matching characters. A blank tag does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string | `Unknown` |  |

Runs: `OgreBotAPI.CastStack:ClearEmbargo`

```text
oc !c -AbilityTag_ResetAbilityTagEmbargo all Stifle
```

### `-AbilityTag_ResetAllAbilityTagAllows`

`-AbilityTag_ResetAllAbilityTagAllows <who>`

Clears every held allow tag on the matching characters, so entries that need an allow tag stop casting until one is held again.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.CastStack:ClearAllAllows`

```text
oc !c -AbilityTag_ResetAllAbilityTagAllows all
```

### `-AbilityTag_ResetAllAbilityTagEmbargos`

`-AbilityTag_ResetAllAbilityTagEmbargos <who>`

Clears every held embargo tag on the matching characters, so entries those tags were blocking may cast again.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.CastStack:ClearAllEmbargos`

```text
oc !c -AbilityTag_ResetAllAbilityTagEmbargos all
```

### `-AbilityTagEmbargo`

`-AbilityTagEmbargo <who> <tagname> <duration> <type> <args>`

Also: `-AbilityTagRotate`, `-AbilityTag`

Holds a cast stack tag on the matching characters for duration seconds: type Embargo (the default) stops entries carrying that embargo tag from casting, and type Allow lets entries that need that allow tag cast. It only takes effect while the Settings tab's Enable Tag Embargo or Enable Tag Allow box is ticked; -m &lt;buff> in the extra arguments ties the tag to a maintained buff, and a missing or 0 duration ends it at once.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `tagname` | string |  |  |
| `duration` | string |  |  |
| `type` | string | `Embargo` |  |
| `args` | rest |  |  |

Runs: `OgreBotAPI.CastStack:HoldTag`

```text
oc !c -AbilityTagEmbargo all Stifle 20 Embargo
```

### `-AbilityTracker_Add`

`-AbilityTracker_Add <who> <abilityname>`

Adds the named ability to the Ability Tracker watch list (an id is stored as the ability's name) and echoes the result. The name is not checked against the export, one already on the list is not added again, and the change is lost unless you save the profile.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `abilityname` | string |  |  |

Runs: `OgreBotAPI.Abilities:TrackerAdd`

```text
oc !c -AbilityTracker_Add ${Me.Name} "Bulwark of Order"
```

### `-AcceptQuest`

`-AcceptQuest <who> <questname>`

Accepts the new-quest offer window that is on screen. It does nothing when the Do not accept quests setting is ticked, and the quest name is not used.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `questname` | string |  |  |

Runs: `OgreBotAPI.Quest:Accept`

```text
oc !c -AcceptQuest igw:${Me.Name}
```

### `-AcceptReward`

`-AcceptReward <who> <num> <windowid>`

Also: `-AReward`

Accepts reward window. If Parameter 2 is Blank or 0 will NOT touch rewards with choices.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `num` | string | `0` | If there choices what reward to pick |
| `windowid` | string | `0` |  |

Runs: `OgreBotAPI.Windows:AcceptReward`

```text
oc !c -AcceptReward igw:${Me.Name} 1 0
```

### `-Actor_Click`

`-Actor_Click <who> <actorname> <exactname>`

Double-clicks an actor right away: a number is taken as an actor id, otherwise it picks the nearest interactable actor whose name contains the text (or matches it exactly when exactname is TRUE). Nothing happens when no such actor is found.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `actorname` | string | `asdf1323` |  |
| `exactname` | string | `FALSE` |  |

Runs: `OgreBotAPI.Actors:Click`

```text
oc !c -Actor_Click ${Me.Name} "Strange Lever" FALSE
```

### `-Actor_ClickQueued`

`-Actor_ClickQueued <who> <actorname> <exactname>`

Picks the actor the same way as -Actor_Click, but puts the click in the action queue: at its turn it double-clicks the actor and waits for the cast bar (4 seconds by default) before the next queued action. If the actor is gone by then, the click is dropped.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `actorname` | string | `asdf1323` |  |
| `exactname` | string | `FALSE` |  |

Runs: `OgreBotAPI.Actors:ClickQueued`

```text
oc !c -Actor_ClickQueued igw:${Me.Name} "Strange Lever" FALSE
```

### `-AddNoOffensiveOn`

`-AddNoOffensiveOn <who> <mobname> <exactmatchonly>`

Adds a mob name to the no-offensive list: while your target matches it, the bot casts no offensive abilities and does not auto-attack. exactmatchonly TRUE (default) needs the exact name, and FALSE matches any name that contains it.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `mobname` | string | `DoesNotExist` |  |
| `exactmatchonly` | bool | `TRUE` | TRUE: only a target with exactly this name. FALSE: any target whose name contains it. |

Runs: `OgreBotAPI.Combat:AddNoOffensive`

```text
oc !c -AddNoOffensiveOn igw:${Me.Name} "${Target.Name}" TRUE
```

### `-Alias_AddEntry`

`-Alias_AddEntry <who> <existingalias> <newalias> <noraid>`

Alias Tab - Adds a new alias entry. Example: To add: *Tank=Bob.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `existingalias` | string |  | Alias: *Tank |
| `newalias` | string |  | Alias name: Bob |
| `noraid` | string | `FALSE` | No raid scanning |

Runs: `OgreBotAPI.ForWho:AddAlias`

```text
oc !c -Alias_AddEntry igw:${Me.Name} *Tank ${Group[1].Name} FALSE
```

### `-Alias_ChangeEntryAlias`

`-Alias_ChangeEntryAlias <who> <existingalias> <newalias> <silentmode>`

Alias Tab - Changes an alias entry. Example: If an entry has *Tank=Bob - you could change all *Tank to *OffTank.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `existingalias` | string |  | Alias. Example: *Tank |
| `newalias` | string |  | New alias name. OffTank |
| `silentmode` | bool | `FALSE` | Suppress the change announcement for this call. TRUE or FALSE. |

Runs: `OgreBotAPI.ForWho:RenameAlias`

```text
oc !c -Alias_ChangeEntryAlias igw:${Me.Name} *Tank *OffTank FALSE
```

### `-Alias_ChangeEntryFor`

`-Alias_ChangeEntryFor <who> <existingalias> <newalias> <silentmode>`

Also: `-Alias_ChangeEntry`

Alias Tab - Changes an alias entry. Example: If an entry has *Tank=Bob - you could change Bob to Alice.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `existingalias` | string |  | Existing alias name. Example: Bob |
| `newalias` | string |  | New alias name. Example: Alice |
| `silentmode` | bool | `FALSE` | Suppress the change announcement for this call. TRUE or FALSE. |

Runs: `OgreBotAPI.ForWho:ChangeAlias`

```text
oc !c -Alias_ChangeEntryFor igw:${Me.Name} ${Group[1].Name} ${Me.Name} FALSE
```

### `-Alias_RemoveEntry`

`-Alias_RemoveEntry <who> <existingalias>`

Deletes the named alias (the leading * is optional) from the Aliases tab of the matched toons, and all (the default) or a blank name deletes every alias. Only the first row with that name goes, and the change lasts once the profile is saved.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `existingalias` | string | `all` |  |

Runs: `OgreBotAPI.ForWho:RemoveAlias`

```text
oc !c -Alias_RemoveEntry igw:${Me.Name} *Tank
```

### `-AltarOfTheAncients`

`-AltarOfTheAncients <who>`

Prays at the Altar Of The Ancients. Note: You need to be REALLY close to it.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Actors:ClickQueued`

```text
oc !c -AltarOfTheAncients ${Me.Name}
```

### `-ApplyVerb`

`-ApplyVerb <who> <actorname> <verb>`

Also: `-Apply_Verb`

Apply a verb to an actor by name [Actor name] [case sensitive verb] - on the toons the for-who names. Note - This is an advanced button.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who acts - leave blank to use the For Who window. |
| `actorname` | string | `All` | The actor's name or part of it, any case, or a type word: npc, namednpc, nokillnpc, pc, special, chest, resource, door |
| `verb` | string | `All` | verb - case sensitive |

Runs: `OgreBotAPI.Actors:ApplyVerb`

```text
oc !c -ApplyVerb igw:${Me.Name} "${Target.Name}" Use
```

### `-ApplyVerbID`

`-ApplyVerbID <who> <actorid> <verb>`

Apply a verb to an actor by its ID [Actor ID] [case sensitive verb] - on the toons the for-who names. Note - This is an advanced button.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who acts - leave blank to use the For Who window. |
| `actorid` | string | `0` | Actor ID |
| `verb` | string | `All` | verb - case sensitive |

Runs: `OgreBotAPI.Actors:ApplyVerbID`

```text
oc !c -ApplyVerbID igw:${Me.Name} ${Target.ID} Use
```

### `-ApplyVerbIDQueued`

`-ApplyVerbIDQueued <who> <actorid> <verb>`

Apply a verb to an actor by its ID, then wait out the cast it starts [Actor ID] [case sensitive verb] - on the toons the for-who names. Waits its turn in the action queue, then up to 5 seconds for a free cast bar. Note - This is an advanced button.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who acts - leave blank to use the For Who window. |
| `actorid` | string | `0` | Actor ID |
| `verb` | string | `All` | verb - case sensitive |

Runs: `OgreBotAPI.Actors:ApplyVerbIDQueued`

```text
oc !c -ApplyVerbIDQueued igw:${Me.Name} ${Target.ID} Use
```

### `-ApplyVerbQueued`

`-ApplyVerbQueued <who> <actorname> <verb>`

Apply a verb to an actor by name, then wait out the cast it starts [Actor name] [case sensitive verb] - on the toons the for-who names. Waits its turn in the action queue, then up to 5 seconds for a free cast bar. Note - This is an advanced button.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who acts - leave blank to use the For Who window. |
| `actorname` | string | `All` | The actor's name or part of it, any case, or a type word: npc, namednpc, nokillnpc, pc, special, chest, resource, door |
| `verb` | string | `All` | verb - case sensitive |

Runs: `OgreBotAPI.Actors:ApplyVerbQueued`

```text
oc !c -ApplyVerbQueued igw:${Me.Name} "${Target.Name}" Use
```

### `-ArcannaseEffigyOfRebirth`

`-ArcannaseEffigyOfRebirth <who>`

Use Arcanna'se Effigy Of Rebirth (KA's statue). Note: You need to be REALLY close to it.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI:ArcannaseEffigyOfRebirth`

```text
oc !c -ArcannaseEffigyOfRebirth ${Me.Name}
```

### `-assist`

`-assist <who> <assistwho>`

Also: `-ass`

Sets assists from parameters.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `assistwho` | string | `${Me.Name}` | Player to assist |

Runs: `OgreBotAPI.Assist:Anchor`

```text
oc !c -assist all ${Me.Name}
```

### `-AssistForWho`

`-AssistForWho <who> <assistwho>`

Sets who the toon assists: from the next pulse it takes its targets from the named player (an alias such as @role works too). A blank name makes the toon assist itself, so it becomes the one others assist.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `assistwho` | string | `${Me.Name}` |  |

Runs: `OgreBotAPI.Assist:Anchor`

```text
oc !c -AssistForWho igw:${Me.Name} ${Me.Name}
```

### `-AuthIfInRaid`

`-AuthIfInRaid <nick> <value>`

Also: `-AIIR`

Authorize an IRC nick if the given toon is in my raid. Runs on every session by design; the first argument is the nick, not a for-who.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `nick` | string | `SupposeToPassAParameterHere` | The IRC nick to authorize. Not a for-who: this row runs on every session on purpose, each checking its own raid. |
| `value` | string |  | The toon that must be in my raid for the nick to be authorized (default: me). |

Runs: `OgreBotAPI.Comms:IrcAuthIfInRaid`

```text
oc !c -AuthIfInRaid ${Group[1].Name} ${Me.Name}
```

### `-AutoConsumeTemporaryFamiliarExperience`

`-AutoConsumeTemporaryFamiliarExperience <who>`

Auto Consumes Temporary Familiar Experience items

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Inventory:AutoConsumeFamiliarXP`

```text
oc !c -AutoConsumeTemporaryFamiliarExperience ${Me.Name}
```

### `-AutoConsumeTemporaryMountTrainingReduction`

`-AutoConsumeTemporaryMountTrainingReduction <who>`

Auto Consumes Temporary Mount Training Reduction items

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Inventory:AutoConsumeMountTraining`

```text
oc !c -AutoConsumeTemporaryMountTrainingReduction ${Me.Name}
```

### `-AutoConsumeTemporaryResearchReduction`

`-AutoConsumeTemporaryResearchReduction <who>`

Auto Consumes Temporary Research Reduction items

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Inventory:AutoConsumeResearch`

```text
oc !c -AutoConsumeTemporaryResearchReduction ${Me.Name}
```

### `-AutoCure`

`-AutoCure <who> <toonname> <args>`

Ask the curers to cure a toon. No kinds = arcane, elemental, noxious and trauma; name kinds (arcane/a, elemental/e, noxious/n, trauma/t, curse, confrontfear) to cure only those. Options: -AutoRemove &lt;seconds> (give up after this long, default 8), -tag &lt;name> (a name -AutoCureRemove can cancel it by). Any other word refuses the request.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `toonname` | string |  |  |
| `args` | rest |  | Kinds, then options: -AutoRemove &lt;seconds>, -tag &lt;name> |

Runs: `OgreBotAPI.Cures:Request`

```text
oc !c -AutoCure igw:${Me.Name} ${Group[1].Name} trauma
```

### `-AutoCureRemove`

`-AutoCureRemove <who> <toonortag>`

Cancel the curse, cure (-AutoCure) and group cure (-AutoGroupCure) requests for a toon or tag.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `toonortag` | string |  | The toon the requests were for, or the -tag they were given |

Runs: `OgreBotAPI.Cures:CancelRequests`

```text
oc !c -AutoCureRemove igw:${Me.Name} ${Me.Name}
```

### `-AutoCurse`

`-AutoCurse <who> <toonname> <args>`

Ask the curers to cure a curse off a toon. Options: -AutoRemove &lt;seconds> (give up after this long, default 8), -tag &lt;name> (a name -AutoCureRemove can cancel it by). Any other word refuses the request.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `toonname` | string |  | The cursed toon |
| `args` | rest |  | Options: -AutoRemove &lt;seconds>, -tag &lt;name> |

Runs: `OgreBotAPI.Cures:RequestCurse`

```text
oc !c -AutoCurse igw:${Me.Name} ${Me.Name} -AutoRemove 20
```

### `-AutoGroupCure`

`-AutoGroupCure <who> <args>`

Cast the group cure once enough of the group carry a detriment. Kinds: arcane/a, elemental/e, noxious/n, trauma/t (none named = any of the four; each kind is counted on its own). Options: -count &lt;n> (at least n of you and the group, default 1), -AutoRemove &lt;seconds> (watch this long, default 8), -tag &lt;name> (a name -AutoCureRemove can cancel it by). Any other word refuses the request.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `args` | rest |  | Kinds, then options: -count &lt;n>, -AutoRemove &lt;seconds>, -tag &lt;name> |

Runs: `OgreBotAPI.Cures:RequestGroupWatch`

```text
oc !c -AutoGroupCure igw:${Me.Name} arcane trauma -count 3
```

### `-autohunt`

`-autohunt <who> <mode>`

Set the Auto-Hunt driver mode: off (stop) or hunt (full grind - scan, camp, prebuff, pull, and walk the path picked on the Auto-Hunt tab between pulls).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `mode` | string | `hunt` | off \| hunt (default hunt). |

Runs: `OgreBotAPI.AutoHunt:SetMode`

```text
oc !c -autohunt ${Me.Name} hunt
```

### `-AutoItemCure`

`-AutoItemCure <who> <type>`

Ask the matched toons to cure themselves with a Cure &lt;type> potion from their bags. A potion only cures its drinker, so there is no victim argument - whoever the for-who matches is who drinks. Leave the type blank for whatever they are actually afflicted with.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `type` | string |  | arcane, elemental, noxious or trauma. Blank (or 'any') = whatever is needed, decided when the potion is actually drunk. |

Runs: `OgreBotAPI.Cures:RequestItem`

```text
oc !c -AutoItemCure igw:${Me.Name} noxious
```

### `-AutoRun`

`-AutoRun <who>`

Presses the auto run key.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Movement:AutoRun`

```text
oc !c -AutoRun igw:${Me.Name}
```

### `-AutoTarget_AddActor`

`-AutoTarget_AddActor <who> <actorname> <hp> <aggroongrouponly> <checkcollision> <maxhp> <aggroonnonfighteronly> <aggroonnotme> <keeplast>`

Also: `-AT_Add`

Adds an entry to the matched toons' AutoTarget working list: the actor name with minimum and maximum HP and its aggro and collision checks, with aggroongrouponly defaulting to TRUE. A blank name adds nothing, and new entries go in above an entry marked keeplast.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `actorname` | string |  |  |
| `hp` | int64 | `0` |  |
| `aggroongrouponly` | string | `TRUE` |  |
| `checkcollision` | string | `FALSE` |  |
| `maxhp` | int64 | `0` |  |
| `aggroonnonfighteronly` | string | `FALSE` |  |
| `aggroonnotme` | string | `FALSE` |  |
| `keeplast` | string | `FALSE` | TRUE: this entry stays last - every later add goes in above it (the IC's named; adds go before the named) |

Runs: `OgreBotAPI.AutoTarget:AddActor`

```text
oc !c -AutoTarget_AddActor igw:${Me.Name} "a frost giant" 0 TRUE FALSE 0 FALSE FALSE FALSE
```

### `-AutoTarget_Clear`

`-AutoTarget_Clear <who>`

Empties the current AutoTarget list and forgets which saved list was loaded. Saved lists are not touched.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.AutoTarget:Clear`

```text
oc !c -AutoTarget_Clear igw:${Me.Name}
```

### `-AutoTarget_ClearActors`

`-AutoTarget_ClearActors <who>`

Also: `-AT_Clear`

Empties the AutoTarget working list on the matched toons, so no list is loaded any more.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.AutoTarget:Clear`

```text
oc !c -AutoTarget_ClearActors igw:${Me.Name}
```

### `-AutoTarget_Disable`

`-AutoTarget_Disable <who> <key>`

Also: `-AT_Disable`

Pauses automatic targeting under the key you give: assist, AutoTarget and the other automatic sources stop changing target, and the current target is held until that key is released with -AutoTarget_Enable. A blank key does nothing, each key releases on its own, and a zone change clears them all.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `key` | string |  |  |

Runs: `OgreBotAPI.AutoTarget:Suppress`

```text
oc !c -AutoTarget_Disable igw:${Me.Name} MyScript
```

### `-AutoTarget_Enable`

`-AutoTarget_Enable <who> <key>`

Also: `-AT_Enable`

Releases the automatic-targeting pause held under the key you give; targeting resumes once no key is left holding it. A blank key does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `key` | string |  |  |

Runs: `OgreBotAPI.AutoTarget:Release`

```text
oc !c -AutoTarget_Enable igw:${Me.Name} MyScript
```

### `-AutoTarget_RemoveActor`

`-AutoTarget_RemoveActor <who> <actorname>`

Also: `-AT_Remove`

Removes every AutoTarget entry matching the actor name - only that actor's entries, the rest of the list stays.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `actorname` | string |  |  |

Runs: `OgreBotAPI.AutoTarget:RemoveActor`

```text
oc !c -AutoTarget_RemoveActor igw:${Me.Name} "a frenzied ghoul"
```

### `-AutoTarget_SetScanHeight`

`-AutoTarget_SetScanHeight <who> <value>`

Also: `-AT_Height`

AutoTarget - Sets a new scan height.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | int64 | `5` | New scan height. Example: 5 |

Runs: `OgreBotAPI.AutoTarget:SetScanHeight`

```text
oc !c -AutoTarget_SetScanHeight igw:${Me.Name} 5
```

### `-AutoTarget_SetScanRadius`

`-AutoTarget_SetScanRadius <who> <value>`

Also: `-AT_Scan`

AutoTarget - Sets a new scan radius.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | int64 | `50` | New scan radius. Example: 50 |

Runs: `OgreBotAPI.AutoTarget:SetScanRadius`

```text
oc !c -AutoTarget_SetScanRadius igw:${Me.Name} 50
```

### `-AutoTargetOCSToggle`

`-AutoTargetOCSToggle <who> <value> <silent>`

Also: `-ATOCST`

Turns AutoTarget's out-of-combat scanning on (TRUE), off (FALSE) or flips it (TOGGLE, the default) on the matched toons. silent TRUE skips the change announcement.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string | `TOGGLE` |  |
| `silent` | bool | `FALSE` |  |

Runs: `OgreBotAPI.Options:Set`

```text
oc !c -AutoTargetOCSToggle igw:${Me.Name} TOGGLE FALSE
```

### `-AutoTargetToggle`

`-AutoTargetToggle <who> <value> <silent>`

Also: `-ATT`

Turns AutoTarget on (TRUE), off (FALSE) or flips it (TOGGLE, the default) on the matched toons. silent TRUE skips the change announcement.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string | `TOGGLE` |  |
| `silent` | bool | `FALSE` |  |

Runs: `OgreBotAPI.Options:Set`

```text
oc !c -AutoTargetToggle igw:${Me.Name} TRUE FALSE
```

### `-BuyFromMerchant`

`-BuyFromMerchant <who> <itemname> <value>`

Buys the quantity (default 1) of the named item from the merchant window that is already open, and accepts the purchase prompt if one comes up. No item, no merchant window, or an item the merchant does not sell each get one line.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `itemname` | string |  |  |
| `value` | string | `1` |  |

Runs: `OgreBotAPI.Merchant:Buy`

```text
oc !c -BuyFromMerchant ${Me.Name} "Bundle of Arrows" 2
```

### `-CallGH`

`-CallGH <who>`

Also: `-CallToGH`

Calls to guild hall if not already in one.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Movement:CallGH`

```text
oc !c -CallGH igw:${Me.Name}
```

### `-campspot`

`-campspot <who> <mindistance> <maxdistance>`

Also: `-cs-set-cs`, `-cs`

Sets campspot.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `mindistance` | float | `2` | Min. Distance |
| `maxdistance` | float | `200` | Max. Distance |

Runs: `OgreBotAPI.CampSpot:SetHere`

```text
oc !c -campspot igw:${Me.Name} 2 200
```

### `-CampToDesktop`

`-CampToDesktop <who> <loginonly>`

Also: `-Camp`

Camps to the login screen, then closes the session unless loginonly is TRUE. Refused while in combat.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `loginonly` | string | `FALSE` |  |

Runs: `OgreBotAPI.Bot:CampToDesktop`

```text
oc !c -CampToDesktop igw:${Me.Name} FALSE
```

### `-CancelCasting`

`-CancelCasting <who> <args>`

Also: `-Cancel_Casting`

Cancels the ability you are casting unless it is one of the ability names you list. -HOAbility, -HOAbilityUI and -CastTime &lt;seconds> narrow when it cancels, -CastAbility, -CastAbilityOnPlayer and -CastHOAbilityIconID queue a cast first, and any other -word cancels nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `args` | rest |  |  |

Runs: `OgreBotAPI.Abilities:CancelCasting`

```text
oc !c -CancelCasting igw:${Me.Name} "Bulwark of Order"
```

### `-cancelcastnoexport`

`-cancelcastnoexport <who> <abilityname>`

Also: `-ccstnoexport`, `-castnoexport`, `-CastAbilitynoexport`, `-cast_abilitynoexport`

Queues the named ability (a name or an id) only if the toon knows it and it is off cooldown, and silently does nothing otherwise. Despite the name it does not cancel the current cast.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `abilityname` | string | `Nothing` |  |

Runs: `OgreBotAPI.Abilities:CastNoExport`

```text
oc !c -cancelcastnoexport igw:${Me.Name} Kick
```

### `-CancelDetrimental`

`-CancelDetrimental <who> <mainid> <backdropid>`

Cancels the detrimental effect on you whose main icon id and backdrop icon id match the two values. Both 0 does nothing, and no match prints a console line.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `mainid` | string | `0` |  |
| `backdropid` | string | `0` |  |

Runs: `OgreBotAPI.Cures:CancelDetrimental`

```text
oc !c -CancelDetrimental igw:${Me.Name} 612 317
```

### `-CancelGroupWaterBreathing`

`-CancelGroupWaterBreathing <who>`

Cancels this class's group water-breathing effect if it is running. A class without one does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Abilities:CancelGroupWaterBreathing`

```text
oc !c -CancelGroupWaterBreathing igw:${Me.Name}
```

### `-CancelMaintained`

`-CancelMaintained <who> <abilityname> <args>`

Also: `-Cancel_Maintained`, `-CancelMaintainedForWho`, `-Cancel_MaintainedForWho`

Cancel Maintained ability

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who acts - leave blank to use the For Who window. |
| `abilityname` | string | `DefaultAbilityHere` | Ability to cancel |
| `args` | rest |  |  |

Runs: `OgreBotAPI.Abilities:CancelMaintainedFor`, `OgreBotAPI.Abilities:CancelMaintainedFor`

```text
oc !c -CancelMaintained igw:${Me.Name} "Spirit of the Wolf"
```

### `-CancelOnCast`

`-CancelOnCast <who> <abilityname>`

Fires the Cancel On Cast rows as if you had just cast this ability. Example: -CancelOnCast igw:${Me.Name} "Kick"

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `abilityname` | string |  | The ability name to trigger on. |

Runs: `OgreBotAPI.Abilities:CancelOnCast`

```text
oc !c -CancelOnCast igw:${Me.Name} Kick
```

### `-Cast_Interrupt`

`-Cast_Interrupt <who> <mobnameid> <calledfrom>`

Also: `-CastInterrupt`

Casts an interrupt the toon has ready at the given mob (an exact name or an actor id), first cancelling its current cast unless that is already an interrupt. It echoes when the mob is not found or no interrupt is ready.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `mobnameid` | string |  |  |
| `calledfrom` | string | `OgreConsole_Cast_Interrupt` |  |

Runs: `OgreBotAPI.Abilities:CastInterrupt`

```text
oc !c -Cast_Interrupt igw:${Me.Name} ${Target.ID} MyScript
```

### `-CastAbility`

`-CastAbility <who> <abilityname>`

Also: `-cancelcast`, `-ccst`, `-cast`, `-cast_ability`

Casts an ability at your current target, by name or id.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `abilityname` | string | `Nothing` | Spell to be cast |

Runs: `OgreBotAPI.Abilities:Cast`

```text
oc !c -CastAbility igw:${Me.Name} Kick
```

### `-CastAbilityInSeconds`

`-CastAbilityInSeconds <who> <abilityname> <seconds>`

Casts the named ability after a delay, through the same checks as -CastAbility when the time is up. A bare number is seconds, a suffix such as 500ms is honoured, and a blank ability name only echoes an error.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `abilityname` | string | `Nothing` |  |
| `seconds` | string | `1` |  |

Runs: `OgreBotAPI.Abilities:CastInSeconds`

```text
oc !c -CastAbilityInSeconds igw:${Me.Name} Kick 5
```

### `-CastAbilityNoChecks`

`-CastAbilityNoChecks <who> <abilityname>`

Tells [Bots] to cast a specific [ability]. Note - Abilities must be base names. Kick will work. Kick III will not. Note - This does NO checks about the ability. It just clicks it.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `abilityname` | string | `Nothing` | Spell to be cast |

Runs: `OgreBotAPI.Abilities:CastNoChecks`

```text
oc !c -CastAbilityNoChecks igw:${Me.Name} Kick
```

### `-CastAbilityOnNPC`

`-CastAbilityOnNPC <who> <abilityname> <mobnameid>`

Also: `-castonnpc`, `-castonmob`

Tells [Bots] to cast a specific [ability] on an [NPC]. Note - Abilities must be base names. Kick will work. Kick III will not.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `abilityname` | string | `Nothing` | Spell to be cast |
| `mobnameid` | string | `0` | NPC ID or NPC Name. \${Target.ID} will work fine |

Runs: `OgreBotAPI.Abilities:CastOnNPC`

```text
oc !c -CastAbilityOnNPC igw:${Me.Name} Kick ${Target.ID}
```

### `-CastAbilityOnPlayer`

`-CastAbilityOnPlayer <who> <abilityname> <onplayer>`

Also: `-cancelcaston`, `-ccaston`, `-caston`, `-cast_ability_on_player`

Tells [Bots] to cast a specific [ability]. Note - Abilities must be base names. Kick will work. Kick III will not.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `abilityname` | string | `Nothing` | Spell to be cast |
| `onplayer` | string | `${Me.Name}` | Cast spell on this player |

Runs: `OgreBotAPI.Abilities:CastOnPlayer`

```text
oc !c -CastAbilityOnPlayer igw:${Me.Name} "Spirit of the Wolf" ${Me.Name}
```

### `-CastAbilityOnPlayerInSeconds`

`-CastAbilityOnPlayerInSeconds <who> <abilityname> <onplayer> <seconds>`

Casts the ability on the named player after a delay, through the same checks as -CastAbilityOnPlayer when the time is up. A bare number is seconds, and a blank player (or DoesNotExist) means the toon that sent the command.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `abilityname` | string | `Nothing` |  |
| `onplayer` | string | `${Me.Name}` |  |
| `seconds` | string | `1` |  |

Runs: `OgreBotAPI.Abilities:CastOnPlayerInSeconds`

```text
oc !c -CastAbilityOnPlayerInSeconds igw:${Me.Name} "Spirit of the Wolf" ${Group[1].Name} 10
```

### `-CastAbilityOnPlayerNoChecks`

`-CastAbilityOnPlayerNoChecks <who> <abilityname> <onplayer> <calledfrom>`

Queues the ability on the named player without the readiness checks -CastAbilityOnPlayer makes, though the player must still be present. A blank player (or DoesNotExist) means yourself, and an ability the toon does not know does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `abilityname` | string | `Nothing` |  |
| `onplayer` | string | `DoesNotExist` |  |
| `calledfrom` | string | `OgreBotAPI` |  |

Runs: `OgreBotAPI.Abilities:CastOnPlayerNoChecks`

```text
oc !c -CastAbilityOnPlayerNoChecks igw:${Me.Name} "Spirit of the Wolf" ${Group[1].Name} MyScript
```

### `-CastBulwarkImmediately`

`-CastBulwarkImmediately <who>`

Casts Bulwark of Order right now: it queues the cast at high priority, cancels any other cast in the way and tries once more a second later if it has not gone off. If the ability is not in the toon's export or not ready, it casts nothing and warns everyone, at most once every 30 seconds.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Abilities:CastBulwark`

```text
oc !c -CastBulwarkImmediately igw:${Me.Name}
```

### `-CastGroupWaterBreathing`

`-CastGroupWaterBreathing <who>`

Casts this class's group water-breathing ability through the normal cast path. A class without one, or a character whose ability export does not list it, does nothing (the reason goes to the log file).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Abilities:CastGroupWaterBreathing`

```text
oc !c -CastGroupWaterBreathing igw:${Me.Name}
```

### `-CastHOIconID`

`-CastHOIconID <who> <iconid> <calledfrom>`

Casts the toon's own ability that matches the given heroic opportunity icon id, through the same checks as -CastAbility. An icon id of -2 or blank does nothing, and so does an icon no owned ability matches right now.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `iconid` | string | `-2` | The HO icon id to cast an ability for (a number, not an ability name); -2 casts nothing. |
| `calledfrom` | string | `CastHOIconID` |  |

Runs: `OgreBotAPI.Abilities:CastHOIcon`

```text
oc !c -CastHOIconID igw:${Me.Name} 3 MyScript
```

### `-CastRescue_AP`

`-CastRescue_AP <who> <calledfrom> <args>`

Casts a rescue at your NPC target: a threat-position-increase ability first, or a force-target ability when there is none (-NoForceTargets skips that step). -TargetID or -ActorID &lt;id> aims at that actor, other arguments narrow the ability query, and a console line says when nothing was found.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `calledfrom` | string | `OgreBotAPI:CastRescue` |  |
| `args` | rest |  |  |

Runs: `OgreBotAPI.Abilities:CastRescue`

```text
oc !c -CastRescue_AP ${Me.Name} CastRescue -NoForceTargets
```

### `-Champions_Zone_Resetter`

`-Champions_Zone_Resetter <who> <zonename>`

Uses your Champion's Zone Lockout Reset item to reset the lockout of the named zone, picking it from the item's select window, and skips when the reset is on cooldown. Runs in the action queue, and prints a console line and stops when the item is not in your bags.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `zonename` | string | `DoesNotExist` |  |

Runs: `OgreBotAPI.Zone:ChampionsResetter`

```text
oc !c -Champions_Zone_Resetter ${Me.Name} "${Zone.Name}"
```

### `-ChangeBeltAdorn`

`-ChangeBeltAdorn <who> <value> <unequip>`

Changes your belt adorn. Valid options are stun stifle mez fear medic.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string | `?` | Which adornment to put on the belt: Stun, Stifle, Mez, Fear or Medic. |
| `unequip` | string | `TRUE` | Unequip belt |

Runs: `OgreBotAPI.Inventory:ChangeBeltAdorn`

```text
oc !c -ChangeBeltAdorn igw:${Me.Name} Stun TRUE
```

### `-ChangeCampSpot`

`-ChangeCampSpot <who> <x> <y> <z>`

Also: `-Change_CampSpot`, `-ccs`, `-ChangeCampSpotWho`, `-Change_Campspot_Who`, `-ccsw`, `-ccsfw`

Relays a change to active campspots.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who acts - leave blank to use the For Who window. |
| `x` | string |  | X, or the name of a point of interest in this zone |
| `y` | string |  | YCord |
| `z` | string |  | ZCord |

Runs: `OgreBotAPI.CampSpot:SetLoc`

```text
oc !c -ChangeCampSpot igw:${Me.Name} ${Me.X} ${Me.Y} ${Me.Z}
```

### `-ChangeCastStackListBoxItem`

`-ChangeCastStackListBoxItem <who> <object> <value> <silentmode>`

Also: `-ChangeCastStack`, `-CCastStack`, `-CCStack`

Changes a list box item on the CAST STACK tab only.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `object` | string |  | Ability name |
| `value` | string | `TRUE` | TRUE - FALSE or TOGGLE |
| `silentmode` | bool | `FALSE` | Silent mode. TRUE or FALSE |

Runs: `OgreBotAPI.CastStack:SetEntry`

```text
oc !c -ChangeCastStackListBoxItem igw:${Me.Name} "Absorb Magic" TOGGLE FALSE
```

### `-ChangeCastStackListBoxItemByTag`

`-ChangeCastStackListBoxItemByTag <who> <object> <value> <partial> <silentmode>`

Also: `-ChangeCastStackByTag`, `-CCastStackByTag`, `-CCStackByTag`

Changes a list box item on the CAST STACK tab only by custom Tags.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `object` | string |  | Tag name |
| `value` | string | `TRUE` | Status: (Enabled/Disabled) TRUE or FALSE or Toggle |
| `partial` | bool | `FALSE` | Partial match: TRUE or FALSE (case sensitive) |
| `silentmode` | bool | `FALSE` | Silent mode. TRUE or FALSE (case sensitive) |

Runs: `OgreBotAPI.CastStack:SetEntryByTag`

```text
oc !c -ChangeCastStackListBoxItemByTag igw:${Me.Name} AE FALSE FALSE FALSE
```

### `-ChangeLootOptions`

`-ChangeLootOptions <who> <args>`

Changes loot options. Parameters after = Options you want. Such as LO or RR or FFA. See wiki for full possible parameters.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `args` | rest |  |  |

Runs: `OgreBotAPI.Loot:SetOptions`

```text
oc !c -ChangeLootOptions ${Me.Name} RR T AN
```

### `-ChangeOgreBotUIOption`

`-ChangeOgreBotUIOption <who> <args>`

Changes an OgreBot option: a checkbox (TRUE / FALSE / TOGGLE), a text box, a dropdown or a slider (its value). Param 1 = For who. Param 2 = the option's name - in OgreBot, right-click the option and choose Copy &lt;name>. Param 3 = the value.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `args` | rest |  |  |

Runs: `OgreBotAPI.Options:Set`

```text
oc !c -ChangeOgreBotUIOption igw:${Me.Name} checkbox_autotarget_enabled TRUE
```

### `-ChangeZoneTo`

`-ChangeZoneTo <who> <value>`

Changes your zone # to someone elses in your group. Example: You are in Phantom Seas 2 and your group is in Phantom Seas 3.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string |  | Toon name's zone to move to. Example: Bob. \${Me.Name} is acceptable also |

Runs: `OgreBotAPI.Zone:ChangeZoneTo`

```text
oc !c -ChangeZoneTo ${Me.Name} ${Group[1].Name}
```

### `-CheckGear`

`-CheckGear <who> <equalorunder>`

Also: `-Gear`

Reports gear conditions. Value to report. Will always report under 30. If you want it to report 90% or below use 90.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `equalorunder` | string | `100` |  |

Runs: `OgreBotAPI.Inventory:CheckGear`

```text
oc !c -CheckGear igw:${Me.Name} 90
```

### `-CheckKunarkAscendingRequirements`

`-CheckKunarkAscendingRequirements <who>`

Will report back any quests that you are missing for Kunark Ascending signature request line requirements.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Quest:CheckKunarkAscending`

```text
oc !c -CheckKunarkAscendingRequirements igw:${Me.Name}
```

### `-CheckMemberLevel`

`-CheckMemberLevel <who> <value>`

Reports EQ2's membership level. Such as Member or silver or free. Optional Parameter: Set to TRUE if you only want to see non-members.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string | `FALSE` |  |

Runs: `OgreBotAPI.Roster:CheckMemberLevel`

```text
oc !c -CheckMemberLevel igw:${Me.Name} FALSE
```

### `-CheckMercenaryTraining`

`-CheckMercenaryTraining <who>`

Resumes your mercenary when it is not out, opens Persona, Mercenary and prints the training progress or starts training; in a full group it stops at once with a console line. Runs in the action queue, and a second press replaces the first.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Consumables:CheckMercenaryTraining`

```text
oc !c -CheckMercenaryTraining ${Me.Name}
```

### `-CheckMountTraining`

`-CheckMountTraining <who>`

Opens Persona, Mounts and starts mount training when it is not running, answering the confirm popup. Runs in the action queue, and you must be on a mount (not a flight transport).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Consumables:CheckMountTraining`

```text
oc !c -CheckMountTraining ${Me.Name} FALSE
```

### `-CheckResearch`

`-CheckResearch <who> <value>`

Checks if your research of abilities is done. Only reports completed by default. Pass TRUE if you want to see how long remaining.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string | `FALSE` | Report all values |

Runs: `OgreBotAPI.Util:CheckResearch`

```text
oc !c -CheckResearch igw:${Me.Name} TRUE
```

### `-CheckVersion`

`-CheckVersion <who> <compareversionto>`

Each session compares its version to the one you pass and reports the verdict to IRC. Leave the version blank to just report versions.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `compareversionto` | string |  | Version to compare against. Blank = just report the version. |

Runs: `OgreBotAPI.Comms:ReportVersion`

```text
oc !c -CheckVersion all
```

### `-ChoiceWindow`

`-ChoiceWindow <who> <value>`

Clicks option N (default 1) on the yes/no choice window on screen. Nothing happens when none is open.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | int64 | `1` |  |

Runs: `OgreBotAPI.Windows:Choice`

```text
oc !c -ChoiceWindow igw:${Me.Name} 1
```

### `-ClassInfo_ChangeValue`

`-ClassInfo_ChangeValue <who> <member> <value>`

Overrides one class check (such as IsFighter) for this character, so the bot treats the class as having that value; auto removes the override. A member that is not a class name, or a value that is not TRUE, FALSE or auto, is refused with a console line, and the override is dropped when you switch characters.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `member` | string | `DoesNotExist` |  |
| `value` | string | `FALSE` |  |

Runs: `OgreBotAPI.Roster:SetClassValue`

```text
oc !c -ClassInfo_ChangeValue ${Me.Name} IsFighter TRUE
```

### `-Clear_Allow_HOICon`

`-Clear_Allow_HOICon <who> <variablename>`

Removes one HO icon id from the allow list.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `variablename` | int64 |  |  |

Runs: `OgreBotAPI.HOs:ClearAllowIcon`

```text
oc !c -Clear_Allow_HOICon ${Me.Name} 12
```

### `-Clear_Allow_HOICons`

`-Clear_Allow_HOICons <who>`

Empties the HO icon allow list, so Heroic Opportunity abilities are no longer limited to it.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.HOs:ClearAllowIcons`

```text
oc !c -Clear_Allow_HOICons ${Me.Name}
```

### `-Clear_Disable_HOICon`

`-Clear_Disable_HOICon <who> <variablename>`

Removes one HO icon id from the disable list.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `variablename` | int64 |  |  |

Runs: `OgreBotAPI.HOs:ClearDisableIcon`

```text
oc !c -Clear_Disable_HOICon ${Me.Name} 24
```

### `-Clear_Disable_HOICons`

`-Clear_Disable_HOICons <who>`

Empties the HO icon disable list.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.HOs:ClearDisableIcons`

```text
oc !c -Clear_Disable_HOICons ${Me.Name}
```

### `-clear_Internalvariable`

`-clear_Internalvariable <who> <variablename>`

Removes the named entry from the bot's internal variable store on this session.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `variablename` | string |  |  |

Runs: `OgreBotAPI.Vars:ClearInternal`

```text
oc !c -clear_Internalvariable ${Me.Name} PullCount
```

### `-clear_Internalvariables`

`-clear_Internalvariables <who>`

Empties the bot's internal variable store on this session.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Vars:ClearAllInternal`

```text
oc !c -clear_Internalvariables ${Me.Name}
```

### `-clear_variable`

`-clear_variable <who> <variablename>`

Removes the named entry from the script variable store on this session.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `variablename` | string |  |  |

Runs: `OgreBotAPI.Vars:Clear`

```text
oc !c -clear_variable igw:${Me.Name} Phase
```

### `-clear_variables`

`-clear_variables <who>`

Empties the script variable store on this session.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Vars:ClearAll`

```text
oc !c -clear_variables igw:${Me.Name}
```

### `-ClearNoOffensiveOn`

`-ClearNoOffensiveOn <who>`

Empties the no-offensive mob name list. The -SetNoOffensive switch is not changed.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Combat:ClearNoOffensive`

```text
oc !c -ClearNoOffensiveOn igw:${Me.Name}
```

### `-CloseExamineWindow`

`-CloseExamineWindow <who>`

Clicks the Close button of the item examine window.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Windows:CloseExamine`

```text
oc !c -CloseExamineWindow ${Me.Name}
```

### `-CloseWindow`

`-CloseWindow <who>`

Also: `-ClsWdn`

Close Window. Closes the top most window in the game.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Windows:Close`

```text
oc !c -CloseWindow igw:${Me.Name}
```

### `-Come2Me`

`-Come2Me <who> <moveto> <precision>`

Also: `-ComeTome`

Tells [Bots] to move to a specific [player].

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to move - leave blank to use the For Who window. |
| `moveto` | string | `${Me.Name}` | Player to move to (the destination toon) |
| `precision` | float | `3` | Precision |

Runs: `OgreBotAPI.Movement:Come2Me`

```text
oc !c -Come2Me igw:${Me.Name} ${Me.Name} 3
```

### `-CompareQuest`

`-CompareQuest <who> <questname> <sender>`

Asks the boxes named whether they are on the same step of a quest as you. Only the box that sends the line asks.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who is asked - leave blank to use the For Who window. all asks your group. |
| `questname` | string |  | The quest to compare. Quote a name with spaces. IE: "A Quest Name" |
| `sender` | string | `${Me.Name}` | The box that asks. Leave this out: it is the box that sent the line. |

Runs: `OgreBotAPI.Quest:CompareUpdate`

```text
oc !c -CompareQuest all "The Quest Name"
```

### `-Consume_Familiars`

`-Consume_Familiars <who>`

Adds Familiars to collection if possible otherwise consumes for experience.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Inventory:ConsumeFamiliars`

```text
oc !c -Consume_Familiars igw:${Me.Name}
```

### `-Consume_Status_Ingots`

`-Consume_Status_Ingots <who> <value>`

Also: `-Consume_Status_Ignots`

Consumes Ingots.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string | `99999` | How Many to consume |

Runs: `OgreBotAPI.Inventory:ConsumeStatusIngots`

```text
oc !c -Consume_Status_Ingots igw:${Me.Name} 10
```

### `-Consume_Status_Tokens`

`-Consume_Status_Tokens <who> <value>`

Consumes Status Tokens.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string | `99999` | How Many to consume |

Runs: `OgreBotAPI.Inventory:ConsumeStatusTokens`

```text
oc !c -Consume_Status_Tokens igw:${Me.Name} 10
```

### `-ConsumeItems_ProcessList_AP`

`-ConsumeItems_ProcessList_AP <who> <args>`

Uses the items on your profile's Consume Items tab, top to bottom, skipping disabled rows, in-combat-only rows out of combat, items on their snack timer and items not ready; it stops after the first item used unless -all is given. -fc ignores the in-combat-only marks and the in-combat throttle, and -st ignores the snack timers.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `args` | rest |  |  |

Runs: `OgreBotAPI.Inventory:ConsumeList`

```text
oc !c -ConsumeItems_ProcessList_AP igw:${Me.Name} -all -st
```

### `-ConversationBubble`

`-ConversationBubble <who> <num>`

Also: `-Conversation_Bubble`

After hailing you can use this to converse with an NPC.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `num` | string | `1` | chat option to choose |

Runs: `OgreBotAPI.Comms:ConversationBubble`

```text
oc !c -ConversationBubble igw:${Me.Name} 1
```

### `-countdown`

`-countdown <who> <time>`

Starts the in-game group countdown for the given number of seconds. Only a grouped group leader does it, everyone else does nothing, and a time of 0 or over 30 echoes an error instead.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `time` | string | `1` |  |

Runs: `OgreBotAPI.Combat:Countdown`

```text
oc !c -countdown ${Me.Name} 10
```

### `-CoV`

`-CoV <who> <traveloption> <toonoption> <allowsamezone>`

Uses Call of the Veteran.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `traveloption` | string | `Teleport` | TravelOption. Teleport or Summon |
| `toonoption` | string | `ToonName` | Toon to interact with |
| `allowsamezone` | string | `FALSE` | Allow Same zone |

Runs: `OgreBotAPI.Consumables:CoV`

```text
oc !c -CoV ${Me.Name} Summon ${Group[1].Name} FALSE
```

### `-Crouch`

`-Crouch <who>`

Presses the crouch key once.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Movement:Crouch`

```text
oc !c -Crouch igw:${Me.Name}
```

### `-CS_ClearAll`

`-CS_ClearAll <who>`

Clears Campspot data

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.CampSpot:ClearAll`

```text
oc !c -CS_ClearAll igw:${Me.Name}
```

### `-CS_ClearCampSpot`

`-CS_ClearCampSpot <who>`

Clears Campspot location only

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.CampSpot:ClearCampSpot`

```text
oc !c -CS_ClearCampSpot igw:${Me.Name}
```

### `-CS_ClearRelative`

`-CS_ClearRelative <who>`

Clears Relative data

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.CampSpot:ClearRelative`

```text
oc !c -CS_ClearRelative igw:${Me.Name}
```

### `-CS_Set_ChangeCampSpot`

`-CS_Set_ChangeCampSpot <who> <x> <y> <z>`

Changes the base campspot.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `x` | string | `${Me.X}` | X, or the name of a point of interest in this zone |
| `y` | string | `${Me.Y}` | Y |
| `z` | string | `${Me.Z}` | Z |

Runs: `OgreBotAPI.CampSpot:SetLoc`

```text
oc !c -CS_Set_ChangeCampSpot igw:${Me.Name} ${Me.X} ${Me.Y} ${Me.Z}
```

### `-CS_Set_ChangeCampSpotBy`

`-CS_Set_ChangeCampSpotBy <who> <x> <y> <z>`

Also: `-ccsbw`, `-ccsbfw`, `-ccsbyforwho`, `-ccsb`, `-ChangeCampSpotBy`, `-cs-set-ccs-by`

Changes the base campspot by.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `x` | string | `0` | X |
| `y` | string | `0` | Y |
| `z` | string | `0` | Z |

Runs: `OgreBotAPI.CampSpot:NudgeBy`

```text
oc !c -CS_Set_ChangeCampSpotBy igw:${Me.Name} 5 0 -5
```

### `-CS_Set_ChangeRelativeCampSpotBy`

`-CS_Set_ChangeRelativeCampSpotBy <who> <x> <y> <z>`

Changes the relative campspot by.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `x` | string | `0` | X delta to ADD to the relative campspot (0 = no change) |
| `y` | string | `0` | Y/height delta to add (0 = no change) |
| `z` | string | `0` | Z delta to add (0 = no change) |

Runs: `OgreBotAPI.CampSpot:SetRelativeBy`

```text
oc !c -CS_Set_ChangeRelativeCampSpotBy igw:${Me.Name} 0 0 10
```

### `-CS_Set_Formation_Circle`

`-CS_Set_Formation_Circle <who> <distance> <x> <y> <z> <userelativecs>`

Also: `-cs-circle`

Creates a circle.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `distance` | float | `7` | Distance from center. Example: 7 |
| `x` | string | `${Me.X}` | X Position of Center, or the name of a point of interest in this zone. \${Me.X} is acceptable |
| `y` | string | `${Me.Y}` | Y Position of Center. \${Me.Y} is acceptable |
| `z` | string | `${Me.Z}` | Z Position of Center. \${Me.Z} is acceptable |
| `userelativecs` | bool | `FALSE` | Use Relative campspot instead of campspot: TRUE or FALSE. |

Runs: `OgreBotAPI.CampSpot:SetFormation`

```text
oc !c -CS_Set_Formation_Circle igw:${Me.Name} 7 ${Me.X} ${Me.Y} ${Me.Z} FALSE
```

### `-CS_Set_Formation_MonkeyInMiddle`

`-CS_Set_Formation_MonkeyInMiddle <who> <distance> <x> <y> <z> <middleman> <userelativecs>`

Also: `-cs-monkey`

Creates a circle with one person in the middle.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `distance` | float | `7` | Distance from center. Example: 7 |
| `x` | string | `${Me.X}` | X Position of Center, or the name of a point of interest in this zone. \${Me.X} is acceptable |
| `y` | string | `${Me.Y}` | Y Position of Center. \${Me.Y} is acceptable |
| `z` | string | `${Me.Z}` | Z Position of Center. \${Me.Z} is acceptable |
| `middleman` | string | `${Me.Name}` | Who will be in the middle. \${Me.Name} is acceptable |
| `userelativecs` | bool | `FALSE` | Use Relative campspot instead of campspot: TRUE or FALSE. |

Runs: `OgreBotAPI.CampSpot:SetFormation`

```text
oc !c -CS_Set_Formation_MonkeyInMiddle igw:${Me.Name} 7 ${Me.X} ${Me.Y} ${Me.Z} ${Me.Name} FALSE
```

### `-CS_Set_Formation_MonkeyInMiddleRaid`

`-CS_Set_Formation_MonkeyInMiddleRaid <who> <middleforwho> <distance> <x> <y> <z> <circlespots> <userelativecs>`

Also: `-cs-monkeyRaid`

Gives each matched toon its own spot on a ring of circlespots spots (default 5, placed by raid order) at distance (default 7) around x y z, while the toons middleforwho matches stand on the centre. userelativecs TRUE sets the relative campspot instead of the base one, and nothing is set (a console line says so) while OgreBot is not open.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `middleforwho` | string |  |  |
| `distance` | float | `7` |  |
| `x` | string | `${Me.X}` | X, or the name of a point of interest in this zone |
| `y` | string | `${Me.Y}` |  |
| `z` | string | `${Me.Z}` |  |
| `circlespots` | string | `5` |  |
| `userelativecs` | bool | `FALSE` |  |

Runs: `OgreBotAPI.CampSpot:SetFormation`

```text
oc !c -CS_Set_Formation_MonkeyInMiddleRaid all igw:${Me.Name} 15 ${Me.X} ${Me.Y} ${Me.Z} 5 FALSE
```

### `-CS_Set_HowClose`

`-CS_Set_HowClose <who> <value>`

Changes the HowClose for CampSpot

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | float | `1` | HowClose |

Runs: `OgreBotAPI.CampSpot:SetHowClose`

```text
oc !c -CS_Set_HowClose igw:${Me.Name} 3
```

### `-CS_Set_HowFar`

`-CS_Set_HowFar <who> <value>`

Changes the HowFar for CampSpot

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | float | `200` | HowFar |

Runs: `OgreBotAPI.CampSpot:SetHowFar`

```text
oc !c -CS_Set_HowFar igw:${Me.Name} 200
```

### `-CS_Set_Relative`

`-CS_Set_Relative <who> <x> <y> <z>`

Sets the relative camp spot to this location (an absolute location, not an offset; -CS_Set_ChangeRelativeCampSpotBy moves it by an offset).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `x` | string | `${Me.X}` | X of the flat relative campspot (absolute coordinate, NOT a diff/offset) |
| `y` | string | `${Me.Y}` | Y/height of the flat relative campspot (absolute, not a diff) |
| `z` | string | `${Me.Z}` | Z of the flat relative campspot (absolute, not a diff) |

Runs: `OgreBotAPI.CampSpot:SetRelativeLoc`

```text
oc !c -CS_Set_Relative igw:${Me.Name} ${Me.X} ${Me.Y} ${Me.Z}
```

### `-CurePotions_Replenish`

`-CurePotions_Replenish <who> <potion>`

Replenishes cure potions from the depot. Default is all. Other options are: Arcane, Trauma, Noxious, Elemental. All other options will be assumed to be the full name.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `potion` | string | `all` | Optional. Which cure: all, arcane, elemental, noxious or trauma. |

Runs: `OgreBotAPI.Cures:ReplenishPotions`

```text
oc !c -CurePotions_Replenish igw:${Me.Name} trauma
```

### `-DeleteQuest`

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

### `-DestroyItem`

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

### `-DestroyItem_NoChecks`

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

### `-Disable_Dispells`

`-Disable_Dispells <who>`

Ticks the No Dispels setting, so the bot stops casting dispels.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Abilities:SetDispellsEnabled`

```text
oc !c -Disable_Dispells igw:${Me.Name}
```

### `-Disable_Interrupts`

`-Disable_Interrupts <who>`

Ticks the No Interrupts setting, and on a Rogue also turns Daring Advance off in the cast stack and cancels it.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Abilities:SetInterruptsEnabled`

```text
oc !c -Disable_Interrupts igw:${Me.Name}
```

### `-Disband`

`-Disband <who>`

Disband your group.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Roster:Disband`

```text
oc !c -Disband ${Me.Name}
```

### `-DispellNPCWithAny`

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

### `-DispellNPCWithItem`

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

### `-DispellNPCWithSpell`

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

### `-DisplayEtherealMissionInfo`

`-DisplayEtherealMissionInfo <who>`

Show which zones are hot right now, when they rotate, and what is next. Legacy name - use -DisplayHotZoneInfo.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Quest:ShowMissionInfo`

```text
oc !c -DisplayEtherealMissionInfo ${Me.Name}
```

### `-DisplayHotZoneInfo`

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

### `-DoHO_Reset`

`-DoHO_Reset <who>`

Clears the HO run record (target, completion count and options) without changing whether DoHO is enabled or its timeout.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.HOs:DoReset`

```text
oc !c -DoHO_Reset igw:${Me.Name}
```

### `-DoHO_Set_Enable`

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

### `-DoHO_Setup`

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

### `-DoNotMove`

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

### `-DoVDebuff`

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

### `-DoVDebuff_Half`

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

### `-Drink_Alcohol`

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

### `-DungeonMakerCancel`

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

### `-Enable_Dispells`

`-Enable_Dispells <who>`

Unticks the No Dispels setting, so the bot casts dispels again.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Abilities:SetDispellsEnabled`

```text
oc !c -Enable_Dispells igw:${Me.Name}
```

### `-Enable_Interrupts`

`-Enable_Interrupts <who>`

Unticks the No Interrupts setting and turns Daring Advance on in the cast stack.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Abilities:SetInterruptsEnabled`

```text
oc !c -Enable_Interrupts igw:${Me.Name}
```

### `-End_Bot`

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

### `-EndScriptOB`

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

### `-EquipCharm`

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

### `-evac`

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

### `-ExamineAllOfItem`

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

### `-ExamineInventoryItem`

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

### `-ExecuteEvent_AP`

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

### `-ExitClient`

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

### `-F2PWindow_Check`

`-F2PWindow_Check <who>`

Closes the All-Access (F2P) upsell window once if it is showing, with a console note. Does nothing when the window is not up.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Windows:F2PWindowCheck`

```text
oc !c -F2PWindow_Check all
```

### `-F2PWindow_SetOptions`

`-F2PWindow_SetOptions <who>`

Turns on the watcher that closes the All Access upsell window (Settings tab: Close F2P upsell window).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI:F2PWindow_SetOptions`

```text
oc !c -F2PWindow_SetOptions all
```

### `-FaceActor`

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

### `-FaceAngle`

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

### `-FaceLoc`

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

### `-FastTravel`

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

### `-FlagToon`

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

### `-FlyDown`

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

### `-FlyStop`

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

### `-FlyUp`

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

### `-FoodDrink_AutoConsume`

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

### `-FoodDrink_Replenish`

`-FoodDrink_Replenish <who>`

Replenishes food and drink from inventory and depot.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Consumables:ReplenishFoodDrink`

```text
oc !c -FoodDrink_Replenish igw:${Me.Name}
```

### `-Force_MountOff`

`-Force_MountOff <who>`

Will dismount you. The down half of Force_MountOn.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Consumables:MountDown`

```text
oc !c -Force_MountOff igw:${Me.Name}
```

### `-Force_MountOn`

`-Force_MountOn <who>`

Will cancel and recast your mount.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Consumables:MountUp`

```text
oc !c -Force_MountOn igw:${Me.Name}
```

### `-ForceAliasUpdate`

`-ForceAliasUpdate <who>`

Drops the cached alias answers on the matched toons, so the next *alias is worked out against the group and raid as they are now.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.ForWho:ForceUpdate`

```text
oc !c -ForceAliasUpdate all
```

### `-forcefollow`

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

### `-GetFlag`

`-GetFlag <who>`

Gets a flag from a guild strategist.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI:GetFlag`

```text
oc !c -GetFlag igw:${Me.Name}
```

### `-GetToConcentration`

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

### `-GetToGH`

`-GetToGH <who>`

Gets you to GH. Using call to GH or call to home or fast travel.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Movement:GetToGH`

```text
oc !c -GetToGH igw:${Me.Name}
```

### `-GroupCure`

`-GroupCure <who>`

Asks the matched toons for an immediate group cure: within the next 2 seconds they cast their class group cure if at least one group member is afflicted.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Cures:RequestGroup`

```text
oc !c -GroupCure igw:${Me.Name}
```

### `-Hail`

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

### `-Heartstone_RekindleBond`

`-Heartstone_RekindleBond <who>`

Will use the Heartstone to rekindle your bond.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Consumables:RekindleHeartstone`

```text
oc !c -Heartstone_RekindleBond ${Me.Name}
```

### `-HO_Cancel_Starter`

`-HO_Cancel_Starter <who>`

Cancels the open Heroic Opportunity starter selection. Nothing happens when no HO starter is showing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.HOs:CancelStarter`

```text
oc !c -HO_Cancel_Starter ${Me.Name}
```

### `-HO_Start`

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

### `-HO_Starter_Advance`

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

### `-HO_Wheel_Advance`

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

### `-holdup`

`-holdup <who>`

Pauses follow and stops the current move. The leader is kept: LetsGo or a new follow resumes it, and the camp spot still pulls the character back.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Movement:StopFollow`

```text
oc !c -holdup igw:${Me.Name}
```

### `-ImmRes`

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

### `-InjectChat`

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

### `-InputTextWindow_Accept`

`-InputTextWindow_Accept <who>`

Clicks the accept button of the text-entry popup on screen. Nothing happens when that popup is not showing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Windows:InputTextAccept`

```text
oc !c -InputTextWindow_Accept igw:${Me.Name}
```

### `-InputTextWindow_AddText`

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

### `-InputTextWindow_ClearText`

`-InputTextWindow_ClearText <who>`

Empties the input box of the text-entry popup on screen. Nothing happens when that popup is not showing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Windows:InputTextClear`

```text
oc !c -InputTextWindow_ClearText igw:${Me.Name}
```

### `-Invite`

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

### `-Inviter`

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

### `-ItemEmbargo`

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

### `-joustin`

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

### `-joustoff`

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

### `-jouston`

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

### `-joustout`

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

### `-Jump`

`-Jump <who>`

Presses the jump key once.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Movement:Jump`

```text
oc !c -Jump igw:${Me.Name}
```

### `-Kick`

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

### `-LandFlyingMount`

`-LandFlyingMount <who>`

Holds the fly-down key until the toon has landed its flying mount, for up to 60 seconds, then releases the key. It runs as a queued action and does nothing outside the world.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Movement:LandFlyingMount`

```text
oc !c -LandFlyingMount igw:${Me.Name}
```

### `-letsgo`

`-letsgo <who>`

This button removes movement restrictions such as HoldUp and campspot.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.CampSpot:Release`

```text
oc !c -letsgo igw:${Me.Name}
```

### `-LoadAutoTargetList`

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

### `-LoadBot`

`-LoadBot <who>`

Loads OgreBot (starts it if it is not running).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Bot:Load`

```text
oc !c -LoadBot igw:${Me.Name}
```

### `-LoadProfile`

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

### `-LogToonIn`

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

### `-LootAll`

`-LootAll <who>`

Clicks Loot All on the loot window of the matched toons. It does nothing on a toon with no loot window open.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Loot:LootAll`

```text
oc !c -LootAll ${Me.Name}
```

### `-MakeLeader`

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

### `-MarkToon`

`-MarkToon <who>`

Marks each selected character (the same as setting flag 24).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Roster:Mark`

```text
oc !c -MarkToon ${Me.Name}
```

### `-Mentor`

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

### `-Mercenary_AddMercenaries`

`-Mercenary_AddMercenaries <who>`

Adds every Mercenary item in your bags, Overseer bag and harvest bag.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Consumables:AddMercenaries`

```text
oc !c -Mercenary_AddMercenaries ${Me.Name}
```

### `-Message`

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

### `-Message_Relay`

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

### `-Move2Area`

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

### `-MoveToAreaNoTarget`

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

### `-NavStop`

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

### `-NavTo`

`-NavTo <who> <x> <y> <z> <fly>`

Also: `-nav-to`, `-nav_to`

Nav (the mesh router) to an x y z, or to a point of interest in this zone. It waits while OgreBot is paused and stops when OgreBot closes. It leaves an encounter's trip alone.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who navs - leave blank to use the For Who window. |
| `x` | string |  | X, or the name of a point of interest in this zone |
| `y` | float |  |  |
| `z` | float |  |  |
| `fly` | string | `nofly` | fly flies the trip; nofly walks it. |

Runs: `OgreBotAPI.Movement:NavTo`

```text
oc !c -NavTo igw:${Me.Name} 120.5 -14 380.25 nofly
```

### `-NoTarget`

`-NoTarget <who>`

Clears everyones target. Useful to stop come2me.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI:NoTarget`

```text
oc !c -NoTarget igw:${Me.Name}
```

### `-ofol---`

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

### `-OFolIncDistance`

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

### `-OgreBotAPI`

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

### `-OgreBotToggleConsoleWindow`

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

### `-OgreCommandOB_AP`

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

### `-OgreConsole_Show`

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

### `-OgreCraft_AddLastScribedRecipe`

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

### `-OgreCraft_AddRecipe`

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

### `-OgreCraft_CompleteNavigation`

`-OgreCraft_CompleteNavigation <who>`

Scripters: tell a waiting craft that your script moved it (it re-checks the distance).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Craft:CompleteNavigation`

```text
oc !c -OgreCraft_CompleteNavigation ${Me.Name}
```

### `-OgreCraft_CraftQueue`

`-OgreCraft_CraftQueue <who>`

Start crafting the queue.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Craft:Start`

```text
oc !c -OgreCraft_CraftQueue ${Me.Name}
```

### `-OgreCraft_DeferNavigation`

`-OgreCraft_DeferNavigation <who>`

Scripters: hand a waiting craft walk back to craft (it moves itself).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Craft:DeferNavigation`

```text
oc !c -OgreCraft_DeferNavigation ${Me.Name}
```

### `-OgreCraft_ScribeRecipe`

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

### `-OgreCraft_StartLLL`

`-OgreCraft_StartLLL <who>`

Start Low Level Leveling - the Low Level Leveling tab settings.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Craft:StartLLL`

```text
oc !c -OgreCraft_StartLLL ${Me.Name}
```

### `-OgreCraft_StartQuest`

`-OgreCraft_StartQuest <who>`

Craft the current quest’s recipe steps - one of each per pass, re-reading the quest, until none is pending.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Craft:StartQuest`

```text
oc !c -OgreCraft_StartQuest ${Me.Name}
```

### `-OgreCraft_StartTinker`

`-OgreCraft_StartTinker <who>`

Start Auto Tinkering - the Auto Tinkering tab settings.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Craft:StartTinker`

```text
oc !c -OgreCraft_StartTinker ${Me.Name}
```

### `-OgreCraft_StartWrits`

`-OgreCraft_StartWrits <who>`

Start crafting writs (rush orders) - the Writs tab settings.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Craft:StartWrits`

```text
oc !c -OgreCraft_StartWrits ${Me.Name}
```

### `-OgreCraft_Stop`

`-OgreCraft_Stop <who>`

Stop the crafting run (queue, writs, quest, Low Level Leveling or Auto Tinkering). With nothing running it says so and drops a pause.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Craft:Stop`

```text
oc !c -OgreCraft_Stop ${Me.Name}
```

### `-ogrefollow`

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

### `-OgreZoneForceReset`

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

### `-OK_Button`

`-OK_Button <who>`

Presses OK to a pop up that has OK.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Windows:OK`

```text
oc !c -OK_Button igw:${Me.Name}
```

### `-OpenAndBuyFromMerchant`

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

### `-OpenAndBuyFromMerchantXTimes`

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

### `-Overseer_AddAgentsToCollection`

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

### `-Overseer_AutoAddOverseerQuests`

`-Overseer_AutoAddOverseerQuests <who>`

Uses the Overseer mission scrolls in your bags to add their quests to your Overseer quest list.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Overseer:AutoAddQuests`

```text
oc !c -Overseer_AutoAddOverseerQuests ${Me.Name}
```

### `-Overseer_BuyMissions`

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

### `-Overseer_CheckQuests`

`-Overseer_CheckQuests <who>`

Runs Overseer scan.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Overseer:CheckQuests`

```text
oc !c -Overseer_CheckQuests ${Me.Name}
```

### `-PackPony`

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

### `-Path`

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

### `-PathStop`

`-PathStop <who>`

Stops the path being walked. The toon stands where it is.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Paths:Stop`

```text
oc !c -PathStop igw:${Me.Name}
```

### `-pause`

`-pause <who>`

Pauses all the bots.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Bot:Pause`

```text
oc !c -pause igw:${Me.Name}
```

### `-PetAssist`

`-PetAssist <who>`

Sends the game's pet autoassist command, so the pet assists its owner.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Pet:Assist`

```text
oc !c -PetAssist igw:${Me.Name}
```

### `-petattack`

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

### `-PetGetLost`

`-PetGetLost <who>`

Sends the game's pet get lost command, dismissing the toon's pet.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Pet:GetLost`

```text
oc !c -PetGetLost igw:${Me.Name}
```

### `-PetOff`

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

### `-POI_Add`

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

### `-Poison_AutoConsume`

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

### `-Poison_Replenish`

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

### `-PortalToGuildHall`

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

### `-ProvingGrounds_Exit`

`-ProvingGrounds_Exit <who>`

Exits Proving Grounds. If in a match will exit the match. If in the lobby will exit the lobby.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Windows:ProvingGroundsExit`

```text
oc !c -ProvingGrounds_Exit igw:${Me.Name}
```

### `-ProvingGrounds_Scoreboard_Close`

`-ProvingGrounds_Scoreboard_Close <who>`

Closes the Proving Grounds scoreboard.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Windows:ProvingGroundsScoreboardClose`

```text
oc !c -ProvingGrounds_Scoreboard_Close igw:${Me.Name}
```

### `-Pushover`

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

### `-Question`

`-Question <who>`

Collects the nearest `?` shiny within 10 meters. The harvest-node twin is -Resource.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Session:CollectShiny`

```text
oc !c -Question ${Me.Name}
```

### `-RaidAuth`

`-RaidAuth <who>`

Authorizes everyone in your raid to each other on their IRC bridges, and nobody outside it. Your bridge asks once; each PC in the raid answers once with -AIIR. Anyone in the raid may ask.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. Several characters on one PC still ask only once. |

Runs: `OgreBotAPI.Comms:IrcRaidAuth`

```text
oc !c -RaidAuth ${Me.Name}
```

### `-RaidInvite`

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

### `-RaidUnauth`

`-RaidUnauth <who>`

Every IRC bridge in your raid removes the nicks it authorized through Auth raid (or -AIIR) and says who. Nicks authorized by hand and the bridge's own nick stay.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. Several characters on one PC still ask only once. |

Runs: `OgreBotAPI.Comms:IrcRaidUnauth`

```text
oc !c -RaidUnauth ${Me.Name}
```

### `-RawCommandOB_AP`

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

### `-Rebuff`

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

### `-RedeemKrono`

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

### `-Reload_Bot`

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

### `-ReloadOgreIRC`

`-ReloadOgreIRC <who>`

Reloads the IRC config on the uplink and reconnects if already connected.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Comms:IrcReload`

```text
oc !c -ReloadOgreIRC all
```

### `-RemoveNoOffensiveOn`

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

### `-RepairGear`

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

### `-ReplyDialog`

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

### `-ReplyDialogClose`

`-ReplyDialogClose <who>`

Closes the reply dialog (the NPC conversation window) if one is open. Does nothing when none is open.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Windows:ReplyClose`

```text
oc !c -ReplyDialogClose igw:${Me.Name}
```

### `-Res`

`-Res <who>`

Turns ressing back on: unchecks Disable CS_Res, so the Cast Stack's Res entries run again.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Session:Res`

```text
oc !c -Res igw:${Me.Name}
```

### `-Research_Material_Check`

`-Research_Material_Check <who>`

Examines each Research Material item in your bags (Advancement, Companion, Mount, Tradeskill, Upgrade and General) and picks the first research option it offers. A type that shows No Eligible Research is skipped with a console line.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Util:CheckResearchMaterials`

```text
oc !c -Research_Material_Check ${Me.Name}
```

### `-ResetActorsLooted`

`-ResetActorsLooted <who>`

Ogrebot only tries to loot each chest once. This will reset it.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Loot:ResetLootedActors`

```text
oc !c -ResetActorsLooted igw:${Me.Name}
```

### `-ResetCameraAngle`

`-ResetCameraAngle <who>`

Resets your Camera Angle.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Client:ResetCamera`

```text
oc !c -ResetCameraAngle igw:${Me.Name}
```

### `-ResetZone`

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

### `-Resource`

`-Resource <who>`

Clicks the nearest Resource.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Session:Harvest`

```text
oc !c -Resource ${Me.Name}
```

### `-ResStone`

`-ResStone <who>`

Priests cast their resurrection stone spell. Other classes do nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Session:ResStone`

```text
oc !c -ResStone igw:${Me.Name}
```

### `-resume`

`-resume <who>`

Resumes all the bots.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Bot:Resume`

```text
oc !c -resume igw:${Me.Name}
```

### `-Revive`

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

### `-Run`

`-Run <who>`

Sets running. Presses the run toggle only if the character is walking.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Movement:SetRunMode`

```text
oc !c -Run igw:${Me.Name}
```

### `-RunScriptOB`

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

### `-Scribe_Empyral`

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

### `-ScrollOf`

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

### `-Select_Window_AP`

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

### `-Select_Window_Spew_AP`

`-Select_Window_Spew_AP <who>`

Lists the options of the select window on screen to the console, numbered from 1.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Windows:SelectSpew`

```text
oc !c -Select_Window_Spew_AP ${Me.Name}
```

### `-Select_Zone_Version`

`-Select_Zone_Version <who>`

Presses OK in the select zone version window. Designed specifically for BoL Heroics.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Zone:SelectVersion`

```text
oc !c -Select_Zone_Version igw:${Me.Name}
```

### `-SellToMerchant`

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

### `-Set_Allow_HOICon`

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

### `-Set_CameraPitch`

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

### `-Set_CampSpotJump_Handle`

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

### `-Set_Disable_HOICon`

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

### `-Set_DisableAllAOEs_AllParams`

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

### `-set_Internalvariable`

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

### `-set_variable`

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

### `-SetAccessLevel`

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

### `-SetAutoLootMode`

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

### `-SetCS_BehindNPC`

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

### `-SetCS_InFrontNPC`

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

### `-SetCS_NPC`

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

### `-SetCS_PositionNPC`

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

### `-SetNoDefensive`

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

### `-SetNoOffensive`

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

### `-SetNoReqBowAbilities`

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

### `-SetUpFor`

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

### `-ShareAllMissions`

`-ShareAllMissions <who>`

Shares all mission quests. Only shares if everyone in group is nearby.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Quest:ShareAllMissions`

```text
oc !c -ShareAllMissions ${Me.Name}
```

### `-ShareMission`

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

### `-ShareQuest`

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

### `-ShareQuestsForZone`

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

### `-ShowAvailableSetups`

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

### `-ShowWikiForQuest`

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

### `-SmartLoot_ReloadDataFromFile`

`-SmartLoot_ReloadDataFromFile <who>`

Re-reads the smart loot data (item loot limits and each character's loot counts) from file on the matched toons. While loot hand-outs are still in progress, the character counts wait until they finish.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Loot:Reload`

```text
oc !c -SmartLoot_ReloadDataFromFile all
```

### `-Special`

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

### `-SpecialZoneSpecific`

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

### `-Spew_BoZ_Research`

`-Spew_BoZ_Research <who>`

Opens the research window if it is not up, waits for it to fill, broadcasts every row as label -> status, then closes the window. It is queued behind other actions, and prints a console line when the window has no rows.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Debug:SpewResearchWindow`

```text
oc !c -Spew_BoZ_Research ${Me.Name}
```

### `-Spew_MissionTimerInfo_AP`

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

### `-Spew_RelayGroup`

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

### `-SpewFlags`

`-SpewFlags <who>`

Posts one OgreConsole line per flag this character holds, as '&lt;name> Flagged &lt;number>', and nothing when it holds none. A marked character also lists flag 24, because the mark is kept as flag 24.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Roster:SpewFlags`

```text
oc !c -SpewFlags igw:${Me.Name}
```

### `-SpewStat`

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

### `-SpewSubscriptionStatus`

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

### `-stand`

`-stand <who>`

If you are FD you will stand up.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Movement:Stand`

```text
oc !c -stand igw:${Me.Name}
```

### `-StatPotions_AutoConsume`

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

### `-StatPotions_Replenish`

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

### `-StopRes`

`-StopRes <who>`

Turns ressing off: checks Disable CS_Res, so the Cast Stack's Res entries are skipped.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Session:StopRes`

```text
oc !c -StopRes igw:${Me.Name}
```

### `-Summon_Familiar`

`-Summon_Familiar <who>`

Summons your familiar.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Consumables:SummonFamiliar`

```text
oc !c -Summon_Familiar igw:${Me.Name}
```

### `-Target`

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

### `-targetlock`

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

### `-Tell`

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

### `-TempAdorns`

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

### `-ThreatFighterIgnoreList_Add`

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

### `-ThreatFighterIgnoreList_Clear`

`-ThreatFighterIgnoreList_Clear <who>`

Empties the threat fighter ignore list.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Combat:ThreatIgnoreClear`

```text
oc !c -ThreatFighterIgnoreList_Clear igw:${Me.Name}
```

### `-ThreatFighterIgnoreList_Remove`

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

### `-Timer`

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

### `-ToggleMainWindow`

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

### `-ToggleZoneReset`

`-ToggleZoneReset <who>`

Loads the Zone Reuse window and reads its table, so the zone reset timers are known and ${OgreBotAPI.Zone.ResetZoneData} can answer. Despite the name it is not a toggle: the window ends closed.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Zone:ResetUpdateInfo`

```text
oc !c -ToggleZoneReset igw:${Me.Name}
```

### `-ToonMarked`

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

### `-Travel`

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

### `-TravelBell`

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

### `-TravelDruid`

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

### `-TravelMesh`

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

### `-TravelMeshFeatures`

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

### `-TravelMeshGroup`

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

### `-TravelMeshPreview`

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

### `-TravelMeshStop`

`-TravelMeshStop <who>`

Stops the travel mesh route in progress.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Travel:MeshStop`

```text
oc !c -TravelMeshStop igw:${Me.Name}
```

### `-TravelSpires`

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

### `-TTS`

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

### `-UnflagAll`

`-UnflagAll <who>`

Removes all Flags designation from characters.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Roster:UnflagAll`

```text
oc !c -UnflagAll igw:${Me.Name}
```

### `-UnflagToon`

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

### `-UnmarkToon`

`-UnmarkToon <who>`

Removes the mark (flag 24) from each selected character.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Roster:Unmark`

```text
oc !c -UnmarkToon ${Me.Name}
```

### `-Unmentor`

`-Unmentor <who>`

Tells [Bots] to unmentor.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Roster:Unmentor`

```text
oc !c -Unmentor igw:${Me.Name}
```

### `-Unpack`

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

### `-Unpack_Consume_Familiars`

`-Unpack_Consume_Familiars <who>`

Unpacks and adds Familiars to collection if possible otherwise consumes for experience.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Inventory:UnpackConsumeFamiliars`

```text
oc !c -Unpack_Consume_Familiars igw:${Me.Name}
```

### `-Unpack_Familiars`

`-Unpack_Familiars <who>`

Unpacks Familiars.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Inventory:UnpackFamiliars`

```text
oc !c -Unpack_Familiars igw:${Me.Name}
```

### `-UpgradeItem`

`-UpgradeItem <who>`

Upgrades a piece of gear: put the old item in bag 1 slot 1 and the new one in bag 1 slot 2. The old item's adornments are moved onto the new one, the old item goes to the end of bag 1, and the new one is equipped. Both must be for the same slot, and the new one must have no adornments yet.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Inventory:UpgradeItem`

```text
oc !c -UpgradeItem ${Me.Name}
```

### `-UplinkOptionChange`

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

### `-UplinkOptionSilent`

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

### `-UseFlag`

`-UseFlag <who>`

Uses a flag from a guild strategist.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI:UseFlag`

```text
oc !c -UseFlag igw:${Me.Name}
```

### `-UseItem`

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

### `-UseItemOnPlayer`

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

### `-Walk`

`-Walk <who>`

Sets walking. Presses the run toggle only if the character is running.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Movement:SetRunMode`

```text
oc !c -Walk igw:${Me.Name}
```

### `-WarnBeforeSave`

`-WarnBeforeSave <who>`

Marks that the Instance Controller has run on these characters, so the OgreBot window warns before saving the profile (cleared when a profile is loaded).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Options:WarnBeforeSave`

```text
oc !c -WarnBeforeSave igw:${Me.Name}
```

### `-Waypoint`

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

### `-Zone`

`-Zone <who>`

Will attempt to zone you.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Zone:Zone`

```text
oc !c -Zone igw:${Me.Name}
```

### `-ZoneDoor`

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

### `-ZoneResetAll`

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
