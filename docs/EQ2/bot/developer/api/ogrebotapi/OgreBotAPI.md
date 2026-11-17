# OgreBotAPI

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Members

### `Abilities`

`${OgreBotAPI.Abilities}`

The Abilities sub-object: the in-memory ability catalog loaded from this character's ability export, the ability reads built on it, and the cast and cancel verbs. Opening OgreBot loads the catalog; without OgreBot open, load it with its :Load before reading abilities from it.

All of it: [OgreBotAPI.Abilities](Abilities.md)

**Returns:** object: the Abilities sub-object; it always exists, and as text it reads OgreBotAPI.Abilities.

```text
echo ${OgreBotAPI.Abilities}
```

### `Access`

`${OgreBotAPI.Access}`

The Access sub-object: this session's access level (SetLevel) and UnauthPCsNearMe, which reports another player nearby who is not one of your own characters.

All of it: [OgreBotAPI.Access](Access.md)

**Returns:** object: the Access sub-object; it always exists, and as text it reads Access[level/highest], this session's level and the account's highest level.

```text
echo ${OgreBotAPI.Access}
```

### `Actors`

`${OgreBotAPI.Actors}`

Opens the Actors sub-object: counting and finding actors near you (by name, by type, NPCs within a range, mob ID, is-a-player), and clicking, hailing or applying a verb to an actor, now or queued. It always resolves and takes no arguments; the work is in its own members and methods.

All of it: [OgreBotAPI.Actors](Actors.md)

**Returns:** OgreBotAPI.Actors object: never NULL; as text it reads OgreBotAPI.Actors.

```text
echo ${OgreBotAPI.Actors}
```

### `Assist`

`${OgreBotAPI.Assist}`

The Assist sub-object: who this character takes its kill target from. Its members (TargetID, InControl, IsAssisting) read that choice, and :Anchor sets it.

All of it: [OgreBotAPI.Assist](Assist.md)

**Returns:** object: the Assist sub-object; it always exists, and as text it reads OgreBotAPI.Assist.

```text
echo ${OgreBotAPI.Assist}
```

### `AutoHunt`

`${OgreBotAPI.AutoHunt}`

The AutoHunt sub-object: the AutoHunt driver's state (Mode, Active, AllowMovement, SafetyTripped, PullTargetID, LastAction, FreezeReason) and its setters (:SetMode, :SetScanRadius, :SetCheckHP, :SetCheckMana).

All of it: [OgreBotAPI.AutoHunt](AutoHunt.md)

**Returns:** object: the AutoHunt sub-object; it always exists, and as text it reads OgreBotAPI.AutoHunt.

```text
echo ${OgreBotAPI.AutoHunt}
```

### `AutoTarget`

`${OgreBotAPI.AutoTarget}`

The AutoTarget sub-object: the auto-target list and its settings - enable, scan radius and height, add or remove actors, presets and saved lists. As text it reports how many entries the current working list holds.

All of it: [OgreBotAPI.AutoTarget](AutoTarget.md)

**Returns:** object: the AutoTarget sub-object; it always exists, and as text it reads AutoTarget[N entries], N being the number of entries in the current working list.

```text
echo ${OgreBotAPI.AutoTarget}
```

*Was (OldBot):* `OgreBotAPI:AutoTarget`

### `Bot`

`${OgreBotAPI.Bot}`

The Bot sub-object: the running bot's own lifecycle - pause, resume, reload, end, camp to desktop, exit the client, run OgreBot commands and scripts. It is the running bot, not the saved profile options.

All of it: [OgreBotAPI.Bot](Bot.md)

**Returns:** object: the Bot sub-object; it always exists, and as text it reads OgreBotAPI.Bot.

```text
echo ${OgreBotAPI.Bot}
```

### `CampSpot`

`${OgreBotAPI.CampSpot}`

The CampSpot sub-object: the camp spot this character holds to - set, nudge, clear and enable it, relative spots, spots behind or in front of an actor, and formations. Its members read the active slot, the effective spot and whether you are at it.

All of it: [OgreBotAPI.CampSpot](CampSpot.md)

**Returns:** object: the CampSpot sub-object; it always exists, and as text it reads OgreBotAPI.CampSpot.

