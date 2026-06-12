# Public API Reference

eq2codex exposes a small **read API** so you can pull item and drop data into your own
tools — a Discord bot, a spreadsheet, an overlay, whatever you're building. It's the same
data the website renders, returned as clean JSON, plus two ready-to-embed PNG images (the
item icon and the full in-game examine tooltip).

**Base URL:** `https://eq2codex.com/api/v1`

> **:bulb: This is a read API.** It's for *fetching* item/drop/merchant data. Uploading your
> own captures (toons, loot) is a separate path handled by the capture clients — see
> [Getting an API Token](getting-a-token.md) and the [About page](https://eq2codex.com/about).

---

## Authentication

The JSON endpoints require an **eq2codex API token** — the same token you create in
[Getting an API Token](getting-a-token.md). Send it as a bearer credential:

```
Authorization: Bearer YOUR_TOKEN
Accept: application/json
```

The two **image endpoints** ([icon](#item-icon-png) and [tooltip](#item-tooltip-png)) are
**unauthenticated on purpose** — so you can drop the URL straight into an `<img>` tag or a
Discord embed and let the client fetch it with no auth header. They only ever serve
publicly-visible items, so there's nothing sensitive behind them.

> **:warning: Keep your token private.** A token is tied to your account. If you think one
> leaked, revoke it from the [API tokens page](https://eq2codex.com/settings/api-tokens) and
> generate a fresh one — see the FAQ in [Getting an API Token](getting-a-token.md).

---

## Conventions

- **Versioned base path** — `/api/v1/`. Additive changes (new fields) won't move it; a
  breaking change would cut a `/v2`.
- **Rate limit** — 300 requests per minute (keyed by your token; by IP on the unauthenticated
  image routes). Over the limit returns **429**.
- **Item IDs** — an item's id (`item_id_a`) is an EQ2 signed 32-bit integer, so it **can be
  negative** (e.g. `-1834603534`). If your tooling only has the unsigned form (a number
  greater than `2147483647`), you can send that — the server normalizes it by subtracting
  2³². Both forms resolve to the same item.

### Response envelopes

- **Detail** endpoints return the object directly: `{ "item_id_a": ..., ... }`.
- **Search** endpoints return `{ "query": "<q>", "count": <n>, "results": [ ... ] }`.

### Errors

| Status | Body | When |
|---|---|---|
| `401` | `{ "message": "Unauthenticated." }` | missing or invalid token |
| `404` | `{ "error": "not_found" }` | unknown item/merchant, or one that isn't public |
| `422` | `{ "message": ..., "errors": {...} }` | bad query parameters |
| `429` | `{ "message": "Too Many Requests" }` | rate limited |

---

## Item search

`GET /api/v1/items/search`

Fuzzy item lookup — type part of a name, get back matching items. Useful as the first step in
a `/item <name>` style command: search, show the user the matches, then fetch the chosen id.

| Param | Type | Required | Notes |
|---|---|---|---|
| `q` | string | yes | 2–120 characters. |
| `limit` | int | no | 1–25, default 10. |

Matching is an anchored prefix on the item name; if that finds nothing it retries once as a
substring match, so a mid-name fragment ("wind xii") still hits.

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
     -H "Accept: application/json" \
     "https://eq2codex.com/api/v1/items/search?q=flow%20like%20wind&limit=5"
```

```json
{
  "query": "flow like wind",
  "count": 2,
  "results": [
    {
      "item_id_a": 123456,
      "name": "Flow Like Wind XII (Grandmaster)",
      "tier": "Fabled",
      "rarity_color": "#cf5567",
      "type": "Spell Scroll",
      "level": 128,
      "resolve": null,
      "icon_url": "https://eq2codex.com/api/v1/items/123456/icon",
      "url": "https://eq2codex.com/items/123456"
    }
  ]
}
```

---

## Item detail (JSON)

`GET /api/v1/items/{item_id_a}`

Everything about one item — the full examine data the website shows, plus where it drops.

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
     -H "Accept: application/json" \
     "https://eq2codex.com/api/v1/items/123456"
```

```json
{
  "item_id_a": 123456,
  "name": "Flow Like Wind XII (Grandmaster)",
  "tier": "Fabled",
  "rarity_color": "#cf5567",
  "type": "Spell Scroll",
  "sub_type": null,
  "level": 128,
  "resolve": null,
  "icon_url": "https://eq2codex.com/api/v1/items/123456/icon",
  "url": "https://eq2codex.com/items/123456",
  "classes": ["monk"],
  "mod_flags": ["NO-TRADE", "NO-VALUE"],
  "examine": {
    "description": null,
    "modifiers": [ { "type": "...", "sub_type": "Haste", "value": 102.9 } ],
    "effects": [ { "name": "...", "description": "..." } ],
    "effect_strings": [ { "text": "Increases bleedthrough...", "indent_level": 0 } ],
    "set_bonuses": [ ],
    "weapon": null,
    "armor": null,
    "charges": { "current": null, "max": 0 },
    "flags": { "no_trade": true, "no_value": true, "lore": false }
  },
  "drops": {
    "total": 47,
    "shown": [
      {
        "zone": "Spiral of Vul [Contested]",
        "source_type": "chest",
        "source_npc": "Gentok the Scourgebringer",
        "chest_type": "Exquisite",
        "contributor_count": 12,
        "last_seen": "2026-06-09T18:03:42+00:00"
      }
    ],
    "more_url": "https://eq2codex.com/items/123456#drops"
  }
}
```

Notes:

- `mod_flags` is the human-facing token list (e.g. `NO-TRADE`) the examine window shows.
- `drops.shown` is capped at **10**, ordered by contributor count then most-recently-seen, with
  private zones (guild halls / placeholders) excluded. `total` is the full count for the same
  query, so you can say "+37 more"; `more_url` deep-links the site's drops section.

---

## Item icon (PNG)

`GET /api/v1/items/{item_id_a}/icon` — *no auth required*

The item's icon as a standalone **PNG**, ready to use as a Discord embed thumbnail or any
`<img>` source. (The website stores icons as tiles in sprite atlases and crops them with CSS;
this endpoint crops the single tile for you and returns a real image.)

```
https://eq2codex.com/api/v1/items/123456/icon
```

- Returns `Content-Type: image/png`, cached for a week.
- **404** if the item is unknown, not public, or has no icon.

> **:memo: No `.png` on the URL — that's intentional.** The path is extension-less; the
> response is still a PNG (it's the `Content-Type` that matters, which is what Discord and
> browsers render from). Don't append `.png`.

---

## Item tooltip (PNG)

`GET /api/v1/items/{item_id_a}/tooltip` — *no auth required*

The **full in-game examine window** — the framed item card with rarity colors, the icon,
adornment-slot gems, and the stat block — rendered as a single **PNG**. This is the
pixel-faithful tooltip the eq2codex new-items Discord feed posts under each item, and a Discord
embed can't reproduce it (an embed gets one accent color and no border), so you get it as an
image instead.

```
https://eq2codex.com/api/v1/items/123456/tooltip
```

- Returns `Content-Type: image/png`, cached for a week. (Unlike the icon it's not marked
  *immutable*, because a re-examine can update the tooltip.)
- **404** if the item is unknown or not public.
- Same extension-less convention as the icon — don't append `.png`.

> **:bulb: Use it as the image in your own embed.** Point your embed's image/thumbnail at this
> URL alongside the JSON from [item detail](#item-detail-json) and you've reproduced the feed's
> look: your text + link from the JSON, the in-game card from this PNG.

---

## Merchant search

`GET /api/v1/merchants/search`

Fuzzy merchant lookup (case-insensitive substring on the merchant name).

| Param | Type | Required | Notes |
|---|---|---|---|
| `q` | string | yes | 2–120 characters. |
| `limit` | int | no | 1–25, default 10. |

```json
{
  "query": "tradesman",
  "count": 1,
  "results": [
    { "id": 42, "name": "Tradesman Halv", "server": "Maj'Dul", "zone_name": "Qeynos Harbor", "guild": null }
  ]
}
```

---

## Merchant detail

`GET /api/v1/merchants/{id}`

A merchant and the items they sell.

```json
{
  "id": 42,
  "name": "Tradesman Halv",
  "server": "Maj'Dul",
  "zone_name": "Qeynos Harbor",
  "guild": null,
  "location": { "x": -12.3, "y": 4.5, "z": 88.1 },
  "notes": "Behind the bank.",
  "url": "https://eq2codex.com/merchants/42",
  "items": {
    "total": 73,
    "shown": [
      {
        "item_id_a": 123456,
        "name": "Cloak of Untold Heroism",
        "tier": "Fabled",
        "rarity_color": "#cf5567",
        "type": "Cloak",
        "level": 130,
        "coin_price": 5000000,
        "coin_price_text": "5p",
        "has_additional_cost": true,
        "icon_url": "https://eq2codex.com/api/v1/items/123456/icon",
        "url": "https://eq2codex.com/items/123456"
      }
    ],
    "more_url": "https://eq2codex.com/merchants/42"
  }
}
```

Notes:

- `items.shown` is capped at **25**, ordered by item name. `coin_price` is raw copper (`null` =
  unknown, `0` = free); `coin_price_text` is the formatted EQ2 coin string.
- `has_additional_cost` means the item also requires an in-game trade-in currency.

---

## Rarity → color map

The `rarity_color` returned with each item matches the website's examine colors — handy if
you're setting a Discord embed's accent color to match the item's tier.

| Tier | Hex |
|---|---|
| Fabled | `#cf5567` |
| Legendary | `#ffc993` |
| Mythical | `#d99fe9` |
| Treasured | `#93d9ff` |
| Uncommon | `#beff93` |
| (other / unknown) | `#cccccc` |

---

*EverQuest 2 is © Daybreak Game Company. eq2codex is an unofficial fan tool.*
