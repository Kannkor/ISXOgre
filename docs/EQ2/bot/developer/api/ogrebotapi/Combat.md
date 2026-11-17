<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# OgreBotAPI.Combat

## Members

### `InCombat`

`${OgreBotAPI.Combat.InCombat}`

TRUE when your character is in combat or something hates it. Always FALSE while you are not in the world, such as at character select.

**Returns:** bool: TRUE when Me.InCombat or Me.IsHated is TRUE; FALSE otherwise or out of the world.

```text
echo ${OgreBotAPI.Combat.InCombat}
```

*Was (OldBot):* `OgreBotAPI.InCombat`

### `IsReady`

`${OgreBotAPI.Combat.IsReady}`

TRUE when OgreBot is up: its main window or mini toolbar is open and a profile is loaded (the same check as ${ISXOgreEQ2.OgreBot.IsReady}); FALSE after it is closed.

**Returns:** bool: TRUE when OgreBot is open and ready; FALSE otherwise.

```text
echo ${OgreBotAPI.Combat.IsReady}
```

*Was (OldBot):* `OgreBotAPI.IsReady`

### `NoDefensive`

`${OgreBotAPI.Combat.NoDefensive}`

TRUE while any no-defensive reason is held (SetNoDefensive). While it is TRUE the bot skips defensive abilities.

**Returns:** bool: TRUE when at least one no-defensive reason is held; FALSE when none is.

```text
echo ${OgreBotAPI.Combat.NoDefensive}
```

*Was (OldBot):* `OgreBotAPI.CheckNoDefensiveOn`

### `NoOffensive`

`${OgreBotAPI.Combat.NoOffensive}`

TRUE while offensive actions are held off: a no-offensive reason is set (SetNoOffensive), or your current NPC target matches the no-offensive list (AddNoOffensive). While it is TRUE the bot skips offensive abilities and, while running, turns auto-attack off.

**Returns:** bool: TRUE when a no-offensive reason is held or the current NPC target is on the no-offensive list; FALSE otherwise.

```text
echo ${OgreBotAPI.Combat.NoOffensive}
```

*Was (OldBot):* `OgreBotAPI.CheckNoOffensiveOn`, `OgreBotAPI.NoOffensiveOn`

### `NoReqBowAbilities`

`${OgreBotAPI.Combat.NoReqBowAbilities}`

Returns the flag SetNoReqBowAbilities sets, FALSE until something sets it. While it is TRUE the cast stack skips abilities that need a bow.

**Returns:** bool: TRUE when SetNoReqBowAbilities turned the flag on; FALSE otherwise.

```text
echo ${OgreBotAPI.Combat.NoReqBowAbilities}
```

*Was (OldBot):* `OgreBotAPI.CheckNoReqBowAbilities`, `OgreBotAPI.bNoReqBowAbilities`

### `Zoning`

`${OgreBotAPI.Combat.Zoning}`

TRUE while a zone change is in progress, including the short wait after arriving before the character is settled. FALSE once you are in a zone and settled.

**Returns:** bool: TRUE while zoning or not yet settled after a zone; FALSE otherwise.

```text
echo ${OgreBotAPI.Combat.Zoning}
```

*Was (OldBot):* `OgreBotAPI.Zoning`

## Methods

### `AddNoOffensive`

`OgreBotAPI.Combat:AddNoOffensive[fw, mobName, exactOnly=TRUE]`

Adds a mob name to the no-offensive list: while your current NPC target matches an entry, NoOffensive is TRUE and the bot holds off offensive abilities and auto-attack. Matching ignores case, adding a name already listed replaces its exactOnly setting, and the list is kept until ClearNoOffensive, LetsGo or the bot closing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `mobName` | string |  | The mob name to add. A blank name is ignored. |
| `exactOnly` | bool | `TRUE` | TRUE matches the whole name only; FALSE matches any target whose name contains mobName. |

```text
OgreBotAPI.Combat:AddNoOffensive[all,"a shield of Yothshaval",TRUE]
```

*Was (OldBot):* `OgreBotAPI:AddNoOffensiveOn`

### `ClearNoOffensive`

`OgreBotAPI.Combat:ClearNoOffensive[fw]`

