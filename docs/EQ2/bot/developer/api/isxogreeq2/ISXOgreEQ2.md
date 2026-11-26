<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# ISXOgreEQ2

## Members

### `AbilityDetails`

`${ISXOgreEQ2.AbilityDetails}`

The AbilityDetails sub-object: the Ability Details window, which opens through OgreBotAPI.Abilities:AbilityDetails, not through this object. :Close closes it (ogre end abilitydetails) and :UI is the window's own click channel, which does nothing without its one argument.

All of it: [ISXOgreEQ2.AbilityDetails](AbilityDetails.md)

**Returns:** object: the AbilityDetails sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.AbilityDetails.

```text
echo ${ISXOgreEQ2.AbilityDetails}
```

### `AbilityEfficiency`

`${ISXOgreEQ2.AbilityEfficiency}`

The AbilityEfficiency sub-object behind ogre ae: :Run opens the Ability Efficiency window (each damaging ability's damage per second, one column per number of targets), :Run[-nogui] writes the report file instead, :Run[-targets,n] sets the targets, :Run[-list] uses the list layout, :Close closes the window, and the window's own :UI channel. It has no members.

All of it: [ISXOgreEQ2.AbilityEfficiency](AbilityEfficiency.md)

**Returns:** object: the AbilityEfficiency sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.AbilityEfficiency.

```text
echo ${ISXOgreEQ2.AbilityEfficiency}
```

### `AbilityUpgrades`

`${ISXOgreEQ2.AbilityUpgrades}`

The AbilityUpgrades sub-object behind ogre oau: :Run[minLevel] reports which Scroll Depot scrolls would upgrade an ability you know, from the given minimum scroll level (a default when left out), and :Run[-h] prints the usage. It only reports, buys nothing, and has no members.

All of it: [ISXOgreEQ2.AbilityUpgrades](AbilityUpgrades.md)

**Returns:** object: the AbilityUpgrades sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.AbilityUpgrades.

```text
echo ${ISXOgreEQ2.AbilityUpgrades}
```

### `Analysis`

`${ISXOgreEQ2.Analysis}`

The Analysis sub-object behind ogre analysis: watches actors, records what changes and when, and scans a zone for actors that match. Its methods are :Open, :Close, :End, :Status, :Demo, :Rate, :Taps, :Monitor, :Scan, :Sessions, :Export, :Import and the panel's :UI, and it has no members.

All of it: [ISXOgreEQ2.Analysis](Analysis.md)

**Returns:** object: the Analysis sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.Analysis.

```text
echo ${ISXOgreEQ2.Analysis}
```

### `AntiAfk`

`${ISXOgreEQ2.AntiAfk}`

The AntiAfk sub-object behind ogre afk: :On[1\|0] starts a /who at random long intervals so the character is not idle (1 silent, 0 with messages, nothing keeps the current setting) and :Off stops it. :Invites[on\|off] is a separate switch that auto-accepts group invites from characters on your own accounts, :Help prints the usage, and it has no members.

All of it: [ISXOgreEQ2.AntiAfk](AntiAfk.md)

**Returns:** object: the AntiAfk sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.AntiAfk.

```text
echo ${ISXOgreEQ2.AntiAfk}
```

### `Auth`

`${ISXOgreEQ2.Auth}`

The Auth sub-object: this session's login name, relay group and access level, with Spew to print them.

All of it: [ISXOgreEQ2.Auth](Auth.md)

**Returns:** object: the Auth sub-object; it always exists, and as text it reads ISXOgreEQ2.Auth.

```text
echo ${ISXOgreEQ2.Auth}
```

### `AutoLogin`

`${ISXOgreEQ2.AutoLogin}`

The auto-login settings window: :Open / :Close / :Toggle show it, and the window's own buttons save, delete or start login profiles and make desktop shortcuts for them. Echoing the object prints ISXOgreEQ2.AutoLogin.

All of it: [ISXOgreEQ2.AutoLogin](AutoLogin.md)

**Returns:** object: the auto-login settings window (type ogreeq2autologin); methods only

```text
echo ${ISXOgreEQ2.AutoLogin}
```

### `BgRender`

`${ISXOgreEQ2.BgRender}`

The BgRender sub-object behind ogre bgrender: while this client is not the foreground window it skips the game's drawing except once a second and caps the background loop, so a background session uses much less CPU and GPU while the bot, the network and scripts keep running. It is off when the extension loads and never skips while you are logging in, zoning, camping or at character select.

All of it: [ISXOgreEQ2.BgRender](BgRender.md)

**Returns:** object: the BgRender sub-object; it always exists, and as text it reads ISXOgreEQ2.BgRender.

```text
echo ${ISXOgreEQ2.BgRender}
```

### `BuildHash`

`${ISXOgreEQ2.BuildHash}`

The fingerprint of the ISXOgreEQ2 file this session loaded: the SHA-256 of its code section as 64 hex characters, the same value the session log's first adapter line shows. Two sessions that show the same value run the same build.

**Returns:** string: 64 hex characters, or NULL if the file could not be read

```text
echo ${ISXOgreEQ2.BuildHash}
```

### `Chat`

`${ISXOgreEQ2.Chat}`

Read-only counters for incoming chat handling: .Lines, .Hits, .Subscribers and per-source counts such as .TellReceived and .TellSent. Echoing the object prints a one-line summary (lines, hits, subscribers).

All of it: [ISXOgreEQ2.Chat](Chat.md)

**Returns:** object: chat handling counters (type ogreeq2chat); members only

```text
echo ${ISXOgreEQ2.Chat}
```

### `ChatCmd`

`${ISXOgreEQ2.ChatCmd}`

The ChatCmd sub-object: the chat commands your own characters send you, off until :On. Its methods are :On, :Off, :Debug, :ReloadAuth, :Test and :Status, and `ogre chatcmd` types them.

All of it: [ISXOgreEQ2.ChatCmd](ChatCmd.md)

**Returns:** object: the ChatCmd sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.ChatCmd.

```text
echo ${ISXOgreEQ2.ChatCmd}
```

### `Class`

`${ISXOgreEQ2.Class}`

Your character's class identity: .Archetype, .ClassTier, .Subclass, .Is[&lt;name>] and the server ruleset flags, with :Update to recompute them from the game. Echoing the object prints ISXOgreEQ2.Class.

All of it: [ISXOgreEQ2.Class](Class.md)

**Returns:** object: your class identity (type ogreeq2class)

```text
echo ${ISXOgreEQ2.Class}
```

### `Codex`

`${ISXOgreEQ2.Codex}`

The Codex sub-object behind ogre codextoon and ogre codexinspect: :Toon uploads your own gear and stats to eq2codex, :Inspect[names] inspects and uploads each named character, and :End stops an inspect pass. Uploads need the codex address and token set up; without them it reports that it is not configured.

All of it: [ISXOgreEQ2.Codex](Codex.md)

**Returns:** object: the Codex sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.Codex.

```text
echo ${ISXOgreEQ2.Codex}
```

### `Collection`

`${ISXOgreEQ2.Collection}`

The Collection sub-object behind ogre cm: :Run adds collectibles to your collection journal, from the depot by default (-small or -large picks the depot) or from your bags with -inventory, and :Stop stops it. Its members Running and Status report the run.

All of it: [ISXOgreEQ2.Collection](Collection.md)

**Returns:** object: the Collection sub-object; it always exists, and as text it reads its status line - "idle", "cm (&lt;n>/&lt;total>, &lt;N> added)" or "cm -inventory (&lt;n>/&lt;total>, &lt;N> added)".

```text
echo ${ISXOgreEQ2.Collection}
```

### `Commands`

`${ISXOgreEQ2.Commands}`

The Commands sub-object: the Commands panel that ogre commands, ogre help or a bare question mark after ogre opens. :Open and :Close show and hide it, and :UI is the panel's own click channel, which does nothing without its one argument.

All of it: [ISXOgreEQ2.Commands](Commands.md)

**Returns:** object: the Commands sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.Commands.

```text
echo ${ISXOgreEQ2.Commands}
```

### `ContentBuilder`

`${ISXOgreEQ2.ContentBuilder}`

The Content Builder window: it draws a zone file or a fight file as boxes and edits it. Its methods open and close the window.

All of it: [ISXOgreEQ2.ContentBuilder](ContentBuilder.md)

**Returns:** The Content Builder object. As text it reads "ISXOgreEQ2.ContentBuilder".

```text
ISXOgreEQ2.ContentBuilder:Open
```

More: [developer/zone-files/builder.md](../../zone-files/builder.md)

### `CoreBuildHash`

`${ISXOgreEQ2.CoreBuildHash}`

The fingerprint of the ISXOgreX file this session loaded, read the same way as BuildHash and shown on the same log line.

**Returns:** string: 64 hex characters, or NULL if the file could not be read

```text
echo ${ISXOgreEQ2.CoreBuildHash}
```

### `Craft`

`${ISXOgreEQ2.Craft}`

The crafting engine and its window: .Running, .Status, .Crafted and .Setting[&lt;id>] read it, and :Open, :Start, :StartWrits, :Stop and :AddRecipe[...] drive it. OgreBotAPI.Craft has the for-who versions of the starts and recipe adds (no Stop); echoing the object prints "&lt;flow>/&lt;status> &lt;crafted> of &lt;total>", such as "queue/crafting Tempered Iron 3 of 10".

All of it: [ISXOgreEQ2.Craft](Craft.md)

**Returns:** object: the crafting engine (type ogreeq2craft)

```text
echo ${ISXOgreEQ2.Craft}
```

### `CraftGm`

`${ISXOgreEQ2.CraftGm}`

The CraftGm sub-object behind ogre craftgm: turns the (Master) spell scrolls you carry into queued (Grandmaster) crafts. Its methods are :Open, :Scan, :Start, :Status, :Stop, :End and :Close, which take the words the command does, and it has no members.

All of it: [ISXOgreEQ2.CraftGm](CraftGm.md)

**Returns:** object: the CraftGm sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.CraftGm.

```text
echo ${ISXOgreEQ2.CraftGm}
```

### `CraftingMats`

`${ISXOgreEQ2.CraftingMats}`

The CraftingMats sub-object behind the ogre craftingmats command: it pulls the materials a signature, daily or weekly craft needs out of the Harvesting Supply Depot. It has the members Lists, Keys and Warnings and the methods :Get, :Plan, :Reload, :Help, :Open, :UI and :End.

All of it: [ISXOgreEQ2.CraftingMats](CraftingMats.md)

**Returns:** object: the CraftingMats sub-object; it always exists, and as text it reads "&lt;N> lists (&lt;keys>)" - how many list files are loaded and their expansion keys.

```text
echo ${ISXOgreEQ2.CraftingMats}
```

### `DepotTransfer`

`${ISXOgreEQ2.DepotTransfer}`

The DepotTransfer sub-object behind ogre housetogh, ogre ghtohouse and ogre smalldepottobigdepot: one bulk depot transfer with three directions (:HouseToGH, :GHToHouse, :SmallToLarge) and :Stop. Each method only starts the transfer, which runs on the pulse and zones through the Portal to Housing and the guild hall Magic Door as needed; Running and Status report it.

All of it: [ISXOgreEQ2.DepotTransfer](DepotTransfer.md)

**Returns:** object: the DepotTransfer sub-object; it always exists, and as text it reads its status line - "idle", or "&lt;depot> (&lt;n>/&lt;total>, &lt;N> pulled)" while a transfer runs.

```text
echo ${ISXOgreEQ2.DepotTransfer}
```

### `Det`

`${ISXOgreEQ2.Det}`

Detrimental effect lookups matched by an effect's main and backdrop icon ids: .DetrimentalInfo[...] and .DetrimentalInfo_JSON read one effect or all of yours, and :DetrimentalCancel / :DetrimentalCacheClear act on them. Echoing the object prints ISXOgreEQ2.Det.

All of it: [ISXOgreEQ2.Det](Det.md)

**Returns:** object: the detrimental effect lookups (type ogreeq2det)

```text
echo ${ISXOgreEQ2.Det}
```

### `EffectTracker`

`${ISXOgreEQ2.EffectTracker}`

The EffectTracker sub-object behind ogre effecttracker: captures what detrimental and NPC effects say they do into a dataset per zone. Its methods are :Open, :Close, :End, :On, :Off, :Npc, :Status, :Reload, :Trace, :Probe, :Bench, :UiDiag, :Demo, :CloseWindow, :Describe, :Merge and the panel's :UI, and it has no members.

All of it: [ISXOgreEQ2.EffectTracker](EffectTracker.md)

**Returns:** object: the EffectTracker sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.EffectTracker.

```text
echo ${ISXOgreEQ2.EffectTracker}
```

### `Encounter`

`${ISXOgreEQ2.Encounter}`

The encounter engine that runs the coded fights: .Loaded, .ActiveCount, .IsActive[&lt;mob>] and .Current read it, and :Reload, :Fire[&lt;mob>] and :List act on it. OgreBotAPI.Encounter is the for-who version of :List; echoing the object prints the loaded and active counts.

All of it: [ISXOgreEQ2.Encounter](Encounter.md)

**Returns:** object: the encounter engine (type ogreeq2encounter)

```text
echo ${ISXOgreEQ2.Encounter}
```

### `EncounterRecorder`

`${ISXOgreEQ2.EncounterRecorder}`

The Encounter Recorder: it records every fight as it happens, one file per box, so the fight can be worked out afterwards from the recording alone. Its methods are the words of `ogre er`.

All of it: [ISXOgreEQ2.EncounterRecorder](EncounterRecorder.md)

**Returns:** The Encounter Recorder object. As text it reads "ISXOgreEQ2.EncounterRecorder".

```text
ISXOgreEQ2.EncounterRecorder:Open
```

More: [developer/zone-files/recorder.md](../../zone-files/recorder.md)

### `Events`

`${ISXOgreEQ2.Events}`

Read-only counters for the game events the extension listens to: .Pending, .Dropped and per-event .Received[&lt;event>] / .Dispatched[&lt;event>] / .Subscribers[&lt;event>]. Echoing the object prints a one-line summary of the counters.

All of it: [ISXOgreEQ2.Events](Events.md)

**Returns:** object: game-event counters (type ogreeq2events); members only

```text
echo ${ISXOgreEQ2.Events}
```

### `Experiment`

`${ISXOgreEQ2.Experiment}`

The Experiment sub-object behind ogre experiment: it raises stats on the tradeskill Experiment tab. :Boost[-stat,n,...] works the item already selected, :Run[row,flags...] works a given item row, :Items lists the rows, and :Status and :Stop round it out; it has no members.

All of it: [ISXOgreEQ2.Experiment](Experiment.md)

**Returns:** object: the Experiment sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.Experiment.

```text
echo ${ISXOgreEQ2.Experiment}
```

### `Export`

`${ISXOgreEQ2.Export}`

The ability exporter: :Abilities[...] writes your abilities to a JSON file over several pulses, and :Config opens its options window (`ogre export`). .Busy is TRUE until the file is written and .Processed / .Total show progress; echoing the object prints ISXOgreEQ2.Export.

All of it: [ISXOgreEQ2.Export](Export.md)

**Returns:** object: the ability exporter (type ogreeq2export)

```text
echo ${ISXOgreEQ2.Export}
```

### `ForWhoGroups`

`${ISXOgreEQ2.ForWhoGroups}`

The ForWhoGroups sub-object behind ogre forwhogroups: named sets of toons you select with one for-who token. Its methods are :List, :Open, :Close, :Reload and the panel's own :UI channel, and it has no members.

All of it: [ISXOgreEQ2.ForWhoGroups](ForWhoGroups.md)

**Returns:** object: the ForWhoGroups sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.ForWhoGroups.

```text
echo ${ISXOgreEQ2.ForWhoGroups}
```

### `Game`

`${ISXOgreEQ2.Game}`

The game-client login and camp helper: :Login[character] logs that character in from the saved accounts, :Camp camps to the login screen and closes the session (:Camp[charselect] stops at character select), and :Abort stops either flow. .Busy and .State read where the flow is; echoing the object prints ISXOgreEQ2.Game.

All of it: [ISXOgreEQ2.Game](Game.md)

**Returns:** object: the login / camp helper (type ogreeq2game)

```text
echo ${ISXOgreEQ2.Game}
```

### `GetQuest`

`${ISXOgreEQ2.GetQuest}`

The GetQuest sub-object behind ogre getquest: :Start hails the NPC configured for this zone and takes its quest, deleting and retaking it until the wanted step comes up or the attempt limit runs out, and it does not walk, so stand next to the NPC first. The other methods are :Stop, :List, :Reload, :Status and :Help, and it has no members.

All of it: [ISXOgreEQ2.GetQuest](GetQuest.md)

**Returns:** object: the GetQuest sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.GetQuest.

```text
echo ${ISXOgreEQ2.GetQuest}
```

### `HarvestLite`

`${ISXOgreEQ2.HarvestLite}`

The HarvestLite sub-object behind ogre hl: while on, it harvests any resource node already within reach and lets go when something attacks you, and it never moves you. It starts off; :On, :Off, :Status and :Interval[ms] control it, and it has no members.

All of it: [ISXOgreEQ2.HarvestLite](HarvestLite.md)

**Returns:** object: the HarvestLite sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.HarvestLite.

```text
echo ${ISXOgreEQ2.HarvestLite}
```

### `Heartstone`

`${ISXOgreEQ2.Heartstone}`

The Heartstone sub-object behind ogre heartstone: on each zone-in it looks for a Heartstone and, when you are within 6 units of it, rekindles the bond every 15 to 30 minutes (random), whether or not OgreBot is running. It starts on; :On, :Off, :Now (try on the next pulse) and :Status control it, and it has no members.

All of it: [ISXOgreEQ2.Heartstone](Heartstone.md)

**Returns:** object: the Heartstone sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.Heartstone.

```text
echo ${ISXOgreEQ2.Heartstone}
```

### `HideEffects`

`${ISXOgreEQ2.HideEffects}`

The HideEffects sub-object behind ogre hideeffects: hides the listed junk effects on your character. Its methods are :Run, :List, :Clear, :Delete[id], :Open, :Reload, :Reset, :Status, :End and the panel's own :UI channel, and it has no members.

All of it: [ISXOgreEQ2.HideEffects](HideEffects.md)

**Returns:** object: the HideEffects sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.HideEffects.

```text
echo ${ISXOgreEQ2.HideEffects}
```

### `HUDs`

`${ISXOgreEQ2.HUDs}`

The on-screen HUD overlay, a click-through window showing the nearest NPC, group or raid member distances and timed raid messages. :Open / :Close show and hide it, :Set and :SetOption change it, and .Diag is a one-line status; echoing the object prints ISXOgreEQ2.HUDs.

All of it: [ISXOgreEQ2.HUDs](HUDs.md)

**Returns:** object: the HUD overlay (type ogreeq2huds)

```text
echo ${ISXOgreEQ2.HUDs}
```

### `IC`

`${ISXOgreEQ2.IC}`

The Instance Controller that runs zones from a list: .Running, .Zone, .Verdict and .Value[&lt;key>] read the run, and :Run, :RunList, :Stop, :Pause / :Resume and :Complete drive it. Echoing the object prints the engine state as JSON, not the run's values (read .Value for those).

All of it: [ISXOgreEQ2.IC](IC.md)

**Returns:** object: the Instance Controller (type ogreeq2ic)

```text
echo ${ISXOgreEQ2.IC}
```

### `InvOps`

`${ISXOgreEQ2.InvOps}`

The InvOps sub-object behind the ogre overflow, ogre mbc and ogre trade commands: :Overflow, :MoveBag and :Trade each only start a flow that then works one step per pulse, and :Stop drops whatever is running. Its members Busy and Status report the flow.

All of it: [ISXOgreEQ2.InvOps](InvOps.md)

**Returns:** object: the InvOps sub-object; it always exists, and as text it reads its status line - "idle", "overflow (&lt;N> popped)", "mbc (&lt;done>/&lt;total>)" or "trade (&lt;done>/&lt;total>)".

```text
echo ${ISXOgreEQ2.InvOps}
```

### `Lag`

`${ISXOgreEQ2.Lag}`

The Lag sub-object behind ogre lag: the frame ledger, every frame of the last few minutes with what it cost and what ran in it. Its methods are :Open, :Close, :Report, :Dump, :Minutes, :On, :Off, :Overhead, :Budget, :Clear and the window's own :UI channel, and it has no members.

All of it: [ISXOgreEQ2.Lag](Lag.md)

**Returns:** object: the Lag sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.Lag.

```text
echo ${ISXOgreEQ2.Lag}
```

### `LevelTransmuting`

`${ISXOgreEQ2.LevelTransmuting}`

The LevelTransmuting sub-object behind ogre leveltransmuting: buys transmuter's stones and transmutes them for skill-ups. Its methods are :Open, :On, :Off, :Status, :End and :Help, and it has no members.

All of it: [ISXOgreEQ2.LevelTransmuting](LevelTransmuting.md)

**Returns:** object: the LevelTransmuting sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.LevelTransmuting.

```text
echo ${ISXOgreEQ2.LevelTransmuting}
```

### `LootScan`

`${ISXOgreEQ2.LootScan}`

The LootScan sub-object: diagnostics for the auto-loot driver, which the Loot tab turns on. Its methods are :Status, :Interval and :Reset, and it has no members.

All of it: [ISXOgreEQ2.LootScan](LootScan.md)

**Returns:** object: the LootScan sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.LootScan.

```text
echo ${ISXOgreEQ2.LootScan}
```

### `MCP`

`${ISXOgreEQ2.MCP}`

The Master Control Panel window: open, close or toggle it, save or reload its button layout, fire a button by id and manage the key binds that press its buttons. Members .ForWho (the For Who in force on this session) and .IrcConnected read its state; echoing the object prints ISXOgreEQ2.MCP.

All of it: [ISXOgreEQ2.MCP](MCP.md)

**Returns:** object: the Master Control Panel (type ogreeq2mcp)

```text
echo ${ISXOgreEQ2.MCP}
```

### `MerchantCraft`

`${ISXOgreEQ2.MerchantCraft}`

The MerchantCraft sub-object behind ogre mc: it buys a merchant's limited recipes and crafts them. :List numbers the targeted merchant's recipes, :Start[recipe words,count] or :Start[#n,count] runs it, :Stop abandons it, and :Status and :Help round it out; it has no members.

All of it: [ISXOgreEQ2.MerchantCraft](MerchantCraft.md)

**Returns:** object: the MerchantCraft sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.MerchantCraft.

```text
echo ${ISXOgreEQ2.MerchantCraft}
```

### `MerchantOps`

`${ISXOgreEQ2.MerchantOps}`

The MerchantOps sub-object behind ogre buyfuel and ogre buycrate: :BuyFuel and :BuyCrate only start a merchant buy that runs on the pulse, and :Stop stops it. Its members Running and Status report the buy.

All of it: [ISXOgreEQ2.MerchantOps](MerchantOps.md)

**Returns:** object: the MerchantOps sub-object; it always exists, and as text it reads its status line - "idle", "buyfuel '&lt;fuel>' (round &lt;N>)" or "buycrate (&lt;n>/&lt;total>)".

```text
echo ${ISXOgreEQ2.MerchantOps}
```

### `Migrate`

`${ISXOgreEQ2.Migrate}`

The Migration Assistant, which copies OldBot settings (such as accounts, profiles, IRC, MCP and IM settings) into the new bot's files. :Open shows each task's status with a re-run button, and :Run re-runs one task; echoing the object prints ISXOgreEQ2.Migrate.

All of it: [ISXOgreEQ2.Migrate](Migrate.md)

**Returns:** object: the Migration Assistant (type ogreeq2migrate); methods only

```text
echo ${ISXOgreEQ2.Migrate}
```

### `Nav`

`${ISXOgreEQ2.Nav}`

Navigation inside the current zone over its navmesh: :To[x,y,z] starts a trip, :Stop ends it, :Set[&lt;key>,&lt;value>] changes a nav setting, and .NavActive / .NavState / .NavDistance follow the trip. Echoing the object prints the trip state and, when there is one, the reason.

All of it: [ISXOgreEQ2.Nav](Nav.md)

**Returns:** object: in-zone navigation (type ogreeq2nav)

```text
echo ${ISXOgreEQ2.Nav}
```

### `NpcCast`

`${ISXOgreEQ2.NpcCast}`

The NpcCast sub-object behind ogre npccast: the NPC cast watch list, its zone data and the cast Monitor. Its methods are :Open, :Status, :End, :Watch, :Unwatch, :Clear, :Radius, :Reload, :Capture, :Import, :Zone, :Monitor and the panel's :UI, and it has no members.

All of it: [ISXOgreEQ2.NpcCast](NpcCast.md)

**Returns:** object: the NpcCast sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.NpcCast.

```text
echo ${ISXOgreEQ2.NpcCast}
```

### `NPCTarget`

`${ISXOgreEQ2.NPCTarget}`

The NPC you are fighting, as an actor: your target when it is a live NPC or named NPC, otherwise your target's target when that is one. Worked out once per pulse while in the world; with no such NPC, or out of the world, the member does not exist, so check (exists) first.

**Returns:** actor: the current NPC kill target; does not exist when there is none. Out of the world it is not refreshed and keeps the last one.

```text
echo ${ISXOgreEQ2.NPCTarget.Name}
```

### `NPCTargetID`

`${ISXOgreEQ2.NPCTargetID}`

The actor id of the NPC you are fighting, picked the same way as ${ISXOgreEQ2.NPCTarget} once per pulse while in the world, and reads 0 out of the world. OgreBotAPI:UpdateNPCTarget refreshes it on demand and ${OgreBotAPI.ValidKillTarget} checks it.

**Returns:** int64: the kill target's actor id; 0 when there is no live NPC target. Out of the world it is not refreshed and keeps its last value.

```text
echo ${ISXOgreEQ2.NPCTargetID}
```

### `OgreBot`

`${ISXOgreEQ2.OgreBot}`

The OgreBot window and its profile settings: open and close the windows, load, create or save profiles, and read a setting with .Value[&lt;id>]. .IsReady is TRUE once a window is up and a profile is loaded; echoing the object prints ISXOgreEQ2.OgreBot.

All of it: [ISXOgreEQ2.OgreBot](OgreBot.md)

**Returns:** object: the OgreBot window and profile store (type ogreeq2ogrebot)

```text
echo ${ISXOgreEQ2.OgreBot}
```

### `OSA`

`${ISXOgreEQ2.OSA}`

The On-Screen Assistant, a window that lists the NPCs in range and targets one when you click its row. It has methods only (:Open, :Close, :Target[actorID]); echoing the object prints ISXOgreEQ2.OSA.

All of it: [ISXOgreEQ2.OSA](OSA.md)

**Returns:** object: the On-Screen Assistant (type ogreeq2osa); methods only

```text
echo ${ISXOgreEQ2.OSA}
```

### `Overseer`

`${ISXOgreEQ2.Overseer}`

The Overseer sub-object behind ogre overseer and ogre buyoverseermissions, for this session only (OgreBotAPI.Overseer is the one that takes a for-who). :Run, :Stop and :Status drive the daily Overseer run; :BuyMissions[flags...], :BuyMissionsStop and :BuyMissionsStatus drive the mission buy.

All of it: [ISXOgreEQ2.Overseer](Overseer.md)

**Returns:** object: the Overseer sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.Overseer.

```text
echo ${ISXOgreEQ2.Overseer}
```

### `PackPony`

`${ISXOgreEQ2.PackPony}`

The PackPony sub-object: one pack pony run, sent out and unloaded straight away. Its methods are :Start, :Stop and :Status, and it has no members; ogre packpony is the Task Runner, not this.

All of it: [ISXOgreEQ2.PackPony](PackPony.md)

**Returns:** object: the PackPony sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.PackPony.

```text
echo ${ISXOgreEQ2.PackPony}
```

### `Paths`

`${ISXOgreEQ2.Paths}`

The Paths sub-object behind ogre paths: the window that lists this zone's points of interest and saved paths. Its methods are :Open, :End and the window's own :UI channel, it has no members, and the walking verbs are OgreBotAPI.Paths.

All of it: [ISXOgreEQ2.Paths](Paths.md)

**Returns:** object: the Paths sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.Paths.

```text
echo ${ISXOgreEQ2.Paths}
```

### `Perf`

`${ISXOgreEQ2.Perf}`

The Perf sub-object behind ogre perf: :Measure[seconds,nothreads] measures the game's frame rate next to the time OgreBot's pulse takes, plus CPU and memory, and prints one report to the console. :Stop reports early and :Status says where a run stands, and it has no members.

All of it: [ISXOgreEQ2.Perf](Perf.md)

**Returns:** object: the Perf sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.Perf.

```text
echo ${ISXOgreEQ2.Perf}
```

### `Persona`

`${ISXOgreEQ2.Persona}`

The Persona sub-object behind `ogre persona`: the window that says which profile file each class uses on this PC. Its methods are :Open, :Close and the window's own :UI channel, and it has no members.

All of it: [ISXOgreEQ2.Persona](Persona.md)

**Returns:** object: the Persona sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.Persona.

```text
echo ${ISXOgreEQ2.Persona}
```

### `PotCb`

`${ISXOgreEQ2.PotCb}`

The PotCb sub-object behind ogre potcb: a sampler for Potency, Crit Bonus and Fervor with its own panel. Its methods are :Open, :On, :Off, :End, :Status, :Reset, :Interval[ms], :Help and the panel's own :UI channel, and it has no members.

All of it: [ISXOgreEQ2.PotCb](PotCb.md)

**Returns:** object: the PotCb sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.PotCb.

```text
echo ${ISXOgreEQ2.PotCb}
```

### `PulseBudget`

`${ISXOgreEQ2.PulseBudget}`

The PulseBudget sub-object behind ogre pulse: the per-frame time each resumable section gets, and its window. Its methods are :Open, :Close, :On, :Off, :Reset, :Ceiling, :Slice, :Report, :JobTest and the panel's own :UI channel, and it has no members.

All of it: [ISXOgreEQ2.PulseBudget](PulseBudget.md)

**Returns:** object: the PulseBudget sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.PulseBudget.

```text
echo ${ISXOgreEQ2.PulseBudget}
```

### `PulseProf`

`${ISXOgreEQ2.PulseProf}`

The PulseProf sub-object behind ogre pulseprof: frame time and native read counts per pulse subsystem. Its methods are :Help, :Report, :Reset, :On, :Off, :Overhead and :Scans, and it has no members.

All of it: [ISXOgreEQ2.PulseProf](PulseProf.md)

**Returns:** object: the PulseProf sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.PulseProf.

```text
echo ${ISXOgreEQ2.PulseProf}
```

### `Pushover`

`${ISXOgreEQ2.Pushover}`

The Pushover sub-object behind ogre pushover: push notifications through Pushover.net, for one session; OgreBotAPI.Comms:Pushover takes a for-who. Its methods are :Status, :Reload, :Message and the credentials window's :UI, and it has no members.

All of it: [ISXOgreEQ2.Pushover](Pushover.md)

**Returns:** object: the Pushover sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.Pushover.

```text
echo ${ISXOgreEQ2.Pushover}
```

### `QuestCompare`

`${ISXOgreEQ2.QuestCompare}`

The QuestCompare sub-object behind ogre questcompare: the small window that shows whether your group is on the same step of a quest as you. Its methods are :Open, :Close and the window's own :UI channel, and it has no members.

All of it: [ISXOgreEQ2.QuestCompare](QuestCompare.md)

**Returns:** object: the QuestCompare sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.QuestCompare.

```text
echo ${ISXOgreEQ2.QuestCompare}
```

### `QuestHelper`

`${ISXOgreEQ2.QuestHelper}`

The QuestHelper sub-object behind ogre quest: once on, it keeps hailing nearby NPCs that offer, update or complete a quest, clicks nearby special objects and answers the conversation, until you turn it off. Its methods are :On (On[1] always takes reply 1), :Off, :Status, :List, :Reload and :Help, and it has no members.

All of it: [ISXOgreEQ2.QuestHelper](QuestHelper.md)

**Returns:** object: the QuestHelper sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.QuestHelper.

```text
echo ${ISXOgreEQ2.QuestHelper}
```

### `Queue`

`${ISXOgreEQ2.Queue}`

The priority action queue that runs casts, item uses, clicks, commands, moves and flows one at a time: :Add or .Enqueue[...] queue an action, .Count / .Entry[N] / .EntryJSON[N] list them and .Status[seq] follows one. :Spew prints every entry and :Remove[seq] drops a waiting one; echoing the object prints ISXOgreEQ2.Queue.

All of it: [ISXOgreEQ2.Queue](Queue.md)

**Returns:** object: the priority action queue (type ogreeq2queue)

```text
echo ${ISXOgreEQ2.Queue}
```

### `Quiver`

`${ISXOgreEQ2.Quiver}`

The Quiver sub-object behind ogre quiver: :Refill tops up your ammo container from your bags and then, in a guild hall, pulls more ammo from the depot, and :Stop stops it. Its members Running and Status report the run.

All of it: [ISXOgreEQ2.Quiver](Quiver.md)

**Returns:** object: the Quiver sub-object; it always exists, and as text it reads its status line - "idle", "filling from bags (&lt;n>/&lt;total>)" or "arming the depot pull".

```text
echo ${ISXOgreEQ2.Quiver}
```

### `Radar`

`${ISXOgreEQ2.Radar}`

The Radar sub-object behind ogre radar: nearby actors on a panel. It has one method per word of the command, from :On and :Off to the settings and the reports, and it has no members.

All of it: [ISXOgreEQ2.Radar](Radar.md)

**Returns:** object: the Radar sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.Radar.

```text
echo ${ISXOgreEQ2.Radar}
```

### `Refine`

`${ISXOgreEQ2.Refine}`

The Refine sub-object behind ogre refine: it refines the Raw and Rare resources in your carried bags. :Start runs one pass, :Plan is a dry run, :Stop, :Status and :Reload round it out, and :Raw, :Rare, :Rewards (on or off) and :Bags (a bag list, all or none) are its settings; it has no members.

All of it: [ISXOgreEQ2.Refine](Refine.md)

**Returns:** object: the Refine sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.Refine.

```text
echo ${ISXOgreEQ2.Refine}
```

### `ReplenishNames`

`${ISXOgreEQ2.ReplenishNames}`

The ReplenishNames sub-object behind ogre replenishnames: the fallback food, drink and potion names the replenish calls use, read from two files. :Show prints the active names and both files, :Reload re-reads them and then prints the same report, and it has no members.

All of it: [ISXOgreEQ2.ReplenishNames](ReplenishNames.md)

**Returns:** object: the ReplenishNames sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.ReplenishNames.

```text
echo ${ISXOgreEQ2.ReplenishNames}
```

### `SafeFall`

`${ISXOgreEQ2.SafeFall}`

The SafeFall sub-object behind ogre safefall: the Safe Fall trainer that flies up, drops, remounts and repeats. Its methods are :Status, :On, :Off, :Open, :End and :Help, and it has no members.

All of it: [ISXOgreEQ2.SafeFall](SafeFall.md)

**Returns:** object: the SafeFall sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.SafeFall.

```text
echo ${ISXOgreEQ2.SafeFall}
```

### `Scheduler`

`${ISXOgreEQ2.Scheduler}`

Timers that fire a LavishScript event after a delay: :FireEvent[delayMs,eventName,...] once, :FireEventEvery[...] on repeat, :Cancel[key] to stop one, with .Count, .Active[key] and .Remaining[key] to check them. The encounter engine's timers share the table and a script sees them too (in .Count, :Spew and :ClearNonPersistent), so a script can watch or act on them; arming a pending key replaces it, and echoing the object prints ISXOgreEQ2.Scheduler.

All of it: [ISXOgreEQ2.Scheduler](Scheduler.md)

**Returns:** object: the event timer scheduler (type ogreeq2scheduler)

```text
echo ${ISXOgreEQ2.Scheduler}
```

### `Spawn`

`${ISXOgreEQ2.Spawn}`

Read-only status for actor spawn and despawn tracking: .LiveCount, .IsLive[&lt;id>], .HasChest / .ChestId for an Exquisite Chest, and event counters, plus :SetOnSpawnDelay[ms] / :ResetOnSpawnDelay for this session. Echoing the object prints a one-line summary (live count, chest id, spawns, despawns).

All of it: [ISXOgreEQ2.Spawn](Spawn.md)

**Returns:** object: spawn tracking status (type ogreeq2spawn)

```text
echo ${ISXOgreEQ2.Spawn}
```

### `TagTimers`

`${ISXOgreEQ2.TagTimers}`

The Tag Timers window, which lists every Embargo and Allow tag on this character. :Open and :Close show and hide it; echoing the object prints ISXOgreEQ2.TagTimers.

All of it: [ISXOgreEQ2.TagTimers](TagTimers.md)

**Returns:** object: the Tag Timers window (type ogreeq2tagtimers); methods only

```text
echo ${ISXOgreEQ2.TagTimers}
```

### `Targeting`

`${ISXOgreEQ2.Targeting}`

The assist and auto-target engine that decides who you attack: .AssistId, .Enabled and .InControl read its decision, :Tick evaluates it and queues a retarget for the next pulse, and :LoadList / :ClearList pick a saved auto-target list. Echoing the object prints ISXOgreEQ2.Targeting.

All of it: [ISXOgreEQ2.Targeting](Targeting.md)

**Returns:** object: the assist / auto-target engine (type ogreeq2targeting)

```text
echo ${ISXOgreEQ2.Targeting}
```

### `TaskRunner`

`${ISXOgreEQ2.TaskRunner}`

The TaskRunner sub-object behind ogre taskrunner: logs characters in one at a time, does the chores that are due, and logs out. Its methods are :Open, :Close, :End, :Status, :Run, :Lists, :Start, :Stop, :Reload, :Plan, :Now, :Clear and the Lists window's :UI, and it has no members.

All of it: [ISXOgreEQ2.TaskRunner](TaskRunner.md)

**Returns:** object: the TaskRunner sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.TaskRunner.

```text
echo ${ISXOgreEQ2.TaskRunner}
```

### `Tour`

`${ISXOgreEQ2.Tour}`

The first-run window tour that teaches resizing a window, its title-bar menu and Save Position. :Open / :Close show and hide it, and :Done / :Skip mark it seen; echoing the object prints ISXOgreEQ2.Tour.

All of it: [ISXOgreEQ2.Tour](Tour.md)

**Returns:** object: the first-run window tour (type ogreeq2tour); methods only

```text
echo ${ISXOgreEQ2.Tour}
```

### `Travel`

`${ISXOgreEQ2.Travel}`

The Travel sub-object behind ogre travel: the Travel Helper window, which lists a fast-travel, spire, druid-ring or bell map's destinations and sends the group to one. Its methods are :Open, :End, :Help and the window's own :UI channel, and it has no members.

All of it: [ISXOgreEQ2.Travel](Travel.md)

**Returns:** object: the Travel sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.Travel.

```text
echo ${ISXOgreEQ2.Travel}
```

### `TravelMesh`

`${ISXOgreEQ2.TravelMesh}`

Zone-to-zone travel routing over the game's travel networks such as bells, spires and druid rings: :Go[&lt;destination>] starts a route, :GoGroup[...] sends the group, :Stop ends it, and .TMActive / .TMState / .TMRoute follow it. Echoing the object prints "idle" with the last reason when no route is running, otherwise the route status.

All of it: [ISXOgreEQ2.TravelMesh](TravelMesh.md)

**Returns:** object: the zone-to-zone travel router (type ogreeq2travelmesh)

```text
echo ${ISXOgreEQ2.TravelMesh}
```

### `Version`

`${ISXOgreEQ2.Version}`

The extension's build date as an 8-digit yyyymmdd string, stamped when the extension was compiled. Echoing ${ISXOgreEQ2} on its own prints "ISXOgreEQ2" followed by the same value.

**Returns:** string: the build date as yyyymmdd, such as 20261103

```text
echo ${ISXOgreEQ2.Version}
```

### `Watcher`

`${ISXOgreEQ2.Watcher}`

The Watcher sub-object behind ogre find, ogre trackshiny and ogre watcher: :Find[words...] watches for actors by name and :TrackShiny[words...] for harvestables of one colour, each announcing and dropping a waypoint when one turns up. :End turns both watches off and closes the Watcher window, and it has no members.

All of it: [ISXOgreEQ2.Watcher](Watcher.md)

**Returns:** object: the Watcher sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.Watcher.

```text
echo ${ISXOgreEQ2.Watcher}
```

### `WindowReactions`

`${ISXOgreEQ2.WindowReactions}`

The WindowReactions sub-object: a diagnostic over what the bot does when a loot, choice or quest window comes up. Its one method is :Status, and it has no members.

All of it: [ISXOgreEQ2.WindowReactions](WindowReactions.md)

**Returns:** object: the WindowReactions sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.WindowReactions.

```text
echo ${ISXOgreEQ2.WindowReactions}
```

### `ZoneReset`

`${ISXOgreEQ2.ZoneReset}`

The ZoneReset sub-object behind ogre zone: the zone-reuse resetter, which reads the game's Zone Reuse window and resets zone timers. Its methods are :Open, :End, :Help, :List, :Dump, :Force, :Add, :AddFilter, :Queue, :Clear, :Reset, :Status, :Flags and the panel's :UI, and it has no members.

All of it: [ISXOgreEQ2.ZoneReset](ZoneReset.md)

**Returns:** object: the ZoneReset sub-object; it always exists, has no members, and as text it reads ISXOgreEQ2.ZoneReset.

```text
echo ${ISXOgreEQ2.ZoneReset}
```
