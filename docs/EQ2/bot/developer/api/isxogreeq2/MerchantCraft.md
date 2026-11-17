<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# ISXOgreEQ2.MerchantCraft

## Methods

### `Help`

`ISXOgreEQ2.MerchantCraft:Help`

Prints the `ogre mc` usage lines to the console and does nothing else. It is what `ogre mc help` runs.

```text
ISXOgreEQ2.MerchantCraft:Help
```

### `List`

`ISXOgreEQ2.MerchantCraft:List`

Reads the recipes your TARGETED merchant sells and prints them numbered, for use with Start["#n"]. It is refused with a console warning when a run is already going, you are not in the world, the target is not a merchant within 9 m, or you lack the Summon Crafting Stations ability.

```text
ISXOgreEQ2.MerchantCraft:List
```

### `Start`

`ISXOgreEQ2.MerchantCraft:Start[words...]`

The engine behind `ogre mc <recipe> [count]`: for each round it buys the recipe from your targeted merchant (only if you do not know it), scribes it, summons the crafting station it needs, empties the craft engine's setup queue and crafts it 3 times. It has the same refusals as List and also refuses with no recipe or while a craft run is going; on a recipe not yet cached it MAKES A SERVER CALL (`.ToRecipeInfo`, to learn the crafting device), and only when the craft panel's "Allow recipe-info server call" option is on, which it is by default.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `words...` | string |  | a partial recipe name (one or more words, first match wins) or "#n" for row n of List's numbering, then an optional trailing whole number = rounds (1 to 999, default 1; each round is 3 crafts) |

```text
ISXOgreEQ2.MerchantCraft:Start[ferrite,bracelet,4]
```

### `Status`

`ISXOgreEQ2.MerchantCraft:Status`

Prints the merchant-craft state (running or idle, the current recipe and round, how many recipes the last scan found) and then the usage lines to the console. It is what bare `ogre mc` and `ogre mc status` run.

```text
ISXOgreEQ2.MerchantCraft:Status
```

### `Stop`

`ISXOgreEQ2.MerchantCraft:Stop`

Abandons the merchant-craft run and prints "mc: stopped.", or "mc: nothing is running." when idle. It does not stop a craft queue the run already started, and a summoned station stays.

```text
ISXOgreEQ2.MerchantCraft:Stop
```
