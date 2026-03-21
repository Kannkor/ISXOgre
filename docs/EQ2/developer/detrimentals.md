# Detrimentals System

ISXOgre provides a built-in detrimental monitoring system that caches your current detrimentals, fires events when they change, and offers TLO access for querying detrimental data — including full JSON output. You can also query detrimentals on other actors (mobs, NPCs, other players) via live lookups.

---

## Events

Three events fire automatically when **your** detrimentals change (self only — events do not fire for other actors):

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

## Named Parameters

Both `DetrimentalInfo` and `DetrimentalInfo_JSON` support named parameters after the required `mainIconID` and `backdropID`. Each flag is a separate comma-separated parameter.

| Flag | Value | Description |
|------|-------|-------------|
| `-actorID` | Actor ID (int64) | Query effects on another actor instead of self. Pass `0` or omit for self. |
| `-maxEffects` | Count (int) | Maximum number of effects to scan. Default: all for self, 7 for other actors. |
| `-ExtraFields` | *(no value)* | _(JSON only)_ Include extended fields from the game server. |

---

## TLO Members

### DetrimentalInfo

Query a specific detrimental field by MainIconID and BackDropIconID.

**Syntax:** `${ISXOgre.DetrimentalInfo[mainIconID, backdropID, returnField]}`

With named parameters:

`${ISXOgre.DetrimentalInfo[mainIconID, backdropID, -actorID, ${ActorID}, -maxEffects, 10, returnField]}`

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `mainIconID` | Yes | — | MainIconID of the detrimental |
| `backdropID` | Yes | — | BackDropIconID of the detrimental |
| `returnField` | No | `exists` | Field to return (see table below). Must be the **last** parameter. |

**Return Fields (int64):**

| Field | Description |
|-------|-------------|
| `exists` | Returns `1` if the detrimental is present, `0` if not |
| `id` | The detrimental's ID (int64) |
| `backdropiconid` | BackDropIconID |
| `mainiconid` | MainIconID |
| `currentincrements` | Current increment count |
| `duration` | Remaining duration (self only — returns 0 for other actors) |
| `maxduration` | Maximum duration (self only — returns 0 for other actors) |
| `cancel` | Cancels the detrimental on self. Returns nothing. |

**Return Fields (string):**

These fields are queried live from the game server via ToEffectInfo. On the first call, they may return empty — call again after a moment.

| Field | Description |
|-------|-------------|
| `Name` | Spell/effect name |
| `Description` | Full description text |
| `Type` | Effect type classification (e.g., "Detrimental") |
| `UsesRemaining` | Remaining uses (-1 = unlimited) |

**Return Type:** `int64` for numeric fields, `string` for extended fields

**Examples:**
```
; Check if a specific detrimental exists on you
if ${ISXOgre.DetrimentalInfo[193,315]}
{
    echo Detrimental exists! Duration: ${ISXOgre.DetrimentalInfo[193,315,duration]}
}

; Check if a detrimental exists on another actor
if ${ISXOgre.DetrimentalInfo[193,315,-actorID,${Target.ID},exists]}
{
    echo Target has the detrimental!
}

; Query with a custom max scan depth
echo ${ISXOgre.DetrimentalInfo[193,315,-actorID,${Target.ID},-maxEffects,15,currentincrements]}

; Get the name of a detrimental (live query, returns string)
echo ${ISXOgre.DetrimentalInfo[193,315,Name]}
```

---

### DetrimentalCancel

Cancel a detrimental on yourself by MainIconID and BackDropIconID.

**Syntax:** `ISXOgre:DetrimentalCancel[mainIconID, backdropID]`

**Example:**
```
; Cancel a specific detrimental
ISXOgre:DetrimentalCancel[193,315]
```

> **Note:** You can also cancel via `DetrimentalInfo` by passing `cancel` as the return field: `${ISXOgre.DetrimentalInfo[193,315,cancel]}`. This returns nothing but attempts the cancel.

---

### DetrimentalInfo_JSON

Get detrimental data as JSON.

**Syntax:** `${ISXOgre.DetrimentalInfo_JSON~}`

With parameters:

