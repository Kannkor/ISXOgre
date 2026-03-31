# Preferred Group & Raid Members

When you need a specific archetype to perform a task, OgreBot normally returns group members in whatever order they appear in the group list. The **Preferred** members solve this by returning members sorted by a built-in **utility priority** — ensuring the most supportive class is chosen first.

For example, if you need "a scout" to click a portal, `GetGroupIDPreferred` will pick a dirge over an assassin, since the dirge provides more group utility and losing their DPS matters less.

---

## How It Works

Each class has a hardcoded priority within its archetype. When you request the Nth preferred member of an archetype, OgreBot finds all matching members in your group (or raid), sorts them by this priority, and returns the one at position N.

### Priority Order by Archetype

| Priority | Scout | Fighter | Priest | Mage |
|----------|-------|---------|--------|------|
| 1 (most preferred) | Dirge | Paladin | Channeler | Coercer |
| 2 | Troubador | Shadowknight | Fury | Illusionist |
| 3 | Brigand | Monk | Warden | Conjuror |
| 4 | Swashbuckler | Bruiser | Inquisitor | Necromancer |
| 5 | Beastlord | Berserker | Templar | Warlock |
| 6 | Assassin | Guardian | Mystic | Wizard |
| 7 | Ranger | | Defiler | |

> **:memo: Note**
>
> The priority ordering is based on general group utility — classes that provide more buffs, debuffs, or support value are preferred over pure DPS classes. This ensures that when a class needs to be pulled away from their normal role (e.g., to click something or handle a mechanic), the least impactful choice is made.

---

## OgreBotAPI Members

### GetGroupIDPreferred

Returns the actor ID of the Nth preferred group member matching the given archetype.

```lavishscript
${OgreBotAPI.GetGroupIDPreferred[archetype, returnResult]}
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `archetype` | string | *(required)* | The archetype to search for: `scout`, `fighter`, `priest`, or `mage` |
| `returnResult` | int | 1 | Which result to return (1 = most preferred, 2 = second most preferred, etc.) |

**Returns:** `int64` — The actor ID of the matching group member, or `0` if not found.

**Examples:**

```lavishscript
;// Get the actor ID of the most utility-oriented scout in the group
variable int64 iScoutID
iScoutID:Set[${OgreBotAPI.GetGroupIDPreferred[scout,1]}]

;// Use it to make the preferred scout interact with something
if ${iScoutID} > 0
    OgreBotAPI:CastAbilityOnNPC["${Actor[id,${iScoutID}].Name}", "Interact", "ClickableObject"]

;// Get the 2nd most preferred fighter (useful when the main tank is busy)
variable int64 iFighterID
iFighterID:Set[${OgreBotAPI.GetGroupIDPreferred[fighter,2]}]
```

---

### GetGroupNamePreferred

Returns the character name of the Nth preferred group member matching the given archetype.

```lavishscript
${OgreBotAPI.GetGroupNamePreferred[archetype, returnResult]}
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `archetype` | string | *(required)* | The archetype to search for: `scout`, `fighter`, `priest`, or `mage` |
| `returnResult` | int | 1 | Which result to return (1 = most preferred, 2 = second most preferred, etc.) |

**Returns:** `string` — The character name of the matching group member, or `NULL` if not found.

**Examples:**

```lavishscript
;// Get the name of the most preferred scout to handle a mechanic
variable string sScoutName
sScoutName:Set[${OgreBotAPI.GetGroupNamePreferred[scout,1]}]

;// Send the preferred mage to a specific camp spot
variable string sMageName
sMageName:Set[${OgreBotAPI.GetGroupNamePreferred[mage,1]}]
if ${sMageName.NotEqual[NULL]}
    OgreBotAPI:ChangeCampSpotWho["${sMageName}", 100.5, 25.0, -50.3]

;// Assign the two most preferred priests to different tasks
variable string sPriest1
variable string sPriest2
sPriest1:Set[${OgreBotAPI.GetGroupNamePreferred[priest,1]}]
sPriest2:Set[${OgreBotAPI.GetGroupNamePreferred[priest,2]}]
```

