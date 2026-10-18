# Developers

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../index.md).
</div>

This section is for people who write their own scripts for OgreBot: raid modules, instance files, side
scripts, MCP buttons, and console lines.

Everything in the new bot has its own TLO and datatypes, so you can explore the scripting surface in game
with `lstype`. The two you will use most are `ISXOgreEQ2` and `OgreBotAPI`.

## Where to start

- **Moving a Classic script over?** Start with [Converting your scripts](converting.md). It has a tool
  that checks a script and fixes what it safely can, and a step-by-step procedure you can hand to Claude.
- **Want a window of your own in game?** [Build your own window](build-your-own-window.md) shows how a script
  or an extension opens one, reads and changes what is in it, and reacts to clicks.
- **Looking up one name?** [Coming from Classic](coming-from-classic/index.md) lists Classic's API
  calls, objects, events and console commands, and what each one is in the new bot.

> **:bulb: Using Claude (or another AI assistant)?**
>
> Point it at `https://kannkor.github.io/ISXOgre/EQ2/bot/llms.txt`. That file lists these pages as plain
> text, so the assistant can read them directly. For a script conversion, also tell it to follow the
> procedure on [Converting your scripts](converting.md).