```text
echo ${OgreBotAPI.CampSpot}
```

### `CastStack`

`${OgreBotAPI.CastStack}`

The CastStack sub-object: the cast stack - load or import it, turn entries and tags on or off, hold and clear tag embargos and allows, and inspect it. Bot:Pause and Bot:Resume pause and run it.

All of it: [OgreBotAPI.CastStack](CastStack.md)

**Returns:** object: the CastStack sub-object; it always exists, and as text it reads OgreBotAPI.CastStack.

```text
echo ${OgreBotAPI.CastStack}
```

### `Client`

`${OgreBotAPI.Client}`

The Client sub-object: things done to the EQ2 client rather than the character - reset the camera, set the camera pitch, and move the mouse. It holds methods only.

All of it: [OgreBotAPI.Client](Client.md)

**Returns:** object: the Client sub-object; it always exists, and as text it reads OgreBotAPI.Client.

```text
echo ${OgreBotAPI.Client}
```

### `Combat`

`${OgreBotAPI.Combat}`

The Combat sub-object: whether you are fighting and what the bot may do while you are - InCombat, the no-offensive and no-defensive switches, the threat ignore list and the countdown.

All of it: [OgreBotAPI.Combat](Combat.md)

**Returns:** object: the Combat sub-object; it always exists, and as text it reads OgreBotAPI.Combat.

```text
echo ${OgreBotAPI.Combat}
```

### `Comms`

`${OgreBotAPI.Comms}`

The Comms sub-object: messaging between your characters - events, messages, broadcasts, tells, group queries and IRC. As text it is a one-line summary of its send and receive counters, prefixed "Comms ".

All of it: [OgreBotAPI.Comms](Comms.md)

**Returns:** object: the Comms sub-object; it always exists, and as text it reads "Comms " followed by the one-line counter summary (the same text as ${OgreBotAPI.Comms.Stats}).

```text
echo ${OgreBotAPI.Comms}
```

### `Consumables`

`${OgreBotAPI.Consumables}`

The Consumables sub-object: things you eat, drink, click, mount or summon - replenish food, drink and stat potions, mount up and down, summon a familiar, rekindle the heartstone, and the mount, mercenary and familiar training checks. It holds methods only.

All of it: [OgreBotAPI.Consumables](Consumables.md)

**Returns:** object: the Consumables sub-object; it always exists, and as text it reads OgreBotAPI.Consumables.

```text
echo ${OgreBotAPI.Consumables}
```

### `Craft`

`${OgreBotAPI.Craft}`

Opens the Craft sub-object: the crafting calls of ${ISXOgreEQ2.Craft} with a for-who in front, so each runs only on the characters it names (add a recipe, start, writs, scribe, tinkering). It has methods only and takes no arguments.

All of it: [OgreBotAPI.Craft](Craft.md)

**Returns:** OgreBotAPI.Craft object: never NULL; as text it reads OgreBotAPI.Craft.

```text
echo ${OgreBotAPI.Craft}
```

### `Cures`

`${OgreBotAPI.Cures}`

The Cures sub-object: cures, curses and dispels - the group curse counts, uncurable and detrimental reads, cure requests, item cures, cancelling a detrimental and replenishing cure potions.

All of it: [OgreBotAPI.Cures](Cures.md)

**Returns:** object: the Cures sub-object; it always exists, and as text it reads OgreBotAPI.Cures.

```text
echo ${OgreBotAPI.Cures}
```

### `Debug`

`${OgreBotAPI.Debug}`

The Debug sub-object: the version, the debug output switches, debug echoes and the variable and stat spews.

All of it: [OgreBotAPI.Debug](Debug.md)

**Returns:** object: the Debug sub-object; it always exists, and as text it reads OgreBotAPI.Debug.

```text
echo ${OgreBotAPI.Debug}
```

### `Encounter`

`${OgreBotAPI.Encounter}`

Opens the Encounter sub-object: one method, List, which lists the available encounter setups on the characters a for-who names. The encounter engine itself is ${ISXOgreEQ2.Encounter}, a different object.

All of it: [OgreBotAPI.Encounter](Encounter.md)

**Returns:** OgreBotAPI.Encounter object: never NULL; as text it reads OgreBotAPI.Encounter.

