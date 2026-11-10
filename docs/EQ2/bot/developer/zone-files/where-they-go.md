# Where zone files go

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../index.md).
</div>

| Root | Folder | What it is |
|---|---|---|
| default | `Scripts\Ogre\EQ2\IC\default\` | The zone files that ship with Ogre. An update can replace them, so do not keep your changes here. |
| test | `Scripts\Ogre\EQ2\IC\test\` | Zone files that are still being tested. |
| custom | `Scripts\OgreSave\EQ2\IC\custom\` | Yours. Ogre's updates never touch this folder. |

- Every file ending in `.json`, in any folder under a root, is read.
- A number at the start of a file name, like `_01_`, sorts the list: numbered files come first, in number order.
- Every root loads. The same file in two roots shows up twice in the IC window: they are separate files, and
  neither replaces the other.

## Your own folders inside custom

`Scripts` is the Scripts folder inside the folder InnerSpace is installed in, so the custom root is
`OgreSave\EQ2\IC\custom\` inside that Scripts folder.

You can make folders of your own inside `custom`, as deep as you like, and keep zone files in them. For example, one
folder per person who writes zone files:

```text
OgreSave\EQ2\IC\custom\kannkor\_01_My_Zone.json
OgreSave\EQ2\IC\custom\lostone\_02_Another_Zone.json
```

The IC window shows them as folders under **custom**. A file's path is its folder inside the root plus its name,
written with `/`, and that is how a script or the console queues it:

```text
ISXOgreEQ2.IC:Queue[add,custom,"kannkor/_01_My_Zone.json"]
ogre ic queue add custom kannkor/_01_My_Zone.json
```

The three roots are fixed: there is no setting that points IC at another folder. Put your files under `custom`.

## File names

The zone files that ship with Ogre are named after their zone: take the zone's name, turn each space into `_`, and
leave out `:` `'` `,` `[` `]` and the backtick. A file for one difficulty adds that difficulty to its name; a file for
several difficulties does not. The number in front is kept.

| File | `zone` | `variants` |
|---|---|---|
| `_01_Oogothl_Sprawl_VerBohten_Atoll.json` | `Oogothl Sprawl: Ver'Bohten Atoll` | `[Solo]`, `[Heroic]` |
| `_01_Sodden_Archipelago_The_Forsaken_Isle.json` | `Sodden Archipelago: The Forsaken Isle` | `[Solo]`, `[Heroic I]` |
| `_01_Sodden_Archipelago_The_Forsaken_Isle_Heroic_II.json` | `Sodden Archipelago: The Forsaken Isle` | `[Heroic II]` |

Your own files in `custom` can have any name. Name them this way and they can be queued by name too.

## Queue a zone by its name

`ogre ic queue add <zone name>` queues the zone file named after that zone. Write the difficulty in the name, the way
the game writes it: `ogre ic queue add Oogothl Sprawl: Ver'Bohten Atoll [Heroic]`. `ogre ic queue add ${Zone.Name}`
queues the zone you are standing in. The console says which file it picked, then queues it as **Add** does.

- The name needs the difficulty whenever the zone has one. Without it nothing is queued, and the line lists the
  difficulties its files cover:
  `"Oogothl Sprawl: Ver'Bohten Atoll" is in a file for [Solo] and [Heroic] - name one: ogre ic queue add Oogothl Sprawl: Ver'Bohten Atoll [Heroic]`.
- A difficulty that no file of that zone covers is refused the same way, and the line lists the ones that are covered.
- Case does not matter: `[heroic]` is `[Heroic]`.
- The cleaned name works too, difficulty included: `ogre ic queue add Oogothl_Sprawl_VerBohten_Atoll_Heroic`.
- When more than one root has a file of that name, `custom` is used first, then `test`, then `default`.
- `ogre ic queue add <root> <zone name>` looks in that root only: `ogre ic queue add custom ${Zone.Name}` queues your own
  file for the zone you are standing in, even if Ogre ships one too.
- `ogre ic queue add <root> <path>` still queues any file by its root and its path (a path ends in `.json`). `ogre ic list`
  prints every loaded file.

A queued zone whose file is renamed follows its zone: the next time IC loads its list, the row points at the zone's
new file, and the console says so.
