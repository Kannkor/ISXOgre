<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# ISXOgreEQ2.Craft

## Members

### `Crafted`

`${ISXOgreEQ2.Craft.Crafted}`

How many crafts the current queue has made: a writ or loop run crafts queue after queue, and this counts the one crafting now. Once nothing is running it reads the count from the last queue that ran, so a finished run does not drop to 0.

**Returns:** int: crafts made so far in the current queue, or in the last queue once idle; 0 before any run.

```text
echo ${ISXOgreEQ2.Craft.Crafted}
```

### `CraftTotal`

`${ISXOgreEQ2.Craft.CraftTotal}`

How many crafts the current queue plans to make: a writ or loop run crafts queue after queue, so this is one queue's total, not the whole run's. Once nothing is running it reads the total of the last queue that ran.

**Returns:** int: the planned craft count of the current queue, or of the last queue once idle; 0 before any run.

```text
echo ${ISXOgreEQ2.Craft.CraftTotal}
```

### `Details`

`${ISXOgreEQ2.Craft.Details}`

The whole crafting picture as one JSON string: running, paused, flow, stage, status, crafted, craftTotal, recipe, row, rows, lastError, and short (a list of name / need / have / fuel for what the latest resource count came up short on). recipe is "" and row / rows are 0 when no queue row is being crafted.

**Returns:** string: a JSON object with the fields listed above.

```text
echo ${ISXOgreEQ2.Craft.Details}
```

### `Flow`

`${ISXOgreEQ2.Craft.Flow}`

Which crafting run is going: idle, queue, writs, autotinkering, lowlevelleveling or quest. It goes back to idle when the run finishes.

**Returns:** string: "idle", "queue", "writs", "autotinkering", "lowlevelleveling" or "quest".

```text
echo ${ISXOgreEQ2.Craft.Flow}
```

### `IsReady`

`${ISXOgreEQ2.Craft.IsReady}`

Whether the crafting engine has started up, which happens on its first pulse after the extension loads. It does not mean the recipe book has been read - see ScanActive and QueueUpdated.

**Returns:** bool: TRUE once the crafting engine has started; FALSE before that.

```text
echo ${ISXOgreEQ2.Craft.IsReady}
```

### `LastError`

`${ISXOgreEQ2.Craft.LastError}`

The last refusal or failure the crafting engine reported, the same line the panel shows in red. It is cleared only when a run passes its start checks.

**Returns:** string: the last error or refusal text; "" when there has been none since the last good start.

```text
echo ${ISXOgreEQ2.Craft.LastError}
```

### `LastScribedRecipeId`

`${ISXOgreEQ2.Craft.LastScribedRecipeId}`

The recipe id of the recipe you scribed most recently, by this engine or by hand, filled in when the recipe book is read again after the game's "put in recipe book" message, so it lags the name briefly. If that name is not found in the re-read book the id keeps the previous recipe's, so it can disagree with LastScribedRecipeName.

**Returns:** int64: the last scribed recipe's id; 0 when none has been seen since the extension loaded.

```text
echo ${ISXOgreEQ2.Craft.LastScribedRecipeId}
```

### `LastScribedRecipeName`

`${ISXOgreEQ2.Craft.LastScribedRecipeName}`

The name of the recipe you scribed most recently, by this engine or by hand, taken from the game's "put in recipe book" message.

**Returns:** string: the last scribed recipe's name; "" when none has been seen since the extension loaded.

```text
echo ${ISXOgreEQ2.Craft.LastScribedRecipeName}
```

### `Lite`

`${ISXOgreEQ2.Craft.Lite}`

Whether craft lite is on - the reaction engine that casts the crafting reaction arts during a craft, also for crafts you start by hand. Opening the panel or starting any run turns it on.

**Returns:** bool: TRUE when craft lite (crafting reactions) is on; FALSE when it is off.

```text
echo ${ISXOgreEQ2.Craft.Lite}
```

### `MissingResources`

`${ISXOgreEQ2.Craft.MissingResources}`

Whether the latest queue's resource count came up short of something it needs. It stays set after the run ends and resets when the next count starts; Details lists what is short.

