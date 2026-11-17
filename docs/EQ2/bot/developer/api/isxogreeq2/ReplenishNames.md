# ISXOgreEQ2.ReplenishNames

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Methods

### `Reload`

`ISXOgreEQ2.ReplenishNames:Reload`

Re-reads both replenish name files now, warning in the console about any problem it finds, then prints the same report as ReplenishNames:Show. A changed file is picked up on its next use anyway, so this is only needed to see the result straight away.

```text
ISXOgreEQ2.ReplenishNames:Reload
```

### `Show`

`ISXOgreEQ2.ReplenishNames:Show`

Prints the fallback potion, food and drink names the replenish options use when nothing better is set, plus where the shipped file and your own file (OgreSave/EQ2/Replenish/custom/replenish-names.json) live. The files are re-read first when either has changed since the last read.

```text
ISXOgreEQ2.ReplenishNames:Show
```
