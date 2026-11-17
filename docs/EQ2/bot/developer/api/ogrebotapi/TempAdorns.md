<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# OgreBotAPI.TempAdorns

## Members

### `IsOpen`

`${OgreBotAPI.TempAdorns.IsOpen}`

Returns whether the Temp Adornments window is open on this session.

**Returns:** bool: TRUE when the Temp Adornments window is open; FALSE when it is not.

```text
echo ${OgreBotAPI.TempAdorns.IsOpen}
```

### `Profiles`

`${OgreBotAPI.TempAdorns.Profiles}`

Returns how many temporary-adornment profiles are saved - one profile file is shared by every character on this PC. The first read loads that file and, when there is none yet, creates it with the default profiles CBOC, Pot and HP plus any profiles saved by the classic Temp Adorns window.

**Returns:** int: the number of saved profiles; 0 when there are none or the profile file could not be read.

```text
echo ${OgreBotAPI.TempAdorns.Profiles}
```

## Methods

### `Apply`

`OgreBotAPI.TempAdorns:Apply[fw, profile]`

Queues putting a profile's temporary adornments on your gear: each listed piece gets its adornment from your bags, even a piece that already has it with time left; it skips only pieces with nothing equipped and adornments you do not carry. A blank or unknown profile name, or not being in the world, prints one console line and queues nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `profile` | string |  | the saved profile to apply, any case (CBOC, Pot and HP exist by default); a two-handed primary row in it is used for Primary when your primary weapon is a two-hander |

```text
OgreBotAPI.TempAdorns:Apply[igw:${Me.Name},CBOC]
```

*Was (OldBot):* `OgreBotAPI:ApplyTempAdorn`, `OgreBotAPI:PoP_TempAdorns`

### `Close`

`OgreBotAPI.TempAdorns:Close[fw]`

Closes the Temp Adornments window. Nothing happens when it is not open.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.TempAdorns:Close[${Me.Name}]
```

### `List`

`OgreBotAPI.TempAdorns:List[fw]`

Prints every saved temporary-adornment profile to the console, one line each with its gear pieces and their adornments. Says so when there are no profiles.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.TempAdorns:List[${Me.Name}]
```

### `Open`

`OgreBotAPI.TempAdorns:Open[fw]`

Opens the Temp Adornments window, where profiles are built, saved, deleted and applied. Works at character select too, and does nothing when the window is already open.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.TempAdorns:Open[${Me.Name}]
```
