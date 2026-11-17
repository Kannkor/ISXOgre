# OgreBotAPI.Overseer

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Methods

### `AddAgents`

`OgreBotAPI.Overseer:AddAgents[fw, destroy=TRUE]`

Adds every Overseer agent card in your bags and Overseer bag to your agent collection, one card per pulse, and prints a count of added, duplicate, converted and destroyed cards when done. With destroy TRUE a duplicate is converted when that gives items and destroyed otherwise (one whose item details do not load in time is left); with FALSE duplicates are kept, and a second call while a pass runs is refused with a console warning.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `destroy` | bool | `TRUE` | TRUE converts or destroys duplicate cards; FALSE keeps them (any word that is not a yes word counts as FALSE) |

```text
OgreBotAPI.Overseer:AddAgents[igw:${Me.Name},FALSE]
```

*Was (OldBot):* `OgreBotAPI:Overseer_AddAgentsToCollection`

### `AutoAddQuests`

`OgreBotAPI.Overseer:AutoAddQuests[fw]`

Uses every Overseer mission scroll in your bags and Overseer bag - the same add pass the daily run does, on its own. It is refused with a console warning while the daily run or another add pass is going.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.Overseer:AutoAddQuests[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Overseer_AutoAddOverseerQuests`

### `BuyMissions`

`OgreBotAPI.Overseer:BuyMissions[fw, flag...]`

Queues an Overseer mission buy run at the merchant, started on the next pulse; with no flags it uses this character's own Overseer Buy tab, and flags such as -season 3, -colour Blue, -num 2, -amount 5, -replenishonly, -noscribe or -destroy override it, each as its own argument (a first word that is not a flag gets one line and starts nothing, a later unknown word is skipped). It needs OgreBot open with a profile loaded and is refused with a console warning when a buy run is already going, and a second call before the next pulse replaces the first.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `flag...` | string |  | Option flags for the run, one per argument, with a flag's value as the next argument (-season, 3); none uses this character's Overseer Buy tab |

```text
OgreBotAPI.Overseer:BuyMissions[igw:${Me.Name},-replenishonly]
```

### `CheckQuests`

`OgreBotAPI.Overseer:CheckQuests[fw]`

Starts the daily Overseer run now instead of waiting for the bot to start it; the run then works through its steps on the pulse. It is refused with a console warning when a run or an add-missions pass is already going or when 'Do not touch overseer at all no matter what' is ticked, and with OgreBot closed it runs on the default options.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.Overseer:CheckQuests[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Overseer_CheckQuests`
