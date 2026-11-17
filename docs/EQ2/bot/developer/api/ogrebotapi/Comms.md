# OgreBotAPI.Comms

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Members

### `Dispatched`

`${OgreBotAPI.Comms.Dispatched}`

How many received events at least one of the bot's own handlers acted on. Events no handler wants, and events dropped by for-who, are not counted.

**Returns:** int64: events handled

```text
echo ${OgreBotAPI.Comms.Dispatched}
```

### `Errors`

`${OgreBotAPI.Comms.Errors}`

How many received events were thrown away as unreadable: bad base64, bad JSON, not an event, a newer envelope version, no name, or a name unfit for a script event. For-who drops and a full inbox are not counted here.

**Returns:** int64: unreadable events

```text
echo ${OgreBotAPI.Comms.Errors}
```

### `GroupQuery`

`${OgreBotAPI.Comms.GroupQuery[fw,question...]}`

With arguments, starts a groupQuery on this session and returns it - every read of this form asks again; with no arguments it is the handle whose .Last, .Done[id] and .Result[id] read queries. Answers come over this PC's relay group only, so group or raid members on other PCs show as missing, and a bad question prints a groupQuery error.

All of it: [OgreBotAPI.Comms.GroupQuery](Comms.GroupQuery.md)

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `question...` | string |  | one JSON object, or -key,value pairs: -question (itemCount, abilityReady, slotResolve or LavishScript["${...}"]), -item, -ability or -slot, -compare with -value, -sendTo (default igw:&lt;me>), -limitMs (default 3000), -askAgainIfBlank |

**Returns:** groupquery object: its text is the new query id (read .Done and .Result on it); NULL when the for-who does not name this character or the question is refused. With no arguments: the handle with .Last, .Done[id], .Result[id]

```text
echo ${OgreBotAPI.Comms.GroupQuery[all,-question,itemCount,-item,"Mechanized Platinum Repository of Reconstruction"]}
```

*Was (OldBot):* `OgreBotAPI.Ask`, `OgreBotAPI.Ask_AllFalse`, `OgreBotAPI.Ask_AllTrue`

### `Query_Active`

`${OgreBotAPI.Comms.Query_Active[id]}`

TRUE while a query is still collecting replies, before its timeout. An empty id reads the last query (Query_Last); an unknown or cleared id reads FALSE.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `id` | string |  | the query id from Query_Last; empty = the last query |

**Returns:** bool: TRUE while the query is collecting replies; FALSE once it is done, or for an unknown id

```text
echo ${OgreBotAPI.Comms.Query_Active[${OgreBotAPI.Comms.Query_Last}]}
```

### `Query_Count`

`${OgreBotAPI.Comms.Query_Count[id]}`

How many characters have replied to a query; an unknown id reads 0. Only in-world sessions on this PC answer, and this session answers its own question.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `id` | string |  | the query id from Query_Last; empty = the last query |

**Returns:** int: replies so far (final once Query_Done); 0 for an unknown id

```text
echo ${OgreBotAPI.Comms.Query_Count[${OgreBotAPI.Comms.Query_Last}]}
```

### `Query_Done`

`${OgreBotAPI.Comms.Query_Done[id]}`

TRUE once a query's timeout has passed and its tally is final. The tally stays readable for 60 seconds after that, then the query is forgotten and this reads FALSE again.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `id` | string |  | the query id from Query_Last; empty = the last query |

**Returns:** bool: TRUE when the query has finished; FALSE while it runs, after it is forgotten, or for an unknown id

```text
echo ${OgreBotAPI.Comms.Query_Done[${OgreBotAPI.Comms.Query_Last}]}
```

### `Query_Json`

`${OgreBotAPI.Comms.Query_Json[id]}`

Every reply to a query as one JSON object of responder name to raw answer: the item count, seconds until the ability is ready, the equipped item name, or the expression's text. An empty id reads the last query.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `id` | string |  | the query id from Query_Last; empty = the last query |

**Returns:** string: JSON such as {"Name1":"5","Name2":"0"}; {} when nobody replied or the id is unknown

```text
echo ${OgreBotAPI.Comms.Query_Json[${OgreBotAPI.Comms.Query_Last}]}
```

### `Query_Last`

`${OgreBotAPI.Comms.Query_Last}`

The id of the last query this session started with Comms:Query; the bot's own group, loot and quest questions do not change it, and a refused :Query leaves the previous id in place.

**Returns:** string: the query id; empty before any query started

```text
echo ${OgreBotAPI.Comms.Query_Last}
```

### `Query_TrueCount`

