<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# ISXOgreEQ2.Heartstone

## Methods

### `Now`

`ISXOgreEQ2.Heartstone:Now`

Makes the next Rekindle Bond attempt happen right away instead of waiting out the 15 to 30 minute timer, or looks for a Heartstone now if none has been found yet. It is refused with a warning while the helper is off, and an attempt still does nothing unless you are within 6 units of the Heartstone.

```text
ISXOgreEQ2.Heartstone:Now
```

### `Off`

`ISXOgreEQ2.Heartstone:Off`

Turns the Heartstone helper off (`ogre end heartstone`): no more scans or rekindles, and it prints 'heartstone: disabled'. This is not saved, so the helper is on again after the extension reloads.

```text
ISXOgreEQ2.Heartstone:Off
```

### `On`

`ISXOgreEQ2.Heartstone:On`

Turns the Heartstone helper back on, prints 'heartstone: ENABLED' and looks again for a Heartstone within 200 units about 3 seconds later. The helper is on by default and works whether or not OgreBot is running: after each zone-in it looks for a Heartstone and, once found, uses Rekindle Bond on it at a random 15 to 30 minute interval, waiting while you are dead or camping out and skipping that turn when you are more than 6 units away.

```text
ISXOgreEQ2.Heartstone:On
```

### `Status`

`ISXOgreEQ2.Heartstone:Status`

Prints the guild-hall Heartstone helper's state (`ogre heartstone`): on or off, whether it has found a Heartstone in this zone, the 6-unit reach, the 15 to 30 minute wait, and its scan, attempt and rekindle counts.

```text
ISXOgreEQ2.Heartstone:Status
```
