# OgreBotAPI.Position

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Members

### `ActorModelSize`

`${OgreBotAPI.Position.ActorModelSize[nameOrId]}`

Returns an actor's model size: its collision radius times its collision scale. Returns 0 when the argument is blank or the actor cannot be found.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `nameOrId` | string |  | the actor: an actor id, an @alias or *alias, pet:&lt;owner>, a class word (the first group or raid member it fits) me or your own name (you), or a name (the nearest actor whose name contains it) |

**Returns:** float: the actor's collision radius times its collision scale; 0 when it is not found.

```text
echo ${OgreBotAPI.Position.ActorModelSize[${Target.ID}]}
```

*Was (OldBot):* `OgreBotAPI.GetActorModelSize`

### `AtAngle`

`${OgreBotAPI.Position.AtAngle[angle,actorNameOrId,dist=3]}`

Returns the point at angle degrees around an actor, measured from the actor's heading, dist plus your model size plus the actor's model size away, at the actor's height plus 0.5. Returns "" when the actor cannot be found; it only computes a point and moves nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `angle` | int |  | whole degrees around the actor from its heading: 0 is directly behind it and 180 directly in front, 90 and -90 its two sides (a fraction is dropped) |
| `actorNameOrId` | string |  | the actor: an actor id, an @alias or *alias, pet:&lt;owner>, a class word (the first group or raid member it fits) me or your own name (you), or a name (the nearest actor whose name contains it) |
| `dist` | float | `3` | the gap between the two bodies, before the model sizes are added |

**Returns:** string: "x,y,z" with two decimals; "" when the actor is not found.

```text
echo ${OgreBotAPI.Position.AtAngle[90,${Target.ID},5]}
```

*Was (OldBot):* `OgreBotAPI.PointAtAngle`

### `AtAngleNoTargetSize`

`${OgreBotAPI.Position.AtAngleNoTargetSize[angle,actorNameOrId,dist=3]}`

Same as Position.AtAngle, but the distance adds only your own model size, not the actor's. Returns "" when the actor cannot be found.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `angle` | int |  | whole degrees around the actor from its heading: 0 is directly behind it and 180 directly in front, 90 and -90 its two sides (a fraction is dropped) |
| `actorNameOrId` | string |  | the actor: an actor id, an @alias or *alias, pet:&lt;owner>, a class word (the first group or raid member it fits) me or your own name (you), or a name (the nearest actor whose name contains it) |
| `dist` | float | `3` | the distance before your model size is added |

**Returns:** string: "x,y,z" with two decimals; "" when the actor is not found.

```text
echo ${OgreBotAPI.Position.AtAngleNoTargetSize[180,${Target.ID},3]}
```

*Was (OldBot):* `OgreBotAPI.PointAtAngleNoSize`

### `DistanceToActor`

`${OgreBotAPI.Position.DistanceToActor[nameOrId=Target]}`

Returns your distance to an actor as the game reports it (the actor's Distance), using your current target when no actor is given. Returns -1 when the actor cannot be found or you are not in the world.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `nameOrId` | string | `Target` | the actor: an actor id, an @alias or *alias, pet:&lt;owner>, a class word (the first group or raid member it fits) me or your own name (you), or a name (the nearest actor whose name contains it); blank = your current target |

**Returns:** float: the distance to the actor; -1 when it is not found or you are not in the world.

```text
echo ${OgreBotAPI.Position.DistanceToActor[${Target.ID}]}
```

*Was (OldBot):* `OgreBotAPI.GameDistanceToActor`

### `FarthestActorFrom`

`${OgreBotAPI.Position.FarthestActorFrom[anchorNameOrId,actorName,minDist=20]}`

Returns the id of the actor named exactly actorName (any case) that is farthest, in straight-line 3D distance, from an anchor actor, as long as it is more than minDist away. Returns 0 when the anchor or no actor of that name is found, or when even the farthest one is not past minDist.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `anchorNameOrId` | string |  | the actor to measure from: an actor id, an @alias or *alias, pet:&lt;owner>, a class word or a name (the nearest actor whose name contains it) |
| `actorName` | string |  | the full name of the actors to choose among (whole-name match, any case) |
| `minDist` | float | `20` | the winner must be farther than this from the anchor, or the answer is 0 |

**Returns:** int64: the chosen actor's id; 0 when there is none.

```text
echo ${OgreBotAPI.Position.FarthestActorFrom[${Target.ID},"a void tentacle",20]}
```

*Was (OldBot):* `OgreBotAPI.GetFarthestActorFrom`, `OgreBotAPI.GetFarthestActorFrom_ref`

### `FarthestGroupDistance`

`${OgreBotAPI.Position.FarthestGroupDistance}`

Returns the distance to the farthest other member of your group. Returns 0 when you are solo or not in the world.

**Returns:** float: the largest distance from you to another group member; 0 when there is none.

```text
echo ${OgreBotAPI.Position.FarthestGroupDistance}
```

*Was (OldBot):* `OgreBotAPI.GetFarthestGroupDistance`, `Obj_OgreUtilities.GroupWithinDistance`

### `MyModelSize`

`${OgreBotAPI.Position.MyModelSize}`

Returns your model size: your collision radius times your collision scale, the body edge the bot adds to its distances.

**Returns:** float: your collision radius times your collision scale.

```text
echo ${OgreBotAPI.Position.MyModelSize}
```

*Was (OldBot):* `OgreBotAPI.GetMyModelSize`

### `Toward`

`${OgreBotAPI.Position.Toward[fx,fy,fz,tx,ty,tz,dist=15]}`

Returns the point dist away from the first point in the direction of the second, measured flat (x and z only), with the second point's y. It does not stop at the second point when dist is longer than the gap, and returns "" when fewer than six coordinates are given.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fx` | float |  | the starting point's x |
| `fy` | float |  | the starting point's y (not used in the result) |
| `fz` | float |  | the starting point's z |
| `tx` | float |  | the point to head toward, x |
| `ty` | float |  | the point to head toward, y (becomes the result's y) |
| `tz` | float |  | the point to head toward, z |
| `dist` | float | `15` | how far from the starting point to go |

**Returns:** string: "x,y,z" with two decimals; "" when fewer than six coordinates are given.

```text
echo ${OgreBotAPI.Position.Toward[${Me.X},${Me.Y},${Me.Z},${Target.X},${Target.Y},${Target.Z},10]}
```

*Was (OldBot):* `OgreBotAPI.PointTowardDist`
