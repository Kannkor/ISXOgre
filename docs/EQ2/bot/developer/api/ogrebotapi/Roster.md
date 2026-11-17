# OgreBotAPI.Roster

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Members

### `ArchetypeOf`

`${OgreBotAPI.Roster.ArchetypeOf[class]}`

The archetype of a subclass name, in lower case: fighter, priest, mage or scout. An actor ID is also accepted and that actor's class is used; a class tier name such as warrior, or anything unknown, reads an empty string.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `class` | string |  | A subclass name such as templar (any case), or an actor ID. |

**Returns:** string - fighter, priest, mage or scout, empty when unknown.

```text
echo ${OgreBotAPI.Roster.ArchetypeOf[${Target.ID}]}
```

*Was (OldBot):* `ClassInfo.Archetype`, `GetArchetypeFromClass`, `GetInfoOb.Archetype`

### `BaseClassOf`

`${OgreBotAPI.Roster.BaseClassOf[class]}`

The class tier of a subclass name, in lower case: templar reads cleric, berserker reads warrior. An actor ID is also accepted and that actor's class is used; anything that is not a subclass reads an empty string.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `class` | string |  | A subclass name such as berserker (any case), or an actor ID. |

**Returns:** string - the class tier (warrior, cleric, bard and so on), empty when unknown.

```text
echo ${OgreBotAPI.Roster.BaseClassOf[berserker]}
```

*Was (OldBot):* `GetInfoOb.GetBaseClass`, `GetInfoOb.GetClass`, `OgreBotAPI.Get_BaseClass`

### `CountGroupBy`

`${OgreBotAPI.Roster.CountGroupBy[mode,search]}`

Counts the members of your group, you included, that match mode and search. Only player characters count: a member whose type reads as anything else (a corpse, for example) is skipped; with no mode it matches by Class, and a mode word the list does not know matches nobody.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `mode` | string | `Class` | How to match: All (everyone; search ignored), Class (exact subclass, e.g. templar), RawClass or ParentClass (class tier, e.g. cleric), Archetype, NotArchetype, Role (tank, priest, enchanter, bard, dps), Cursed (search ignored), KraletusCharmers (coercers and troubadors, search ignored). Empty means Class; any other word matches nobody. |
| `search` | string |  | The class, tier, archetype or role name to match, any case. |

**Returns:** int - number of matching group members, 0 when none match.

```text
echo ${OgreBotAPI.Roster.CountGroupBy[Archetype,priest]}
```

*Was (OldBot):* `OgreBotAPI.CountGroupBy`, `GetInfoOb.CountGroupBy_`, `CheckGroupSetup`

### `CountRaidBy`

`${OgreBotAPI.Roster.CountRaidBy[mode,search]}`

Counts the members of your raid, you included, that match mode and search; in a raid every member counts, corpses too. When you are not in a raid it answers exactly as CountGroupBy does.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `mode` | string | `Class` | How to match: All, Class, RawClass or ParentClass, Archetype, NotArchetype, Role, Cursed, KraletusCharmers. Empty means Class; any other word matches nobody. |
| `search` | string |  | The class, tier, archetype or role name to match, any case. |

**Returns:** int - number of matching raid members (group members when not in a raid).

```text
echo ${OgreBotAPI.Roster.CountRaidBy[Role,priest]}
```

*Was (OldBot):* `OgreBotAPI.CountRaidBy`, `GetInfoOb.CountRaidBy_`

### `Flagged`

`${OgreBotAPI.Roster.Flagged[n=1]}`

TRUE when flag number n is set on this character. Flags are kept by this session only, are set with Roster:Flag, and can be read anywhere, even outside the world; flag 24 is the same state as Marked.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `n` | int | `1` | The flag number to check. |

**Returns:** bool - TRUE when flag n is set.

```text
echo ${OgreBotAPI.Roster.Flagged[2]}
```

*Was (OldBot):* `GetInfoOb.FlaggedToon`, `GetInfoOb:ToonFlagged`, `OgreBotAPI.ToonFlagged`

