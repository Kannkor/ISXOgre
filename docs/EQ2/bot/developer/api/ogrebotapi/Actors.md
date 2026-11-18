<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# OgreBotAPI.Actors

## Members

### `CountByName`

`${OgreBotAPI.Actors.CountByName[name,...]}`

Counts the actors around you with this name, an exact match in any case unless -partial is given. Optional flags narrow it by distance and type, and the count is 0 when nothing matches.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | string |  | the actor name to count; case does not matter |
| `...` | flags |  | any of: -partial (or -substring) to count names that contain the text; -distance F to count only actors within F (999 or more means no limit, the default); -Type S to count only actors whose Type is S, any case |

**Returns:** int: how many actors match; 0 when none do.

```text
echo ${OgreBotAPI.Actors.CountByName["a gnoll",-partial,-distance,30]}
```

*Was (OldBot):* `OgreBotAPI.GetActorCountByName`

### `CountByType`

`${OgreBotAPI.Actors.CountByType[type,-distance,distance]}`

Counts the actors of one Type (NPC, NamedNPC, PC, Corpse and so on, any case), optionally only those within a distance; the type may be a lone word or follow -Type, and each flag and its value are separate arguments. With no type given it counts Type Special, and PC never counts you, because your own Type is Me.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `type` | string | `Special` | the actor Type to count, any case; -Type and then the type works the same |
| `-distance` | string |  | the word -distance, when a distance follows it |
| `distance` | float | `999` | count only actors within this distance; 999 or more means no limit |

**Returns:** int: how many actors of that type are in range; 0 when none are.

```text
echo ${OgreBotAPI.Actors.CountByType[NPC,-distance,20]}
```

*Was (OldBot):* `OgreBotAPI.GetActorCountByType`

### `IsPC`

`${OgreBotAPI.Actors.IsPC[actorType]}`

Tells you whether an actor Type word means a player character. Pass the actor's Type, not its name or id.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `actorType` | string |  | an actor's Type, such as the value of ${Target.Type} |

**Returns:** bool: TRUE when the type is Me or PC (any case); FALSE for anything else.

```text
echo ${OgreBotAPI.Actors.IsPC[${Target.Type}]}
```

*Was (OldBot):* `OgreBotAPI.IsAPC`

### `MobID`

`${OgreBotAPI.Actors.MobID[name]}`

Returns the id of the nearest actor whose name matches exactly, in any case. A number is handed back only when that actor is here, and the usual target words (@ aliases, pet:&lt;owner>, a class word for a group or raid member) are understood too.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | string |  | the actor's full name, or an actor id |

**Returns:** int64: the actor id; 0 when no actor matches, the name is blank or that id is not here.

```text
echo ${OgreBotAPI.Actors.MobID["a goblin scout"]}
```

*Was (OldBot):* `GetInfoOb.ActorToID`, `GetInfoOb.GetMobID`, `Obj_OgreIH.Get_NPC_ID`

### `NPCsWithin`

`${OgreBotAPI.Actors.NPCsWithin[distance]}`

Counts the living NPCs and named NPCs within the distance, aggro or not, measured edge to edge: your own model size and each mob's size widen the reach, as an area spell around you does. A distance of 0 or less counts nothing and prints a console warning.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `distance` | float |  | the radius around you, above 0 |

**Returns:** int: how many living NPCs and named NPCs are in reach; 0 when none are, when the distance is not above 0, or when the actor list is not ready yet.

```text
echo ${OgreBotAPI.Actors.NPCsWithin[10]}
```

*Was (OldBot):* `OgreBotAPI.NPCsWithinRange`

## Methods

### `ApplyVerb`

`OgreBotAPI.Actors:ApplyVerb[fw, actor, verb]`

Applies a verb at once to the actor whose id you give, else the nearest one whose name contains the text, or of that type when the text is a type word, using the game's apply_verb command. A blank actor or verb gets one line, and so does an actor that does not match.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `actor` | string |  | the actor's name or part of it, any case, its actor id, or a type word: npc, namednpc, nokillnpc, pc, special, chest, resource, door |
| `verb` | string |  | the verb as it shows on the actor's right-click menu |

```text
OgreBotAPI.Actors:ApplyVerb[igw:${Me.Name},"Strange Device","Use"]
```

*Was (OldBot):* `OgreBotAPI:ApplyVerbForWho`, `OgreBotAPI:ApplyVerbIDForWho`, `OgreBotAPI:ApplyVerb`

### `ApplyVerbQueued`

`OgreBotAPI.Actors:ApplyVerbQueued[fw, actor, verb, waitDs=40]`

