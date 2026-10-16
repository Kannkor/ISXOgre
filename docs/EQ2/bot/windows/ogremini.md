# OgreBot

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../index.md).
</div>

> **:bulb: In game - the ? button on this window says**
>
> The small OgreBot window: a quick remote for pausing the bot and showing or hiding the main OgreBot window.
>
> **What you can do here**
>
> - **Pause / Resume** - Pause stops the bot acting on its own (casting, following, camp spot, looting, Auto-Hunt). The button turns yellow and reads Resume.
> - **Hide Main / Show Main** - hides or shows the main OgreBot window. The bot keeps running.
>
> **Good to know**
>
> - The X on this window stops OgreBot completely, the same as the X on the main window. Unsaved changes are lost.
> - A yellow star (*) in the title bar means the profile has unsaved changes.
> - Pause only affects this character. Commands you send still work while paused.

**Open it:** It opens by itself whenever OgreBot loads (type `ogre`), next to the main OgreBot window. `ogre end bot` closes both. Opening it again while it is open does nothing (typing `ogre` reloads the whole bot instead).

[![OgreBot](../assets/ogremini/window.png)](../assets/ogremini/window.png "Click for full size")

## What it is for

The small OgreBot window is a two-button remote for the bot. Pause stops the bot from acting on its own and Resume starts it again. Hide Main hides the big OgreBot window and Show Main brings it back. OgreBot normally loads with the big window hidden, so this small window is what you see.

## Pause and Resume

[![Pause and Resume](../assets/ogremini/pause.png)](../assets/ogremini/pause.png "Click for full size")

| Control | What it does | Default |
|---|---|---|
| **Pause / Resume** | Pause stops this character's bot from acting on its own, for example: no new casts from the cast stack, no following, no pulling back to the camp spot, no looting, no auto-targeting, no Auto-Hunt. Commands you send still work. The button turns yellow and reads Resume. Click it to start the bot again.<br>*Only this character pauses, not the group. If something else pauses or resumes the bot, the button updates by itself.* | running (Pause shown) after `ogre`; paused after `ogre -p` or `ogre -ph` |

## Show / Hide the main window

[![Show / Hide the main window](../assets/ogremini/main.png)](../assets/ogremini/main.png "Click for full size")

| Control | What it does | Default |
|---|---|---|
| **Hide Main / Show Main** | Hides the big OgreBot window, or shows it again. The bot keeps running either way. Only the window is hidden. | Show Main (the big window starts hidden after `ogre`) |

## Title bar

[![Title bar](../assets/ogremini/titlebar.png)](../assets/ogremini/titlebar.png "Click for full size")

| Control | What it does | Default |
|---|---|---|
| *** (yellow star)** | The profile has changes that are not saved yet. Save them on the big OgreBot window. | hidden |
| **Title bar close (X)** | Shuts OgreBot down completely, the same as the X on the big window. Both windows close, movement and HUDs stop, the profile is unloaded, and unsaved changes are thrown away.<br>*To just get the big window out of the way, use Hide Main.* |  |

## What the window shows

- Pause (green) = the bot is running. Resume (yellow) = the bot is paused.
- Show Main = the big window is hidden. Hide Main = it is on screen.

## Good to know

- The X on this small window stops OgreBot. It is not a minimize.
- Pause only stops what the bot decides by itself. Commands from you or your group still run.

## Paused, with the main window hidden

![Paused](../assets/ogremini/paused.png)