### `GroupIDBy`

`${OgreBotAPI.Roster.GroupIDBy[mode,search,rank=1]}`

The actor ID of the rank-th group member, you included, that matches mode and search, with matches sorted alphabetically by name. Only player characters are considered (a corpse is skipped); reads 0 when nobody matches or rank is past the last match.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `mode` | string | `Class` | How to match: All, Class, RawClass or ParentClass, Archetype, NotArchetype, Role, Cursed, KraletusCharmers. Empty means Class; any other word matches nobody. |
| `search` | string |  | The class, tier, archetype or role name to match, any case. |
| `rank` | int | `1` | Which match to return, counting from 1 in name order. |

**Returns:** int64 - the member's actor ID, 0 when there is no such match.

```text
echo ${OgreBotAPI.Roster.GroupIDBy[Class,templar,1]}
```

*Was (OldBot):* `OgreBotAPI.GetGroupIDBy`, `GetInfoOb.GetGroupIDBy_`

### `GroupIDPreferred`

`${OgreBotAPI.Roster.GroupIDPreferred[search,rank=1]}`

The actor ID of the rank-th group member, you included, whose archetype or role matches search, ordered by how useful that class is to spare (for dps the order is flipped so pure damage classes come first). Only player characters are considered (a corpse is skipped), a member matching any of the listed pools counts, ties go to the pool listed first and then to name, and it reads 0 when nobody matches.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `search` | string |  | One or more archetypes or roles separated by \|, for example scout, dps or scout\|mage. |
| `rank` | int | `1` | Which match to return, counting from 1 in preferred order. |

**Returns:** int64 - the member's actor ID, 0 when there is no such match.

```text
echo ${OgreBotAPI.Roster.GroupIDPreferred[scout|mage,1]}
```

*Was (OldBot):* `GetInfoOb.GetGroupIDPreferred_`, `OgreBotAPI.GetGroupIDPreferred`

### `GroupNameBy`

`${OgreBotAPI.Roster.GroupNameBy[mode,search,rank=1]}`

The name of the rank-th group member, you included, that matches mode and search, with matches sorted alphabetically by name. Only player characters are considered (a corpse is skipped), as in GroupIDBy, so the same rank names the same member in both; reads an empty string when nobody matches or rank is past the last match.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `mode` | string | `Class` | How to match: All, Class, RawClass or ParentClass, Archetype, NotArchetype, Role, Cursed, KraletusCharmers. Empty means Class; any other word matches nobody. |
| `search` | string |  | The class, tier, archetype or role name to match, any case. |
| `rank` | int | `1` | Which match to return, counting from 1 in name order. |

**Returns:** string - the member's name, empty when there is no such match.

```text
echo ${OgreBotAPI.Roster.GroupNameBy[Class,templar,1]}
```

*Was (OldBot):* `GetInfoOb.GetGroupInformation`, `GetInfoOb.GetGroupNameBy_`, `OgreBotAPI.GetGroupNameBy`

### `GroupNamePreferred`

`${OgreBotAPI.Roster.GroupNamePreferred[search,rank=1]}`

The name of the rank-th group member, you included, whose archetype or role matches search, in the same preferred order as GroupIDPreferred, so the same rank names the same member in both (a corpse is skipped). search can list several pools with \|; reads an empty string when nobody matches.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `search` | string |  | One or more archetypes or roles separated by \|, for example scout, dps or scout\|mage. |
| `rank` | int | `1` | Which match to return, counting from 1 in preferred order. |

**Returns:** string - the member's name, empty when there is no such match.

```text
echo ${OgreBotAPI.Roster.GroupNamePreferred[dps,1]}
```

*Was (OldBot):* `GetInfoOb.GetGroupNamePreferred_`, `OgreBotAPI.GetGroupNamePreferred`

### `GroupSize`

`${OgreBotAPI.Roster.GroupSize}`

How many people are in your group, counting you, so a solo character reads 1. Reads NULL when you are not in the world.

**Returns:** int - group members including you.

```text
echo ${OgreBotAPI.Roster.GroupSize}
```

