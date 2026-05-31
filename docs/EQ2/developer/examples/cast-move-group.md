# Move the group to a safe spot on cast

A standalone script that watches one mob for one ability. When that ability **starts** casting, your toon moves to a safe spot. When it **finishes**, a 4-second timer fires a custom event that returns the toon to its normal campspot.

> **:warning: Requires a recent OgreBot build** and an active campspot for the fight. See the [Examples overview](index.md) for both requirements.

---

## What it does

- Turns on NPC cast monitoring for one mob.
- When that mob **starts** casting a specific ability → moves your toon to a safe spot.
- When that ability **finishes** casting → starts a 4-second timer, and when the timer fires a custom event, the toon returns to the normal campspot.

This is the **timer → event** pattern in action.

---

## What you edit

All edit points are marked `<<< EDIT` in the code:

- The **mob name** (exactly as it appears when you `/target` it).
- The **ability ID** to watch — get this from **Ogre Analysis** (it isn't available from in-game APIs).
- The **safe-spot coordinates** (`X,Y,Z`). Stand where you want the toon to go and read your loc.

You can also tune `ReturnDelaySeconds` (how long after the cast ends before returning).

---

## How it works

**Cast monitoring** — `OgreBotAPI:NPC_CastMonitoring["all","${This.MobName}"]` enables monitoring and auto-checks the box. The bot's background monitor fires the global events `OgreEvent_CastMonitoring_CastingStarted` / `OgreEvent_CastMonitoring_CastingEnded`; the object attaches handlers to them using the standard [OgreEvents](../ogre-events.md) attach/detach pattern.

**Move and return** — uses the relative campspot from the [CampSpot System](../camp-spot.md). `OgreBotAPI:CRCS["${Me.Name}",x,y,z]` overrides the campspot with an absolute safe spot; `OgreBotAPI:ClearRCS["${Me.Name}"]` clears it so the toon returns to wherever the normal campspot is now. Because the script runs on every toon, each toon moves itself. (To move the whole group from one toon instead, the comments show the `oc !c -CS_Set_Relative` / `-CS_ClearRelative` equivalents.)

**Timer → event** — when the cast ends, the handler starts an `Object_Timer`:

```lavishscript
Timer_Return:SetSeconds[4,"CastMonMover_ReturnNow","-TriggerEventName","CastMonMover_ReturnNow"]
```

When the 4 seconds elapse, the timer automatically fires the custom event `CastMonMover_ReturnNow` (registered with `LavishScript:RegisterEvent` and hooked with `Event[...]:AttachAtom`), whose handler does the return. `Object_Timer` ships with the bot and is included via `OgreCommon/Object_Timer.iss`.

> **:memo: Note**
>
> The object's `Shutdown` method is a destructor — LavishScript calls it automatically when the script ends and the script-scoped object is destroyed. It detaches the event handlers so they don't linger or double-fire. See [`OgreBotAPI`](../ogrebot-api.md) for `InCombat` / `IsReady` state checks used here.

---

## How to run

```lavishscript
; Run on everyone in the group:
oc !ci -RunScriptOB igw:${Me.Name} CastMon_MoveGroup_Standalone

; Run on just yourself:
run CastMon_MoveGroup_Standalone

; Stop later (on each toon):
endscript CastMon_MoveGroup_Standalone
```

Stop the old copy before re-launching so events don't attach twice.

---

## The script

```lavishscript
;==============================================================================
; EXAMPLE 1 (STANDALONE): Move toons to a different campspot when a mob casts,
;                         then return 4 seconds AFTER the cast ends.
;------------------------------------------------------------------------------
; Answers the Discord question:
;   "is there a way to tell toons to go to a different campspot when a mob
;    spell starts casting?"
;
; This is a STANDALONE script. You do NOT need OgreBot's source code. You drop
; this .iss in your Scripts folder and RUN it on your toons. It talks to the
; bot only through the public OgreBotAPI object (which is always available) and
; OgreBot's cross-session "oc" commands.
;
; WHAT IT DOES
;   - Turns on NPC cast monitoring for one mob.
;   - When that mob STARTS casting a specific ability -> moves your toon(s) to
;     a safe spot.
;   - When that ability FINISHES casting -> starts a 4-second timer, and when
;     the timer fires a custom EVENT, the toon returns to the normal campspot.
;     (This shows the timer -> event pattern you asked about.)
;
; HOW TO RUN IT  (the "running on everyone" model)
;   1. Put this file in your InnerSpace Scripts folder (where you run scripts from).
;   2. From any toon in the group, launch it on EVERYONE in the group:
;          oc !ci -RunScriptOB igw:${Me.Name} CastMon_MoveGroup_Standalone
;      (To run on just yourself:  run CastMon_MoveGroup_Standalone )
;   3. To stop it later, on each toon:  endscript CastMon_MoveGroup_Standalone
;      (or use  oc !ci -RunScriptOB ...  again only after stopping the old one,
;       so the events don't get attached twice).
;
; WHAT YOU MUST EDIT  (search for "<<< EDIT"):
;   - The mob name
;   - The ability ID to watch  (get this from Ogre Analysis)
;   - The safe-spot coordinates
;
; REQUIREMENT: your toons must already have a campspot active for the fight
;   (your normal bot fight setup / the dynamic campspot checkbox). The "move"
;   is a RELATIVE override of that campspot, and the "return" clears the
;   override so they go back to wherever the campspot is now.
;==============================================================================

; Object_Timer ships with the bot in the OgreCommon folder - this include is
; safe for a standalone script and gives us the timer -> event feature.
#include "${LavishScript.HomeDirectory}/Scripts/OgreCommon/Object_Timer.iss"

;------------------------------------------------------------------------------
; The worker object. All our state and event handlers live in here.
;------------------------------------------------------------------------------
objectdef Object_CastMonMover
{
	; <<< EDIT: exact mob name (as it appears when you /target it).
	variable string MobName="Boss Name Here"

	; <<< EDIT: the ability ID to react to (from Ogre Analysis).
	variable int64 DangerSpellID=1234567890

	; <<< EDIT: where to send the toon when the cast starts. Format: X,Y,Z
	;           Stand where you want them to go and read your loc to get this.
	variable point3f SafeSpot=100.0,10.0,-50.0

	; How long to wait AFTER the cast ends before returning. (seconds)
	variable float ReturnDelaySeconds=4.0

	; A timer that, when it expires, fires the "CastMonMover_ReturnNow" event.
	variable Object_Timer Timer_Return

	; Stops us moving / returning more than once per cast.
	variable bool bMovedOut=FALSE

	;--------------------------------------------------------------------------
	; Called once at startup.
	;--------------------------------------------------------------------------
	method Setup()
	{
		; Turn on NPC cast monitoring for our mob. This single call also
		; AUTO-ENABLES the "npc cast monitoring" checkbox - no manual toggle.
		OgreBotAPI:NPC_CastMonitoring["all","${This.MobName}"]

		; Listen for the cast-monitoring events (these are global; the bot's
		; background monitor fires them, our object just listens).
		Event[OgreEvent_CastMonitoring_CastingStarted]:AttachAtom[This:OgreEvent_CastMonitoring_CastingStarted]
		Event[OgreEvent_CastMonitoring_CastingEnded]:AttachAtom[This:OgreEvent_CastMonitoring_CastingEnded]

		; Register our OWN custom event and attach its handler. The Object_Timer
		; will fire this event by name when it expires (see CastingEnded below).
		LavishScript:RegisterEvent[CastMonMover_ReturnNow]
		Event[CastMonMover_ReturnNow]:AttachAtom[This:CastMonMover_ReturnNow]

		echo CastMonMover: watching "${This.MobName}" for ability ${This.DangerSpellID}
	}

	;--------------------------------------------------------------------------
	; Destructor. LavishScript calls Shutdown automatically whenever this object
	; is destroyed (script ends naturally/forcefully, scope ends, deletevariable).
	; We use it to detach our event handlers so they don't linger / double-fire.
	;--------------------------------------------------------------------------
	method Shutdown()
	{
		Event[OgreEvent_CastMonitoring_CastingStarted]:DetachAtom[This:OgreEvent_CastMonitoring_CastingStarted]
		Event[OgreEvent_CastMonitoring_CastingEnded]:DetachAtom[This:OgreEvent_CastMonitoring_CastingEnded]
		Event[CastMonMover_ReturnNow]:DetachAtom[This:CastMonMover_ReturnNow]
	}

	;--------------------------------------------------------------------------
	; Fires when a monitored mob STARTS casting.
	;--------------------------------------------------------------------------
	method OgreEvent_CastMonitoring_CastingStarted(int64 _ActorID, int64 _AbilityID, float _AbilityCastingTime)
	{
		; Only react in combat.
		if !${OgreBotAPI.InCombat}
			return

		; Only react to the one spell we care about.
		if ${_AbilityID} != ${This.DangerSpellID}
			return

		if ${This.bMovedOut}
			return
		This.bMovedOut:Set[TRUE]

		; Cancel any pending "return" timer from a previous cast.
		This.Timer_Return:Stop

		; Move MY toon to the safe spot. CRCS = Change Relative Camp Spot: it
		; overrides the current campspot with this absolute location. Because
		; this script runs on every toon, every toon moves itself.
		;
		;   "${Me.Name}" = just this toon (this is a LOCAL OgreBotAPI call).
		;
		; (If instead you run this on ONE toon and want IT to move the whole
		;  group, replace the line below with:
		;     oc !c -CS_Set_Relative igw:${Me.Name} ${This.SafeSpot.XYZ[" "]}
		;  which routes the move to every toon in the group.)
		OgreBotAPI:CRCS["${Me.Name}",${This.SafeSpot}]

		echo CastMonMover: "${This.MobName}" started casting - moving to safe spot.
	}

	;--------------------------------------------------------------------------
	; Fires when a monitored mob FINISHES casting.
	; We don't return immediately - we start a 4-second timer that will fire
	; our custom event "CastMonMover_ReturnNow".
	;--------------------------------------------------------------------------
	method OgreEvent_CastMonitoring_CastingEnded(int64 _ActorID, int64 _AbilityID)
	{
		if ${_AbilityID} != ${This.DangerSpellID}
			return

		if !${This.bMovedOut}
			return

		; Start a timer for ReturnDelaySeconds. The 4 args to SetSeconds are:
		;   1) seconds to wait
		;   2) a name for this timer (free text)
		;   3) "-TriggerEventName"
		;   4) the event to fire when the timer expires
		; When the timer hits 0 it automatically fires CastMonMover_ReturnNow,
		; which runs the method below. THIS is the timer -> event pattern.
		This.Timer_Return:SetSeconds[${This.ReturnDelaySeconds},"CastMonMover_ReturnNow","-TriggerEventName","CastMonMover_ReturnNow"]

		echo CastMonMover: cast ended - returning in ${This.ReturnDelaySeconds}s.
	}

	;--------------------------------------------------------------------------
	; Our custom event handler - runs ~4 seconds after the cast ended because
	; the Object_Timer fired the "CastMonMover_ReturnNow" event.
	;--------------------------------------------------------------------------
	method CastMonMover_ReturnNow()
	{
		This.bMovedOut:Set[FALSE]

		; Clear the relative override -> toon returns to the normal campspot.
		; (Group-on-one-toon variant:  oc !c -CS_ClearRelative igw:${Me.Name} )
		OgreBotAPI:ClearRCS["${Me.Name}"]

		echo CastMonMover: returned to campspot.
	}
}

;------------------------------------------------------------------------------
; Script-scoped instance of our object.
;------------------------------------------------------------------------------
variable Object_CastMonMover Mover

function main()
{
	; Wait until the bot/API is ready before we call any OgreBotAPI methods.
	while !${OgreBotAPI.IsReady}
		wait 10

	Mover:Setup

	; Keep the script alive so the events can keep firing. Everything happens
	; in the event handlers above; this loop just idles.
	;
	; To stop: endscript CastMon_MoveGroup_Standalone
	; (Cleanup is automatic - the object's Shutdown method fires when the script
	;  ends and the script-scoped Mover object is destroyed.)
	while 1
		wait 50
}
```

---

## Related Documentation

- [Spread to own spots](cast-spread-spots.md) — The companion example using per-toon spots
- [Examples overview](index.md) — How to run, requirements, and shared concepts
- [CampSpot System](../camp-spot.md) — Relative campspot (CRCS / ClearRCS)
- [OgreEvents](../ogre-events.md) — Event attach/detach pattern
- [OgreBotAPI Reference](../ogrebot-api.md) — Full API for controlling OgreBot
