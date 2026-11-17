# ISXOgreEQ2.QuestHelper

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Methods

### `Help`

`ISXOgreEQ2.QuestHelper:Help`

Prints the `ogre quest` usage lines (start, stop, status, list, reload) to the console.

```text
ISXOgreEQ2.QuestHelper:Help
```

### `List`

`ISXOgreEQ2.QuestHelper:List`

Prints what the loaded reply table holds: the total rule count, the rules that apply in every zone, the rules in each zone's own list, and the counts of ignored objects and chat captures. A zone that has its own list does not also use the every-zone rules.

```text
ISXOgreEQ2.QuestHelper:List
```

### `Off`

`ISXOgreEQ2.QuestHelper:Off`

Stops the quest helper and prints its hail, object-click and reply counts, which add up across every run this session. When it is not running it prints 'questhelper: not running.' instead.

```text
ISXOgreEQ2.QuestHelper:Off
```

### `On`

`ISXOgreEQ2.QuestHelper:On[option1]`

Starts the quest helper (`ogre quest`), which runs until QuestHelper:Off and about every half second answers an open NPC conversation from its reply table (or takes the only reply), otherwise hails a non-attackable NPC within 10 units that has a quest to give, update or complete, otherwise double-clicks an interactable object within 5 units that is not on its ignore list and is not a way out of the zone (a name with the word zone, teleporter or exit), logging every hail and click with its zone. It does nothing while you are moving, out of the world or in a guild hall, the hail goes through the bot's queued Hail action, and it prints one line when it starts (or says it is already running).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `option1` | int | `none` | Optional. 1 = always click reply 1 and ignore the reply table; leave it out to use the table. Any other value is refused with one line and nothing starts. Calling On again while it runs switches this mode. |

```text
ISXOgreEQ2.QuestHelper:On[1]
```

### `Reload`

`ISXOgreEQ2.QuestHelper:Reload`

Re-reads the reply table from the shipped files (Scripts/Ogre/EQ2/QuestHelper/default) and your own (Scripts/OgreSave/EQ2/QuestHelper/custom), warns about each file that fails to load, and prints the rule count. If no file loads at all, the table already in use is kept and the line says so instead of a loaded count.

```text
ISXOgreEQ2.QuestHelper:Reload
```

### `Status`

`ISXOgreEQ2.QuestHelper:Status`

Prints the quest helper's state to the console: running or stopped, whether it always takes reply 1, your zone, what it last did, how long since it last acted, its hail, object-click and reply counts for this run (they start from 0 at each start), and how many reply rules are loaded.

```text
ISXOgreEQ2.QuestHelper:Status
```