`${OgreBotAPI.Comms.Query_TrueCount[id]}`

How many replies to a query answered TRUE: has the item, ability ready, slot filled, or the expression read true. An empty id reads the last query; an unknown id reads 0.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `id` | string |  | the query id from Query_Last; empty = the last query |

**Returns:** int: TRUE replies so far; 0 for an unknown id

```text
echo ${OgreBotAPI.Comms.Query_TrueCount[${OgreBotAPI.Comms.Query_Last}]}
```

### `Queued`

`${OgreBotAPI.Comms.Queued}`

How many received events are waiting to be handled right now. They are handled on the next pulse, so this is normally 0.

**Returns:** int64: events waiting

```text
echo ${OgreBotAPI.Comms.Queued}
```

### `Received`

`${OgreBotAPI.Comms.Received}`

How many events this session has received from its relay group since it loaded or since the last ResetStats, counting its own events and events its for-who then dropped. It stays 0 when the uplink's OgreConsoleHub is not loaded, because then nothing comes back.

**Returns:** int64: events received

```text
echo ${OgreBotAPI.Comms.Received}
```

### `Stats`

`${OgreBotAPI.Comms.Stats}`

This session's comms counters as one line: received, queued, handled, dropped by for-who, sent, and errors by kind. It is a local read that sends nothing, and echo ${OgreBotAPI.Comms} prints the same line.

**Returns:** string: the counter line, e.g. recv=12 q=0 proc=12 disp=10 nosub=2 refired=12 cfwdrop=0 emit=5 err[b64=0 json=0 type=0 ver=0 name=0 refname=0] of=0 tid[recv=... pulse=...]

```text
echo ${OgreBotAPI.Comms.Stats}
```

### `UplinkName`

`${OgreBotAPI.Comms.UplinkName}`

Inner Space's uplink name for this PC, read from ${InnerSpace.Uplink}. A local read; every session on the PC reads the same text.

**Returns:** string: the value of ${InnerSpace.Uplink}

```text
echo ${OgreBotAPI.Comms.UplinkName}
```

*Was (OldBot):* `GetInfoOb.UplinkName`, `OgreBotAPI.UplinkName`

## Methods

### `AddAnnounce`

`OgreBotAPI.Comms:AddAnnounce[fw, ability, to, text]`

Adds a row to this character's Announce tab and saves it in the loaded profile like a panel edit; from then on, casting the ability sends text to the to place (group or raid chat, a tell to the target, a game command, or a console command). An unknown ability or place, empty text, a duplicate row or no loaded profile is refused with a console line, and nothing announces while the Announce tab is switched off.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `ability` | string |  | the ability's name (any rank) or id, from this character's ability export |
| `to` | string |  | where to announce: Group, Raid, Tell To Target, In-Game Command or Execute In Console (any case) |
| `text` | string |  | the announce text; everything after to is joined back with commas, so it need not be quoted |

```text
OgreBotAPI.Comms:AddAnnounce[${Me.Name},Rescue,Group,"Rescue on *Target*"]
```

*Was (OldBot):* `OgreBotAPI:Announce_AddEntry`

### `Broadcast`

`OgreBotAPI.Comms:Broadcast[fw, text, -tab name..., -sound ding|alarm]`

Sends the text to every session in this PC's relay group, this one included; each shows "[Notify] &lt;sender>: &lt;text>" in its OgreConsole (and the -tab tab) and plays the -sound. fw picks which sessions send, not who receives; it never leaves the PC, and with no OgreConsoleHub in the uplink nobody shows it, not even this session.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `text` | string |  | the line to show; commas in it are kept |
| `-tab name...` | string |  | followed by an OgreConsole tab name - each receiver also puts the line in that tab; may be repeated |
| `-sound ding\|alarm` | string |  | followed by ding or alarm - each receiver plays that sound; a bare -sound is ding |

```text
OgreBotAPI.Comms:Broadcast[${Me.Name},"Named is up",-sound,alarm]
```

*Was (OldBot):* `OgreBotAPI:Message_Relay`

### `ConversationBubble`

`OgreBotAPI.Comms:ConversationBubble[fw, num=1]`

Clicks reply number num in the NPC conversation window open on this session; needs a character in the world. When no conversation is open or it has no such reply nothing is clicked, and only the log file says so.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `num` | int | `1` | which reply to click, counting from 1 as SpewConversationBubbles numbers them |

```text
OgreBotAPI.Comms:ConversationBubble[igw:${Me.Name},2]
```

*Was (OldBot):* `OgreBotAPI:ConversationBubble`, `OgreBotAPI:OptNum`, `call Obj_OgreUtilities.DoConversation`

