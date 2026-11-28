# OgreBotAPI.Quest

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Members

### `ActorHas`

`${OgreBotAPI.Quest.ActorHas[actorId]}`

Whether the actor with this id is within a distance of 10 and offers a quest or has a quest update or hand-in for you. With no id it prints a console line and answers FALSE.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `actorId` | int64 |  | the actor id to check; required |

**Returns:** bool: TRUE when that actor is within 10 and has a quest offer, update or hand-in; FALSE otherwise.

```text
echo ${OgreBotAPI.Quest.ActorHas[${Target.ID}]}
```

*Was (OldBot):* `OgreBotAPI.ActorHasQuest`

### `Have`

`${OgreBotAPI.Quest.Have[name]}`

Whether a quest with this exact name, in any case, is in your active quest journal. No name, or not being in the world, answers FALSE.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `name` | string |  | the full quest name to look for; case does not matter |

**Returns:** bool: TRUE when the quest is in your active journal; FALSE otherwise.

```text
echo ${OgreBotAPI.Quest.Have["Feathers For Sethis"]}
```

*Was (OldBot):* `OgreBotAPI.HaveQuest`, `Obj_OgreIH.Check_Quest_Exists`

## Methods

### `Accept`

`OgreBotAPI.Quest:Accept[fw, questName=""]`

Clicks Accept on an offered new quest window, never a quest reward window, and does nothing when none is offered. It accepts whether or not the Settings Do not auto accept quests box is ticked, since that box stops only the automatic accept; given a name, a group leader with auto share on shares that quest two seconds later.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `questName` | string | `""` | the quest to share after accepting; blank accepts with no share |

```text
OgreBotAPI.Quest:Accept[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:AcceptQuest`, `Obj_OgreUtilities:AcceptQuest`

### `CheckKunarkAscending`

`OgreBotAPI.Quest:CheckKunarkAscending[fw]`

Opens and closes the quest journal, then prints which Kunark Ascending prerequisite quests you have not completed: the languages, the heritage quest, the signature line and an Epic 1.0 quest. It runs in turn on the action queue and ends with a completed line.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Quest:CheckKunarkAscending[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:CheckKunarkAscendingRequirements`

### `CompareUpdate`

`OgreBotAPI.Quest:CompareUpdate[fw, questName, sender]`

Reads your own steps for a quest and asks other characters to compare theirs; a character on a different step says so in its own console and you get a tally. The character that runs it asks, the for-who is who is asked, and all or blank asks the rest of your group.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): which characters are asked; all or blank is your group but you |
| `questName` | string |  | the quest to compare; a missing one prints a console line |
| `sender` | character name |  | the character that asks; the -CompareQuest console line fills it. Leave it out in a script: the character running it asks, and any other name makes the call do nothing |

```text
OgreBotAPI.Quest:CompareUpdate[all,"Feathers For Sethis"]
```

*Was (OldBot):* `OgreBotAPI:CompareQuestUpdate`

### `Delete`

`OgreBotAPI.Quest:Delete[fw, questName]`

Deletes one quest from your own journal straight away and prints the result. There is no group leader check, and a quest that is not in the journal or has moved in it is not deleted.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `questName` | string |  | the exact quest name, any case |

```text
OgreBotAPI.Quest:Delete[${Me.Name},"Feathers For Sethis"]
```

*Was (OldBot):* `OgreBotAPI:DeleteQuest`, `Obj_OgreUtilities:DeleteQuest`, `Obj_OgreUtilities:DeleteQuestActual`

### `ShareAllMissions`

`OgreBotAPI.Quest:ShareAllMissions[fw]`

Shares every active mission in your journal with the group, waiting up to 5 minutes for the group to gather within 30 and then 3 seconds between shares. With all only the group leader shares, and it says so in the console when you are not grouped or have no missions.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Quest:ShareAllMissions[all]
```

*Was (OldBot):* `OgreBotAPI:ShareAllMissions`

### `ShareMission`

`OgreBotAPI.Quest:ShareMission[fw, questName]`

Like :ShareQuest, but the quest must be a mission (its journal category starts with Mission). It says so in the console when it is not an active mission, the name is blank or you are not grouped.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `questName` | string |  | the exact mission name, any case |

```text
OgreBotAPI.Quest:ShareMission[all,"Feathers For Sethis"]
```

*Was (OldBot):* `OgreBotAPI:ShareMission`

### `ShareQuest`

`OgreBotAPI.Quest:ShareQuest[fw, questName]`

Shares one quest from your journal with the group, after waiting up to 5 minutes for the group to gather within 30. With all only the group leader shares, and it says so in the console when the name is blank, the quest is not in your journal or you are not grouped.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `questName` | string |  | the exact quest name, any case |

```text
OgreBotAPI.Quest:ShareQuest[all,"Feathers For Sethis"]
```

*Was (OldBot):* `OgreBotAPI:ShareQuest`

### `ShareQuestWhenAble`

`OgreBotAPI.Quest:ShareQuestWhenAble[fw, questName, zoneName]`

Shares one quest once the group has gathered (waiting up to 5 minutes), but only while you are in zoneName - leaving that zone first stops the share with a console line. With all only the group leader shares.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `questName` | string |  | the exact quest name, any case |
| `zoneName` | string |  | the zone the share is for; blank means the zone you are in now |

```text
OgreBotAPI.Quest:ShareQuestWhenAble[all,"Feathers For Sethis","${Zone.Name}"]
```

*Was (OldBot):* `OgreBotAPI:ShareQuestWhenAble`

### `ShowMissionInfo`

`OgreBotAPI.Quest:ShowMissionInfo[fw]`

Opens the Zone Reuse window's Hot Zones tab and prints one line to the console: the newest expansion's hot zone (each zone named once, without [Heroic] / [Solo]) and the time until it changes, or that the game's list has just expired. It runs on every addressed character, with no group leader check.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Quest:ShowMissionInfo[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:DisplayEtherealMissionInfo`

### `ShowWiki`

`OgreBotAPI.Quest:ShowWiki[fw, name=""]`

Opens the EverQuest 2 wiki page for a quest in your web browser; a blank name uses the quest selected in the quest journal, and with none selected a console line says so and nothing opens. A blank for-who means is1 here, not all.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `name` | string | `""` | the quest to look up; blank uses the quest selected in the journal |

```text
OgreBotAPI.Quest:ShowWiki[${Me.Name},"Feathers For Sethis"]
```

*Was (OldBot):* `OgreBotAPI:ShowWikiForQuest`

### `SpewMissionTimers`

`OgreBotAPI.Quest:SpewMissionTimers[fw, ...searches]`

Opens the quest journal on its Mission Timers tab and sends one oc line per mission whose name contains a search word, with the time to reset and whether it is completed. With no search word it prints a reminder and nothing else, and it closes the journal when done.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `...searches` | string |  | one or more words; a mission matches when its name contains any of them, in any case |

```text
OgreBotAPI.Quest:SpewMissionTimers[${Me.Name},Weekly,Daily]
```

*Was (OldBot):* `OgreBotAPI:Spew_MissionTimerInfo`
