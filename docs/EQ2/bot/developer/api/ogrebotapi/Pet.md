# OgreBotAPI.Pet

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Methods

### `Assist`

`OgreBotAPI.Pet:Assist[fw]`

Sends the game command /pet autoassist right away, which toggles your pet assisting you. There is no check that you have a pet, and nothing happens when not in the world or the for-who does not name this character.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.Pet:Assist[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:PetAssist`

### `Attack`

`OgreBotAPI.Pet:Attack[fw]`

Sends the game command /pet attack right away, so your pet attacks your current target. There is no check that you have a pet, and nothing happens when not in the world or the for-who does not name this character.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.Pet:Attack[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:PetAttack`

### `GetLost`

`OgreBotAPI.Pet:GetLost[fw]`

Sends the game command /pet getlost right away, which dismisses your pet. There is no check that you have a pet, and nothing happens when not in the world or the for-who does not name this character.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.Pet:GetLost[all]
```

*Was (OldBot):* `OgreBotAPI:PetGetLost`

### `Off`

`OgreBotAPI.Pet:Off[fw]`

Sends the game command /pet backoff right away, so your pet stops attacking. There is no check that you have a pet, and nothing happens when not in the world or the for-who does not name this character.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.Pet:Off[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:PetOff`