### `GuildFlagLocation`

`${OgreBotAPI.Roster.GuildFlagLocation}`

The text the game shows for your guild's flag location. Reads NULL when you are not in the world, and an empty string when the game has no value.

**Returns:** string - the guild flag location as the game labels it.

```text
echo ${OgreBotAPI.Roster.GuildFlagLocation}
```

*Was (OldBot):* `OgreBotAPI.GuildFlagLocation`

### `InEQ2Chars`

`${OgreBotAPI.Roster.InEQ2Chars[speaker,fullAccountOnly=FALSE]}`

TRUE when speaker is on the list the chat commands trust: every character saved in your account list, on any account (characters not yet assigned to one included), and the name OgreIRCSession, matched in any case. With fullAccountOnly TRUE it is TRUE only when that character also has complete account details saved, the kind a login needs; it works outside the world.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `speaker` | string |  | The character name to look up. |
| `fullAccountOnly` | bool | `FALSE` | TRUE to require complete saved account details for that character, not just its name on the list. |

**Returns:** bool - TRUE when the name is on that list.

```text
echo ${OgreBotAPI.Roster.InEQ2Chars[${Target.Name}]}
```

*Was (OldBot):* `OgreBotAPI.InEQ2Chars`

### `InRaid`

`${OgreBotAPI.Roster.InRaid}`

TRUE when you are in a raid. Reads NULL when you are not in the world (character select, zoning).

**Returns:** bool - TRUE in a raid, FALSE otherwise.

```text
echo ${OgreBotAPI.Roster.InRaid}
```

### `InZone`

`${OgreBotAPI.Roster.InZone[within=0]}`

TRUE when every other member of your group is in this zone and alive, and, when within is above 0, no farther away than within. Solo reads TRUE, outside the world reads FALSE; it checks your group only, never the rest of a raid.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `within` | float | `0` | The farthest a member may be from you. 0 skips the distance check. |

**Returns:** bool - TRUE when the whole group is here.

```text
echo ${OgreBotAPI.Roster.InZone[50]}
```

*Was (OldBot):* `GetInfoOb.GroupInZone`, `OgreBotAPI.GroupInZone`, `call Obj_OgreUtilities.CheckIfGroupInSameZone`

### `IsGroupLeader`

`${OgreBotAPI.Roster.IsGroupLeader}`

TRUE when you lead your group, and also TRUE when you are solo. Reads NULL when you are not in the world.

**Returns:** bool - TRUE when you are the group leader or solo.

```text
echo ${OgreBotAPI.Roster.IsGroupLeader}
```

*Was (OldBot):* `OgreBotAPI.IsGroupLeader`

### `Marked`

`${OgreBotAPI.Roster.Marked}`

TRUE when this character is marked (set with Roster:Mark). Marked is flag 24, so Flagged[24] reads the same thing; it can be read anywhere, even outside the world.

**Returns:** bool - TRUE when this character is marked.

```text
echo ${OgreBotAPI.Roster.Marked}
```

*Was (OldBot):* `GetInfoOb.ToonMarked`

### `NearestOfClass`

`${OgreBotAPI.Roster.NearestOfClass[class,range=50,scope=auto,includeMe=TRUE]}`

The actor ID of a group or raid member of the given class who is within range, or 0 when there is none. A match is the subclass, its class tier or its archetype (warrior finds a berserker, fighter finds any fighter); you are checked first and returned with no distance test when includeMe is TRUE, then the closest member in range wins.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `class` | string |  | A subclass, class tier or archetype name, any case. Empty reads 0. |
| `range` | float | `50` | The farthest a member may be. Members whose distance reads 0 are never matched. |
| `scope` | string | `auto` | auto (your raid when in one, else your group), raid, or any other word for your group. |
| `includeMe` | bool | `TRUE` | TRUE to answer with your own ID when your class matches. |

**Returns:** int64 - the matching member's actor ID, 0 when none is in range.

```text
echo ${OgreBotAPI.Roster.NearestOfClass[priest,30,auto,FALSE]}
```

