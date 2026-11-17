<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# OgreBotAPI.Assist

## Members

### `InControl`

`${OgreBotAPI.Assist.InControl}`

Whether this character picks its own target instead of following someone else's. With the Auto Assist box off nobody drives this character, so it reads TRUE.

**Returns:** bool: TRUE when auto-target is on, the Auto Assist box is off, you are the assist anchor, or no assist rule names anyone to follow; FALSE when you follow another player, and FALSE when not in the world.

```text
echo ${OgreBotAPI.Assist.InControl}
```

*Was (OldBot):* `OgreBotAPI.InControlOfAssisting`

### `IsAssisting`

`${OgreBotAPI.Assist.IsAssisting}`

The exact opposite of InControl: whether this character follows someone else's target. It reads FALSE whenever the Auto Assist box is off.

**Returns:** bool: TRUE when the Auto Assist box is on and you follow another player's target; FALSE when you pick your own target, and FALSE when not in the world.

```text
echo ${OgreBotAPI.Assist.IsAssisting}
```

*Was (OldBot):* `GetInfoOb.IsAssisting`, `OgreBotAPI.IsAssisting`

### `TargetID`

`${OgreBotAPI.Assist.TargetID}`

The assist decision as one number: who this character would take its target from right now. It is read fresh on each call and reports the decision even when the Auto Assist box is off or auto-target is on.

**Returns:** int64: greater than 0 is the ID to target (with Direct Assist Targeting on, the assisted player's target; otherwise the assisted player, which is your own ID when you are the anchor); 0 when you pick your own target; -1 when your current target should be left alone (Direct Assist Targeting on and the player you assist has no live target); NULL when not in the world.

```text
echo ${OgreBotAPI.Assist.TargetID}
```

*Was (OldBot):* `OgreBotAPI.GetAssistID`

## Methods

### `Anchor`

`OgreBotAPI.Assist:Anchor[fw, who=me]`

Sets who this character takes its kill target from: a group or raid member's name or alias, an actor ID, blank for yourself, or off to clear it (the literal word me is looked up as a name and sets nothing). It does not target anything itself - the bot retargets on its pulse while Auto Assist is ticked, a name not in your group or raid sets nothing and says so in the console, and the anchor clears when you zone into a different zone.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `who` | string | `me` | The player to assist: a name, an alias, an actor ID, or off to clear the anchor; blank anchors on yourself |

```text
OgreBotAPI.Assist:Anchor[igw:${Me.Name},${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:AssistForWho`, `OgreBotAPI:Assist`
