# OgreBotAPI.CampSpot

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Members

### `Active`

`${OgreBotAPI.CampSpot.Active}`

The camp spot slot the leash is using now, 1 to 8. It starts at 1 and only SetActive or ResetAll change it.

**Returns:** int - the active slot number (1 to 8).

```text
echo ${OgreBotAPI.CampSpot.Active}
```

### `AnchorLoc`

`${OgreBotAPI.CampSpot.AnchorLoc}`

The active slot's own spot as one "x,y,z" text without the relative layer, or "" when the active slot has no spot. Use it as the fixed reference when a relative layer may be in play; EffectiveLoc is where the character will actually go.

**Returns:** string - "x,y,z", or "" when there is no spot.

```text
echo ${OgreBotAPI.CampSpot.AnchorLoc}
```

*Was (OldBot):* `Ogre_CampSpot.AbsoluteCampSpotLoc`, `Ogre_CampSpot.Get_AbsoluteCampSpot`

### `AnchorX`

`${OgreBotAPI.CampSpot.AnchorX}`

The X coordinate of the active slot's own spot, without the relative layer. It reads 0 when the active slot has no spot.

**Returns:** float - the X coordinate, or 0 when there is no spot.

```text
echo ${OgreBotAPI.CampSpot.AnchorX}
```

### `AnchorY`

`${OgreBotAPI.CampSpot.AnchorY}`

The Y coordinate of the active slot's own spot, without the relative layer. It reads 0 when the active slot has no spot.

**Returns:** float - the Y coordinate, or 0 when there is no spot.

```text
echo ${OgreBotAPI.CampSpot.AnchorY}
```

### `AnchorZ`

`${OgreBotAPI.CampSpot.AnchorZ}`

The Z coordinate of the active slot's own spot, without the relative layer. It reads 0 when the active slot has no spot.

**Returns:** float - the Z coordinate, or 0 when there is no spot.

```text
echo ${OgreBotAPI.CampSpot.AnchorZ}
```

### `AtCampSpot`

`${OgreBotAPI.CampSpot.AtCampSpot}`

TRUE when this character is closer to the effective spot than HowClose, measured in 2D unless Use3D is on. It reads FALSE when the active slot has no spot, and it does not check the zone.

**Returns:** bool - TRUE if at the camp spot.

```text
echo ${OgreBotAPI.CampSpot.AtCampSpot}
```

*Was (OldBot):* `Ogre_CampSpot.AtCampSpot`

### `DistanceTo`

`${OgreBotAPI.CampSpot.DistanceTo}`

The distance from this character to the effective spot, measured the way the leash measures it: on the ground plane (X and Z) unless Use3D is on. It reads -1 when the active slot has no spot.

**Returns:** float - the distance, or -1 when there is no spot.

```text
echo ${OgreBotAPI.CampSpot.DistanceTo}
```

*Was (OldBot):* `Ogre_CampSpot.DistanceFromCampSpot`

### `EffectiveLoc`

`${OgreBotAPI.CampSpot.EffectiveLoc}`

Where the leash will take this character: the active slot's spot with the relative layer applied, as one "x,y,z" text with two decimals. It is "" when the active slot has no spot.

**Returns:** string - "x,y,z", or "" when there is no spot.

```text
echo ${OgreBotAPI.CampSpot.EffectiveLoc}
```

*Was (OldBot):* `Ogre_CampSpot.Get_CampSpot`, `Ogre_CampSpot.Get_RelativeCampSpot`, `Ogre_CampSpot.RelativeCampSpotLoc`

### `EffectiveX`

`${OgreBotAPI.CampSpot.EffectiveX}`

The X coordinate of the spot the leash will take this character to, with the relative layer applied. It reads 0 when the active slot has no spot, so check HasSpot first.

**Returns:** float - the X coordinate, or 0 when there is no spot.

```text
echo ${OgreBotAPI.CampSpot.EffectiveX}
```

*Was (OldBot):* `Ogre_CampSpot.Get_X`

### `EffectiveY`

`${OgreBotAPI.CampSpot.EffectiveY}`

The Y coordinate of the spot the leash will take this character to, with the relative layer applied. It reads 0 when the active slot has no spot, so check HasSpot first.