`${ISXOgre.DetrimentalInfo_JSON[mainIconID, backdropID, -actorID, ${ActorID}, -maxEffects, 10, -ExtraFields]~}`

All named parameters are optional.

#### Get All Detrimentals (No Parameters)

Returns all cached detrimentals on yourself as a JSON array.

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

#### Get a Specific Detrimental

Returns a single detrimental matching the given MainIconID and BackDropIconID.

```
variable jsonvalueref jvDetInfo1="${ISXOgre.DetrimentalInfo_JSON[193,315]~}"
echo Specific: ${jvDetInfo1.AsJSON}
echo Duration: ${jvDetInfo1.Get["Duration"]}
```

**Output:**
```
Specific: {"ID":99857,"BackDropIconID":315,"MainIconID":193,"CurrentIncrements":0,"Duration":34.0,"MaxDuration":36.0}
Duration: 34.000000
```

#### With Extended Fields

Pass `-ExtraFields` to include additional fields queried live from the game server.

```
variable jsonvalueref jvDetInfo2="${ISXOgre.DetrimentalInfo_JSON[193,315,-ExtraFields]~}"
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

#### Querying Another Actor

Use `-actorID` to query effects on a mob, NPC, or another player.

```
; Get all effects on target (scans up to 7 by default)
variable jsonvalueref jvTargetEffects="${ISXOgre.DetrimentalInfo_JSON[0,0,-actorID,${Target.ID}]~}"
echo Target effects: ${jvTargetEffects.AsJSON}

; Get a specific effect on target with extra fields
variable jsonvalueref jvTargetDet="${ISXOgre.DetrimentalInfo_JSON[193,315,-actorID,${Target.ID},-ExtraFields]~}"
echo ${jvTargetDet.Get["Name"]}

; Increase scan depth to check more effects
variable jsonvalueref jvDeep="${ISXOgre.DetrimentalInfo_JSON[0,0,-actorID,${Target.ID},-maxEffects,20]~}"
```

> **Note:** When querying other actors, `Duration` and `MaxDuration` will always be `0.0` because the game does not expose duration data for effects on other actors.

> **Note:** The default max effects scanned is 7 for other actors (to limit performance impact). Use `-maxEffects` to increase or decrease this limit. For self, all detrimentals are scanned by default.

**Extended Fields:**

| Field | JSON Type | Description |
|-------|-----------|-------------|
| `Name` | string | Spell/effect name |
| `Description` | string | Full description text |
| `Type` | string | Effect type classification |
| `UsesRemaining` | number (int) | Remaining uses (-1 = unlimited) |
| `NumEffectStrings` | number (int) | Count of effect strings |
| `EffectStrings` | array of strings | Individual effect descriptions |

> **Note:** The extended fields (`Name`, `Description`, `Type`, etc.) are queried live from the game server via ISXEQ2. On the first call, these fields may return empty because the server has not yet responded with the data. Simply call again after a moment and the fields will be populated.

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

> **Note:** If a value outside the 100-5000 range is provided, an error message will be displayed in the console and the scan time will not be changed.

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
| `Duration` | number (int) | Remaining duration in seconds (self only — 0 for other actors) |
| `MaxDuration` | number (int) | Maximum duration in seconds (self only — 0 for other actors) |

### Extended Fields (-ExtraFields Only)

These fields require a live server query and are only included when `-ExtraFields` is passed to `DetrimentalInfo_JSON`.

| Field | JSON Type | Description |
|-------|-----------|-------------|
| `Name` | string | Spell/effect name |
| `Description` | string | Full description text |
| `Type` | string | Effect type classification |
| `UsesRemaining` | number (int) | Remaining uses (-1 = unlimited) |
| `NumEffectStrings` | number (int) | Count of effect strings |
| `EffectStrings` | array of strings | Individual effect descriptions |

---

## Self vs Actor Queries

| Feature | Self (actorID=0) | Other Actors |
|---------|-------------------|--------------|
| Data source | Cached (updated every scan cycle) | Live query (on demand) |
| Events | Yes | No |
| Duration / MaxDuration | Available | Always 0 |
| Default max effects | All | 7 |
| Performance | Fast (cached) | Slower (live DataParse calls) |
