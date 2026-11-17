<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# OgreBotAPI.Movement

## Members

### `Active`

`${OgreBotAPI.Movement.Active}`

TRUE while the bot's mover is driving your character anywhere. That includes Movement:ToLoc, Come2Me and Move2Area, but also follow, the camp spot and nav trips.

**Returns:** bool: TRUE while a move is in progress; FALSE when the mover is idle.

```text
echo ${OgreBotAPI.Movement.Active}
```

### `AllowMovement`

`${OgreBotAPI.Movement.AllowMovement}`

TRUE when no movement block is held, the exact opposite of Blocked with no reason. It does not count the camp spot holds left by Come2Me, Move2Area or JoustIn.

**Returns:** bool: TRUE when no block is held; FALSE when at least one is.

```text
echo ${OgreBotAPI.Movement.AllowMovement}
```

*Was (OldBot):* `Obj_CampSpot.AllowCampSpot`, `Obj_Movement.AllowCampSpot`, `Ogre_CampSpot.AllowCampSpot`

### `AlreadyFacing`

`${OgreBotAPI.Movement.AlreadyFacing[id]}`

TRUE when your heading is within 45 degrees of the heading to the actor with this ID. FALSE when you are not in the world or the actor is not known.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `id` | int64 |  | The actor ID to measure against (a number, such as ${Target.ID}). A name is not looked up. |

**Returns:** bool: TRUE when you are roughly facing the actor; FALSE when you are not, are not in the world, or the actor is not known.

```text
echo ${OgreBotAPI.Movement.AlreadyFacing[${Target.ID}]}
```

### `BehindLoc`

`${OgreBotAPI.Movement.BehindLoc[id,dist]}`

A point the given distance directly behind the actor, based on the way the actor is facing, at the actor's height. Returns an empty string when the actor is not found.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `id` | int64 |  | The actor ID to measure against (a number, such as ${Target.ID}). A name is not looked up. |
| `dist` | float | `5` | How far from the actor the point is, in meters. |

**Returns:** string: "x,y,z" behind the actor; "" when the actor is not found.

```text
echo ${OgreBotAPI.Movement.BehindLoc[${Target.ID},5]}
```

### `BlockCount`

`${OgreBotAPI.Movement.BlockCount}`

How many different movement blocks are held right now. Adding the same reason twice counts once.

**Returns:** int: the number of distinct block reasons held; 0 when movement is free.

```text
echo ${OgreBotAPI.Movement.BlockCount}
```

*Was (OldBot):* `Obj_CampSpot.uAllowMovement`, `Obj_Movement.uAllowMovement`, `Ogre_CampSpot.uAllowMovement`

### `Blocked`

`${OgreBotAPI.Movement.Blocked[reason]}`

With a reason, TRUE when that named movement block is held; with the reason left blank, TRUE when any block is held. Reason names are case-sensitive, and the bot's own movers add blocks too while they run.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `reason` | string |  | The block name to check, as given to Movement:Block. Leave it blank to ask whether any block is held. |

**Returns:** bool: TRUE when the named block (or, with no reason, any block) is held; FALSE otherwise.

```text
echo ${OgreBotAPI.Movement.Blocked[MyScript]}
```

*Was (OldBot):* `Obj_CampSpot.Disabled`, `Obj_Movement.Disabled`, `Ogre_CampSpot.Disabled`

### `BlockReasons`

`${OgreBotAPI.Movement.BlockReasons}`

The names of every movement block held right now, so you can see what is stopping a character. This includes blocks the bot's own movers hold while they run.

**Returns:** string: the block reasons separated by commas; "" when no block is held.

```text
echo ${OgreBotAPI.Movement.BlockReasons}
```

*Was (OldBot):* `Obj_CampSpot.sc_ItemsAffectingMovement`, `Obj_Movement.sc_ItemsAffectingMovement`, `Ogre_CampSpot.sc_ItemsAffectingMovement`

### `Distance2DTo`