**Returns:** float - the Y coordinate, or 0 when there is no spot.

```text
echo ${OgreBotAPI.CampSpot.EffectiveY}
```

*Was (OldBot):* `Ogre_CampSpot.Get_Y`

### `EffectiveZ`

`${OgreBotAPI.CampSpot.EffectiveZ}`

The Z coordinate of the spot the leash will take this character to, with the relative layer applied. It reads 0 when the active slot has no spot, so check HasSpot first.

**Returns:** float - the Z coordinate, or 0 when there is no spot.

```text
echo ${OgreBotAPI.CampSpot.EffectiveZ}
```

*Was (OldBot):* `Ogre_CampSpot.Get_Z`

### `Enabled`

`${OgreBotAPI.CampSpot.Enabled}`

TRUE while the leash is turned on. It starts TRUE and only the Enable and Disable methods change it; the leash still needs a spot in the current zone to move anyone.

**Returns:** bool - TRUE if the leash is on.

```text
echo ${OgreBotAPI.CampSpot.Enabled}
```

### `HasSpot`

`${OgreBotAPI.CampSpot.HasSpot}`

TRUE when the active slot holds a camp spot. It does not check the zone or whether the leash is on.

**Returns:** bool - TRUE if the active slot has a spot.

```text
echo ${OgreBotAPI.CampSpot.HasSpot}
```

### `HowClose`

`${OgreBotAPI.CampSpot.HowClose}`

The arrival radius of the active slot: inside this distance the character counts as at the camp spot and the leash stops. A slot that was never set reads 1.

**Returns:** float - the arrival radius.

```text
echo ${OgreBotAPI.CampSpot.HowClose}
```

*Was (OldBot):* `Ogre_CampSpot.Get_HowClose`, `Ogre_CampSpot.HowClose`

### `HowFar`

`${OgreBotAPI.CampSpot.HowFar}`

The leash radius of the active slot: the leash walks the character back only from farther than HowClose and no farther than HowFar, and beyond HowFar it does not chase. A slot that was never set reads 125.

**Returns:** float - the leash radius.

```text
echo ${OgreBotAPI.CampSpot.HowFar}
```

*Was (OldBot):* `Ogre_CampSpot.Get_HowFar`, `Ogre_CampSpot.HowFar`

### `Leashing`

`${OgreBotAPI.CampSpot.Leashing}`

TRUE while the leash is walking this character back toward the camp spot right now. It goes FALSE once the character arrives, is paused, dead, zoning, or held by a movement block.

**Returns:** bool - TRUE while the leash is moving the character.

```text
echo ${OgreBotAPI.CampSpot.Leashing}
```

*Was (OldBot):* `Ogre_CampSpot.ValidStayAtCampSpotOptions`

### `MaxSlots`

`${OgreBotAPI.CampSpot.MaxSlots}`

The number of camp spot slots there are. It is always 8.

**Returns:** int - 8.

```text
echo ${OgreBotAPI.CampSpot.MaxSlots}
```

### `OutsideLeash`

`${OgreBotAPI.CampSpot.OutsideLeash}`

TRUE when this character is farther from the effective spot than HowFar, which is where the leash stops trying to walk back. FALSE when the active slot has no spot.

**Returns:** bool - TRUE if beyond the leash radius.

```text
echo ${OgreBotAPI.CampSpot.OutsideLeash}
```

### `RelativeActive`

`${OgreBotAPI.CampSpot.RelativeActive}`

TRUE when the relative layer changes where the character goes: the effective spot differs from the anchor, or the offset is not 0,0,0. UsingRelativeBy answers a different question (which mode the layer is in).

**Returns:** bool - TRUE if a relative layer is in effect.

```text
echo ${OgreBotAPI.CampSpot.RelativeActive}
```

*Was (OldBot):* `Ogre_CampSpot.UsingRelative`

### `RelativeLoc`

`${OgreBotAPI.CampSpot.RelativeLoc}`

The relative layer as one "x,y,z" text: the offset in offset mode, or the fixed destination after SetRelativeLoc. It reads "0.00,0.00,0.00" when the layer is clear.

**Returns:** string - "x,y,z".

```text
echo ${OgreBotAPI.CampSpot.RelativeLoc}
```