### `Emit`

`OgreBotAPI.Comms:Emit[fw, name, cfw="", dest="", ev=1, dataJson=""]`

Sends a named event to every session in this session's relay group on this PC, this one included; each session whose for-who matches cfw runs its handlers and fires the script event OgreComms_&lt;name> with the event JSON. It never leaves the PC and needs OgreConsoleHub in the uplink - without it nothing arrives anywhere and, a few seconds on, a "comms egress is BLIND" warning prints; an empty name gets a refusal line and invalid dataJson is refused (log file only).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `name` | string |  | the event name (required); letters, digits and _ up to 64 characters, or no OgreComms_ script event fires |
| `cfw` | string | `""` | for-who checked by each receiving session; empty = every session. A session not in the world (login screen, character select, zoning) takes in only what needs no game - messages, tag changes, group and key-bind updates - and throws momentary requests (casts, script events) away; a changed MCP file is kept once and read when it reaches the world; the OgreComms_ script event fires only in the world |
| `dest` | string | `""` | the relay group to deliver to; empty = this session's relay group (Relay Groups tab) |
| `ev` | int | `1` | the data version number stamped on the event |
| `dataJson` | string | `""` | a JSON value carried as the event's data; must be valid JSON |

```text
OgreBotAPI.Comms:Emit[${Me.Name},MyEvent]
```

### `ExecuteEvent`

`OgreBotAPI.Comms:ExecuteEvent[fw, name, ...]`

Runs Event["name"]:Execute[...] on this session with the remaining arguments joined by commas, as written (not quoted). Local only - nothing is sent; needs a character in the world.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `name` | string |  | the LavishScript event to fire |
| `...` | string |  | arguments passed to the event, in order |

```text
OgreBotAPI.Comms:ExecuteEvent[${Me.Name},MyScript_Pull,${Target.ID}]
```

*Was (OldBot):* `OgreBotAPI:ExecuteEvent_JSON`, `OgreBotAPI:ExecuteEvent`

### `GroupQuery`

`OgreBotAPI.Comms:GroupQuery[fw, question...]`

Starts a groupQuery: asks group or raid members a question and judges the answers; read the id from ${OgreBotAPI.Comms.GroupQuery.Last} and the result JSON from .Result[id], which also fires OgreEvent_GroupQueryDone. Answers come over this PC's relay group only, so members on other PCs show as missing, and a bad question prints a groupQuery error to the console.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `question...` | string |  | one JSON object, or -key,value pairs: -question (itemCount, abilityReady, slotResolve or LavishScript["${...}"]), -item, -ability or -slot, -compare with -value, -sendTo (default igw:&lt;me>), -limitMs (default 3000), -askAgainIfBlank |

```text
OgreBotAPI.Comms:GroupQuery[${Me.Name},-question,abilityReady,-ability,Rescue,-sendTo,igw:${Me.Name}]
```

### `Ingest`

`OgreBotAPI.Comms:Ingest[fw, wire]`

Hands a base64 event envelope to this session's comms receiver as if it had arrived from the relay group; it is handled on the next pulse. Nothing is sent anywhere, and unreadable input only adds to Errors.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `wire` | string |  | the base64-encoded event envelope JSON |

```text
OgreBotAPI.Comms:Ingest[${Me.Name},eyJ2IjoxLCJmcm9tIjoiaXMxIiwiZGVzdGluYXRpb24iOiJvZ3JlX2V2ZXJxdWVzdDIiLCJ0eXBlIjoiZXZlbnQiLCJhcmdzIjp7Im5hbWUiOiJNeUV2ZW50IiwiZXYiOjF9fQ==]
```

### `InjectChat`

`OgreBotAPI.Comms:InjectChat[fw, chat=Nothing]`

Feeds the text into this session's own chat handling as a raid-chat line from the bot's built-in speaker OgreIRCSession, on the next pulse, so chat triggers and chat commands act on it. Nothing is said in game or sent anywhere; needs a character in the world.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `chat` | string | `Nothing` | the chat text to inject |

```text
OgreBotAPI.Comms:InjectChat[${Me.Name},"burn now"]
```

*Was (OldBot):* `OgreBotAPI:InjectChat`

### `IrcAuthIfInRaid`

`OgreBotAPI.Comms:IrcAuthIfInRaid[nick, toon]`

