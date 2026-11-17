# ISXOgreEQ2.Chat

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Members

### `Hits`

`${ISXOgreEQ2.Chat.Hits}`

Total times a filtered chat listener matched a line and ran, since the extension loaded. Listeners that receive every line are not counted here.

**Returns:** int64: filtered-listener matches since the extension loaded

```text
echo ${ISXOgreEQ2.Chat.Hits}
```

### `Lines`

`${ISXOgreEQ2.Chat.Lines}`

Total lines handed to the extension's chat listeners since it loaded: every chat-channel line, game text line and announcement, injected lines included. A read-only counter that only goes up.

**Returns:** int64: lines passed to the chat listeners since the extension loaded

```text
echo ${ISXOgreEQ2.Chat.Lines}
```

### `Matchers`

`${ISXOgreEQ2.Chat.Matchers}`

How many registered chat listeners are filtered - they run only when a line matches their pattern.

**Returns:** int: current filtered listener count

```text
echo ${ISXOgreEQ2.Chat.Matchers}
```

### `RawSubs`

`${ISXOgreEQ2.Chat.RawSubs}`

How many registered chat listeners receive every line and do their own parsing.

**Returns:** int: current every-line listener count

```text
echo ${ISXOgreEQ2.Chat.RawSubs}
```

### `SeenAnnounce`

`${ISXOgreEQ2.Chat.SeenAnnounce}`

Announcements received since the extension loaded (EQ2's announcement event).

**Returns:** int64: announcements received since the extension loaded

```text
echo ${ISXOgreEQ2.Chat.SeenAnnounce}
```

### `SeenChat`

`${ISXOgreEQ2.Chat.SeenChat}`

Chat-channel lines received since the extension loaded (EQ2's incoming chat text event). Lines injected through OgreBotAPI.Comms:InjectChat are counted here too, once processed on the next pulse.

**Returns:** int64: chat-channel lines received since the extension loaded

```text
echo ${ISXOgreEQ2.Chat.SeenChat}
```

### `SeenText`

`${ISXOgreEQ2.Chat.SeenText}`

Game text lines received since the extension loaded (EQ2's incoming text event: system messages, combat text and other text the game prints).

**Returns:** int64: game text lines received since the extension loaded

```text
echo ${ISXOgreEQ2.Chat.SeenText}
```

### `Subscribers`

`${ISXOgreEQ2.Chat.Subscribers}`

How many chat listeners are registered inside the extension right now: the every-line listeners plus the filtered ones (RawSubs + Matchers).

**Returns:** int: current listener count, RawSubs plus Matchers

```text
echo ${ISXOgreEQ2.Chat.Subscribers}
```

### `TellReceived`

`${ISXOgreEQ2.Chat.TellReceived}`

Tells addressed to you since the extension loaded. Each one also fires the OgreEvent_InGameTell event.

**Returns:** int64: tells received since the extension loaded

```text
echo ${ISXOgreEQ2.Chat.TellReceived}
```

### `TellSent`

`${ISXOgreEQ2.Chat.TellSent}`

Tells you sent since the extension loaded. Each one also fires the OgreEvent_InGameTellSent event.

**Returns:** int64: tells sent since the extension loaded

```text
echo ${ISXOgreEQ2.Chat.TellSent}
```
