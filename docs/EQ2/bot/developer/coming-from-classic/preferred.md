<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../index.md).
</div>

# Preferred group members

The `…Preferred` calls Classic's *Preferred Group & Raid Members* page described - pick the best member of an archetype in a fixed priority order - and what each one is in the new bot.

> **:warning: An old call does nothing now - it does not give an error**
>
> The new bot does not keep the old names. A call to an old method silently does nothing and a read of an old member gives `NULL`. Find your name below and write what the row says instead.

## At a glance

| What happened | Names |
|---|---|
| ✏️ Renamed | 9 |
| ➡️ Lives somewhere else | 3 |
| ⛔ Not ported yet | 1 |
| **Total** | **13** |

## The Preferred calls

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `GetInfoOb:Get_GroupIDsPreferred` | does nothing | `${OgreBotAPI.Roster.SortGroupByID[<mode>,<search>]}` | ➡️ Lives somewhere else |  |
| `GetInfoOb:Get_GroupNamesPreferred` | does nothing | `${OgreBotAPI.Roster.SortGroupByID[<mode>,<search>]}` | ➡️ Lives somewhere else |  |
| `GetInfoOb:Get_RaidIDsPreferred` | does nothing | `OgreBotAPI.Roster.RaidIDPreferred` | ✏️ Renamed | it has NO consumer callers - both apparent 'call sites' are prose inside a BLOCK COMMENT in describing how the tier-keyed ordering works. My site counter strips `;`-prefixed lines but not block comments, so entries with 1-2 sites are worth eyeballing. |
| `GetInfoOb:Get_RaidNamesPreferred` | does nothing | `${OgreBotAPI.Roster.SortGroupByID[<mode>,<search>]}` | ➡️ Lives somewhere else |  |
| `GetInfoOb.GetClassPreferredOrder` | reads NULL | — | ⛔ Not ported yet | the class-priority ladder. It survives as the ORDERING inside `Roster.*Preferred`, but is not exposed as a read of its own. |
| `OgreBotAPI.GetGroupIDPreferred` | reads NULL | `OgreBotAPI.Roster.GroupIDPreferred` | ✏️ Renamed |  |
| `GetInfoOb.GetGroupIDPreferred_` | reads NULL | `OgreBotAPI.Roster.GroupIDPreferred` | ✏️ Renamed |  |
| `OgreBotAPI.GetGroupNamePreferred` | reads NULL | `OgreBotAPI.Roster.GroupNamePreferred` | ✏️ Renamed |  |
| `GetInfoOb.GetGroupNamePreferred_` | reads NULL | `OgreBotAPI.Roster.GroupNamePreferred` | ✏️ Renamed |  |
| `OgreBotAPI.GetRaidIDPreferred` | reads NULL | `OgreBotAPI.Roster.RaidIDPreferred` | ✏️ Renamed |  |
| `GetInfoOb.GetRaidIDPreferred_` | reads NULL | `OgreBotAPI.Roster.RaidIDPreferred` | ✏️ Renamed |  |
| `OgreBotAPI.GetRaidNamePreferred` | reads NULL | `OgreBotAPI.Roster.RaidNamePreferred` | ✏️ Renamed |  |
| `GetInfoOb.GetRaidNamePreferred_` | reads NULL | `OgreBotAPI.Roster.RaidNamePreferred` | ✏️ Renamed |  |

## Not in the new bot yet

If your script needs one of these, leave it out for now and tell us - this list is what still needs work.

- `GetInfoOb.GetClassPreferredOrder` - not ported yet