*Was (OldBot):* `GetInfoOb.Class`

### `RaidIDBy`

`${OgreBotAPI.Roster.RaidIDBy[mode,search,rank=1]}`

The actor ID of the rank-th raid member, you included, that matches mode and search, sorted alphabetically by name; in a raid every member is considered, corpses too. When you are not in a raid it answers exactly as GroupIDBy does, and it reads 0 when nobody matches.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `mode` | string | `Class` | How to match: All, Class, RawClass or ParentClass, Archetype, NotArchetype, Role, Cursed, KraletusCharmers. Empty means Class; any other word matches nobody. |
| `search` | string |  | The class, tier, archetype or role name to match, any case. |
| `rank` | int | `1` | Which match to return, counting from 1 in name order. |

**Returns:** int64 - the member's actor ID, 0 when there is no such match.

```text
echo ${OgreBotAPI.Roster.RaidIDBy[Archetype,priest,2]}
```

*Was (OldBot):* `GetInfoOb.GetRaidIDBy_`, `OgreBotAPI.GetRaidIDBy`

### `RaidIDPreferred`

`${OgreBotAPI.Roster.RaidIDPreferred[search,rank=1]}`

The actor ID of the rank-th raid member, you included, whose archetype or role matches search, in preferred order (see GroupIDPreferred). When you are not in a raid it answers exactly as GroupIDPreferred does; reads 0 when nobody matches.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `search` | string |  | One or more archetypes or roles separated by \|, for example scout, dps or scout\|mage. |
| `rank` | int | `1` | Which match to return, counting from 1 in preferred order. |

**Returns:** int64 - the member's actor ID, 0 when there is no such match.

```text
echo ${OgreBotAPI.Roster.RaidIDPreferred[priest,2]}
```

*Was (OldBot):* `GetInfoOb.GetRaidIDPreferred_`, `GetInfoOb:Get_RaidIDsPreferred`, `OgreBotAPI.GetRaidIDPreferred`

### `RaidNameBy`

`${OgreBotAPI.Roster.RaidNameBy[mode,search,rank=1]}`

The name of the rank-th raid member, you included, that matches mode and search, sorted alphabetically by name. When you are not in a raid it answers exactly as GroupNameBy does, and it reads an empty string when nobody matches.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `mode` | string | `Class` | How to match: All, Class, RawClass or ParentClass, Archetype, NotArchetype, Role, Cursed, KraletusCharmers. Empty means Class; any other word matches nobody. |
| `search` | string |  | The class, tier, archetype or role name to match, any case. |
| `rank` | int | `1` | Which match to return, counting from 1 in name order. |

**Returns:** string - the member's name, empty when there is no such match.

```text
echo ${OgreBotAPI.Roster.RaidNameBy[Role,tank,1]}
```

*Was (OldBot):* `GetInfoOb.GetRaidNameBy_`, `OgreBotAPI.GetRaidNameBy`

### `RaidNamePreferred`

`${OgreBotAPI.Roster.RaidNamePreferred[search,rank=1]}`

The name of the rank-th raid member, you included, whose archetype or role matches search, in preferred order (see GroupIDPreferred). When you are not in a raid it answers exactly as GroupNamePreferred does; reads an empty string when nobody matches.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `search` | string |  | One or more archetypes or roles separated by \|, for example scout, dps or scout\|mage. |
| `rank` | int | `1` | Which match to return, counting from 1 in preferred order. |

**Returns:** string - the member's name, empty when there is no such match.

```text
echo ${OgreBotAPI.Roster.RaidNamePreferred[scout|mage,1]}
```

*Was (OldBot):* `GetInfoOb.GetRaidNamePreferred_`, `OgreBotAPI.GetRaidNamePreferred`

### `RaidSize`

`${OgreBotAPI.Roster.RaidSize}`

How many people are in your raid, counting you. Reads 0 when you are not in a raid, and NULL when you are not in the world.

**Returns:** int - raid members including you, 0 when not in a raid.

