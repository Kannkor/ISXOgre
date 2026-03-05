# OgreCraftAPI Reference

The `OgreCraftAPI` is the primary interface for interacting with OgreCraft from scripts and automation. It provides methods and members for controlling crafting operations, managing recipe queues, scribing recipes, and handling navigation during crafting workflows.

This reference covers every available method and member on the `OgreCraftAPI` object. Use it as a comprehensive lookup when writing crafting automation scripts or integrating OgreCraft with other systems like Instance Controllers.

---

## Usage Pattern

```lavishscript
OgreCraftAPI:MethodName["param1", param2]
${OgreCraftAPI.MemberName}
```

> **:memo: Note**
>
> OgreCraft must be loaded before using the API. Always check `${OgreCraftAPI.IsReady}` before making calls.

## The _ForWho Parameter

Several methods accept a `_ForWho` parameter that controls which characters execute the command:

| Target | Description |
|--------|-------------|
| `"all"` | All characters |
| `"${Me.Name}"` | Only the current character |

> **:bulb: Tip**
>
> When using cross-session commands (`oc !c` or `oc !ci`), prefix with `igw:${Me.Name}` to scope the command to your group.

---

## Members

Members are read-only properties accessed with `${OgreCraftAPI.MemberName}`.

| Member | Return Type | Description |
|--------|-------------|-------------|
| `Version` | `string` | Returns the current OgreCraft version |
| `IsReady` | `bool` | Returns `TRUE` if OgreCraft is fully loaded and ready |
| `Paused` | `bool` | Returns `TRUE` if OgreCraft is currently paused |
| `QueuedCommands` | `bool` | Returns `TRUE` if there are queued commands waiting to execute |
| `Crafting` | `bool` | Returns `TRUE` if OgreCraft is actively crafting |
| `QueueUpdated` | `bool` | Returns `TRUE` if the recipe queue has finished processing updates |
| `WaitingForNavigation` | `bool` | Returns `TRUE` if OgreCraft is waiting for navigation to complete |
| `Get_NavigationDetails` | `jsonvalue` | Returns a JSON object with details about the current navigation request |
| `RecipesInQueue` | `int` | Returns the number of recipes currently in the crafting queue |

### Member Examples

```lavishscript
; Check if OgreCraft is loaded before doing anything
if ${OgreCraftAPI.IsReady}
{
    echo OgreCraft is ready! Version: ${OgreCraftAPI.Version}
}

; Wait for OgreCraft to be ready
while !${OgreCraftAPI.IsReady}
    wait 10

; Check if currently crafting
if ${OgreCraftAPI.Crafting}
{
    echo OgreCraft is actively crafting.
}

; Check how many recipes are queued
echo Recipes in queue: ${OgreCraftAPI.RecipesInQueue}

; Check if the queue has finished processing
if ${OgreCraftAPI.QueueUpdated}
{
    echo Queue is up to date.
}

; Check if paused
if ${OgreCraftAPI.Paused}
{
    echo OgreCraft is paused.
}

; Handle navigation requests
if ${OgreCraftAPI.WaitingForNavigation}
{
    variable jsonvalue navDetails
    navDetails:SetValue[${OgreCraftAPI.Get_NavigationDetails.AsJSON~}]
    echo Navigation required: ${navDetails.AsJSON~}
}
```

---

## Methods

Methods perform actions and are called with `OgreCraftAPI:MethodName[params]`.

### Recipe Management

| Method | Description |
|--------|-------------|
| `ScribeRecipe(string _ForWho="all", string _RecipeName="all")` | Scribe recipe books from inventory |
| `AddRecipe(string _RecipeNameOrID, int _Quantity=1)` | Add a recipe to the crafting queue by name or ID |
| `AddRecipeNameForWho(string _ForWho="all", string _RecipeName="lastknownrecipe", int _Quantity=1)` | Add a recipe to the queue for specific characters |
| `AddLastScribedRecipe(string _ForWho="all", int _Quantity=1)` | Add the most recently scribed recipe to the queue |
| `AddRecipeListFromFile(string _FileInfo)` | Load a list of recipes from a file into the queue |
| `AddRecipesFromQuest()` | Automatically add recipes needed for the current crafting writ |
| `BuyAllTinkeringRecipes()` | Purchase all tinkering recipes from the vendor |

