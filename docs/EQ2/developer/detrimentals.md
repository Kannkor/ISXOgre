# Detrimentals System

ISXOgre provides a built-in detrimental monitoring system that caches your current detrimentals, fires events when they change, and offers TLO access for querying detrimental data — including full JSON output.

---

## Events

Three events fire automatically when your detrimentals change:

| Event | When It Fires |
|-------|---------------|
| `OgreEvent_OnDetrimentalAdded` | A new detrimental appears on you |
| `OgreEvent_OnDetrimentalUpdated` | An existing detrimental's properties change (duration, increments, etc.) |
| `OgreEvent_OnDetrimentalRemoved` | A detrimental is removed from you |

Each event provides 6 arguments in this order:

| Arg # | Field | Type |
|-------|-------|------|
| 1 | ID | int64 |
| 2 | BackDropIconID | int |
| 3 | MainIconID | int |
| 4 | CurrentIncrements | int |
| 5 | Duration | int |
| 6 | MaxDuration | int |

### Event Example

```
function main()
{
    variable Object_EventTest Obj_EventTest

    while 1
    {
        waitframe
    }
}

objectdef Object_EventTest
{
    method Initialize()
    {
        Event["OgreEvent_OnDetrimentalAdded"]:AttachAtom["This:OgreEvent_OnDetrimentalAdded"]
        Event["OgreEvent_OnDetrimentalUpdated"]:AttachAtom["This:OgreEvent_OnDetrimentalUpdated"]
        Event["OgreEvent_OnDetrimentalRemoved"]:AttachAtom["This:OgreEvent_OnDetrimentalRemoved"]
    }

    method OgreEvent_OnDetrimentalAdded(int64 _ID, int _BackDropIconID, int _MainIconID, int _CurrentIncrements, int _Duration, int _MaxDuration)
    {
        echo ${Time}: Added - ID: ${_ID}, BackDropIconID: ${_BackDropIconID}, MainIconID: ${_MainIconID}, Duration: ${_Duration}/${_MaxDuration}
    }

    method OgreEvent_OnDetrimentalUpdated(int64 _ID, int _BackDropIconID, int _MainIconID, int _CurrentIncrements, int _Duration, int _MaxDuration)
    {
        echo ${Time}: Changed - ID: ${_ID}, BackDropIconID: ${_BackDropIconID}, MainIconID: ${_MainIconID}, Duration: ${_Duration}/${_MaxDuration}
    }

    method OgreEvent_OnDetrimentalRemoved(int64 _ID, int _BackDropIconID, int _MainIconID, int _CurrentIncrements, int _Duration, int _MaxDuration)
    {
        echo ${Time}: Removed - ID: ${_ID}, BackDropIconID: ${_BackDropIconID}, MainIconID: ${_MainIconID}
    }
}
```

**Output:**
```
20:44:56: Added - ID: 105054, BackDropIconID: 315, MainIconID: 186, Duration: 71/72
20:44:57: Changed - ID: 105054, BackDropIconID: 315, MainIconID: 186, Duration: 70/72
20:44:58: Changed - ID: 105054, BackDropIconID: 315, MainIconID: 186, Duration: 69/72
20:44:59: Changed - ID: 105054, BackDropIconID: 315, MainIconID: 186, Duration: 68/72
20:44:59: Added - ID: 105082, BackDropIconID: 315, MainIconID: 193, Duration: 35/36
20:45:00: Changed - ID: 105054, BackDropIconID: 315, MainIconID: 186, Duration: 67/72
20:45:00: Changed - ID: 105082, BackDropIconID: 315, MainIconID: 193, Duration: 34/36
20:45:01: Changed - ID: 105054, BackDropIconID: 315, MainIconID: 186, Duration: 66/72
20:45:01: Changed - ID: 105082, BackDropIconID: 315, MainIconID: 193, Duration: 33/36
<snipped>
20:45:33: Changed - ID: 105082, BackDropIconID: 315, MainIconID: 193, Duration: 1/36
20:45:33: Changed - ID: 105054, BackDropIconID: 315, MainIconID: 186, Duration: 34/72
20:45:34: Changed - ID: 105082, BackDropIconID: 315, MainIconID: 193, Duration: 0/36
20:45:34: Changed - ID: 105054, BackDropIconID: 315, MainIconID: 186, Duration: 33/72
20:45:35: Changed - ID: 105054, BackDropIconID: 315, MainIconID: 186, Duration: 32/72
20:45:35: Removed - ID: 105082, BackDropIconID: 315, MainIconID: 193
<snipped>
20:45:55: Removed - ID: 105054, BackDropIconID: 315, MainIconID: 186
```

---

## TLO Members

### DetrimentalInfo

Query a specific cached detrimental field by BackDropIconID and MainIconID.

**Syntax:** `${ISXOgre.DetrimentalInfo[backdropID, mainIconID, actorID, returnField]}`

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `backdropID` | Yes | — | BackDropIconID of the detrimental |
| `mainIconID` | Yes | — | MainIconID of the detrimental |
| `actorID` | No | `0` | Actor ID. Currently only supports `0` or `${Me.ID}` (both mean self). Does **not** work on other actors at this time. |
| `returnField` | No | `exists` | Field to return (see table below) |

**Return Fields:**

| Field | Description |
|-------|-------------|
| `exists` | Returns `1` if the detrimental is present, `0` if not |
| `id` | The detrimental's ID (int64) |
| `backdropiconid` | BackDropIconID |
| `mainiconid` | MainIconID |
| `currentincrements` | Current increment count |
| `duration` | Remaining duration |
| `maxduration` | Maximum duration |

**Return Type:** `int64`