*Was (OldBot):* `Ogre_CampSpot.Get_RelativeMods`, `Ogre_CampSpot.RelativeLoc`

### `RelativeX`

`${OgreBotAPI.CampSpot.RelativeX}`

The X part of the relative layer: an offset when UsingRelativeBy is TRUE, or the fixed destination's X after SetRelativeLoc. It reads 0 when the layer is clear.

**Returns:** float - the X value of the relative layer.

```text
echo ${OgreBotAPI.CampSpot.RelativeX}
```

### `RelativeY`

`${OgreBotAPI.CampSpot.RelativeY}`

The Y part of the relative layer: an offset when UsingRelativeBy is TRUE, or the fixed destination's Y after SetRelativeLoc. It reads 0 when the layer is clear.

**Returns:** float - the Y value of the relative layer.

```text
echo ${OgreBotAPI.CampSpot.RelativeY}
```

### `RelativeZ`

`${OgreBotAPI.CampSpot.RelativeZ}`

The Z part of the relative layer: an offset when UsingRelativeBy is TRUE, or the fixed destination's Z after SetRelativeLoc. It reads 0 when the layer is clear.

**Returns:** float - the Z value of the relative layer.

```text
echo ${OgreBotAPI.CampSpot.RelativeZ}
```

### `SlotCount`

`${OgreBotAPI.CampSpot.SlotCount}`

How many of the 8 camp spot slots currently hold a spot. Slots that are not active still count.

**Returns:** int - the number of slots with a spot (0 to 8).

```text
echo ${OgreBotAPI.CampSpot.SlotCount}
```

### `SlotHasSpot`

`${OgreBotAPI.CampSpot.SlotHasSpot[n]}`

TRUE when slot n holds a camp spot, whether or not it is the active slot. A missing n or one outside 1 to 8 reads FALSE.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `n` | int |  | The slot number to check, 1 to 8. |

**Returns:** bool - TRUE if slot n has a spot.

```text
echo ${OgreBotAPI.CampSpot.SlotHasSpot[2]}
```

### `Use3D`

`${OgreBotAPI.CampSpot.Use3D}`

TRUE when the active slot measures distance in 3D. FALSE (the default) measures on the ground plane only (X and Z), ignoring height.

**Returns:** bool - TRUE for 3D distances.

```text
echo ${OgreBotAPI.CampSpot.Use3D}
```

*Was (OldBot):* `Ogre_CampSpot.Get_Use3D`, `Ogre_CampSpot.bUse3D`

### `UsingRelativeBy`

`${OgreBotAPI.CampSpot.UsingRelativeBy}`

TRUE when the relative layer is an offset added to the spot (the default, and still TRUE with a 0,0,0 offset); FALSE after SetRelativeLoc, when it is a fixed destination instead. To ask whether the layer changes anything, read RelativeActive.

**Returns:** bool - TRUE in offset mode.

```text
echo ${OgreBotAPI.CampSpot.UsingRelativeBy}
```

*Was (OldBot):* `Ogre_CampSpot.UsingRelativeBy`

### `ValidOptions`

`${OgreBotAPI.CampSpot.ValidOptions}`

TRUE when everything ValidOptionsCommon checks is true and this character is in the zone the active spot was set in. It does not look at Enabled or at how far away the character is, and reads the two options when asked, so a change made while the leash is paused counts at once.

**Returns:** bool - TRUE if the camp spot options are in force here.

```text
echo ${OgreBotAPI.CampSpot.ValidOptions}
```

*Was (OldBot):* `Ogre_CampSpot.ValidCampSpotOptions`

### `ValidOptionsCommon`

`${OgreBotAPI.CampSpot.ValidOptionsCommon}`

TRUE when the Allow Camp Spot and Dynamic Camp Spot options are both on, no movement block or leash hold is in, and the active slot has a spot. It does not check the zone (ValidOptions does), and reads the two options when asked, so a change made while the leash is paused counts at once.

**Returns:** bool - TRUE if the camp spot options allow the leash.

```text
echo ${OgreBotAPI.CampSpot.ValidOptionsCommon}
```

*Was (OldBot):* `Ogre_CampSpot.ValidCampSpotOptionsCommon`

### `Zone`

