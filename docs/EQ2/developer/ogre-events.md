# OgreEvents

OgreBot fires events at key moments so your scripts can react without polling. Attach a handler to any event you care about, and your method is called automatically when it fires.

---

## Available Events

| Event | Description |
|-------|-------------|
| `OgreEvent_OnAbilityCast` | You cast an ability |
| `OgreEvent_OnAbilityCastCompleted` | Your ability cast finishes |
| `OgreEvent_OnItemUse` | You use an item |
| `OgreEvent_OthersOnAbilityCast` | Another group member casts an ability |
| `OgreEvent_OthersOnAbilityCastCompleted` | Another group member's cast finishes |
| `OgreEvent_OthersOnItemUse` | Another group member uses an item |
| `OgreEvent_OnGainedTithe` | You gain a tithe point |
| `OgreEvent_GearConditionReport` | Gear condition update |
| `OgreEvent_SmartLootAssigned` | Smart loot assigned to a character |
| `OgreEvent_KronoRedemption` | A Krono redemption attempt completed |
| `OgreEvent_InGameTell` | An in-game tell was received |
| `OgreEvent_InGameTellSent` | An in-game tell was sent |
| `OgreEvent_SpewStats` | Stats data broadcast |
| `OgreEvent_OnAbilityReadyTimersUpdate` | Ability ready timers updated |

---

## How Events Work

### 1. Attach Your Handler

Use `AttachAtom` to connect your method to an event:

```
Event[OgreEvent_KronoRedemption]:AttachAtom[MyKronoHandler]
```

### 2. Define the Handler Method

Your method signature must match the event's parameters:

```
method MyKronoHandler(string _sCharacterName, bool _bSuccess)
{
    if ${_bSuccess}
        echo ${_sCharacterName} redeemed a Krono!
    else
        echo ${_sCharacterName} failed to redeem a Krono.
}
```

### 3. Detach When Done

Always detach when your script ends to avoid orphaned handlers:

```
Event[OgreEvent_KronoRedemption]:DetachAtom[MyKronoHandler]
```

> **:memo: Note**
>
> If your handler is a method inside an `objectdef`, use the `Object:Method` syntax:
> ```
> Event[OgreEvent_KronoRedemption]:AttachAtom[MyObject:MyKronoHandler]
> Event[OgreEvent_KronoRedemption]:DetachAtom[MyObject:MyKronoHandler]
> ```

---

## Event Reference

### OgreEvent_KronoRedemption

Fires when a Krono redemption attempt completes — either successfully or with a failure.

| Parameter | Type | Description |
|-----------|------|-------------|
| `_sCharacterName` | `string` | Name of the character who attempted the redemption |
| `_bSuccess` | `bool` | `TRUE` if redeemed successfully, `FALSE` if it failed |

**Example:**

```
function main()
{
    Event[OgreEvent_KronoRedemption]:AttachAtom[OnKrono]

    while 1
    {
        waitframe
    }
}

method OnKrono(string _sCharacterName, bool _bSuccess)
{
    if ${_bSuccess}
        echo ${Time}: ${_sCharacterName} redeemed a Krono successfully!
    else
        echo ${Time}: ${_sCharacterName} failed to redeem a Krono.
}
```

---

### OgreEvent_OnAbilityCast

Fires when you cast an ability.

| Parameter | Type | Description |
|-----------|------|-------------|
| `_Caster` | `string` | Name of the caster |
| `_AbilityID` | `uint` | Ability ID |
| `_AbilityName` | `string` | Name of the ability |
| `_OnPlayerID` | `uint` | Target player ID (0 if no target) |
| `_OnPlayer` | `string` | Target player name (empty if no target) |

```
method OnAbilityCast(string _Caster, uint _AbilityID, string _AbilityName, uint _OnPlayerID, string _OnPlayer)
```

---

### OgreEvent_OnAbilityCastCompleted

Fires when your ability cast finishes.

