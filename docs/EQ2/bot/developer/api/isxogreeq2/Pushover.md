# ISXOgreEQ2.Pushover

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Methods

### `Message`

`ISXOgreEQ2.Pushover:Message[words]`

Queues a notification, the same as `ogre pushover <message>`. With no words it prints one warning and sends nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `words` | string |  | The message text, then any of -title, -priority, -sound, -device, -retry and -expire, each taking the next word; one argument each; required. |

```text
ISXOgreEQ2.Pushover:Message["raid is up","-title","Raid Night"]
```

### `Reload`

`ISXOgreEQ2.Pushover:Reload`

Re-reads your Pushover credentials file and prints the status line. With words after it, it sends them as a message that starts with reload.

```text
ISXOgreEQ2.Pushover:Reload
```

### `Status`

`ISXOgreEQ2.Pushover:Status`

Prints whether Pushover is configured and how many messages wait, then the usage, the same as bare `ogre pushover`; the keys are never printed in full. With words after it, it sends them as a message that starts with status.

```text
ISXOgreEQ2.Pushover:Status
```
