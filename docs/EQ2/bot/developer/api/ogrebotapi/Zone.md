# OgreBotAPI.Zone

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Members

### `CityRestrictions`

`${OgreBotAPI.Zone.CityRestrictions}`

TRUE in one of the bot's 17 city zones, such as The City of Freeport or Qeynos Province District, unless Allow City Casting is ticked. FALSE out of world.

**Returns:** bool: TRUE in a listed city with Allow City Casting unticked; FALSE otherwise or out of world.

```text
echo ${OgreBotAPI.Zone.CityRestrictions}
```

*Was (OldBot):* `OgreBotAPI.CityRestrictions`

### `CleanName`

`${OgreBotAPI.Zone.CleanName[name]}`

The same cleaned name as Name, made safe for file and setting names: spaces become underscores and the characters , [ ] : ' and ` are removed. Reads "" out of world when no name is passed.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | text | `${Zone.Name}` | a zone name to clean; blank means the zone you are in |

**Returns:** string: the cleaned zone name with underscores for spaces; "" out of world when no name is given.

```text
echo ${OgreBotAPI.Zone.CleanName}
```

*Was (OldBot):* `OgreBotAPI.CleanZoneName`, `Ogre_Instance_Controller.CleanZoneName`

### `InGuildHall`

`${OgreBotAPI.Zone.InGuildHall}`

TRUE when the zone's short name contains guildhall, except the Island of Mara Estate (guildhall_mara). FALSE out of world.

**Returns:** bool: TRUE in a guild hall; FALSE elsewhere or out of world.

```text
echo ${OgreBotAPI.Zone.InGuildHall}
```

*Was (OldBot):* `GetInfoOb.InGuildHallZone`, `Obj_OgreUtilities.InGuildHallZone`, `OgreBotAPI.InGuildHallZone`

### `InHouse`

`${OgreBotAPI.Zone.InHouse}`

TRUE when you look to be inside a house: not in a guild hall, and a Magic Door to the Guild Hall or a market bulletin board is in the zone. It is a guess from those two objects; FALSE out of world.

**Returns:** bool: TRUE when either object is in the zone and it is not a guild hall; FALSE otherwise or out of world.

```text
echo ${OgreBotAPI.Zone.InHouse}
```

*Was (OldBot):* `GetInfoOb.InHouseZone`, `OgreBotAPI.InHouseZone`

### `InHouseAccess`

`${OgreBotAPI.Zone.InHouseAccess}`

TRUE in one of the eight zones the bot treats as house-access zones: Antonica, Halas, the two Qeynos zones, Timorous Deep, Greater Faydark, Neriak and Freeport. This is the outdoor zone, not the house itself; FALSE out of world.

**Returns:** bool: TRUE when the zone's short name is antonica, halas, qeynos_combined01, qeynos_combined02, exp04_rgn_timorous_deep, exp03_rgn_greater_faydark, neriak or freeport_combined; FALSE otherwise or out of world.

```text
echo ${OgreBotAPI.Zone.InHouseAccess}
```

*Was (OldBot):* `GetInfoOb.InHouseAccessZone`, `OgreBotAPI.InHouseAccessZone`

### `InInstance`

`${OgreBotAPI.Zone.InInstance}`

