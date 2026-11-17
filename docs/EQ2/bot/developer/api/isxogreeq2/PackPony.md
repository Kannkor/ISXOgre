# ISXOgreEQ2.PackPony

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Methods

### `Start`

`ISXOgreEQ2.PackPony:Start[word,word]`

Sends the pack pony out and unloads it, once. An unknown word refuses the whole line and nothing starts; a run that cannot start says why.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `word` | string |  | nodismiss leaves the pony summoned afterwards. Optional. |
| `word` | string |  | nopause does not pause OgreBot for the run. Optional. |

```text
ISXOgreEQ2.PackPony:Start[nodismiss]
```

### `Status`

`ISXOgreEQ2.PackPony:Status`

Prints whether a run is going, its phase, and how the last run ended.

```text
ISXOgreEQ2.PackPony:Status
```

### `Stop`

`ISXOgreEQ2.PackPony:Stop`

Abandons a run in progress and cleans up after it. With no run it says so.

```text
ISXOgreEQ2.PackPony:Stop
```