```text
echo ${OgreBotAPI.Encounter}
```

### `Events`

`${OgreBotAPI.Events}`

The Events sub-object: add and remove rows of the Chat, Spawn and Despawn event tabs, the same rows the panel edits. It holds methods only.

All of it: [OgreBotAPI.Events](Events.md)

**Returns:** object: the Events sub-object; it always exists, and as text it reads OgreBotAPI.Events.

```text
echo ${OgreBotAPI.Events}
```

### `ForWho`

`${OgreBotAPI.ForWho}`

Opens the ForWho sub-object: ask whether a for-who expression selects this character or a named group member, and manage for-who aliases (add, remove, change, rename, list). It always resolves and takes no arguments.

All of it: [OgreBotAPI.ForWho](ForWho.md)

**Returns:** OgreBotAPI.ForWho object: never NULL; as text it reads OgreBotAPI.ForWho.

```text
echo ${OgreBotAPI.ForWho}
```

### `HOs`

`${OgreBotAPI.HOs}`

Opens the HOs sub-object: heroic opportunity reads (is the starter or wheel up, which wheel, who can start or advance it, time left) and the verbs that start, advance or cancel one and set which icons may be used. It always resolves and takes no arguments.

All of it: [OgreBotAPI.HOs](HOs.md)

**Returns:** OgreBotAPI.HOs object: never NULL; as text it reads OgreBotAPI.HOs.

```text
echo ${OgreBotAPI.HOs}
```

### `IM`

`${OgreBotAPI.IM}`

The IM sub-object: the Inventory Manager session - IsOpen, IsRunning, Status and one method per `ogre im` word. As text it is the session's status line, not the object's name.

All of it: [OgreBotAPI.IM](IM.md)

**Returns:** object: the IM sub-object; it always exists, and as text it reads the status line - "closed", or "open" (or "closed (running headless)") followed by ", idle" or ", running &lt;mode>", plus "; will close when finished (-end)" when that is pending.

```text
echo ${OgreBotAPI.IM}
```

### `Inventory`

`${OgreBotAPI.Inventory}`

Opens the Inventory sub-object: item counts, free bag slots, equipment slot names, adornments, and the verbs that use, examine, equip, unpack, consume or destroy items plus the item rotation embargo list. It always resolves and takes no arguments.

All of it: [OgreBotAPI.Inventory](Inventory.md)

**Returns:** OgreBotAPI.Inventory object: never NULL; as text it reads OgreBotAPI.Inventory.

```text
echo ${OgreBotAPI.Inventory}
```

### `Loot`

`${OgreBotAPI.Loot}`

Opens the Loot sub-object: loading the loot rule files, deciding what to do with each item in a loot window, loot-all, auto-loot mode and the loot options. It always resolves and takes no arguments.

All of it: [OgreBotAPI.Loot](Loot.md)

**Returns:** OgreBotAPI.Loot object: never NULL; as text it reads OgreBotAPI.Loot.

```text
echo ${OgreBotAPI.Loot}
```

### `Looting`

`${OgreBotAPI.Looting}`

TRUE while looting is going on: a loot window is open, or OgreBot did loot work (opened a corpse, chest or shiny, or worked a loot window) in the last 3 seconds. It simply runs out 3 seconds after the last loot activity, so a script waiting for looting to finish can poll it.

**Returns:** bool: TRUE when a loot window is open or the last loot activity was under 3 seconds ago; FALSE otherwise (including when nothing has been looted yet).

```text
echo ${OgreBotAPI.Looting}
```

*Was (OldBot):* `Obj_OgreIH.LastLootWindowAppeared`, `Obj_OgreIH:EQ2_onLootWindowAppeared`, `Object_Instance_Inherit.LastLootWindowAppeared`

### `Merchant`

`${OgreBotAPI.Merchant}`

Opens the Merchant sub-object: buying from, selling to and repairing at an NPC merchant (not the broker and not the depot). It has methods only and takes no arguments.

All of it: [OgreBotAPI.Merchant](Merchant.md)

**Returns:** OgreBotAPI.Merchant object: never NULL; as text it reads OgreBotAPI.Merchant.

```text
echo ${OgreBotAPI.Merchant}
```

