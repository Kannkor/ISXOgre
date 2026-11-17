<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# ISXOgreEQ2.ContentBuilder

## Methods

### `End`

`ISXOgreEQ2.ContentBuilder:End`

Closes the Content Builder window (the same as `ogre end contentbuilder` and the window's X). Changes that were not saved are kept and offered back the next time the window opens, and a run it started goes on.

```text
ISXOgreEQ2.ContentBuilder:End
```

### `Open`

`ISXOgreEQ2.ContentBuilder:Open[tier,path]`

Opens the Content Builder window (the same as `ogre contentbuilder`), on a zone file when you name one. A window that is already open comes to the front, and asks before it opens that file over unsaved changes; without the Ogre UI desktop it prints a warning.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `tier` | string | `none` | The root the zone file is in: default or custom. Leave both out to open the window as it was. |
| `path` | string | `none` | The zone file's path inside that root, ending in .json. A path with spaces may be quoted or written as several words. |

```text
ISXOgreEQ2.ContentBuilder:Open[custom,"My_Zone.json"]
```

More: [developer/zone-files/builder.md](../../zone-files/builder.md)
