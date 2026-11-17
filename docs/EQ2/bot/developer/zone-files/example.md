# A zone file, start to finish

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../index.md).
</div>

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

Then come the **steps**. Each named gets a few: walk to it, kill it, loot what it left, and say how it went. A long
walk is cut into legs (`named1.walk.s01`, `named1.walk.s02`, and so on), and each leg is followed by a short
[waitForLoot](steps.md#waitforloot) whose `when` (see [Steps](how-it-runs.md#steps)) makes it run only when something
lies dead within 20 meters. Here is the last leg before the first named, and that named's own steps:

```json
    ...
    {
      "stepId": "named1.walk.s13",
      "do": "path",
      "using": "campspot",
      "spots": [
        [
          -793.151367,
          144.102356,
          353.17868
        ]
      ]
    },
    {
      "stepId": "named1.walk.s13.loot",
      "do": "waitForLoot",
      "settleMs": 1000,
      "limitMs": 15000,
      "onTimeout": "proceed",
      "when": [
        {
          "count": {
            "of": "actors",
            "find": {
              "query": "IsDead && Distance < 20"
            },
            "compare": ">=",
            "value": 1
          }
        }
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
      "stepId": "named1.corpses",
      "do": "waitForLoot",
      ...
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

`named1.corpses` is the same wait for loot as the one after each leg, for what the fight left on the ground.

And the file ends with **the way out**: the last leg and its wait for loot, then `endOfZone`, which clicks the exit
that appears near the last boss once it is dead. If that exit is not there, the next step runs, so the door step after
it is the fallback: it walks the group to the door called Exit and clicks it. Every zone file must have a way out (see
[The way out](how-it-runs.md#the-way-out)):

```json
    ...
    {
      "stepId": "exit.walk.s05",
      "do": "path",
      "using": "campspot",
      "spots": [
        [
          -772.972534,
          299.070923,
          249.26976
        ]
      ]
    },
    {
      "stepId": "exit.walk.s05.loot",
      "do": "waitForLoot",
      ...
    },
    {
      "stepId": "exit.endOfZone",
      "do": "zoneOut",
      "op": "endOfZone"
    },
    {
      "stepId": "exit.door",
      "do": "zoneOut",
      "op": "door",
      "name": "Exit",
      "walk": true
    }
  ]
}
```
