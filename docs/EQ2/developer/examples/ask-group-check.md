# Group readiness check

A standalone script that runs on **one** toon and asks the **whole group** a few questions before a pull: *is anyone already in combat?*, *does everyone have the required item?*, and *who's missing it?* It prints a clear go / no-go and the roster, using the [Ask Query System](../ask-query-system.md).

Unlike the cast-monitoring examples (which run on every toon), this one runs on a **single** toon — the Ask wrappers broadcast the questions to the group for you.

> **:warning: Requires a recent OgreBot build on every box.** Each member answers the query about itself, so every box you target must run a build that includes the Ask system. Boxes on an older build won't reply and show up as non-responders.

---

## What it does

- Asks the group **"is anyone already in combat?"** — if so, it stops (don't pull).
- Asks **"does everyone have the required item?"** — a member without it reports `NULL`.
- If someone's missing it, dumps a **JSON roster** of each member's value so you can see who.
- Prints **how many** members are ready.

---

## What you edit

All edit points are marked `<<< EDIT` in the code:

- The **required item name** (exactly as it appears in your inventory).

---

## Which wrappers it uses

| Question | Wrapper | Expression |
|----------|---------|------------|
| Anyone in combat? | `Ask_AnyTrue` | `Me.InCombat == TRUE` |
| Everyone has the item? | `Ask_AllTrue` | `Me.Inventory[<item>].Name != NULL` |
| Who has what? | `Ask_Json` | `Me.Inventory[<item>].Name` |
| How many ready? | `Ask_CountTrue` | `Me.Inventory[<item>].Name != NULL` |

> **:bulb: Bare expressions.** Note the `-expr` values are bare paths (`Me.InCombat`), not `${Me.InCombat}`. Each member resolves the path against itself; a `${...}` here would be evaluated on the caller before sending. See the [Ask Query System](../ask-query-system.md) page for why.

---

## How to run

```lavishscript
; Run on a single toon (it asks the whole group for you):
run AskGroupCheck_Standalone

; Or launch it on one specific toon from anywhere:
oc !ci -RunScriptOB <ToonName> AskGroupCheck_Standalone
```

There's nothing to stop — the script asks its questions, prints the result, and exits.

---

## The script

```lavishscript
;==============================================================================
; EXAMPLE (STANDALONE): Group readiness check before a pull.
;------------------------------------------------------------------------------
; Runs on ONE toon and asks the WHOLE GROUP a few questions using the public
; OgreBotAPI "Ask" system. No OgreBot source needed - it only calls public
; OgreBotAPI members and reads ${Return}.
;
; WHAT IT DOES
;   - Asks "is anyone already in combat?"  -> if yes, stop (don't pull).
;   - Asks "does everyone have the required item?" (a member without it
;     reports the literal text "NULL").
;   - If someone is missing it, dumps a JSON roster of each member's value.
;   - Prints how many members are ready.
;
; WHY ONE TOON (not "run on everyone")
;   The Ask wrappers broadcast the question to the group and collect the
;   replies on the calling toon. So you run this on a single toon - it does
;   the fan-out for you - unlike the cast-monitoring examples that run on all.
;
; HOW TO RUN
;   run AskGroupCheck_Standalone
;
; WHAT YOU MUST EDIT  (search for "<<< EDIT"):
;   - The required item name.
;
; NOTE on -expr: pass the BARE path ("Me.InCombat"), NOT "${Me.InCombat}".
;   Each member resolves it against itself; a ${} here would be evaluated on
;   the caller before it is ever sent.
;==============================================================================

function main()
{
	; Wait until the local bot is ready before issuing cross-session queries.
	while !${OgreBotAPI.IsReady}
		wait 10

	; <<< EDIT: the item every member should be carrying for this fight.
	variable string RequiredItem="Required Totem"

	variable string Target="igw:${Me.Name}"   ; whole group
	variable jsonvalue jvRoster

	echo === Group readiness check (group of ${Me.GroupCount}) ===

	;--------------------------------------------------------------------------
	; 1) Is anyone already in combat? If so, hold the pull.
	;--------------------------------------------------------------------------
	call OgreBotAPI.Ask_AnyTrue "${Target}" -expr "Me.InCombat" -op "==" -value "TRUE"
	if ${Return}
	{
		echo NO-GO: someone is already in combat.
		return
	}
	echo OK: nobody is in combat.

	;--------------------------------------------------------------------------
	; 2) Does EVERYONE have the required item?
	;    A member without it reports the literal text "NULL", so "!= NULL"
	;    means "has it".
	;--------------------------------------------------------------------------
	call OgreBotAPI.Ask_AllTrue "${Target}" -expr "Me.Inventory[${RequiredItem}].Name" -op "!=" -value "NULL"
	if ${Return}
	{
		echo OK: everyone has "${RequiredItem}".
	}
	else
	{
		echo NO-GO: at least one member is missing "${RequiredItem}".

		; Show who has what. Load the JSON straight into a jsonvalue to read it.
		call OgreBotAPI.Ask_Json "${Target}" -expr "Me.Inventory[${RequiredItem}].Name"
		jvRoster:SetValue["${Return~}"]
		echo Roster: ${jvRoster.AsJSON}
	}

	;--------------------------------------------------------------------------
	; 3) How many members are carrying it?
	;--------------------------------------------------------------------------
	call OgreBotAPI.Ask_CountTrue "${Target}" -expr "Me.Inventory[${RequiredItem}].Name" -op "!=" -value "NULL"
	echo ${Return} of ${Me.GroupCount} members have "${RequiredItem}".

	echo === Check complete ===
}
```

---

## Sample output

```text
=== Group readiness check (group of 6) ===
OK: nobody is in combat.
NO-GO: at least one member is missing "Required Totem".
Roster: {"Toon1":"Required Totem","Toon2":"NULL","Toon3":"Required Totem","Toon4":"Required Totem","Toon5":"NULL","Toon6":"Required Totem"}
4 of 6 members have "Required Totem".
=== Check complete ===
```

> **:memo: Want examine/ItemInfo data?** This example reads `Me.Inventory[...].Name`, which is available instantly. If you query something that loads from the server (anything through `ToItemInfo` / examine), add `-ServerCall` so each member warms the data and retries before replying. See the [Ask Query System](../ask-query-system.md) page.

---

## Related Documentation

- [Ask Query System](../ask-query-system.md) — Wrappers, flags, semantics, and concurrency
- [Examples overview](index.md) — How to run and shared concepts
- [OgreBotAPI Reference](../ogrebot-api.md) — Full API for controlling OgreBot
- [Coding Practices](../coding-practices.md) — Naming conventions and code style
