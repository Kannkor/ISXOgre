# OgreBotAPI.Encounter

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Methods

### `List`

`OgreBotAPI.Encounter:List[fw]`

Prints in this character's console the encounter coding for the current zone: one line per fight with its named mobs, (DISABLED) when switched off, and its file. With none it prints "No encounter coding for this zone"; the Settings tab's No Available Setups box does not silence it.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.Encounter:List[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:DisplayAvailableSetups`
