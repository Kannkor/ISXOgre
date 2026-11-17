# OgreBotAPI.AutoHunt

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Members

### `Active`

`${OgreBotAPI.AutoHunt.Active}`

TRUE when AutoHunt is switched on in Hunt mode. It reflects the mode only, so it stays TRUE while the hunt sits idle because OgreBot is closed or the bot is paused.

**Returns:** bool: TRUE when the mode is Hunt; FALSE when it is Off.

```text
echo ${OgreBotAPI.AutoHunt.Active}
```

### `AllowMovement`

`${OgreBotAPI.AutoHunt.AllowMovement}`

TRUE when AutoHunt is letting this character move: a camp spot pulls again and the path picked on the Auto-Hunt tab walks on. It is FALSE while it holds position because a safety check tripped or a mob or an add is being dealt with, and TRUE while the character flies, since AutoHunt holds nothing in the air; it is updated on each hunt tick, and it reads FALSE after the mode is set to Off.

**Returns:** bool: TRUE when AutoHunt has released its hold on movement; FALSE when it is holding position or AutoHunt is Off.

```text
echo ${OgreBotAPI.AutoHunt.AllowMovement}
```

### `FreezeReason`

`${OgreBotAPI.AutoHunt.FreezeReason}`

Which safety check stopped the hunt on its last tick, or None when it was safe or the character was flying (the checks are not read in the air). It is not cleared when the mode is set to Off, so it can still show the last reason after AutoHunt is turned off.

**Returns:** string: None, Aggro, Dead, LowHP, LowMana or ExquisiteChest. Only the first check that tripped is named, and a group or raid member who is not in the zone counts as Dead or LowHP when those checks are on.

```text
echo ${OgreBotAPI.AutoHunt.FreezeReason}
```

### `LastAction`

`${OgreBotAPI.AutoHunt.LastAction}`

What AutoHunt decided to do on its last tick. It reads None after the mode is set to Off and keeps the last value while the hunt sits idle.

**Returns:** string: None, Walk, HoldPosition, MoveGroupToCamp, Prebuff, AcquireTarget, Pull or Cleanup. Walk means no mob is in reach, or the character is flying and AutoHunt pulls nothing in the air, so the character may walk on. None while the character is dead: AutoHunt holds as it stands.

```text
echo ${OgreBotAPI.AutoHunt.LastAction}
```

### `Mode`

`${OgreBotAPI.AutoHunt.Mode}`

The AutoHunt mode this character is in: Off or Hunt. It starts as Off when the extension loads and is not saved, and it still reads Hunt while the hunt sits idle because OgreBot is closed or the bot is paused.

**Returns:** string: Off or Hunt.

```text
echo ${OgreBotAPI.AutoHunt.Mode}
```

### `PullTargetID`

`${OgreBotAPI.AutoHunt.PullTargetID}`

The actor ID of the mob the last Hunt tick picked to pull, or 0 when none was found in the scan radius or the character is flying (no pull in the air); a different answer counts only after it has held for 0.3 seconds. It is 0 after the mode is set to Off, and an add already attacking the group is handled first but is not shown here.

**Returns:** int64: the actor ID picked to pull on the last tick; 0 when there was none.

```text
echo ${OgreBotAPI.AutoHunt.PullTargetID}
```

### `SafetyTripped`

`${OgreBotAPI.AutoHunt.SafetyTripped}`

TRUE when one of the AutoHunt safety checks (aggro, dead, low health, low power, exquisite chest) stopped the hunt on its last tick. It keeps the last tick's value while the hunt sits idle and reads FALSE after the mode is set to Off.

**Returns:** bool: TRUE when a safety check that is ticked in the AutoHunt settings tripped on the last tick; FALSE when all were clear, the character was flying (the checks are not read in the air) or AutoHunt is Off.

```text
echo ${OgreBotAPI.AutoHunt.SafetyTripped}
```

## Methods

### `SetCheckHP`

`OgreBotAPI.AutoHunt:SetCheckHP[fw, n]`

Sets the AutoHunt Check HP threshold in the loaded OgreBot profile: with Check HP ticked, the hunt holds position while any group or raid member (this character included) is below n percent health, and a member who is not in the zone counts too; it does not tick the checkbox, and 0 never trips. A missing value or no loaded profile prints a line and sets nothing, a value outside 0 to 100 or a word is stored clamped with a line saying so, and the change is kept only when the profile is saved.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `n` | int |  | Health percent; the hunt holds when a member is below it. 0 never trips; outside 0 to 100 it is clamped. |

```text
OgreBotAPI.AutoHunt:SetCheckHP[igw:${Me.Name},60]
```

*Was (OldBot):* `OgreBotAPI:AutoHunt_CheckHP`

### `SetCheckMana`

`OgreBotAPI.AutoHunt:SetCheckMana[fw, n]`

Sets the AutoHunt Check Mana threshold in the loaded OgreBot profile: with Check Mana ticked, the hunt holds position while any group or raid member in the zone (this character included) is below n percent power; it does not tick the checkbox, and 0 never trips. A missing value or no loaded profile prints a line and sets nothing, a value outside 0 to 100 or a word is stored clamped with a line saying so, and the change is kept only when the profile is saved.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `n` | int |  | Power percent; the hunt holds when a member is below it. 0 never trips; outside 0 to 100 it is clamped. |

```text
OgreBotAPI.AutoHunt:SetCheckMana[igw:${Me.Name},30]
```

*Was (OldBot):* `OgreBotAPI:AutoHunt_CheckMana`

### `SetMode`

`OgreBotAPI.AutoHunt:SetMode[fw, off|hunt]`

Sets the AutoHunt mode on each matching character: off stops it, ends its walk, releases its hold on the camp spot and lets go a group it holds at a camp, and hunt tells the rest of its group to follow it, then picks a mob in the scan radius (an add on the group first), targets it, uses the first ready ability or item from the AutoHunt pull list and walks the path picked on the Auto-Hunt tab between pulls. The mode is not saved, and an unknown word, or hunt while OgreBot is not open, sets Off and echoes why to the console.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `off\|hunt` | string |  | The mode, any case: off or hunt. Blank means off, and any other word, movement, on and grind included, sets Off. Hunt sends the follow once, as an OgreFollow through OgreConsole, so only characters on this PC get it; off leaves them following. With the Campspot or CS-JO-JI option a pull camps the whole group at this character's spot, a new pull from the same spot sends nothing, and the group is let go (a LetsGo, and this character's own camp cleared) once no mob has been in reach for 1.5 seconds, or at once when the bot is paused or the mode goes off. In the air it pulls, targets and holds nothing (a pull it was working ends, and one console line says so as it takes off), and while it is dead it holds everything as it is. |

```text
OgreBotAPI.AutoHunt:SetMode[${Me.Name},hunt]
```

*Was (OldBot):* `OgreBotAPI:AutoHunt_SetMode`

### `SetScanRadius`

`OgreBotAPI.AutoHunt:SetScanRadius[fw, n]`

Sets the AutoHunt scan radius in the loaded OgreBot profile, the distance Hunt mode searches for a mob to pull; 0 means the longest reach among your enabled pull abilities (35 when none has a reach on file). A missing value or no loaded profile prints a line and sets nothing, a negative or a word is stored as 0 with a line saying so, and the change is kept only when the profile is saved.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `n` | int |  | Scan radius in game units; 0 uses the longest reach among your pull abilities. |

```text
OgreBotAPI.AutoHunt:SetScanRadius[igw:${Me.Name},50]
```

*Was (OldBot):* `OgreBotAPI:AutoHunt_ScanRadius`