#### Recipe Management Examples

```lavishscript
; Scribe all recipe books in your inventory
OgreCraftAPI:ScribeRecipe["all", "all"]

; Scribe a specific recipe book
OgreCraftAPI:ScribeRecipe["${Me.Name}", "Advanced Carpenter Volume 99"]

; Add a recipe to the queue by name (craft 5 of them)
OgreCraftAPI:AddRecipe["Alder Round Shield", 5]

; Add a recipe to the queue by recipe ID
OgreCraftAPI:AddRecipe["12345", 1]

; Add a recipe for a specific character
OgreCraftAPI:AddRecipeNameForWho["${Me.Name}", "Alder Round Shield", 10]

; Add the last scribed recipe to the queue
OgreCraftAPI:AddLastScribedRecipe["all", 1]

; Load recipes from a saved file
OgreCraftAPI:AddRecipeListFromFile["MyRecipeList.json"]

; Add recipes needed for the current writ quest
OgreCraftAPI:AddRecipesFromQuest

; Buy all tinkering recipes from Fizza Cogsworth
OgreCraftAPI:BuyAllTinkeringRecipes
```

### Crafting Control

| Method | Description |
|--------|-------------|
| `Start(string _ForWho="all")` | Start crafting the recipes in the queue |
| `StartWrits(string _ForWho="all")` | Start crafting in writ mode |
| `StartLLL(string _ForWho="all")` | Start low-level leveling mode |

#### Crafting Control Examples

```lavishscript
; Start crafting the queued recipes
OgreCraftAPI:Start["all"]

; Start crafting only on the current character
OgreCraftAPI:Start["${Me.Name}"]

; Start writ crafting mode
OgreCraftAPI:StartWrits["all"]

; Start low-level leveling mode
OgreCraftAPI:StartLLL["${Me.Name}"]
```

### Navigation

| Method | Description |
|--------|-------------|
| `Complete_Navigation()` | Signal that navigation has been completed |

#### Navigation Example

```lavishscript
; Check if OgreCraft needs you to navigate somewhere
if ${OgreCraftAPI.WaitingForNavigation}
{
    ; Read the navigation details
    variable jsonvalue navDetails
    navDetails:SetValue[${OgreCraftAPI.Get_NavigationDetails.AsJSON~}]
    echo Navigation needed: ${navDetails.AsJSON~}

    ; ... perform your navigation logic here ...

    ; Tell OgreCraft that navigation is complete
    OgreCraftAPI:Complete_Navigation
}
```

### UI Control

| Method | Description |
|--------|-------------|
| `ShowMainWindow(bool TorF=TRUE)` | Show or hide the OgreCraft main window |
| `ShowQueueWindow(bool TorF=TRUE)` | Show or hide the OgreCraft queue window |

#### UI Control Examples

```lavishscript
; Show the main OgreCraft window
OgreCraftAPI:ShowMainWindow[TRUE]

; Hide the main window
OgreCraftAPI:ShowMainWindow[FALSE]

; Show the queue window
OgreCraftAPI:ShowQueueWindow[TRUE]

; Hide the queue window
OgreCraftAPI:ShowQueueWindow[FALSE]
```

---

## Common Workflows

### Basic Crafting

A simple workflow to add recipes and start crafting:

```lavishscript
; Wait for OgreCraft to be ready
while !${OgreCraftAPI.IsReady}
    wait 10

; Add recipes to the queue
OgreCraftAPI:AddRecipe["Alder Round Shield", 5]
OgreCraftAPI:AddRecipe["Ash Wooden Kite Shield", 3]

; Wait for the queue to process
while !${OgreCraftAPI.QueueUpdated}
    wait 5

; Start crafting
OgreCraftAPI:Start["${Me.Name}"]
```

