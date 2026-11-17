# OgreBotAPI.Access

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Members

### `UnauthPCsNearMe`

`${OgreBotAPI.Access.UnauthPCsNearMe[dist]}`

TRUE when another player character closer to you than dist is not one of the characters saved in your accounts list (EQ2Chars), matched by name ignoring case. Your own character never counts, a nearby player whose name has not loaded counts as not yours, and a dist that is not a number reads as 0, which is always FALSE.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `dist` | float | `999` | range from you; a player counts only when strictly closer than this |

**Returns:** bool: TRUE when at least one player character within dist is not one of your saved characters; FALSE when no other player is within dist or every one of them is yours.

```text
echo ${OgreBotAPI.Access.UnauthPCsNearMe[200]}
```

*Was (OldBot):* `OgreBotAPI.UnauthPCsNearMe`

## Methods

### `SetLevel`

`OgreBotAPI.Access:SetLevel[fw, value, silent=FALSE]`

Sets this session's access level to value at once, clamped between 0 and the highest level your account has; asking for more than that uses your highest level and prints a warning. The new level is announced in the console only when it actually changed, and silent TRUE hides both the warning and the announcement; it also works at the character select screen.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `value` | int |  | the level to set; below 0 becomes 0, above your highest level becomes your highest level, and a value that is not a number counts as 0 |
| `silent` | bool | `FALSE` | TRUE hides the over-the-maximum warning and the level-changed announcement |

```text
OgreBotAPI.Access:SetLevel[${Me.Name},0]
```
