# The steps, one by one

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../index.md).
</div>

## path

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
| `killWithin` | | Meters, up to `100`. Kill the trash on the way: when a mob comes this close, the group stops where it is, kills every mob that close, then walks on. |
| `killTypes` | `["NPC"]` | With `killWithin`: the kinds of mob to stop for, as for [`trash`](#trash): `"NPC"`, `"NamedNPC"`, `"Special"`. |
| `killLimitMs` | `120000` | With `killWithin`: the longest one stop may take. Then the mob is left behind, the console says so, and the walk goes on. |

**Example: walk to the named, killing the trash on the way.** The group walks past two spots to the named. Any mob
that comes within 15 m of the IC character stops the walk until it is dead. A mob that is not dead after a minute is
left behind.

```json
{ "stepId": "named2.walk", "do": "path", "using": "nav",
  "spots": [[-310.4, 52.1, 118.7], [-262.9, 55.8, 160.3], [-221.0, 58.2, 204.6]],
  "killWithin": 15, "killLimitMs": 60000 },
{ "stepId": "named2", "do": "named", "name": "The Named", "spot": [-205.3, 58.9, 221.4] }
```

- **A stop.** The walk halts where the IC character is. With `nav` the group gathers on the IC character; with
  `campspot` everyone's camp spot is put where the IC character stands. Every mob of `killTypes` within `killWithin`
  is then pulled and killed from there, one at a time, the same way a [`trash`](#trash) step kills. When none is
  left, the walk goes on to the spot it was walking to.
- **Only what comes close.** The walk never leaves its way to look for a mob. To clear a whole room, put a
  [`trash`](#trash) step at the spot instead.
- **Nameds are walked past.** Add `"killTypes": ["NPC", "NamedNPC"]` to stop for them too. Anything that attacks the
  group is fought either way.
- **Left behind.** When a stop takes longer than `killLimitMs`, the console names the mobs it leaves, and the walk goes
  on. That is not a failure. The walk does not stop for those mobs again on that stretch (a `nav` walk goes in
  stretches of about 50 m).
- **Time.** The stops do not count against `spotLimitMs`.
- **The console** says each stop and what it is for (`named2.walk: a bog slug 12 m away - stopping to kill it`), and
  how many were killed when the walk goes on.

## named

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

## loot

Loots the chest, the shinies or the corpses. The group goes to them if needed, waits for the looting, then goes back.

```json
{ "stepId": "named1.chest", "do": "loot", "op": "chest" }
```

A chest is found by its kind (the game's actor type "Chest"), not by its name. When the named was killed moments ago and
no chest is there yet, the step waits up to 8 seconds after the kill for one to appear.

| Key | Default | What it does |
|---|---|---|
| `op` | required | `"chest"`, `"shinies"` or `"corpses"`. |
| `within` | `75` (`50` for corpses) | How far to look. For corpses it is measured from where the step started. |
| `boss` | `false` | `true` on the boss chest: **Skip no-trade boss chest** applies to it. |
| `back` | `true` | Go back to where the step started afterwards. |
| `noTrade` | the IC window's options | `"loot"` or `"skip"`: what to do with no-trade items, for this step only. |
| `corpses` | `true` | Chest only: loot the corpses after the chest. `false` leaves them. |
| `corpsesWithin` | `50` | Chest only: how far from where the step started to look for corpses. |

A chest step also loots the corpses around it once the chest is done. The group walks to each corpse that has not
been looted yet, nearest first, waits for OgreBot to loot it, and goes back once at the end. `op: "corpses"` does
only that, for use anywhere, such as after a trash pull. The corpses are skipped when **Do not loot Corpses** is
ticked on OgreBot's Loot tab, or when OgreBot looting is off; the log says so. The corpses stop after two minutes,
not counting fights. For corpses, `within` and `corpsesWithin` go up to `100`, and a bigger one is used as `100`. A
`corpses` that is not `true` or `false`, or a `corpsesWithin` that is not a number above 0, is ignored. The load says
each of these.

It records `looted`, `nothingToLoot`, `left` (something was left, said in the log) or `skipped`. On a chest step it is
the chest's result; the corpses are added to the same log line. A loot step never fails the zone.

## zoneOut

The way out. See [The way out](how-it-runs.md#the-way-out).

## teleporter

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

## hunt

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

## waitForCombat

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

## waitForLoot

Waits until OgreBot has looted everything in reach.

| Key | Default | What it does |
|---|---|---|
| `settleMs` | `3000` | Give the loot this long to show up. |
| `limitMs` | `120000` | The longest it waits. `0` for no limit. |
| `onTimeout` | `"proceed"` | At the limit: `"proceed"` or `"fail"`. |

## trash

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

To kill the trash on the way to a spot rather than around one, give the [`path`](#path) step `killWithin`.

## reward

Takes a reward from the reward window.

```json
{ "stepId": "boss.reward", "do": "reward", "choose": 2 }
```

| Key | Default | What it does |
|---|---|---|
| `choose` | required | Which reward: its number (1 = the first) or its name. |
| `limitMs` | `5000` | How long to wait for the window. |
| `sendTo` | the whole group | Who takes it. |

## groupQuery

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

**Example: wait until someone's Bladedance is ready.** A loop asks the group every 2 seconds and stops once anyone
answers yes. Each member checks its own Bladedance; a member without it answers no.

```json
{ "stepId": "bladedance", "repeat": { "until": { "varEquals": { "scope": "encounter", "name": "bd.anyYes", "value": "TRUE" } }, "max": 30 },
  "steps": [
    { "stepId": "bladedance.ask", "do": "groupQuery", "var": "bd", "question": "abilityReady", "ability": "Bladedance" },
    { "stepId": "bladedance.gap", "wait": "ms", "limitMs": 2000, "onTimeout": "proceed" }
  ] }
```

- To wait for one member's, add `"sendTo": "Mirelle"` to the `groupQuery` step, so only Mirelle is asked.
- The loop checks `until` after each pass. After `max` passes (about two and a half minutes here, since each ask can
  take up to 3 seconds) it stops waiting and the zone goes on. It does not fail.
- A misspelt answer name, like `bd.anyYess`, is refused when the file loads.

## progress

Marks a step as done (`"op": "complete"`) or skipped (`"op": "skip"`), so a later start or resume leaves it out.

```json
{ "stepId": "progress.1", "do": "progress", "op": "complete", "id": "named1" }
```

## recover

The wipe recovery steps, for `onWipe` and `afterWipe`. `op` is `"revive"`, `"evac"` (back to the `entrance`),
`"callGH"` or `"callHome"`. `limitMs` is how long each may take. A `revive` can take `at`: the row of the revive
window to use, like `"Entrance"`. When the window has no such row, each character revives at the last revive point
the window lists and says which.

```json
"onWipe": [
  { "stepId": "wipe.revive", "do": "recover", "op": "revive", "limitMs": 20000 }
]
```
