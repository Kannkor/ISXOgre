# Coding Practices

Coding conventions and preferences for writing LavishScript / ISXEQ2 / OgreBot code. Follow these when writing or modifying scripts to maintain consistency across the codebase.

These conventions are short but important -- consistent naming makes scripts easier to read, debug, and maintain, especially when working across many encounter modules.

---

## Variable Naming

### Parameter vs Non-Parameter Variables

**Parameters** always start with an underscore (`_`). Non-parameter variables never start with an underscore.

```lavishscript
; Parameters -- underscore prefix
function MyFunction(string _sMyString, int _iMyInt)

; Non-parameters -- no underscore
variable string sMyString
variable int iMyInt
```

!!! tip
    This convention makes it immediately clear whether a variable was passed in as a parameter or declared locally.

### Type Prefixes

Every variable should include a type prefix (or postfix for `point3f`) to indicate its type at a glance. This applies to both parameters and non-parameters.

| Type | Prefix | Parameter Example | Variable Example |
|------|--------|-------------------|------------------|
| `string` | `s` | `_sPlayerName` | `sPlayerName` |
| `int` | `i` | `_iCounter` | `iCounter` |
| `int64` | `i` | `_iActorID` | `iActorID` |
| `float` | `f` | `_fDistance` | `fDistance` |
| `bool` | `b` | `_bJousted` | `bJousted` |
| `point3f` | `loc` | `_locDestination` | `locRaidSpot` |

### Collection & Container Prefixes

For container types, combine the container prefix with the subtype prefix:

| Type | Prefix | Example |
|------|--------|---------|
| `collection:int` | `ci` | `ciPlayerCounts` |
| `collection:int64` | `ci` | `ciActorIDs` |
| `collection:string` | `cs` | `csPlayerNames` |
| `collection:float` | `cf` | `cfDistances` |
| `index:string` | `is` | `isPlayerNames` |
| `index:int` | `ii` | `iiValues` |
| `index:int64` | `ii` | `iiActorIDs` |
| `index:float` | `if` | `ifDistances` |
| `index:point3f` | `iloc` | `ilocRaidSpots` |
| `index:bool` | `ib` | `ibFlags` |
| `set` | `set` | `setNames` |

### Object Variables

For object type variables, shorten `Object_Name` to `Obj_Name_Description`:

| Object Type | Example Variable |
|-------------|-----------------|
| `Object_Timer` | `Obj_Timer_CureRequest` |
| `Object_IconIDs` | `Obj_IconIDs_Curse` |
| `Object_ZoneModuleInherit_GetAwayToCure` | `Obj_GATC_Spread` |

```lavishscript
variable Object_Timer Obj_Timer_CureRequest
variable Object_IconIDs Obj_IconIDs_GazeDebuff=316 231
```

---

## Range Checks

When checking if a number falls between two values, use `.Between[min,max]` (inclusive) instead of chained comparisons.

**Correct:**

```lavishscript
if ${fDuration.Between[1,10]}
{
    ; Duration is between 1 and 10 inclusive
}
```

!!! warning "Do NOT do this"
    ```lavishscript
    if ${fDuration} > 0 && ${fDuration} <= 10
    {
        ; Avoid chained comparisons for range checks
    }
    ```
    Use `.Between[min,max]` instead for cleaner, more readable code.

---

## Related Documentation

- [OgreBotAPI Reference](ogrebot-api.md) - Complete API method and member reference
- [Cross-Session Commands](cross-session-commands.md) - Command syntax and targeting
- [CampSpot System](camp-spot.md) - Positioning and movement reference
- [Encounter Coding](encounter-coding.md) - How to write encounter modules
