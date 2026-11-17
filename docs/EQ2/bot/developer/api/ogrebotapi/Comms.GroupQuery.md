<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# OgreBotAPI.Comms.GroupQuery

## Members

### `Done`

`${OgreBotAPI.Comms.GroupQuery.Done[id]}`

Whether a group query has finished. With no id it reads the query this object was started as, else the last one; an id from another session matches nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `id` | string |  | The query id from Last (like gq:is1:4); blank reads the bound or last query |

**Returns:** bool: TRUE once the query has finished; FALSE while it runs, for an id this session did not start, and again 60 seconds after it finished, when the result is dropped.

```text
echo ${OgreBotAPI.Comms.GroupQuery.Done[${OgreBotAPI.Comms.GroupQuery.Last}]}
```

### `Last`

`${OgreBotAPI.Comms.GroupQuery.Last}`

The id of the last group query this session started, from ${OgreBotAPI.Comms.GroupQuery[fw,...]} or OgreBotAPI.Comms:GroupQuery. Pass it to Done and Result to read that query.

**Returns:** string: the id, like gq:is1:4; "" when this session has not started one.

```text
echo ${OgreBotAPI.Comms.GroupQuery.Last}
```

### `Result`

`${OgreBotAPI.Comms.GroupQuery.Result[id]}`

The result of a finished group query, as JSON. With no id it reads the query this object was started as, else the last one; the result stays readable for 60 seconds after the query finishes.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `id` | string |  | The query id from Last (like gq:is1:4); blank reads the bound or last query |

**Returns:** string: the result JSON once finished; "" while it runs, for an id this session did not start, and after the 60 seconds are up.

```text
echo ${OgreBotAPI.Comms.GroupQuery.Result[${OgreBotAPI.Comms.GroupQuery.Last}]}
```
