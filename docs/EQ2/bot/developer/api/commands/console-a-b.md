# Console commands: A-B

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## `-AbilityEmbargo`

`-AbilityEmbargo <who> <abilityid> <duration> <args>`

Also: `-AbilityRotate`

Embargo an ability (its name or id) for N seconds on the toons the for-who names (an ability rotation: the caster tells the others not to cast it).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who embargoes - leave blank to use the For Who window; `all` = every session that hears it. |
| `abilityid` | string |  |  |
| `duration` | string |  |  |
| `args` | rest |  |  |

Runs: `OgreBotAPI.Abilities:AddEmbargo`

```text
oc !c -AbilityEmbargo all 1234567890 15
```

## `-AbilityEmbargo_ResetAbilityEmbargo`

`-AbilityEmbargo_ResetAbilityEmbargo <who> <value>`

Clears the embargo on one ability, given by name or id, on the matching characters. A name that cannot be found (including the default Unknown) does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string | `Unknown` |  |

Runs: `OgreBotAPI.Abilities:ClearEmbargo`

```text
oc !c -AbilityEmbargo_ResetAbilityEmbargo all 1234567890
```

## `-AbilityEmbargo_ResetAllAbilityEmbargos`

`-AbilityEmbargo_ResetAllAbilityEmbargos <who>`

Clears every ability embargo on the matching characters, so their cast stacks may cast those abilities again. Item embargos are not touched.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Abilities:ClearAllEmbargos`

```text
oc !c -AbilityEmbargo_ResetAllAbilityEmbargos all
```

## `-AbilityTag_ResetAbilityTagAllow`

`-AbilityTag_ResetAbilityTagAllow <who> <value>`

Clears one held allow tag, by name, on the matching characters. A blank tag does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string | `Unknown` |  |

Runs: `OgreBotAPI.CastStack:ClearAllow`

```text
oc !c -AbilityTag_ResetAbilityTagAllow all Stifle
```

## `-AbilityTag_ResetAbilityTagEmbargo`

`-AbilityTag_ResetAbilityTagEmbargo <who> <value>`

Also: `-AbilityEmbargo_ResetAbilityTagEmbargo`

Clears one held embargo tag, by name, on the matching characters. A blank tag does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string | `Unknown` |  |

Runs: `OgreBotAPI.CastStack:ClearEmbargo`

```text
oc !c -AbilityTag_ResetAbilityTagEmbargo all Stifle
```

## `-AbilityTag_ResetAllAbilityTagAllows`

`-AbilityTag_ResetAllAbilityTagAllows <who>`

Clears every held allow tag on the matching characters, so entries that need an allow tag stop casting until one is held again.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.CastStack:ClearAllAllows`

```text
oc !c -AbilityTag_ResetAllAbilityTagAllows all
```

## `-AbilityTag_ResetAllAbilityTagEmbargos`

`-AbilityTag_ResetAllAbilityTagEmbargos <who>`