**Returns:** bool: TRUE when the latest resource count was short; FALSE before any count and when nothing was short.

```text
echo ${ISXOgreEQ2.Craft.MissingResources}
```

### `NavigationDetails`

`${ISXOgreEQ2.Craft.NavigationDetails}`

The most recent navigation request as a JSON string, the same payload OgreCraft_NavigationRequired passes: requestID, action, category, key, displayName, customNamedPoint, precision, zone, characterName, targetFound, and targetID / targetName / targetX / targetY / targetZ / targetDistance when the target was found. It keeps the last request after it is answered and is "" before the first one.

**Returns:** string: the last navigation request's JSON; "" when no request has been made since the extension loaded.

```text
echo ${ISXOgreEQ2.Craft.NavigationDetails}
```

### `Paused`

`${ISXOgreEQ2.Craft.Paused}`

Whether the crafting pause is on. A pause turned on with no run going still reads TRUE but holds nothing, and the next start clears it.

**Returns:** bool: TRUE when the crafting pause is on; FALSE otherwise.

```text
echo ${ISXOgreEQ2.Craft.Paused}
```

### `QueueUpdated`

`${ISXOgreEQ2.Craft.QueueUpdated}`

Whether every recipe add and queue load you asked for has landed in the setup queue. An add or load asked while the recipe book is still being read waits for the read, and this is FALSE until it lands.

**Returns:** bool: TRUE when no add or queue load is waiting for the recipe book; FALSE while one waits.

```text
echo ${ISXOgreEQ2.Craft.QueueUpdated}
```

### `Recipes`

`${ISXOgreEQ2.Craft.Recipes}`

How many recipes the engine has indexed from your recipe book. It is 0 until the book has been read; a read starts when a run starts, when you scribe a recipe or on Scan, and also when the panel opens or craft lite turns on unless Do NOT load recipes on startup is ticked.

**Returns:** int: the number of recipes indexed by the last recipe-book read; 0 before the first read.

```text
echo ${ISXOgreEQ2.Craft.Recipes}
```

### `RecipesInQueue`

`${ISXOgreEQ2.Craft.RecipesInQueue}`

How many recipe rows are in the setup queue (the queue Start crafts). It counts rows, not the quantity to craft.

**Returns:** int: the number of rows in the setup queue; 0 when it is empty.

```text
echo ${ISXOgreEQ2.Craft.RecipesInQueue}
```

### `Running`

`${ISXOgreEQ2.Craft.Running}`

Whether a crafting run is going: a setup-queue run, writs, auto tinkering, low level leveling or quest crafting. A paused run still counts as running.

**Returns:** bool: TRUE while any crafting run is going (paused or not); FALSE when crafting is idle.

```text
echo ${ISXOgreEQ2.Craft.Running}
```

### `ScanActive`

`${ISXOgreEQ2.Craft.ScanActive}`

Whether the engine is reading your recipe book right now. Runs wait for the read to finish before they resolve any recipe.

**Returns:** bool: TRUE while the recipe book is being read; FALSE otherwise.

```text
echo ${ISXOgreEQ2.Craft.ScanActive}
```

### `Setting`

`${ISXOgreEQ2.Craft.Setting[id]}`

One crafting panel setting, read by its id, as the raw stored text. An id that has never been saved returns "" (the built-in default is not filled in), and a call with no id returns NULL.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `id` | string |  | The panel setting id, such as slider_craft_writcount or checkbox_craft_useevents. |

**Returns:** string: the stored value of that setting; "" when it is not set.

```text
echo ${ISXOgreEQ2.Craft.Setting[slider_craft_writcount]}
```

### `Stage`

`${ISXOgreEQ2.Craft.Stage}`

One word for what crafting is doing right now, such as countingResources, findingStation, walking, crafting, findingWrit, turningIn, buyingBooks or disposing. It reads idle when nothing is running.

**Returns:** string: the current stage word; "idle" when no run is going.

```text
echo ${ISXOgreEQ2.Craft.Stage}
```

### `Status`

`${ISXOgreEQ2.Craft.Status}`

