# OgreBotAPI.Merchant

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Methods

### `Buy`

`OgreBotAPI.Merchant:Buy[fw, item, qty=1]`

With a merchant window already open, buys qty of the named item from the merchant's list, right away, and accepts the purchase prompt if one comes up. No item, no merchant window, or an item the merchant does not carry each get one line.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `item` | string |  | Name of the item on the merchant's list |
| `qty` | int | `1` | How many to buy |

```text
OgreBotAPI.Merchant:Buy[${Me.Name},"Fishing Bait",20]
```

*Was (OldBot):* `OgreBotAPI:BuyFromMerchant`, `Obj_OgreIH:BuyFromMerchant`

### `OpenAndBuy`

`OgreBotAPI.Merchant:OpenAndBuy[fw, merchant, item, qty=1]`

Queued: opens the merchant window by double-clicking the nearest actor whose name contains merchant (unless a merchant window is already open), waits up to 3 seconds for it, buys qty of item and accepts the purchase confirmation. A missing name prints a console line, a window that never opens or an item the merchant does not carry prints a line and buys nothing, and no matching actor stops it silently.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `merchant` | string |  | Name (or part of the name) of the merchant to open |
| `item` | string |  | Name of the item on the merchant's list |
| `qty` | int | `1` | How many to buy |

```text
OgreBotAPI.Merchant:OpenAndBuy[${Me.Name},"Provisioner","Fishing Bait",20]
```

*Was (OldBot):* `OgreBotAPI:OpenAndBuyFromMerchant`

### `OpenAndBuyXTimes`

`OgreBotAPI.Merchant:OpenAndBuyXTimes[fw, merchant, item, qty, times]`

Queued: does OpenAndBuy times times in a row - each round opens the merchant if needed, buys qty of item and accepts the confirmation. A missing merchant or item name, or times of 0 or less, prints a console line and nothing runs.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `merchant` | string |  | Name (or part of the name) of the merchant to open |
| `item` | string |  | Name of the item on the merchant's list |
| `qty` | int |  | How many to buy each round (1 when blank) |
| `times` | int |  | How many rounds to buy (1 when blank) |

```text
OgreBotAPI.Merchant:OpenAndBuyXTimes[${Me.Name},"Provisioner","Fishing Bait",100,3]
```

*Was (OldBot):* `OgreBotAPI:OpenAndBuyFromMerchantXTimes`

### `Repair`

`OgreBotAPI.Merchant:Repair[fw, force=FALSE]`

Queued: unless force is TRUE, checks your primary and chest items and stops with "no repair needed" when both are at 100% condition. Otherwise finds a known mender within 10m (prints "no mender within 10m" if none), stops auto-attack, opens it, repairs everything and closes the window.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `force` | bool | `FALSE` | TRUE to repair even when primary and chest are already at 100% |

```text
OgreBotAPI.Merchant:Repair[igw:${Me.Name},FALSE]
```

*Was (OldBot):* `OgreBotAPI:RepairGear`

### `Sell`

`OgreBotAPI.Merchant:Sell[fw, item, qty=1]`

With a merchant window already open, sells qty of the named item from your bags, right away. No item, no merchant window, or an item not in the sell list each get one line.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `item` | string |  | Name of the item in your bags |
| `qty` | int | `1` | How many to sell |

```text
OgreBotAPI.Merchant:Sell[${Me.Name},"Rough Ruby",5]
```

*Was (OldBot):* `OgreBotAPI:SellToMerchant`, `Obj_OgreIH:SellToMerchant`
