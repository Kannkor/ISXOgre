# Chat Events

<!-- TODO: Add screenshot -->

The Chat Events tab enables monitoring of chat text for specific phrases and automatic execution of code when triggers occur. This tab must be enabled via the **Enable Chat Events** checkbox on the Settings 2 tab.

## Settings

### Text to watch for

The string of text that you want the bot to look for to take action on.

### Code to execute

A single line of code that runs when the monitored text appears. This supports commands from the OgreBotAPI.

### [OC] On success - Send message to Ogre Console

When enabled, the bot will notify you via the Ogre Console upon detecting the watched text.

### [Ding] On success

When enabled, the bot will play an audible sound to notify you of the event when the trigger text is found.

## Example

| Field | Value |
|-------|-------|
| **Text to watch for** | `Hail, Kannkor` |
| **Code to execute** | `OgreBotAPI:Jump[all]` |
| **[OC] On success** | Checked |
| **[Ding] On success** | Checked |

**Result:** The bot monitors chat and, upon detecting "Hail, Kannkor", executes the jump command for all group members while sending a console notification and playing an audio alert.

<!-- Source: wiki.ogregaming.com - This page may need updating -->
