<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# OgreBotAPI.Craft

## Methods

### `AddLastScribedRecipe`

`OgreBotAPI.Craft:AddLastScribedRecipe[fw, qty=1]`

Adds the recipe you last scribed this session (by the bot or by hand) to the craft setup queue. With nothing scribed yet it prints a warning and adds nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `qty` | int | `1` | How many to craft; 0 or less becomes 1. |

```text
OgreBotAPI.Craft:AddLastScribedRecipe[${Me.Name},5]
```

*Was (OldBot):* `OgreCraft:AddLastScribedRecipe`, `OgreCraftAPI:AddLastScribedRecipe`

### `AddRecipe`

`OgreBotAPI.Craft:AddRecipe[fw, nameOrID|lastknownrecipe, qty=1]`

Adds a recipe to the craft setup queue by full name, by part of a name that matches only one recipe (4 letters or more), by recipe ID, or lastknownrecipe for the recipe last scribed this session. A recipe not in your recipe book prints a warning and adds nothing; if the book has not been read yet the add waits and runs once it has.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `nameOrID\|lastknownrecipe` | string |  | The recipe name, its ID (plain digits), or lastknownrecipe. A name may also be passed as several arguments; they are joined with spaces. |
| `qty` | int | `1` | How many to craft. Read only when it is the last argument and a whole number; 0 or less becomes 1. |

```text
OgreBotAPI.Craft:AddRecipe[${Me.Name},"Tempered Iron",2]
```

*Was (OldBot):* `OgreCraft:AddRecipeNameForWho`, `OgreCraftAPI:AddRecipeNameForWho`

### `BuyAllTinkeringRecipes`

`OgreBotAPI.Craft:BuyAllTinkeringRecipes[fw]`

Buys every tinkering recipe book you do not already know or carry from Fizza Cogsworth. It is refused unless you carry at least 3 platinum, are in Steamfont Mountains and are within 10 meters of her, and also while a crafting flow or merchant errand is running.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Craft:BuyAllTinkeringRecipes[${Me.Name}]
```

### `CompleteNavigation`

`OgreBotAPI.Craft:CompleteNavigation[fw]`

Answers craft's OgreCraft_NavigationRequired event (sent only when the craft setting to use events for movement is on) to say your script has moved the character; craft then checks the distance again and carries on. If no request is waiting it prints a warning.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Craft:CompleteNavigation[${Me.Name}]
```

### `DeferNavigation`

`OgreBotAPI.Craft:DeferNavigation[fw]`

Answers craft's OgreCraft_NavigationRequired event to say your script will not move the character, so craft uses its own movement. If no request is waiting it prints a warning.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Craft:DeferNavigation[${Me.Name}]
```

### `ScribeRecipe`

`OgreBotAPI.Craft:ScribeRecipe[fw, name|all=all]`

Scribes recipe scrolls from your bags one at a time, then opens and closes the tradeskill book. A name scribes only scrolls whose full item name matches it in any case (a name with a comma arrives whole), nothing matching prints a line and does nothing, and a call while scribing adds the new scrolls to the run.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `name\|all` | string | `all` | The scroll's full item name in any case, or all for every scribeable scroll in your bags. Left empty it scribes all. |

```text
OgreBotAPI.Craft:ScribeRecipe[${Me.Name},all]
```

*Was (OldBot):* `OgreCraft:ScribeRecipe`, `OgreCraftAPI:ScribeRecipe`

### `Start`

`OgreBotAPI.Craft:Start[fw]`

Starts crafting the setup queue. It is refused with a console line when you are not in the world, a crafting flow is already running, or the setup queue is empty, and a refused start changes nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Craft:Start[${Me.Name}]
```

*Was (OldBot):* `OgreCraft:Start`, `OgreCraftAPI:Start`

### `StartLLL`

`OgreBotAPI.Craft:StartLLL[fw]`

Starts low level leveling: rounds of buying recipe books, crafting the highest standard recipe at or below your tradeskill level, and selling or destroying what was made when the panel's settings say so. It stops at tradeskill level 9 or 19, and is refused when a crafting flow is already running or you are not in the world.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Craft:StartLLL[${Me.Name}]
```

*Was (OldBot):* `OgreCraftAPI:StartLLL`

### `StartQuest`

`OgreBotAPI.Craft:StartQuest[fw]`

Crafts the recipe steps of the quest selected in your journal, one of each per pass, until no craftable step is left. It is refused when no quest is selected, a crafting flow is already running, or you are not in the world, and a refused start changes nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Craft:StartQuest[${Me.Name}]
```

### `StartTinker`

`OgreBotAPI.Craft:StartTinker[fw]`

Starts auto tinkering: rounds of buying recipe books, crafting the highest-level tinkering recipe you know, and selling or destroying what was made when the panel's settings say so, until tinkering is maxed. It stops if the character has no tinkering skill, and is refused when a crafting flow is already running or you are not in the world.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Craft:StartTinker[${Me.Name}]
```

### `StartWrits`

`OgreBotAPI.Craft:StartWrits[fw]`

Starts the rush order (writ) run for the number of writs set in the craft settings. It is refused below tradeskill level 20, when a crafting flow is already running, or when you are not in the world, and a refused start changes nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Craft:StartWrits[${Me.Name}]
```

*Was (OldBot):* `OgreCraftAPI:StartWrits`

### `Stop`

`OgreBotAPI.Craft:Stop[fw]`

Stops the running crafting run (queue, writs, quest, Low Level Leveling or Auto Tinkering) on the characters the for-who names, the same as ISXOgreEQ2.Craft:Stop. With nothing running it drops a pause and prints that nothing was running.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Craft:Stop[igw:${Me.Name}]
```
