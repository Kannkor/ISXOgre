# ISXOgreEQ2.AbilityEfficiency

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Methods

### `Close`

`ISXOgreEQ2.AbilityEfficiency:Close`

Closes the Ability Efficiency window. This is what `ogre end ae` and the window's X do; nothing else is running to stop.

```text
ISXOgreEQ2.AbilityEfficiency:Close
```

### `Run`

`ISXOgreEQ2.AbilityEfficiency:Run[-nogui,-targets,n,-list]`

Scores every ability in your loaded ability export as the damage in its description divided by cast plus recovery time (recast is not counted), and with no argument opens the Ability Efficiency window, one column per number of targets (the same as `ogre ae`). With no export loaded it says to run `ogre export`, -h or help prints the usage, and any other word is refused.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `-nogui` | switch |  | write the report file instead of opening the window, best first, to Scripts/OgreSave/EQ2/OgreBot/AbilityEfficiency/&lt;name>_&lt;subclass>_&lt;server>_AbilityEfficiency.txt, and print the top 20 (classic OgreBot's `ae`) |
| `-targets` | switch |  | followed by n: the window opens with n target columns; with -nogui the file gets one column per number of targets, best first at n |
| `n` | int | `4 in the window (or its saved choice); none in the file` | the number of targets after -targets, 1 to 20 |
| `-list` | switch |  | the list layout: one line per ability and number of targets, best first (an AE repeats once per count); the window opens in it, and with -nogui the file is written in it |

```text
ISXOgreEQ2.AbilityEfficiency:Run[-nogui,-targets,6,-list]
```
