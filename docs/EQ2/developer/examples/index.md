# Example Scripts

These are **standalone scripts** — you do **not** need OgreBot's source code. Drop the `.iss` in your InnerSpace Scripts folder and run it. The scripts talk to the bot only through the public [`OgreBotAPI`](../ogrebot-api.md) object and OgreBot's cross-session `oc` commands, so nothing in the bot has to be edited.

Each example answers a real question — *"is there a way to tell toons to go to a different campspot when a mob spell starts casting?"* — and is written to be read inline so you can see exactly how the pieces fit together.

> **:warning: Requires a recent OgreBot build.** These examples call the whole-group `OgreBotAPI` members `CountGroupBy` / `GetGroupNameBy` / `GetGroupIDBy` (and the `...Raid...` variants). If your build predates them you'll get an "unknown member" error.

---

## The examples

| Page | What it does | Teaches |
|------|--------------|---------|
| [Move group on cast](cast-move-group.md) | Toon moves to **one** safe spot on cast start; returns **4 seconds after** the cast ends. | Cast monitoring + campspot move + **timer → event** pattern. |
| [Spread to own spots](cast-spread-spots.md) | **Each toon → its own** spot (rank 1, 2, 3…); returns immediately on cast end. | The "same order on everyone" trick. |
| [Group readiness check](ask-group-check.md) | Runs on **one** toon and asks the **whole group** if it's ready to pull (combat, required item, roster). | The [Ask Query System](../ask-query-system.md) — fan-out questions and combined answers. |

---

## How to run (the "running on everyone" model)

Both examples are designed to run **on every toon** — each toon moves itself. This is the cleaner model: no single controller, no cross-session round-trips during the mechanic.

1. Put the `.iss` in your InnerSpace Scripts folder (the same folder you run your other scripts from).
2. From any toon, launch it on everyone in the group:
   ```lavishscript
   oc !ci -RunScriptOB igw:${Me.Name} CastMon_MoveGroup_Standalone
   ```
   (Run on just yourself with `run CastMon_MoveGroup_Standalone`.)
3. Stop later on each toon:
   ```lavishscript
   endscript CastMon_MoveGroup_Standalone
   ```
   Stop the old copy before re-launching, so events don't attach twice.

> **:bulb: Tip**
>
> If you'd rather run on **one** toon and have it move the whole group, swap the local `CRCS` / `ClearRCS` calls for the cross-session equivalents (these are noted in the script comments):
> ```lavishscript
> oc !c -CS_Set_Relative igw:${Me.Name} X Y Z   ; move whole group
> oc !c -CS_ClearRelative igw:${Me.Name}        ; return whole group
> ```

---

## How the key pieces work

### Cast monitoring

`OgreBotAPI:NPC_CastMonitoring["all","Mob Name"]` enables monitoring (and auto-checks the box). The bot's background monitor then fires the global events `OgreEvent_CastMonitoring_CastingStarted` / `OgreEvent_CastMonitoring_CastingEnded`, which the example objects listen for. See [OgreEvents](../ogre-events.md) for the attach/detach pattern these handlers follow.

### Moving and returning (relative campspot)

The examples use the *relative campspot* system from the [CampSpot System](../camp-spot.md):

- `OgreBotAPI:CRCS["${Me.Name}",x,y,z]` overrides the campspot with an absolute location.
- `OgreBotAPI:ClearRCS["${Me.Name}"]` clears the override so the toon returns to wherever its normal campspot is **now**.

> **:warning: Requires an active campspot.** The toons must already have a campspot active for the fight (normal bot setup) for the relative override to take effect. The move is a relative override of that campspot; the return clears the override.

### Same order on everyone

The spread example uses OgreBot's built-in group ordering through the public [`OgreBotAPI`](../ogrebot-api.md) wrappers. `${OgreBotAPI.CountGroupBy["all","All"]}` gives the group size and `${OgreBotAPI.GetGroupIDBy["all","All",N]}` gives the Nth member's **actor ID** (1-based) in an order that is **identical on every session**. Each toon walks that list and matches `${Me.ID}` to find its own rank, then moves to its own spot. No communication needed.

> **:memo: Preferred vs By**
>
> `OgreBotAPI` exposes two families. The **whole-group** family — `CountGroupBy` / `GetGroupNameBy` / `GetGroupIDBy` (and the `...Raid...` variants) — takes a `SearchWith` of `"All"` to enumerate everyone, or `Class` / `Archetype` / `ParentClass` / `Role` / etc. to filter. The older [`...Preferred`](../preferred-group-members.md) family is archetype/role-filtered only — passing `"all"` to it matches nobody. For a whole-group spread, use the `...By` wrappers with `"All"`.

> **:bulb: Prefer ID over name.** In a given zone an actor's ID is the same for every observer (it only changes when the actor zones/despawns), so matching on `${Me.ID}` is the most reliable way for each toon to find itself.

---

## If you only need to INTERRUPT (no movement)

No script needed at all — use OgreBot's XML MobInfo approach with `<Setting Name="CastInterrupt">TRUE</Setting>`.

---

## Related Documentation

- [OgreBotAPI Reference](../ogrebot-api.md) — Full API for controlling OgreBot
- [CampSpot System](../camp-spot.md) — Relative campspot (CRCS / ClearRCS)
- [OgreEvents](../ogre-events.md) — Event attach/detach pattern
- [Preferred Group Members](../preferred-group-members.md) — Group & raid member ordering
- [Coding Practices](../coding-practices.md) — Naming conventions and code style