**Example:**
```
; Check if a specific detrimental exists
if ${ISXOgre.DetrimentalInfo[315,193]}
{
    echo Detrimental exists! Duration: ${ISXOgre.DetrimentalInfo[315,193,0,duration]}
}
```

---

### DetrimentalInfo_JSON

Get detrimental data as JSON. Supports three modes depending on the parameters provided.

#### Mode 1: All Detrimentals (No Parameters)

Returns all cached detrimentals as a JSON array.

**Syntax:** `${ISXOgre.DetrimentalInfo_JSON~}`

**Example:**
```
variable jsonvalueref jvDetInfo="${ISXOgre.DetrimentalInfo_JSON~}"
echo ALL: ${jvDetInfo.AsJSON}

; Access a specific detrimental from the array (1-based index)
echo First det duration: ${jvDetInfo.Get[1].Get["Duration"]}
```

**Output:**
```
ALL: [{"ID":99834,"BackDropIconID":315,"MainIconID":186,"CurrentIncrements":0,"Duration":67.0,"MaxDuration":72.0},{"ID":99857,"BackDropIconID":315,"MainIconID":193,"CurrentIncrements":0,"Duration":34.0,"MaxDuration":36.0}]
First det duration: 67.000000
```

#### Mode 2: Specific Detrimental (Cached Fields Only)

Returns a single detrimental matching the given BackDropIconID and MainIconID.

**Syntax:** `${ISXOgre.DetrimentalInfo_JSON[backdropID, mainIconID]~}`

**Example:**
```
variable jsonvalueref jvDetInfo1="${ISXOgre.DetrimentalInfo_JSON[315,193]~}"
echo Specific: ${jvDetInfo1.AsJSON}
echo Duration: ${jvDetInfo1.Get["Duration"]}
```

**Output:**
```
Specific: {"ID":99857,"BackDropIconID":315,"MainIconID":193,"CurrentIncrements":0,"Duration":34.0,"MaxDuration":36.0}
Duration: 34.000000
```

#### Mode 3: Specific Detrimental with Extended Fields

Pass `TRUE` as the third parameter to include additional fields that are queried live from the game server.

**Syntax:** `${ISXOgre.DetrimentalInfo_JSON[backdropID, mainIconID, TRUE]~}`

**Example:**
```
variable jsonvalueref jvDetInfo2="${ISXOgre.DetrimentalInfo_JSON[315,193,TRUE]~}"
echo Extended: ${jvDetInfo2.AsJSON}
echo Name: ${jvDetInfo2.Get["Name"]}
echo Description: ${jvDetInfo2.Get["Description"]}
```

**Output:**
```
Extended: {"ID":99857,"BackDropIconID":315,"MainIconID":193,"CurrentIncrements":0,"Duration":29.0,"MaxDuration":36.0,"Name":"Deny VII","Description":"An impairment that decreases the target's strength and\nintelligence.","Type":"Detrimental","UsesRemaining":-1,"NumEffectStrings":0,"EffectStrings":[]}
Name: Deny VII
Description: An impairment that decreases the target's strength and intelligence.
```

**Extended Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `Name` | string | Name of the spell/effect |
| `Description` | string | Full description text |
| `Type` | string | Effect type (e.g., "Detrimental") |
| `UsesRemaining` | int | Uses remaining (-1 if unlimited) |
| `NumEffectStrings` | int | Number of effect strings |
| `EffectStrings` | array | Array of effect description strings |

> **:warning: Warning**
>
> The extended fields (`Name`, `Description`, `Type`, etc.) are queried live from the game server via ISXEQ2. On the first call, these fields may return empty because the server has not yet responded with the data. Simply call again after a moment and the fields will be populated.

---

## Methods

### DetrimentalCacheClear

Clears the internal detrimental cache. The cache will be rebuilt on the next scan cycle.

**Syntax:** `ISXOgre:DetrimentalCacheClear`

---

### Set_DetrimentalScanTime

Change how often detrimentals are scanned. Valid range is 100 to 5000 milliseconds.

**Syntax:** `ISXOgre:Set_DetrimentalScanTime[milliseconds]`

**Default:** `500` (half a second)

**Example:**
```
; Scan every 250ms for faster detection
ISXOgre:Set_DetrimentalScanTime[250]

; Scan every 1 second to reduce overhead
ISXOgre:Set_DetrimentalScanTime[1000]
```

> **:memo: Note**
>
> If a value outside the 100–5000 range is provided, an error message will be displayed in the console and the scan time will not be changed.

---

## JSON Field Reference

### Cached Fields (Always Available)

These fields are updated every scan cycle and are always present in JSON output.

| Field | JSON Type | Description |
|-------|-----------|-------------|
| `ID` | number (int64) | Unique detrimental ID |
| `BackDropIconID` | number (int) | Backdrop icon identifier |
| `MainIconID` | number (int) | Main icon identifier |
| `CurrentIncrements` | number (int) | Current increment count |
| `Duration` | number (int) | Remaining duration in seconds |
| `MaxDuration` | number (int) | Maximum duration in seconds |

### Extended Fields (TRUE Parameter Only)

These fields require a live server query and are only included when `TRUE` is passed as the third parameter to `DetrimentalInfo_JSON`.

| Field | JSON Type | Description |
|-------|-----------|-------------|
| `Name` | string | Spell/effect name |
| `Description` | string | Full description text |
| `Type` | string | Effect type classification |
| `UsesRemaining` | number (int) | Remaining uses (-1 = unlimited) |
| `NumEffectStrings` | number (int) | Count of effect strings |
| `EffectStrings` | array of strings | Individual effect descriptions |
