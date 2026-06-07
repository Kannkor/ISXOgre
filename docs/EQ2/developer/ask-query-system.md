# Ask Query System

A generic, event-based way for **one** character to ask a question of the **whole group** and get a single combined answer back. The caller broadcasts a LavishScript expression (with an optional comparison); every targeted member evaluates it **locally** against itself and reports back; the caller's wrapper aggregates the replies and returns one reduced result — a yes/no, a count, or a JSON list.

Think of it as a one-liner for *"is everyone …?"*, *"is anyone …?"*, *"how many …?"*, and *"what does each member have for …?"* — without writing any cross-session plumbing yourself.

> **:warning: Requires a recent OgreBot build on every box.** The query runs on each member, so all boxes you target must be running a build that includes the Ask system. Boxes on an older build simply won't reply (they'll show up as non-responders).

---

## The wrappers

All are members of the public `OgreBotAPI` object. Each is a `function` (the internal reply-wait loop needs to yield), so you call them with `call` and read the result from `${Return}`.

| Wrapper | Returns |
|---------|---------|
| `OgreBotAPI.Ask_AllTrue` | `TRUE` only if **every** responder's comparison was true |
| `OgreBotAPI.Ask_AnyTrue` | `TRUE` if **at least one** responder's comparison was true |
| `OgreBotAPI.Ask_AnyFalse` | `TRUE` if **any** member is not confirmed true (`= !AllTrue`) — a non-responder (timeout/NULL) counts as not-true |
| `OgreBotAPI.Ask_AllFalse` | `TRUE` only if **no** member is confirmed true (`= !AnyTrue`) |
| `OgreBotAPI.Ask_CountTrue` | integer count of responders whose comparison was true |
| `OgreBotAPI.Ask_Json` | JSON object `{"<Name>":"<raw value>", ...}` of every responder |

> **:bulb: True/False are a complete pair.** The `*False` wrappers are convenience inverses of the `*True` ones. The same logic is also reachable by flipping the comparison operator — `Ask_AnyFalse(expr == X)` is equivalent to `Ask_AnyTrue(expr != X)`. Use whichever reads more clearly.

---

## Call shape

```lavishscript
call OgreBotAPI.Ask_<Mode> "<ForWho>" -expr "<expression>" [-op "<op>"] [-value "<value>"] [flags...]
variable string Result="${Return}"
```

- **`<ForWho>`** is the **leading positional** argument (the target filter). Everything after it is named flags.
- Use **`igw:${Me.Name}`** to target your whole group. (`igw` = "in group with".)

### Flags

| Flag | Default | Meaning |
|------|---------|---------|
| `-expr` | *(required)* | The expression each member evaluates **against itself**. Pass the **bare** path — see the warning below. |
| `-op` | `==` | Comparison operator: `==`  `!=`  `>`  `<`  `>=`  `<=`. |
| `-value` | `TRUE` | The right-hand side of the comparison. |
| `-ServerCall` | off | For values that aren't ready instantly (e.g. examine/ItemInfo data right after zoning), each member retries locally until the data warms, then replies. |
| `-Timeout` | `80` | How long the caller waits for replies, in **tenths of a second** (`80` = 8 s). |
| `-Expected` | group size | How many replies to wait for before reducing early. Defaults to `Me.GroupCount` (minimum 1). |
| `-RetryMax` | `5` | With `-ServerCall`, how many warm-up retries each member makes before giving up and replying `**TIMEOUT**`. |

> **:warning: Pass the BARE expression, not `${...}`.** Write `-expr "Me.InCombat"`, **not** `-expr "${Me.InCombat}"`. The remote member resolves it with double-expansion on its own side; a `${...}` here would be evaluated on the **caller** before it's ever sent, so every member would answer the caller's value instead of its own.

---

## Examples

### Is the whole group out of combat?

```lavishscript
call OgreBotAPI.Ask_AllTrue "igw:${Me.Name}" -expr "Me.InCombat" -op "==" -value "FALSE"
if ${Return}
    echo Everyone is out of combat - safe to pull.
```

### Is anyone already in combat? (don't pull)

```lavishscript
call OgreBotAPI.Ask_AnyTrue "igw:${Me.Name}" -expr "Me.InCombat" -op "==" -value "TRUE"
if ${Return}
    echo Someone is already fighting - hold the pull.
```

### How many members are above level 100?

```lavishscript
call OgreBotAPI.Ask_CountTrue "igw:${Me.Name}" -expr "Me.Level" -op ">=" -value "100"
echo ${Return} members are level 100+.
```

### Does anyone NOT have a required item? (raid prep)

```lavishscript
; Each member checks its own inventory. A member without the item reports "NULL".
call OgreBotAPI.Ask_AnyFalse "igw:${Me.Name}" -expr "Me.Inventory[Required Totem].Name" -op "!=" -value "NULL"
if ${Return}
    echo At least one member is missing the totem.
```

### Get each member's actual value (JSON list)

```lavishscript
call OgreBotAPI.Ask_Json "igw:${Me.Name}" -expr "Me.Equipment[1].ToItemInfo.Name" -ServerCall
variable jsonvalue jvNames
jvNames:SetValue["${Return~}"]
echo ${jvNames.AsJSON}
; -> {"Toon1":"Some Weapon Name","Toon2":"Another Weapon","Toon3":"NULL", ...}
```

> **:memo: Values with spaces and apostrophes are safe.** The JSON result round-trips full names like `Toon2:"Crested Buckler of the Vanguard"` intact. Load `${Return}` straight into a `jsonvalue` to walk it.

---

## How it works (under the hood)

1. The wrapper generates a unique **query ID** (`<CallerName>_<counter>`), so concurrent queries never collide — you can run several at once and each gets its own correct answer.
2. It broadcasts the question to the targeted members over OgreBot's cross-session channel.
3. Each member evaluates `-expr` against itself, applies the comparison, and fires a reply event back to the caller carrying both the `TRUE`/`FALSE` result **and** the raw value.
4. The caller tallies replies per query ID until `-Expected` are in (or `-Timeout` elapses), then reduces to the requested form.

> **:bulb: Concurrency is safe.** Because every query is keyed by its own ID, two scripts (or two calls in the same script) asking different questions at the same time will not interfere — each returns its own independent, correct result.

### Non-responders and timeouts

A member that doesn't reply in time (old build, zoning, busy) is simply absent from the tally. That's why `Ask_AnyFalse` treats a non-responder as **not** confirmed-true: if you can't confirm everyone is good, you usually want to know. If you only care about members that actually answered, use `Ask_CountTrue` / `Ask_Json` and compare against the count you got back.

### `-ServerCall` for examine data

Item/examine data isn't always in memory the instant you ask (e.g. right after zoning). With `-ServerCall`, a member that reads an empty/`NULL` value asks the server for it and retries locally up to `-RetryMax` times before replying. A value that never warms comes back as `**TIMEOUT**`. Use `-ServerCall` for any expression that reads `ToItemInfo` / examine fields; you don't need it for instant values like `Me.Level` or `Me.InCombat`.

---

## See it in action

- [Group readiness check](examples/ask-group-check.md) — a standalone script that gates a pull on the whole group being ready, using several wrappers together.

---

## Related Documentation

- [OgreBotAPI Reference](ogrebot-api.md) — Full API for controlling OgreBot
- [OgreEvents](ogre-events.md) — The event attach/detach pattern the reply transport is built on
- [Coding Practices](coding-practices.md) — Naming conventions and code style