Clears every held embargo tag on the matching characters, so entries those tags were blocking may cast again.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.CastStack:ClearAllEmbargos`

```text
oc !c -AbilityTag_ResetAllAbilityTagEmbargos all
```

## `-AbilityTagEmbargo`

`-AbilityTagEmbargo <who> <tagname> <duration> <type> <args>`

Also: `-AbilityTagRotate`, `-AbilityTag`

Holds a cast stack tag on the matching characters for duration seconds: type Embargo (the default) stops entries carrying that embargo tag from casting, and type Allow lets entries that need that allow tag cast. It only takes effect while the Settings tab's Enable Tag Embargo or Enable Tag Allow box is ticked; -m &lt;buff> in the extra arguments ties the tag to a maintained buff, and a missing or 0 duration ends it at once.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `tagname` | string |  |  |
| `duration` | string |  |  |
| `type` | string | `Embargo` |  |
| `args` | rest |  |  |

Runs: `OgreBotAPI.CastStack:HoldTag`

```text
oc !c -AbilityTagEmbargo all Stifle 20 Embargo
```

## `-AbilityTracker_Add`

`-AbilityTracker_Add <who> <abilityname>`

Adds the named ability to the Ability Tracker watch list (an id is stored as the ability's name) and echoes the result. The name is not checked against the export, one already on the list is not added again, and the change is lost unless you save the profile.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `abilityname` | string |  |  |

Runs: `OgreBotAPI.Abilities:TrackerAdd`

```text
oc !c -AbilityTracker_Add ${Me.Name} "Bulwark of Order"
```

## `-AcceptQuest`

`-AcceptQuest <who> <questname>`

Accepts the new-quest offer window that is on screen. It does nothing when the Do not accept quests setting is ticked, and the quest name is not used.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `questname` | string |  |  |

Runs: `OgreBotAPI.Quest:Accept`

```text
oc !c -AcceptQuest igw:${Me.Name}
```

## `-AcceptReward`

`-AcceptReward <who> <num> <windowid>`

Also: `-AReward`

Accepts reward window. If Parameter 2 is Blank or 0 will NOT touch rewards with choices.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `num` | string | `0` | If there choices what reward to pick |
| `windowid` | string | `0` |  |

Runs: `OgreBotAPI.Windows:AcceptReward`

```text
oc !c -AcceptReward igw:${Me.Name} 1 0
```

## `-Actor_Click`

`-Actor_Click <who> <actorname> <exactname>`

Double-clicks an actor right away: a number is taken as an actor id, otherwise it picks the nearest interactable actor whose name contains the text (or matches it exactly when exactname is TRUE). Nothing happens when no such actor is found.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `actorname` | string | `asdf1323` |  |
| `exactname` | string | `FALSE` |  |

Runs: `OgreBotAPI.Actors:Click`

```text
oc !c -Actor_Click ${Me.Name} "Strange Lever" FALSE
```

## `-Actor_ClickQueued`

`-Actor_ClickQueued <who> <actorname> <exactname>`

Picks the actor the same way as -Actor_Click, but puts the click in the action queue: at its turn it double-clicks the actor and waits for the cast bar (4 seconds by default) before the next queued action. If the actor is gone by then, the click is dropped.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `actorname` | string | `asdf1323` |  |
| `exactname` | string | `FALSE` |  |

Runs: `OgreBotAPI.Actors:ClickQueued`

```text
oc !c -Actor_ClickQueued igw:${Me.Name} "Strange Lever" FALSE
```

## `-AddNoOffensiveOn`

`-AddNoOffensiveOn <who> <mobname> <exactmatchonly>`

Adds a mob name to the no-offensive list: while your target matches it, the bot casts no offensive abilities and does not auto-attack. exactmatchonly TRUE (default) needs the exact name, and FALSE matches any name that contains it.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `mobname` | string | `DoesNotExist` |  |
| `exactmatchonly` | bool | `TRUE` | TRUE: only a target with exactly this name. FALSE: any target whose name contains it. |

Runs: `OgreBotAPI.Combat:AddNoOffensive`

```text
oc !c -AddNoOffensiveOn igw:${Me.Name} "${Target.Name}" TRUE
```

## `-Alias_AddEntry`

`-Alias_AddEntry <who> <existingalias> <newalias> <noraid>`

Alias Tab - Adds a new alias entry. Example: To add: *Tank=Bob.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `existingalias` | string |  | Alias: *Tank |
| `newalias` | string |  | Alias name: Bob |
| `noraid` | string | `FALSE` | No raid scanning |

Runs: `OgreBotAPI.ForWho:AddAlias`

```text
oc !c -Alias_AddEntry igw:${Me.Name} *Tank ${Group[1].Name} FALSE
```

## `-Alias_ChangeEntryAlias`

`-Alias_ChangeEntryAlias <who> <existingalias> <newalias> <silentmode>`

Alias Tab - Changes an alias entry. Example: If an entry has *Tank=Bob - you could change all *Tank to *OffTank.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `existingalias` | string |  | Alias. Example: *Tank |
| `newalias` | string |  | New alias name. OffTank |
| `silentmode` | bool | `FALSE` | Suppress the change announcement for this call. TRUE or FALSE. |

Runs: `OgreBotAPI.ForWho:RenameAlias`

```text
oc !c -Alias_ChangeEntryAlias igw:${Me.Name} *Tank *OffTank FALSE
```

## `-Alias_ChangeEntryFor`

`-Alias_ChangeEntryFor <who> <existingalias> <newalias> <silentmode>`

Also: `-Alias_ChangeEntry`

Alias Tab - Changes an alias entry. Example: If an entry has *Tank=Bob - you could change Bob to Alice.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `existingalias` | string |  | Existing alias name. Example: Bob |
| `newalias` | string |  | New alias name. Example: Alice |
| `silentmode` | bool | `FALSE` | Suppress the change announcement for this call. TRUE or FALSE. |

Runs: `OgreBotAPI.ForWho:ChangeAlias`

```text
oc !c -Alias_ChangeEntryFor igw:${Me.Name} ${Group[1].Name} ${Me.Name} FALSE
```

## `-Alias_RemoveEntry`

`-Alias_RemoveEntry <who> <existingalias>`

Deletes the named alias (the leading * is optional) from the Aliases tab of the matched toons, and all (the default) or a blank name deletes every alias. Only the first row with that name goes, and the change lasts once the profile is saved.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `existingalias` | string | `all` |  |

Runs: `OgreBotAPI.ForWho:RemoveAlias`

```text
oc !c -Alias_RemoveEntry igw:${Me.Name} *Tank
```

## `-AltarOfTheAncients`

`-AltarOfTheAncients <who>`

Prays at the Altar Of The Ancients. Note: You need to be REALLY close to it.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Actors:ClickQueued`

