<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# ISXOgreEQ2.Codex

## Methods

### `End`

`ISXOgreEQ2.Codex:End`

Stops a running Codex inspect pass: drops the names still waiting, closes the inspect window and prints how many were not inspected - the same as ogre end codexinspect. Players already uploaded keep their cooldown; with no pass running it does nothing.

```text
ISXOgreEQ2.Codex:End
```

### `Inspect`

`ISXOgreEQ2.Codex:Inspect[names,setting]`

Queues the named players to be inspected one at a time, 3 s apart, each one an inspect request to the game server (a server request), and each uploaded to Codex as an active raid member - the same as ogre codexinspect. A name inspected in the last 5 minutes (by default) is skipped, reset clears the active raid roster on Codex, status (or ?) or no argument prints the status line, and the console says how many were queued.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `names` | string |  | a comma-separated list of player names, or reset, or status / ? |
| `setting` | string | `""` | optional; leave it out |

```text
ISXOgreEQ2.Codex:Inspect[status]
```

### `Toon`

`ISXOgreEQ2.Codex:Toon[word]`

Inspects your own character and uploads its snapshot to Codex - the same as ogre codextoon: it sends the game an inspect request for you (a server request), then uploads over the web and prints the result when the upload answers. With status (or ?) it only prints the Codex status line, and it refuses with a message when Codex is not set up, you are not in the world, or an upload is already running.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `word` | string | `""` | status or ? prints the Codex status line instead of uploading; leave it out to upload |

```text
ISXOgreEQ2.Codex:Toon[status]
```