The crafting engine's status line, the same text the panel shows, such as "idle", "crafting &lt;recipe>", "scanning recipes", "paused" or "waiting for your navigation script (...)". A refused start does not change it - the reason is in LastError.

**Returns:** string: the current status text; "idle" when nothing is running.

```text
echo ${ISXOgreEQ2.Craft.Status}
```

### `WaitingForNavigation`

`${ISXOgreEQ2.Craft.WaitingForNavigation}`

Whether the crafting engine is waiting for your script to move the character, after it fired OgreCraft_NavigationRequired. This happens only with the "use events" setting (checkbox_craft_useevents) on; the wait has no time limit and Stop ends it.

**Returns:** bool: TRUE while a navigation request is waiting for CompleteNavigation or DeferNavigation; FALSE otherwise.

```text
echo ${ISXOgreEQ2.Craft.WaitingForNavigation}
```

## Methods

### `AddLastScribedRecipe`

`ISXOgreEQ2.Craft:AddLastScribedRecipe[qty]`

Adds the recipe you last scribed this session (by the bot or by hand) to the craft setup queue, waiting for the recipe book to be read first when needed. With nothing scribed yet it prints a warning and adds nothing; it is the same as OgreBotAPI.Craft:AddLastScribedRecipe.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `qty` | int |  | How many to craft; left out, 0 or less it is 1. |

```text
ISXOgreEQ2.Craft:AddLastScribedRecipe[2]
```

### `AddRecipe`

`ISXOgreEQ2.Craft:AddRecipe[nameOrID|lastknownrecipe, qty]`

Adds a recipe to the craft setup queue by full name, by part of a name that matches only one recipe (4 letters or more), by recipe ID, or lastknownrecipe for the recipe last scribed this session; a recipe already queued gets the quantity added. A recipe not in your book prints a warning and adds nothing, an add made before the book is read waits for it, and this is OgreBotAPI.Craft:AddRecipe without the for-who.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `nameOrID\|lastknownrecipe` | string |  | The recipe name, its ID (plain digits), or lastknownrecipe. A name may also be passed as several arguments; they are joined with spaces. |
| `qty` | int |  | How many to craft. Read only when it is the last of two or more arguments and a whole number; left out it is 1, and 0 or less becomes 1. |

```text
ISXOgreEQ2.Craft:AddRecipe["Tempered Iron",2]
```

### `AddRecipeListFromFile`

`ISXOgreEQ2.Craft:AddRecipeListFromFile[file]`