```text
oc !c -AltarOfTheAncients ${Me.Name}
```

## `-ApplyVerb`

`-ApplyVerb <who> <actorname> <verb>`

Also: `-Apply_Verb`

Apply a verb to an actor by name [Actor name] [case sensitive verb] - on the toons the for-who names. Note - This is an advanced button.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who acts - leave blank to use the For Who window. |
| `actorname` | string | `All` | The actor's name or part of it, any case, or a type word: npc, namednpc, nokillnpc, pc, special, chest, resource, door |
| `verb` | string | `All` | verb - case sensitive |

Runs: `OgreBotAPI.Actors:ApplyVerb`

```text
oc !c -ApplyVerb igw:${Me.Name} "${Target.Name}" Use
```

## `-ApplyVerbID`

`-ApplyVerbID <who> <actorid> <verb>`

Apply a verb to an actor by its ID [Actor ID] [case sensitive verb] - on the toons the for-who names. Note - This is an advanced button.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who acts - leave blank to use the For Who window. |
| `actorid` | string | `0` | Actor ID |
| `verb` | string | `All` | verb - case sensitive |

Runs: `OgreBotAPI.Actors:ApplyVerbID`

```text
oc !c -ApplyVerbID igw:${Me.Name} ${Target.ID} Use
```

## `-ApplyVerbIDQueued`

`-ApplyVerbIDQueued <who> <actorid> <verb>`

Apply a verb to an actor by its ID, then wait out the cast it starts [Actor ID] [case sensitive verb] - on the toons the for-who names. Waits its turn in the action queue, then up to 5 seconds for a free cast bar. Note - This is an advanced button.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who acts - leave blank to use the For Who window. |
| `actorid` | string | `0` | Actor ID |
| `verb` | string | `All` | verb - case sensitive |

Runs: `OgreBotAPI.Actors:ApplyVerbIDQueued`

```text
oc !c -ApplyVerbIDQueued igw:${Me.Name} ${Target.ID} Use
```

## `-ApplyVerbQueued`

`-ApplyVerbQueued <who> <actorname> <verb>`

Apply a verb to an actor by name, then wait out the cast it starts [Actor name] [case sensitive verb] - on the toons the for-who names. Waits its turn in the action queue, then up to 5 seconds for a free cast bar. Note - This is an advanced button.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who acts - leave blank to use the For Who window. |
| `actorname` | string | `All` | The actor's name or part of it, any case, or a type word: npc, namednpc, nokillnpc, pc, special, chest, resource, door |
| `verb` | string | `All` | verb - case sensitive |

