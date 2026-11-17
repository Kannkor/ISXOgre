# ISXOgreEQ2.MerchantOps

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Members

### `Running`

`${ISXOgreEQ2.MerchantOps.Running}`

TRUE while a buyfuel or buycrate run is in progress. Only one runs at a time; starting another is refused with a busy warning.

**Returns:** bool: TRUE while a fuel or crate purchase run is going; FALSE when idle.

```text
echo ${ISXOgreEQ2.MerchantOps.Running}
```

### `Status`

`${ISXOgreEQ2.MerchantOps.Status}`

One line naming the running merchant run and its progress, or "idle". It is the same text `${ISXOgreEQ2.MerchantOps}` returns.

**Returns:** string: "idle", "buyfuel '&lt;fuel>' (round n)" or "buycrate (done/total)".

```text
echo ${ISXOgreEQ2.MerchantOps.Status}
```

## Methods

### `BuyCrate`

`ISXOgreEQ2.MerchantOps:BuyCrate[flags...]`

The engine behind `ogre buycrate`: targets and opens this zone's crate merchant (who must be nearby), buys one of each chosen heroic and raid crate, accepts the purchase prompt and closes the merchant. Only exp17_dun_fordel_midst and exp18_rgn_svarni_expanse have one (Svarni sells no heroic crate), and anywhere else, or when nothing matches the flags, the call is refused with a warning.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `flags...` | string | `-all` | -r/-raid for the raid crate, -h/-heroic for the heroic crate, -all for both; read left to right, so `-raid -all` buys both and `-all -raid` only the raid crate; unknown words are ignored |

```text
ISXOgreEQ2.MerchantOps:BuyCrate[-h]
```

### `BuyFuel`

`ISXOgreEQ2.MerchantOps:BuyFuel[amount]`

The engine behind `ogre buyfuel`: at the guild hall Fuel Depot (within 11 m) it counts how much of the fuel you have EXAMINED the depot holds, buys the shortfall from the merchant titled Guild Fuel Merchant and deposits it, repeating for at most 10 rounds. It is refused when nothing is examined, a run is already going or you are not in the world, and stops with a console warning when the depot is missing, too far or does not open.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `amount` | int | `90000` | how much of the fuel the depot should end up holding; missing, not a whole number, or 0 or less uses 90000 |

```text
ISXOgreEQ2.MerchantOps:BuyFuel[20000]
```

### `Stop`

`ISXOgreEQ2.MerchantOps:Stop`

Stops a running buyfuel or buycrate and prints "merchant: stopped."; does nothing when idle. Open depot or merchant windows are left as they are.

```text
ISXOgreEQ2.MerchantOps:Stop
```
