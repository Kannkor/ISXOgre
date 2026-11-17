<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# ISXOgreEQ2.Auth

## Members

### `AccessLevel`

`${ISXOgreEQ2.Auth.AccessLevel}`

The access level text the Ogre login reported for this account. If the login did not send one, it reads a fixed default value.

**Returns:** string: the account's access level as text; a fixed default value when the login did not send one.

```text
echo ${ISXOgreEQ2.Auth.AccessLevel}
```

### `AccessLevelNum`

`${ISXOgreEQ2.Auth.AccessLevelNum}`

The account's access level as a number, as the Ogre login reported it. It reads -1 when the login sent no number.

**Returns:** int: the account's access level number; -1 when the login sent no number.

```text
echo ${ISXOgreEQ2.Auth.AccessLevelNum}
```

### `Authorized`

`${ISXOgreEQ2.Auth.Authorized}`

Whether this session's Ogre login was accepted. In normal use it reads TRUE, because the extension does not stay loaded without an accepted login.

**Returns:** bool: TRUE when this session's Ogre login was accepted; FALSE otherwise.

```text
echo ${ISXOgreEQ2.Auth.Authorized}
```

### `RelayGroup`

`${ISXOgreEQ2.Auth.RelayGroup}`

The relay group this session sends its relays to right now - ogre_everquest2 unless the Relay Groups tab sets another. It is the same value the bot's own relays use, so it follows a change on that tab at once.

**Returns:** string: the current relay group name.

```text
echo ${ISXOgreEQ2.Auth.RelayGroup}
```

### `Username`

`${ISXOgreEQ2.Auth.Username}`

The Ogre account username this session logged in with. Empty when the login sent no username.

**Returns:** string: the Ogre account username; empty when none was sent.

```text
echo ${ISXOgreEQ2.Auth.Username}
```

## Methods

### `Spew`

`ISXOgreEQ2.Auth:Spew`

Prints one line to the console with this session's Ogre username, whether its login was accepted, its access level text and number, and the relay group it sends to.

```text
ISXOgreEQ2.Auth:Spew
```
