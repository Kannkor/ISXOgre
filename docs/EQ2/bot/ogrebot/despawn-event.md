# Despawn Event

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../index.md).
</div>

Despawn Event is the opposite of Spawn Events: it fires when something whose name contains your text disappears. The bot can then run a console command, post a line to OgreConsole, play a 'Ding' sound, or any mix of the three. Nothing happens until you tick "Enable Despawn Event" on the Settings tab. Build events with the boxes at the top; they appear in the Configured Events list below.

[![Despawn Event tab](../assets/ogrebot/tab-despawn-event.png)](../assets/ogrebot/tab-despawn-event.png "Click for full size")

| Option | What it does | Default |
|---|---|---|
| **Configured Events** | Your despawn events. Click a row to edit it, double-click to switch it off or on, drag a row to reorder, and click X to delete it.<br>*A switched-off row is kept but never fires.* | empty |

## Add an event

| Control | What it does | Default |
|---|---|---|
| **Actor to watch for** | Part or all of the name to watch for. The event fires when something with a matching name disappears. Upper and lower case must match exactly.<br>*Required. An event with no name cannot be added.* | empty |
| **Code to execute (leave blank for nothing)** | A console command to run when a match disappears. It runs exactly as if you typed it into the InnerSpace console. Leave it blank if you only want the OC line or the Ding. | empty |
| **OC - on success, send a message to OgreConsole** | When a match disappears, a line goes to OgreConsole saying which character saw it, the text it matched and the full name. | off |
| **Ding - on success, play a 'Ding'** | When a match disappears, a 'Ding' sound plays on this PC. | off |
| **Add** | Adds the event to the list below. Pressing Enter in either text box does the same. While you are editing a row this button reads Update and saves your changes to that row. |  |
| **Clear Options** | Unticks OC and Ding. Ticks otherwise carry over to the next event you add. |  |
| **Cancel** | Only shown while editing a row. Stops editing without changing the row. |  |

## Good to know

- Nothing here works until "Enable Despawn Event" is ticked on the Settings tab.
- The name match is case-sensitive: "vindicator" does not match "a Vindicator". Part of the name is enough.
- Something leaving your view can count as disappearing, not only a mob that dies or despawns.
- An event with no command, no OC and no Ding is ignored, and the console prints a warning about it.
- The OC and Ding ticks stay ticked for the next event you add. Use Clear Options to untick them.
- Despawn events keep working while OgreBot is paused.