### Writ Crafting

Set up and run a crafting writ:

```lavishscript
; Wait for OgreCraft to be ready
while !${OgreCraftAPI.IsReady}
    wait 10

; Add writ recipes automatically from the current quest
OgreCraftAPI:AddRecipesFromQuest

; Wait for the queue to process
while !${OgreCraftAPI.QueueUpdated}
    wait 5

; Start writ mode
OgreCraftAPI:StartWrits["${Me.Name}"]
```

### Scribe and Craft

Scribe new recipe books then craft:

```lavishscript
; Wait for OgreCraft to be ready
while !${OgreCraftAPI.IsReady}
    wait 10

; Scribe all recipe books in inventory
OgreCraftAPI:ScribeRecipe["${Me.Name}", "all"]

; Add the last scribed recipe to the queue
OgreCraftAPI:AddLastScribedRecipe["${Me.Name}", 10]

; Wait for the queue to process
while !${OgreCraftAPI.QueueUpdated}
    wait 5

; Start crafting
OgreCraftAPI:Start["${Me.Name}"]
```

---

## Events

OgreCraft fires the following events that your scripts can listen for:

| Event | Description |
|-------|-------------|
| `OgreCraft_NavigationRequired` | Fired when OgreCraft needs navigation to a crafting device or merchant |
| `OgreCraft_RecipeQueueUpdated` | Fired when the recipe queue has been modified |
| `OgreCraft_CraftingStatusUpdate` | Fired when the crafting status changes |

### Listening for Events

```lavishscript
function main()
{
    ; Attach to crafting events
    LavishScript:RegisterEvent[OgreCraft_NavigationRequired]
    Event[OgreCraft_NavigationRequired]:AttachAtom[OnNavigationRequired]

    LavishScript:RegisterEvent[OgreCraft_RecipeQueueUpdated]
    Event[OgreCraft_RecipeQueueUpdated]:AttachAtom[OnQueueUpdated]

    LavishScript:RegisterEvent[OgreCraft_CraftingStatusUpdate]
    Event[OgreCraft_CraftingStatusUpdate]:AttachAtom[OnCraftingStatus]

    ; Your main loop here
    while TRUE
    {
        wait 10
    }
}

function OnNavigationRequired(jsonvalue _jvNavDetails)
{
    echo Navigation required: ${_jvNavDetails.AsJSON~}
}

function OnQueueUpdated(jsonvalue _jvDetails)
{
    echo Queue updated: ${_jvDetails.AsJSON~}
}

function OnCraftingStatus(jsonvalue _jvDetails)
{
    echo Crafting status: ${_jvDetails.AsJSON~}
}
```

---

## Best Practices

> **:bulb: Always Check IsReady**
>
> Before making any API calls, always verify that OgreCraft is loaded with `${OgreCraftAPI.IsReady}`.

> **:bulb: Wait for QueueUpdated**
>
> After adding recipes to the queue, wait for `${OgreCraftAPI.QueueUpdated}` to return `TRUE` before starting crafting. This ensures all recipes have been processed.

> **:warning: Legacy API**
>
> The old `OgreCraft` object (accessed via `${OgreCraft.IsReady}`, `OgreCraft:Start`, etc.) is deprecated. Always use `OgreCraftAPI` instead. If you see console messages about changed calls, update your scripts to use the new API.

---

## Related Documentation

- [OgreCraft Overview](../tools/ogrecraft.md) - General OgreCraft usage and features
- [OgreBotAPI Reference](ogrebot-api.md) - The main OgreBot automation API
- [Coding Practices](coding-practices.md) - Variable naming conventions and code style

<!-- Source: EQ2OgreCraft/OgreCraftUI2.iss — Object_OgreCraftAPI (lines 35-129) -->