| Parameter | Type | Description |
|-----------|------|-------------|
| `_Caster` | `string` | Name of the caster |
| `_AbilityID` | `uint` | Ability ID |
| `_AbilityName` | `string` | Name of the ability |

```
method OnAbilityCastCompleted(string _Caster, uint _AbilityID, string _AbilityName)
```

---

### OgreEvent_OnItemUse

Fires when you use an item.

| Parameter | Type | Description |
|-----------|------|-------------|
| `_Caster` | `string` | Name of the caster |
| `_AbilityName` | `string` | Name of the item |
| `_OnPlayerID` | `uint` | Target player ID (0 if no target) |
| `_OnPlayer` | `string` | Target player name (empty if no target) |

```
method OnItemUse(string _Caster, string _AbilityName, uint _OnPlayerID, string _OnPlayer)
```

---

### OgreEvent_OthersOnAbilityCast

Fires when another group member casts an ability. Same parameters as `OgreEvent_OnAbilityCast`.

```
method OthersOnAbilityCast(string _Caster, uint _AbilityID, string _AbilityName, uint _OnPlayerID, string _OnPlayer)
```

---

### OgreEvent_OthersOnAbilityCastCompleted

Fires when another group member's cast finishes. Same parameters as `OgreEvent_OnAbilityCastCompleted`.

```
method OthersOnAbilityCastCompleted(string _Caster, uint _AbilityID, string _AbilityName)
```

---

### OgreEvent_OthersOnItemUse

Fires when another group member uses an item. Same parameters as `OgreEvent_OnItemUse`.

```
method OthersOnItemUse(string _Caster, string _AbilityName, uint _OnPlayerID, string _OnPlayer)
```

---

### OgreEvent_OnGainedTithe

Fires when you gain a tithe point. No parameters.

```
method OnGainedTithe()
```

---

### OgreEvent_SmartLootAssigned

Fires when smart loot is assigned.

| Parameter | Type | Description |
|-----------|------|-------------|
| `_Toon` | `string` | Character who received the loot |
| `_Item` | `string` | Item name |
| `_Value` | `int` | Quantity |

```
method OnSmartLootAssigned(string _Toon, string _Item, int _Value)
```

---

### OgreEvent_GearConditionReport

Fires with gear condition data.

| Parameter | Type | Description |
|-----------|------|-------------|
| `_Caster` | `string` | Character name |
| `_GearAmount` | `uint` | Gear condition amount |

```
method OnGearConditionReport(string _Caster, uint _GearAmount)
```

---

### OgreEvent_InGameTell

Fires when an in-game tell is received.

| Parameter | Type | Description |
|-----------|------|-------------|
| `Speaker` | `string` | Who sent the tell |
| `ChatTarget` | `string` | Who received the tell |
| `Message` | `string` | The message content |

```
method OnInGameTell(string Speaker, string ChatTarget, string Message)
```

---

### OgreEvent_InGameTellSent

Fires when an in-game tell is sent. Same parameters as `OgreEvent_InGameTell`.

```
method OnInGameTellSent(string Speaker, string ChatTarget, string Message)
```

---

### OgreEvent_OnAbilityReadyTimersUpdate

Fires when ability ready timers are updated.

| Parameter | Type | Description |
|-----------|------|-------------|
| `_Toon` | `string` | Character name |
| `_AbilityID` | `int64` | Ability ID |
| `_AbilityName` | `string` | Ability name |
| `_TimeUntilReady` | `float` | Seconds until the ability is ready |

```
method OnAbilityReadyTimersUpdate(string _Toon, int64 _AbilityID, string _AbilityName, float _TimeUntilReady)
```

---

## Related Documentation

- [OgreBotAPI Reference](ogrebot-api.md) — Full API for controlling OgreBot
- [Detrimentals System](detrimentals.md) — Detrimental monitoring events
- [Coding Practices](coding-practices.md) — Naming conventions and code style
