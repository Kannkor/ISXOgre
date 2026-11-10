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
[The way out](how-it-runs.md#the-way-out)):

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
