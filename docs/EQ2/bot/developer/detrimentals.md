# Detrimentals

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../index.md).
</div>

What Classic's *Detrimentals System* page described - the detrimental members and events of the old `ISXOgre` extension, and the `AskDetrimentals` helper - and what each one is in the new bot.

> **:warning: An old call does nothing now - it does not give an error**
>
> The new bot does not keep the old names. A call to an old method silently does nothing and a read of an old member gives `NULL`. Find your name below and write what the row says instead.

## At a glance

| What happened | Names |
|---|---|
| ➡️ Moved | 20 |
| ➡️ Lives somewhere else | 7 |
| ✅ Works as is | 3 |
| **Total** | **30** |

## Worked examples

One real Classic line per kind of change, and the line that replaces it.

### ➡️ Moved: `ISXOgre.DetrimentalInfo`

```
; before (Classic)
return ${ISXOgre.DetrimentalInfo[${_MainID}, ${_BackDropID}, -actorID, ${_ActorID}, "${_Return}"]}
; after (new bot)
return ${ISXOgreEQ2.Det.DetrimentalInfo[${_MainID}, ${_BackDropID}, -actorID, ${_ActorID}, "${_Return}"]}
```

## ISXOgre detrimental members and events

The old `ISXOgre` extension is not loaded with the new bot, so every `${ISXOgre.…}` read gives `NULL`.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `ISXOgre.DetrimentalInfo` | does nothing | `ISXOgreEQ2.Det.DetrimentalInfo` | ➡️ Moved | This is the direct ISXOgre read. Classic's WRAPPER ${OgreBotAPI.DetrimentalInfo[...]} is a different name and maps to ${OgreBotAPI.Cures.Detrimental}. The new read adds one numeric field, iseffectinfoavailable. |
| `ISXOgre.DetrimentalInfo_JSON` | does nothing | `ISXOgreEQ2.Det.DetrimentalInfo_JSON` | ➡️ Moved | Classic's only sites are commented-out debug echoes in two raid modules. |
| `ISXOgre:DetrimentalCacheClear` | does nothing | `ISXOgreEQ2.Det:DetrimentalCacheClear` | ➡️ Moved |  |
| `ISXOgre:DetrimentalCancel` | does nothing | `ISXOgreEQ2.Det:DetrimentalCancel` | ➡️ Moved | OgreBotAPI.Cures:CancelDetrimental[forwho, main, back] is the fleet-addressed form of the same job. |
| `ISXOgre:Set_DetrimentalScanTime` | does nothing | `ISXOgreEQ2.Det:Set_DetrimentalScanTime` | ➡️ Moved |  |

## AskDetrimentals

**Note A** (7 rows below): IC file: the `groupQuery` step - counts, allYes / anyYes / allNo / anyNo, per-member flags, raw answers, ready-made for-who lists. Script: the same engine - ${ISXOgreEQ2.Comms.GroupQuery[&lt;fw&gt;, -question, &lt;question&gt;, ...]} starts it and reads as its id; then ${ISXOgreEQ2.Comms.GroupQuery.Done[id]} / .Result[id] (JSON, the same names), or the event OgreEvent_GroupQueryDone(id, json).

**Note B** (6 rows below): Det NOT present: Classic answered NULL; the new read answers 0. Test exists first rather than relying on NULL.

**Note C** (4 rows below): An empty answer is now an empty STRING; Classic answered NULL (no object) when the read came back empty or the det was absent. Poll the new numeric field iseffectinfoavailable first: it is the examine-ready gate, so you stop re-reading an empty string.

