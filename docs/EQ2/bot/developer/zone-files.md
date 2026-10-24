# Write your own zone files

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../index.md).
</div>

A **zone file** tells the Instance Controller (IC) how to run one instanced zone: where the group walks, which
nameds it kills, what it loots, and how it leaves. It is a JSON file. IC reads it from the top, one step at a
time, on the character that runs IC, and that character leads the group through it.

The zone files that ship with Ogre are written the same way, so the best way to learn is to open one beside this
page. The examples below are cut from `Oogothl Sprawl - Ver'Bohten Atoll` and `Gerion - Dominion of Pain`, both in
`Scripts\Ogre\EQ2\IC\default\Rage of Cthurath\`.

> **No promises.** Use this at your own risk, and expect it to change. That said, Kannkor works hard to keep
> things backwards compatible.

## Quick start

1. Make the folder `Scripts\OgreSave\EQ2\IC\custom\` if it is not there. Folders inside it are fine; the IC window
   shows them as folders.
2. Copy a shipped zone file into it to start from, and give it a name of your own.
3. Edit it. Then press **Reload** in the IC window. It prints `N zone(s) from M file(s) - X skipped, Y warning(s)`.
   If anything was skipped, type `ogre ic reload` in the console: it prints one line per problem, saying which file
   and what is wrong.
4. Pick **custom** in the IC window's root list, queue your zone, and press **Run**.

## Where zone files go

| Root | Folder | What it is |
|---|---|---|
| default | `Scripts\Ogre\EQ2\IC\default\` | The zone files that ship with Ogre. An update can replace them, so do not keep your changes here. |
| test | `Scripts\Ogre\EQ2\IC\test\` | Zone files that are still being tested. |
| custom | `Scripts\OgreSave\EQ2\IC\custom\` | Yours. Ogre's updates never touch this folder. |

- Every file ending in `.json`, in any folder under a root, is read.
- A number at the start of a file name, like `_01_`, sorts the list: numbered files come first, in number order.
- Every root loads. The same file in two roots shows up twice in the IC window: they are separate files, and
  neither replaces the other.

## A zone file, start to finish

The top of the file says which zone it is for:

```json
{
  ...
  "zone": "Oogothl Sprawl: Ver'Bohten Atoll",
  "variants": [
    "[Solo]",
    "[Heroic]"
  ],
  "expansion": "Rage of Cthurath",
  ...
  "progression": "sequential",
  "entrance": {
    "loc": [
      -859.879944,
      169.465637,
      127.360184
    ],
    "tolerance": 10
  },
  "rerunWholeZoneAfterWipe": true,
  "steps": [
```

Then come the **steps**. Each named gets a few: walk to it, kill it, loot its chest and the shinies, and say how it
went:

```json
    {
      "stepId": "named1.walk",
      "do": "path",
      "using": "nav",
      "spots": [
        [
          -793.151367,
          144.102356,
          353.17868
        ]
      ]
    },
    {
      "stepId": "named1",
      "do": "named",
      "name": "Glorfab Flit",
      "spot": [
        -755.151001,
        144.302704,
        340.9729
      ]
    },
    {
      "stepId": "named1.chest",
      "do": "loot",
      "op": "chest"
    },
    {
      "stepId": "named1.shinies",
      "do": "loot",
      "op": "shinies"
    },
    {
      "stepId": "named1.said",
      "do": "announce",
      "message": "Ver'Bohten Atoll 1/5: Glorfab Flit - {{ic.run.verdicts.named1}}, chest {{ic.run.verdicts.named1.chest}}, shinies {{ic.run.verdicts.named1.shinies}}"
    },
```

And the file ends with **the way out**: walk to the exit, then click it. Every zone file must have a way out (see
[The way out](#the-way-out)):

```json
    {
      "stepId": "exit.walk",
      "do": "path",
      "using": "nav",
      "spots": [
        [
          -772.972534,
          299.070923,
          249.26976
        ]
      ]
    },
    {
      "stepId": "exit.door",
      "do": "zoneOut",
      "op": "door",
      "name": "Exit"
    }
  ]
}
```

## The top of the file

| Key | Needed | What it does |
|---|---|---|
| `zone` | yes | The zone's name as the game shows it, without the difficulty: `"Oogothl Sprawl: Ver'Bohten Atoll"`. IC uses it to tell whether you are standing in the zone, and to travel there. |
| `variants` | yes | Every difficulty this file covers, as the game writes it: `["[Solo]", "[Heroic]"]`. Use `[]` for a zone with no difficulty in its name. The IC window offers these when you queue the file. |
| `steps` | | The main list of steps. Most files only need this one. |
| `enter`, `exit` | | Steps to run before `steps`, and after them. See [How a run goes](#how-a-run-goes). |
| `entrance` | | Where the zone-in puts you: `{ "loc": [x, y, z], "tolerance": 10 }` (tolerance in meters, 30 if left out). Wipe recovery uses it to know the group is back at the zone-in. A file with nameds and no `entrance` loads with a warning. |
| `progression` | | `"sequential"` (the default) or `"open"`. When a run starts part-way, or after a wipe, IC works out which nameds are already dead. With `sequential`, a named that is still standing means every named before it in the file is dead, and IC skips them. With `open`, nameds can die in any order, so only the ones IC saw die count. **Use `sequential` only when each named appears only after the one before it dies.** If any later named is already up when you zone in, or a named has to be spawned by an event first (a ring event, a script, anything with a `spawnWaitMs`), use `"open"`. Otherwise a run that starts with that named not spawned yet sees the later named standing and skips it. Getting `open` wrong only costs a walk over ground you already cleared; getting `sequential` wrong skips a named. |
| `enabled` | | `false` hides the file in the IC window, and it will not run. Write `true` or `false`, not `"false"`. |
| `rerunWholeZoneAfterWipe` | | `true`: after a wipe recovery, run the whole file again from the top. For zones with teleporters inside, where the group cannot walk back to where it died. Starting such a zone part-way is only allowed where the group already stands. |
| `wipeAttempts` | | How many times wipe recovery may run before IC gives the zone up: `0` to `10`, `2` if left out. |
| `onWipe` | | Your own wipe recovery steps (see [`recover`](#recover)). Leave it out for the built-in recovery. `[]` means no recovery: the first wipe gives the zone up. |
| `afterWipe` | | Your own steps for when the zone is given up. Leave it out for the built-in ones: revive, then whatever the IC window's **After a lost zone** says. |
| `fileOptions` | | Up to 3 names for the IC window's **IC File Option 1-3** boxes: `["Skip the side named"]`. Your steps read the boxes as `{{ic.options.fileOption1}}` (`TRUE` or `FALSE`), and the **IC File Args** box as `{{ic.options.fileArgs}}`. |
| `options` | | Your own values for this file. Steps read them as `{{ic.zone.options.<name>}}`. IC itself does nothing with them. |
| `difficulty` | | A difficulty menu for the IC window: `{ "choices": ["Easy", "Hard"] }` or `{ "minValue": 1, "maxValue": 5 }`. The run does not use it yet. |
| `run` | | Hands the zone to a script instead of steps: `{ "iss": "<path under Scripts>" }`, or to another zone file in the same root: `{ "json": "<path>" }`. A file has steps or `run`, never both. A script must call `ISXOgreEQ2.IC:Complete` when it is done, or the run counts as failed. |
| `expansion`, `author` | | Notes for people. IC does not use them. |

**A key IC does not read does nothing, and Reload says so.** It is a warning, so the file still loads. The line
names the key and the nearest key IC does read (see [Checking your file](#checking-your-file)). A key starting with
`_`, like `_comment`, is a note: it is never said, so use it for notes.

## How a run goes

- **Before the first step**, IC applies your Startup Options. After a zone-in, it waits until everyone has
  arrived, then gives the group a few seconds to rebuff.
- **The lists run in order: `enter`, then `steps`, then `exit`.** One step at a time, on the character that runs
  IC. Steps like `path`, `named`, `loot` and `zoneOut` move the whole group; most other actions act on the IC
  character alone unless they take `sendTo` (see [Other actions](#other-actions)).
- **A step that fails** ends its list (see `onFail` below). If `enter` fails, `steps` does not run. `exit` still runs
  after a failure.
- **When `steps` finish**, **Halt at end of zone** pauses IC right there, inside the zone. The zone end options
  (Call to guild hall after each zone, Stay in zone until a zone is ready) run at the `zoneOut` step.
- **A `zoneOut` that takes the group out ends its list.** Anything after it in that list is skipped.
- **End**, **Max wait per zone** and closing the IC window stop the run where it stands. `exit` does not run.
- **Wipes** are watched during `enter` and `steps`. IC runs the wipe recovery, then starts the zone again, leaving
  out what is already done. After `wipeAttempts` recoveries, IC gives the zone up: the `afterWipe` steps run, `exit`
  does not, and the list moves on to the next zone.
- **Starting part-way.** The IC window's **named #** starts a zone at a named: IC backs up over the steps that lead
  to it (its walk, for instance) so they run too. It only works when you are already standing in that zone. A run
  that zones in always starts from the top.

## Steps

```json
{ "stepId": "named1.chest", "do": "loot", "op": "chest" }
```

Every step that does something has a **`do`**: the action. The rest of the keys belong to that action. All the
actions are listed in [The steps, one by one](#the-steps-one-by-one).

| Key | What it does |
|---|---|
| `stepId` | The step's name. It shows in the log and the IC window, and the step's result is kept under it. |
| `onFail` | `"fail"` or `"proceed"`. With `fail`, a step that fails ends its list. With `proceed`, the list goes on. A step in a list starts as `fail`; a step inside a loop starts as `proceed`. |
| `when` | A condition. The step runs only when it is true; when it is false the step is skipped, and that is not a failure. The conditions are the ones fight files use (an example is in [Loops](#loops)). |
| `throttleMs` | Skips the step if it ran less than this many milliseconds ago. Handy inside loops. |

**Name your steps the way the shipped files do.** Call each named `named1`, `named2`, ..., and the steps that belong
to it `named1.walk`, `named1.chest`, `named1.said`. IC relies on this. **Skip the boss** leaves out the boss and
every step named after it. **named #** and resuming after a stop back up to the steps of the named before.
A named with no `stepId` cannot be remembered as done.

### Waiting

```json
{ "stepId": "settle", "wait": "ms", "limitMs": 1500, "onTimeout": "proceed" }
```

A `wait` step holds the list. `limitMs` and `onTimeout` are always needed: there are no defaults.

- `"wait": "ms"` is a fixed pause of `limitMs` milliseconds. Its `onTimeout` must be `"proceed"`.
- `"wait": <condition>` holds until the condition is true, for at most `limitMs`. Then `onTimeout` decides:
  `"proceed"` goes on, `"fail"` ends the list.
- `"wait": "atCampSpot"` holds until the IC character stands at its camp spot (see the loop below).

### Loops

`repeat` runs its own `steps` again and again. `{ "times": 3 }` runs them 3 times.
`{ "until": <condition>, "max": 10 }` runs them until the condition is true, but never more than `max` times;
`max` is required.

`forEach` runs its `steps` once for each actor it finds (`"find"`) or each spot in a list
(`"spots": [[x, y, z], ...]`). `"as"` names the one being visited. Inside, `{{seq.<as>.x}}`, `.y`, `.z`, `.loc`,
`.id`, `.name` and `.distance` read it.

Here the group runs to each light the boss calls, while the lights are up and the boss is not on top of them:

```json
    {
      "stepId": "named1.lights",
      "when": [
        {
          "count": {
            "of": "actors",
            "find": {
              "query": "Name == \"boss_01_knight_light\" && Distance < 100"
            },
            "compare": ">=",
            "value": 1
          }
        },
        ...
      ],
      "repeat": {
        "until": [
          ...
        ],
        "max": 10
      },
      "steps": [
        {
          "stepId": "named1.light",
          "forEach": {
            "find": {
              "query": "Name == \"boss_01_knight_light\" && Distance < 100"
            },
            "as": "light",
            "max": 1
          },
          "steps": [
            ...
            {
              "stepId": "named1.light.go.group",
              "do": "campSpot",
              "op": "setLoc",
              "x": "{{seq.light.x}}",
              "y": "{{seq.light.y}}",
              "z": "{{seq.light.z}}",
              "sendTo": "igwbn:{{me}}"
            },
            {
              "stepId": "named1.light.there",
              "wait": "atCampSpot",
              "limitMs": 15000,
              "onTimeout": "proceed"
            },
            ...
```

A loop step has no `do` of its own: the work goes in its `steps`. Loops can sit inside loops.

The steps inside a loop are checked when the file loads, the same as every other step.

### Values you can use in text

Anything in `{{ }}` inside a step's text is filled in when the step runs. The `ic` ones:

| Value | What it holds |
|---|---|
| `{{ic.zone.name}}`, `{{ic.zone.variant}}`, `{{ic.zone.fullName}}` | The zone, its difficulty (`[Heroic]`), and both together. |
| `{{ic.zone.tier}}` | Which root the file came from: `default`, `test` or `custom`. |
| `{{ic.zone.file}}` | The file's path inside its root. |
| `{{ic.zone.entrance}}` | The file's `entrance`. |
| `{{ic.zone.options.<name>}}` | The file's own `options`. |
| `{{ic.options.<name>}}` | The IC window's options, as `TRUE`/`FALSE` (or text): `haltAtEnd`, `loop`, `zoneIn`, `resetZones`, `afterWipe`, `skipBoss`, `skipShinies`, `pauseForNoTradeShinies`, `doNotLootNoTradeBossChest`, `summonMenderToSell`, `callGHAfterEachZone`, `stayInZoneUntilZoneReady`, `skipGroupChecks`, `fileOption1` to `fileOption3`, `fileArgs`. |
| `{{ic.run.verdicts.<stepId>}}` | How a step ended. `named`, `loot` and `zoneOut` steps record one: `killed`, `looted`, `zonedOut` and so on. |
| `{{ic.run.id}}`, `{{ic.run.attempts}}` | This run's id, and how many tries it has had (1, then one more after each wipe recovery). |
| `{{ic.run.completed}}`, `{{ic.run.skipped}}` | The steps (by `stepId`) known to be done or skipped. |
| `{{ic.list.name}}`, `{{ic.list.entry}}`, `{{ic.list.of}}` | The list this run is part of, which row it is, and how many rows there are. Empty when the zone was run on its own. |
| `{{ic.group.size}}`, `{{ic.group.mode}}` | How many are in the group, and `group` or `raid`. |
| `{{me}}` | The IC character's name. |
| `{{encounter.<name>}}` | A value saved during this run, for example a [`groupQuery`](#groupquery) answer. |

- A name that does not exist reads as empty text. Only the first word after `ic.` is checked when the file loads,
  so `{{ic.option.loop}}` is refused, but a misspelling further in (`{{ic.zone.nmae}}`) just reads empty.
- A LavishScript value is written `LavishScript["${Me.Name}"]`. A bare `${...}` is refused when the file loads.
- While a zone runs, `ogre ic value` in the console prints all of these, and `ogre ic value run.id` prints one.

## The way out

**Every zone file must say how it leaves the zone.** It needs a `zoneOut` step somewhere in `enter`, `steps` or
`exit` (inside a loop counts). A file without one is skipped when IC loads it, with this line in the log:

```
no way out: every zone file states its exit - add { "stepId": "exit", "do": "zoneOut", "op": "auto" } as its last step ...
```

That way a zone never just ends with the group still standing in it, and you can always see from the file how it
leaves. (Files that hand the zone to a script with `run` are left out of this rule: the script leaves its own way.)

| `op` | What it does |
|---|---|
| `door` | Clicks the exit you name: `{ "do": "zoneOut", "op": "door", "name": "Exit" }`. The name must be exact. |
| `auto` | The built-in zone out, the same as Classic's: finds the nearest clickable exit named `zone exit`, `exit`, `zone_exit` or `exit_spawned` anywhere in the zone, walks the group there and clicks it. If it finds none, the step fails, and the log lists what is clickable nearby, so you can see the exit's real name and use it with `door`. |
| `endOfZone` | Like `auto`, but only looks within `searchWithin` meters (100 if left out). For the exit that appears near the last boss once it is dead. If it is not there, that is not a failure, and the next step runs: put a fallback after it. |
| `none` | Stays in the zone, on purpose. The zone end options still run first. It takes no other keys. |

Keys for `door`, `auto` and `endOfZone`:

| Key | Default | What it does |
|---|---|---|
| `name` | `door`: required. `auto`, `endOfZone`: the four names above | The exit to click. `auto` and `endOfZone` also take a list of names. |
| `destination` | the last row | When the zone list pops up, which row to pick: its text, or its number (1 = the first). |
| `within` | `30` | How close the group must be to click. |
| `walk` | `door`: `false`. `auto`, `endOfZone`: `true` | Walk the group to the exit when it is farther than `within`. With `false`, walk there with a `path` step first. |
| `findLimitMs` | `10000` | How long to look for the exit. |
| `zoneLimitMs` | `40000` | Zoning must start this soon after the click. IC clicks once more, then gives up. |
| `groupLimitMs` | `120000` | How long to wait for everyone to arrive in the new zone. |

What happens at a `zoneOut` step, in order:

1. **Halt at end of zone**, if it is ticked: IC halts here, inside the zone, until you press Resume.
2. The zone end options: **Call to guild hall after each zone** or **Stay in zone until a zone is ready**.
3. Just before the group moves to the exit, a Paladin's Consecrate and a Berserker's Open Wounds are cancelled, so
   they do not pull more on the way.
4. Everyone clicks the exit, and the zone list's row is picked for everyone.
5. In the new zone, IC waits for the group. Anyone who lands in a different copy of the zone (Phantom Seas 3
   instead of 2) is asked to come to the leader's copy, up to three times.

A zone out that fails does not fail the zone: the run still counts as done, with a failure noted.

**With Loop on**, a zone never starts again inside the instance it just finished. If a zone's exit did not take the
group out, the list stops and says so. Stop and Run starts it again where you stand.

## The steps, one by one

### path

Moves the group along a list of spots, in order. At each spot it waits until everyone is there, alive and out of
combat, then goes on.

```json
{ "stepId": "named1.walk", "do": "path", "using": "nav", "spots": [[-793.151367, 144.102356, 353.17868]] }
```

| Key | Default | What it does |
|---|---|---|
| `using` | required | `"nav"`: everyone finds their own way there. `"campspot"`: moves the group's camp spot from spot to spot, in straight lines. |
| `spots` | required | The spots, `[x, y, z]` each, in order. |
| `groupWithin` | `10` | How close to the spot everyone must be before going on. |
| `spotLimitMs` | `30000` | Time allowed per spot. Fights, pauses and deaths do not count. |
| `onSpotTimeout` | `"retry"` | When a spot takes too long: `"retry"` it once, then fail; `"fail"`; or `"proceed"` to the next spot. |
| `waitForCombat` | `true` | Hold at each spot while anything is fighting the group. `false` to not hold, or the keys of [`waitForCombat`](#waitforcombat). |
| `fly` | `false` | With `nav`: fly where it can. |
| `waitForStragglers` | `true` | With `nav`: wait for anyone who falls far behind on the way. |
| `exitOnActorAggro` | | An actor's name. The walk ends the moment it is fighting the group. |
| `fromStart` | `false` | With `campspot`: always start at the first spot. Without it, a group already near a later spot joins the walk there. |
| `sendTo` | the whole group | Who walks. |

### named

Kills a named: buffs up, walks to the kill spot, pulls, fights, waits for it to die, then holds until the fight is
over.

```json
{ "stepId": "named1", "do": "named", "name": "Glorfab Flit", "spot": [-755.151001, 144.302704, 340.9729] }
```

| Key | Default | What it does |
|---|---|---|
| `name` | required | The named's exact name. |
| `spot` | | Where to fight it. |
| `navTo` | `false` | `true`: walk the group to the named itself, wherever it is, and fight it there. |
| `aliases` | | Other names it shows up or dies under: `["A Shade of X"]`. |
| `boss` | `false` | `true` for the zone's last boss: **Skip the boss** and the boss chest options apply to it. |
| `spawnWaitMs` | `0` | How long to wait for it to show up. |
| `pullLimitMs` | `30000` | It must be fighting the group this soon after the pull. |
| `limitMs` | `3600000` | The longest the whole fight may take. |
| `scanRadius` | `50` | How far out to look for it when pulling. |
| `scanHeight` | | How far up or down to look for it when pulling. |
| `prebuffMs` | `10000` | How long to let the group buff up first. `0` for no buff-up. |
| `waitForCombat` | `true` | The hold after the kill, as for `path`. |

It records `killed`, `alreadyDead`, `skipped` (Skip the boss), `neverSpawned` or `timedOut`. A named that never
spawns does not fail the zone; the run goes on and notes it.

### loot

Loots the chest, or the shinies. The group goes to them if needed, waits for the looting, then goes back.

```json
{ "stepId": "named1.chest", "do": "loot", "op": "chest" }
```

| Key | Default | What it does |
|---|---|---|
| `op` | required | `"chest"` or `"shinies"`. |
| `within` | `75` | How far to look. |
| `boss` | `false` | `true` on the boss chest: **Skip no-trade boss chest** applies to it. |
| `back` | `true` | Go back to where the step started afterwards. |
| `noTrade` | the IC window's options | `"loot"` or `"skip"`: what to do with no-trade items, for this step only. |

It records `looted`, `nothingToLoot`, `left` (something was left, said in the log) or `skipped`. A loot step never
fails the zone.

### zoneOut

The way out. See [The way out](#the-way-out).

### teleporter

Takes the group through a teleporter inside the zone. Everyone clicks it, then IC waits until everyone has moved.

```json
{ "stepId": "named2.teleporter", "do": "teleporter", "name": "telelport crystal", "landing": [-870.090027, 200.009995, 278.209991] }
```

| Key | Default | What it does |
|---|---|---|
| `name` | required | The teleporter's exact name. Copy it from the game: this one really is spelt `telelport crystal`. |
| `landing` | | Where it puts the group. With it, a run that starts part-way can begin on the far side. |
| `walkOnto` | | For a portal you walk onto instead of clicking: its `[x, y, z]`. Needs `landing`. Use it instead of `name`. |
| `limitMs` | `20000` | How long everyone has to get through. |

### hunt

Kills everything with a name like `name`, until `until` appears. For nameds that spawn after their adds die.

```json
{ "stepId": "named3.hunt", "do": "hunt", "name": "Mucktail", "until": "Vexven Mucktail" }
```

| Key | Default | What it does |
|---|---|---|
| `name` | required | Part of the name of the mobs to kill. |
| `until` | required | The exact name of what ends the hunt: once it is up, the group goes to it and the step ends. |
| `untilLine` | | A chat line that ends the hunt too, when part of it matches. |
| `spots` | | Where to look from when nothing is in sight, in turn. |
| `limitMs` | `900000` | The longest the hunt may take. |

Running out of time does not fail the zone. During the hunt, the IC character's AutoTarget is on, with a 35 meter
radius. When the hunt ends, it goes back to how it was.

### waitForCombat

Holds while anything is fighting the group. `path` and `named` do this by themselves; this step is for the places
in between.

```json
{ "stepId": "settle", "do": "waitForCombat", "noProgressMs": 20000, "onNoProgress": "moveOn" }
```

| Key | Default | What it does |
|---|---|---|
| `settleMs` | `2000` | When a mob is close, give it this long to join in first. |
| `settleWithin` | `15` | How close "close" is, in meters. |
| `noProgressMs` | `15000` | A fight where nothing changes for this long is stuck. |
| `onNoProgress` | `"moveOn"` | A stuck fight: `"moveOn"` and leave it, or `"fail"`. A named is never left. |
| `limitMs` | none | The longest the step may hold. Reaching it while still fighting fails the step. |

### waitForLoot

Waits until OgreBot has looted everything in reach.

| Key | Default | What it does |
|---|---|---|
| `settleMs` | `3000` | Give the loot this long to show up. |
| `limitMs` | `120000` | The longest it waits. `0` for no limit. |
| `onTimeout` | `"proceed"` | At the limit: `"proceed"` or `"fail"`. |

### trash

Clears every mob inside a circle around where the step starts, one at a time. Can also hold for waves.

```json
{ "stepId": "ring.trash", "do": "trash", "radius": 40, "until": "Ring Master", "whenEmpty": "wait", "quietMs": 60000 }
```

| Key | Default | What it does |
|---|---|---|
| `radius` | `30` | The circle, in meters. |
| `types` | `["NPC"]` | What counts: `"NPC"`, `"NamedNPC"`, `"Special"`. |
| `until` | | An exact name. The step ends when it appears. |
| `whenEmpty` | `"done"` | When the circle is clear: `"done"`, or `"wait"` for the next wave. |
| `quietMs` | `60000` | With `wait`: the step ends after this long with nothing in the circle and nothing fighting the group. |
| `move` | `"none"` | `"nav"` or `"campspot"` to walk to mobs more than 20 meters away. The group comes back at the end. |
| `limitMs` | `600000` | The longest it may take. Reaching it fails the step. |

### reward

Takes a reward from the reward window.

```json
{ "stepId": "boss.reward", "do": "reward", "choose": 2 }
```

| Key | Default | What it does |
|---|---|---|
| `choose` | required | Which reward: its number (1 = the first) or its name. |
| `limitMs` | `5000` | How long to wait for the window. |
| `sendTo` | the whole group | Who takes it. |

### groupQuery

Asks the whole group a question and saves the answers, so later steps can act on them.

```json
{ "stepId": "bots", "do": "groupQuery", "var": "bots", "question": "itemCount", "item": "Mechanized Platinum Repository of Reconstruction" }
```

| Key | What it does |
|---|---|
| `var` | The name the answers are saved under. |
| `question` | `"itemCount"` with `item`, `"abilityReady"` with `ability`, `"slotResolve"` with `slot`, or `LavishScript["${...}"]`, which each member works out for themselves. |
| `compare`, `value` | Together: turns each answer into a yes or a no, for example `"compare": ">="`, `"value": 1`. |
| `sendTo` | Who is asked. The whole group if left out. |
| `limitMs` | How long to wait for answers: `3000` if left out. |

The answers are read as `{{encounter.<var>.<answer>}}`: `askedCount`, `answeredCount`, `yesCount`, `noCount`,
`missingCount`, `allYes`, `anyYes`, `allNo`, `anyNo`, `yesWho`, `noWho`, `missingWho`, and for each member
`answer.<Name>`, `yes.<Name>`, `no.<Name>`, `missing.<Name>`.

### progress

Marks a step as done (`"op": "complete"`) or skipped (`"op": "skip"`), so a later start or resume leaves it out.

```json
{ "stepId": "progress.1", "do": "progress", "op": "complete", "id": "named1" }
```

### recover

The wipe recovery steps, for `onWipe` and `afterWipe`. `op` is `"revive"`, `"evac"` (back to the `entrance`),
`"callGH"` or `"callHome"`. `limitMs` is how long each may take. A `revive` can take `at`: the row of the revive
window to use, like `"Entrance"`.

```json
"onWipe": [
  { "stepId": "wipe.revive", "do": "recover", "op": "revive", "limitMs": 20000 }
]
```

## Other actions

These come from fight files, and the shipped zone files use them too. They run on the IC character. Add
`sendTo` to have others do it as well: `"sendTo": "igwbn:{{me}}"` is everyone in the group but the IC character.

| Action | What it does |
|---|---|
| `announce` | Writes `message` in the IC character's console. `"console": true` sends it to every character's console. |
| `autotarget` | The IC character's AutoTarget: `"op": "addActor"` with `name`, `"removeActor"`, `"clear"`, or `"set"` with `radius`, `height` or `enabled`. |
| `campSpot` | Camp spots: `"op": "enable"`, `"setLoc"` with `x`, `y`, `z`, or `"clearAll"`. Takes `sendTo`. |
| `actorInteract` | Clicks an actor by `name` (`"op": "doubleClick"`, which takes `sendTo`), or targets it (`"op": "target"`). An actor that is not there fails the step, so it is often written with `"onFail": "proceed"`. |
| `movement` | `"op": "setRunMode"` with `"mode": "walk"` or `"run"`. Takes `sendTo`. IC sets running back when the zone ends. |
| `ogreBotUIOption` | Ticks or unticks an OgreBot option by its `id` (`"value": "TRUE"` / `"FALSE"`), or puts it back (`"op": "restore"`). Takes `sendTo`. |
| `raw` | Runs any InnerSpace `command` on the IC character. |

These are checked when the file loads, by the same rules fight files use. A missing key the action needs, or a wrong
`op`, skips the file. A key the action does not read is a warning.

## Checking your file

Press **Reload** after every change. A file with a problem is **skipped**: it does not show in the IC window, and
`ogre ic reload` says why, one line per problem, like this:

```
custom/My Zone.json: steps[3]: path: `using` must be "campspot" or "nav"
```

`steps[3]` is the third step in `steps`; a step inside a loop shows as `steps[5].steps[1]`.

Some things only **warn**: the file still loads, but read the warning. The most common is a key nothing reads, which
is usually a typo:

```
custom/My Zone.json: steps[3]: path: 'spotLimitMS' is not a field of this action - nothing reads it, so as written it does nothing - did you mean 'spotLimitMs'?
```

Two mistakes are not caught when the file loads: a misspelt condition (in `when`, `wait` or `until`), and two
steps with the same `stepId`. So watch the log the first time a new file runs.

## Checklist

- [ ] `zone` and `variants` match what the game shows for the zone.
- [ ] Every named step has a `stepId` (`named1`, `named2`, ...), and the steps that go with it are named after it
      (`named1.walk`, `named1.chest`).
- [ ] The last boss has `"boss": true`.
- [ ] The file has an `entrance`.
- [ ] The file has a `zoneOut` step: `auto`, or `door` with the exit's name.
- [ ] **Reload** says `0 skipped, 0 warning(s)`.
