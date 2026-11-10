# How a zone file runs

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../index.md).
</div>

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
| `onWipe` | | Your own wipe recovery steps (see [`recover`](steps.md#recover)). Leave it out for the built-in recovery. `[]` means no recovery: the first wipe gives the zone up. |
| `afterWipe` | | Your own steps for when the zone is given up. Leave it out for the built-in ones: revive, then whatever the IC window's **After a lost zone** says. |
| `fileOptions` | | Up to 3 names for the IC window's **IC File Option 1-3** boxes: `["Skip the side named"]`. Your steps read the boxes as `{{ic.options.fileOption1}}` (`TRUE` or `FALSE`), and the **IC File Args** box as `{{ic.options.fileArgs}}`. |
| `options` | | Your own values for this file. Steps read them as `{{ic.zone.options.<name>}}`. IC itself does nothing with them. |
| `difficulty` | | A difficulty menu for the IC window: `{ "choices": ["Easy", "Hard"] }` or `{ "minValue": 1, "maxValue": 5 }`. The run does not use it yet. |
| `run` | | Hands the zone to a script instead of steps: `{ "iss": "<path under Scripts>" }`, or to another zone file in the same root: `{ "json": "<path>" }`. A file has steps or `run`, never both. A script must call `ISXOgreEQ2.IC:Complete` when it is done, or the run counts as failed. |
| `expansion`, `author` | | Notes for people. IC does not use them. |

**A key IC does not read does nothing, and Reload says so.** It is a warning, so the file still loads. The line
names the key and the nearest key IC does read (see [Checking your file](checking.md#checking-your-file)). A key starting with
`_`, like `_comment`, is a note: it is never said, so use it for notes.

## How a run goes

- **Before the first step**, IC applies your Startup Options. After a zone-in, it waits until everyone has
  arrived, then gives the group a few seconds to rebuff.
- **The lists run in order: `enter`, then `steps`, then `exit`.** One step at a time, on the character that runs
  IC. Steps like `path`, `named`, `loot` and `zoneOut` move the whole group; most other actions act on the IC
  character alone unless they take `sendTo` (see [Other actions](other-actions.md)).
- **A step that fails** ends its list (see `onFail` below). If `enter` fails, `steps` does not run. `exit` still runs
  after a failure.
- **When `steps` finish**, **Halt at end of zone** pauses IC right there, inside the zone. The zone end options
  (Call to guild hall after each zone, Stay in zone until a zone is ready) run at the `zoneOut` step.
- **A `zoneOut` that takes the group out ends its list.** Anything after it in that list is skipped.
- **End**, **Max wait per zone** and closing the IC window stop the run where it stands. `exit` does not run.
- **Wipes** are watched during `enter` and `steps`. IC runs the wipe recovery, then starts the zone again, leaving
  out what is already done. The built-in recovery revives everyone at the entrance, evacuates if they are not there,
  and then rests for a minute so revive sickness wears off and buffs go back up. After `wipeAttempts` recoveries, IC gives the zone up: the `afterWipe` steps run, `exit`
  does not, and the list moves on to the next zone.
- **Starting part-way.** The IC window's **named #** starts a zone at a named: IC backs up over the steps that lead
  to it (its walk, for instance) so they run too. It only works when you are already standing in that zone. A run
  that zones in always starts from the top.

## Steps

```json
{ "stepId": "named1.chest", "do": "loot", "op": "chest" }
```

Every step that does something has a **`do`**: the action. The rest of the keys belong to that action. All the
actions are listed in [The steps, one by one](steps.md).

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

`forEach` can also walk saved values: `"vars": { "prefix": "<start of the name>" }` visits every value whose name
starts with it, and `{{seq.<as>.name}}` is the rest of the name. Add `"groupMember": true` when that rest is a
character's name: only members of the group are visited, with their names spelt as the game spells them.

**Example: the first character with Escape ready casts it.** No character name is written into the file. Each member
answers for itself, and `max: 1` stops after the first yes. If nobody has it ready, nothing is cast and the zone goes on.

```json
{ "stepId": "escape.ask", "do": "groupQuery", "var": "escapeReady", "question": "abilityReady", "ability": "Escape" },
{ "stepId": "escape.first",
  "forEach": { "vars": { "prefix": "escapeReady.yes.", "groupMember": true }, "as": "caster", "max": 1 },
  "steps": [
    { "stepId": "escape.cast", "do": "castAbility", "ability": "Escape", "sendTo": "{{seq.caster.name}}" }
  ] }
```

"First" means first in alphabetical order among the members who answered yes, not first in the group.

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
| `{{encounter.<name>}}` | A value saved during this run, for example a [`groupQuery`](steps.md#groupquery) answer. |

- A name that does not exist reads as empty text. Only the first word after `ic.` is checked when the file loads,
  so `{{ic.option.loop}}` is refused, but a misspelling further in (`{{ic.zone.nmae}}`) just reads empty.
- A LavishScript value is written `LavishScript["${Me.Name}"]`. A bare `${...}` is refused when the file loads.
- While a zone runs, `ogre ic value` in the console prints all of these, and `ogre ic value run.id` prints one.

## The way out

**Every zone file must say how it leaves the zone.** It needs a `zoneOut` step somewhere in `enter`, `steps` or
`exit` (inside a loop counts). A file without one is **not valid**: it still shows in the Instance Controller's zone
list, in red and marked *not valid*, but it cannot be queued or run. Click it and the bar under the list says why:

```
no way out: every zone file states its exit - add { "stepId": "exit", "do": "zoneOut", "op": "auto" } as its last step ...
```

Every other reason a file cannot load (a JSON mistake, an unknown step) is shown the same way, all of them at once.

That way a zone never just ends with the group still standing in it, and you can always see from the file how it
leaves. (Files that hand the zone to a script with `run` are left out of this rule: the script leaves its own way.)

**A zone with no exit of its own** needs nothing made up: end it with `{ "stepId": "exit", "do": "zoneOut", "op": "none" }`.
`none` still runs the Instance Controller's end of zone first, so with **Call to GH after each zone** ticked the group
is called to the guild hall; without it, the group stays in the zone.

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