TRUE when the zone name contains a [ (instances are named like that, such as [Heroic] or [Solo]) and you are not in a guild hall. FALSE out of world.

**Returns:** bool: TRUE in an instance; FALSE in an open zone, a guild hall, or out of world.

```text
echo ${OgreBotAPI.Zone.InInstance}
```

*Was (OldBot):* `GetInfoOb.InAInstance`, `OgreBotAPI.InInstance`

### `Name`

`${OgreBotAPI.Zone.Name[name]}`

The zone name with colour codes and the trailing instance number removed. Every trailing digit and space is stripped, so a name that really ends in a number loses it; "" out of world when no name is passed.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | text | `${Zone.Name}` | a zone name to clean; blank means the zone you are in |

**Returns:** string: the cleaned zone name; "" out of world when no name is given.

```text
echo ${OgreBotAPI.Zone.Name}
```

*Was (OldBot):* `OgreBotAPI.ZoneName`

### `ResetReady`

`${OgreBotAPI.Zone.ResetReady}`

TRUE once the Zone Reuse table has been read at least once and no re-read is asked for or running. Wait for it after ResetUpdateInfo before reading ResetZoneData.

**Returns:** bool: TRUE when the table is in and not being re-read; FALSE before the first read or while a re-read is pending.

```text
echo ${OgreBotAPI.Zone.ResetReady}
```

*Was (OldBot):* `OgreBotAPI.ZoneReset_IsReady`

### `ResetUpdating`

`${OgreBotAPI.Zone.ResetUpdating}`

TRUE while a Zone Reuse re-read is asked for or running.

**Returns:** bool: TRUE while a re-read is pending or running; FALSE otherwise.

```text
echo ${OgreBotAPI.Zone.ResetUpdating}
```

*Was (OldBot):* `OgreBotAPI.ZoneReset_IsUpdating`

### `ResetZoneData`

`${OgreBotAPI.Zone.ResetZoneData[zone,field]}`

One zone's entry from the Zone Reuse window, as last read by ResetUpdateInfo. A zone that is not in the table reads FALSE, and an unknown field prints a console line and reads FALSE.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `zone` | text |  | the zone name exactly as the Zone Reuse window shows it, any case |
| `field` | text |  | blank reads TRUE when the zone has an entry; otherwise ZoneName, IsSet (TRUE when its timer state is known), Resettable, TimeLeft (seconds) or TextTimeLeft |

**Returns:** bool, int64 or string by field: TRUE/FALSE for blank, IsSet and Resettable; seconds for TimeLeft; text for ZoneName and TextTimeLeft. FALSE when the zone is not in the table.

```text
echo ${OgreBotAPI.Zone.ResetZoneData["${OgreBotAPI.Zone.Name}",Resettable]}
```

*Was (OldBot):* `OgreBotAPI.ZoneReset_Get_ZoneData`

## Methods

### `ChampionsResetter`

`OgreBotAPI.Zone:ChampionsResetter[fw, zone]`

Resets one zone with your Champion's Zone Lockout Reset item: examines it, then picks the zone in the window it opens. Prints a console line when the item is not in your bags, is on cooldown, or does not list the zone.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `zone` | text |  | the zone name as the item's window lists it |

```text
OgreBotAPI.Zone:ChampionsResetter[${Me.Name},"${OgreBotAPI.Zone.Name}"]
```

*Was (OldBot):* `OgreBotAPI:Champions_Zone_Resetter`

### `ChangeZoneTo`

`OgreBotAPI.Zone:ChangeZoneTo[fw, toWho]`

When the group member is in another instance of your zone, sends the game's /zone_to_group_member_zone command for them on this character. A name that is not in your group or a different zone prints a console line; nothing happens when they share your instance.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `toWho` | character name |  | the group member whose instance to join |

```text
OgreBotAPI.Zone:ChangeZoneTo[${Me.Name},${Group[1].Name}]
```

*Was (OldBot):* `OgreBotAPI:ChangeZoneTo`, `Obj_OgreIH:ChangeZoneTo`

### `ForceReset`

`OgreBotAPI.Zone:ForceReset[fw, zone]`

Presses Force Reset in the Zone Reuse window for one named zone, which uses up one of your limited force-reset charges. A blank zone prints a console line and does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `zone` | text |  | the zone name as the Zone Reuse window shows it |

```text
OgreBotAPI.Zone:ForceReset[${Me.Name},"${OgreBotAPI.Zone.Name}"]
```

### `ResetAll`

`OgreBotAPI.Zone:ResetAll[fw, allowRaid=FALSE]`

Runs the game's reset_all_zone_timers command on each matching character. In a raid it does nothing unless allowRaid is TRUE.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `allowRaid` | bool | `FALSE` | TRUE to reset even while in a raid |

```text
OgreBotAPI.Zone:ResetAll[igw:${Me.Name},FALSE]
```

*Was (OldBot):* `OgreBotAPI:ZoneResetAll`

### `ResetUpdateInfo`

`OgreBotAPI.Zone:ResetUpdateInfo[fw]`

Asks the bot to re-read the Zone Reuse window, which it opens and closes to do so. Asking again while a re-read is pending does nothing extra; ResetUpdating and ResetReady follow it.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.Zone:ResetUpdateInfo[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:ToggleZoneReuse`, `Obj_OgreUtilities:ZoneReset_PopulateInternalMemory`, `OgreBotAPI:ZoneReset_UpdateInfo`

### `ResetZone`

`OgreBotAPI.Zone:ResetZone[fw, zone]`

Resets the lockout timer for one zone on each matching character, opening the Zone Reuse window first when the bot has no zone data yet. A blank zone prints a console line and does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `zone` | text |  | the zone name as the Zone Reuse window shows it |

```text
OgreBotAPI.Zone:ResetZone[igw:${Me.Name},"${OgreBotAPI.Zone.Name}"]
```

*Was (OldBot):* `OgreBotAPI:ResetZone`

### `SelectVersion`

`OgreBotAPI.Zone:SelectVersion[fw]`

Clicks the OK button of the game's select zone version window on each matching character. When the window is not open it prints a console line instead.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.Zone:SelectVersion[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Select_Zone_Version`

### `ShareQuestsForZone`

`OgreBotAPI.Zone:ShareQuestsForZone[fw, zone=""]`

Shares, one at a time after the group has gathered, the Hot Zones missions in your journal that belong to this zone. It works only while you are in that zone, and with for-who all only the group leader shares.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `zone` | text | `""` | the zone the missions are for; blank means the zone you are in. Another zone prints a console line and shares nothing. |

```text
OgreBotAPI.Zone:ShareQuestsForZone[all]
```

*Was (OldBot):* `OgreBotAPI:ShareQuestsForZone`, `OgreBotAPI:CheckToShareQuest`

### `SpecialZoneSpecific`

`OgreBotAPI.Zone:SpecialZoneSpecific[fw]`

The Special button: in zones with a known puzzle it clicks the puzzle object in reach (a clock, door, brazier, rope, zip line or orb) or hands the press to that zone's fight. Anywhere else it double-clicks the nearest interactable object of a special type.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.Zone:SpecialZoneSpecific[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:SpecialZoneSpecific`, `call Obj_OgreIH.ZoneSpecialwait`, `call Object_Instance_Inherit.ZoneSpecialwait`

### `Zone`

`OgreBotAPI.Zone:Zone[fw]`

Double-clicks the nearest zone exit on each matching character: an object named with exit, else with zone_, else the nearest door, else a NoKill NPC within 30 meters. Does nothing in a guild hall.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.Zone:Zone[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Zone`