```text
echo ${OgreBotAPI.Roster.RaidSize}
```

### `RoleOf`

`${OgreBotAPI.Roster.RoleOf[class]}`

The role of a subclass or class tier name, in lower case: tank, priest, enchanter, bard or dps. An actor ID is also accepted and that actor's class is used; anything unknown reads an empty string.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `class` | string |  | A subclass or class tier name such as wizard or sorcerer (any case), or an actor ID. |

**Returns:** string - tank, priest, enchanter, bard or dps, empty when unknown.

```text
echo ${OgreBotAPI.Roster.RoleOf[${Target.ID}]}
```

*Was (OldBot):* `GetInfoOb.GetRole`, `OgreBotAPI.Get_Role`

### `SortGroupByID`

`${OgreBotAPI.Roster.SortGroupByID[mode,search,exclude]}`

Your own position, counting from 1, among the group members that match mode and search, ordered by actor ID read as text (so 100 sorts before 99). Every character in the group gets a different number, which is what makes it useful for picking spots; reads 0 when you do not match yourself.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `mode` | string | `Class` | How to match: All, Class, RawClass or ParentClass, Archetype, NotArchetype, Role, Cursed, KraletusCharmers. Empty means Class; any other word matches nobody. |
| `search` | string |  | The class, tier, archetype or role name to match, any case. |
| `exclude` | string |  | A character name to leave out of the ordering, any case. Empty leaves nobody out. |

**Returns:** int - your 1-based position among the matches, 0 when you are not one of them.

```text
echo ${OgreBotAPI.Roster.SortGroupByID[Archetype,scout]}
```

*Was (OldBot):* `GetInfoOb:Get_GroupIDs`, `GetInfoOb.SortGroupByIDBy_`, `OgreBotAPI.SortGroupByIDBy`

### `SortRaidByID`

`${OgreBotAPI.Roster.SortRaidByID[mode,search,exclude]}`

Your own position, counting from 1, among the raid members that match mode and search, ordered by actor ID read as text. When you are not in a raid it answers exactly as SortGroupByID does; reads 0 when you do not match yourself.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `mode` | string | `Class` | How to match: All, Class, RawClass or ParentClass, Archetype, NotArchetype, Role, Cursed, KraletusCharmers. Empty means Class; any other word matches nobody. |
| `search` | string |  | The class, tier, archetype or role name to match, any case. |
| `exclude` | string |  | A character name to leave out of the ordering, any case. Empty leaves nobody out. |

**Returns:** int - your 1-based position among the matches, 0 when you are not one of them.

```text
echo ${OgreBotAPI.Roster.SortRaidByID[Role,dps]}
```

*Was (OldBot):* `GetInfoOb.SortRaidByIDBy_`, `OgreBotAPI.SortRaidByIDBy`

## Methods

### `CheckMemberLevel`

`OgreBotAPI.Roster:CheckMemberLevel[fw, onlyNonMembers=FALSE]`

Each selected character prints "&lt;name> Membership level: &lt;level>" on the InnerSpace console, using the game's subscription level. With onlyNonMembers TRUE, characters whose level reads Member print nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `onlyNonMembers` | bool | `FALSE` | TRUE to print only for characters that are not Member. |

```text
OgreBotAPI.Roster:CheckMemberLevel[all,TRUE]
```

*Was (OldBot):* `OgreBotAPI:CheckMemberLevel`

### `Disband`

`OgreBotAPI.Roster:Disband[fw]`

Each selected character sends the game's /disband, which takes it out of its group. It needs the character in the world.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.Roster:Disband[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Disband`

### `Flag`

`OgreBotAPI.Roster:Flag[fw, n=1]`

Sets flag number n on each selected character. When the flag was not already set, a line saying so goes to OgreConsole; setting a flag that is already set is silent, a number outside 1 to 24 is refused with a console line, and it works outside the world.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `n` | int | `1` | The flag number to set, 1 to 24. Flag 24 is the same state as Mark. |

```text
OgreBotAPI.Roster:Flag[${Me.Name},2]
```

