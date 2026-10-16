# OgreCraft

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../index.md).
</div>

What Classic's *OgreCraftAPI Reference* page described, plus the crafting bot's own `OgreCraft` object, and what each one is in the new bot.

> **:warning: An old call does nothing now - it does not give an error**
>
> The new bot does not keep the old names. A call to an old method silently does nothing and a read of an old member gives `NULL`. Find your name below and write what the row says instead.

## At a glance

| What happened | Names |
|---|---|
| ⚠️ Arguments changed | 3 |
| ⚠️ Argument order changed | 4 |
| ✏️ Renamed | 7 |
| ➡️ Moved | 23 |
| ➡️ Lives somewhere else | 5 |
| ⛔ Removed | 7 |
| ✅ Works as is | 3 |
| **Total** | **52** |

## Worked examples

One real Classic line per kind of change, and the line that replaces it.

### ⚠️ Argument order changed: `OgreCraft:AddRecipeName`

```
; before (Classic)
OgreCraft:AddRecipeName[100,"Voidpiercer's Crossbow of Endurance"]
; after (new bot)
ISXOgreEQ2.Craft:AddRecipe["Voidpiercer's Crossbow of Endurance",100]
```

### ✏️ Renamed: `OgreCraft.Crafting`

```
; before (Classic)
while ${OgreCraft.Crafting}
; after (new bot)
while ${ISXOgreEQ2.Craft.Running}
```

### ➡️ Moved: `OgreCraft.IsReady`

```
; before (Classic)
while !${OgreCraft.IsReady}
; after (new bot)
while !${ISXOgreEQ2.Craft.IsReady}
```