### `Movement`

`${OgreBotAPI.Movement}`

Opens the Movement sub-object: distance, heading and facing reads, points around an actor, and the walking verbs - move to a loc, navigate, follow, joust, face, fly, jump, crouch, evac and movement blocks. It always resolves and takes no arguments.

All of it: [OgreBotAPI.Movement](Movement.md)

**Returns:** OgreBotAPI.Movement object: never NULL; as text it reads OgreBotAPI.Movement.

```text
echo ${OgreBotAPI.Movement}
```

### `NPCUnkillableBug`

`${OgreBotAPI.NPCUnkillableBug}`

TRUE when your current target looks stuck in the unkillable state: an NPC or NamedNPC that cannot turn, is feign-dead, is not aggro and is rooted. FALSE when you have no target or are not in the world.

**Returns:** bool: TRUE when your target is an NPC or NamedNPC with CanTurn FALSE, IsFD TRUE, IsAggro FALSE and IsRooted TRUE; FALSE otherwise, with no target, or out of the world.

```text
echo ${OgreBotAPI.NPCUnkillableBug}
```

*Was (OldBot):* `OgreBotAPI.NPCUnkillableBug`

### `Options`

`${OgreBotAPI.Options}`

Opens the Options sub-object: read an OgreBot option value, set options, load a profile, revert, and warn before saving. As text it shows the loaded profile name, or "no profile" when none is loaded.

All of it: [OgreBotAPI.Options](Options.md)

**Returns:** OgreBotAPI.Options object: never NULL; as text it reads Options[&lt;profile name>], or Options[no profile].

```text
echo ${OgreBotAPI.Options}
```

### `Overseer`

`${OgreBotAPI.Overseer}`

Opens the Overseer sub-object: four Overseer verbs (add agents, check quests, auto-add quests, buy missions). The Overseer engine itself is run from ${ISXOgreEQ2.Overseer}, a different object.

All of it: [OgreBotAPI.Overseer](Overseer.md)

**Returns:** OgreBotAPI.Overseer object: never NULL; as text it reads OgreBotAPI.Overseer.

```text
echo ${OgreBotAPI.Overseer}
```

### `Paths`

`${OgreBotAPI.Paths}`

Opens the Paths sub-object: saved walks through the zone you are in, each a list of points of interest or locations. It always resolves and takes no arguments.

All of it: [OgreBotAPI.Paths](Paths.md)

**Returns:** OgreBotAPI.Paths object: never NULL; as text it reads OgreBotAPI.Paths.

```text
echo ${OgreBotAPI.Paths}
```

### `Pet`

`${OgreBotAPI.Pet}`

Opens the Pet sub-object: four pet commands - attack, back off, assist and get lost. It has methods only and takes no arguments.

All of it: [OgreBotAPI.Pet](Pet.md)

**Returns:** OgreBotAPI.Pet object: never NULL; as text it reads OgreBotAPI.Pet.

```text
echo ${OgreBotAPI.Pet}
```

### `POI`

`${OgreBotAPI.POI}`

Opens the POI sub-object: named spots in the zone you are in, which -TravelMesh and every verb that takes a location can use by name. It always resolves and takes no arguments.

All of it: [OgreBotAPI.POI](POI.md)

**Returns:** OgreBotAPI.POI object: never NULL; as text it reads OgreBotAPI.POI.

```text
echo ${OgreBotAPI.POI}
```

### `Position`

`${OgreBotAPI.Position}`

Opens the Position sub-object: geometry reads - a point at an angle from an actor, a point toward another, distance to an actor, the farthest group member or actor, and model sizes. It has members only and takes no arguments.

All of it: [OgreBotAPI.Position](Position.md)

**Returns:** OgreBotAPI.Position object: never NULL; as text it reads OgreBotAPI.Position.

```text
echo ${OgreBotAPI.Position}
```

### `Quest`

`${OgreBotAPI.Quest}`

Opens the Quest sub-object: whether you or an actor has a quest, and the quest and mission verbs - share, accept, delete, show info and mission timers. It always resolves and takes no arguments.

All of it: [OgreBotAPI.Quest](Quest.md)

