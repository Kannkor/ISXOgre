# Encounter recording format, version 1

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../index.md).
</div>

> This page is made from the recorder's own tables each time the bot is built, so it says exactly what the
> recorder writes - no more and no less.

A recording is one file per box per fight. The file is JSON lines: one row a line, written as it happens, in the
order it happened on that box. The first row is the `header`. A file is whole at every moment - nothing is kept
back for the end of the fight.

One pull of a named is one folder, and a named's pulls share that named's folder:
`OgreSave/EQ2/EncounterRecorder/<Zone>/<Named>/<date and time>/<Toon>.jsonl`. A pull with no named is NOT
written unless "Record trash pulls" is switched on; it is then under
`<Zone>/_Trash/<date and time> <an NPC of it>/`. A recording begun by hand with nothing engaged is under
`<Zone>/_Event/`. The date and time in a folder's name are the PC's local time; the UTC start is in every header
(`utcMs`) and in the pull's `fight.json`. A named's folder holds `encounter.json`: every named its pulls have had.
A folder whose name begins with `_` is never a named's.

## Every row

| Field | Holds | What it is | Published copy |
|---|---|---|---|
| `t` | a whole number | ms since the recording began on this box (the header's utcMs is t = 0) | keep |
| `k` | text | the kind of row | keep |

A field may be left out of a row; a row never carries a field its kind does not list.

## The kinds of row

### `header`

- `header`: the file's first row: who recorded it, where, and when t = 0 was

| Field | Holds | What it is | Published copy |
|---|---|---|---|
| `v` | a whole number | the format version | keep |
| `toon` | text | the character that recorded this file | actorName |
| `class` | text | its class | game |
| `meId` | a whole number | its actor id in this zone - the id its own rows carry | actor |
| `zone` | text | the zone's name exactly as the game gives it | game |
| `zoneShort` | text | the zone's short name | game |
| `utcMs` | a whole number | the UTC time of t = 0, in ms since 1970 | drop |
| `pc` | text | a tag of the PC that recorded it: files with the same tag share one clock | drop |
| `client` | text | the game client's build | drop |
| `bot` | text | the bot's build | drop |
| `fightFile` | text | the fight file armed for this fight - NOT WRITTEN YET: a file begins at the pull, before the engine has picked one; the `bot` rows (`armed`, `fire`) name it | drop |

### `fight`

- `fight`: the fight began or ended

| Field | Holds | What it is | Published copy |
|---|---|---|---|
| `ev` | one of: start end | which edge | keep |
| `by` | one of: auto hand | started or ended by the recorder itself, or by hand | drop |
| `outcome` | one of: kill wipe reset zoned stopped split | on the end row: how it ended (split: a named joined a fight that had none - the fight goes on in the named's own folder, which begins with the seconds before) | keep |
| `named` | a list of text | the NPCs engaged that make it a named's fight (flagged named by the game; outside a raid, epic too), in the order they were engaged | actorNames |
| `ids` | a list of whole numbers | their actor ids, in the same order | actors |

### `text`

- `text`: a line of game text (EQ2_onIncomingText)

| Field | Holds | What it is | Published copy |
|---|---|---|---|
| `msg` | text | the line, verbatim | said |
| `type` | a whole number | the text type number the game gave it (what a rule's chatType compares for on: text) | keep |

### `chat`

- `chat`: a line an NPC said (EQ2_onIncomingChatText). A player's line is never recorded

| Field | Holds | What it is | Published copy |
|---|---|---|---|
| `msg` | text | the line, verbatim | said |
| `chatType` | a whole number | the chat type number the game gave it | keep |
| `speaker` | text | who said it | actorName |
| `target` | text | who it was said to | actorName |
| `channel` | text | the channel's name | drop |
| `speakerId` | a whole number | the speaker's actor id | actor |
| `targetId` | a whole number | the target's actor id | actor |

### `announcement`

- `announcement`: an on-screen announcement (EQ2_onAnnouncement)

| Field | Holds | What it is | Published copy |
|---|---|---|---|
| `msg` | text | the on-screen text, verbatim | said |
| `sound` | text | the sound it came with | game |
| `timer` | a number | the seconds the game showed it for | keep |

### `spawn`, `spawnLate`, `actor`

- `spawn`: an actor entered the actor list (never a player; a pet only with the `pets` switch on)
- `spawnLate`: the same actor about a second later, with its name and look settled
- `actor`: an actor that was already there: written once in a file, the first pass the actor is in range (at the pull, everyone there)

| Field | Holds | What it is | Published copy |
|---|---|---|---|
| `id` | a whole number | the actor's id - the same on every box in the zone | actor |
| `name` | text | its name, as the spawn event carried it | actorName |
| `type` | text | its type: NPC, NamedNPC, NoKill NPC, Special, PC, ... | game |
| `level` | a whole number | its level | keep |
| `named` | true or false | the game marks it named or epic | keep |
| `epic` | true or false | the game marks it epic | keep |
| `x` | a number | where it is | keep |
| `y` | a number |  | keep |
| `z` | a number |  | keep |
| `health` | a whole number | its health, in percent | keep |
| `target` | a whole number | the id of its target, 0 for none | actor |
| `aura` | text | its aura | game |
| `overlay` | text | its overlay | game |
| `tintFlags` | a whole number | its tint flags | keep |
| `guild` | text | the guild line under its name | drop |
| `tooltip` | text | its tooltip | drop |
| `animation` | text | its current animation | game |

### `despawn`

- `despawn`: an actor a spawn or an actor row described left the actor list

| Field | Holds | What it is | Published copy |
|---|---|---|---|
| `id` | a whole number | the actor's id | actor |
| `name` | text | its name | actorName |

### `set`

- `set`: one member of one actor changed. A named's Health is also read on the frame a line of text, an announcement, a cast or a spawn is written, so the health beside that row is the health when it happened

| Field | Holds | What it is | Published copy |
|---|---|---|---|
| `id` | a whole number | the actor's id | actor |
| `m` | text | the member, by its ISXEQ2 name. An NPC: Health, Target, Power, InCombatMode, IsDead, ThreatToMe, Type (it can change under one id: NoKill NPC to NPC, NPC to Corpse), CurrentAnimation, Aura, Overlay, Mood, VisualVariant, TintFlags. The recording toon: Health, Power, Target, InCombat, IsDead. An empty Aura / Overlay / Mood / CurrentAnimation / VisualVariant at an actor's first read is not written | game |
| `v` | a number, text, or true or false | its new value | member |

### `pos`

- `pos`: an actor moved (an NPC of the fight, or one of the group's or raid's own players - no other player is followed)

| Field | Holds | What it is | Published copy |
|---|---|---|---|
| `id` | a whole number | the actor's id | actor |
| `x` | a number |  | keep |
| `y` | a number |  | keep |
| `z` | a number |  | keep |
| `h` | a number | its heading | keep |

### `member`

- `member`: a member of the recording toon's group or raid

| Field | Holds | What it is | Published copy |
|---|---|---|---|
| `id` | a whole number | the member's actor id, 0 when the member is not in the zone | actor |
| `name` | text | the member's name | actorName |
| `class` | text | the member's class | game |
| `group` | a whole number | the raid group the member is in, from 1 | keep |
| `slot` | a whole number | the member's place in that group, from 1 | keep |
| `left` | true or false | true on the row that says the member left | keep |

### `castStart`

- `castStart`: an NPC began to cast

| Field | Holds | What it is | Published copy |
|---|---|---|---|
| `id` | a whole number | the caster's actor id | actor |
| `name` | text | the caster's name | actorName |
| `abilityId` | a whole number | the ability's id | keep |
| `castTime` | a number | its cast time in seconds, as the game gave it at the start | keep |
| `spell` | text | the ability's name, when a cast bar showed it | game |

### `castEnd`

- `castEnd`: an NPC's cast ended (finished or interrupted - the game does not say which)

| Field | Holds | What it is | Published copy |
|---|---|---|---|
| `id` | a whole number | the caster's actor id | actor |
| `name` | text | the caster's name | actorName |
| `abilityId` | a whole number | the ability's id | keep |
| `ms` | a whole number | how long the cast was seen running | keep |

### `castName`

- `castName`: the name of an ability, learned after its cast was written

| Field | Holds | What it is | Published copy |
|---|---|---|---|
| `abilityId` | a whole number | the ability's id | keep |
| `spell` | text | its name | game |

### `myCast`

- `myCast`: the recording toon cast an ability or used an item. A cast that was skipped or refused is not recorded. **Never in a published copy.**

| Field | Holds | What it is | Published copy |
|---|---|---|---|
| `by` | one of: bot hand | bot: the bot issued it - an ability or an item use whose command went out. hand: it was seen on this toon's cast bar with no cast of the bot's behind it, so the player pressed it. An ability with no cast time pressed by hand is never seen | drop |
| `abilityId` | a whole number | the ability's id (not on an item use) | drop |
| `spell` | text | the ability's name: the bot's own name for it, or the cast bar's label for a hand cast | drop |
| `item` | text | the item the bot used | drop |
| `target` | text | who the bot aimed it at, when its cast named someone. Not there = at the toon's target of that moment, and for a hand cast not known: the cast bar never says, and it is never guessed | drop |
| `targetId` | a whole number | that target's actor id, when the bot's cast carried one | drop |
| `why` | text | which part of the bot issued it (the cast stack, a fight file, the pull, ...) | drop |

### `det`

- `det`: a detrimental on the recording toon landed, changed or left

| Field | Holds | What it is | Published copy |
|---|---|---|---|
| `ev` | one of: add set end | it landed, it changed, it left | keep |
| `inst` | a whole number | the application's id | keep |
| `main` | a whole number | its main icon | keep |
| `back` | a whole number | its backdrop icon | keep |
| `stacks` | a whole number | its increments | keep |
| `dur` | a number | seconds left | keep |
| `maxDur` | a number | its full length in seconds | keep |
| `what` | text | which det it is: the key of a `what` row | game |

### `effect`

- `effect`: an effect on another actor landed, changed or left

| Field | Holds | What it is | Published copy |
|---|---|---|---|
| `ev` | one of: add set end | it landed, it changed, it left | keep |
| `id` | a whole number | the actor's id | actor |
| `name` | text | the actor's name | actorName |
| `inst` | a whole number | the application's id | keep |
| `main` | a whole number | its main icon | keep |
| `back` | a whole number | its backdrop icon | keep |
| `stacks` | a whole number | its increments | keep |
| `slot` | a whole number | its place in the actor's effect list, from 1 | keep |
| `what` | text | which effect it is: the key of a `what` row | game |

### `afflict`

- `afflict`: the recording toon's affliction counters changed

| Field | Holds | What it is | Published copy |
|---|---|---|---|
| `trauma` | a whole number |  | keep |
| `arcane` | a whole number |  | keep |
| `noxious` | a whole number |  | keep |
| `elemental` | a whole number |  | keep |
| `cursed` | a whole number |  | keep |

### `what`

- `what`: what an effect is: its name and text

| Field | Holds | What it is | Published copy |
|---|---|---|---|
| `key` | text | the key `det` and `effect` rows point at | game |
| `inst` | a whole number | with "Examine every det" on: the det instance (a `det` row's `inst`) this is the name and text of - two dets can share a key | keep |
| `main` | a whole number | main icon | keep |
| `back` | a whole number | backdrop icon | keep |
| `name` | text | the effect's name | game |
| `lines` | a list of text | the lines of its examine window | game |
| `desc` | text | its description | game |
| `type` | text | its type | game |
| `from` | a list of text | not there: the Effect Tracker read the effect in this zone. There: this pair of icons was read BEFORE, and a pair is read once ever - these are the zones (the tracker's file names) whose files hold this name and text. Two effects can share a pair of icons: `name` then has each name with " / " between, and `lines` each one's lines under a "[name]" line | drop |

### `untold`

- `untold`: the Untold level of a named of the fight, read once from the buff on it

| Field | Holds | What it is | Published copy |
|---|---|---|---|
| `id` | a whole number | the named's actor id | actor |
| `tier` | a whole number | the Untold level: the roman number in the name of the buff on it ("Cloak of Cthurath XXIV" is 24) | keep |

### `abilityGained`

- `abilityGained`: the recording toon gained an ability (EQ2_onAbilityGained) - another class granted it, for example. Nothing is written when it goes away: the game says nothing then

| Field | Holds | What it is | Published copy |
|---|---|---|---|
| `name` | text | the ability, as the game names it in the event | game |
| `tier` | a whole number | the number the event gives beside it - not the ability's Tier (a granted Salve gave 5 while its Tier read Adept) | keep |

### `bot`

- `bot`: what the fight engine did. **Never in a published copy.**

| Field | Holds | What it is | Published copy |
|---|---|---|---|
| `ev` | one of: scope armed hit fire drop action | what happened | drop |
| `mob` | text | the fight's named | drop |
| `rule` | text | the rule's id | drop |
| `on` | text | the trigger word of a hit or a drop | drop |
| `detail` | text | the engine's own line | drop |

### `mark`

- `mark`: a note dropped by hand. **Never in a published copy.**

| Field | Holds | What it is | Published copy |
|---|---|---|---|
| `text` | text | a note dropped on the timeline by hand | drop |

### `gap`

- `gap`: rows were lost here

| Field | Holds | What it is | Published copy |
|---|---|---|---|
| `dropped` | a whole number | how many rows were lost | keep |

## A published copy

A fight put on the web site for other raiders names nobody. Nothing is searched for: the last column of every
table above says what a published copy does with that field, and every field has a mark.
The recording on the PC is never changed.

| Mark | What a published copy does |
|---|---|
| keep | written as it is: a number, true or false, or one of the table's own words. Nothing in it can name anyone |
| drop | left out |
| actor | an actor's id. A player's or a pet's becomes a number of the published copy's own (below zero); an NPC's stays; one no row places is 0. A row whose own actor (`id`) nobody can place, or is a pet, is not in the copy |
| actors | a list of actor ids, each as `actor` |
| actorName | an actor's name. A player's becomes its alias (`G2Ranger1`), a pet's "<its owner's alias>'s pet" ("a pet" when the recording does not say whose). An NPC's stays, and only a name the recording itself says is an NPC's: any other becomes "(someone)" |
| actorNames | a list of actor names, each as `actorName` |
| said | a line the game said while the fight ran. The players' own side of the fight is left out. In the rest every known name is replaced; a line is then shown only when every word of it that starts with a capital is accounted for (an NPC's name, the zone, an ability or an effect, a common word, a word the game writes without a capital elsewhere in the pull, a word the publisher approved), and is withheld and listed for the publisher otherwise |
| game | the game's own fixed words: a class, a zone, an actor's type, an ability's or an effect's name and text, a sound, an animation. Kept, with every known name in it replaced. The last search of the finished copy still reads it |
| member | a `set` row's value, decided by the row's `m`: `Target` is an actor's id, the other members the table names hold nothing of a player, and a member the pass does not know drops the row |

## Where a recording holds what a fight file reacts to

One line for every trigger word, every key of a trigger's match and every condition of the fight vocabulary.
The bot's build checks this list against the engine's own tables, so a trigger or a condition added to the
vocabulary is always listed here.

### Triggers (`on`)

| Trigger | Rows | Fields | To know |
|---|---|---|---|
| `spawn` | `spawn` | `name`, `named` |  |
| `spawnDelayed` | `spawnLate` | `name`, `named` | the engine re-reads the name about a second after the spawn; so does this row |
| `despawn` | `despawn` | `name` |  |
| `detAdded` | `det` | `ev`, `main`, `back` | ev add. The engine fires once per icon pair; a det row is one application - two applications of one pair are two rows |
| `detUpdated` | `det` | `ev`, `stacks`, `dur` | ev set |
| `detRemoved` | `det` | `ev`, `main`, `back` | ev end |
| `chat` | `chat` | `msg`, `chatType`, `speaker`, `target`, `channel` |  |
| `text` | `text` | `msg`, `type` |  |
| `announcement` | `announcement` | `msg`, `sound` |  |
| `castEnded` | `castEnd` | `name`, `abilityId` |  |

Every trigger word is recorded.

### A trigger's `match`

| Family and key | Rows | Fields | To know |
|---|---|---|---|
| `spawn.name` | `spawn`, `spawnLate`, `despawn` | `name` |  |
| `spawn.named` | `spawn`, `spawnLate` | `named` |  |
| `det.main` | `det` | `main` |  |
| `det.back` | `det` | `back` |  |
| `det.value` | `det` | `stacks`, `dur` | the value to compare against is read off the det's rows |
| `chat.chatType` | `chat`, `text` | `chatType`, `type` | a chat row's chatType; a text row's type |
| `chat.needle` | `chat`, `text`, `announcement` | `msg`, `speaker`, `target`, `channel`, `sound` | the text to look for is cut from the line as recorded |
| `cast.named` | `castEnd`, `castStart` | `name` |  |
| `cast.abilityId` | `castEnd`, `castStart` | `abilityId` |  |

### Conditions (`when`)

| Condition | Rows | Fields | To know |
|---|---|---|---|
| `actorCoord` | `pos`, `actor`, `spawn` | `x`, `y`, `z` |  |
| `actorIs` | `actor`, `spawn`, `spawnLate`, `set` | `name`, `type`, `aura`, `overlay`, `tintFlags`, `guild`, `tooltip`, `animation`, `target`, `m`, `v` | the look at the spawn, then a set row for each member that changes |
| `actorNear` | `pos`, `actor`, `spawn` | `x`, `y`, `z` |  |
| `actorPresent` | `actor`, `spawn`, `spawnLate`, `despawn` | `name`, `type` |  |
| `actorTarget` | `set`, `actor`, `member` | `m`, `v`, `target`, `class` | the actor's Target as it changes; the target's class from the member rows |
| `afflicted` | `afflict`, `member` | `trauma`, `arcane`, `noxious`, `elemental`, `cursed`, `name` | each box records its own counters: another toon's are in that toon's recording |
| `chatMatch` | `chat` | `msg`, `chatType`, `speaker`, `target`, `channel` |  |
| `collision` | `pos` | `x`, `y`, `z` | the two points are recorded; whether geometry blocks the line between them is not |
| `count` | `actor`, `spawn`, `spawnLate`, `despawn`, `set`, `pos`, `afflict` | `name`, `type`, `health`, `target`, `aura`, `overlay`, `tintFlags`, `x`, `y`, `z`, `m`, `v`, `cursed` | a count of actors is counted from their rows; a count of the bot's variables or roster is the bot's own state |
| `detTimeLeft` | `det` | `dur`, `maxDur` | the game gives an effect on ANOTHER actor no time left, so an effect row has none |
| `distance` | `pos`, `actor`, `spawn` | `x`, `y`, `z` |  |
| `engaged` | `set`, `actor` | `m`, `v`, `target` | the named's Target: 0 is not engaged |
| `groupDistance` | `pos`, `member` | `x`, `y`, `z`, `name` |  |
| `hasDet` | `det`, `effect` | `main`, `back`, `stacks`, `slot` | on the toon: det rows. On another actor: effect rows, with the slot the effect sits in |
| `inCombat` | `set` | `m`, `v` | the recording toon's InCombat |
| `inMyGroup` | `member` | `name`, `group` |  |
| `mobHealthPct` | `set`, `actor` | `m`, `v`, `health` | the mob's Health as it changes |
| `myStat` | `set`, `afflict` | `m`, `v`, `trauma`, `arcane`, `noxious`, `elemental`, `cursed` | the toon's Health and Power as set rows on its own id, and its affliction counters; its other stats are its own state |
| `namedCasting` | `castStart`, `castEnd` | `name`, `abilityId`, `castTime` |  |
| `nearSpot` | `pos` | `x`, `y`, `z` |  |
| `raidSlot` | `member` | `group`, `slot` |  |
| `textContains` | `chat`, `text`, `announcement` | `msg`, `speaker`, `target`, `channel` |  |
| `textEquals` | `chat`, `text`, `announcement` | `msg`, `speaker`, `target`, `channel` |  |
| `threatToMe` | `set` | `m`, `v` | the mob's ThreatToMe as it changes, on each box |
| `untoldTier` | `untold` | `id`, `tier` | an `untold` row: written once a named a file, in a zone whose name says Untold (since 2026-11-24 - an older recording has none) |
| `zone` | `header` | `zone` |  |

### Conditions the recorder does not hold yet

The game shows these and a recording does not have them.

| Condition | Why |
|---|---|
| `abilityReady` | an ability a fight hands the toon is not recorded yet: nothing writes a row when the book gains one |
| `hasAbility` | an ability a fight hands the toon is not recorded yet: nothing writes a row when the book gains one |
| `hasItem` | an item a fight hands the toon is not recorded yet: nothing writes a row when the bags gain one |
| `heroicOpportunity` | the heroic opportunity wheel's state is not recorded yet |
| `itemReady` | an item a fight hands the toon is not recorded yet: nothing writes a row when the bags gain one |
| `lootWindow` | the game's windows are not recorded |
| `questStep` | quest progress is not recorded |
| `replyDialog` | the game's windows are not recorded |
| `rewardWindow` | the game's windows are not recorded |
| `zoneDoorWindow` | the game's windows are not recorded |

### Not from the game

31 names of the vocabulary are the bot's own state, a timer or the writer's own choice
(how a name is compared, which field, a variable, an option, a camp spot). There is nothing in a recording to
point at for them, and they are not listed.
