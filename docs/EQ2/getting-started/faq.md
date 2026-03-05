# Frequently Asked Questions

---

## Getting Started

### What do I do first?

Check the [pricing page](../about/pricing.md) to obtain a subscription, then follow the [Installation Guide](installation.md) step by step.

### I just subscribed. Now what?

Follow the [Installation Guide](installation.md) from start to finish. It walks you through downloading, installing, authenticating, and running OgreBot for the first time. If you have questions after completing the walkthrough, visit the [Contact](../community/contact.md) page for support options.

### How do I auto-load ISXOgre?

See the [Auto-Loading ISXOgre](auto-loading.md) guide to configure InnerSpace to load ISXOgre automatically every time you launch EQ2.

### How do I copy text from the console?

See [How to Copy from the Console](copy-from-console.md).

### How do I connect multiple computers via Uplink?

See [Connecting Computers via Uplink](connect-computers.md).

### How do I remove the memory and FPS display?

See [Removing Memory and FPS Display](remove-fps-display.md).

---

## OgreBot Usage

### OgreBot seems very slow at casting spells. What is wrong?

You likely have **Ability Queue** turned off in EQ2. This is a game setting, not an OgreBot setting.

1. Open your EQ2 game options
2. Find the **Ability Queue** setting
3. Turn it **on**
4. Restart the game

### My spells or abilities are missing from OgreBot.

You need to run an export so OgreBot can learn your abilities:

1. Open the InnerSpace console (press `~`)
2. Type `ogre export` and press Enter
3. **Do not zone or recast abilities** while the export runs
4. When the export finishes, reload OgreBot by typing `ogre` in the console

> **:bulb: Exporting Individual Abilities**
>
> You can export a single ability by name: `ogre export SpellNameHere`
> You can also export by spell ID if needed.

> **:memo: Multiple AA Specs**
>
> If you use multiple AA specs, export each spec separately so OgreBot knows about all your abilities.

### OgreBot stops casting. What is wrong?

See [Troubleshooting: Bot Stops Casting](bot-stops-casting.md) for step-by-step diagnosis.

---

## Troubleshooting

### I am getting an error about an incomplete index.

This usually happens when you move, sell, or destroy an item while OgreBot is scanning your items in the Item page of the UI. Close the Item tab and rescan your items.

### One of my UI windows has disappeared.

If your game resolution changed or a window was dragged off-screen, you can reset window positions:

1. Open the InnerSpace console (press `~`)
2. Type `run uireset` and press Enter

This resets all OgreBot window positions back to their defaults.

### How do I repatch ISXOgre?

See [Repatching ISXOgre](repatching.md). In most cases, simply opening a new session will automatically apply any needed patches.

### Why is ISXOgre deleting files?

ISXOgre removes `awesomium_process.exe` (an outdated web-browser framework bundled with EQ2) by renaming and then deleting it. This prevents conflicts with the game client. This is expected behavior and nothing to worry about.

---

## Getting Help

### I need help and cannot figure something out!

Before asking for help, please:

1. **Read the error message carefully** -- it often tells you exactly what is wrong
2. **Search the wiki and documentation** -- your question may already be answered
3. **Provide the exact error text** when asking for help, not a paraphrase
4. **Stick to facts** -- describe what happened, not what you think happened
5. **Be respectful** -- community members volunteer their time to help

> **:bulb: Best Place to Ask**
>
> Discord is the most active community channel for getting help. See the [Contact](../community/contact.md) page for the invite link.

### I have a feature request!

See [Feature Requests](../community/feature-requests.md) for how to submit a good request.

---

## Still Have Questions?

If your question is not answered here, check the [Contact](../community/contact.md) page for ways to reach the community and developers.

<!-- Source: wiki.ogregaming.com/eq2/index.php/Ogre:FAQ - This page may need updating -->