Runs: `OgreBotAPI.Actors:ApplyVerbQueued`

```text
oc !c -ApplyVerbQueued igw:${Me.Name} "${Target.Name}" Use
```

## `-ArcannaseEffigyOfRebirth`

`-ArcannaseEffigyOfRebirth <who>`

Use Arcanna'se Effigy Of Rebirth (KA's statue). Note: You need to be REALLY close to it.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI:ArcannaseEffigyOfRebirth`

```text
oc !c -ArcannaseEffigyOfRebirth ${Me.Name}
```

## `-assist`

`-assist <who> <assistwho>`

Also: `-ass`

Sets assists from parameters.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `assistwho` | string | `${Me.Name}` | Player to assist |

Runs: `OgreBotAPI.Assist:Anchor`

```text
oc !c -assist all ${Me.Name}
```

## `-AssistForWho`

`-AssistForWho <who> <assistwho>`

Sets who the toon assists: from the next pulse it takes its targets from the named player (an alias such as @role works too). A blank name makes the toon assist itself, so it becomes the one others assist.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `assistwho` | string | `${Me.Name}` |  |

Runs: `OgreBotAPI.Assist:Anchor`

```text
oc !c -AssistForWho igw:${Me.Name} ${Me.Name}
```

## `-AuthIfInRaid`

`-AuthIfInRaid <nick> <value>`

Also: `-AIIR`

Authorize an IRC nick if the given toon is in my raid. Runs on every session by design; the first argument is the nick, not a for-who.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `nick` | string | `SupposeToPassAParameterHere` | The IRC nick to authorize. Not a for-who: this row runs on every session on purpose, each checking its own raid. |
| `value` | string |  | The toon that must be in my raid for the nick to be authorized (default: me). |

Runs: `OgreBotAPI.Comms:IrcAuthIfInRaid`

```text
oc !c -AuthIfInRaid ${Group[1].Name} ${Me.Name}
```

## `-AutoConsumeTemporaryFamiliarExperience`

`-AutoConsumeTemporaryFamiliarExperience <who>`

Auto Consumes Temporary Familiar Experience items

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Inventory:AutoConsumeFamiliarXP`

```text
oc !c -AutoConsumeTemporaryFamiliarExperience ${Me.Name}
```

## `-AutoConsumeTemporaryMountTrainingReduction`

`-AutoConsumeTemporaryMountTrainingReduction <who>`

Auto Consumes Temporary Mount Training Reduction items

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Inventory:AutoConsumeMountTraining`

```text
oc !c -AutoConsumeTemporaryMountTrainingReduction ${Me.Name}
```

## `-AutoConsumeTemporaryResearchReduction`

`-AutoConsumeTemporaryResearchReduction <who>`

Auto Consumes Temporary Research Reduction items

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Inventory:AutoConsumeResearch`

```text
oc !c -AutoConsumeTemporaryResearchReduction ${Me.Name}
```

## `-AutoCure`

`-AutoCure <who> <toonname> <args>`

Ask the curers to cure a toon. No kinds = arcane, elemental, noxious and trauma; name kinds (arcane/a, elemental/e, noxious/n, trauma/t, curse, confrontfear) to cure only those. Options: -AutoRemove &lt;seconds> (give up after this long, default 8), -tag &lt;name> (a name -AutoCureRemove can cancel it by). Any other word refuses the request.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `toonname` | string |  |  |
| `args` | rest |  | Kinds, then options: -AutoRemove &lt;seconds>, -tag &lt;name> |

Runs: `OgreBotAPI.Cures:Request`

```text
oc !c -AutoCure igw:${Me.Name} ${Group[1].Name} trauma
```

## `-AutoCureRemove`

`-AutoCureRemove <who> <toonortag>`

Cancel the curse, cure (-AutoCure) and group cure (-AutoGroupCure) requests for a toon or tag.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `toonortag` | string |  | The toon the requests were for, or the -tag they were given |

Runs: `OgreBotAPI.Cures:CancelRequests`

```text
oc !c -AutoCureRemove igw:${Me.Name} ${Me.Name}
```

## `-AutoCurse`

`-AutoCurse <who> <toonname> <args>`

