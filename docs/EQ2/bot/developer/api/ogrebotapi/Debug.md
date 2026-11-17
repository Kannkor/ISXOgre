<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# OgreBotAPI.Debug

## Members

### `CheckVersion`

`${OgreBotAPI.Debug.CheckVersion[fw,compareTo]}`

Compares this session's version with compareTo and returns a one-line verdict that names the character. It returns "" when the for-who does not match this character or the character is not in the world.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `compareTo` | string |  | the version to compare with, as ${ISXOgreEQ2.Version} gives it; blank just reports this session's version |

**Returns:** string: "SAME: &lt;name> (&lt;version>)" when they match; "DIFFERENT: &lt;name> - Mine: &lt;version> Requested: &lt;compareTo>" when they do not; "VERSION: &lt;name> (&lt;version>)" when compareTo is blank; "" when the for-who does not match or the character is not in the world

```text
echo ${OgreBotAPI.Debug.CheckVersion[all,${ISXOgreEQ2.Version}]}
```

*Was (OldBot):* `OgreBotAPI.CheckVersion`

### `DebugPrefix`

`${OgreBotAPI.Debug.DebugPrefix}`

A time-stamped prefix for your own debug lines: the current time followed by ": OgreBot:". The bot does not add it to anything for you, :DebugEcho included.

**Returns:** string: "&lt;time>: OgreBot:", for example "14:03:22: OgreBot:"

```text
echo ${OgreBotAPI.Debug.DebugPrefix} checking loot
```

*Was (OldBot):* `OgreBotAPI.DebugMessage`, `OgreBotDebug.Prefix`

## Methods

### `BroadcastStat`

`OgreBotAPI.Debug:BroadcastStat[fw, type, value, where=oc]`

Reads one fact about this character, sends "&lt;name> --> &lt;label> &lt;value>" to where `where` says and fires the OgreEvent_SpewStats event with the same data. An unknown type or stat sends a "SpewStat:" error line instead, and faction, currency and recipe open a game window, so their answer comes a moment later.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `type` | string |  | what to report: stat, item, missingitem, abilityready, abilityidready, abilityidcd, marked, faction, currency, recipe or ascension (a leading - is allowed); quest and missingquest answer with a not-yet error |
| `value` | string |  | what to look up for that type: a stat key such as potency or haste, an item name, an ability id, a faction name or all, a currency name (eth and loyalty are short names), or a recipe name; leave blank for marked and ascension. An item you have none of sends nothing |
| `where` | string | `oc` | where the line goes: oc (the Ogre console on every session), irc, or event (no line, only the event); any other word goes to oc |

```text
OgreBotAPI.Debug:BroadcastStat[all,stat,potency,oc]
```

*Was (OldBot):* `OgreBotAPI.SpewStat`, `OgreBotAPI:Get_Faction`

### `DebugEcho`

`OgreBotAPI.Debug:DebugEcho[fw, a, b]`

Echoes a and b, joined by a space, to this session's console, but only while debug mode is on (see :SetDebugMode). With debug mode off, which is the default, it prints nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `a` | string |  | the first part of the line |
| `b` | string |  | the second part, printed after a space |

```text
OgreBotAPI.Debug:DebugEcho[${Me.Name},"Target:",${Target.Name}]
```

### `Echo`

`OgreBotAPI.Debug:Echo[fw, text, text2=""]`

Echoes text and text2, joined by a space, to this session's console. Only characters the for-who matches print it, and it works out of the world too.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `text` | string |  | the first part of the line |
| `text2` | string | `""` | the second part, printed after a space |

```text
OgreBotAPI.Debug:Echo[${Me.Name},"Pull ready","waiting on tank"]
```

*Was (OldBot):* `OgreBotAPI:Echo`, `OgreBotDebug:Echo`

### `SetDebugMode`

`OgreBotAPI.Debug:SetDebugMode[fw, on=TRUE]`

Turns debug mode on or off; while it is on, :DebugEcho prints its lines. Debug mode starts off, and a word that is not a yes/no word leaves it as it is.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `on` | bool | `TRUE` | TRUE turns debug mode on, FALSE turns it off |

```text
OgreBotAPI.Debug:SetDebugMode[all,TRUE]
```

*Was (OldBot):* `OgreBotAPI:SetDebugMode`

### `SpewInternalVariables`

`OgreBotAPI.Debug:SpewInternalVariables[fw]`

Echoes every internal variable as "name -> value" to this session's console, in name order. These are the values stored with OgreBotAPI.Vars:SetInternal; an empty store prints nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Debug:SpewInternalVariables[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Spew_InternalVariables`

### `SpewResearchWindow`

`OgreBotAPI.Debug:SpewResearchWindow[fw]`

Queues a job that opens the Knowledge window's research page if it is not up, broadcasts every row to every session as "&lt;label> -> &lt;status>", then closes the window if it opened it. It needs the character in the world, and with no rows it echoes a note to the console instead.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Debug:SpewResearchWindow[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Spew_BoZ_Research`

### `SpewSubscriptionStatus`

`OgreBotAPI.Debug:SpewSubscriptionStatus[fw]`

Reads the game's All Access membership status from the tooltip of the Marketplace window's All Access button and broadcasts it to every session as Good, Need to claim, Need more time, Not a member or Unknown, followed by the tooltip text. It does not open the window, and a tooltip it cannot read reports as Unknown.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Debug:SpewSubscriptionStatus[all]
```

*Was (OldBot):* `OgreBotAPI:SpewSubscriptionStatus`

### `SpewVariables`

`OgreBotAPI.Debug:SpewVariables[fw]`

Echoes every script variable as "name -> value" to this session's console, in name order. These are the values stored with OgreBotAPI.Vars:Set; an empty store prints nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Debug:SpewVariables[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Spew_Variables`
