# Ask Query System

A generic, event-based way for **one** character to ask a question of the **whole group** and get a single combined answer back. The caller broadcasts a LavishScript expression (with an optional comparison); every targeted member evaluates it **locally** against itself and reports back; the caller's wrapper aggregates the replies and returns one reduced result — a yes/no, a count, or a JSON list.

Think of it as a one-liner for *"is everyone …?"*, *"is anyone …?"*, *"how many …?"*, and *"what does each member have for …?"* — without writing any cross-session plumbing yourself.

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

### One entry, any mode: `OgreBotAPI.Ask`

The six named wrappers above are readable aliases. There is also a single `OgreBotAPI.Ask` that takes the reduction as a **`-Mode <value>`** flag instead of baking it into the function name:

```lavishscript
call OgreBotAPI.Ask "<ForWho>" <jsonOut|NULL> -Mode <mode> -expr "<expression>" [flags...]
```

`<mode>` is one of `alltrue` `anytrue` `anyfalse` `allfalse` `counttrue` `json` (case-insensitive; default `alltrue` if you omit `-Mode`). It behaves **exactly** like the matching wrapper — same positionals, same flags, same return — so `Ask … -Mode counttrue` is identical to `Ask_CountTrue …`.

Reach for `Ask` when the reduction is **chosen at runtime** (e.g. `-Mode "${sMode}"`); reach for a named wrapper when it's fixed, since `Ask_AllTrue` reads more clearly than `Ask … -Mode alltrue`.

> **:warning: An unknown `-Mode` is rejected, not guessed.** A typo'd mode echoes `Error: OgreBotAPI.Ask unknown -Mode …` and returns `FALSE` rather than silently reducing as the wrong mode (a wrong boolean reduce would look like a legitimate `FALSE`).

---

## Call shape

```lavishscript
variable string Result
call OgreBotAPI.Ask_<Mode> "<ForWho>" <jsonOut|NULL> -expr "<expression>" [-op "<op>"] [-value "<value>"] [flags...]
Result:Set["${Return}"]
```

> **:warning: Declare the result variable, then `:Set` it *after* the call.** LavishScript preprocesses variable declarations, so `variable string Result="${Return}"` evaluates `${Return}` before the `call` ever runs — `Result` would be `NULL`. Declare it first and assign with `Result:Set["${Return}"]` after the call returns (or just read `${Return}` directly).

