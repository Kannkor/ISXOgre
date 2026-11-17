<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# ISXOgreEQ2.AbilityEfficiency

## Methods

### `Run`

`ISXOgreEQ2.AbilityEfficiency:Run[-h]`

Scores every ability in your loaded ability export as the damage in its description divided by cast plus recovery time (recast is not counted), writes one Name\|Value line per ability best first to Scripts/OgreSave/EQ2/OgreBot/AbilityEfficiency/&lt;name>_&lt;subclass>_&lt;server>_AbilityEfficiency.txt and prints the top 20 (the same as `ogre ae`). With no export loaded it prints an error telling you to run `ogre export`, and any argument other than a help word is refused.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `-h` | switch |  | print the usage instead of running (-help, --help, ? and help work too) |

```text
ISXOgreEQ2.AbilityEfficiency:Run
```