`${OgreBotAPI.CampSpot.Zone}`

The short name of the zone the active slot's spot was set in; the leash only acts in that zone. It is "" when the slot was never set with SetHere, SetSlotHere or SetFormation, or after ClearAll.

**Returns:** string - the zone short name, or "".

```text
echo ${OgreBotAPI.CampSpot.Zone}
```

*Was (OldBot):* `Ogre_CampSpot.CSZoneName`

## Methods

### `ClearAll`

`OgreBotAPI.CampSpot:ClearAll[fw]`

Clears the spot and zone in all 8 slots and clears the relative layer, and also drops any hold on the leash (for example from a joust). Each slot keeps its radii and the active slot stays the same; ResetAll resets those too.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.CampSpot:ClearAll[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:ClearAll`, `Ogre_CampSpot:ClearAll`

### `ClearCampSpot`

`OgreBotAPI.CampSpot:ClearCampSpot[fw]`

Clears the spot in the active slot, so the leash stops. The slot keeps its zone and radii, the relative layer is kept, and the other slots are not touched.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.CampSpot:ClearCampSpot[igw:${Me.Name}]
```

*Was (OldBot):* `Ogre_CampSpot:ClearCampSpot`

### `ClearRelative`

`OgreBotAPI.CampSpot:ClearRelative[fw]`

Clears the relative layer back to a 0,0,0 offset, so the leash goes to the active slot's own spot again. The spots are not touched, and it works even when OgreBot is closed.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.CampSpot:ClearRelative[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:ClearRCS`, `Ogre_CampSpot:ClearRelative`

### `Disable`

`OgreBotAPI.CampSpot:Disable[fw]`

Turns the leash off, for every slot. The spots are kept, so Enable picks up where it left off.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.CampSpot:Disable[igw:${Me.Name}]
```

### `Enable`

`OgreBotAPI.CampSpot:Enable[fw]`

Turns the leash on, for every slot. The leash is on by default; it still needs a spot in the current zone to move anyone.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.CampSpot:Enable[igw:${Me.Name}]
```

### `NudgeBy`

`OgreBotAPI.CampSpot:NudgeBy[fw, dx=0, dy=0, dz=0]`

Adds dx, dy and dz to the active slot's camp spot, keeping its zone and radii; a slot with no spot stays as it is, with one line. Nothing is set, with a line on the console, when OgreBot is not open (unless Movement:UseWithoutOgreBot is on).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `dx` | float | `0` | Amount added to X. |
| `dy` | float | `0` | Amount added to Y. |
| `dz` | float | `0` | Amount added to Z. |

```text
OgreBotAPI.CampSpot:NudgeBy[igw:${Me.Name},5,0,0]
```

*Was (OldBot):* `Ogre_CampSpot:Set_ChangeCampSpotBy`

### `Release`

`OgreBotAPI.CampSpot:Release[fw]`

Lets the character go: clears every camp spot (as ClearAll), stops a running jump route, clears the manual target overrides, the reasons that hold auto target, the reasons that stop offensive and defensive abilities, the no-offensive list, the threat ignore list, the no-bow flag and the HO icon lists, resumes a held follow, unlocks facing, turns Ignore Joust Commands off and stands a feigned toon. Named movement blocks set with Movement:Block stay in.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.CampSpot:Release[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:LetsGo`, `LetsGo`

### `ResetAll`

`OgreBotAPI.CampSpot:ResetAll[fw]`

Puts all 8 slots back to new: no spot, no zone, radii 1 and 125, 3D off; clears the relative layer and makes slot 1 active. It also drops any hold on the leash, as ClearAll does, and it does not change Enabled.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.CampSpot:ResetAll[igw:${Me.Name}]
```

### `SetActive`

`OgreBotAPI.CampSpot:SetActive[fw, n]`

Makes slot n the one the leash uses, so the character heads for that slot's spot, and the relative layer carries over to it. A missing n or one outside 1 to 8 does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `n` | int |  | The slot to use, 1 to 8. |

```text
OgreBotAPI.CampSpot:SetActive[igw:${Me.Name},2]
```

### `SetFormation`

`OgreBotAPI.CampSpot:SetFormation[fw, kind=circle, dist=7, x, y, z, useRelative=FALSE, middle="", circleSpots=0]`

Places each character on a ring of radius dist around x,y,z and makes that the active slot's camp spot in the current zone, so the leash walks it there: circle spaces by group order 60 degrees apart, monkey 72 degrees with the named middle character on the centre, and monkeyraid 360/circleSpots degrees (default 5) by raid order with the middle for-who on the centre. The centre is required: a missing x, y or z, or one that is not a number, prints a line and does nothing, as does an unknown kind or OgreBot not open.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `kind` | string | `circle` | circle, monkey or monkeyraid. |
| `dist` | float | `7` | Ring radius; 0 or less means 7. |
| `x` | float or name |  | X of the centre, or the whole centre as one word: the name of a point of interest in this zone, or x,y,z. An unknown name prints one line and does nothing. |
| `y` | float |  | Y of the centre. Not read when x holds the whole location. |
| `z` | float |  | Z of the centre. Not read when x holds the whole location. |
| `useRelative` | bool | `FALSE` | TRUE to also set the ring spot as the relative layer's fixed destination. |
| `middle` | string | `""` | Who stands on the centre: a character name for monkey, a for-who for monkeyraid, TRUE for this character; FALSE or blank for nobody. Ignored for circle. |
| `circleSpots` | int | `0` | Number of ring spots for monkeyraid; less than 1 means 5. |

```text
OgreBotAPI.CampSpot:SetFormation[igw:${Me.Name},circle,7,${Me.X},${Me.Y},${Me.Z},FALSE,"",0]
```

*Was (OldBot):* `OgreBotAPI:Set_Formation_Circle`, `OgreBotAPI:Set_Formation_MonkeyInMiddle`, `OgreBotAPI:Set_Formation_MonkeyInMiddleRaid`

### `SetHere`

`OgreBotAPI.CampSpot:SetHere[fw, howClose=2, howFar=200]`

Sets the active slot's camp spot to where this character stands now, in the current zone, with the given arrival and leash radii (0 or less falls back to 1 and 125); the relative layer is kept. Nothing is set, with a line on the console, when OgreBot is not open (unless Movement:UseWithoutOgreBot is on) or when the Allow Camp Spot option is off.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `howClose` | float | `2` | Arrival radius: inside this distance the character counts as at the spot. |
| `howFar` | float | `200` | Leash radius: the leash walks back only from within this distance. |

```text
OgreBotAPI.CampSpot:SetHere[igw:${Me.Name},2,200]
```

*Was (OldBot):* `OgreBotAPI:CampSpot`, `Ogre_CampSpot:Set_CS`, `Ogre_CampSpot:Set_CampSpot`

### `SetHowClose`

`OgreBotAPI.CampSpot:SetHowClose[fw, v=0]`

Sets the active slot's arrival radius: inside this distance the character counts as at the spot. 0 or less (and the default) sets 1, and it works without a spot.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `v` | float | `0` | The arrival radius; 0 or less means 1. |

```text
OgreBotAPI.CampSpot:SetHowClose[igw:${Me.Name},3]
```

*Was (OldBot):* `Ogre_CampSpot:Set_HowClose`

### `SetHowFar`

`OgreBotAPI.CampSpot:SetHowFar[fw, v=0]`

Sets the active slot's leash radius: the leash walks back only from within this distance. 0 or less (and the default) sets 125, and it works without a spot.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `v` | float | `0` | The leash radius; 0 or less means 125. |

```text
OgreBotAPI.CampSpot:SetHowFar[igw:${Me.Name},150]
```

*Was (OldBot):* `Ogre_CampSpot:Set_HowFar`

### `SetLoc`

`OgreBotAPI.CampSpot:SetLoc[fw, x|point, y, z]`

Moves the active slot's camp spot to x,y,z (three values, one "x,y,z" text, or the name of a point of interest in this zone), keeping its zone and radii; it does not start a camp on its own, so the leash only walks there if the slot was set with SetHere, SetSlotHere or SetFormation in this zone. A missing, NULL or non-number coordinate or an unknown name sets nothing and prints a warning, and nothing is set (with a console line) when OgreBot is not open, unless Movement:UseWithoutOgreBot is on.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `x\|point` | float or name |  | X coordinate of the new spot, or the whole spot as one word: "x,y,z" or the name of a point of interest in this zone. |
| `y` | float |  | Y coordinate of the new spot. Not read when x holds the whole location. |
| `z` | float |  | Z coordinate of the new spot. Not read when x holds the whole location. |

```text
OgreBotAPI.CampSpot:SetLoc[igw:${Me.Name},${Me.X},${Me.Y},${Me.Z}]
```

*Was (OldBot):* `OgreBotAPI:CCS`, `OgreBotAPI:ChangeCampSpotWho`, `Ogre_CampSpot:Set_ChangeCampSpot`

### `SetLocAtAngleFromActor`

`OgreBotAPI.CampSpot:SetLocAtAngleFromActor[fw, angle, nameOrId, dist=3, skipIfAggro=FALSE, includeNpcSize=TRUE]`

Moves the active slot's camp spot to dist from the actor at angle degrees from the way it faces (0 is the SetLocBehindActor spot, 180 the SetLocInFrontOfActor spot), and with includeNpcSize TRUE the actor's size is added, so the same dist lands farther out than those two. Nothing happens when the actor is not found or is this character, and like SetLoc it moves the leash only if the slot was set with SetHere, SetSlotHere or SetFormation in this zone.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `angle` | float |  | Degrees from the actor's facing; 0 is behind, 180 is in front. |
| `nameOrId` | string |  | The actor: an ID, a name, an @role, pet:&lt;owner> or a class word. Blank uses this character's NPC target (its target, or its target's target). |
| `dist` | float | `3` | Distance from the actor; this character's own size is added. |
| `skipIfAggro` | bool | `FALSE` | TRUE to do nothing while the actor's threat on this character is at 100. |
| `includeNpcSize` | bool | `TRUE` | TRUE to add the actor's size to the distance as well. |

```text
OgreBotAPI.CampSpot:SetLocAtAngleFromActor[igw:${Me.Name},90,${Target.ID},3,FALSE,TRUE]
```

*Was (OldBot):* `OgreBotAPI:SetCS_NPC_ForWho`, `OgreBotAPI:SetCS_NPC`

### `SetLocBehindActor`

`OgreBotAPI.CampSpot:SetLocBehindActor[fw, nameOrId, dist=3, skipIfAggro=FALSE]`

Moves the active slot's camp spot to dist behind the actor, from the way it faces now (a one-time spot, not a follow), and the character walks there; nothing happens when the actor is not found or is this character. Like SetLoc, it moves the leash only if the slot was set with SetHere, SetSlotHere or SetFormation in this zone.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `nameOrId` | string |  | The actor: an ID, a name, an @role, pet:&lt;owner> or a class word. Blank uses this character's NPC target (its target, or its target's target). |
| `dist` | float | `3` | Distance from the actor; this character's own size is added. |
| `skipIfAggro` | bool | `FALSE` | TRUE to do nothing while the actor's threat on this character is at 100. |

```text
OgreBotAPI.CampSpot:SetLocBehindActor[igw:${Me.Name},${Target.ID},3,FALSE]
```

*Was (OldBot):* `OgreBotAPI:SetCS_BehindNPC`

### `SetLocByRole`

`OgreBotAPI.CampSpot:SetLocByRole[fw, nameOrId, dist=3, skipIfAggro=FALSE]`

Each character picks its own side - fighters take the spot in front of the actor and everyone else the spot behind it, as SetLocInFrontOfActor and SetLocBehindActor do; nothing happens when the actor is not found or is this character. Like SetLoc, it moves the leash only if the slot was set with SetHere, SetSlotHere or SetFormation in this zone.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `nameOrId` | string |  | The actor: an ID, a name, an @role, pet:&lt;owner> or a class word. Blank uses this character's NPC target (its target, or its target's target). |
| `dist` | float | `3` | Distance from the actor; this character's own size is added. |
| `skipIfAggro` | bool | `FALSE` | TRUE to do nothing while the actor's threat on this character is at 100. |

```text
OgreBotAPI.CampSpot:SetLocByRole[igw:${Me.Name},${Target.ID},3,FALSE]
```

*Was (OldBot):* `OgreBotAPI:SetCS_PositionNPC`

### `SetLocInFrontOfActor`

`OgreBotAPI.CampSpot:SetLocInFrontOfActor[fw, nameOrId, dist=3, skipIfAggro=FALSE]`

Moves the active slot's camp spot to dist in front of the actor, from the way it faces now (a one-time spot, not a follow), and the character walks there; nothing happens when the actor is not found or is this character. Like SetLoc, it moves the leash only if the slot was set with SetHere, SetSlotHere or SetFormation in this zone.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `nameOrId` | string |  | The actor: an ID, a name, an @role, pet:&lt;owner> or a class word. Blank uses this character's NPC target (its target, or its target's target). |
| `dist` | float | `3` | Distance from the actor; this character's own size is added. |
| `skipIfAggro` | bool | `FALSE` | TRUE to do nothing while the actor's threat on this character is at 100. |

```text
OgreBotAPI.CampSpot:SetLocInFrontOfActor[igw:${Me.Name},${Target.ID},3,FALSE]
```

*Was (OldBot):* `OgreBotAPI:SetCS_InFrontNPC`

### `SetRelativeBy`

`OgreBotAPI.CampSpot:SetRelativeBy[fw, dx=0, dy=0, dz=0]`

Adds dx, dy and dz to the relative offset (it does not replace it) and puts the layer in offset mode, so the leash goes to the active slot's spot plus the offset; after SetRelativeLoc the spot stays where it is and moves by exactly that amount. Nothing is set, with a line on the console, when OgreBot is not open (unless Movement:UseWithoutOgreBot is on).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `dx` | float | `0` | Amount added to the X offset. |
| `dy` | float | `0` | Amount added to the Y offset. |
| `dz` | float | `0` | Amount added to the Z offset. |

```text
OgreBotAPI.CampSpot:SetRelativeBy[igw:${Me.Name},0,0,5]
```

*Was (OldBot):* `OgreBotAPI:CS_Set_ChangeRelativeCampSpotBy`, `Ogre_CampSpot:Set_ChangeRelativeCampSpotBy`

### `SetRelativeLoc`

`OgreBotAPI.CampSpot:SetRelativeLoc[fw, x, y, z]`

Makes x,y,z the fixed destination of the relative layer, so the leash takes this character there instead of the slot's spot (which is kept, and ClearRelative goes back to it); x, y and z are all required, and a missing, NULL or non-number value gets one line and sets nothing. Nothing is set, with a line on the console, when OgreBot is not open (unless Movement:UseWithoutOgreBot is on).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `x` | float |  | X of the destination. |
| `y` | float |  | Y of the destination. |
| `z` | float |  | Z of the destination. |

```text
OgreBotAPI.CampSpot:SetRelativeLoc[igw:${Me.Name},${Target.X},${Target.Y},${Target.Z}]
```

*Was (OldBot):* `OgreBotAPI:CRCS`, `OgreBotAPI:Set_Relative`, `Ogre_CampSpot:Set_Relative`

### `SetSlotHere`

`OgreBotAPI.CampSpot:SetSlotHere[fw, n=1, howClose=2, howFar=200]`

Sets slot n (1 to 8; anything else does nothing) to where this character stands now, in the current zone, without changing the active slot, so the leash uses it once SetActive picks that slot. Nothing is set, with a line on the console, when OgreBot is not open (unless Movement:UseWithoutOgreBot is on) or the Allow Camp Spot option is off.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `n` | int | `1` | The slot to set, 1 to 8. |
| `howClose` | float | `2` | Arrival radius for that slot (0 or less falls back to 1). |
| `howFar` | float | `200` | Leash radius for that slot (0 or less falls back to 125). |

```text
OgreBotAPI.CampSpot:SetSlotHere[${Me.Name},2,2,200]
```

### `SetUse3D`

`OgreBotAPI.CampSpot:SetUse3D[fw, on=TRUE]`

Turns 3D distance on or off for the active slot; off measures on the ground plane only (X and Z). Left out means on, and a word that is not yes or no leaves it as it is.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `on` | bool | `TRUE` | TRUE for 3D distances, FALSE for ground-plane distances. |

```text
OgreBotAPI.CampSpot:SetUse3D[igw:${Me.Name},TRUE]
```

*Was (OldBot):* `Ogre_CampSpot:Set_Use3D`
