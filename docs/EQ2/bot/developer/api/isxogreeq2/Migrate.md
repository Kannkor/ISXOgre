<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# ISXOgreEQ2.Migrate

## Methods

### `Cancel`

`ISXOgreEQ2.Migrate:Cancel[task]`

Backs out of a pending overwrite confirmation for one task, putting its row back to its normal state. It does nothing when that task is not waiting for a confirmation or the name is unknown.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `task` | string |  | the task whose confirmation to cancel: accounts, imsettings, imlists, profiles, irc, mcp or isprofile |

```text
ISXOgreEQ2.Migrate:Cancel[profiles]
```

### `Close`

`ISXOgreEQ2.Migrate:Close`

Closes the Migration Assistant window and cancels its pending auto-close. Nothing that has already run is undone.

```text
ISXOgreEQ2.Migrate:Close
```

### `Open`

`ISXOgreEQ2.Migrate:Open`

Opens the Migration Assistant window (the same as `ogre migrate`), listing each migration task with its status and a re-run button. Before it opens it silently runs any task whose old file exists and whose new file does not, and when the window is already up it does nothing.

```text
ISXOgreEQ2.Migrate:Open
```

### `RequestRerun`

`ISXOgreEQ2.Migrate:RequestRerun[task]`

Puts one task's row in the Migration Assistant into its overwrite confirmation state, the same as clicking its re-run button; it reads and writes no files. It only does so when that task's old source data exists, otherwise nothing changes.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `task` | string |  | the task to ask about: accounts, imsettings, imlists, profiles, irc, mcp or isprofile |

```text
ISXOgreEQ2.Migrate:RequestRerun[accounts]
```

### `Run`

`ISXOgreEQ2.Migrate:Run[task,overwrite]`

Runs one migration task now, copying old OgreBot data into the new store (your old XML files are kept); the isprofile task instead asks InnerSpace to add its game profile and ignores overwrite. Without overwrite a task whose new file already exists is not rewritten and its row asks you to confirm instead, an unknown task name does nothing, and the result shows in the Migration Assistant window and the log.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `task` | string |  | the task to run: accounts, imsettings, imlists, profiles, irc, mcp or isprofile |
| `overwrite` | string |  | the word overwrite (any case) to replace data that already exists; anything else, or leaving it out, keeps existing data |

```text
ISXOgreEQ2.Migrate:Run[irc]
```
