# Spread each toon to its own spot on cast

A standalone script that watches one mob for one ability. When that ability **starts** casting, **each toon moves to its own** spread spot (rank 1, rank 2, rank 3…). When it **finishes**, each toon returns immediately. The trick is that every session computes the **same order** independently, so no communication is needed.

> **:warning: Requires a recent OgreBot build** and an active campspot for the fight. See the [Examples overview](index.md) for both requirements.

---

## What it does

- Turns on NPC cast monitoring for one mob.
- When that mob **starts** casting a specific ability → **each toon moves to its OWN** spread spot (spot 1, spot 2, spot 3, …).
- When that ability **finishes** casting → each toon returns immediately. (For a delayed/timer-based return, see [Move group on cast](cast-move-group.md).)

---

## What you edit

All edit points are marked `<<< EDIT` in the code:

- The **mob name** (exactly as it appears when you `/target` it).
- The **ability ID** to watch — get this from **Ogre Analysis**.
- **One spread spot per group member**, defined in `SetupSpots()`. Insert order = rank order: the first `Insert` is rank #1, the second is rank #2, and so on.

---

## How it works

**Cast monitoring** — `OgreBotAPI:NPC_CastMonitoring["all","${This.MobName}"]` enables monitoring and auto-checks the box. The bot's background monitor fires `OgreEvent_CastMonitoring_CastingStarted` / `OgreEvent_CastMonitoring_CastingEnded`; the object attaches handlers using the standard [OgreEvents](../ogre-events.md) pattern.

**Move and return** — uses the relative campspot from the [CampSpot System](../camp-spot.md). `OgreBotAPI:CRCS["${Me.Name}",x,y,z]` overrides to the toon's own spot; `OgreBotAPI:ClearRCS["${Me.Name}"]` clears it on cast end.

**Same order on everyone** (the key part) — the script runs on every toon, and each toon independently computes the same ordering via the public [`OgreBotAPI`](../ogrebot-api.md) wrappers:

