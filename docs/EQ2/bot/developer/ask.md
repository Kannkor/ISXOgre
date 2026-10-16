# Ask query system

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../index.md).
</div>

The calls Classic's *Ask Query System* page described - one question asked of the whole group, answered by every session - and what each one is in the new bot.

> **:warning: An old call does nothing now - it does not give an error**
>
> The new bot does not keep the old names. A call to an old method silently does nothing and a read of an old member gives `NULL`. Find your name below and write what the row says instead.

## At a glance

| What happened | Names |
|---|---|
| ➡️ Lives somewhere else | 20 |
| ✅ Works as is | 1 |
| **Total** | **21** |

## The Ask calls

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreBotAPI:Ask` | does nothing | IC file: the `groupQuery` step (ic-actions/09-groupQuery.md) - counts, allYes / anyYes / allNo / anyNo, per-member flags, raw answers, ready-made for-who lists. Script: the same engine - ${ISXOgreEQ2.Comms.GroupQuery[&lt;fw&gt;, -question, &lt;question&gt;, ...]} starts it and reads as its id; then ${ISXOgreEQ2.Comms.GroupQuery.Done[id]} / .Result[id] (JSON, the same names), or the event OgreEvent_GroupQueryDone(id, json). | ➡️ Lives somewhere else |  |
| `call OgreBotAPI.Ask_AllFalse` | does nothing | IC file: the `groupQuery` step (ic-actions/09-groupQuery.md) - counts, allYes / anyYes / allNo / anyNo, per-member flags, raw answers, ready-made for-who lists. Script: the same engine - ${ISXOgreEQ2.Comms.GroupQuery[&lt;fw&gt;, -question, &lt;question&gt;, ...]} starts it and reads as its id; then ${ISXOgreEQ2.Comms.GroupQuery.Done[id]} / .Result[id] (JSON, the same names), or the event OgreEvent_GroupQueryDone(id, json). | ➡️ Lives somewhere else |  |
| `call OgreBotAPI.Ask_AllTrue` | does nothing | IC file: the `groupQuery` step (ic-actions/09-groupQuery.md) - counts, allYes / anyYes / allNo / anyNo, per-member flags, raw answers, ready-made for-who lists. Script: the same engine - ${ISXOgreEQ2.Comms.GroupQuery[&lt;fw&gt;, -question, &lt;question&gt;, ...]} starts it and reads as its id; then ${ISXOgreEQ2.Comms.GroupQuery.Done[id]} / .Result[id] (JSON, the same names), or the event OgreEvent_GroupQueryDone(id, json). | ➡️ Lives somewhere else |  |
| `call OgreBotAPI.Ask_AnyFalse` | does nothing | IC file: the `groupQuery` step (ic-actions/09-groupQuery.md) - counts, allYes / anyYes / allNo / anyNo, per-member flags, raw answers, ready-made for-who lists. Script: the same engine - ${ISXOgreEQ2.Comms.GroupQuery[&lt;fw&gt;, -question, &lt;question&gt;, ...]} starts it and reads as its id; then ${ISXOgreEQ2.Comms.GroupQuery.Done[id]} / .Result[id] (JSON, the same names), or the event OgreEvent_GroupQueryDone(id, json). | ➡️ Lives somewhere else |  |
| `call OgreBotAPI.Ask_AnyTrue` | does nothing | IC file: the `groupQuery` step (ic-actions/09-groupQuery.md) - counts, allYes / anyYes / allNo / anyNo, per-member flags, raw answers, ready-made for-who lists. Script: the same engine - ${ISXOgreEQ2.Comms.GroupQuery[&lt;fw&gt;, -question, &lt;question&gt;, ...]} starts it and reads as its id; then ${ISXOgreEQ2.Comms.GroupQuery.Done[id]} / .Result[id] (JSON, the same names), or the event OgreEvent_GroupQueryDone(id, json). | ➡️ Lives somewhere else |  |
| `OgreBotAPI:Ask_ClearQuery` | does nothing | `ISXOgreEQ2.Comms:Query_Clear[<fw>, id] (a finished QueryBus result also clears itself after 60 s).` | ➡️ Lives somewhere else | gained a for-who; it had none. |
| `OgreBotAPI.Ask_Count` | reads NULL | `ISXOgreEQ2.Comms.Query_Count[id] / Query_TrueCount[id] / Query_Json[id] (the QueryBus tally of a Comms:Query).` | ➡️ Lives somewhere else |  |
| `OgreBotAPI.Ask_CountBy` | reads NULL | No replacement as a member: groupQuery works out who was asked from the leader's roster and sendTo, and ends the query when they have all answered. In a script, count the roster yourself (ISXOgreEQ2.Roster). | ➡️ Lives somewhere else |  |
| `OgreBotAPI.Ask_Counter` | reads NULL | IC file: the `groupQuery` step (ic-actions/09-groupQuery.md) - counts, allYes / anyYes / allNo / anyNo, per-member flags, raw answers, ready-made for-who lists. Script: the same engine - ${ISXOgreEQ2.Comms.GroupQuery[&lt;fw&gt;, -question, &lt;question&gt;, ...]} starts it and reads as its id; then ${ISXOgreEQ2.Comms.GroupQuery.Done[id]} / .Result[id] (JSON, the same names), or the event OgreEvent_GroupQueryDone(id, json). | ➡️ Lives somewhere else |  |
| `OgreBotAPI.Ask_CountForToken` | reads NULL | No replacement as a member: groupQuery works out who was asked from the leader's roster and sendTo, and ends the query when they have all answered. In a script, count the roster yourself (ISXOgreEQ2.Roster). | ➡️ Lives somewhere else |  |
| `call OgreBotAPI.Ask_CountTrue` | does nothing | IC file: the `groupQuery` step (ic-actions/09-groupQuery.md) - counts, allYes / anyYes / allNo / anyNo, per-member flags, raw answers, ready-made for-who lists. Script: the same engine - ${ISXOgreEQ2.Comms.GroupQuery[&lt;fw&gt;, -question, &lt;question&gt;, ...]} starts it and reads as its id; then ${ISXOgreEQ2.Comms.GroupQuery.Done[id]} / .Result[id] (JSON, the same names), or the event OgreEvent_GroupQueryDone(id, json). | ➡️ Lives somewhere else |  |
| `OgreBotAPI.Ask_ExpectedFor` | reads NULL | No replacement as a member: groupQuery works out who was asked from the leader's roster and sendTo, and ends the query when they have all answered. In a script, count the roster yourself (ISXOgreEQ2.Roster). | ➡️ Lives somewhere else |  |
| `OgreBotAPI.Ask_IsRaidScope` | reads NULL | No replacement as a member: groupQuery works out who was asked from the leader's roster and sendTo, and ends the query when they have all answered. In a script, count the roster yourself (ISXOgreEQ2.Roster). | ➡️ Lives somewhere else |  |
| `call OgreBotAPI.Ask_Json` | does nothing | IC file: the `groupQuery` step (ic-actions/09-groupQuery.md) - counts, allYes / anyYes / allNo / anyNo, per-member flags, raw answers, ready-made for-who lists. Script: the same engine - ${ISXOgreEQ2.Comms.GroupQuery[&lt;fw&gt;, -question, &lt;question&gt;, ...]} starts it and reads as its id; then ${ISXOgreEQ2.Comms.GroupQuery.Done[id]} / .Result[id] (JSON, the same names), or the event OgreEvent_GroupQueryDone(id, json). | ➡️ Lives somewhere else |  |
| `OgreBotAPI.Ask_JsonFor` | reads NULL | IC file: the `groupQuery` step (ic-actions/09-groupQuery.md) - counts, allYes / anyYes / allNo / anyNo, per-member flags, raw answers, ready-made for-who lists. Script: the same engine - ${ISXOgreEQ2.Comms.GroupQuery[&lt;fw&gt;, -question, &lt;question&gt;, ...]} starts it and reads as its id; then ${ISXOgreEQ2.Comms.GroupQuery.Done[id]} / .Result[id] (JSON, the same names), or the event OgreEvent_GroupQueryDone(id, json). | ➡️ Lives somewhere else |  |
| `OgreBotAPI.Ask_JsonStore` | reads NULL | IC file: the `groupQuery` step (ic-actions/09-groupQuery.md) - counts, allYes / anyYes / allNo / anyNo, per-member flags, raw answers, ready-made for-who lists. Script: the same engine - ${ISXOgreEQ2.Comms.GroupQuery[&lt;fw&gt;, -question, &lt;question&gt;, ...]} starts it and reads as its id; then ${ISXOgreEQ2.Comms.GroupQuery.Done[id]} / .Result[id] (JSON, the same names), or the event OgreEvent_GroupQueryDone(id, json). | ➡️ Lives somewhere else |  |
| `OgreBotAPI.Ask_ResponseCount` | reads NULL | `ISXOgreEQ2.Comms.Query_Count[id] / Query_TrueCount[id] / Query_Json[id] (the QueryBus tally of a Comms:Query).` | ➡️ Lives somewhere else |  |
| `call OgreBotAPI.Ask_Run` | does nothing | IC file: the `groupQuery` step (ic-actions/09-groupQuery.md) - counts, allYes / anyYes / allNo / anyNo, per-member flags, raw answers, ready-made for-who lists. Script: the same engine - ${ISXOgreEQ2.Comms.GroupQuery[&lt;fw&gt;, -question, &lt;question&gt;, ...]} starts it and reads as its id; then ${ISXOgreEQ2.Comms.GroupQuery.Done[id]} / .Result[id] (JSON, the same names), or the event OgreEvent_GroupQueryDone(id, json). | ➡️ Lives somewhere else |  |
| `OgreBotAPI.Ask_TrueCount` | reads NULL | `ISXOgreEQ2.Comms.Query_Count[id] / Query_TrueCount[id] / Query_Json[id] (the QueryBus tally of a Comms:Query).` | ➡️ Lives somewhere else |  |
| `OgreBotAPI.Ask_TrueCountFor` | reads NULL | `ISXOgreEQ2.Comms.Query_Count[id] / Query_TrueCount[id] / Query_Json[id] (the QueryBus tally of a Comms:Query).` | ➡️ Lives somewhere else |  |
| `OgreBotAPI.GE_CheckSkip` | works | — | ✅ Works as is |  |
