# Collection Manager

The Ogre Collection Manager automatically scribes collectibles from your collection depots or inventory.

---

## Depot Version

Stand near a collection depot and run one of the following commands:

```
ogre collection
ogre collections
ogre cm
```

The script navigates through the collection depot inventory and adds every collectible to your collections. It works with both standard and large collection depots, automatically selecting the closest one.

**Optional parameters:**

| Command | Description |
|---------|-------------|
| `ogre cm -large` | Force use of the large depot |
| `ogre cm -small` | Force use of the small depot |

**To stop:**

```
ogre end collection
ogre end collections
ogre end cm
```

---

## Inventory Version

To scribe collectibles directly from your inventory:

```
ogre cm 1
ogre cm -inventory
```

The script goes through your inventory and adds every collectible to your collections.

**To stop:** Same end commands as the depot version.

---

## Notes

- Only requirement is proximity to a collection depot (for depot version)
- On completion, you will see a summary message, e.g.: `Ogre Collection Manager added 125 collectibles in 407.1 Seconds.`

<!-- Source: wiki.ogregaming.com/eq2/index.php/Ogre_Collection_Manager - This page may need updating -->
