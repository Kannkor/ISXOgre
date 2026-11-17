# OgreBotAPI.Loot

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Members

### `ItemCount`

`${OgreBotAPI.Loot.ItemCount}`

How many distinct item names have a SmartLoot cap in the loaded loot files. It is 0 until the loot files have been loaded.

**Returns:** int: the number of capped item names; 0 when nothing is loaded.

```text
echo ${OgreBotAPI.Loot.ItemCount}
```

### `Loaded`

`${OgreBotAPI.Loot.Loaded}`

TRUE once the SmartLoot item caps file has been read, which happens on every profile load and on :Load or :Reload. Answers about this session only.

**Returns:** bool: TRUE when the item caps file (ItemLootData) was read; FALSE before a load or when that file is missing or unreadable.

```text
echo ${OgreBotAPI.Loot.Loaded}
```

### `WindowExists`

`${OgreBotAPI.Loot.WindowExists}`

Whether a loot window is open on this session. With two loot windows open it answers about the topmost one.

**Returns:** bool: TRUE when a loot window is open; FALSE when none is.

```text
echo ${OgreBotAPI.Loot.WindowExists}
```

*Was (OldBot):* `OgreBotAPI.LootWindowExists`

### `WindowID`

`${OgreBotAPI.Loot.WindowID}`

The id of the open loot window, or 0 when there is none. With two loot windows open it is the topmost one.

**Returns:** int64: the loot window id; 0 when no loot window is open.

```text
echo ${OgreBotAPI.Loot.WindowID}
```

*Was (OldBot):* `OgreBotAPI.Get_LootWindowID`

## Methods

### `BuildToonItemsToBeZeroed`

`OgreBotAPI.Loot:BuildToonItemsToBeZeroed[fw, toon, item, ...]`

Adds character and item pairs to a list of SmartLoot counts to reset to 0, ready for :ProcessToonItemsToBeZeroed. It can be called several times to build a long list, and a character left without an item is dropped with a warning.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `toon` | string |  | the character whose count for the item is reset |
| `item` | string |  | the item name for that character; colour codes are removed |
| `...` | string |  | more character and item pairs, in the same order |

```text
OgreBotAPI.Loot:BuildToonItemsToBeZeroed[${Me.Name},${Me.Name},"Gleaming Crown",${Group[1].Name},"Gleaming Crown"]
```

*Was (OldBot):* `OgreBotAPI:SmartLoot_BuildToonItemsToBeZeroed`

### `Config`

`OgreBotAPI.Loot:Config[fw, mode=open]`

Opens the SmartLoot config panel, or closes it when mode is close. Opening a panel that is already open does nothing, so unsaved edits in it are kept.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `mode` | string | `open` | close closes the panel; any other value opens it |

```text
OgreBotAPI.Loot:Config[${Me.Name},close]
```

### `Decide`

`OgreBotAPI.Loot:Decide[fw, execute=FALSE]`

Works out what SmartLoot would do with every open loot window in turn and prints the plan for each item of a Leader Only one; by default it is a dry run that clicks nothing. With execute it records the counts and assigns or loots for real on the next pulse, and it does nothing but print a line when OgreBot has no profile, is paused or has no loot window open, or for each window that is not Leader Only.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `execute` | bool | `FALSE` | execute, force or a true word (TRUE, 1, yes, on) performs the plan; anything else, or nothing, is a dry run |

```text
OgreBotAPI.Loot:Decide[${Me.Name},execute]
```

### `LootAll`

`OgreBotAPI.Loot:LootAll[fw]`

Clicks Loot All on the open loot window. Does nothing when no loot window is open.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Loot:LootAll[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:LootWindowLootAll`

### `Migrate`

`OgreBotAPI.Loot:Migrate[fw, overwrite=FALSE]`

Converts the older XML loot files into the JSON loot store and prints how many files were written, blocked or missing. JSON files that already exist are left alone unless overwrite is given, and the loot data is reloaded when anything was written.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `overwrite` | bool | `FALSE` | overwrite, force or a true word (TRUE, 1, yes, on) replaces JSON files that already exist; anything else leaves them alone |

```text
OgreBotAPI.Loot:Migrate[${Me.Name},overwrite]
```

### `ProcessToonItemsToBeZeroed`

`OgreBotAPI.Loot:ProcessToonItemsToBeZeroed[fw]`

Sets every collected character and item count to 0, which makes those characters eligible for the item again, saves the loot counts file and empties the list. It prints how many were reset, and with nothing collected or an unreadable counts file it saves nothing and says so.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Loot:ProcessToonItemsToBeZeroed[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:SmartLoot_ProcessToonItemsToBeZeroed`

### `Reload`

`OgreBotAPI.Loot:Reload[fw]`

Reads the SmartLoot item caps and per-character loot counts from the saved loot files again and prints the cap count. Use it after editing the loot files by hand.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Loot:Reload[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:SmartLoot_ReloadDataFromFile`

### `ResetLootedActors`

`OgreBotAPI.Loot:ResetLootedActors[fw]`

Forgets which actors auto-loot has already looted or opened, so the next scan can try them again. The same reset happens by itself on every zone change.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Loot:ResetLootedActors[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:ResetActorsLooted`

### `SetAutoLootMode`

`OgreBotAPI.Loot:SetAutoLootMode[fw, mode]`

Sets this character's own auto-loot mode in the game, 0 none, 1 auto-greed or 2 auto-decline; out of the world nothing is sent. A missing mode prints a console line and sends nothing, and any other value sets 0 with a line saying so.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `mode` | text |  | 0, 1 or 2, or the words AN, AG or AD that Loot:SetOptions takes |

```text
OgreBotAPI.Loot:SetAutoLootMode[${Me.Name},1]
```

*Was (OldBot):* `OgreBotAPI:SetAutoLootMode`

### `SetOptions`

`OgreBotAPI.Loot:SetOptions[fw, token, ...]`

Sets the group loot method, rarity and auto-loot mode from short loot words, one per argument and in any order; a kind you do not name is left as it is. The group leader opens the group options window and applies them through the action queue, while anyone else only sets their own auto-loot mode; out of the world nothing is sent.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `token` | string |  | one loot word: method LO, FFA, Lotto, NBG or RR (the long names such as Leader Only or Round Robin work too); rarity All, T, L or F (with or without +); auto-loot AN, AG or AD. An unknown word is ignored with a console warning |
| `...` | string |  | more loot words of the same kinds |

```text
OgreBotAPI.Loot:SetOptions[${Me.Name},LO,T+,AN]
```

*Was (OldBot):* `OgreBotAPI:ChangeLootOptions`