*Was (OldBot):* `OgreBotAPI:FlagToon`, `GetInfoOb:FlagToon`

### `FlagNextPerson`

`OgreBotAPI.Roster:FlagNextPerson[fw, mark=1, via=any, search..., -GroupOnly]`

Finds the next character after you and tells that character, over IRC and over oc to every session on this PC, to set flag mark on itself. A group goes in actor id order, so every box agrees on who is next, and a raid in slot order; both wrap round, and nothing is sent when nobody passes.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `mark` | int | `1` | The flag number the next person sets. |
| `via` | string | `any` | any, archetype or baseclass: who may be next. Any other word means any. |
| `search...` | string |  | the archetypes or base classes to match; left out, your own |
| `-GroupOnly` | switch |  | use the group even when you are in a raid |

```text
OgreBotAPI.Roster:FlagNextPerson[${Me.Name},3]
```

*Was (OldBot):* `OgreBotAPI:FlagNextPerson`, `OgreBotAPI:FlagToonNextPerson`

### `Invite`

`OgreBotAPI.Roster:Invite[fw, who]`

Each selected character sends a group invite to who; an alias such as @Healer1 is turned into that character's name first. Nobody already in your group or raid is invited (silently); a missing name, or one that is not plain letters, is refused with one line on the InnerSpace console.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `who` | string |  | The character to invite, by name or alias; me means you, who are always skipped. Required. |

```text
OgreBotAPI.Roster:Invite[${Me.Name},${Target.Name}]
```

*Was (OldBot):* `OgreBotAPI:Invite`

### `Inviter`

`OgreBotAPI.Roster:Inviter[fw, toon...]`

Each selected character invites a list of characters in order, about one second apart, skipping anyone already with it; names may also be split by spaces or commas. Put -r (or -ri, -raidinvite) before a name to raid-invite that one; -from, -i and -inviter are not supported here and skip the name after them with a warning, and starting a new list stops one that is still running.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `toon...` | string |  | The names (or aliases) to invite, in order, each optionally led by -r for a raid invite. Any other word starting with - is skipped. |

```text
OgreBotAPI.Roster:Inviter[${Me.Name},${Target.Name}]
```

*Was (OldBot):* `OgreBotAPI:Inviter`

### `Kick`

`OgreBotAPI.Roster:Kick[fw, who]`

Each selected character kicks who from its group; an alias is turned into a name first. A missing name, or one that is not in the group (you are never in the list), prints one line on the InnerSpace console and kicks nobody.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `who` | string |  | The group member to kick, by name or alias. |

```text
OgreBotAPI.Roster:Kick[${Me.Name},${Group[1].Name}]
```

### `MakeLeader`

`OgreBotAPI.Roster:MakeLeader[fw, leader]`

Each selected character that leads its group hands leadership to leader; an alias is turned into a name first. Nothing happens, silently, when leader is the running character, it is not the leader, or leader is not in its group; a missing name, or one that is not plain letters, is refused with one line on the InnerSpace console.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `leader` | string |  | The group member to make leader, by name or alias; me means you, which does nothing. Required. |

```text
OgreBotAPI.Roster:MakeLeader[${Me.Name},${Group[1].Name}]
```

*Was (OldBot):* `OgreBotAPI:MakeLeader`

### `Mark`

`OgreBotAPI.Roster:Mark[fw]`