`${OgreBotAPI.Movement.Distance2DTo[id]}`

The flat distance from you to the actor with this ID, ignoring height (X and Z only). Returns -1 when the ID is 0, is not a number, or no such actor is nearby.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `id` | int64 |  | The actor ID to measure against (a number, such as ${Target.ID}). A name is not looked up. |

**Returns:** float: the ground distance in meters; -1 when the actor is not found.

```text
echo ${OgreBotAPI.Movement.Distance2DTo[${Target.ID}]}
```

### `DistanceTo`

`${OgreBotAPI.Movement.DistanceTo[id]}`

The straight-line (3D) distance from you to the actor with this ID. Returns -1 when the ID is 0, is not a number, or no such actor is nearby.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `id` | int64 |  | The actor ID to measure against (a number, such as ${Target.ID}). A name is not looked up. |

**Returns:** float: the distance in meters; -1 when the actor is not found.

```text
echo ${OgreBotAPI.Movement.DistanceTo[${Target.ID}]}
```

### `FaceLockActor`

`${OgreBotAPI.Movement.FaceLockActor}`

The ID of the actor the face lock is holding you toward.

**Returns:** int64: the locked actor's ID; 0 when the lock is on a location, or when no lock is held.

```text
echo ${OgreBotAPI.Movement.FaceLockActor}
```

### `FaceLocked`

`${OgreBotAPI.Movement.FaceLocked}`

TRUE while a face lock from Movement:FaceLock or :FaceLockLoc is held on this session. While it is held, nothing else can turn you and movement waits.

**Returns:** bool: TRUE while a face lock is held; FALSE when there is none.

```text
echo ${OgreBotAPI.Movement.FaceLocked}
```

### `FaceLockRemaining`

`${OgreBotAPI.Movement.FaceLockRemaining}`

How long the current face lock has left before it lets go on its own, in milliseconds.

**Returns:** int: milliseconds left on the lock; 0 when no lock is held.

```text
echo ${OgreBotAPI.Movement.FaceLockRemaining}
```

### `FrontLoc`

`${OgreBotAPI.Movement.FrontLoc[id,dist]}`

A point the given distance directly in front of the actor, based on the way the actor is facing, at the actor's height. Returns an empty string when the actor is not found.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `id` | int64 |  | The actor ID to measure against (a number, such as ${Target.ID}). A name is not looked up. |
| `dist` | float | `5` | How far from the actor the point is, in meters. |

**Returns:** string: "x,y,z" in front of the actor; "" when the actor is not found.

```text
echo ${OgreBotAPI.Movement.FrontLoc[${Target.ID},8]}
```

### `GettingToGH`

`${OgreBotAPI.Movement.GettingToGH}`

TRUE while a trip started by Movement:GetToGH is waiting in the action queue or running. It goes FALSE on its own once that trip finishes, fails or is removed.

**Returns:** bool: TRUE while a guild hall trip is in progress; FALSE otherwise.

```text
echo ${OgreBotAPI.Movement.GettingToGH}
```

*Was (OldBot):* `OgreBotAPI.GettingToGH`

### `GoalDistance`

`${OgreBotAPI.Movement.GoalDistance}`

How far you still are from the goal of the move in progress. A Movement:ToLoc move measures this flat, ignoring height.

**Returns:** float: the distance in meters to the current goal; -1 when no move is in progress, or during a straight climb or descent.

```text
echo ${OgreBotAPI.Movement.GoalDistance}
```

### `HeadingTo`

`${OgreBotAPI.Movement.HeadingTo[id]}`

The heading, in degrees, you would face to look at the actor with this ID. An unknown ID reads -1.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `id` | int64 |  | The actor ID to measure against (a number, such as ${Target.ID}). A name is not looked up. |

**Returns:** float: a heading in degrees; -1 when the actor is not found.

```text
echo ${OgreBotAPI.Movement.HeadingTo[${Target.ID}]}
```

### `LeftLoc`

`${OgreBotAPI.Movement.LeftLoc[id,dist]}`