Ask the curers to cure a curse off a toon. Options: -AutoRemove &lt;seconds> (give up after this long, default 8), -tag &lt;name> (a name -AutoCureRemove can cancel it by). Any other word refuses the request.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `toonname` | string |  | The cursed toon |
| `args` | rest |  | Options: -AutoRemove &lt;seconds>, -tag &lt;name> |

Runs: `OgreBotAPI.Cures:RequestCurse`

```text
oc !c -AutoCurse igw:${Me.Name} ${Me.Name} -AutoRemove 20
```

## `-AutoGroupCure`

`-AutoGroupCure <who> <args>`

Cast the group cure once enough of the group carry a detriment. Kinds: arcane/a, elemental/e, noxious/n, trauma/t (none named = any of the four; each kind is counted on its own). Options: -count &lt;n> (at least n of you and the group, default 1), -AutoRemove &lt;seconds> (watch this long, default 8), -tag &lt;name> (a name -AutoCureRemove can cancel it by). Any other word refuses the request.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `args` | rest |  | Kinds, then options: -count &lt;n>, -AutoRemove &lt;seconds>, -tag &lt;name> |

Runs: `OgreBotAPI.Cures:RequestGroupWatch`

```text
oc !c -AutoGroupCure igw:${Me.Name} arcane trauma -count 3
```

## `-autohunt`

`-autohunt <who> <mode>`

Set the Auto-Hunt driver mode: off (stop) or hunt (full grind - scan, camp, prebuff, pull, and walk the path picked on the Auto-Hunt tab between pulls).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `mode` | string | `hunt` | off \| hunt (default hunt). |

Runs: `OgreBotAPI.AutoHunt:SetMode`

```text
oc !c -autohunt ${Me.Name} hunt
```

## `-AutoItemCure`

`-AutoItemCure <who> <type>`

Ask the matched toons to cure themselves with a Cure &lt;type> potion from their bags. A potion only cures its drinker, so there is no victim argument - whoever the for-who matches is who drinks. Leave the type blank for whatever they are actually afflicted with.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `type` | string |  | arcane, elemental, noxious or trauma. Blank (or 'any') = whatever is needed, decided when the potion is actually drunk. |

Runs: `OgreBotAPI.Cures:RequestItem`

```text
oc !c -AutoItemCure igw:${Me.Name} noxious
```

## `-AutoRun`

`-AutoRun <who>`

Presses the auto run key.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.Movement:AutoRun`

```text
oc !c -AutoRun igw:${Me.Name}
```

## `-AutoTarget_AddActor`

`-AutoTarget_AddActor <who> <actorname> <hp> <aggroongrouponly> <checkcollision> <maxhp> <aggroonnonfighteronly> <aggroonnotme> <keeplast>`

Also: `-AT_Add`

Adds an entry to the matched toons' AutoTarget working list: the actor name with minimum and maximum HP and its aggro and collision checks, with aggroongrouponly defaulting to TRUE. A blank name adds nothing, and new entries go in above an entry marked keeplast.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `actorname` | string |  |  |
| `hp` | int64 | `0` |  |
| `aggroongrouponly` | string | `TRUE` |  |
| `checkcollision` | string | `FALSE` |  |
| `maxhp` | int64 | `0` |  |
| `aggroonnonfighteronly` | string | `FALSE` |  |
| `aggroonnotme` | string | `FALSE` |  |
| `keeplast` | string | `FALSE` | TRUE: this entry stays last - every later add goes in above it (the IC's named; adds go before the named) |

Runs: `OgreBotAPI.AutoTarget:AddActor`

```text
oc !c -AutoTarget_AddActor igw:${Me.Name} "a frost giant" 0 TRUE FALSE 0 FALSE FALSE FALSE
```

## `-AutoTarget_Clear`

`-AutoTarget_Clear <who>`

Empties the current AutoTarget list and forgets which saved list was loaded. Saved lists are not touched.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.AutoTarget:Clear`

```text
oc !c -AutoTarget_Clear igw:${Me.Name}
```

## `-AutoTarget_ClearActors`

`-AutoTarget_ClearActors <who>`