Marks each selected character, which is the same as setting flag 24. A line goes to OgreConsole when the character was not already marked; it works outside the world.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.Roster:Mark[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:MarkToon`, `GetInfoOb:MarkToon`

### `Mentor`

`OgreBotAPI.Roster:Mentor[fw, name]`

Each selected character mentors the group member name, but only when that member is in its group, is lower level, and neither of them is already mentoring. An alias is turned into a name first; a missing name gets one line, and any other case does nothing, silently.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `name` | string |  | The group member to mentor, by name or alias. Required. |

```text
OgreBotAPI.Roster:Mentor[${Me.Name},${Group[1].Name}]
```

*Was (OldBot):* `Mentor`, `OgreBotAPI:Mentor`

### `RaidInvite`

`OgreBotAPI.Roster:RaidInvite[fw, who]`

Each selected character sends a raid invite to who; an alias is turned into a name first. Nobody already in your raid or your own group is invited (silently); a missing name, or one that is not plain letters, is refused with one line on the InnerSpace console.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `who` | string |  | The character to raid-invite, by name or alias; me means you, who are always skipped. Required. |

```text
OgreBotAPI.Roster:RaidInvite[${Me.Name},${Target.Name}]
```

*Was (OldBot):* `OgreBotAPI:RaidInvite`

### `SetClassValue`

`OgreBotAPI.Roster:SetClassValue[fw, member, value]`

Forces one of the bot's class checks to TRUE or FALSE for each selected character, for example IsFighter TRUE so a non-fighter runs fighter logic, and auto removes the override. The setting lasts until another character is loaded in that session; a missing argument, a member that is not a class name, or a value that is not TRUE, FALSE or auto prints one line on the InnerSpace console and changes nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `member` | string |  | The class check to force: an archetype, class tier or subclass name, with or without Is (IsFighter, Fighter, IsTemplar). |
| `value` | string |  | TRUE or FALSE (yes/no style words also work), or auto to remove the override. |

```text
OgreBotAPI.Roster:SetClassValue[${Me.Name},IsFighter,TRUE]
```

*Was (OldBot):* `OgreBotAPI:ClassInfo_ChangeValue`

### `SpewFlags`

`OgreBotAPI.Roster:SpewFlags[fw]`

Each selected character sends one OgreConsole line per flag it holds, in number order, reading "&lt;name> Flagged &lt;n>". A character with no flags says nothing; it needs the character in the world.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.Roster:SpewFlags[all]
```

*Was (OldBot):* `OgreBotAPI:SpewFlags`, `GetInfoOb:SpewFlags`

### `SpewMarked`

`OgreBotAPI.Roster:SpewMarked[fw, where]`

Each selected character reports whether it is marked, as a line reading "&lt;name> --> Marked: TRUE" (or FALSE), and also raises the stat-report event. The line goes to OgreConsole unless where says otherwise and needs the character in the world; today it always reads FALSE, even for a marked character.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `where` | string |  | oc (OgreConsole), irc, or event (no visible line, only the event). Empty or any other word means oc. |

```text
OgreBotAPI.Roster:SpewMarked[all,oc]
```

*Was (OldBot):* `OgreBotAPI:ToonMarked`

### `Unflag`

`OgreBotAPI.Roster:Unflag[fw, n=1]`

Clears flag number n on each selected character. When the flag was set, a line saying so goes to OgreConsole; clearing a flag that is not set is silent, a number outside 1 to 24 is refused with a console line, and it works outside the world.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `n` | int | `1` | The flag number to clear, 1 to 24. |

```text
OgreBotAPI.Roster:Unflag[all,2]
```

*Was (OldBot):* `OgreBotAPI:UnflagToon`, `GetInfoOb:UnflagToon`

### `UnflagAll`

`OgreBotAPI.Roster:UnflagAll[fw]`

Clears every flag on each selected character, the mark (flag 24) included. One OgreConsole line is written for each flag that was set; nothing is written when none were.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.Roster:UnflagAll[all]
```

*Was (OldBot):* `OgreBotAPI:UnflagAll`, `GetInfoOb:UnflagAll`

### `Unmark`

`OgreBotAPI.Roster:Unmark[fw]`

Removes the mark (flag 24) from each selected character. A line goes to OgreConsole when the character was marked; otherwise it is silent.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.Roster:Unmark[all]
```

*Was (OldBot):* `OgreBotAPI:UnmarkToon`, `GetInfoOb:UnmarkToon`

### `Unmentor`

`OgreBotAPI.Roster:Unmentor[fw]`

Each selected character stops mentoring, but only when its effective level differs from its level; otherwise nothing is sent.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.Roster:Unmentor[all]
```

*Was (OldBot):* `OgreBotAPI:Unmentor`
