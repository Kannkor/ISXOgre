<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# OgreBotAPI.Session

## Members

### `AtCharacterSelect`

`${OgreBotAPI.Session.AtCharacterSelect}`

Whether the character select screen is showing. It works with no character logged in.

**Returns:** bool: TRUE while the character select screen is visible; FALSE otherwise

```text
echo ${OgreBotAPI.Session.AtCharacterSelect}
```

*Was (OldBot):* `OgreBotAPI.AtCharacterSelect`

### `CharacterName`

`${OgreBotAPI.Session.CharacterName}`

This character's name. It returns "" when not in the world, for example at character select.

**Returns:** string: the character's name; "" out of the world

```text
echo ${OgreBotAPI.Session.CharacterName}
```

*Was (OldBot):* `OgreBotAPI.CurrentCharacter`

### `ReviveLocation`

`${OgreBotAPI.Session.ReviveLocation[option,exact]}`

While you are dead, finds the revive point named by option in the death window and returns its row number. It returns 0 when you are alive, not in the world, give no option, or no revive point matches.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `option` | string |  | a row number, or a revive point name such as Entrance, compared case-insensitively with the text before the bracket; a row that is not a revive point is never chosen |
| `exact` | bool | `FALSE` | TRUE: the name must match in full; FALSE: the name may be part of the revive point's name |

**Returns:** int: the row number (from 1) of the matching revive point; 0 when there is none

```text
echo ${OgreBotAPI.Session.ReviveLocation[Entrance,FALSE]}
```

*Was (OldBot):* `OgreBotAPI.Get_ReviveLocation`

## Methods

### `CollectShiny`

`OgreBotAPI.Session:CollectShiny[fw]`

Targets the nearest collectible shiny, by the Loot tab's own test (an actor named only a question mark or an exclamation mark, or a resource whose name has a question mark), and collects it if it is within 10 meters. Nothing happens when none is that close; this runs on demand and is separate from the Loot tab's own shiny collecting.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Session:CollectShiny[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Question`

### `Harvest`

`OgreBotAPI.Session:Harvest[fw]`

Targets the nearest harvest node and collects from it, if that node is within 10 meters. Nothing happens when no node is that close, and the collect is sent at once, not queued.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Session:Harvest[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Resource`

### `ImmRes`

`OgreBotAPI.Session:ImmRes[fw, howManyDead=2]`

Queues a cast of Immaculate Revival when it is ready and enough of the group is dead: each dead group member counts 1, while a dead fighter or priest, or being dead yourself, counts 6. It does nothing for a character without the ability.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `howManyDead` | int | `2` | the count it takes before it casts; below 1 it never casts |

```text
OgreBotAPI.Session:ImmRes[igw:${Me.Name},3]
```

*Was (OldBot):* `OgreBotAPI:ImmRes`

### `LogToonIn`

`OgreBotAPI.Session:LogToonIn[forToon, toon, server="", class=""]`

Logs toon in on the one session forToon names, from the login screen, from character select, or from the world on another character (camping out first, unless in combat). It needs a saved login for toon on this PC and says so on the console when there is none.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `forToon` | string |  | the session that should act: its InnerSpace session name or its character's name, case-insensitive - at character select or the login screen, the character it last played (so a box a zone dropped to character select answers to its toon), and mid-zone only the session name; all, classes and groups do not match, and a blank gets one line |
| `toon` | string |  | the character to log in; a blank gets one line |
| `server` | string |  | the server, by name or short form (ior, md), for a character saved on more than one; blank uses its default server |
| `class` | string |  | the class to log in as, like ranger; blank logs in whatever class it was |

```text
OgreBotAPI.Session:LogToonIn[is2,${Group[1].Name}]
```

*Was (OldBot):* `OgreBotAPI:LogToonIn`, `OgreBotAPI:LoginAtCharacterSelect`

### `PlayAtCharacterSelect`

`OgreBotAPI.Session:PlayAtCharacterSelect[fw]`

Presses the Play button on the character select screen. It does nothing unless that screen is showing, and it works with no character in the world.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Session:PlayAtCharacterSelect[all]
```

*Was (OldBot):* `OgreBotAPI:PlayAtCharacterSelect`

### `Res`

`OgreBotAPI.Session:Res[fw]`

Lets the cast stack cast res abilities again by unchecking Disable CS_Res. It is silent, and it turns ressing on even if you turned it off by hand.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Session:Res[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Res`

### `ResStone`

`OgreBotAPI.Session:ResStone[fw]`

Queues this class's res stone spell when it is ready: Divine Awakening for a cleric, Spirit Guide for a shaman, Favor of the Phoenix for a druid, Channel Soul for a channeler. Any other class does nothing, so it is safe to send to the whole group.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Session:ResStone[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:ResStone`

### `Revive`

`OgreBotAPI.Session:Revive[fw, option=0, exact=FALSE]`

With option 0, presses Revive on the death window when you are dead (a living character clicks nothing); with a row number or revive point name, picks that point and presses Revive half a second later, or the last revive point the window lists when none matches, saying on the console which points there are. A dead character that revives this way has its camp spot cleared, because it comes back away from where it fell.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `option` | string | `0` | 0 for the death window's default revive, or a revive point row number or name, matched as ${OgreBotAPI.Session.ReviveLocation} matches it; when nothing matches, the last revive point the window lists is used (no revive only when it lists none) |
| `exact` | bool | `FALSE` | TRUE: a name must match in full; FALSE: it may be part of the revive point's name |

```text
OgreBotAPI.Session:Revive[igw:${Me.Name},Entrance]
```

*Was (OldBot):* `OgreBotAPI:Revive`, `Revive`, `call Obj_OgreUtilities.Revive`

### `StopRes`

`OgreBotAPI.Session:StopRes[fw]`

Stops the cast stack casting res abilities by checking Disable CS_Res. It is silent; :Res turns ressing back on.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Session:StopRes[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:StopRes`