If toon is in this character's raid, tells this PC's IRC bridge to accept commands from the IRC nick nick, marked as learned through the raid so IrcRaidUnauth can take it back. There is no for-who - every in-world session checks and prints a line saying whether toon is in its raid; nothing happens if the IRC bridge is not loaded in the uplink.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `nick` | string |  | the IRC nick to accept, as written |
| `toon` | string |  | the character whose raid membership decides it |

```text
OgreBotAPI.Comms:IrcAuthIfInRaid[${Me.Name}_IRC,${Group[1].Name}]
```

*Was (OldBot):* `OgreBotAPI:OgreIRC_AuthIfInRaid`

### `IrcConnect`

`OgreBotAPI.Comms:IrcConnect[fw]`

Loads the IRC bridge (OgreIRCHub) in this PC's uplink if it is not loaded and connects it to IRC with the saved settings; already connected = no change. It prints "irc: connecting" either way, and if the settings file cannot be read the bridge says so and does not connect.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Comms:IrcConnect[${Me.Name}]
```

### `IrcDisconnect`

`OgreBotAPI.Comms:IrcDisconnect[fw]`

Asks this PC's IRC bridge to disconnect from IRC; the bridge stays loaded and idle. It prints "irc: asking the uplink OgreIRCHub to disconnect (it stays loaded)." and the bridge reports the result on the uplink.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Comms:IrcDisconnect[${Me.Name}]
```

### `IrcRaidAuth`

`OgreBotAPI.Comms:IrcRaidAuth[fw]`

Asks, over IRC, every IRC bridge whose PC has a character in this raid to accept commands from each other's nicks; characters outside the raid take no part. Needs a character in a raid and IRC connected - otherwise it prints why and asks nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Comms:IrcRaidAuth[${Me.Name}]
```

### `IrcRaidCheck`

`OgreBotAPI.Comms:IrcRaidCheck[fw, ask, toon]`

Answers this PC's IRC bridge: if toon is in this character's raid, it reports this character's name back for question number ask. It says nothing when toon is not in the raid, when ask is not all digits, or out of the world; the bridge calls this itself.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `ask` | int |  | the bridge's question number (digits only) |
| `toon` | string |  | the character that asked; must be a plain name |

```text
OgreBotAPI.Comms:IrcRaidCheck[all,12,${Group[1].Name}]
```

### `IrcRaidUnauth`

`OgreBotAPI.Comms:IrcRaidUnauth[fw]`

Asks, over IRC, every IRC bridge in this raid to drop the nicks it accepted through the raid; nicks accepted any other way stay. Needs a character in a raid and IRC connected - otherwise it prints why and asks nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Comms:IrcRaidUnauth[${Me.Name}]
```

### `IrcReload`

`OgreBotAPI.Comms:IrcReload[fw]`

Makes this PC's IRC bridge re-read its settings and reconnect with them, but only if it is connected - an idle bridge stays idle. It prints "irc: reloading the uplink hub config."; a settings file that does not read is only written to the bridge's log.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Comms:IrcReload[${Me.Name}]
```

### `LogStats`

`OgreBotAPI.Comms:LogStats[fw]`

Prints the Stats counter line to this session's console and writes it to the log file. Local only.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Comms:LogStats[all]
```

### `Message`

`OgreBotAPI.Comms:Message[fw, text, -tab name..., -sound ding|alarm]`

Prints "[Message] &lt;text>" in this session's OgreConsole (the Inner Space console when OgreConsole is not available); nothing goes to other sessions, IRC or game chat. -tab also puts it in that OgreConsole tab and -sound plays the sound here; an unknown sound name warns and plays nothing, and an empty text does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `text` | string |  | the line to show; commas in it are kept |
| `-tab name...` | string |  | followed by an OgreConsole tab name - the line also lands in that tab; may be repeated |
| `-sound ding\|alarm` | string |  | followed by ding or alarm - plays that sound with the line; a bare -sound is ding |

```text
OgreBotAPI.Comms:Message[${Me.Name},"Pull in 10 seconds",-sound,ding]
```

*Was (OldBot):* `OgreBotAPI:Message`, `OgreBotAPI:Message_NT`

### `Pushover`

`OgreBotAPI.Comms:Pushover[fw, message..., -title t, -priority n]`

Sends a push notification through the Pushover service from this session; every word that is not a flag becomes the message. Not configured (no app token or user key), switched off in the profile, or no message = nothing sent and a warning, and -sound, -device, -retry and -expire are accepted but ignored.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `message...` | string |  | the notification text; unflagged words are joined with spaces |
| `-title t` | string |  | followed by the notification title |
| `-priority n` | int | `0` | followed by a Pushover priority, -2 to 2 |