Adds the recipes of one of your saved craft queues to the setup queue (the panel's Load Queue replaces it instead), warning about any recipe not in this character's book. The name is a queue in your queues folder, any path is cut off and a .json or .xml ending dropped, a missing name or file prints a warning, and a queue that needs the recipe book waits for the book to be read.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `file` | string |  | The saved queue's name, with or without .json, as saved from the craft panel; a folder in front of it is ignored. |

```text
ISXOgreEQ2.Craft:AddRecipeListFromFile["MyQueue.json"]
```

### `BuyAllTinkeringRecipes`

`ISXOgreEQ2.Craft:BuyAllTinkeringRecipes[]`

Buys every tinkering recipe book you do not already know or carry from Fizza Cogsworth, then scribes the ones your skill allows when the Scribe recipes setting is on. It is refused unless you carry at least 3 platinum, are in Steamfont Mountains and are within 10 meters of her, and also while a crafting flow or merchant errand is running (the same as OgreBotAPI.Craft:BuyAllTinkeringRecipes).

```text
ISXOgreEQ2.Craft:BuyAllTinkeringRecipes
```

### `Catalog`

`ISXOgreEQ2.Craft:Catalog[]`

Prints how much the craft data files loaded: devices, universal devices, merchant types, recipe book series, conversions and partial conversions. The files are loaded first if they were not yet.

```text
ISXOgreEQ2.Craft:Catalog
```

### `Clear`

`ISXOgreEQ2.Craft:Clear[]`

Empties the craft setup queue, whether or not a flow is running, and prints setup queue cleared. Each row it drops fires OgreCraft_RecipeQueueUpdated as a removed row, as a remove does.

```text
ISXOgreEQ2.Craft:Clear
```

### `CompleteNavigation`

`ISXOgreEQ2.Craft:CompleteNavigation[]`

Answers craft's OgreCraft_NavigationRequired event (sent only when the craft setting to use events for movement is on) to say your script has moved the character; craft then takes the nearest station or NPC of the same name within 100 m and checks the distance again. If no request is waiting it prints a warning, and it is the same as OgreBotAPI.Craft:CompleteNavigation.

```text
ISXOgreEQ2.Craft:CompleteNavigation
```

### `DeferNavigation`

`ISXOgreEQ2.Craft:DeferNavigation[]`

Answers craft's OgreCraft_NavigationRequired event to say your script will not move the character, so craft walks there with its own movement. If no request is waiting it prints a warning, and it is the same as OgreBotAPI.Craft:DeferNavigation.

```text
ISXOgreEQ2.Craft:DeferNavigation
```

### `End`

`ISXOgreEQ2.Craft:End[]`

Closes the craft window and ends all of crafting: the running flow, craft's own movement, a merchant errand, a summoned station, and craft lite. It is the same as ogre end craft and the window's X; use Stop to stop a run and keep the window.

```text
ISXOgreEQ2.Craft:End
```

### `Help`

`ISXOgreEQ2.Craft:Help[]`

Prints the ogre craft console words and their arguments to the console. It changes nothing.

```text
ISXOgreEQ2.Craft:Help
```

### `Lite`

`ISXOgreEQ2.Craft:Lite`

Turns craft lite on, so the crafting reactions are cast for you during crafting rounds, and prints a console line when the state changes; turned on in the world with the recipe book not yet read, it also starts reading the book unless the "Do NOT load recipes on startup" setting is ticked. Opening the panel and starting any crafting flow turn it on as well.

```text
ISXOgreEQ2.Craft:Lite
```

### `LiteOff`

`ISXOgreEQ2.Craft:LiteOff`

Turns craft lite off, so no crafting reactions are cast, drops any reaction waiting to be cast, and prints a console line when the state changes. Starting any crafting flow turns it back on.

```text
ISXOgreEQ2.Craft:LiteOff
```

### `Minimize`

`ISXOgreEQ2.Craft:Minimize[]`

Rolls the craft window up to its header while crafting carries on; Open brings it back. With the window not open it does nothing.

```text
ISXOgreEQ2.Craft:Minimize
```

### `Open`

`ISXOgreEQ2.Craft:Open`

Opens the crafting panel, or brings back a minimized one, and turns craft lite on - the same as a bare `ogre craft`. A panel that cannot open prints why and leaves craft as it was, and with the "Do NOT load recipes on startup" setting ticked an unread recipe book stays unread.

```text
ISXOgreEQ2.Craft:Open
```

### `Pause`

`ISXOgreEQ2.Craft:Pause[on|off]`

Pauses or resumes crafting: off resumes, and on, any other word or no argument pauses. A craft already begun finishes and nothing new starts while paused, and a pause made with no flow running is dropped when the next flow starts.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `on\|off` | string | `on` | off resumes; on, any other word, or nothing pauses. |

```text
ISXOgreEQ2.Craft:Pause[on]
```

### `Queue`

`ISXOgreEQ2.Craft:Queue[]`

Prints each row of the craft setup queue to the console as quantity, recipe name and recipe ID, or setup queue is empty. It changes nothing.

```text
ISXOgreEQ2.Craft:Queue
```

### `Reload`

`ISXOgreEQ2.Craft:Reload`

Writes any setting changed in the last second, then reloads the craft settings from disk and the craft data files (devices, merchants, recipe books and reaction arts), printing what the data files loaded.

```text
ISXOgreEQ2.Craft:Reload
```

### `Save`

`ISXOgreEQ2.Craft:Save`

Writes changed craft settings to disk now instead of waiting for the automatic save, and prints settings saved or settings NOT saved (saved also when nothing had changed and nothing was written). It refuses to write over a settings file that could not be read.

```text
ISXOgreEQ2.Craft:Save
```

### `Scan`

`ISXOgreEQ2.Craft:Scan`

Re-reads your recipe book from the start, opening the book so the client lists every recipe, and restarts a scan already in progress. Out of the world it does nothing and prints nothing.

```text
ISXOgreEQ2.Craft:Scan
```

### `ScribeRecipe`

`ISXOgreEQ2.Craft:ScribeRecipe[name|all=all]`

Scribes recipe scrolls from your bags one at a time, then opens and closes the tradeskill book so the new recipes are listed. A name scribes only scrolls whose full item name matches it in any case (a name with a comma arrives whole), nothing matching prints a line, and a call while scribing adds the new scrolls to the run (the same as OgreBotAPI.Craft:ScribeRecipe).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name\|all` | string | `all` | The scroll's full item name in any case, or all for every scribeable scroll in your bags. Left empty it scribes all. |

```text
ISXOgreEQ2.Craft:ScribeRecipe[all]
```

### `Set`

`ISXOgreEQ2.Craft:Set[key,value]`

Changes one craft setting by its key and prints the new value; it is saved by itself about a second later. Both arguments are required, and a key that is not a craft setting (any case is accepted) prints a warning and saves nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `key` | string |  | The setting's key, the panel control's id such as checkbox_craft_scriberecipes. |
| `value` | string |  | The new value, stored as given (TRUE or FALSE for a checkbox). |

```text
ISXOgreEQ2.Craft:Set[checkbox_craft_scriberecipes,TRUE]
```

### `Start`

`ISXOgreEQ2.Craft:Start`

Starts crafting the setup queue, the same as `ogre craft start` and OgreBotAPI.Craft:Start (without the for-who). It is refused with a console line and LastError when you are not in the world, a run is already going, or the setup queue is empty, and a refused start changes nothing.

```text
ISXOgreEQ2.Craft:Start
```

### `StartLLL`

`ISXOgreEQ2.Craft:StartLLL`

Starts low level leveling, a loop that crafts low-level recipes round after round and stops when your tradeskill level is 9, or 19 or higher - the same as `ogre craft lll` and OgreBotAPI.Craft:StartLLL. It is refused when you are not in the world or a run is already going.

```text
ISXOgreEQ2.Craft:StartLLL
```

### `StartQuest`

`ISXOgreEQ2.Craft:StartQuest[]`

Crafts the recipe steps of the quest selected in your journal, one of each per pass, until no craftable step is left; it keeps to that quest even if you select another one mid-run. It is refused when no quest is selected, a crafting flow is already running, or you are not in the world, and is the same as OgreBotAPI.Craft:StartQuest.

```text
ISXOgreEQ2.Craft:StartQuest
```

### `StartTinker`

`ISXOgreEQ2.Craft:StartTinker`

Starts auto tinkering, a loop that crafts tinkering recipes round after round and ends when you have no tinkering skill or it is at its maximum - the same as `ogre craft tinker` and OgreBotAPI.Craft:StartTinker. It is refused when you are not in the world or a run is already going.

```text
ISXOgreEQ2.Craft:StartTinker
```

### `StartWrits`

`ISXOgreEQ2.Craft:StartWrits`

Starts a writs (rush order) run for as many writs as the writ count setting (default 10), the same as `ogre craft writs` and OgreBotAPI.Craft:StartWrits. It is refused below tradeskill level 20, when you are not in the world, or when a run is already going.

```text
ISXOgreEQ2.Craft:StartWrits
```

### `Status`

`ISXOgreEQ2.Craft:Status[]`

Prints the crafting state to the console: craft lite on or off, the flow, the status text, crafted of total, the number of recipes read from your book, and the last error when there is one. It changes nothing.

```text
ISXOgreEQ2.Craft:Status
```

### `Stop`

`ISXOgreEQ2.Craft:Stop`

Stops the running crafting run and drops a pause, printing "craft: stopping (Craft:Stop)." to the console, while the panel stays open (End closes it). With no run going it drops a pause and prints that nothing is running, the same as `ogre craft stop`.

```text
ISXOgreEQ2.Craft:Stop
```
