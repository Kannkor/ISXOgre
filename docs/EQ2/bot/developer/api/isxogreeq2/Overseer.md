<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# ISXOgreEQ2.Overseer

## Methods

### `BuyMissions`

`ISXOgreEQ2.Overseer:BuyMissions[flag...]`

Starts a run that buys Overseer missions at the merchant on this session, using this character's Overseer Buy tab with any flags overriding it: -season N, -colour C, -num N, -amount N (at most 20), -replenishonly, -scribe or -noscribe, -destroy or -nodestroy, -gettogh or -nogettogh (go to the guild hall when done); unknown words are skipped. Refused with a console line when OgreBot is not open with a profile, a buy run is already going, or the first argument is not a -flag - the same run OgreBotAPI.Overseer:BuyMissions queues with a for-who.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `flag...` | string |  | Optional flags, one per argument, each value as its own argument after its flag; none uses the Overseer Buy tab as saved |

```text
ISXOgreEQ2.Overseer:BuyMissions[-season,2,-amount,5]
```

### `BuyMissionsStatus`

`ISXOgreEQ2.Overseer:BuyMissionsStatus`

Prints whether the Overseer mission buy run is idle or, if running, the phase it is in.

```text
ISXOgreEQ2.Overseer:BuyMissionsStatus
```

### `BuyMissionsStop`

`ISXOgreEQ2.Overseer:BuyMissionsStop`

Aborts the Overseer mission buy run in progress and prints the reason. Prints "nothing running." when idle; same as `ogre end buyoverseermissions`.

```text
ISXOgreEQ2.Overseer:BuyMissionsStop
```

### `Run`

`ISXOgreEQ2.Overseer:Run`

Starts a manual Overseer run on this session now, skipping the 60-minute throttle; it uses OgreBot's Overseer tab when OgreBot is open, and the defaults (complete finished quests, add bag missions, start mishaps and new quests, take rewards) when it is not. Refused with a console line when any argument is passed, a run is already going, a bag-mission add is busy, or 'Do not touch overseer at all no matter what' is ticked - the same run as OgreBotAPI.Overseer:CheckQuests and `ogre overseer`.

```text
ISXOgreEQ2.Overseer:Run
```

### `Status`

`ISXOgreEQ2.Overseer:Status`

Prints the Overseer run's current phase, whether it is running, and how many quests it has started and completed. When idle after a run it also prints roughly how many seconds until the next automatic run is allowed.

```text
ISXOgreEQ2.Overseer:Status
```

### `Stop`

`ISXOgreEQ2.Overseer:Stop`

Ends the Overseer run in progress on this session and prints "run aborted", or prints "nothing to stop" when idle. Same as `ogre end overseer`.

```text
ISXOgreEQ2.Overseer:Stop
```
