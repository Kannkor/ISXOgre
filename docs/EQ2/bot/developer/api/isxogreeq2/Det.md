# ISXOgreEQ2.Det

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Members

### `DetrimentalInfo`

`${ISXOgreEQ2.Det.DetrimentalInfo[mainIconID,backdropIconID,-actorID,-maxEffects,field]}`

One field of a detrimental effect matched by its icon pair: on you (no -actorID, or your own ID) it reads the bot's detrimental tracker, which refreshes about every 500 ms, and for any other actor it walks that actor's effect list live, the first 10 effects unless -maxEffects says otherwise. Numeric fields (exists, id, mainiconid, backdropiconid, currentincrements, duration, maxduration, iseffectinfoavailable) come back as a number - 0 when not found, duration in whole seconds, and always 0 for duration on another actor - while any other field name (Name, Description, Type...) reads the game's effect info, a server request, and the read is NULL out of the world or with fewer than two arguments.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `mainIconID` | int |  | the effect's MainIconID |
| `backdropIconID` | int |  | the effect's BackDropIconID |
| `-actorID` | switch | `0 (you)` | -actorID &lt;id>: read this actor's effects instead of yours |
| `-maxEffects` | switch | `10` | -maxEffects &lt;n>: how many of another actor's effects to walk; 0 walks them all; not used for you |
| `field` | string | `exists` | the field to return; the last word that is not a switch wins. A read changes nothing: ISXOgreEQ2.Det:DetrimentalCancel is the way to cancel |

**Returns:** int64 or string: exists is 1 or 0; id, icon ids, currentincrements, duration and maxduration are numbers (0 when not found); any other field is a string (empty when not found).

```text
echo ${ISXOgreEQ2.Det.DetrimentalInfo[176,313,-actorID,${Target.ID},currentincrements]}
```

### `DetrimentalInfo_JSON`

`${ISXOgreEQ2.Det.DetrimentalInfo_JSON[mainIconID,backdropIconID,-actorID,-maxEffects,-ExtraFields]}`

A detrimental effect as JSON (ID, BackDropIconID, MainIconID, CurrentIncrements, Duration, MaxDuration): with no icon pair (or 0,0) a JSON array of every detrimental on you (or of another actor's first effects with -actorID), and with an icon pair that one effect as an object, {} when not found. The switches are read in any position and the first two other arguments are the icon pair; Duration and MaxDuration are always 0 for another actor, and the read is NULL out of the world.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `mainIconID` | int | `0` | the effect's MainIconID; 0 with backdropIconID 0 lists every effect |
| `backdropIconID` | int | `0` | the effect's BackDropIconID; with fewer than two icon arguments there is no pair (0,0) |
| `-actorID` | switch | `0 (you)` | -actorID &lt;id>: read this actor's effects instead of yours |
| `-maxEffects` | switch | `10` | -maxEffects &lt;n>: how many of another actor's effects to walk; 0 walks them all; not used for you |
| `-ExtraFields` | switch | `off` | -ExtraFields: add Name, Description, Type, UsesRemaining, NumEffectStrings and EffectStrings to a matched effect (a server request); not applied to the whole list |

**Returns:** string: a JSON array (every effect) or a JSON object (one matched effect, {} when not found).

```text
echo ${ISXOgreEQ2.Det.DetrimentalInfo_JSON}
```

## Methods

### `DetrimentalCacheClear`

`ISXOgreEQ2.Det:DetrimentalCacheClear`

Empties the bot's detrimental tracker, so its next scan sees every detrimental still on you as new. That fires OgreEvent_OnDetrimentalAdded again for each of them and echoes a +det line for each.

```text
ISXOgreEQ2.Det:DetrimentalCacheClear
```

### `DetrimentalCancel`

`ISXOgreEQ2.Det:DetrimentalCancel[mainIconID,backdropIconID]`

Cancels the detrimental effect on you with this icon pair, immediately, and echoes a cancel line to the console when it finds it. It says nothing when no such effect is on you; OgreBotAPI.Cures:CancelDetrimental is the same cancel with a for-who and a not-found message.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `mainIconID` | int |  | the effect's MainIconID |
| `backdropIconID` | int |  | the effect's BackDropIconID |

```text
ISXOgreEQ2.Det:DetrimentalCancel[176,313]
```

### `Dump`

`ISXOgreEQ2.Det:Dump[mode,-noinfo]`

The `ogre dets` console dump: lists every detrimental on you from the tracker (dets, the default), your maintained spells and their targets (m), or your target's effects (target), one line each. By default it also reads each detrimental's Name and Description, a server request per effect, which -noinfo skips; out of the world it only prints a warning.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `mode` | string | `dets` | dets (or det, d), m (or maintained), target (or t); -h, -help or ? as the first word prints usage |
| `-noinfo` | switch | `off` | skip the Name and Description reads; -info turns them back on |

```text
ISXOgreEQ2.Det:Dump[dets,-noinfo]
```

### `Set_DetrimentalScanTime`

`ISXOgreEQ2.Det:Set_DetrimentalScanTime[ms]`

Sets how often, in milliseconds, the bot's detrimental tracker rescans your detrimentals (500 by default); every reader of the tracker sees the change. A value outside 100 to 5000 is refused with a console warning and the interval stays as it was, and the setting is not saved.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `ms` | int |  | the scan interval in milliseconds, 100 to 5000 |

```text
ISXOgreEQ2.Det:Set_DetrimentalScanTime[250]
```
