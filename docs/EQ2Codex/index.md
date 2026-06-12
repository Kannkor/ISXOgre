# EQ2 Codex

**eq2codex** is a community-built database of EverQuest 2 item, drop, and character data. An Ogre Gaming project by **Kannkor** and **LostOne**.

**Live site:** [https://eq2codex.com](https://eq2codex.com)

---

## How much does it cost?

Nothing — eq2codex is free. It's a community project, built to give EverQuest 2 players a place to look up item and drop details while Census is down.

---

## What it offers

- **Searchable item database** — browse EQ2 items with their full in-game examine windows, sprites, stats, effects, and class restrictions.
- **Drop sources** — see which mobs and zones drop each item, aggregated from community contributions.
- **Character pages** — upload your toons via OgreBot and get full stat/gear/adornment pages, plus side-by-side comparisons.
- **Raid roster + gear report** — build a persistent raid roster (your toons or census-shadow toons), see everyone's gear and adornments side by side, and compare against a curated adornment sheet.
- **Adornment sheets** — curate "the right adornments per slot" for your guild's role/tier and apply them to any raid's gear report for green/yellow/red compliance scoring.
- **[Public JSON API](api-reference.md)** — structured access to item and drop data, plus ready-to-embed icon and tooltip images.

---

## Walkthroughs

If you're new to codex, the docs below walk through each surface in order — pick the one you want and dive in.

### Uploading data

- **[Getting an API Token](getting-a-token.md)** — set up the eq2codex account and token that the ACT plugin and OgreBot's **Codex Inspect** / **Codex Toons** tabs use to push your data to the site. Start here if you want your toons to show up.

### Building on the data

- **[Public API Reference](api-reference.md)** — pull item, drop, and merchant data into your own tools (a Discord bot, a spreadsheet, an overlay) as clean JSON, plus ready-to-embed icon and full-tooltip PNG images. Needs a token from the page above.

### Working with your characters

- **[Comparing Characters](compare-characters.md)** — put two toons side by side and see every stat, gear slot, and adornment difference with explicit Δ columns. Works for both your OgreBot-uploaded toons and census-only shadow toons.
- **[My Raids](my-raids.md)** — build a persistent raid roster (OgreBot toons, census shadows, or a mix), arrange them into raid groups, and read the whole raid's gear and adornments in one table.
- **[Adornment Sheets](adornment-sheets.md)** — curate a reusable "the right adornments per slot" list (white/blue/black/orange/cyan/green), share it with other users, and apply it to any raid's gear report to instantly see who's compliant and who's not.

---

## How data gets in

eq2codex doesn't scrape. Data comes from capture clients that upload directly from your game session:

- **ACT plugin** — Advanced Combat Tracker plugin that uploads loot drops live as they happen. *Available now.*
- **OgreBot — Codex Inspect / Codex Toons tabs** — uploads roster, gear, adornments, and stats for your in-game toons. *Available now.*
- **Standalone log scanner** — Python tool that reads EQ2 chat logs and uploads loot drops. Install + setup instructions at [eq2codex.com/install/standalone](https://eq2codex.com/install/standalone).

All clients use the same JSON API and connect to the same uploader account. Drops are aggregated community-wide; the system counts distinct contributors per drop, not individual contribution counts.

Each client requires an API token — see [Getting an API Token](getting-a-token.md). Capture client downloads and setup instructions are on the [About page](https://eq2codex.com/about).

---

*EverQuest 2 is © Daybreak Game Company. eq2codex is an unofficial fan tool.*
