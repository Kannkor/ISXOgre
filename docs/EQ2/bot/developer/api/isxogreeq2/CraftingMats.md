# ISXOgreEQ2.CraftingMats

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Members

### `Keys`

`${ISXOgreEQ2.CraftingMats.Keys}`

The keys of the loaded lists, comma separated - each key is also the flag that picks that list in Get and Plan (the shipped ones are cd, ka, mm, pop and vov). Re-reads the list files first if any changed on disk.

**Returns:** string: the loaded list keys joined with ", "; "" when none loaded

```text
echo ${ISXOgreEQ2.CraftingMats.Keys}
```

### `Lists`

`${ISXOgreEQ2.CraftingMats.Lists}`

How many crafting-mats lists are loaded: the shipped ones plus your own from OgreSave/EQ2/CraftingMats/custom. Reading it first re-reads the list files if any changed on disk; any load warnings are in Warnings, and Get, Plan and Reload print them.

**Returns:** int: number of loaded lists; 0 when no list files were found

```text
echo ${ISXOgreEQ2.CraftingMats.Lists}
```

### `Warnings`

`${ISXOgreEQ2.CraftingMats.Warnings}`

The warnings the last load of the list files produced, such as an unreadable file; Get, Plan and Reload also print them each time they run. Re-reads the list files first if any changed on disk.

**Returns:** string: the warnings joined with " \| "; "" when the load was clean

```text
echo ${ISXOgreEQ2.CraftingMats.Warnings}
```

## Methods

### `End`

`ISXOgreEQ2.CraftingMats:End`

Stops a depot withdraw that a crafting-mats run started (only that one) and closes the editor window; unsaved edits are kept for the next Open. This is what `ogre end craftingmats` and the window's X do.

```text
ISXOgreEQ2.CraftingMats:End
```

### `Get`

`ISXOgreEQ2.CraftingMats:Get[flags...]`

Works out the mats for the chosen lists and categories, prints any list-file warnings and the plan, then starts pulling them from the Harvesting Supply Depot and buying any fuel at the Guild Fuel Merchant on the pulse after the call returns (the same as `ogre craftingmats -<flags>`). No flags pulls the Visions of Vetrovia signature line; nothing is pulled when not in world, when another depot errand is running, or when only unknown words were given, and the run stops if no depot is within 11 of you.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `flags...` | string |  | Any mix, dash optional, any case: a list key (-vov, -cd, -mm, -pop, -ka or your own list's key), -sig / -s, -daily / -d, -weekly / -w, -plan to print only, help. A list with no category uses its own signature line (daily + weekly for Kunark's Ascending), a category with no list uses Visions of Vetrovia, and unknown words are ignored with one warning. |

```text
ISXOgreEQ2.CraftingMats:Get[-vov,-daily,-weekly]
```

### `Help`

`ISXOgreEQ2.CraftingMats:Help`

Prints the `ogre craftingmats` usage to the console: the list and category flags, the defaults, the script calls and where to put your own lists so updates never overwrite them.

```text
ISXOgreEQ2.CraftingMats:Help
```

### `Open`

`ISXOgreEQ2.CraftingMats:Open`

Opens the Crafting Mats list editor window, where you change a list and save it to your own custom file (the same as bare `ogre craftingmats`). Calling it while the window is open changes nothing, and without the Ogre UI desktop it prints a warning instead.

```text
ISXOgreEQ2.CraftingMats:Open
```

### `Plan`

`ISXOgreEQ2.CraftingMats:Plan[flags...]`

Prints any list-file warnings and the shopping list Get would use - the mats to pull from the depot and the fuel to buy - and touches neither the depot nor the merchant. Takes the same flags as Get; no flags plans the Visions of Vetrovia signature line.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `flags...` | string |  | Any mix, dash optional, any case: a list key (-vov, -cd, -mm, -pop, -ka or your own list's key), -sig / -s, -daily / -d, -weekly / -w, -plan to print only, help. A list with no category uses its own signature line (daily + weekly for Kunark's Ascending), a category with no list uses Visions of Vetrovia, and unknown words are ignored with one warning. |

```text
ISXOgreEQ2.CraftingMats:Plan[-ka]
```

### `Reload`

`ISXOgreEQ2.CraftingMats:Reload`

Re-reads every list file from disk now, prints any warnings the load produced, then "craftingmats: reloaded -" with the list count and keys. Rarely needed: the lists are re-read by themselves whenever a list file changes.

```text
ISXOgreEQ2.CraftingMats:Reload
```