- **`<ForWho>`** is the **first positional** argument (the target filter). Use **`igw:${Me.Name}`** to target your whole group. (`igw` = "in group with".)
- **`<jsonOut|NULL>`** is the **second positional** — your own `jsonvalue` variable to be filled with the per-member breakdown `{"<Name>":"<raw value>", ...}` in the *same* call, or `NULL` (or `""`) to skip it. See [Per-member breakdown](#per-member-breakdown-the-jsonout-slot).
- Everything after those two positionals is named flags.

> **:warning: The breakdown slot is required — pass `NULL` when you don't want it.** Both positionals are fixed: if you skip the second one, your first flag (`-expr …`) lands in the breakdown slot and the query breaks. When you don't need the per-member data, write `NULL` there.

### Flags

| Flag | Default | Meaning |
|------|---------|---------|
| `-Mode` | `alltrue` | **`OgreBotAPI.Ask` only.** Which reduction to apply: `alltrue` `anytrue` `anyfalse` `allfalse` `counttrue` `json` (case-insensitive). The named wrappers set this for you. |
| `-expr` | *(required)* | The expression each member evaluates **against itself**. Pass the **bare** path — see the warning below. |
| `-op` | `==` | Comparison operator: `==`  `!=`  `>`  `<`  `>=`  `<=`. |
| `-value` | `TRUE` | The right-hand side of the comparison. |
| `-ServerCall` | off | For values that aren't ready instantly (e.g. examine/ItemInfo data right after zoning), each member retries locally until the data warms, then replies. |
| `-Timeout` | `80` | How long the caller waits for replies, in **tenths of a second** (`80` = 8 s). |
| `-Expected` | *(auto)* | How many replies to wait for before reducing early. **Auto-derived from `<ForWho>`** — see [Smart `-Expected`](#smart-expected-auto-counting-who-should-reply) below. Pass it explicitly only to override. |
| `-RespondersOnly` | off | Reduce over **who actually replied** instead of the expected count. Affects `Ask_AllTrue` / `Ask_AnyFalse` only — see [Strict vs responders-only](#strict-vs-responders-only) below. |
| `-RetryMax` | `5` | With `-ServerCall`, how many warm-up retries each member makes before giving up and replying `**TIMEOUT**`. |

> **:warning: Pass the BARE expression, not `${...}`.** Write `-expr "Me.InCombat"`, **not** `-expr "${Me.InCombat}"`. The remote member resolves it with double-expansion on its own side; a `${...}` here would be evaluated on the **caller** before it's ever sent, so every member would answer the caller's value instead of its own.

---

## Examples

### Is the whole group out of combat?

```lavishscript
call OgreBotAPI.Ask_AllTrue "igw:${Me.Name}" NULL -expr "Me.InCombat" -op "==" -value "FALSE"
if ${Return}
    echo Everyone is out of combat - safe to pull.
```

### Is anyone already in combat? (don't pull)

```lavishscript
call OgreBotAPI.Ask_AnyTrue "igw:${Me.Name}" NULL -expr "Me.InCombat" -op "==" -value "TRUE"
if ${Return}
    echo Someone is already fighting - hold the pull.
```

### How many members are above level 100?

```lavishscript
call OgreBotAPI.Ask_CountTrue "igw:${Me.Name}" NULL -expr "Me.Level" -op ">=" -value "100"
echo ${Return} members are level 100+.
```

### Does anyone NOT have a required item? (raid prep)

```lavishscript
; Each member checks its own inventory. A member without the item reports "NULL".
; Pass a jsonvalue in slot 2 so a FALSE result can tell you exactly WHO is missing it.
variable jsonvalue jvTotem
call OgreBotAPI.Ask_AnyFalse "igw:${Me.Name}" jvTotem -expr "Me.Inventory[Required Totem].Name" -op "!=" -value "NULL"
if ${Return}
    echo At least one member is missing the totem: ${jvTotem.AsJSON}
```

### Get each member's actual value (JSON list)

```lavishscript
variable jsonvalue jvNames
call OgreBotAPI.Ask_Json "igw:${Me.Name}" jvNames -expr "Me.Equipment[1].ToItemInfo.Name" -ServerCall
echo ${jvNames.AsJSON}
; -> {"Toon1":"Some Weapon Name","Toon2":"Another Weapon","Toon3":"NULL", ...}
```

> **:memo: Values with spaces and apostrophes are safe.** The JSON result round-trips full names like `Toon2:"Crested Buckler of the Vanguard"` intact. For `Ask_Json` the same JSON also comes back in `${Return}` if you'd rather read it that way.

### Pick the reduction at runtime (`Ask -Mode`)

When the reduction isn't known until the script decides it, use `OgreBotAPI.Ask` and feed `-Mode` from a variable instead of branching to a different wrapper:

```lavishscript
; sMode decided elsewhere at runtime
variable string sMode="counttrue"
call OgreBotAPI.Ask "igw:${Me.Name}" NULL -Mode "${sMode}" -expr "Me.Level" -op ">=" -value "100"
echo Result (${sMode}): ${Return}
```

---

## Per-member breakdown (the `jsonOut` slot)

Every wrapper's **second positional** is an optional `jsonvalue` to fill with the per-member result of *this* query — `{"<Name>":"<raw value>", ...}` — populated in the **same broadcast** that produces the reduced answer. This is how a `FALSE` from `Ask_AllTrue` (or a `TRUE` from `Ask_AnyFalse`) can tell you **who** without a second query whose data might have drifted in between.

```lavishscript
variable jsonvalue jvWho
call OgreBotAPI.Ask_AllTrue "igw:${Me.Name}" jvWho -expr "Me.Level" -op ">=" -value "100"
if !${Return}
{
    ; jvWho holds every member's actual level - walk it to see who fell short.
    echo Not everyone is 100+. Levels: ${jvWho.AsJSON}
}
```

- Pass `NULL` (or `""`) when you don't want the breakdown — see the warning under [Call shape](#call-shape).
- The variable is passed **by reference** (a weakref parameter), so it works on **any** scope, including a function-local in your own standalone script. (A by-name approach can't reach a caller's local — the reference binding can.)
- It's filled for **every** mode, so you can pair the breakdown with `Ask_AllTrue`, `Ask_CountTrue`, etc., not just `Ask_Json`.

---

## Smart `-Expected` (auto-counting who should reply)

`Ask_AllTrue` / `Ask_AnyFalse` need to know **how many** members *should* answer so a silent non-responder can count against the result. Rather than make you hand-count, the wrapper derives that number from your `<ForWho>` filter automatically — so you usually never pass `-Expected` at all.

- **Whole group** (`igw:${Me.Name}`) → `Me.GroupCount`.
- **Whole raid** (`irw:` / `irzw:` / `irwbn:` / `irzwbn:` prefixes) → `Me.RaidCount`.
- **A single class/archetype filter** (e.g. `igw:${Me.Name}+mage`, `irw:${Me.Name}+templar`) → it actually **counts how many of that kind you have**, using the same group/raid roster the bot already tracks. Ask the mages and it expects exactly as many replies as you have mages.
- **Anything more complex** (an `|` OR-group, more than one `+` term, or a negated `-`/`!` term) → falls back to the full group or raid count. It errs toward the larger number so a strict `AllTrue` never passes by under-counting.

The class/archetype words it understands mirror the `ForWho` filter itself: archetypes (`fighter`/`scout`/`mage`/`priest`, plus `healer`), the composites `melee` and `caster`, parent classes (`crusader`, `warrior`, `brawler`, `bard`, `predator`, `rogue`, `druid`, `shaman`, `cleric`, `enchanter`, `summoner`, `sorcerer`), and any specific subclass by name.

> **:bulb: When to override.** Pass `-Expected N` yourself only when you know the real number better than the filter does — e.g. you're targeting a hand-picked subset by name, or someone is intentionally offline and you don't want them counted. For the common "ask everyone" or "ask the mages" cases, leave it off.

```lavishscript
; No -Expected needed: it counts your mages and waits for exactly that many.
call OgreBotAPI.Ask_AllTrue "igw:${Me.Name}+mage" NULL -expr "Me.InCombat" -op "==" -value "FALSE"
if ${Return}
    echo Every mage is out of combat.
```

---

## Strict vs responders-only

For `Ask_AllTrue` (and its inverse `Ask_AnyFalse`) there are two honest ways to handle the member who never answers — old build, zoning, crashed. The flag `-RespondersOnly` picks which one you get:

| Mode | `Ask_AllTrue` is `TRUE` when… | Use it when… |
|------|------------------------------|--------------|
| **Strict** *(default)* | the number of true replies **reaches the expected count** — a non-responder counts as not-true. | A miss is dangerous and you'd rather get a `FALSE` and look into it (e.g. *"is everyone's belt rune correct before the pull?"*). |
| **Responders-only** (`-RespondersOnly`) | **every member that replied** was true, and at least one did. Non-responders are ignored. | You only care about the toons actually present/answering and a silent box shouldn't sink the result. |

> **:warning: Responders-only can pass on partial data.** If 6 should answer, 1 is silent, and the other 5 are all true, strict returns `FALSE` (only 5 of 6 confirmed) while `-RespondersOnly` returns `TRUE` (all 5 answers were true). The `>=1 reply` guard means a query where **nobody** answers is always `FALSE`, never a vacuous `TRUE`. Default to strict for safety gates; opt into responders-only deliberately.

---

## How it works (under the hood)

1. The wrapper generates a unique **query ID** (`<CallerName>_<counter>`), so concurrent queries never collide — you can run several at once and each gets its own correct answer.
2. It broadcasts the question to the targeted members over OgreBot's cross-session channel.
3. Each member evaluates `-expr` against itself, applies the comparison, and fires a reply event back to the caller carrying both the `TRUE`/`FALSE` result **and** the raw value.
4. The caller tallies replies per query ID until `-Expected` are in (or `-Timeout` elapses), then reduces to the requested form.

> **:bulb: Concurrency is safe.** Because every query is keyed by its own ID, two scripts (or two calls in the same script) asking different questions at the same time will not interfere — each returns its own independent, correct result.

### Non-responders and timeouts

A member that doesn't reply in time (old build, zoning, busy) is simply absent from the tally. By default `Ask_AllTrue` / `Ask_AnyFalse` treat a non-responder as **not** confirmed-true: if you can't confirm everyone is good, you usually want to know. That comparison is against the [auto-derived `-Expected`](#smart-expected-auto-counting-who-should-reply) count. If you only care about members that actually answered, pass [`-RespondersOnly`](#strict-vs-responders-only) (or use `Ask_CountTrue` / `Ask_Json` and compare against the count you got back).

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