- `${OgreBotAPI.CountGroupBy["all","All"]}` — total members in the group.
- `${OgreBotAPI.GetGroupIDBy["all","All",N]}` — the **actor ID** of the Nth member (1-based), in an order that is **identical on every session** (alphabetical by character name under the hood, so it's stable).

Each toon loops from `N=1` to the count, compares each member's actor ID to `${Me.ID}`, and the match is its own rank. Then it moves to `SpreadSpots[myRank]`. No communication needed — every toon arrives at the same answer.

> **:bulb: Why ID, not name.** In a given zone an actor's ID is the same for every observer (it only changes when the actor zones/despawns), so matching on `${Me.ID}` is the most reliable way for each toon to find itself.

> **:memo: Preferred vs By**
>
> This example uses the whole-group `...By` family (`CountGroupBy` / `GetGroupIDBy`) with a `SearchWith` of `"All"`, which enumerates everyone. The older [`...Preferred`](../preferred-group-members.md) family is **archetype/role-only** — passing `"all"` to it matches nobody, so it is *not* what you want for a whole-group spread. Note that the Preferred family is archetype-only by design.

---

## How to run

```lavishscript
; Run on everyone in the group:
oc !ci -RunScriptOB igw:${Me.Name} CastMon_SpreadToOwnSpots_Standalone

; Run on just yourself:
run CastMon_SpreadToOwnSpots_Standalone

; Stop later (on each toon):
endscript CastMon_SpreadToOwnSpots_Standalone
```

Stop the old copy before re-launching so events don't attach twice.

---

## The script

```lavishscript
;==============================================================================
; EXAMPLE 2 (STANDALONE): Send each toon to its OWN campspot when a mob casts.
;------------------------------------------------------------------------------
; This is the "respective campspot" version from the Discord answer:
;
;   "If the script is running on everyone, then you determine the same order
;    on everyone, and everyone goes to their respective campspot."
;
; Like Example 1, this is STANDALONE - no OgreBot source needed. It uses only
; the public OgreBotAPI object and native ISXEQ2 group info.
;
; WHAT IT DOES
;   - Turns on NPC cast monitoring for one mob.
;   - When that mob STARTS casting a specific ability -> EACH toon moves to its
;     OWN spread spot (spot 1, spot 2, spot 3, ...).
;   - When that ability FINISHES casting -> each toon returns immediately.
;     (For a delayed/timer-based return, see Example 1.)
;
; HOW THE "SAME ORDER ON EVERYONE" WORKS  (the key part)
;   This script runs on every toon. We use OgreBot's built-in group ordering
;   through the public OgreBotAPI wrappers (CountGroupBy / GetGroupIDBy), which
;   return the group members in a fixed order that is IDENTICAL on every
;   session. Each toon walks that list, matches its own actor ID (${Me.ID}) to
;   find its position (#1, #2, #3...), and moves to SpreadSpots[myPosition]. No
;   communication needed - every toon independently computes the same order.
;   (We match by actor ID rather than name: in a given zone an actor's ID is
;    the same for every observer, so it's the most reliable thing to key on.)
;
; HOW TO RUN IT  (same as Example 1)
;   1. Put this file in your InnerSpace Scripts folder (where you run scripts from).
;   2. Launch on everyone in the group:
;          oc !ci -RunScriptOB igw:${Me.Name} CastMon_SpreadToOwnSpots_Standalone
;   3. Stop later on each toon:  endscript CastMon_SpreadToOwnSpots_Standalone
;
; WHAT YOU MUST EDIT  (search for "<<< EDIT"):
;   - The mob name
;   - The ability ID  (from Ogre Analysis)
;   - One spread spot per group member
;
; REQUIREMENT: toons must already have a campspot active for the fight (normal
;   bot setup). The move is a RELATIVE override; the return clears it.
;==============================================================================

objectdef Object_CastMonSpread
{
	; <<< EDIT: exact mob name.
	variable string MobName="Boss Name Here"

	; <<< EDIT: ability ID to react to (from Ogre Analysis).
	variable int64 DangerSpellID=1234567890

	; <<< EDIT: one spot per group member. SpreadSpots[1] is for rank #1, etc.
	;           Defined in SetupSpots() below so order is explicit.
	variable index:point3f SpreadSpots

	; This toon's rank in the agreed order (1..6). 0 = no spot assigned.
	variable int iMyRank=0

	variable bool bMovedOut=FALSE

	method Setup()
	{
		This:SetupSpots

		OgreBotAPI:NPC_CastMonitoring["all","${This.MobName}"]
		Event[OgreEvent_CastMonitoring_CastingStarted]:AttachAtom[This:OgreEvent_CastMonitoring_CastingStarted]
		Event[OgreEvent_CastMonitoring_CastingEnded]:AttachAtom[This:OgreEvent_CastMonitoring_CastingEnded]

		echo CastMonSpread: watching "${This.MobName}" for ability ${This.DangerSpellID}
	}

	;--------------------------------------------------------------------------
	; Destructor - LavishScript calls Shutdown automatically when this object is
	; destroyed (script end, scope end, deletevariable). Detach event handlers.
	;--------------------------------------------------------------------------
	method Shutdown()
	{
		Event[OgreEvent_CastMonitoring_CastingStarted]:DetachAtom[This:OgreEvent_CastMonitoring_CastingStarted]
		Event[OgreEvent_CastMonitoring_CastingEnded]:DetachAtom[This:OgreEvent_CastMonitoring_CastingEnded]
	}

	;--------------------------------------------------------------------------
	; <<< EDIT: define your spread spots here. Insert order = rank order.
	;           First Insert = spot for rank #1, second = rank #2, etc.
	;--------------------------------------------------------------------------
	method SetupSpots()
	{
		; NOTE: LavishScript comments must be on their OWN line - a ';' only starts
		;       a comment when it is the first non-whitespace char on the line.
		;       A trailing ';' after a command is NOT a comment (it gets parsed as
		;       part of the statement), so each rank label is its own line below.
		; rank 1
		This.SpreadSpots:Insert[100.0,10.0,-50.0]
		; rank 2
		This.SpreadSpots:Insert[105.0,10.0,-50.0]
		; rank 3
		This.SpreadSpots:Insert[110.0,10.0,-50.0]
		; rank 4
		This.SpreadSpots:Insert[115.0,10.0,-50.0]
		; rank 5
		This.SpreadSpots:Insert[120.0,10.0,-50.0]
		; rank 6
		This.SpreadSpots:Insert[125.0,10.0,-50.0]
	}

	;--------------------------------------------------------------------------
	; Work out MY rank using OgreBot's built-in group ordering, via the public
	; OgreBotAPI passthroughs:
	;   OgreBotAPI.CountGroupBy["all","All"]      = total members in the group
	;   OgreBotAPI.GetGroupIDBy["all","All",N]    = actor ID of the Nth member
	;                                               (1-based) in a fixed order
	;                                               that is identical on every
	;                                               session.
	; The "All" search mode returns the whole group (it ignores the first arg).
	; We compare each member's actor ID to ${Me.ID} - IDs are preferred over
	; names: an actor's ID is the same for everyone in the zone, so every toon
	; independently computes the exact same rank with no communication.
	; (The order itself is alphabetical by character name under the hood, which
	;  is why it's stable and identical across sessions.)
	;--------------------------------------------------------------------------
	method ComputeMyRank()
	{
		variable int iTotal=${OgreBotAPI.CountGroupBy["all","All"]}
		variable int iCounter

		This.iMyRank:Set[0]

		for ( iCounter:Set[1] ; ${iCounter} <= ${iTotal} ; iCounter:Inc )
		{
			if ${OgreBotAPI.GetGroupIDBy["all","All",${iCounter}]} == ${Me.ID}
			{
				This.iMyRank:Set[${iCounter}]
				break
			}
		}
	}

	;--------------------------------------------------------------------------
	; Cast STARTS -> each toon moves itself to its own spot.
	;--------------------------------------------------------------------------
	method OgreEvent_CastMonitoring_CastingStarted(int64 _ActorID, int64 _AbilityID, float _AbilityCastingTime)
	{
		if !${OgreBotAPI.InCombat}
			return

		if ${_AbilityID} != ${This.DangerSpellID}
			return

		if ${This.bMovedOut}
			return

		; Figure out which spot is mine (recomputed each cast in case the group
		; changed).
		This:ComputeMyRank

		; Safety: make sure we actually have a spot for our rank.
		if ${This.iMyRank} < 1 || ${This.iMyRank} > ${This.SpreadSpots.Used}
		{
			echo CastMonSpread: no spot for rank ${This.iMyRank} - not moving.
			return
		}

		This.bMovedOut:Set[TRUE]

		; Move MY toon to MY spot. CRCS = Change Relative Camp Spot (override).
		OgreBotAPI:CRCS["${Me.Name}",${This.SpreadSpots[${This.iMyRank}]}]

		echo CastMonSpread: moving to spread spot #${This.iMyRank}.
	}

	;--------------------------------------------------------------------------
	; Cast ENDS -> return immediately (clear the relative override).
	;--------------------------------------------------------------------------
	method OgreEvent_CastMonitoring_CastingEnded(int64 _ActorID, int64 _AbilityID)
	{
		if ${_AbilityID} != ${This.DangerSpellID}
			return

		if !${This.bMovedOut}
			return
		This.bMovedOut:Set[FALSE]

		OgreBotAPI:ClearRCS["${Me.Name}"]

		echo CastMonSpread: returned to campspot.
	}
}

variable Object_CastMonSpread Spread

function main()
{
	while !${OgreBotAPI.IsReady}
		wait 10

	Spread:Setup

	; To stop: endscript CastMon_SpreadToOwnSpots_Standalone
	; (Cleanup is automatic - the object's Shutdown destructor detaches events
	;  when the script ends and the Spread object is destroyed.)
	while 1
		wait 50
}
```

---

## Related Documentation

- [Move group on cast](cast-move-group.md) — The companion example with a timer-delayed return
- [Examples overview](index.md) — How to run, requirements, and shared concepts
- [Preferred Group Members](../preferred-group-members.md) — Group & raid member ordering
- [CampSpot System](../camp-spot.md) — Relative campspot (CRCS / ClearRCS)
- [OgreBotAPI Reference](../ogrebot-api.md) — Full API for controlling OgreBot