**Returns:** OgreBotAPI.Quest object: never NULL; as text it reads OgreBotAPI.Quest.

```text
echo ${OgreBotAPI.Quest}
```

### `Roster`

`${OgreBotAPI.Roster}`

Opens the Roster sub-object: group and raid reads (sizes, counts and members picked by class, archetype or role, leader, in zone) and the group verbs - flag, mark, invite, disband, make leader, mentor, kick. It always resolves and takes no arguments.

All of it: [OgreBotAPI.Roster](Roster.md)

**Returns:** OgreBotAPI.Roster object: never NULL; as text it reads OgreBotAPI.Roster.

```text
echo ${OgreBotAPI.Roster}
```

### `Session`

`${OgreBotAPI.Session}`

Opens the Session sub-object: whether this client is at character select, the character name, revive and res verbs, harvesting a node, collecting a shiny, and logging a character in. As text it shows your character name, which is empty while you are not in the world.

All of it: [OgreBotAPI.Session](Session.md)

**Returns:** OgreBotAPI.Session object: never NULL; as text it reads Session[&lt;your character name>], or Session[] out of the world.

```text
echo ${OgreBotAPI.Session}
```

### `TempAdorns`

`${OgreBotAPI.TempAdorns}`

The TempAdorns sub-object: the temporary-adornment profiles - IsOpen, Profiles, the window (:Open, :Close, :UI), :Apply and :List.

All of it: [OgreBotAPI.TempAdorns](TempAdorns.md)

**Returns:** object: the TempAdorns sub-object; it always exists, and as text it reads OgreBotAPI.TempAdorns.

```text
echo ${OgreBotAPI.TempAdorns}
```

### `Travel`

`${OgreBotAPI.Travel}`

Opens the Travel sub-object: ordinary travel - bells, druid rings, spires, the guild hall, zone doors and the travel mesh. It always resolves and takes no arguments.

All of it: [OgreBotAPI.Travel](Travel.md)

**Returns:** OgreBotAPI.Travel object: never NULL; as text it reads OgreBotAPI.Travel.

```text
echo ${OgreBotAPI.Travel}
```

### `Util`

`${OgreBotAPI.Util}`

The Util sub-object: helpers LavishScript does not have - number and text conversions, rounding, range checks, colour-code and zone-number stripping, time formatting, MD5, file-exists, plus on-screen timers and delayed actions.

All of it: [OgreBotAPI.Util](Util.md)

**Returns:** object: the Util sub-object; it always exists, and as text it reads OgreBotAPI.Util.

```text
echo ${OgreBotAPI.Util}
```

### `ValidKillTarget`

`${OgreBotAPI.ValidKillTarget}`

TRUE when the bot's current NPC kill target still exists. The kill target is refreshed once per pulse in the world: your target if it is a living NPC or NamedNPC, otherwise your target's target if that is one.

**Returns:** bool: TRUE when there is an NPC kill target and its actor still exists; FALSE when there is none (${ISXOgreEQ2.NPCTargetID} reads 0) or the actor is gone.

```text
echo ${OgreBotAPI.ValidKillTarget}
```

*Was (OldBot):* `OgreBotAPI.ValidKillTarget`

### `Vars`

`${OgreBotAPI.Vars}`

Opens the Vars sub-object: two named-value stores - a plain one for your scripts (Get, Set, Clear) and the bot's own internal one (GetInternal, SetInternal, ClearInternal). It always resolves and takes no arguments.

All of it: [OgreBotAPI.Vars](Vars.md)

**Returns:** OgreBotAPI.Vars object: never NULL; as text it reads OgreBotAPI.Vars.

```text
echo ${OgreBotAPI.Vars}
```

### `Windows`

`${OgreBotAPI.Windows}`

Opens the Windows sub-object: game dialogs and windows - NPC reply choices, reward windows, the examine window, text-input windows, the OK button, and showing or toggling the OgreBot console and main window. It always resolves and takes no arguments.

All of it: [OgreBotAPI.Windows](Windows.md)

**Returns:** OgreBotAPI.Windows object: never NULL; as text it reads OgreBotAPI.Windows.

```text
echo ${OgreBotAPI.Windows}
```

### `Zone`

`${OgreBotAPI.Zone}`

