<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# `ogre` commands

## `abilitydetails`

`ogre abilitydetails [name or id]`

Show every field your ability export holds for an ability, with a search

| Word | Type | Default | Meaning |
|---|---|---|---|
| `<name or id>` | text | the window opens with nothing picked | An ability's name or ID: a base name picks the rank the bot uses, a rank's full name or an ID picks exactly that rank, and the search box is filled in with it. |

```text
ogre abilitydetails Kick
```

## `account`

`ogre account`

Show this session's account and access level

```text
ogre account
```

## `ae`

`ogre ae [-nogui] [-targets <n>] [-list]`

Also: `ogre abilityefficiency`

Your abilities' damage / (cast + recovery), at 1 to n targets: a window, or -nogui for the report file

```text
ogre ae
```

## `afk`

`ogre afk [0|on|off]`

Also: `ogre antiafk`

Keep the session alive (bare = silent; 0 = noisy; off = stop)

| Word | Type | Default | Meaning |
|---|---|---|---|
| `0` | word | bare `ogre afk` turns it on silent | Turn the keepalive on in noisy mode: it prints a line each time it sends its /who all (every 10 to 15 minutes). |
| `on` | word |  | Turn the keepalive on and keep the silent or noisy choice it already has. |
| `off` | word |  | Stop the keepalive (the same as `ogre end afk`); invite accepting is not changed. |
| `invites` | word | off at load | `invites on` or `invites off`: auto-accept group invites from names on your characters list; separate from the keepalive. |

```text
ogre afk off
```

## `analysis`

`ogre analysis [scan|monitor|taps|export|import|end]`

Also: `ogre anal`

Watch actors, record what changes and when, and diff two of them

| Word | Type | Default | Meaning |
|---|---|---|---|
| `scan` | word | bare `ogre analysis` opens the window | Scan the zone's actors; add `<member>=<value>` terms (`<member><<value>` and `<member>><value>` too) to keep only matching ones, none reuses the window's terms or scans everything. |
| `monitor` | word |  | `monitor on\|off\|clear\|list`, or `monitor add <id\|target\|cursor>` / `monitor remove <id>`: pick the actors to watch and record their changes. |
| `taps` | word |  | `taps on` or `taps off`: log the choice and reward windows that appear (any word but off turns them on). |
| `export` | word |  | `export [<name>]`: save what was recorded to a file. |
| `import` | word |  | `import <name\|path>`: load a saved session back in. |
| `end` | word |  | Stop sampling, the taps and any scan, then close the window (the same as `ogre end analysis`). |
| `panel` | word |  | Open the window. |
| `close` | word |  | Close the window only; recording goes on. |
| `status` | word |  | Print what is monitored, the sample count, the scan and the taps. |
| `rate` | word |  | `rate <ms>`: how often monitored actors are sampled, 100 to 10000 ms. |
| `sessions` | word |  | List the saved sessions you can import. |

```text
ogre analysis monitor add target
```

## `assist`

`ogre assist`

Show who this toon is assisting right now, and why

```text
ogre assist
```

## `atb`

`ogre atb`

Also: `ogre autotargetbalance`

Open OgreBot at the AutoTarget tab (Balance generator)

```text
ogre atb
```

## `autologin`

`ogre autologin`

Open the auto-login config panel

```text
ogre autologin
```

## `bgrender`

`ogre bgrender [on|off|draw <ms>|hz <n>|force on|off|hold <name>|release <name>|clear]`

Skip drawing while this client is in the background (once a second; full drawing when active)

| Word | Type | Default | Meaning |
|---|---|---|---|
| `on` | word | off at load; bare `ogre bgrender` prints the status | Turn background render skipping on. |
| `off` | word |  | Turn it off - full drawing again (the same as `ogre end bgrender`). |
| `draw` | word |  | Set how often a background client still draws a frame, the `<ms>` after it. |
| `<ms>` | number | 1000 | The background draw interval in milliseconds; 0 means never draw in the background. |
| `hz` | word |  | Set the background loop cap, the `<n>` after it. |
| `<n>` | number | 100 | Loops per second while in the background; 0 means no cap. |
| `hold` | word |  | `hold <name>`: keep every frame drawn until that name is released (for scripts that need the screen drawn). |
| `release` | word |  | `release <name>`: drop that hold. |
| `clear` | word |  | Drop every hold. |

```text
ogre bgrender on
```

## `bot`

`ogre bot [<toon>] [-s <server>] [-c <class>]`

Load OgreBot (logs &lt;toon> in first if given, on that server and as that class if given)

| Word | Type | Default | Meaning |
|---|---|---|---|
| `<toon>` | name | OgreBot loads on the character you are on now | Log this character in first, then load OgreBot. |
| `-s` | flag |  | Log in on the server named next (`-server` works too); needed when the character is on more than one server and none is the default. |
| `<server>` | name | the character's default server | The server for `-s`; `ogre login -?` lists the short forms. |
| `-c` | flag |  | Log in as the class named next (`-class` works too). |
| `<class>` | name | whatever class it was | The class for `-c`. |

```text
ogre bot Mytoon
```

## `buycrate`

`ogre buycrate [-r|-h|-all]`

Buy this zone's heroic/raid crates (-r raid, -h heroic, -all)

| Word | Type | Default | Meaning |
|---|---|---|---|
| `-r` | flag | with no flag both crates are bought | Buy only the raid crate (`-raid` works too). |
| `-h` | flag |  | Buy only the heroic crate (`-heroic` works too). |
| `-all` | flag | on | Buy both the heroic and the raid crate. |

```text
ogre buycrate -r
```

## `buyfuel`

`ogre buyfuel [amount]`

Buy the EXAMINED fuel up to &lt;amount> in the guild fuel depot

| Word | Type | Default | Meaning |
|---|---|---|---|
| `<amount>` | number | 90000 | Buy the examined fuel until the guild Fuel Depot holds this many. |

```text
ogre buyfuel 50000
```

## `buyoverseermissions`

`ogre buyoverseermissions [flags] | stop | status`

Also: `ogre bom`

Buy Overseer missions from the Administrator agent

| Word | Type | Default | Meaning |
|---|---|---|---|
| `-season` | flag | bare = the options on this character's Overseer Buy tab | `-season <n>`: only missions of season 1 to 7 (`-s` works too). |
| `-colour` | flag | any colour | `-colour <name>`: only Blue, Yellow, Purple or Green missions (`-c` / `-color` work too). |
| `-num` | flag | 10 | `-num <n>`: how many different missions to buy (`-n` works too). |
| `-amount` | flag | 10 | `-amount <n>`: how many of each to buy, at most 20 (`-a` works too). |
| `-replenishonly` | flag | off | Only top up missions you already have (`-r` / `-ro` work too). |
| `-noscribe` | flag | scribe is on | Do not scribe the bought missions (`-scribe` turns it back on). |
| `-destroy` | flag | off | Destroy the copies left over after scribing (`-nodestroy` turns it off). |
| `-gettogh` | flag | off | Go to the guild hall when the run finishes (`-gh`; `-nogettogh` / `-nogh` turn it off). |
| `stop` | word |  | Stop a running buy (`abort` works too). |
| `status` | word |  | Print how the buy run is going. |

```text
ogre buyoverseermissions -num 5 -amount 2
```

## `camp`

`ogre camp [charselect]`

Camp out to login+exit ('charselect' stays at char select)

| Word | Type | Default | Meaning |
|---|---|---|---|
| `charselect` | word | camps to the login screen, then exits the game | Camp to character select and stay there (`cs` / `select` work too). |