A point the given distance to the actor's left side, based on the way the actor is facing, at the actor's height. Returns an empty string when the actor is not found.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `id` | int64 |  | The actor ID to measure against (a number, such as ${Target.ID}). A name is not looked up. |
| `dist` | float | `5` | How far from the actor the point is, in meters. |

**Returns:** string: "x,y,z" to the actor's left; "" when the actor is not found.

```text
echo ${OgreBotAPI.Movement.LeftLoc[${Target.ID},5]}
```

### `MyLoc`

`${OgreBotAPI.Movement.MyLoc}`

Your current location as text, three numbers with two decimals each.

**Returns:** string: "x,y,z" - where your character is now.

```text
echo ${OgreBotAPI.Movement.MyLoc}
```

### `RightLoc`

`${OgreBotAPI.Movement.RightLoc[id,dist]}`

A point the given distance to the actor's right side, based on the way the actor is facing, at the actor's height. Returns an empty string when the actor is not found.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `id` | int64 |  | The actor ID to measure against (a number, such as ${Target.ID}). A name is not looked up. |
| `dist` | float | `5` | How far from the actor the point is, in meters. |

**Returns:** string: "x,y,z" to the actor's right; "" when the actor is not found.

```text
echo ${OgreBotAPI.Movement.RightLoc[${Target.ID},5]}
```

### `UseWithoutOgreBot`

`${OgreBotAPI.Movement.UseWithoutOgreBot}`

Whether movement is allowed while OgreBot is not open, as set by Movement:UseWithoutOgreBot. It starts FALSE in every session.

**Returns:** bool: TRUE when movement runs without OgreBot open; FALSE when movement needs OgreBot open.

```text
echo ${OgreBotAPI.Movement.UseWithoutOgreBot}
```

## Methods

### `AutoRun`

`OgreBotAPI.Movement:AutoRun[fw]`