Opens the Zone sub-object: the zone name and what kind of place it is (instance, guild hall, house), plus zoning and the zone reset verbs. It always resolves and takes no arguments.

All of it: [OgreBotAPI.Zone](Zone.md)

**Returns:** OgreBotAPI.Zone object: never NULL; as text it reads OgreBotAPI.Zone.

```text
echo ${OgreBotAPI.Zone}
```

## Methods

### `ArcannaseEffigyOfRebirth`

`OgreBotAPI:ArcannaseEffigyOfRebirth[fw]`

Double-clicks the nearest Arcanna'se Effigy Of Rebirth, at once. Nothing happens, silently, when none is within a distance of 3.5.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI:ArcannaseEffigyOfRebirth[all]
```

*Was (OldBot):* `OgreBotAPI:ArcannaseEffigyOfRebirth`

### `DoVDebuff`

`OgreBotAPI:DoVDebuff[fw, mob, allowMoving=setting]`

Queues your archetype's raid debuff on the mob: Demoralizing Swipe (fighter), Slice of Despair (scout), Pall of the Elements (mage) or Divine Despair (priest). It is skipped when the ability is 5 seconds or more from ready, or the mob is out of range and moving is not allowed; a missing mob, ability or archetype echoes a line and does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `mob` | string |  | The mob: an actor ID, or a name (the nearest actor whose name contains it). |
| `allowMoving` | bool | `setting` | TRUE walks into range first when the mob is too far away (the range is the ability export's); FALSE skips the cast instead. Left out, the DoV raid debuff "allow moving" setting decides. |

```text
OgreBotAPI:DoVDebuff[all,${Target.ID}]
```

*Was (OldBot):* `OgreBotAPI:DoVDebuff`

### `DoVDebuff_Half`

`OgreBotAPI:DoVDebuff_Half[fw, mob, archetype=auto, odd=TRUE, allowMoving=setting]`

Like DoVDebuff, but only characters of one archetype cast, and only half of them: the odd or even ranks when that archetype's raid members (group members outside a raid) are ordered by character ID. Most refusals are silent - a different archetype, the other half, or no DoV debuff found on the mob when archetype is auto.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `mob` | string |  | The mob: an actor ID, or a name (the nearest actor whose name contains it). |
| `archetype` | string | `auto` | fighter, scout, mage or priest - the archetype that casts. auto reads the mob's effects for a DoV raid debuff icon and uses that archetype. |
| `odd` | bool | `TRUE` | TRUE: the odd ranks (1st, 3rd, ...) cast; FALSE: the even ranks. |
| `allowMoving` | bool | `setting` | TRUE walks into range first when the mob is too far away; FALSE skips the cast instead. Left out, the DoV raid debuff "allow moving" setting decides. |

```text
OgreBotAPI:DoVDebuff_Half[all,${Target.ID},auto,TRUE]
```

*Was (OldBot):* `OgreBotAPI:DoVDebuff_Half`

### `F2PWindow_SetOptions`

`OgreBotAPI:F2PWindow_SetOptions[fw]`

Ticks the Settings tab option that closes the All-Access upsell window, which the bot then checks about every 100 seconds, and echoes that the watcher is enabled; with no OgreBot profile loaded the option is not ticked, though the echo still prints.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI:F2PWindow_SetOptions[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:F2PWindow_SetOptions`

### `GetFlag`

`OgreBotAPI:GetFlag[fw]`