---

### GetRaidIDPreferred

Returns the actor ID of the Nth preferred raid member matching the given archetype. If you are not in a raid, this automatically falls back to searching the group instead.

```lavishscript
${OgreBotAPI.GetRaidIDPreferred[archetype, returnResult]}
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `archetype` | string | *(required)* | The archetype to search for: `scout`, `fighter`, `priest`, or `mage` |
| `returnResult` | int | 1 | Which result to return (1 = most preferred, 2 = second most preferred, etc.) |

**Returns:** `int64` — The actor ID of the matching raid member, or `0` if not found.

**Examples:**

```lavishscript
;// Get the most preferred scout across the entire raid
variable int64 iRaidScoutID
iRaidScoutID:Set[${OgreBotAPI.GetRaidIDPreferred[scout,1]}]

;// Works in both raid and group contexts — falls back to group if not in a raid
variable int64 iPriestID
iPriestID:Set[${OgreBotAPI.GetRaidIDPreferred[priest,1]}]
```

---

### GetRaidNamePreferred

Returns the character name of the Nth preferred raid member matching the given archetype. If you are not in a raid, this automatically falls back to searching the group instead.

```lavishscript
${OgreBotAPI.GetRaidNamePreferred[archetype, returnResult]}
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `archetype` | string | *(required)* | The archetype to search for: `scout`, `fighter`, `priest`, or `mage` |
| `returnResult` | int | 1 | Which result to return (1 = most preferred, 2 = second most preferred, etc.) |

**Returns:** `string` — The character name of the matching raid member, or `NULL` if not found.

**Examples:**

```lavishscript
;// Get the name of the most preferred fighter in the raid for a mechanic assignment
variable string sFighterName
sFighterName:Set[${OgreBotAPI.GetRaidNamePreferred[fighter,1]}]

;// Loop through the top 3 preferred scouts in the raid
variable int iCounter
variable string sName
for ( iCounter:Set[1] ; ${iCounter} <= 3 ; iCounter:Inc )
{
    sName:Set[${OgreBotAPI.GetRaidNamePreferred[scout,${iCounter}]}]
    if ${sName.NotEqual[NULL]}
        echo Preferred scout ${iCounter}: ${sName}
}
```

---

## Comparison with Existing Members

| Use Case | Existing (unordered) | Preferred (utility-sorted) |
|----------|---------------------|---------------------------|
| Get a scout's actor ID from group | `${GetInfoOb.GetGroupIDBy_[scout,archetype,1]}` | `${OgreBotAPI.GetGroupIDPreferred[scout,1]}` |
| Get a priest's name from group | `${GetInfoOb.GetGroupNameBy_[priest,archetype,1]}` | `${OgreBotAPI.GetGroupNamePreferred[priest,1]}` |
| Get a fighter's actor ID from raid | `${GetInfoOb.GetRaidIDBy_[fighter,archetype,1]}` | `${OgreBotAPI.GetRaidIDPreferred[fighter,1]}` |
| Get a mage's name from raid | `${GetInfoOb.GetRaidNameBy_[mage,archetype,1]}` | `${OgreBotAPI.GetRaidNamePreferred[mage,1]}` |

> **:bulb: Tip**
>
> The existing `GetGroupIDBy_` and `GetRaidIDBy_` members are unchanged and still available. Use the Preferred versions when you want the most utility-oriented class chosen first. Use the existing versions when the order doesn't matter or when you need to search by criteria other than archetype (e.g., by specific class, role, or parent class).

---

## Related Documentation

- [OgreBotAPI Reference](ogrebot-api.md) — Full reference for all OgreBotAPI methods and members

<!-- Source: OgreBotDev.iss - GetGroupIDPreferred_, GetGroupNamePreferred_, GetRaidIDPreferred_, GetRaidNamePreferred_ members on Object_OgreBotAPI and GetInfoObject -->
