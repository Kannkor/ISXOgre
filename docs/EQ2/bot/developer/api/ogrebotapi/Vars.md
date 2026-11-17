<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# OgreBotAPI.Vars

## Members

### `Bool`

`${OgreBotAPI.Vars.Bool[name]}`

Reads the script variable name as a yes/no: TRUE only when its whole value is 1, true, yes or on in any case. A missing variable, an empty value or any other text (2, enabled, a value with spaces around it) reads FALSE.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | string |  | The variable name, case-sensitive. |

**Returns:** bool: TRUE when the stored value is a yes word; FALSE otherwise, including when the variable is missing.

```text
echo ${OgreBotAPI.Vars.Bool[UseCampSpot]}
```

*Was (OldBot):* `OgreBotAPI.Get_Variable_Bool`

### `Exists`

`${OgreBotAPI.Vars.Exists[name]}`

TRUE when a variable called name is in this session's script variable store, even if its value is empty. Use it to tell a missing variable from an empty one, since Get returns an empty string for both.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | string |  | The variable name, case-sensitive. |

**Returns:** bool: TRUE when the variable is stored; FALSE when it is missing or name is blank.

```text
echo ${OgreBotAPI.Vars.Exists[PullCount]}
```

*Was (OldBot):* `OgreBotAPI.Get_VariableExists`

### `Get`

`${OgreBotAPI.Vars.Get[name]}`

The value stored under name in this session's script variable store (set with OgreBotAPI.Vars:Set), or an empty string when there is no such variable. Names ignore case, and the store lives in memory on this session only: it is not shared with other characters, not saved, and lasts until it is cleared or the extension is unloaded.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | string |  | The variable name; case does not matter. |

**Returns:** string: the stored value; empty when the variable is missing or was set to an empty value.

```text
echo ${OgreBotAPI.Vars.Get[PullCount]}
```

*Was (OldBot):* `OgreBotAPI.Get_Variable`, `OgreBotAPI.Variables`

### `GetInternal`

`${OgreBotAPI.Vars.GetInternal[name]}`

The value stored under name in the internal variable store (set with OgreBotAPI.Vars:SetInternal), or an empty string when there is no such variable. It is a separate store from Get and Set but lives the same way: in memory on this session only, not shared, not saved; names ignore case.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | string |  | The internal variable name; case does not matter. |

**Returns:** string: the stored value; empty when the variable is missing or was set to an empty value.

```text
echo ${OgreBotAPI.Vars.GetInternal[LastZone]}
```

*Was (OldBot):* `OgreBotAPI.Get_InternalVariable`, `OgreBotAPI.InternalVariables`

### `InternalExists`

`${OgreBotAPI.Vars.InternalExists[name]}`

TRUE when a variable called name is in this session's internal variable store, even if its value is empty. It only looks at the internal store, not the one Get and Set use.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | string |  | The internal variable name, case-sensitive. |

**Returns:** bool: TRUE when the internal variable is stored; FALSE when it is missing or name is blank.

```text
echo ${OgreBotAPI.Vars.InternalExists[LastZone]}
```

*Was (OldBot):* `OgreBotAPI.Get_InternalVariableExists`

## Methods

### `Clear`

`OgreBotAPI.Vars:Clear[fw, name]`

Removes the variable name from the script variable store on each matching character, so Exists then reads FALSE and Get an empty string. Nothing happens when name is blank or the variable is missing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `name` | string |  | The variable name to remove, case-sensitive. |

```text
OgreBotAPI.Vars:Clear[${Me.Name},PullCount]
```

*Was (OldBot):* `OgreBotAPI:Clear_Variable`

### `ClearAll`

`OgreBotAPI.Vars:ClearAll[fw]`

Removes every variable from the script variable store on each matching character. The internal store is not touched (use ClearAllInternal).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Vars:ClearAll[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Clear_Variables`

### `ClearAllInternal`

`OgreBotAPI.Vars:ClearAllInternal[fw]`

Removes every variable from the internal variable store on each matching character. The store Get and Set use is not touched.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Vars:ClearAllInternal[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Clear_InternalVariables`

### `ClearInternal`

`OgreBotAPI.Vars:ClearInternal[fw, name]`

Removes the variable name from the internal variable store on each matching character, so InternalExists then reads FALSE. Nothing happens when name is blank or the variable is missing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `name` | string |  | The internal variable name to remove, case-sensitive. |

```text
OgreBotAPI.Vars:ClearInternal[${Me.Name},LastZone]
```

*Was (OldBot):* `OgreBotAPI:Clear_InternalVariable`

### `Set`

`OgreBotAPI.Vars:Set[fw, name, value]`

Stores value under name in the script variable store on each matching character, replacing any earlier value; a blank value is stored as an empty string. Nothing happens when name is blank, and a successful set prints nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `name` | string |  | The variable name; case does not matter. Blank does nothing. |
| `value` | string |  | The text to store. Blank stores an empty value. |

```text
OgreBotAPI.Vars:Set[igw:${Me.Name},PullCount,3]
```

*Was (OldBot):* `OgreBotAPI:Set_Variable`

### `SetInternal`

`OgreBotAPI.Vars:SetInternal[fw, name, value]`

Stores value under name in the internal variable store on each matching character, replacing any earlier value. Nothing happens when name is blank, and the store Get and Set use is not touched.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `name` | string |  | The internal variable name; case does not matter. Blank does nothing. |
| `value` | string |  | The text to store. Blank stores an empty value. |

```text
OgreBotAPI.Vars:SetInternal[${Me.Name},LastZone,antonica]
```

*Was (OldBot):* `OgreBotAPI:Set_InternalVariable`
