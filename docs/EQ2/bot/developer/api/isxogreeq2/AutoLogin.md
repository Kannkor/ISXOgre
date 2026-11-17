# ISXOgreEQ2.AutoLogin

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Methods

### `Close`

`ISXOgreEQ2.AutoLogin:Close`

Closes the Auto-Login window if it is open. Nothing is saved or changed.

```text
ISXOgreEQ2.AutoLogin:Close
```

### `Open`

`ISXOgreEQ2.AutoLogin:Open`

Opens the in-game Auto-Login window, where you build auto-login profiles (which characters to log in from your saved logins) and start them. Does nothing if the window is already open, and prints a console error if the window's own files are missing.

```text
ISXOgreEQ2.AutoLogin:Open
```

### `Refresh`

`ISXOgreEQ2.AutoLogin:Refresh`

Re-reads the saved auto-login profiles and repaints the profile list in the Auto-Login window when the list has changed.

```text
ISXOgreEQ2.AutoLogin:Refresh
```

### `Toggle`

`ISXOgreEQ2.AutoLogin:Toggle`

Opens the Auto-Login window when it is closed and closes it when it is open.

```text
ISXOgreEQ2.AutoLogin:Toggle
```
