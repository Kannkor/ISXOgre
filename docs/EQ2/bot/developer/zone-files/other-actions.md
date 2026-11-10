# Other actions

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../index.md).
</div>

These come from fight files, and the shipped zone files use them too. They run on the IC character. Add
`sendTo` to have others do it as well: `"sendTo": "igwbn:{{me}}"` is everyone in the group but the IC character.

| Action | What it does |
|---|---|
| `announce` | Writes `message` in the IC character's console. `"console": true` sends it to every character's console. |
| `autotarget` | The IC character's AutoTarget: `"op": "addActor"` with `name`, `"removeActor"`, `"clear"`, or `"set"` with `radius`, `height` or `enabled`. |
| `campSpot` | Camp spots: `"op": "enable"`, `"setLoc"` with `x`, `y`, `z`, or `"clearAll"`. Takes `sendTo`. |
| `actorInteract` | Clicks an actor by `name` (`"op": "doubleClick"`, which takes `sendTo`), or targets it (`"op": "target"`). An actor that is not there fails the step, so it is often written with `"onFail": "proceed"`. |
| `movement` | `"op": "setRunMode"` with `"mode": "walk"` or `"run"`. Takes `sendTo`. IC sets running back when the zone ends. |
| `ogreBotUIOption` | Ticks or unticks an OgreBot option by its `id` (`"value": "TRUE"` / `"FALSE"`), or puts it back (`"op": "restore"`). Takes `sendTo`. |
| `raw` | Runs any InnerSpace `command` on the IC character. |

These are checked when the file loads, by the same rules fight files use. A missing key the action needs, or a wrong
`op`, skips the file. A key the action does not read is a warning.

**Example: walk to a door, click it open, walk on through.** The group walks to the door, the IC character clicks
it, everyone waits a moment for it to swing, and then they walk to the far side.

```json
{ "stepId": "gate.walk",  "do": "path", "using": "nav", "spots": [[-120.5, 12.0, 340.2]] },
{ "stepId": "gate.open",  "do": "actorInteract", "op": "doubleClick", "name": "Gate Lever" },
{ "stepId": "gate.swing", "wait": "ms", "limitMs": 1500, "onTimeout": "proceed" },
{ "stepId": "gate.past",  "do": "path", "using": "nav", "spots": [[-160.0, 12.0, 365.8]] }
```

- The click is made by the IC character only, which is enough for most doors. Add `"sendTo": "igwbn:{{me}}"` if every
  character has to click it.
- If the door is not there, the click fails and so does the run. Add `"onFail": "proceed"` when the door is sometimes
  already open or gone.
- A walk opens an ordinary door by itself: when something solid blocks the way, it looks for an actor with "door" in
  its name close by and clicks it. You need this example for anything else, such as a lever, or a door that is not
  called a door.
