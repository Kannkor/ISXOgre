<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# ISXOgreEQ2.Watcher

## Methods

### `End`

`ISXOgreEQ2.Watcher:End`

Turns off both the name watch (Find) and the shiny watch (TrackShiny), closes the Watcher window and prints which of them were on; the off state is saved, so they stay off on the next load. This is what `ogre end watcher` and the window's close button do.

```text
ISXOgreEQ2.Watcher:End
```

### `Find`

`ISXOgreEQ2.Watcher:Find[word...]`

Watches for actors by exact name, case not mattering (`ogre find`): given names it replaces the watch list, arms and checks the zone once, then each time a watched name spawns it prints where, broadcasts '&lt;you>: APPEARED: &lt;name>' to your bot sessions and sets an in-game waypoint on it, and it prints when one despawns (these alerts are skipped in a guild hall). A first word that is an option does that instead (-add or -remove &lt;name>, -clear, -list, -on, -off, -scan, -status, -panel opens the Watcher window, -rorr adds the four Renewal of Ro researchers to the names), no words prints the usage, and the list and armed state are saved and restored on the next load.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `word...` | string | `none (prints the usage)` | the names to watch (quote a name that has spaces), or one option first followed by its value |

```text
ISXOgreEQ2.Watcher:Find[${Target.Name}]
```

### `TrackShiny`

`ISXOgreEQ2.Watcher:TrackShiny[word...]`

Watches for shiny harvest nodes of one colour within 100 units, every 500 ms by default (`ogre trackshiny`): when it finds one it did not just announce, it prints '&lt;colour> shiny!', broadcasts it to your bot sessions and sets an in-game waypoint on it. No word arms it on Purple, a colour name (White, Green, Purple, Red, BlueShimmer, Blue) arms that colour and an unknown one is refused with the list, the options are -off, -status, -colours (or -colors), -interval &lt;ms> (held to 250..30000) and -panel, and the settings are saved and restored on the next load.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `word...` | string | `Purple` | a colour to watch for, or one option first followed by its value |

```text
ISXOgreEQ2.Watcher:TrackShiny[Red]
```