Queues a verb on the actor whose id you give, else the nearest one whose name contains the text, or of that type when the text is a type word, then waits out the cast it starts, exactly as ApplyVerbIDQueued does. The actor is looked up when you call it; a blank actor or verb, or no match, gets one line and queues nothing, and one gone by its turn is dropped with a console line.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `actor` | string |  | the actor's name or part of it, any case, its actor id, or a type word: npc, namednpc, nokillnpc, pc, special, chest, resource, door |
| `verb` | string |  | the verb as it shows on the actor's right-click menu |
| `waitDs` | int | `40` | the longest wait for the cast to end, in tenths of a second |

```text
OgreBotAPI.Actors:ApplyVerbQueued[igw:${Me.Name},"Strange Device","Use"]
```

*Was (OldBot):* `OgreBotAPI:ApplyVerbIDQueuedForWho`, `OgreBotAPI:ApplyVerbQueuedForWho`

### `Click`

`OgreBotAPI.Actors:Click[fw, nameOrId, ...]`

Double-clicks an actor at once: an id as given, or else the nearest interactable actor whose name contains the text (or matches it exactly when the third argument is TRUE). Nothing happens, with no message, when no actor is found.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `nameOrId` | string |  | an actor id, or a name to search for among interactable actors |
| `...` | bool |  | exact: TRUE matches the whole name (any case) instead of any name containing it; default FALSE |

```text
OgreBotAPI.Actors:Click[${Me.Name},"Strange Lever"]
```

*Was (OldBot):* `OgreBotAPI:Actor_Click`, `call Obj_OgreUtilities.HandleClickActor`

### `ClickQueued`

`OgreBotAPI.Actors:ClickQueued[fw, nameOrId, ...]`

Queues a double-click on an actor found the same way as Click, then waits out the cast the click starts. At its turn it waits up to 5 seconds for a free cast bar, clicks once, and holds the cast bar until that cast ends or the wait runs out; an actor gone by then is dropped with a console line.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `nameOrId` | string |  | an actor id, or a name to search for among interactable actors |
| `...` | bool, int |  | exact, then waitDs: exact TRUE matches the whole name instead of any name containing it (default FALSE); waitDs is the longest wait for the cast to end, in tenths of a second (default 40) |

```text
OgreBotAPI.Actors:ClickQueued[${Me.Name},"Ancient Altar",FALSE,60]
```

*Was (OldBot):* `OgreBotAPI:Actor_ClickQueued`, `OgreBotAPI:AltarOfTheAncients`, `OgreBotAPI:TargetAndDoubleClickActor`

### `Hail`

`OgreBotAPI.Actors:Hail[fw, nameOrId]`

Queues a hail: target the actor, face it, then hail, about 0.3 seconds apart, and the hail is abandoned if the target does not change to that actor within 1 second. A blank or 0 hails the nearest nokill NPC within 10 (nothing happens when there is none); a name that finds nobody, or an id that is not here, says so on the console and hails nobody.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `nameOrId` | string |  | an actor id, a name (any actor whose name contains it, nearest first), an @ alias or pet:&lt;owner>; blank or 0 uses the nokill NPC fallback |

```text
OgreBotAPI.Actors:Hail[${Me.Name},${Target.ID}]
```

*Was (OldBot):* `OgreBotAPI:HailNPC`, `call Obj_OgreUtilities.DoHail`, `call Obj_OgreUtilities.DoHailID`

### `SetCastMonitoring`

`OgreBotAPI.Actors:SetCastMonitoring[fw, -watch "<mob>" ..., -unwatch "<mob>, -clear, -radius N]`

Adds or removes the mob names this script asks NPC cast monitoring to watch, or sets the scan radius, for this zone; -watch and -radius also tick NPC Cast Monitoring, and watched mobs in range raise OgreEvent_CastMonitoring_CastingStarted and OgreEvent_CastMonitoring_CastingEnded. Flags run in the order written with one console line each, watches added by the zone or an encounter are never touched, and one bad flag refuses the whole call.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `-watch "<mob>" ...` | string |  | -watch followed by a mob name to watch, matched as a whole name in any case; repeat the pair for more mobs; it ends at the next zone or when NPC Cast Monitoring is unticked, and the tick stays |
| `-unwatch "<mob>` | string |  | -unwatch followed by a mob name to stop watching (only a watch a script added) |
| `-clear` | flag |  | drops every watch scripts added |
| `-radius N` | int |  | -radius followed by the scan radius, a whole number from 5 to 500 (default 50); it beats the zone's own radius and ends at the next zone or when NPC Cast Monitoring is unticked |

```text
OgreBotAPI.Actors:SetCastMonitoring[${Me.Name},-watch,"a ravenous gnoll",-radius,60]
```

*Was (OldBot):* `OgreBotAPI:NPC_CastMonitoring`
