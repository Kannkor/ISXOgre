<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# ISXOgreEQ2.GetQuest

## Methods

### `Help`

`ISXOgreEQ2.GetQuest:Help`

Prints the `ogre getquest` usage lines (start, list, reload, status, stop) to the console, with the reminder that you must stand next to the NPC because it does not walk.

```text
ISXOgreEQ2.GetQuest:Help
```

### `List`

`ISXOgreEQ2.GetQuest:List`

Prints every loaded quest row: the quest name, the NPC to hail, the wanted step and the zones it is for, with rows that were never checked against the live game marked [UNVERIFIED]. Prints a warning when no rows are loaded.

```text
ISXOgreEQ2.GetQuest:List
```

### `Reload`

`ISXOgreEQ2.GetQuest:Reload`

Re-reads the quest rows from the shipped files (Scripts/Ogre/EQ2/GetQuest/default) and your own (Scripts/OgreSave/EQ2/GetQuest/custom) and prints how many loaded. It is refused with a warning while a run is active.

```text
ISXOgreEQ2.GetQuest:Reload
```

### `Start`

`ISXOgreEQ2.GetQuest:Start`

For the zone you are in (`ogre getquest`), hails the configured NPC and takes its quest, then deletes it from your journal and takes it again until it lands on the wanted step or the row's attempt cap (50 by default) runs out; it never walks, so stand within 15 units of the NPC first. It runs on the bot's action queue and refuses with one line while already running, out of the world, or when no row exists for the zone; it turns on the Do Not Accept Quests setting at the start and puts it back when the run ends, and a round that fails (NPC out of range, no conversation) prints why and ends the run; only a wrong step takes another round.

```text
ISXOgreEQ2.GetQuest:Start
```

### `Status`

`ISXOgreEQ2.GetQuest:Status`

Prints whether a quest reroll is running or idle, how many rows are loaded, your zone, the last result, and the session's run, success and failure counts.

```text
ISXOgreEQ2.GetQuest:Status
```

### `Stop`

`ISXOgreEQ2.GetQuest:Stop`

Aborts a running quest reroll, restores the Do Not Accept Quests setting and prints 'getquest: aborted (auto-accept restored).', and a round already under way stops at its next step. When nothing is running it prints 'getquest: not running.' instead.

```text
ISXOgreEQ2.GetQuest:Stop
```
