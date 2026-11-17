# Console commands: ISXOgreX

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## `-auth`

`-auth <nick>`

IRC only: authorizes an IRC nick to send this hub commands.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `nick` | string |  | The IRC nick to authorize |

```text
irc !c -auth SomeNick
```

## `-authlist`

`-authlist`

IRC only: says which IRC nicks are authorized.

```text
irc !c -authlist
```

## `-KillSession`

`-KillSession <target>`

IRC only, authorized senders only: ends one InnerSpace session on this PC, or all of them.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `target` | string |  | The session name (is1, is2, ...) or all |

```text
irc !c -KillSession is3
```

## `-LaunchAutoLogin`

`-LaunchAutoLogin <profile>`

From IRC, authorised senders only: runs an auto-login profile.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `profile` | one |  | The auto-login profile to run. |

```text
irc !c -LaunchAutoLogin MyProfile
```

## `-List_AutoLoginProfiles`

`-List_AutoLoginProfiles`

From IRC, authorised senders only: lists the auto-login profiles. -details adds each row, -profile &lt;name> shows one.

```text
irc !c -List_AutoLoginProfiles
```

## `-List_Sessions`

`-List_Sessions`

IRC only, authorized senders only: lists this PC's InnerSpace sessions.

```text
irc !c -List_Sessions
```

## `-LoadCharacter`

`-LoadCharacter <toon>`

From IRC, authorised senders only: logs one toon in, using the first auto-login profile that holds it.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `toon` | one |  | The toon, or toon:isN to name the session. |

```text
irc !c -LoadCharacter MyToon
```

## `-unauth`

`-unauth <nick>`

IRC only: removes an IRC nick from the authorized list.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `nick` | string |  | The IRC nick to remove |

```text
irc !c -unauth SomeNick
```

## `-unauthall`

`-unauthall`

IRC only: clears the authorized list.

```text
irc !c -unauthall
```