Also: `-AT_Clear`

Empties the AutoTarget working list on the matched toons, so no list is loaded any more.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |

Runs: `OgreBotAPI.AutoTarget:Clear`

```text
oc !c -AutoTarget_ClearActors igw:${Me.Name}
```

## `-AutoTarget_Disable`

`-AutoTarget_Disable <who> <key>`

Also: `-AT_Disable`

Pauses automatic targeting under the key you give: assist, AutoTarget and the other automatic sources stop changing target, and the current target is held until that key is released with -AutoTarget_Enable. A blank key does nothing, each key releases on its own, and a zone change clears them all.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `key` | string |  |  |

Runs: `OgreBotAPI.AutoTarget:Suppress`

```text
oc !c -AutoTarget_Disable igw:${Me.Name} MyScript
```

## `-AutoTarget_Enable`

`-AutoTarget_Enable <who> <key>`

Also: `-AT_Enable`

Releases the automatic-targeting pause held under the key you give; targeting resumes once no key is left holding it. A blank key does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `key` | string |  |  |

Runs: `OgreBotAPI.AutoTarget:Release`

```text
oc !c -AutoTarget_Enable igw:${Me.Name} MyScript
```

## `-AutoTarget_RemoveActor`

`-AutoTarget_RemoveActor <who> <actorname>`

Also: `-AT_Remove`

Removes every AutoTarget entry matching the actor name - only that actor's entries, the rest of the list stays.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `actorname` | string |  |  |

Runs: `OgreBotAPI.AutoTarget:RemoveActor`

```text
oc !c -AutoTarget_RemoveActor igw:${Me.Name} "a frenzied ghoul"
```

## `-AutoTarget_SetScanHeight`

`-AutoTarget_SetScanHeight <who> <value>`

Also: `-AT_Height`

AutoTarget - Sets a new scan height.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | int64 | `5` | New scan height. Example: 5 |

Runs: `OgreBotAPI.AutoTarget:SetScanHeight`

```text
oc !c -AutoTarget_SetScanHeight igw:${Me.Name} 5
```

## `-AutoTarget_SetScanRadius`

`-AutoTarget_SetScanRadius <who> <value>`

Also: `-AT_Scan`

AutoTarget - Sets a new scan radius.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | int64 | `50` | New scan radius. Example: 50 |

Runs: `OgreBotAPI.AutoTarget:SetScanRadius`

```text
oc !c -AutoTarget_SetScanRadius igw:${Me.Name} 50
```

## `-AutoTargetOCSToggle`

`-AutoTargetOCSToggle <who> <value> <silent>`

Also: `-ATOCST`

Turns AutoTarget's out-of-combat scanning on (TRUE), off (FALSE) or flips it (TOGGLE, the default) on the matched toons. silent TRUE skips the change announcement.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string | `TOGGLE` |  |
| `silent` | bool | `FALSE` |  |

Runs: `OgreBotAPI.Options:Set`

```text
oc !c -AutoTargetOCSToggle igw:${Me.Name} TOGGLE FALSE
```

## `-AutoTargetToggle`

`-AutoTargetToggle <who> <value> <silent>`

Also: `-ATT`

Turns AutoTarget on (TRUE), off (FALSE) or flips it (TOGGLE, the default) on the matched toons. silent TRUE skips the change announcement.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `value` | string | `TOGGLE` |  |
| `silent` | bool | `FALSE` |  |

Runs: `OgreBotAPI.Options:Set`

```text
oc !c -AutoTargetToggle igw:${Me.Name} TRUE FALSE
```

## `-BuyFromMerchant`

`-BuyFromMerchant <who> <itemname> <value>`

Buys the quantity (default 1) of the named item from the merchant window that is already open, and accepts the purchase prompt if one comes up. No item, no merchant window, or an item the merchant does not sell each get one line.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `who` | forwho | `auto` | Who to target - leave blank to use the For Who window. |
| `itemname` | string |  |  |
| `value` | string | `1` |  |

Runs: `OgreBotAPI.Merchant:Buy`

```text
oc !c -BuyFromMerchant ${Me.Name} "Bundle of Arrows" 2
```
