<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# ISXOgreEQ2.AbilityUpgrades

## Methods

### `Run`

`ISXOgreEQ2.AbilityUpgrades:Run[minLevel]`

With a container window open it reads that one and leaves it open; otherwise it opens each Scroll Depot within 30 units in turn, reads it and closes it, and either way reports which spell scrolls upgrade an ability you already know, both in your console and to your other sessions through the Ogre console with your name in front (the same as `ogre oau`). It is queued, scribes or uses nothing, and is refused with a console line when you are not in the world, no ability export is loaded, a scan is already running or the level is not a whole number from 1 to 1000.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `minLevel` | int | `121` | ignore scrolls below this level (1 to 1000); -h prints the usage instead |

```text
ISXOgreEQ2.AbilityUpgrades:Run[125]
```
