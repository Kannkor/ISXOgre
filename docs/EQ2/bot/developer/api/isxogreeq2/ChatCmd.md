# ISXOgreEQ2.ChatCmd

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Methods

### `Debug`

`ISXOgreEQ2.ChatCmd:Debug[state]`

Turns the router's debug lines on or off. Anything but on, true or 1, or nothing, turns them off.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `state` | string |  | on, true or 1 turns it on. Optional: off when left out. |

```text
ISXOgreEQ2.ChatCmd:Debug[on]
```

### `Off`

`ISXOgreEQ2.ChatCmd:Off`

Turns chat commands off. The Broadcast guild talk box keeps working.

```text
ISXOgreEQ2.ChatCmd:Off
```

### `On`

`ISXOgreEQ2.ChatCmd:On`

Turns chat commands on: commands from your authorized characters are run.

```text
ISXOgreEQ2.ChatCmd:On
```

### `ReloadAuth`

`ISXOgreEQ2.ChatCmd:ReloadAuth`

Rebuilds the set of authorized characters from the accounts store and says how many names it holds.

```text
ISXOgreEQ2.ChatCmd:ReloadAuth
```

### `Status`

`ISXOgreEQ2.ChatCmd:Status`

Prints the router's state to the console: on or off, debug, the authorized names, and lines seen, dispatched and rejected.

```text
ISXOgreEQ2.ChatCmd:Status
```

### `Test`

`ISXOgreEQ2.ChatCmd:Test[chattype,speaker,message]`

A dry run: prints what would happen to a made-up chat line right now and runs nothing. With chat commands off it shows them off; with no chat type or speaker it prints one warning.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `chattype` | int |  | The chat type number. |
| `speaker` | string |  | Who said it. |
| `message` | string |  | What was said; every further argument joins it. Optional. |

```text
ISXOgreEQ2.ChatCmd:Test[16,Bob,"mount up"]
```
