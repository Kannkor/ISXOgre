# Troubleshooting: Bot Stops Casting

If OgreBot stops casting spells unexpectedly, it is always for a reason. The most common cause is abilities placed in the wrong section.

---

## Step 1: Check Spell Placement

OgreBot expects abilities to be in the correct sections:

- **Buffs** should be in the buffs section
- **Combat arts and spells** should be in the combat section
- **Self/group spells** should target yourself
- **Other spells** should have a valid PC target

> **:warning: Important**
>
> OgreBot assumes you have entered all abilities into the correct sections. If a buff is placed in the combat section or a combat art is placed in buffs, the bot may stop casting.

---

## Step 2: Review All Tabs

Go through each configuration tab and verify that every ability is in the correct location and has the correct target.

---

## Step 3: Enable Debug Mode

If the above steps do not resolve the issue:

1. Open the OgreBot main window
2. Click the **Debug** tab (bottom-left area)
3. Enable **CastingDebug**
4. Watch the console output -- it will show which ability is causing the bot to stop

---

## Step 4: Investigate the Problem Ability

Once you identify the ability from the debug output:

1. Find it in your OgreBot configuration
2. Verify it is in the correct section
3. Verify it has a valid target
4. Check that the ability is not on cooldown or restricted

If the ability appears correctly configured but still causes issues, visit the [Contact](../community/contact.md) page for community support options.

<!-- Source: wiki.ogregaming.com/eq2/index.php/Help:BotStopsCasting -->