Presses your autorun key once (Num Lock unless you have bound another), which toggles autorun in the game.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Movement:AutoRun[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:AutoRun`

### `Block`

`OgreBotAPI.Movement:Block[fw, reason]`

Adds a named movement block and stops the move in progress. While any block is held the camp spot, follow, new nav trips and queued moves all stay still, but a direct Movement:ToLoc, Come2Me or Move2Area still moves; a blank reason prints a line and adds nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `reason` | string |  | A name for this block, so Movement:Unblock can release exactly this one. Case-sensitive. |

```text
OgreBotAPI.Movement:Block[${Me.Name},MyScript]
```

*Was (OldBot):* `Obj_CampSpot:Disable`, `Obj_Movement:Disable`, `Ogre_CampSpot:Disable`

### `CallGH`

`OgreBotAPI.Movement:CallGH[fw]`

Queues a cast of Call to Guild Hall after a short random wait (0.5 to 3.4 seconds). A Brigand in Safehouse has it cancelled first; does nothing when you are already in the guild hall.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Movement:CallGH[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:CallGH`, `call Obj_OgreUtilities.CallToGH`

### `ClearBlocks`

`OgreBotAPI.Movement:ClearBlocks[fw]`

Releases every movement block at once, including blocks the bot's own movers hold, which ends a nav trip under way. It does not release the camp spot holds from Come2Me, Move2Area or JoustIn.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Movement:ClearBlocks[${Me.Name}]
```

*Was (OldBot):* `Obj_CampSpot:Clear`, `Obj_Movement:Clear`, `Ogre_CampSpot:Clear`

### `Come2Me`

`OgreBotAPI.Movement:Come2Me[fw, toWho=me, precision=3]`

Runs to where the named character is standing at the moment of the call, stopping within the precision; it needs OgreBot open (or Movement:UseWithoutOgreBot) and prints a line when it is not, and a character with Allow Camp Spot off stays put and prints a line. On arrival the character stays there instead of going back to its camp spot until JoustOut or LetsGo, a name that matches nobody here prints a line and does nothing, and after 10 seconds stuck the move stops with one line.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `toWho` | string | `me` | Who to run to: a name (part of a name works), an actor ID or an @ alias. Blank means yourself. |
| `precision` | float | `3` | How close counts as arrived, in meters. |

```text
OgreBotAPI.Movement:Come2Me[${Me.Name},${Group[1].Name},3]
```

*Was (OldBot):* `OgreBotAPI:Come2Me`

### `Crouch`

`OgreBotAPI.Movement:Crouch[fw]`

Presses your crouch key once (Z unless you have bound another).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Movement:Crouch[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Crouch`, `OgreCrouchKey`

### `Evac`

`OgreBotAPI.Movement:Evac[fw, mode=""]`

Queues your class evacuation spell when you have one and it is ready (Escape for scouts, Shadowy Elusion for Shadowknights, Depart for Wizards, Verdurous Journey for Wardens). With mode totem, a character without a ready class evac uses a Totem of Escape from its bags instead, and prints a line when it has none or it is on cooldown; without totem it prints one line saying why it did not evacuate.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `mode` | string | `""` | Blank for the class evac only; totem to fall back to a Totem of Escape. |

```text
OgreBotAPI.Movement:Evac[${Me.Name},totem]
```

*Was (OldBot):* `OgreBotAPI:Evac`, `call Obj_OgreUtilities.CastEvac`

### `FaceActor`

`OgreBotAPI.Movement:FaceActor[fw, nameOrId]`

Turns you to face the actor, found by exact name, actor ID or @ alias. No actor given (0 counts as none) prints an error, an actor that is not here prints a line, and nothing turns while a face lock is held.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `nameOrId` | string |  | The actor's exact name, its actor ID, or an @ alias. |

```text
OgreBotAPI.Movement:FaceActor[${Me.Name},${Target.ID}]
```

*Was (OldBot):* `OgreBotAPI:FaceActor`, `Obj_OgreIH:FaceActor`

### `FaceAngle`

`OgreBotAPI.Movement:FaceAngle[fw, angle]`

Turns you to the heading in degrees (0 is north). A missing angle prints an error, and nothing turns while a face lock is held.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `angle` | float |  | The heading to face, in degrees. |

```text
OgreBotAPI.Movement:FaceAngle[${Me.Name},180]
```

*Was (OldBot):* `OgreBotAPI:FaceAngle`, `Obj_OgreIH:FaceAngle`

### `FaceLoc`

`OgreBotAPI.Movement:FaceLoc[fw, x, y, z]`

Turns you to face the location using X and Z; the height is not used. A missing x or z prints an error, and nothing turns while a face lock is held.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `x` | float or name |  | X of the location, or the whole location as one word: the name of a point of interest in this zone, or x,y,z. An unknown name prints one line and does nothing. |
| `y` | float |  | Y (height). Ignored - a heading is flat - and kept so a location pastes in as x,y,z (${Me.Loc} as is). |
| `z` | float |  | Z of the location. Not read when x holds the whole location. |

```text
OgreBotAPI.Movement:FaceLoc[${Me.Name},100,20,-250]
```

*Was (OldBot):* `OgreBotAPI:FaceLoc`, `Obj_OgreIH:FaceLoc`

### `FaceLock`

`OgreBotAPI.Movement:FaceLock[fw, nameOrId, ttlSeconds=0]`

Turns you to the actor and holds that heading, turning again when you drift more than 45 degrees (at most once a second); while held, nothing else can turn you, movement waits and the game's /follow is stopped. The lock ends after ttlSeconds, on Movement:FaceUnlock, LetsGo, zoning, death or camping, or when the actor is gone, and an actor that is not found takes no lock.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `nameOrId` | string |  | The actor's exact name, its actor ID, or an @ alias. |
| `ttlSeconds` | int | `0` | How long the lock lasts, in seconds. 0 or blank means 15; the most is 120. |

```text
OgreBotAPI.Movement:FaceLock[${Me.Name},${Target.ID},10]
```

### `FaceLockLoc`

`OgreBotAPI.Movement:FaceLockLoc[fw, x, z, ttlSeconds=0]`

Turns you toward the location and holds that heading, the same way Movement:FaceLock does for an actor. A missing x or z prints an error, and the lock ends after ttlSeconds, on Movement:FaceUnlock, LetsGo, zoning, death or camping.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `x` | float or name |  | X of the location to face, or the whole location as one word: the name of a point of interest in this zone, or x,y,z. An unknown name prints one line and does nothing. |
| `z` | float |  | Z of the location to face. Not read when x holds the whole location. |
| `ttlSeconds` | int | `0` | How long the lock lasts, in seconds. 0 or blank means 15; the most is 120. |

```text
OgreBotAPI.Movement:FaceLockLoc[${Me.Name},100,-250,10]
```

### `FaceUnlock`

`OgreBotAPI.Movement:FaceUnlock[fw]`

Releases the face lock, so other turns and movement carry on. Does nothing when no lock is held.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Movement:FaceUnlock[${Me.Name}]
```

### `FlyDown`

`OgreBotAPI.Movement:FlyDown[fw]`

Holds your fly down key (End unless you have bound another) and keeps holding it until Movement:FlyStop. Use Movement:LandFlyingMount to descend and stop on landing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Movement:FlyDown[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:FlyDown`, `Obj_OgreIH:FlyDown`, `call Obj_LICH.FlySwimDown`

### `FlyStop`

`OgreBotAPI.Movement:FlyStop[fw]`

Lets go of both the fly up and fly down keys, whichever one was held.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Movement:FlyStop[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:FlyStop`, `Obj_OgreIH:FlyStop`

### `FlyUp`

`OgreBotAPI.Movement:FlyUp[fw]`

Holds your fly up key (Home unless you have bound another) and keeps holding it until Movement:FlyStop. It only climbs when you are on a flying mount or swimming.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Movement:FlyUp[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:FlyUp`, `Obj_OgreIH:FlyUp`, `call Obj_LICH.FlySwimUp`

### `Follow`

`OgreBotAPI.Movement:Follow[fw, leader=off, minDistance=8, maxDistance=200, breakWithNoTarget=FALSE, backOffDistance=0]`

Follows the leader with the bot's own follow, moving up when farther than minDistance and stopping when the leader is beyond maxDistance; it stops the game's /follow and needs OgreBot open (or Movement:UseWithoutOgreBot) to start. A leader of off, blank or your own name turns follow off, as does off given as the for-who; an unknown leader or bad distances print a line.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `leader` | string | `off` | Who to follow: a character name, an actor ID, or off to stop following. |
| `minDistance` | float | `8` | Follow moves up when the leader is farther than this, in meters. Must be above 0. |
| `maxDistance` | float | `200` | Follow stops chasing when the leader is this far or farther. Must be above minDistance. |
| `breakWithNoTarget` | bool | `FALSE` | TRUE to turn follow off the first time it needs to move up while you have no target. |
| `backOffDistance` | float | `0` | Back away from a leader closer than this, in meters. 0 is off; otherwise at least 1 less than minDistance. |

```text
OgreBotAPI.Movement:Follow[${Me.Name},${Group[1].Name},8,200,FALSE,0]
```

*Was (OldBot):* `OgreBotAPI:OFollow`

### `FollowDistanceDown`

`OgreBotAPI.Movement:FollowDistanceDown[fw]`

Takes 2 meters off the follow distances: minDistance never goes below 1, and maxDistance is left alone when minDistance hits that floor. A back-off distance shrinks with them and turns off when there is no room left.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Movement:FollowDistanceDown[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:OFolDecDistance`

### `FollowDistanceUp`

`OgreBotAPI.Movement:FollowDistanceUp[fw]`

Adds 2 meters to both follow distances (and to the back-off distance when one is set).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Movement:FollowDistanceUp[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:OFolIncDistance`

### `ForceFollow`

`OgreBotAPI.Movement:ForceFollow[fw]`

Starts the game's /follow on the character named in the OgreBot panel's auto follow setting. It does nothing unless auto follow is ticked and that character is in your group and alive.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Movement:ForceFollow[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:ForceFollow`

### `GetToConcentration`

`OgreBotAPI.Movement:GetToConcentration[fw, concentration=4]`

Cancels your maintained buffs that use concentration, last one first, only until used concentration is down to the given amount, counting what each buff costs. It does nothing when you already use that much or less.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `concentration` | int | `4` | The used concentration to get down to. |

```text
OgreBotAPI.Movement:GetToConcentration[${Me.Name},3]
```

*Was (OldBot):* `OgreBotAPI:GetToConcentration`, `Obj_OgreIH:GetToConcentration`

### `GetToGH`

`OgreBotAPI.Movement:GetToGH[fw]`

Queues a trip to the guild hall: Call to Guild Hall when it is ready, otherwise Call to Home (or fast travel) to housing and then the house door to the guild hall, picked when the trip starts. It prints a line and does nothing when a trip is already in progress, when you are already in the guild hall, or when no route is ready.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Movement:GetToGH[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:GetToGH`, `call OgreBotAPI.HouseWindowToGH`

### `JoustIn`

`OgreBotAPI.Movement:JoustIn[fw]`

Holds the character where it is instead of going back to its camp spot, unless it was told JoustOff, and resumes a paused follow. It has no effect while no camp spot is set, and JoustOut releases it.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Movement:JoustIn[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:JoustIn`

### `JoustOff`

`OgreBotAPI.Movement:JoustOff[fw]`

Makes the character ignore later JoustIn calls, so it does not hold where it is. Left blank the for-who is Casters, not all, and it does nothing while no camp spot is set.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Movement:JoustOff[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:JoustOff`

### `JoustOn`

`OgreBotAPI.Movement:JoustOn[fw]`

Makes the character obey JoustIn again. Left blank the for-who is Melee, not all, and it does nothing while no camp spot is set.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Movement:JoustOn[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:JoustOn`

### `JoustOut`

`OgreBotAPI.Movement:JoustOut[fw]`

Releases the JoustIn hold, and the hold left by Come2Me or Move2Area, so the character goes back to its camp spot.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Movement:JoustOut[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:JoustOut`

### `Jump`

`OgreBotAPI.Movement:Jump[fw]`

Presses your jump key once (Space unless you have bound another).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Movement:Jump[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Jump`, `Obj_OgreUtilities:Jump`, `OgreJumpKey`

### `JumpRoute`

`OgreBotAPI.Movement:JumpRoute[fw, start, jump, end, completed="", flag...]`

Walks to start, then on to end, pressing jump once when passing within 2 meters of the jump point, and on arrival sets the camp spot to completed (or to end). It runs in the background and gives up after 10 seconds by default; a bad point or flag, or a route already running, prints why.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `start` | string |  | The first point to walk to, as "x,y,z". |
| `jump` | string |  | Where to jump on the way to end, as "x,y,z". |
| `end` | string |  | Where the route ends, as "x,y,z". |
| `completed` | string | `""` | The camp spot to set on arrival, as "x,y,z". Blank, or an X of 0, uses end. |
| `flag...` | string |  | Optional flags, one per argument, each followed by its value: -JumpDistance meters (default 2), -MaxTimer seconds per try (default 10), -Attempts 1 to 10, -RetryDelay seconds, -AboveY height that counts as success, -RunMode walk or run. |

```text
OgreBotAPI.Movement:JumpRoute[${Me.Name},"100,20,-250","104,20,-246","110,25,-240","",-JumpDistance,1,-MaxTimer,12]
```

*Was (OldBot):* `OgreBotAPI:Set_CampSpotJump_Handle`, `Obj_CampSpotJump:Handle`, `Obj_CampSpotJump:HandleAdvanced`

### `LandFlyingMount`

`OgreBotAPI.Movement:LandFlyingMount[fw]`

Queues a landing: holds your fly down key until you are no longer flying, for up to 60 seconds, then lets go of it. Does nothing when you are not on a flying mount.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Movement:LandFlyingMount[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:LandFlyingMount`

### `Move2Area`

`OgreBotAPI.Movement:Move2Area[fw, x, y, z, precision=3]`

Runs to the location (X and Z, height ignored) and then stays there instead of going back to its camp spot until JoustOut or LetsGo. Only a character that has a target moves; it needs OgreBot open (or Movement:UseWithoutOgreBot) and prints a line when it is not, a character with Allow Camp Spot off stays put and prints a line, a missing x or z prints an error, and after 10 seconds stuck the move stops with one line.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `x` | float or name |  | X of the location, or the whole location as one word: the name of a point of interest in this zone, or x,y,z. An unknown name prints one line and does nothing. |
| `y` | float |  | Y (height). Not used: this is a ground move, so you can paste ${Me.Loc} as is. |
| `z` | float |  | Z of the location. Not read when x holds the whole location. |
| `precision` | float | `3` | How close counts as arrived, in meters. |

```text
OgreBotAPI.Movement:Move2Area[${Me.Name},100,20,-250,3]
```

*Was (OldBot):* `OgreBotAPI:Move2Area`

### `Move2AreaNoTarget`

`OgreBotAPI.Movement:Move2AreaNoTarget[fw, x, y, z, precision=3]`

The same as Move2Area, but the character moves whether or not it has a target. It runs to X and Z (height ignored) and then stays there instead of going back to its camp spot until JoustOut or LetsGo, a character with Allow Camp Spot off stays put and prints a line, and after 10 seconds stuck the move stops with one line.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `x` | float or name |  | X of the location, or the whole location as one word: the name of a point of interest in this zone, or x,y,z. An unknown name prints one line and does nothing. |
| `y` | float |  | Y (height). Not used: this is a ground move, so you can paste ${Me.Loc} as is. |
| `z` | float |  | Z of the location. Not read when x holds the whole location. |
| `precision` | float | `3` | How close counts as arrived, in meters. |

```text
OgreBotAPI.Movement:Move2AreaNoTarget[${Me.Name},100,20,-250,3]
```

*Was (OldBot):* `OgreBotAPI:Move2AreaNoTarget`

### `NavStop`

`OgreBotAPI.Movement:NavStop[fw]`

Stops the nav trip under way, unless that trip belongs to an encounter. Does nothing when no trip is running.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Movement:NavStop[${Me.Name}]
```

### `NavTo`

`OgreBotAPI.Movement:NavTo[fw, x, y, z, mode=walk]`

Starts a nav trip over the navmesh to the location, replacing any trip under way; it waits while OgreBot is paused and stops when OgreBot closes. It leaves an encounter's trip alone and prints a line saying so, a missing x, y or z or one that is not a number prints an error, and a trip that cannot start prints why.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `x` | float or name |  | X of the location, or the whole location as one word: the name of a point of interest in this zone, or x,y,z. An unknown name prints one line and does nothing. |
| `y` | float |  | Y (height) of the location. Not read when x holds the whole location. |
| `z` | float |  | Z of the location. Not read when x holds the whole location. |
| `mode` | string | `walk` | fly to fly there; any other word walks. |

```text
OgreBotAPI.Movement:NavTo[${Me.Name},100,20,-250,walk]
```

*Was (OldBot):* `call Obj_OgreUtilities.NavTo`, `call Obj_OgreUtilities.NavToLoc`

### `SetRunMode`

`OgreBotAPI.Movement:SetRunMode[fw, run]`

Sets running (TRUE) or walking (FALSE), pressing the game's run toggle only when the current mode is the other one. A blank value, or a word that is not yes or no, prints a line and changes nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `run` | bool |  | TRUE to run, FALSE to walk. Required. |

```text
OgreBotAPI.Movement:SetRunMode[${Me.Name},TRUE]
```

*Was (OldBot):* `OgreBotAPI:RunWalk`

### `Stand`

`OgreBotAPI.Movement:Stand[fw]`

Stands you up when you are feigning death. Does nothing otherwise.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Movement:Stand[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Stand`

### `Stop`

`OgreBotAPI.Movement:Stop[fw]`

Stops the move in progress right away and lets go of the movement keys. Follow, the camp spot or a nav trip can start a new move on their next pulse, so use Movement:Block to keep a character still.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Movement:Stop[${Me.Name}]
```

### `StopFollow`

`OgreBotAPI.Movement:StopFollow[fw]`

Pauses follow (the leader is kept), stops the game's /follow and stops the move in progress right away. LetsGo, JoustIn or a new Movement:Follow resumes follow, and the camp spot still pulls the character back.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Movement:StopFollow[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:HoldUp`, `OgreBotAPI:NoMove`

### `StopJumpRoute`

`OgreBotAPI.Movement:StopJumpRoute[fw]`

Stops the jump route that is running. Does nothing when none is running.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Movement:StopJumpRoute[${Me.Name}]
```

*Was (OldBot):* `Obj_CampSpotJump:Stop`

### `ToLoc`

`OgreBotAPI.Movement:ToLoc[fw, x, y, z, precision=0]`

Runs straight to the location and stops once within the precision, measured flat (X and Z); it returns at once and the move carries on in the background, with OgreBot closed too (Movement:Stop ends it). A missing x, y or z, or one that is not a number, prints an error and does nothing, and the move does not hold the camp spot, so a character with a camp spot can walk back afterwards.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `x` | float or name |  | X of the location, or the whole location as one word: the name of a point of interest in this zone, or x,y,z. An unknown name prints one line and does nothing. |
| `y` | float |  | Y (height) of the location. Not read when x holds the whole location. |
| `z` | float |  | Z of the location. Not read when x holds the whole location. |
| `precision` | float | `0` | How close counts as arrived, in meters. 0 or blank uses 2. |

```text
OgreBotAPI.Movement:ToLoc[${Me.Name},100,20,-250,3]
```

### `Unblock`

`OgreBotAPI.Movement:Unblock[fw, reason]`

Releases the named movement block and leaves any others in place. A reason that is not held does nothing; a blank reason prints a line.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `reason` | string |  | The block name given to Movement:Block. Case-sensitive. |

```text
OgreBotAPI.Movement:Unblock[${Me.Name},MyScript]
```

*Was (OldBot):* `Obj_CampSpot:Enable`, `Obj_Movement:Enable`, `Ogre_CampSpot:Enable`

### `UseWithoutOgreBot`

`OgreBotAPI.Movement:UseWithoutOgreBot[fw, 1|0=0]`

Lets Come2Me, Move2Area, follow and the camp spot move the character while OgreBot is not open (1 or TRUE), or puts back the need for OgreBot to be open (0 or FALSE). Left blank it turns the option off, a word that is not yes or no leaves it as it is, and it lasts until the session ends.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `1\|0` | bool | `0` | 1 or TRUE to allow movement without OgreBot open; 0 or FALSE to require OgreBot. |

```text
OgreBotAPI.Movement:UseWithoutOgreBot[${Me.Name},1]
```

### `Waypoint`

`OgreBotAPI.Movement:Waypoint[fw, x, y, z]`

Sends the game's /waypoint command for the location, which shows the in-game waypoint trail to it. A missing x, y or z prints an error and does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `x` | float or name |  | X of the location, or the whole location as one word: the name of a point of interest in this zone, or x,y,z. An unknown name prints one line and does nothing. |
| `y` | float |  | Y (height) of the location. Not read when x holds the whole location. |
| `z` | float |  | Z of the location. Not read when x holds the whole location. |

```text
OgreBotAPI.Movement:Waypoint[${Me.Name},100,20,-250]
```

*Was (OldBot):* `OgreBotAPI:Waypoint`