```text
ogre camp charselect
```

## `chatcmd`

`ogre chatcmd [off|status|debug [on|off]|reloadauth|test <chattype> <speaker> [message]]`

Run the commands your own characters send you in chat

| Word | Type | Default | Meaning |
|---|---|---|---|
| `off` | word | bare `ogre chatcmd` turns it on | Stop running commands sent to you in chat (the same as `ogre end chatcmd`). |
| `status` | word |  | Print whether it is on, how many names it trusts, and how many lines it ran or rejected. |
| `reloadauth` | word |  | Re-read the names of your own characters whose chat lines it will obey. |

```text
ogre chatcmd status
```

## `cm`

`ogre cm [-small|-large]`

Also: `ogre collection`, `ogre collections`

Add collectibles from your collectible depot to your collections

| Word | Type | Default | Meaning |
|---|---|---|---|
| `-small` | flag | the nearest Collectible Depot, else your Personal Collectible Stash | Use the Collectible Depot (the small one) only. |
| `-large` | flag |  | Use the Collectible Depot (Large) only. |
| `-inventory` | flag | off | Add the collectibles in your bags instead of a depot (`1` / `-1` work too). |

```text
ogre cm -large
```

## `codexinspect`

`ogre codexinspect <Name[,Name...]|reset>`

Inspect group/raid members and upload their gear to eq2codex.com

| Word | Type | Default | Meaning |
|---|---|---|---|
| `<Name[,Name...]>` | text | bare prints the status and the usage | Inspect these group or raid members (names split by commas) and upload their gear to eq2codex.com. |
| `reset` | word |  | Reset your active raid on eq2codex.com. |
| `status` | word |  | Print how the upload pass is going (`?` works too). |

```text
ogre codexinspect Alpha,Bravo
```

## `codextoon`

`ogre codextoon [status]`

Upload your own gear/stat snapshot to eq2codex.com

| Word | Type | Default | Meaning |
|---|---|---|---|
| `status` | word | bare uploads your own gear and stats now | Print the upload status instead of uploading (`?` works too). |

```text
ogre codextoon
```

## `commandpacks`

`ogre commandpacks`

Also: `ogre packs`

Re-read the console's commands, including command packs (Scripts/OgreExternal)

```text
ogre commandpacks
```

## `commands`

`ogre commands`

Also: `ogre help`

Open the Commands panel: every ogre command, searchable and runnable

```text
ogre commands
```

## `console`

`ogre console`

Also: `ogre oc`, `ogre ogreconsole`

Open the OgreConsole window

```text
ogre console
```

## `contentbuilder`

`ogre contentbuilder`

Also: `ogre icbuilder`

Build and edit Instance Controller zone files and fight files as boxes: every step and its options, checked as you go

```text
ogre contentbuilder
```

## `craft`

`ogre craft [status|start|writs|tinker|lll|stop|end|minimize|scan|add|set|shop|?]`

Also: `ogre craft2`

Open the crafting panel

| Word | Type | Default | Meaning |
|---|---|---|---|
| `status` | word | bare `ogre craft` opens the panel and turns on craft reactions | Print what crafting is doing, how many are crafted and the last error. |
| `start` | word |  | Craft what is in the queue. |
| `writs` | word |  | Run the writ flow. |
| `tinker` | word |  | Run auto tinkering. |
| `lll` | word |  | Run low level leveling. |
| `stop` | word |  | Stop the run; the panel stays open. |
| `end` | word |  | Stop everything and close the window (the same as `ogre end craft`). |
| `minimize` | word |  | Roll the window up to its title bar; crafting goes on, bare `ogre craft` brings it back. |
| `scan` | word |  | Re-read your recipe book. |
| `add` | word |  | `add <recipe name\|id\|lastknownrecipe> [<quantity>]`: put a recipe in the queue; a trailing whole number is the quantity (default 1), lastknownrecipe is the last one you scribed. |
| `set` | word |  | `set <key> <value>`: change one craft setting (saved a second later). |
| `shop` | word |  | `shop books`, `shop sell <name>...` or `shop destroy <name>...`: run one merchant errand by hand (not while a craft runs). |
| `?` | word |  | Print the word list (`help` works too). |
| `pause` | word |  | `pause` or `pause on` pauses the run; `pause off` resumes it. |
| `clear` | word |  | Empty the queue. |
| `queue` | word |  | List what is in the queue. |
| `quest` | word |  | Craft the recipe steps of your current quest until none is left. |
| `save` | word |  | Save the craft settings now. |
| `reload` | word |  | Re-read the craft settings and the data files. |

```text
ogre craft writs
```

## `craftgm`

`ogre craftgm [<range>] | scan [<range>] | start [<range>] | queue [<range>] | status | stop | end | close  [depot|nodepot]`

Open the Grandmaster crafting panel ((Master) scrolls -> (Grandmaster) crafts)

| Word | Type | Default | Meaning |
|---|---|---|---|
| `<range>` | text | bare opens the panel and does nothing else | A level (`131`), a range (`131-135` or `131 135`), or `all`; on its own it opens the panel with the range filled in and scans nothing. |
| `scan` | word |  | `scan [<range>]`: open the panel and find the (Master) scrolls to craft, crafting nothing. |
| `start` | word |  | `start [<range>]`: open the panel and scan, queue and craft the (Grandmaster) recipes. |
| `queue` | word |  | `queue [<range>]`: scan and replace the Craft queue with the (Grandmaster) recipes, then stop; never uses the Scroll Depot. |
| `status` | word |  | Print the state; does not touch the panel. |
| `stop` | word |  | Stop a run; the panel stays as it is. |
| `end` | word |  | Stop a run and close the panel (the same as `ogre end craftgm`). |
| `close` | word |  | The same as end. |
| `depot` | word | as last set (off to start) | Also pull scrolls from the Scroll Depot; sticks, and works with any word that takes a range. |
| `nodepot` | word |  | Use your bags only (`bagsonly` works too); sticks. |

```text
ogre craftgm start 131-135 depot
```

## `craftingmats`

`ogre craftingmats [-<expansion> -<category> ...] | ogre craftingmats plan|help|end`

Also: `ogre cmats`

Edit the crafting-mats lists; with flags, pull a craft's mats from the harvest depot

