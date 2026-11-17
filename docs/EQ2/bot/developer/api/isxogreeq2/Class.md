# ISXOgreEQ2.Class

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Members

### `Archetype`

`${ISXOgreEQ2.Class.Archetype}`

The local character's archetype in lowercase: fighter, priest, mage or scout. It is read from the game the first time it is asked for once in world and refreshed on every zone load; it is empty before any character has been read, and a ChangeValue override does not change it (only Is does).

**Returns:** string: fighter, priest, mage or scout; empty when no character has been read yet or the game's value is not recognised

```text
echo ${ISXOgreEQ2.Class.Archetype}
```

### `AscensionClass`

`${ISXOgreEQ2.Class.AscensionClass}`

The local character's ascension class: Thaumaturgist, Elementalist, Etherealist or Geomancer, in that capitalisation. Empty when the character has no ascension class or none of those names is found in the game's ascension label.

**Returns:** string: Thaumaturgist, Elementalist, Etherealist or Geomancer; empty when none is found

```text
echo ${ISXOgreEQ2.Class.AscensionClass}
```

### `ClassTier`

`${ISXOgreEQ2.Class.ClassTier}`

The local character's class grouping, the level between archetype and subclass, in lowercase: warrior, crusader, brawler, cleric, druid, shaman, shaper, sorcerer, enchanter, summoner, bard, rogue, predator or animalist. Empty before any character has been read.

**Returns:** string: the lowercase class grouping; empty when no character has been read yet or the game's value is not recognised

```text
echo ${ISXOgreEQ2.Class.ClassTier}
```

### `HasEpic2`

`${ISXOgreEQ2.Class.HasEpic2}`

TRUE for a ranger who owns the ranger epic 2.0 ability, FALSE otherwise. The buff is hidden and kept up, so owning it is taken to mean it is on.

**Returns:** bool: TRUE when the character is a ranger who owns the epic 2.0 ability; FALSE otherwise

```text
echo ${ISXOgreEQ2.Class.HasEpic2}
```

### `Is`

`${ISXOgreEQ2.Class.Is[name]}`

TRUE when name matches the local character's archetype, class grouping or class, case-insensitive, with an optional leading Is ignored, so Is[Scout], Is[predator] and Is[IsRanger] all answer TRUE for a ranger. A value forced with ChangeValue for that name wins over the real class, and no argument returns FALSE.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | string |  | An archetype, class grouping or class name, optionally prefixed with Is (fighter, crusader, paladin, IsPaladin) |

**Returns:** bool: TRUE when the name matches the character (or a ChangeValue override for it is TRUE); FALSE otherwise or when no name is given

```text
echo ${ISXOgreEQ2.Class.Is[templar]}
```

### `OnBGServer`

`${ISXOgreEQ2.Class.OnBGServer}`

TRUE when the current server is the Battlegrounds server. The server name match is case-insensitive.

**Returns:** bool: TRUE on Battlegrounds; FALSE on any other server or before the server has been read

```text
echo ${ISXOgreEQ2.Class.OnBGServer}
```

### `OnKaladimServer`

`${ISXOgreEQ2.Class.OnKaladimServer}`

TRUE when the current server is Kaladim. Kaladim also counts as TLE, so OnTLEServer is TRUE there too.

**Returns:** bool: TRUE on Kaladim; FALSE on any other server or before the server has been read

```text
echo ${ISXOgreEQ2.Class.OnKaladimServer}
```

### `OnTLEServer`

`${ISXOgreEQ2.Class.OnTLEServer}`

TRUE when the current server is a Time Locked Expansion server: Kaladim, Varsoon, Fallen Gate, Stormhold, Deathtoll, Zarrakon or Wuoshi. The server is read with the class identity (first read and every zone load) and again by UpdateServer.

**Returns:** bool: TRUE on one of the listed TLE servers; FALSE on any other server or before the server has been read

```text
echo ${ISXOgreEQ2.Class.OnTLEServer}
```

### `OnVarsoonServer`

`${ISXOgreEQ2.Class.OnVarsoonServer}`

TRUE when the current server is Varsoon. Varsoon also counts as TLE, so OnTLEServer is TRUE there too.

**Returns:** bool: TRUE on Varsoon; FALSE on any other server or before the server has been read

```text
echo ${ISXOgreEQ2.Class.OnVarsoonServer}
```

### `Ruleset`

`${ISXOgreEQ2.Class.Ruleset}`

The current server's ruleset as one word: Battlegrounds, TLE or Live. Any server not on the TLE or Battlegrounds list answers Live, including before the server has been read.

**Returns:** string: Battlegrounds, TLE or Live

```text
echo ${ISXOgreEQ2.Class.Ruleset}
```

### `Subclass`

`${ISXOgreEQ2.Class.Subclass}`

The local character's final class in lowercase, such as templar, ranger or shadowknight (one of the 26 classes). Empty before any character has been read.

**Returns:** string: the lowercase class name; empty when no character has been read yet or the game's value is not recognised

```text
echo ${ISXOgreEQ2.Class.Subclass}
```

### `WaterBreathingAbility`

`${ISXOgreEQ2.Class.WaterBreathingAbility}`

The name of the group water-breathing ability the bot uses for the local character's class: Water Spirit for a mystic, Abominus for a defiler. Every other class, channeler included, answers empty.

**Returns:** string: Water Spirit, Abominus, or empty for every other class

```text
echo ${ISXOgreEQ2.Class.WaterBreathingAbility}
```

## Methods

### `ChangeValue`

`ISXOgreEQ2.Class:ChangeValue[member,value]`

Forces Is[member] to answer value for the local character, so ChangeValue[IsFighter,TRUE] makes a non-fighter run fighter logic, and auto removes the override so it reads what the game says again; it lasts across zones until set again or a different character is read. A missing argument, a member that is not an archetype, class or subclass, or a value that is not TRUE, FALSE or auto prints one line and stores nothing, the same line as OgreBotAPI.Roster:SetClassValue.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `member` | string |  | The class name to force, with or without a leading Is (IsFighter, fighter, IsTemplar): an archetype, class or subclass |
| `value` | string |  | TRUE or FALSE (also 1/0, yes/no, on/off) to force it, or auto to remove the override |

```text
ISXOgreEQ2.Class:ChangeValue[IsFighter,TRUE]
```

### `Update`

`ISXOgreEQ2.Class:Update`

Re-reads the local character's name, class, ascension class and server from the game right away; out of world the read is held and happens on the first Class read once in world. ChangeValue overrides survive for the same character but are dropped when a different character is read, and a console line says so whenever the identity changes.

```text
ISXOgreEQ2.Class:Update
```

### `UpdateServer`

`ISXOgreEQ2.Class:UpdateServer`

Re-reads the server name now and resets OnTLEServer, OnKaladimServer, OnVarsoonServer, OnBGServer and Ruleset from it. Class values are not touched.

```text
ISXOgreEQ2.Class:UpdateServer
```