```text
OgreBotAPI.Comms:Pushover[${Me.Name},"Raid wiped",-title,EQ2,-priority,1]
```

*Was (OldBot):* `OgreBotAPI:Pushover`, `Obj_Pushover.PushoverSendMsg`, `Obj_Pushover`

### `Query`

`OgreBotAPI.Comms:Query[fw, kind, cfw="", timeoutMs=0, paramsJson=""]`

Asks every in-world session in this PC's relay group a typed question and tallies the replies; read the new id from Query_Last, then Query_Count, Query_TrueCount and Query_Json once Query_Done. Sessions on other PCs never answer (it does not use IRC), with no OgreConsoleHub in the uplink nobody answers, not even this session, and an unknown kind or one of the bot's own (lootBid, questSteps) is refused (log file only).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `kind` | string |  | the question: itemCount, abilityReady, slotResolve or eval (required) |
| `cfw` | string | `""` | for-who checked by each session before it answers; empty = every session |
| `timeoutMs` | int | `0` | how long to collect replies in milliseconds; 0 or less = 3000, capped at 60000 |
| `paramsJson` | string | `""` | the question's JSON: itemCount {"item":"name"}, abilityReady {"ability":"name or id"}, slotResolve {"slot":"slot name or number"}, eval {"expr":"a LavishScript expression"}; missing or wrong = nobody answers |

```text
OgreBotAPI.Comms:Query[${Me.Name},itemCount,all,5000,{"item":"Mechanized Platinum Repository of Reconstruction"}]
```

### `Query_Clear`

`OgreBotAPI.Comms:Query_Clear[fw, id=""]`

Forgets a query and its tally on this session; its Query_* reads go back to FALSE, 0 and {}. Leave id empty for the last Comms:Query - an unknown id does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `id` | string | `""` | the query id to forget; empty = the last query (the word last itself is not recognised) |

```text
OgreBotAPI.Comms:Query_Clear[${Me.Name}]
```

### `ReportVersion`

`OgreBotAPI.Comms:ReportVersion[fw, compareTo]`

Says this character's bot version in IRC: "VERSION: &lt;name> (&lt;version>)" when compareTo is empty, else "SAME: &lt;name> (&lt;version>)" or "DIFFERENT: &lt;name> - Mine: &lt;version> Requested: &lt;compareTo>". Needs a character in the world; while IRC is not connected the IRC bridge holds the line and sends it once it connects.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `compareTo` | string |  | the version to compare against; empty = just report the version |

```text
OgreBotAPI.Comms:ReportVersion[all,""]
```

### `ResetStats`

`OgreBotAPI.Comms:ResetStats[fw]`

Zeroes this session's comms counters (Stats, Received, Dispatched, Errors) and restarts the silent-hub warning's clock. Local only; prints nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Comms:ResetStats[all]
```

### `SendTell`

`OgreBotAPI.Comms:SendTell[fw, target, message]`

Sends an in-game /tell from this character to target, in game chat; needs a character in the world. If target or message contains NULL the tell is not sent and an "Unable to send" line goes to IRC instead (the IRC bridge holds it until IRC connects).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `target` | string |  | the character to send the tell to |
| `message` | string |  | the tell's text; commas in it are kept |

```text
OgreBotAPI.Comms:SendTell[${Me.Name},${Group[1].Name},"Ready when you are"]
```

*Was (OldBot):* `OgreBotAPI:Send_Tell`

### `SpewConversationBubbles`

`OgreBotAPI.Comms:SpewConversationBubbles[fw]`

Prints the replies the open NPC conversation window offers to this session's console, numbered the way ConversationBubble clicks them. With no conversation open it prints "no conversation window open."

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Comms:SpewConversationBubbles[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:ConversationBubbleSpew`

### `SpewRelayGroup`

`OgreBotAPI.Comms:SpewRelayGroup[fw]`

Sends "&lt;name>: OgreRelayGroup: &lt;group>" to every session in this PC's relay group, naming the relay group this session uses now. Same path as Broadcast - nobody shows it without OgreConsoleHub in the uplink - and it needs a character in the world.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.Comms:SpewRelayGroup[all]
```

*Was (OldBot):* `OgreBotAPI:Spew_RelayGroup`

### `TTS`

`OgreBotAPI.Comms:TTS[fw, text]`

Speaks the text aloud on this PC through Inner Space (uplink speak). An empty for-who means is1, not all, so by default only session is1 speaks; empty text does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `text` | string |  | the words to speak |

```text
OgreBotAPI.Comms:TTS[${Me.Name},"Tank is low"]
```

*Was (OldBot):* `OgreBotAPI:TTS`