| Word | Type | Default | Meaning |
|---|---|---|---|
| `-<expansion>` | flag | with only a category, Visions of Vetrovia | Which list to pull from: -vov, -cd, -mm, -pop or -ka (any list file's key); several may be given. |
| `-<category>` | flag | the list's own line (signature; for -ka daily and weekly) | -sig (or -s), -daily (or -d) or -weekly (or -w). |
| `plan` | word |  | `plan [-<expansion> -<category> ...]`: print the shopping list and stop, without the depot (`preview` and `-plan` work too). |
| `help` | word |  | Print the usage (`?` works too). |
| `end` | word |  | Stop a pull and close the editor (the same as `ogre end craftingmats`). |
| `panel` | word | bare `ogre craftingmats` opens the editor | Open the list editor (`config` / `edit` work too). |

```text
ogre craftingmats -vov -sig
```

## `craftlite`

`ogre craftlite`

Also: `ogre cl`

Cast crafting reactions only (no panel, no queue)

```text
ogre craftlite
```

## `dets`

`ogre dets [m|target] [-noinfo]`

Also: `ogre detrimentals`

Dump your detrimentals, with Name and Description (a server read each; -noinfo skips them)

| Word | Type | Default | Meaning |
|---|---|---|---|
| `m` | word | your own detrimentals | Dump your maintained effects instead (`maintained` works too). |
| `target` | word |  | Dump your target's effects instead (`t` works too). |
| `-noinfo` | flag | Name and Description are read (one server read each) | Skip the Name and Description - a cheap dump with the icon pair only. |

```text
ogre dets target -noinfo
```

## `effecttracker`

`ogre effecttracker [on|off|npc on|merge|status|end]`

Also: `ogre oet`

Capture what every detrimental and NPC effect says it does, into the shared zone dataset

| Word | Type | Default | Meaning |
|---|---|---|---|
| `on` | word | bare opens the window | Start capturing your detrimental effects. |
| `off` | word |  | Stop both captures (players and NPCs); the window stays open. |
| `npc` | word |  | `npc on` or `npc off`: also capture NPC effects. |
| `merge` | word |  | Merge every character's captures for the zone you are in into the zone's one dataset file. |
| `status` | word |  | Print what is armed and how much was captured. |
| `end` | word |  | Stop both captures and close the window (the same as `ogre end effecttracker`). |
| `panel` | word |  | Open the window. |
| `close` | word |  | Close the window only. |
| `reload` | word |  | Re-read the capture files from disk; anything not yet saved is dropped. |
| `describe` | word | on | `describe on` or `describe off`: read each new effect's info once from the server (off loses only the Description). |
| `closewindow` | word |  | `closewindow [all]`: close one leftover examine window, or all of them. |

```text
ogre effecttracker on
```

## `encounter`

`ogre encounter [reload|debug comms|steps on|off|sequences]`

Encounter authoring: reload the json from disk, toggle the debug echoes, list live sequences

| Word | Type | Default | Meaning |
|---|---|---|---|
| `reload` | word | bare prints the word list | Re-read the encounter json from disk and swap it in; a line follows with the loaded, scanned and error counts. |
| `debug` | word |  | `debug comms on\|off` or `debug steps on\|off`: console echo for comms or step changes; `debug` alone prints the current switches. |
| `sequences` | word |  | List every live sequence: its step, how long it has been there and what holds it (`seq` works too). |

```text
ogre encounter reload
```

## `encounterrecorder`

`ogre er [on | off | end | status | start | stop | mark <text> | pets | npceffects | everydet | trash | onforwho | offforwho | pages [zone] [rebuild] | upload [on|off|now] | raid <slug> | raids]`

Also: `ogre er`

Record every fight as it happens: one folder per named, one per pull

## `examine`

`ogre examine [on|off|reset]`

Examine each NEW detrimental signature once and report it

| Word | Type | Default | Meaning |
|---|---|---|---|
| `on` | word | bare turns it on | Examine each new detrimental once and report its Name and Description (`start` works too). |
| `off` | word |  | Stop examining (`stop` works too; the same as `ogre end examine`). |
| `reset` | word |  | Forget the ones already seen, so each is examined again (`clear` works too). |
| `status` | word |  | Print whether it is on and what it has seen. |

```text
ogre examine reset
```

## `experiment`

`ogre experiment [-<stat> <n>]... | items | run <row> ...`

Also: `ogre experimentui`

Boost item stats on the tradeskill Experiment tab

| Word | Type | Default | Meaning |
|---|---|---|---|
| `-<stat>` | flag | bare prints the status and the usage | A stat to boost on the item already selected on the Experiment tab: -potency (or -p), -critbonus (or -cb), or any other option's label. |
| `<n>` | number |  | How many times to boost the stat before it; a count of 0 or less adds nothing. |
| `items` | word |  | List the item rows on the Experiment tab. |
| `run` | word |  | `run <row> -<stat> <n> ...`: the same boost on item row `<row>` from `items`. |
| `stop` | word |  | Stop and put the window size back (`off` works too; the same as `ogre end experiment`). |
| `status` | word |  | Print the state and the usage. |

```text
ogre experiment -potency 3
```

## `export`

`ogre export [flags]`

Also: `ogre abilityexport`

Open the export panel (-start runs it now, -default uses defaults)

| Word | Type | Default | Meaning |
|---|---|---|---|
| `-default` | flag | the current saved options | Use the default options for this run only; the saved ones are not changed. |
| `-start` | flag | bare opens the options panel | Run the export now, without the options panel. |
| `-stop` | flag |  | Stop an export that is running. |

```text
ogre export -default -start
```

## `find`

`ogre find <name> [-rorr]`

Watch for named actors and waypoint them when they spawn

| Word | Type | Default | Meaning |
|---|---|---|---|
| `<name>` | name | bare prints the usage and the built-in options | Watch for actors with exactly this name (any case); each word is one name, and the list replaces the old one and does one scan now. |
| `-rorr` | flag |  | Watch for the four Renewal of Ro researchers. |
| `-add` | flag |  | `-add <name>`: add a name to the list. |
| `-remove` | flag |  | `-remove <name>`: take a name off the list. |
| `-clear` | flag |  | Empty the list. |
| `-list` | flag |  | Print the list. |
| `-on` | flag |  | Start watching. |
| `-off` | flag |  | Stop watching (the same as `ogre end find`). |
| `-scan` | flag |  | Look for the listed names now. |
| `-status` | flag |  | Print whether it is watching and how many names. |
| `-panel` | flag |  | Open the window. |

```text
ogre find Gorenaire
```

## `forwhogroups`

`ogre forwhogroups [list|panel|reload]`

Also: `ogre fwg`

Name a set of toons once, then select them all with one *Team:&lt;group> for-who token

| Word | Type | Default | Meaning |
|---|---|---|---|
| `list` | word | bare prints the groups | Print every group and its toons. |
| `panel` | word |  | Open the editor where you name groups (`config` works too). |
| `reload` | word |  | Re-read the groups from disk (`refresh` works too). |
| `close` | word |  | Close the editor (the same as `ogre end forwhogroups`). |

```text
ogre forwhogroups panel
```

## `getquest`

`ogre getquest [list|reload|status|off]`

Hail the configured NPC for this zone and pick up its quest (you must be standing next to them)

| Word | Type | Default | Meaning |
|---|---|---|---|
| `list` | word | bare hails this zone's NPC and takes the quest | Print which areas are loaded and for which zones. |
| `reload` | word |  | Re-read the data files (refused while a run is going). |
| `status` | word |  | Print the run's state and counts. |
| `off` | word |  | Stop a run (`stop` works too; the same as `ogre end getquest`). |

```text
ogre getquest status
```

## `ghtohouse`

`ogre ghtohouse [flags]`

Move the guild-hall depots into your house ones (-all, -scroll, ...)

| Word | Type | Default | Meaning |
|---|---|---|---|
| `-all` | flag | no depot = refused | Move all eight shared depots (harvest, ammo, adorn, food, lore, potion, collectible, fuel); not scroll. |
| `-harvest` | flag |  | Move the harvest depot (`-h` works too). |
| `-ammo` | flag |  | Move the ammo depot. |
| `-adorn` | flag |  | Move the adornment depot. |
| `-food` | flag |  | Move the food and drink depot. |
| `-lore` | flag |  | Move the lore and legend depot. |
| `-potion` | flag |  | Move the poison, potion and totem depot. |
| `-collectible` | flag |  | Move the collectible depot (`-collect` / `-c` work too). |
| `-fuel` | flag |  | Move the fuel depot. |
| `-scroll` | flag |  | Move the scroll depot (only this direction has one). |
| `-no<depot>` | flag |  | Turn one depot back off, e.g. `-nofuel` after `-all` (also `-nh`, `-nc`). |
| `<owner>` | name | your own house | Whose house to deposit into. |

```text
ogre ghtohouse -all -scroll
```

## `heartstone`

`ogre heartstone [on|off|now]`

Also: `ogre hs`

Rekindle a guild-hall Heartstone (always-on; arms itself at zone-in)

| Word | Type | Default | Meaning |
|---|---|---|---|
| `on` | word | on; bare prints the status | Turn the Heartstone rekindler on. |
| `off` | word |  | Turn it off (the same as `ogre end heartstone`). |
| `now` | word |  | Try a rekindle on the next pulse, or look for a Heartstone if it has not found one yet. |

```text
ogre heartstone now
```

## `hideeffects`

`ogre hideeffects [panel|clear|end]`

Hide the listed junk effects on your character (plain `ogre hideeffects` runs it now)

| Word | Type | Default | Meaning |
|---|---|---|---|
| `panel` | word | bare runs it now | Open the editor for the list of effects to hide (`config` works too). |
| `clear` | word |  | Un-hide every effect the client is hiding. |
| `end` | word |  | Stop a run and close the window (the same as `ogre end hideeffects`); hidden effects stay hidden. |
| `run` | word |  | Hide the listed effects on your character now. |
| `list` | word |  | Have the client print what it is hiding, in the EQ2 chat window. |
| `delete` | word |  | `delete <id>`: un-hide one effect (`del` works too). |
| `reload` | word |  | Re-read the effect list files. |
| `reset` | word |  | Delete your own edits so the list is back to what shipped. |
| `status` | word |  | Print what is loaded, what applies to this character and how the last run went. |

```text
ogre hideeffects panel
```

## `hl`

`ogre hl [off|status|interval <ms>]`

Also: `ogre harvestlite`

Collect resource nodes already in reach (no walking)

| Word | Type | Default | Meaning |
|---|---|---|---|
| `off` | word | bare turns it on | Stop collecting (the same as `ogre end hl`). |
| `status` | word |  | Print whether it is on and what it has done. |
| `interval` | word |  | Set how often it looks for nodes in reach, the `<ms>` after it. |
| `<ms>` | number | 500 | The pass interval in milliseconds, 250 to 10000. |

```text
ogre hl interval 1000
```

## `housetogh`

`ogre housetogh [flags]`

Move your house depots into the guild-hall ones (-all, -harvest, ...)

| Word | Type | Default | Meaning |
|---|---|---|---|
| `-all` | flag | no depot = refused | Move all eight depots (harvest, ammo, adorn, food, lore, potion, collectible, fuel). |
| `-harvest` | flag |  | Move the harvest depot (`-h` works too). |
| `-ammo` | flag |  | Move the ammo depot. |
| `-adorn` | flag |  | Move the adornment depot. |
| `-food` | flag |  | Move the food and drink depot. |
| `-lore` | flag |  | Move the lore and legend depot. |
| `-potion` | flag |  | Move the poison, potion and totem depot. |
| `-collectible` | flag |  | Move the collectible depot (`-collect` / `-c` work too). |
| `-fuel` | flag |  | Move the fuel depot. |
| `-no<depot>` | flag |  | Turn one depot back off, e.g. `-nofuel` after `-all` (also `-nh`, `-nc`). |
| `<owner>` | name | your own house | Whose house to take from. |

```text
ogre housetogh -all -nofuel
```

## `ic`

`ogre ic [status|list|run|check|pause|end|options] | ogre ic -<option>[=off] ...`

Also: `ogre icx`, `ogre instancecontroller`

Open the instance controller - run zones from a queue (doc 28)

| Word | Type | Default | Meaning |
|---|---|---|---|
| `status` | word | bare opens the window | Print the run's state as text. |
| `list` | word |  | `list [<filter>]`: every loaded zone file, or those whose zone or path holds the filter. |
| `run` | word |  | `run <tier> <relative/path.json>`: run that one zone file (not the list); tier is default, test or custom. |
| `check` | word |  | `check [<zone>]`: which files claim the zone (no zone = the one you are in) and whether it is available. |
| `pause` | word |  | Pause the run. |
| `end` | word |  | Close the instance controller out (the same as `ogre end ic` and the window's X). |
| `options` | word |  | `options` lists every option; `options -<option>[=on\|off] ...` sets them. |
| `-<option>` | flag | a bare -option means on | Set any option of the window, e.g. `-loop`, `-haltAtEnd=off`, `-maxwait=30`; several at once. |
| `resume` | word |  | Resume a paused run. |
| `stop` | word |  | End the run (the window's End button). |
| `runlist` | word |  | `runlist [<row>]`: run the queue from the top, or from row `<row>`. |
| `queue` | word |  | `queue` lists it; `queue add <zone name>`, `queue add <tier> <path.json>`, `queue startat <row> <N>` (start that row at step N) or `queue clear`. |
| `wipe` | word |  | Declare a wipe now and start recovering. |
| `reload` | word |  | Re-read the zone files (the window's Reload). |
| `refresh` | word |  | Refresh the zone lock table. |
| `panel` | word |  | Open the window. |

```text
ogre ic -loop -haltAtEnd=off
```

## `im`

`ogre im [-depot -sell -destroy -tse -end] | depot|sell|destroy|tse|restock|trade <args> | chain | status | stop | close`

Also: `ogre inventorymanager`

Inventory manager - the window is the session; runs depot/sell/destroy/tse/restock/trade

| Word | Type | Default | Meaning |
|---|---|---|---|
| `-depot` | flag | bare opens the window | In a chain: deposit to depots. Chain flags run in order: -depot, -sell, -destroy, -tse, -restock, -trade. |
| `-sell` | flag |  | In a chain: sell to the merchant. |
| `-destroy` | flag |  | In a chain: destroy the listed items. |
| `-tse` | flag |  | In a chain: consume items for tradeskill experience. |
| `-end` | flag |  | Close the window once the chain is done. |
| `depot` | word |  | `depot <depot flags>`: deposit into house or guild-hall depots; `ogre im help` lists the flags. |
| `sell` | word |  | Sell; `sell preview\|list\|add\|remove\|status\|stop\|reload` too. |
| `destroy` | word |  | Destroy the list, or `destroy <name>` for one item; `destroy preview\|list\|add\|remove\|status\|stop` too. |
| `tse` | word |  | Consume items for tradeskill experience; `tse -stopafter <n>` stops after that many. |
| `restock` | word |  | `restock [<profile>]` buys up to a profile; `restock list\|show <profile>\|preview\|stop` too. |
| `trade` | word |  | Run the trade queue; `trade add <player> <qty\|all> <item>`, `trade list\|remove <n>\|clear\|preview`. |
| `chain` | word |  | Show what each chain flag does. |
| `status` | word |  | Print what the window and each mode is doing. |
| `stop` | word |  | Stop whatever mode or chain is running. |
| `close` | word |  | Close the window only. |
| `end` | word |  | Stop and close the window (the same as `ogre end im`). |
| `queue` | word |  | `queue <mode>`: run that mode when the current one finishes; `queue` alone shows what waits. |
| `console` | word |  | `console [always\|running\|never\|clear]`: the activity log strip. |
| `settings` | word |  | Print the saved options; `settings bag ...` and `settings tse <option> <value>` change them. |
| `transmute` | word |  | `transmute <name>`: transmute that item. |
| `reload` | word |  | Re-read the data files. |
| `help` | word |  | Print the full usage (`?` works too). |

```text
ogre im -depot -sell -end
```

## `info`

`ogre config`

Also: `ogre options`, `ogre config`

Open Ogre Options (account, UI scale, theme, per-game options)

```text
ogre config
```

## `irc`

`ogre irc`

Also: `ogre ogreirc`

Connect to IRC (`ogre end irc` disconnects). `irc <message>` sends.

```text
ogre irc
```

## `keys`

`ogre keys`

Also: `ogre keyboard`, `ogre kbd`

Dump the keyboard state (Shift stuck? run it while it happens and send the lines)

```text
ogre keys
```

## `lag`

`ogre lag [report [s]|dump [s]|on|off|overhead|budget <ms> <ms>|minutes <1-60>|clear|close]`

Every frame of the last few minutes - what it cost and what ran in it; find and open the FPS dips

| Word | Type | Default | Meaning |
|---|---|---|---|
| `report` | word | bare opens the window | Print a report of the last `<s>` seconds: the FPS dips and what caused them. |
| `<s>` | number | 60 for report; everything recorded for dump | How many seconds back report or dump looks. |
| `dump` | word |  | Save the last `<s>` seconds of frames to a file (the save itself costs one frame). |
| `on` | word | on | Record every frame (saved). |
| `off` | word |  | Stop recording; frames already recorded are kept. |
| `overhead` | word |  | Measure and print what the recorder itself costs. |
| `budget` | word | 25 and 33.3 ms | `budget <ms> <ms>`: the two frame budgets the report counts against; the second must be above the first. |
| `minutes` | word | 5 | `minutes <1-60>`: how many minutes of frames are kept; it starts again empty. |
| `clear` | word |  | Throw away the recorded frames. |
| `close` | word |  | Close the window (the same as `ogre end lag`). |

```text
ogre lag report 30
```

## `leveltransmuting`

`ogre leveltransmuting [on|off|status|end]`

Also: `ogre lt`

Buy transmuter's stones from Barnaby, then transmute them, for transmuting skill-ups

| Word | Type | Default | Meaning |
|---|---|---|---|
| `on` | word | bare opens the panel | Start: buy transmuter's stones from Barnaby (travelling there if needed), transmute them, and repeat. |
| `<count>` | number | 60 | For `on`: stones to hold per merchant visit, 1 to 800. |
| `<rounds>` | number | 20 | For `on`: stop after this many rounds, 1 to 500; there is no unlimited mode. |
| `off` | word |  | Stop the run. |
| `status` | word |  | Print the run's phase and round count. |
| `end` | word |  | Stop and close the panel (the same as `ogre end leveltransmuting`). |
| `panel` | word |  | Open the panel (`gui` / `ui` work too). |

```text
ogre leveltransmuting on 60 20
```

## `login`

`ogre login <toon> [-s <server>] [-c <class>]`

Log a character in (does not load OgreBot). 'ogre login -?' lists the server short forms

| Word | Type | Default | Meaning |
|---|---|---|---|
| `<toon>` | name |  | The character to log in; nothing happens without it. |
| `-s` | flag | the character's default row | Log in on this server, a full name or a short form such as `ab`; it matters only for a name on more than one server. |
| `-c` | flag | logs in whatever class it was | Log in as this class; a character already in the world as another class camps and comes back as it. |
| `-?` | flag |  | List the server short forms instead of logging in. |

```text
ogre login Mytoon -s ab
```

## `mbc`

`ogre mbc <from> <to>`

Also: `ogre movebagcontents`

Move a bag's contents into another bag (bags 1-6)

| Word | Type | Default | Meaning |
|---|---|---|---|
| `<from>` | number |  | The bag (1-6) to empty. |
| `<to>` | number |  | The bag (1-6) to move its items into. |

```text
ogre mbc 2 5
```

## `mcp`

`ogre mcp`

Also: `ogre ogremcp`

Open the Master Control Panel

```text
ogre mcp
```

## `merchant_craft`

`ogre mc [list | #<n>|<recipe> [count]]`

Also: `ogre mc`

Buy limited recipes from a merchant, then craft them

| Word | Type | Default | Meaning |
|---|---|---|---|
| `list` | word |  | Scan the targeted merchant and number the limited recipes it sells. |
| `<recipe>` | text |  | Part of a recipe name: each round buys it if you do not know it, scribes it, summons the station and crafts 3. |
| `#<n>` | word |  | Use row `<n>` from the last `ogre mc list` instead of a name. |
| `<count>` | number | 1 | After the recipe: how many rounds to run (1-999). |
| `stop` | word |  | Abandon the run (the same as `ogre end mc`). |
| `status` | word | this is what no word does | Say what it is doing and what the last scan found, then the usage. |
| `help` | word |  | Show the usage. |

```text
ogre mc ferrite bracelet 4
```

## `mesh`

`ogre mesh <destination>`

Also: `ogre ogretravelmesh`

Travel to a destination across the zone-network mesh

| Word | Type | Default | Meaning |
|---|---|---|---|
| `<destination>` | text |  | The zone to travel to; the whole rest of the line is one name, spaces and all. |

```text
ogre mesh Qeynos Harbor
```

## `migrate`

`ogre migrate`

Review migration status and re-run any item

```text
ogre migrate
```

## `move`

`ogre move`

NOT PORTED YET - comes with the new movement and navigation

```text
ogre move
```

## `moveincombat`

`ogre moveincombat`

NOT PORTED YET - comes with the new movement and navigation

```text
ogre moveincombat
```

## `movent`

`ogre movent`

NOT PORTED YET - comes with the new movement and navigation

```text
ogre movent
```

## `nav`

`ogre nav -loc \"x,y,z\" [flags]`

Also: `ogre navigate`

Walk somewhere over the baked navmesh (`ogre nav -help` for the flags)

| Word | Type | Default | Meaning |
|---|---|---|---|
| `-loc` | flag |  | Walk to these coordinates: x,y,z as one quoted word or three words (Y is up). |
| `-precision` | flag |  | Stop within this many units of the spot; it stays set for the session. |
| `-fly` | flag | auto: flies only on a long detour | Fly this trip. |
| `-nofly` | flag | auto: flies only on a long detour | Never fly this trip. |
| `-nodoors` | flag | doors are opened | Do not open doors on the way. |
| `-doors` | flag |  | Open doors on the way again. |
| `-on` | flag |  | Let nav move this character. |
| `-off` | flag |  | Stop nav from moving this character at all. |
| `-set` | flag |  | Change one nav setting: `-set <key> <value>` (arrive, lookmax, avoid, doortries and more). `-set` alone lists the keys. |
| `-reset` | flag |  | Put every nav setting back to its default, or only `<key>` when you name one. |
| `-panel` | flag |  | Open the nav window now and on every trip. |
| `-nopanel` | flag |  | Close the nav window and stop it opening on each trip. |
| `stop` | word |  | Stop the trip; the nav window stays open. |
| `end` | word |  | Stop the trip and close the nav window (the same as `ogre end nav`). |
| `status` | word |  | Say what nav is doing, which mesh is loaded and any setting you changed. |
| `panel` | word |  | Open the nav window. |
| `help` | word | this is what no word does | Show the flags. |

```text
ogre nav -loc "100,20,-300" -precision 3
```

## `navlib`

`ogre navlib`

NOT PORTED YET - comes with the new navigation

```text
ogre navlib
```

## `npccast`

`ogre npccast [monitor [target|named|all|off|copy]|status|zone|capture|reload|import|end]`

Also: `ogre npccastmonitoring`

Log what mobs cast (spell name + ability id) to copy or send; watch named mobs' casts - interrupt them or run your own commands

| Word | Type | Default | Meaning |
|---|---|---|---|
| `monitor` | word |  | Start the cast monitor: each cast is logged with mob, spell name, ability id and cast time, ready to copy. |
| `target` | word | the monitor's default | After `monitor`: watch your target and its target (these casts come with the spell name). |
| `named` | word |  | After `monitor`: also watch every named mob nearby. |
| `all` | word |  | After `monitor`: also watch every NPC nearby. |
| `off` | word |  | After `monitor`: stop the monitor (it saves its list). |
| `copy` | word |  | After `monitor`: put the logged casts on the clipboard. |
| `watch` | word |  | Add a mob to the watch list: `watch <mob name>`, every word after it is the name. |
| `unwatch` | word |  | Take a mob off the watch list: `unwatch <mob name>`. |
| `clear` | word |  | Clear the watches you added; the zone's and the fights' own stay. |
| `radius` | word |  | Set the scan radius for this zone: `radius <n>`. |
| `status` | word |  | Show the scan counters, the watch list and what is being cast now. |
| `zone` | word |  | Show the cast data loaded for this zone. |
| `capture` | word |  | Add the spell your target is casting right now to your own copy of this zone's file. |
| `reload` | word |  | Re-read this zone's cast files. |
| `import` | word |  | Copy the shipped OgreBot Classic custom cast files into your own folder, never over a file you already have. |
| `end` | word |  | Stop the monitor and close the window (the same as `ogre end npccast`); the watch list keeps running. |

```text
ogre npccast monitor named
```

## `oau`

`ogre oau [minLevel]`

Also: `ogre abilityupgrades`, `ogre ogreabilityupgrades`

Report which Scroll Depot scrolls upgrade an ability you know

| Word | Type | Default | Meaning |
|---|---|---|---|
| `<minLevel>` | number | 121 | Ignore scrolls below this level (1-1000). |

```text
ogre oau 125
```

## `osa`

`ogre osa`

Open the On-Screen Assistant

```text
ogre osa
```

## `overflow`

`ogre overflow`

Move overflow-window items into your bags

```text
ogre overflow
```

## `overseer`

`ogre overseer [status|stop]`

Run the daily Overseer missions

| Word | Type | Default | Meaning |
|---|---|---|---|
| `run` | word | this is what no word does | Run the daily Overseer missions now. |
| `stop` | word |  | Stop the run (the same as `ogre end overseer`). |
| `status` | word |  | Say what the run is doing, how many it started and finished, and when the next run may start. |

```text
ogre overseer status
```

## `patch`

`ogre patch [status|revert-ext]`

Also: `ogre patcher`, `ogre update`

Check for and apply updates (status: the release you are on; revert-ext: undo a core self-update)

| Word | Type | Default | Meaning |
|---|---|---|---|
| `status` | word |  | Say which release you are on. |
| `revert-ext` | word |  | Undo a core self-update. |
| `mesh` | word |  | The navmesh download setting; with no word after it, a summary of the meshes. |
| `all` | word |  | After `mesh`: every mesh downloads in the background. |
| `ondemand` | word |  | After `mesh`: a zone's mesh downloads when you need it. |
| `off` | word |  | After `mesh`: no meshes download. |
| `ignore` | word |  | The files the patcher never writes; with no word after it, the list. |
| `add` | word |  | After `ignore`: add `<path>` to that list. |
| `remove` | word |  | After `ignore`: take `<path>` off that list. |
| `list` | word |  | After `ignore`: show the list. |
| `<path>` | text |  | After `ignore add` or `ignore remove`: a path from the InnerSpace folder, such as Scripts/Ogre/EQ2/x.json. |

```text
ogre patch mesh ondemand
```

## `paths`

`ogre paths [<path>]`

This zone's points of interest and saved paths: add them, order them, walk them, import OgreBot Classic's

| Word | Type | Default | Meaning |
|---|---|---|---|
| `<path>` | text | opens the window | Open the window on this saved path of the current zone; the whole rest of the line is one name. |

```text
ogre paths Bank Run
```

## `perf`

`ogre perf [seconds] [nothreads] | stop | status`

Also: `ogre fps`

Measure the frame rate and what uses each frame - run it while it lags and paste the report

| Word | Type | Default | Meaning |
|---|---|---|---|
| `<seconds>` | number | 10 | How long to measure (3-120 seconds); the report prints when it ends. |
| `nothreads` | word | the thread sampler runs | Measure without the thread sampler. |
| `stop` | word |  | Stop early and print the report now, or cancel one that has not started (the same as `ogre end perf`). |
| `status` | word |  | Say whether it is measuring and how long is left. |

```text
ogre perf 30
```

## `persona`

`ogre persona [<class>]`

Change this character's class, or with no class open the window to say which profile file each class uses on this PC; one character's own setting is on OgreBot's Persona tab

| Word | Type | Default | Meaning |
|---|---|---|---|
| `<class>` | name | opens the Persona window | Change this character to that class; it camps and comes back as it (you must be in the world). |

```text
ogre persona ranger
```

## `potcb`

`ogre potcb [on|off|status|reset|interval <ms>|end]`

Also: `ogre cbpot`

Track Potency / Crit Bonus / Fervor during fights - min, max, average and time at cap

| Word | Type | Default | Meaning |
|---|---|---|---|
| `on` | word |  | Start sampling. |
| `off` | word |  | Stop sampling and close the window. |
| `status` | word |  | Print every figure to the console. |
| `reset` | word |  | Clear the history and keep sampling. |
| `interval` | word |  | Set how often it samples; with no number, say the current one. |
| `<ms>` | number | 200 | After `interval`: the time between samples, 50-10000 ms. |
| `end` | word |  | Stop sampling and always close the window (the same as `ogre end potcb`). |
| `help` | word |  | Show the usage. |

```text
ogre potcb interval 500
```

## `pulse`

`ogre pulse [report|on|off|reset|ceiling <us>|slice <section> <us>|jobtest on|off]`

Also: `ogre pulsebudget`

Tune the per-frame time slice each resumable section gets

| Word | Type | Default | Meaning |
|---|---|---|---|
| `report` | word |  | Print the budget report: every resumable section, its number and its slice. |
| `on` | word |  | Turn the shared frame ceiling on and reset the counters. |
| `off` | word |  | Turn the shared frame ceiling off; each section keeps its own slice. |
| `reset` | word |  | Reset the counters. |
| `ceiling` | word |  | Set the shared frame ceiling to `<us>` microseconds (0 = none). |
| `slice` | word |  | Set one section's time per frame: `slice <section> <us>` (0 = finish it in one frame). |
| `<section>` | text |  | After `slice`: a section's name or its number from `ogre pulse report`. |
| `<us>` | number |  | After `ceiling` or `slice`: the time in microseconds. |
| `close` | word |  | Close the Pulse Budget window; the budget keeps running. |

```text
ogre pulse ceiling 2000
```

## `pulseprof`

`ogre pulseprof [report [n] [reads]|reset|on|off|overhead|scans [n|reset|on|off]]`

Frame time and native reads per pulse subsystem

| Word | Type | Default | Meaning |
|---|---|---|---|
| `report` | word |  | Print the top subsystems by frame time. |
| `<n>` | number | 20 | After `report` or `scans`: how many rows to print. |
| `reads` | word |  | After `report <n>`: break the rows down by native reads instead of time. |
| `reset` | word |  | Reset the counters. |
| `on` | word |  | Start profiling, counters reset. |
| `off` | word |  | Stop profiling; the counters freeze (the same as `ogre end pulseprof`). |
| `overhead` | word |  | Measure what the profiler itself costs. |
| `scans` | word |  | Report actor lookups by call site; `scans on`, `scans off` and `scans reset` switch or clear that count. |

```text
ogre pulseprof report 10 reads
```

## `pushover`

`ogre pushover <message> [-title T] [-priority N] | status|reload`

Send a push notification through Pushover.net

| Word | Type | Default | Meaning |
|---|---|---|---|
| `<message>` | text |  | The text to send; every word that is not a flag is part of the message. |
| `-title` | flag | the title in your Pushover settings | The notification's title (the next word). |
| `-priority` | flag | the priority in your Pushover settings | The priority, -2 to 2; 2 is an emergency that repeats until seen. |
| `-sound` | flag | the sound in your Pushover settings | The sound to play (the next word). |
| `-device` | flag | the device in your Pushover settings | Send to this one device (the next word). |
| `-retry` | flag | the retry in your Pushover settings | For priority 2: how often to repeat it, in seconds. |
| `-expire` | flag | the expire in your Pushover settings | For priority 2: when to stop repeating it, in seconds. |
| `status` | word | this is what no word does | Say whether Pushover is set up, and the usage; with more words after it, the whole line is a message. |
| `reload` | word |  | Re-read your Pushover settings; with more words after it, the whole line is a message. |

```text
ogre pushover Raid is ready -title EQ2 -priority 1
```

## `quest`

`ogre quest [1]`

Also: `ogre questhelper`, `ogre qh`

Watch for quest NPCs and dialogs and do the clicking (1 = always take reply 1)

| Word | Type | Default | Meaning |
|---|---|---|---|
| `on` | word | this is what no word does | Start watching for quest NPCs and dialogs; `on 1` is the same as `1`. |
| `1` | word |  | Start watching and always take reply 1. |
| `off` | word |  | Stop (the same as `ogre end quest`). |
| `status` | word |  | Show its state, counters and what it last did. |
| `list` | word |  | Show what the reply table holds. |
| `reload` | word |  | Re-read the reply table. |
| `help` | word |  | Show the usage. |

```text
ogre quest 1
```

## `questcompare`

`ogre questcompare`

Also: `ogre qc`, `ogre compare`

Show whether your group is on the same step of a quest as you (`ogre end questcompare` closes it)

| Word | Type | Default | Meaning |
|---|---|---|---|
| `close` | word |  | Close the window (also `off`, or `ogre end questcompare`). |

```text
ogre questcompare
```

## `quiver`

`ogre quiver`

Refill your quiver/pouch from your bags, then the ammo depot

```text
ogre quiver
```

## `radar`

`ogre radar [on|off|<verb>]`

Also: `ogre r`

Show what is around you - nearby actors on a panel (`ogre end radar` to stop)

| Word | Type | Default | Meaning |
|---|---|---|---|
| `on` | word | this is what no word does | Start scanning and open the panel. |
| `off` | word |  | Stop scanning and close the panel (the same as `ogre end radar`). |
| `toggle` | word |  | Turn it on if it is off, off if it is on. |
| `panel` | word |  | Open or close only the panel: `panel on` or `panel off`; scanning is not changed. |
| `click` | word |  | `click on` lets the mouse pass through the panel to the game; `click off` makes the panel take it again. |
| `settings` | word |  | Open the settings drawer, even when the panel lets the mouse through. |
| `uireset` | word |  | Put the panel's look back to its defaults when you cannot reach it (press Save in the drawer to keep it). |
| `radius` | word |  | The display radius, 5-500 game units; with no number, say the current one. |
| `rate` | word |  | Refreshes per second, 0-60; with no number, say the current one. |
| `cap` | word |  | Draw only the nearest `<n>` blips, 0-5000 (0 = all); with no number, say the current one. |
| `<n>` | number |  | After `radius`, `rate` or `cap`: the new value. |
| `status` | word |  | Show the radar's settings and state. |
| `help` | word |  | List the radar's words. |

```text
ogre radar radius 100
```

## `refine`

`ogre refine [start|stop|plan|raw|rare|bags|rewards]`

Refine the Raw/Rare resources in your carried bags

| Word | Type | Default | Meaning |
|---|---|---|---|
| `status` | word | this is what no word does | Show its state, settings and the usage. |
| `start` | word |  | Refine once over the chosen bags. |
| `stop` | word |  | Stop the run (the same as `ogre end refine`). |
| `plan` | word |  | A dry run: list what would be refined and what is skipped; nothing is refined. |
| `raw` | word | on | Refine Raw resources: `raw on` or `raw off`. |
| `rare` | word | off | Refine Rare resources: `rare on` or `rare off`. |
| `rewards` | word | off | Accept reward windows during a run: `rewards on` or `rewards off`. It accepts any reward window, a quest's too. |
| `on` | word |  | After `raw`, `rare` or `rewards`: turn it on. |
| `off` | word |  | After `raw`, `rare` or `rewards`: turn it off. |
| `bags` | word | bags 1 and 2 | Which carried bags to refine: bag numbers (1,2,3 or 1 2 3), `all` or `none`. |
| `reload` | word |  | Re-read the resource table. |

```text
ogre refine bags 1,2,3
```

## `reloadbot`

`ogre reloadbot`

Reload OgreBot if it is running (does nothing if it is not)

```text
ogre reloadbot
```

## `replenishnames`

`ogre replenishnames [show|reload]`

Also: `ogre staples`

The fallback food/drink/potion names the *_Replenish depot verbs use - yours, in a file

| Word | Type | Default | Meaning |
|---|---|---|---|
| `show` | word | this is what no word does | Print the fallback potion, food and drink names in use. |
| `reload` | word |  | Re-read your names file, then print them. |

```text
ogre replenishnames reload
```

## `safefall`

`ogre safefall [on|off|panel|end]`

Also: `ogre levelsafefall`

Level Safe Fall: fly up, drop, remount, repeat

| Word | Type | Default | Meaning |
|---|---|---|---|
| `status` | word | this is what no word does | Show the trainer's state and the usage. |
| `on` | word |  | Start: mount, climb, dismount, fall, repeat. |
| `<ticks>` | number | 30 | After `on`: the flight time in tenths of a second (5-600); it grows by 5 every 100 rounds. |
| `off` | word |  | Stop the trainer. |
| `panel` | word |  | Open the Safe Fall window. |
| `end` | word |  | Stop and close the window (the same as `ogre end safefall`). |
| `help` | word |  | Show the usage. |

```text
ogre safefall on 40
```

## `sessions`

`ogre sessions [on|off]`

The uplink's session watch: on/off until the uplink restarts (the saved switch is in ogre config); bare: list every session it hears

| Word | Type | Default | Meaning |
|---|---|---|---|
| `on` | word |  | Turn the uplink's session watch on until the uplink restarts. |
| `off` | word |  | Turn it off until the uplink restarts. |

```text
ogre sessions on
```

## `smalldepottobigdepot`

`ogre smalldepottobigdepot [-type]`

Also: `ogre sd2bd`

Empty a guild-hall depot into its (Large) twin

| Word | Type | Default | Meaning |
|---|---|---|---|
| `-harvest` | flag | this is the default type | Empty the Harvesting Supply Depot into its (Large) twin. |
| `-adorn` | flag |  | Empty the Adornment Depot instead. |
| `-ammo` | flag |  | Empty the ammo depot instead. |
| `-scroll` | flag |  | Empty the Scroll Depot instead. |
| `-collectible` | flag |  | Empty the collectible depot instead. |
| `-food` | flag |  | Empty the Food & Drink Depot instead. |
| `-fuel` | flag |  | Empty the fuel depot instead. |
| `-lore` | flag |  | Empty the Lore & Legend Depot instead. |
| `-potion` | flag |  | Empty the Poison, Potion, & Totem Depot instead. |
| `-donotdeposit` | flag | deposits | When your bags fill, stop instead of putting them into the large depot. |

```text
ogre smalldepottobigdepot -adorn
```

## `smartloot`

`ogre smartloot`

Also: `ogre sl`

Open the SmartLoot quota editor

```text
ogre smartloot
```

## `tags`

`ogre tags`

Also: `ogre tagtimers`

Open the Tag Timers window: every Embargo and Allow tag on this character

```text
ogre tags
```

## `taskrunner`

`ogre taskrunner [-list <list>|run <list>|start|stop|end|status|panel|lists]`

Also: `ogre tr`, `ogre packpony`, `ogre pony`

Cycle characters through their scheduled chores

| Word | Type | Default | Meaning |
|---|---|---|---|
| `-list` | flag |  | Start this session on a list: `-list <list>` (the classic spelling of `run`). |
| `run` | word |  | Start this session on a list: `run <list>`. |
| `<list>` | name |  | After `-list`, `run` or `plan`: the list's name. |
| `once` | word | the list's own setting | After the list: go through it once. |
| `loop` | word | the list's own setting | After the list: keep going round it. |
| `stagger` | word | the stagger setting | After the list: turn stagger on for this run. |
| `nostagger` | word | the stagger setting | After the list: turn stagger off for this run. |
| `start` | word |  | Cycle every configured character; only when no lists are set up. |
| `stop` | word |  | Stop the run; the window stays open. |
| `end` | word |  | Stop the run and close the window (the same as `ogre end taskrunner`). |
| `status` | word |  | Print the run's state. |
| `close` | word |  | Close the Lists window. |
| `lists` | word |  | Show the lists and their characters. |
| `reload` | word |  | Re-read the task files (refused while a character is mid-batch). |
| `plan` | word | this session's list | Show what is due, character by character; nothing runs. |
| `now` | word |  | Check what is due right away instead of waiting. |
| `clear` | word | every character | Clear error and back-off records: all, one `<toon>`, or one `<task>` of that character. |
| `<toon>` | name |  | After `clear`: the character. |
| `<task>` | name |  | After `clear <toon>`: the task. |

```text
ogre taskrunner run mylist loop
```

## `tempadorns`

`ogre tempadorns [<profile> | list | end]`

Pick the temporary adornment for each gear piece and save it as a profile; `ogre tempadorns <profile>` applies one

| Word | Type | Default | Meaning |
|---|---|---|---|
| `<profile>` | name | opens the window | Apply this saved profile: each gear piece it names gets its temporary adornment. |
| `list` | word |  | Print the saved profiles. |
| `end` | word |  | Close the window (the same as `ogre end tempadorns`). |

```text
ogre tempadorns CBOC
```

## `tour`

`ogre tour`

Open the new-user tour

```text
ogre tour
```

## `trackshiny`

`ogre trackshiny [colour]`

Watch for a coloured shiny and waypoint it

| Word | Type | Default | Meaning |
|---|---|---|---|
| `<colour>` | name | Purple | Watch the whole zone for shinies of this colour and waypoint them: White, Green, Purple, Red, BlueShimmer or Blue. |
| `-off` | flag |  | Stop watching (also `ogre end trackshiny`). |
| `-colours` | flag |  | List the colours. |
| `-interval` | flag |  | How often to look, in ms (250-30000): `-interval <ms>`. |
| `-status` | flag |  | Show what it is watching for and what it found. |
| `-panel` | flag |  | Open the Watcher window. |

```text
ogre trackshiny Blue
```

## `trade`

`ogre trade [count]`

Also: `ogre tradeit`

Trade the EXAMINED item to your target (default 12 stacks)

| Word | Type | Default | Meaning |
|---|---|---|---|
| `<count>` | number | 12 | How many stacks of the examined item to put in the trade with your target. |

```text
ogre trade 5
```

## `travel`

`ogre travel [fast|spire|druid|bell|map|end]`

Also: `ogre travelhelper`

Open the Travel Helper: list a fast-travel, spire, druid-ring or bell map's destinations and send the group to one

| Word | Type | Default | Meaning |
|---|---|---|---|
| `fast` | word |  | Open the window and list the fast-travel destinations. |
| `spire` | word |  | Open the window and list the wizard spire destinations. |
| `druid` | word |  | Open the window and list the druid ring destinations. |
| `bell` | word |  | Open the window and list the bell destinations. |
| `map` | word |  | Open the window and list the destinations of the travel map you have open. |
| `end` | word |  | Stop a list and close the window (the same as `ogre end travel`). |
| `help` | word |  | Show the usage. |

```text
ogre travel spire
```

## `travelsurvey`

`ogre travelsurvey [-r <radius>] [-all]`

Also: `ogre tsurvey`

Record every actor near you into the travel survey (for building the zone corpus)

| Word | Type | Default | Meaning |
|---|---|---|---|
| `-r` | flag | 200 | Record actors within this many units: `-r <radius>`. |
| `-all` | flag |  | Record every actor the client holds, however far. |

```text
ogre travelsurvey -r 300
```

## `version`

`ogre version`

Which OgreBot release you are on (the name the What's new page uses) and when the core was built

```text
ogre version
```

## `watcher`

`ogre watcher`

Open the Watcher window (Find Actor + Track Shiny)

```text
ogre watcher
```

## `windowreset`

`ogre windowreset`

Also: `ogre resetwindows`

Open Reset UI Windows - put windows back where they started

```text
ogre windowreset
```

## `zone`

`ogre zone [force <name>|end]`

Also: `ogre reset`, `ogre zonereset`

Open the zone-reuse resetter (OldBot's `zone` / `reset`)

| Word | Type | Default | Meaning |
|---|---|---|---|
| `list` | word |  | Refresh and print the zone table (the Zone Reuse window opens and closes). |
| `force` | word |  | Force-reset one zone, `force <zone name>`; this spends one of your reset charges. |
| `add` | word |  | Add one zone to the reset queue: `add <zone name>`. |
| `addfilter` | word |  | Add many zones to the queue at once: `resettable` (the default), `noraid` or `notlocked`. |
| `queue` | word |  | Show the reset queue. |
| `clear` | word |  | Empty the reset queue. |
| `reset` | word |  | Reset the timers of every zone in the queue. |
| `fleet` | word |  | After `reset`: do it for the characters picked in the For Who window too. |
| `status` | word |  | Show the counters and what it is doing. |
| `end` | word |  | Stop what it was asked to do and close the window (the same as `ogre end zone`). |
| `help` | word |  | Show the usage. |
| `-zone` | flag |  | Reset one zone's timer: `-zone <name>`, every word up to the next flag is the name. |
| `-force` | flag |  | With `-zone`: force-reset it, which spends a charge. |
| `-all` | flag |  | Reset every resettable zone; raid zones are skipped. |
| `-allowraid` | flag |  | With `-all`: include raid zones. |
| `-fleet` | flag |  | Do it for the characters picked in the For Who window too. |

```text
ogre zone add Kralet Penumbra: The Hive Mind
```