**Note D** (3 rows below): Two behaviour changes: (1) the diff is keyed on the ICON PAIR, not the effect ID - a recast that gets a new ID is an Updated, not Removed+Added, and two dets with the same icons fire once; still says "ID-keyed" (stale comment). (2) No scan and no events while you are dead.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `event:OgreEvent_OnDetrimentalAdded` | works | — | ✅ Works as is | Note D |
| `event:OgreEvent_OnDetrimentalRemoved` | works | — | ✅ Works as is | Note D |
| `event:OgreEvent_OnDetrimentalUpdated` | works | — | ✅ Works as is | Note D |
| `ISXOgre.DetrimentalInfo[main,back,-actorID,<id>,field]` | does nothing | `ISXOgreEQ2.Det.DetrimentalInfo[main,back,-actorID,<id>,field]` | ➡️ Moved |  |
| `ISXOgre.DetrimentalInfo[main,back,-maxEffects,<n>,field]` | does nothing | `ISXOgreEQ2.Det.DetrimentalInfo[main,back,-maxEffects,<n>,field]` | ➡️ Moved | The default is 7 in the code today, the same as Classic - but the comments beside it say 10. If you need more than 7, pass -maxEffects explicitly. |
| `ISXOgre.DetrimentalInfo[main,back,backdropiconid]` | does nothing | `ISXOgreEQ2.Det.DetrimentalInfo[main,back,backdropiconid]` | ➡️ Moved | Note B |
| `ISXOgre.DetrimentalInfo[main,back,cancel]` | does nothing | `ISXOgreEQ2.Det.DetrimentalInfo[main,back,cancel]` | ➡️ Moved | A read that acts is easy to miss in review - ISXOgreEQ2.Det:DetrimentalCancel[main,back] says the same thing out loud. |
| `ISXOgre.DetrimentalInfo[main,back,currentincrements]` | does nothing | `ISXOgreEQ2.Det.DetrimentalInfo[main,back,currentincrements]` | ➡️ Moved | Note B |
| `ISXOgre.DetrimentalInfo[main,back,Description]` | does nothing | `ISXOgreEQ2.Det.DetrimentalInfo[main,back,Description]` | ➡️ Moved | Note C |
| `ISXOgre.DetrimentalInfo[main,back,duration]` | does nothing | `ISXOgreEQ2.Det.DetrimentalInfo[main,back,duration]` | ➡️ Moved | Note B |
| `ISXOgre.DetrimentalInfo[main,back,exists]` | does nothing | `ISXOgreEQ2.Det.DetrimentalInfo[main,back,exists]` | ➡️ Moved |  |
| `ISXOgre.DetrimentalInfo[main,back,id]` | does nothing | `ISXOgreEQ2.Det.DetrimentalInfo[main,back,id]` | ➡️ Moved | Note B |
| `ISXOgre.DetrimentalInfo[main,back,mainiconid]` | does nothing | `ISXOgreEQ2.Det.DetrimentalInfo[main,back,mainiconid]` | ➡️ Moved | Note B |
| `ISXOgre.DetrimentalInfo[main,back,maxduration]` | does nothing | `ISXOgreEQ2.Det.DetrimentalInfo[main,back,maxduration]` | ➡️ Moved | Note B |
| `ISXOgre.DetrimentalInfo[main,back,Name]` | does nothing | `ISXOgreEQ2.Det.DetrimentalInfo[main,back,Name]` | ➡️ Moved | Note C |
| `ISXOgre.DetrimentalInfo[main,back,Type]` | does nothing | `ISXOgreEQ2.Det.DetrimentalInfo[main,back,Type]` | ➡️ Moved | Note C |
| `ISXOgre.DetrimentalInfo[main,back,UsesRemaining]` | does nothing | `ISXOgreEQ2.Det.DetrimentalInfo[main,back,UsesRemaining]` | ➡️ Moved | Note C |
| `ISXOgre.DetrimentalInfo_JSON[main,back,-ExtraFields]` | does nothing | `ISXOgreEQ2.Det.DetrimentalInfo_JSON[main,back,-ExtraFields]` | ➡️ Moved | The extra fields are live server reads, empty on the first touch - the same caveat the doc gave. |
| `OgreBotAPI.Ask` | does nothing | `ISXOgreEQ2.Comms:Query` | ➡️ Lives somewhere else | Note A |
| `OgreBotAPI.Ask_AllFalse` | does nothing | `ISXOgreEQ2.Comms:Query` | ➡️ Lives somewhere else | Note A |
| `OgreBotAPI.Ask_AllTrue` | does nothing | `ISXOgreEQ2.Comms:Query` | ➡️ Lives somewhere else | Note A |
| `OgreBotAPI.Ask_AnyFalse` | does nothing | `ISXOgreEQ2.Comms:Query` | ➡️ Lives somewhere else | Note A |
| `OgreBotAPI.Ask_AnyTrue` | does nothing | `ISXOgreEQ2.Comms:Query` | ➡️ Lives somewhere else | Note A |
| `OgreBotAPI.Ask_CountTrue` | does nothing | `ISXOgreEQ2.Comms:Query` | ➡️ Lives somewhere else | Note A |
| `OgreBotAPI.Ask_Json` | does nothing | `ISXOgreEQ2.Comms:Query` | ➡️ Lives somewhere else | Note A |