Empties the no-offensive list built by AddNoOffensive. Reasons set with SetNoOffensive are not touched.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Combat:ClearNoOffensive[all]
```

*Was (OldBot):* `OgreBotAPI:ClearNoOffensiveOn`

### `Countdown`

`OgreBotAPI.Combat:Countdown[fw, seconds=10]`

When this character is grouped and is the group leader, runs the game's countdown for the given seconds; on anyone else it does nothing. A number below 1 counts down from 1 and one over 30 from 30, with a console line saying so.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `seconds` | int | `10` | Seconds to count down, 1 to 30. A word that is not a number reads as 0, so it counts down from 1. The -countdown console row passes 1 when its time is left blank. |

```text
OgreBotAPI.Combat:Countdown[igw:${Me.Name},5]
```

*Was (OldBot):* `OgreBotAPI:Countdown`

### `RemoveNoOffensive`

`OgreBotAPI.Combat:RemoveNoOffensive[fw,mobName]`

Takes a mob name off the no-offensive list that Combat:AddNoOffensive adds to; the name is matched ignoring case. A name not on the list changes nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `mobName` | string |  | The mob name to take off the list. A blank name is ignored. |

```text
OgreBotAPI.Combat:RemoveNoOffensive[all,"a shield of Yothshaval"]
```

*Was (OldBot):* `OgreBotAPI:RemoveNoOffensiveOn`

### `SetNoDefensive`

`OgreBotAPI.Combat:SetNoDefensive[fw, on=TRUE, reason=""]`

Turns no-defensive on or off by reason: on adds the reason (manual when blank), off with a reason removes just that one, and off with no reason clears them all. While any reason is held the bot skips defensive abilities; LetsGo and reopening the bot clear every reason.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `on` | bool | `TRUE` | TRUE adds the reason; FALSE removes it, or every reason when reason is blank. A word that is not yes or no changes nothing. |
| `reason` | string | `""` | A name for why it is on, so several callers can hold it at once. Blank means manual when adding and every reason when removing. |

```text
OgreBotAPI.Combat:SetNoDefensive[igw:${Me.Name},FALSE,"tank swap"]
```

*Was (OldBot):* `OgreBotAPI:SetNoDefensive`

### `SetNoOffensive`

`OgreBotAPI.Combat:SetNoOffensive[fw, on=TRUE, reason=""]`

Turns no-offensive on or off by reason: on adds the reason (manual when blank), off with a reason removes just that one, and off with no reason clears them all. While any reason is held the bot skips offensive abilities and turns auto-attack off; LetsGo and reopening the bot clear every reason.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `on` | bool | `TRUE` | TRUE adds the reason; FALSE removes it, or every reason when reason is blank. A word that is not yes or no changes nothing. |
| `reason` | string | `""` | A name for why it is on, so several callers can hold it at once. Blank means manual when adding and every reason when removing. |

```text
OgreBotAPI.Combat:SetNoOffensive[igw:${Me.Name},TRUE,"tank swap"]
```

*Was (OldBot):* `OgreBotAPI:SetNoOffensive`

### `SetNoReqBowAbilities`

`OgreBotAPI.Combat:SetNoReqBowAbilities[fw, on=TRUE]`

Sets the flag NoReqBowAbilities reports, and needs the character in the world. While it is on the cast stack skips abilities that need a bow; LetsGo and closing the bot turn it off.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `on` | bool | `TRUE` | TRUE turns the flag on; FALSE turns it off. A word that is not yes or no leaves it as it is. |

```text
OgreBotAPI.Combat:SetNoReqBowAbilities[${Me.Name},FALSE]
```

*Was (OldBot):* `OgreBotAPI:SetNoReqBowAbilities`

### `ThreatIgnoreAdd`

`OgreBotAPI.Combat:ThreatIgnoreAdd[fw, name...]`

Adds fighter names to the threat ignore list: a fighter on it holding aggro does not count as a fighter already tanking, so your taunts and threat abilities are still used. Matching ignores case, blank and NULL names are skipped, and the list is cleared when the bot is opened or closed.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `name...` | string |  | One or more fighters' character names to add. |

```text
OgreBotAPI.Combat:ThreatIgnoreAdd[igw:${Me.Name},${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:ThreatFighterIgnoreList_Add`

### `ThreatIgnoreClear`

`OgreBotAPI.Combat:ThreatIgnoreClear[fw]`

Empties the threat ignore list. Needs the character in the world.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Combat:ThreatIgnoreClear[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:ThreatFighterIgnoreList_Clear`

### `ThreatIgnoreList`

`OgreBotAPI.Combat:ThreatIgnoreList[fw]`

Prints the threat ignore list to the console: a ThreatFighterIgnoreList -- Start -- line, then one name per line. There is no end line, and the character must be in the world.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Combat:ThreatIgnoreList[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI.ThreatFighterIgnoreList`, `OgreBotAPI:ThreatFighterIgnoreList_List`

### `ThreatIgnoreRemove`

`OgreBotAPI.Combat:ThreatIgnoreRemove[fw, name...]`

Removes each named fighter from the threat ignore list, in any case. A name that is not on the list is ignored, and the character must be in the world.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `name...` | string |  | One or more character names to remove. |

```text
OgreBotAPI.Combat:ThreatIgnoreRemove[igw:${Me.Name},${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:ThreatFighterIgnoreList_Remove`
