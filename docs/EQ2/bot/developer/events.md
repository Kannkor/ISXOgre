# OgreEvents

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../index.md).
</div>

The events Classic's *OgreEvents* page listed, and whether the new bot still raises each one.

> **:warning: An event the new bot does not raise never fires**
>
> Attaching to it still works without an error, so the script looks fine and the handler simply never runs.

## At a glance

| What happened | Names |
|---|---|
| ➡️ Lives somewhere else | 5 |
| ⛔ Not ported yet | 12 |
| ⛔ Removed | 1 |
| ✅ Works as is | 13 |
| **Total** | **31** |

## Events

An atom attached to an event the new bot never raises never runs - and nothing says so.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `OgreEvents:CreateEvents` | does nothing | automatic (no call) | ➡️ Lives somewhere else | Nothing to call: the new bot registers every event itself. |
| `OgreEvent_GearConditionReport` | works | — | ✅ Works as is |  |
| `OgreEvent_InGameTell` | works | — | ✅ Works as is |  |
| `OgreEvent_InGameTellSent` | works | — | ✅ Works as is |  |
| `OgreEvent_KronoRedemption` | works | — | ✅ Works as is |  |
| `OgreEvent_OnAbilityCast` | works | — | ✅ Works as is |  |
| `OgreEvent_OnAbilityCastCompleted` | works | — | ✅ Works as is |  |
| `OgreEvent_OnAbilityReadyTimersUpdate` | works | — | ✅ Works as is | LOCAL only now ( 'Local-only event (no relay twin)'). Classic sent it raid-wide (irw:), so a script on ANOTHER session that listened for this toon's timers hears nothing. |
| `OgreEvent_OnGainedTithe` | never fires | — | ⛔ Removed | Classic: registered and NEVER fired (no Execute of it anywhere in EQ2OgreBot / EQ2OgreCommon / OgreCommon) - the doc's 'You gain a tithe point' never happened. New: registered, never fired. Registration REMOVED: "Tith is dead in game". |
| `OgreEvent_OnItemUse` | works | — | ✅ Works as is | It also fires for food, drink and potions now, not only clickies. |
| `OgreEvent_OthersOnAbilityCast` | works | — | ✅ Works as is |  |
| `OgreEvent_OthersOnAbilityCastCompleted` | works | — | ✅ Works as is |  |
| `OgreEvent_OthersOnItemUse` | works | — | ✅ Works as is |  |
| `OgreEvent_SmartLootAssigned` | works | — | ✅ Works as is |  |
| `OgreEvent_SpewStats` | works | — | ✅ Works as is |  |
| `OgreEvents:OgreEvent_GearConditionReport` | does nothing | — | ⛔ Not ported yet | Classic handler returns on its first line - dead. |
| `OgreEvents:OgreEvent_InGameTell` | does nothing | automatic (no call) | ➡️ Lives somewhere else | Nothing to call: the new bot relays and pushes tells by itself; the OgreBot settings above switch the parts. |
| `OgreEvents:OgreEvent_InGameTellSent` | does nothing | automatic (no call) | ➡️ Lives somewhere else | Nothing to call: the new bot does this by itself. |
| `OgreEvents:OgreEvent_KronoRedemption` | does nothing | — | ⛔ Not ported yet | Classic handler, attached at, only echoes 'redeemed / failed to redeem a Krono' to the console. The new bot fires the event but has no console echo attached to it; searched and. Attach your own atom if you want the line. |
| `OgreEvents:OgreEvent_OnAbilityCast` | does nothing | automatic (no call) | ➡️ Lives somewhere else | Nothing to call: the new bot relays every cast by itself. |
| `OgreEvents:OgreEvent_OnAbilityCastCompleted` | does nothing | — | ⛔ Not ported yet | Classic handler relays the completion to the other sessions as OgreEvent_OthersOnAbilityCastCompleted. New: no cast-completion event is raised at all, so there is nothing to relay. |
| `OgreEvents:OgreEvent_OnAbilityReadyTimersUpdate` | does nothing | — | ⛔ Not ported yet | Classic echo-only handler, never attached (42 commented out). Dead in Classic. The event fires on the new bot - see event:OgreEvent_OnAbilityReadyTimersUpdate. |
| `OgreEvents:OgreEvent_OnAbilityReadyTimersUpdate2` | does nothing | — | ⛔ Not ported yet | Classic echo-only test handler, never attached (43 commented out). Dead in Classic. |
| `OgreEvents:OgreEvent_OnGainedTithe` | does nothing | — | ⛔ Not ported yet | Classic handler: with checkbox_settings_autospend_deitypoints, queue OgreBotAPI:SpendDietyPoints. Dead twice in Classic: nothing ever fires OgreEvent_OnGainedTithe (no Execute in EQ2OgreBot / EQ2OgreCommon / OgreCommon), and SpendDietyPoints' working line is commented out. New: the event is a registered stub and there is no deity-point spender. |
| `OgreEvents:OgreEvent_OnItemUse` | does nothing | automatic (no call) | ➡️ Lives somewhere else | Nothing to call: the new bot relays every item use by itself. |
| `OgreEvents:OgreEvent_OthersOnAbilityCast` | does nothing | — | ⛔ Not ported yet | Classic handler returns on its first line - dead. Nothing to port. |
| `OgreEvents:OgreEvent_OthersOnAbilityCastCompleted` | does nothing | — | ⛔ Not ported yet | Classic handler has an EMPTY body. Nothing to port. |
| `OgreEvents:OgreEvent_OthersOnItemUse` | does nothing | — | ⛔ Not ported yet | Classic handler returns on its first line - dead. Nothing to port. |
| `OgreEvents:OgreEvent_SmartLootAssigned` | does nothing | — | ⛔ Not ported yet | Classic 'Testing only' handler that echoes '&lt;toon&gt; looted &lt;n&gt; &lt;item&gt;'. The new bot fires the event with no echo attached; searched /. |
| `OgreEvents:OgreEvent_SpewStats` | does nothing | — | ⛔ Not ported yet | Classic handler only echoes the JSON, and is NOT attached (its AttachAtom is commented out, :39). Dead in Classic. The event itself fires on the new bot - see event:OgreEvent_SpewStats. |
| `OgreEvents:OgreEvent_SpewStats2` | does nothing | — | ⛔ Not ported yet | Classic test handler that echoes the JSON; never attached (40 commented out). Dead in Classic. |

## Not in the new bot yet

If your script needs one of these, leave it out for now and tell us - this list is what still needs work.

- `OgreEvents:OgreEvent_GearConditionReport` - not ported yet
- `OgreEvents:OgreEvent_KronoRedemption` - not ported yet
- `OgreEvents:OgreEvent_OnAbilityCastCompleted` - not ported yet
- `OgreEvents:OgreEvent_OnAbilityReadyTimersUpdate` - not ported yet
- `OgreEvents:OgreEvent_OnAbilityReadyTimersUpdate2` - not ported yet
- `OgreEvents:OgreEvent_OnGainedTithe` - not ported yet
- `OgreEvents:OgreEvent_OthersOnAbilityCast` - not ported yet
- `OgreEvents:OgreEvent_OthersOnAbilityCastCompleted` - not ported yet
- `OgreEvents:OgreEvent_OthersOnItemUse` - not ported yet
- `OgreEvents:OgreEvent_SmartLootAssigned` - not ported yet
- `OgreEvents:OgreEvent_SpewStats` - not ported yet
- `OgreEvents:OgreEvent_SpewStats2` - not ported yet