## OgreCraftAPI

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreCraftAPI:AddLastScribedRecipe` | does nothing | `OgreBotAPI.Craft:AddLastScribedRecipe` | ➡️ Moved | Same argument order [forwho, quantity]. Says so and does nothing if nothing was scribed this session. |
| `OgreCraftAPI:AddRecipe` | does nothing | `ISXOgreEQ2.Craft:AddRecipe` | ➡️ Moved | Same arguments, same order. Also accepts 'lastknownrecipe'. For another session: OgreBotAPI.Craft:AddRecipe[forwho,nameOrID,qty]. |
| `OgreCraftAPI:AddRecipeListFromFile` | does nothing | `ISXOgreEQ2.Craft:AddRecipeListFromFile` | ➡️ Moved | The argument is the name of one of your saved queues; the extension is optional. There is no for-who door: OgreBotAPI.Craft does not register it. |
| `OgreCraftAPI:AddRecipeNameForWho` | does nothing | `OgreBotAPI.Craft:AddRecipe` | ⚠️ Argument order changed | Renamed AND reordered. OgreCraft (ogre craftold) order: [forwho, quantity, name]. OgreCraftAPI (ogre craft) and the doc: [forwho, name, quantity]. New: [forwho, name\|id\|lastknownrecipe, quantity]. The name is now required - there is no default; pass lastknownrecipe explicitly. |
| `OgreCraftAPI:AddRecipesFromQuest` | does nothing | `ISXOgreEQ2.Craft:StartQuest` | ✏️ Renamed | It now CRAFTS, not just queues - do not follow it with Start or StartWrits. Select the quest in the journal first. For another session: OgreBotAPI.Craft:StartQuest[forwho]. |
| `OgreCraftAPI:BuyAllTinkeringRecipes` | does nothing | `ISXOgreEQ2.Craft:BuyAllTinkeringRecipes` | ➡️ Moved | For another session: OgreBotAPI.Craft:BuyAllTinkeringRecipes[forwho]. |
| `OgreCraftAPI:Complete_Navigation` | does nothing | `ISXOgreEQ2.Craft:CompleteNavigation` | ✏️ Renamed | Underscore dropped. For another session: OgreBotAPI.Craft:CompleteNavigation[forwho]. |
| `OgreCraftAPI.Crafting` | reads NULL | `ISXOgreEQ2.Craft.Running` | ✏️ Renamed |  |
| `OgreCraftAPI:Defer_Navigation` | does nothing | `ISXOgreEQ2.Craft:DeferNavigation` | ✏️ Renamed | Underscore dropped. For another session: OgreBotAPI.Craft:DeferNavigation[forwho]. |
| `OgreCraft_CraftingStatusUpdate` | works | — | ✅ Works as is |  |
| `OgreCraft_NavigationRequired` | works | — | ✅ Works as is | Same name and one-JSON-argument payload. Answer it with ISXOgreEQ2.Craft:CompleteNavigation / :DeferNavigation (the underscore forms went). |
| `OgreCraft_RecipeQueueUpdated` | works | — | ✅ Works as is |  |
| `OgreCraftAPI.Get_NavigationDetails` | reads NULL | `ISXOgreEQ2.Craft.NavigationDetails` | ⚠️ Arguments changed | Renamed AND the return type changed: it is a string of JSON, not a jsonvalue - `${...Get_NavigationDetails.AsJSON~}` no longer applies. Parse it into your own jsonvalue (e.g. jv:SetValue["${ISXOgreEQ2.Craft.NavigationDetails~}"]). |
| `OgreCraftAPI.IsReady` | reads NULL | `ISXOgreEQ2.Craft.IsReady` | ➡️ Moved |  |
| `OgreCraftAPI.Paused` | reads NULL | `ISXOgreEQ2.Craft.Paused` | ➡️ Moved |  |
| `OgreCraftAPI.QueuedCommands` | reads NULL | `ISXOgreEQ2.Craft.Running` | ➡️ Lives somewhere else | Busy y/n: ${ISXOgreEQ2.Craft.Running}. What it is doing: ${ISXOgreEQ2.Craft.Stage} (a word to branch on: countingResources checkingFuel nextRecipe findingStation summoningStation walking crafting finishing / findingWrit gettingWrit waitingForWrit readingSteps clipboard turningIn nextWrit / buyingBooks pickingRecipe disposing / idle), .Status (display text), .Crafted / .CraftTotal (3 of 10). All of it at once: ${ISXOgreEQ2.Craft.Details} (JSON: running paused flow stage status crafted craftTotal recipe row rows lastError). Done, without polling: the event OgreCraft_CraftingStatusUpdate - Status CraftQueue_End / Writs_End / Quest_End / AutoTinkering_End / LLL_End.<br>… |
| `OgreCraftAPI.QueueUpdated` | reads NULL | `ISXOgreEQ2.Craft.QueueUpdated` | ➡️ Moved |  |
| `OgreCraftAPI.RecipesInQueue` | reads NULL | `ISXOgreEQ2.Craft.RecipesInQueue` | ➡️ Moved | The new count is setup-queue ROWS (Craft2's meaning).'s version actually counted distinct COMPONENTS (ic_Components), so a craftold script's number will differ. |
| `OgreCraftAPI:ScribeRecipe` | does nothing | `OgreBotAPI.Craft:ScribeRecipe` | ➡️ Moved | Same argument order [forwho, name\|all]. The script door without a for-who is ISXOgreEQ2.Craft:ScribeRecipe[name]. |
| `OgreCraftAPI:ShowMainWindow` | does nothing | `ISXOgreEQ2.Craft:Open` | ⚠️ Arguments changed | One bool became two calls: TRUE -&gt; ISXOgreEQ2.Craft:Open, FALSE -&gt; ISXOgreEQ2.Craft:Close. Open also turns on the reaction engine (craft lite) and marks craft open. |
| `OgreCraftAPI:ShowQueueWindow` | does nothing | `ogre craft` | ➡️ Lives somewhere else | No scriptable equivalent of showing/hiding just the queue; open the panel (ISXOgreEQ2.Craft:Open) and use its Queues tab. |
| `OgreCraftAPI:Start` | does nothing | `OgreBotAPI.Craft:Start` | ➡️ Moved | Same argument [forwho]. The script door without a for-who is ISXOgreEQ2.Craft:Start. |
| `OgreCraftAPI:StartLLL` | does nothing | `OgreBotAPI.Craft:StartLLL` | ➡️ Moved | Same argument [forwho]. Script door without for-who: ISXOgreEQ2.Craft:StartLLL. |
| `OgreCraftAPI:StartWrits` | does nothing | `OgreBotAPI.Craft:StartWrits` | ➡️ Moved | Same argument [forwho]. Script door without for-who: ISXOgreEQ2.Craft:StartWrits. |
| `OgreCraftAPI.Version` | reads NULL | `ISXOgreEQ2.Version` | ➡️ Lives somewhere else | This is the whole extension's version, not a separate craft version. |
| `OgreCraftAPI.WaitingForNavigation` | reads NULL | `ISXOgreEQ2.Craft.WaitingForNavigation` | ➡️ Moved |  |

## OgreCraft

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreCraft:AddLastScribedRecipe` | does nothing | `OgreBotAPI.Craft:AddLastScribedRecipe` | ➡️ Moved | Same argument order [forwho, quantity]. Says so and does nothing if nothing was scribed this session. |
| `OgreCraft:AddRecipeID` | does nothing | `ISXOgreEQ2.Craft:AddRecipe` | ⚠️ Argument order changed | Classic order [quantity, id]; new order [id, quantity]. Renamed too (AddRecipeID and AddRecipeName are one call now). |
| `OgreCraft:AddRecipeListFromFile` | does nothing | `ISXOgreEQ2.Craft:AddRecipeListFromFile` | ➡️ Moved | The argument is the name of one of your saved queues; the extension is optional. There is no for-who door: OgreBotAPI.Craft does not register it. |
| `OgreCraft:AddRecipeName` | does nothing | `ISXOgreEQ2.Craft:AddRecipe` | ⚠️ Argument order changed | Classic order [quantity, name]; new order [name, quantity] (quantity defaults to 1). Renamed too. For another session, OgreBotAPI.Craft:AddRecipe takes the same two with the for-who in front. |
| `OgreCraft:AddRecipeNameForWho` | does nothing | `OgreBotAPI.Craft:AddRecipe` | ⚠️ Argument order changed | Renamed AND reordered. OgreCraft (ogre craftold) order: [forwho, quantity, name]. OgreCraftAPI (ogre craft) and the doc: [forwho, name, quantity]. New: [forwho, name\|id\|lastknownrecipe, quantity]. The name is now required - there is no default; pass lastknownrecipe explicitly. |
| `OgreCraft:BuyTinkering` | does nothing | `ISXOgreEQ2.Craft:BuyAllTinkeringRecipes` | ✏️ Renamed | For another session: OgreBotAPI.Craft:BuyAllTinkeringRecipes[forwho]. Scribing follows the panel's 'Scribe recipes' box. |
| `OgreCraft:CheckForMissingDevices` | does nothing | — | ⛔ Removed | The Classic call never did anything - delete the line. |
| `OgreCraft.Crafting` | reads NULL | `ISXOgreEQ2.Craft.Running` | ✏️ Renamed |  |
| `OgreCraft:DumpMissingResources` | does nothing | — | ⛔ Removed | Read ${ISXOgreEQ2.Craft.Details} - a JSON string; its "short" array has each missing resource's name, need, have and fuel flag.<br>Classic craft1 copied sc_MissingResources into a caller-named global collection; craft2 dropped it and nothing calls it. Removed 2026-10-14: the list is ${ISXOgreEQ2.Craft.Details} "short". |
| `OgreCraft:DumpRecipeIDList` | does nothing | — | ⛔ Removed | Nothing calls it - delete the line. ${ISXOgreEQ2.Craft.RecipesInQueue} gives the row count. |
| `OgreCraft.iCounter` | reads NULL | — | ⛔ Removed | An object-scope loop counter of the older Object_OgreCraftAPI (used by its own for-loops); never part of the script API, and the documented object has no such member. |
| `OgreCraft.IsReady` | reads NULL | `ISXOgreEQ2.Craft.IsReady` | ➡️ Moved |  |
| `OgreCraft.LastScribedRecipeID` | reads NULL | `ISXOgreEQ2.Craft.LastScribedRecipeId` | ✏️ Renamed | ID -&gt; Id (the bot's one spelling). 0 until a scribe is seen this session. |
| `OgreCraft.LastScribedRecipeName` | reads NULL | `ISXOgreEQ2.Craft.LastScribedRecipeName` | ➡️ Moved | "" until a scribe is seen this session. |
| `OgreCraft.MissingDevice` | reads NULL | — | ⛔ Removed | It never returned a value - delete the read. |
| `OgreCraft.MissingResources` | reads NULL | `ISXOgreEQ2.Craft.MissingResources` | ➡️ Moved | TRUE when the latest queue's count came up short (fuel the run bought is not short). It is known once a run has counted (stage countingResources ends) and stays readable after the run; FALSE before any count and when 'Do not process resources' skips it. The list: ${ISXOgreEQ2.Craft.Details} "short" (name / need / have / fuel). |
| `OgreCraft.Paused` | reads NULL | `ISXOgreEQ2.Craft.Paused` | ➡️ Moved |  |
| `OgreCraft.QueuedCommands` | reads NULL | `ISXOgreEQ2.Craft.Running` | ➡️ Lives somewhere else | Busy y/n: ${ISXOgreEQ2.Craft.Running}. What it is doing: ${ISXOgreEQ2.Craft.Stage} (a word to branch on: countingResources checkingFuel nextRecipe findingStation summoningStation walking crafting finishing / findingWrit gettingWrit waitingForWrit readingSteps clipboard turningIn nextWrit / buyingBooks pickingRecipe disposing / idle), .Status (display text), .Crafted / .CraftTotal (3 of 10). All of it at once: ${ISXOgreEQ2.Craft.Details} (JSON: running paused flow stage status crafted craftTotal recipe row rows lastError). Done, without polling: the event OgreCraft_CraftingStatusUpdate - Status CraftQueue_End / Writs_End / Quest_End / AutoTinkering_End / LLL_End.<br>… |
| `OgreCraft.QueueUpdated` | reads NULL | `ISXOgreEQ2.Craft.QueueUpdated` | ➡️ Moved |  |
| `OgreCraft.RecipesInQueue` | reads NULL | `ISXOgreEQ2.Craft.RecipesInQueue` | ➡️ Moved | The new count is setup-queue ROWS (Craft2's meaning).'s version actually counted distinct COMPONENTS (ic_Components), so a craftold script's number will differ. |
| `OgreCraft:ScribeRecipe` | does nothing | `OgreBotAPI.Craft:ScribeRecipe` | ➡️ Moved | Same argument order [forwho, name\|all]. The script door without a for-who is ISXOgreEQ2.Craft:ScribeRecipe[name]. |
| `OgreCraft:ShowMainWindow` | does nothing | `ISXOgreEQ2.Craft:Open` | ⚠️ Arguments changed | One bool became two calls: TRUE -&gt; ISXOgreEQ2.Craft:Open, FALSE -&gt; ISXOgreEQ2.Craft:Close. Open also turns on the reaction engine (craft lite) and marks craft open. |
| `OgreCraft:ShowQueueWindow` | does nothing | `ogre craft` | ➡️ Lives somewhere else | No scriptable equivalent of showing/hiding just the queue; open the panel (ISXOgreEQ2.Craft:Open) and use its Queues tab. |
| `OgreCraft:Start` | does nothing | `OgreBotAPI.Craft:Start` | ➡️ Moved | Same argument [forwho]. The script door without a for-who is ISXOgreEQ2.Craft:Start. |
| `OgreCraft:UpdateScribedRecipe` | does nothing | — | ⛔ Removed | Nothing to call - delete the line. The last scribed recipe is tracked automatically, including scrolls scribed by hand. |
| `OgreCraft:UpdateWritFiles` | does nothing | — | ⛔ Removed | Delete the line; there are no writ XML files to reload. |
