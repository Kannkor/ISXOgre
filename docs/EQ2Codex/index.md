# EQ2 Codex

**eq2codex** is a community-built database of EverQuest 2 item, drop, and character data. An Ogre Gaming project by **Kannkor** and **LostOne**, separate from ISXOgre / OgreBot.

**Live site:** [https://eq2codex.com](https://eq2codex.com)

---

## What It Offers

- **Searchable item database** — browse EQ2 items with their full in-game examine windows, sprites, stats, effects, and class restrictions.
- **Drop sources** — see which mobs and zones drop each item, aggregated from community contributions.
- **Character dashboards** — authenticated user dashboards for personal toon planning (in progress).
- **Public JSON API** — structured access to item and drop data.

## How Data Gets In

eq2codex doesn't scrape. Data comes from capture clients that upload directly from your game session:

- **ACT plugin** — Advanced Combat Tracker plugin that uploads loot drops live as they happen. *Available now.*
- **Standalone log scanner** — Python tool that reads EQ2 chat logs and uploads loot drops. *Coming soon.*

Both clients use the same JSON API and connect to the same uploader account. Drops are aggregated community-wide; the system counts distinct contributors per drop, not individual contribution counts.

Capture client downloads and setup instructions are on the [About page](https://eq2codex.com/about).

---

## Documentation

Full user documentation is in progress. In the meantime, the [About page](https://eq2codex.com/about) on the live site has the most up-to-date overview of capture clients and project status.

---

*EverQuest 2 is © Daybreak Game Company. eq2codex is an unofficial fan tool.*