Queues a job that talks to the guild strategist and takes a tactical rally banner (conversation reply 3). It echoes and stops when no strategist is within a distance of 10 or you already carry a banner.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI:GetFlag[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:GetFlag`

### `NoTarget`

`OgreBotAPI:NoTarget[fw]`

Clears your target at once (the game's /target_none).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI:NoTarget[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:NoTarget`

### `Prepare_TankSwapping`

`OgreBotAPI:Prepare_TankSwapping[fw]`

Gets the group ready for tank swapping: Guardians turn off Recapture, Bruisers turn off and cancel Hostility and Alternate: Shiftiness, and fighters tick the option to cast no force-target abilities. Everyone also cancels Subtle Strikes, drops the TankSwap no-offensive hold and clears the threat ignore list, all at once (not queued).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI:Prepare_TankSwapping[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Prepare_TankSwapping`

### `Remove_Prepare_TankSwapping`

`OgreBotAPI:Remove_Prepare_TankSwapping[fw]`

Undoes Prepare_TankSwapping: Guardians turn Recapture back on, Bruisers turn Hostility and Alternate: Shiftiness back on in the cast stack (they are not recast), and fighters untick the no force-target option. Everyone also cancels Subtle Strikes, drops the TankSwap no-offensive hold and clears the threat ignore list.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI:Remove_Prepare_TankSwapping[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Remove_Prepare_TankSwapping`

### `ResetFor_Intercept`

`OgreBotAPI:ResetFor_Intercept[fw]`

Turns back on exactly the cast stack entries SetUpFor_Intercept turned off on this character, so an Intercept that was already off stays off. The Guardian entry is touched on a Guardian only.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI:ResetFor_Intercept[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:ResetFor_Intercept`

### `Scribe_Empyral`

`OgreBotAPI:Scribe_Empyral[fw, nameFilter=Empyral]`

Queues a job that scribes every scribeable item in your bags whose name contains nameFilter, one at a time, then opens and closes the knowledge book so new recipes show. Pass * to scribe everything scribeable; when nothing matches it echoes that and does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `nameFilter` | string | `Empyral` | Text the item name must contain (case-insensitive), or * for every scribeable item. |

```text
OgreBotAPI:Scribe_Empyral[${Me.Name},Empyral]
```

*Was (OldBot):* `OgreBotAPI:Scribe_Empyral`

### `SetUpFor_Intercept`

`OgreBotAPI:SetUpFor_Intercept[fw]`

Turns the Intercept ability off in the cast stack on every class, and on a Guardian also the Guardian ability, cancelling the Guardian buff it is maintaining. The bot does this itself before it casts Intercept when the game says a groupmate needs it; ResetFor_Intercept puts back what this turned off.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI:SetUpFor_Intercept[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:SetUpFor_Intercept`

### `Special`

`OgreBotAPI:Special[fw]`

Double-clicks the nearest interactable actor whose type contains "special" (a clickable object), at once. There is no range limit, and nothing happens when there is none.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI:Special[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Special`, `call Obj_OgreIH.Specialwait`, `call Obj_OgreUtilities.HandleClickActor_Special`

### `Target`

`OgreBotAPI:Target[fw, target]`

Targets an actor once, at top priority, on the bot's next pulse (even while paused); it does not hold the target, so auto-target or assist may change it later. me or your own name targets yourself; a blank target or one that resolves to nothing does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `target` | string |  | Who to target: an actor ID, me, an @role, pet:&lt;owner>, or a name (the nearest actor whose name contains it). |

```text
OgreBotAPI:Target[all,${Target.ID}]
```

*Was (OldBot):* `OgreBotAPI:Target`, `call Obj_OgreUtilities.DoTarget`

### `TargetLock`

`OgreBotAPI:TargetLock[fw, target=clear]`

Locks your target onto one actor and keeps it there, above auto-target and assist, until you clear it, a LetsGo runs or you change zone; a new lock replaces the old one. clear, off, 0 or a blank target releases the lock, and a target that resolves to nothing leaves the current lock as it is.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `target` | string | `clear` | The actor to lock onto: an actor ID, an @role, pet:&lt;owner>, or a name (the nearest actor whose name contains it); clear, off or 0 releases the lock. |

```text
OgreBotAPI:TargetLock[all,${Target.ID}]
```

*Was (OldBot):* `OgreBotAPI:TargetLock`

### `UpdateNPCTarget`

`OgreBotAPI:UpdateNPCTarget[fw]`

Re-reads your NPC target right now: your target if it is a live NPC, otherwise your target's target. The bot already does this every frame in the world, so a script only needs it to see a target change within the same frame.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI:UpdateNPCTarget[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:UpdateNPCTarget`

### `UseFlag`

`OgreBotAPI:UseFlag[fw]`

Queues a job that talks to the guild strategist and picks reply 2, which sends you to your guild's rally point. It echoes and stops when no strategist is within a distance of 10; a Brigand's Safehouse is cancelled first.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI:UseFlag[igw:${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:UseFlag`
