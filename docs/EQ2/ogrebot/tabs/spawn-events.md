# Spawn Events

<!-- TODO: Add screenshot -->

The Spawn Events tab enables monitoring for specific NPC spawns and executes code when triggers occur. This tab must be enabled via the **Enable Spawn Events** checkbox on the Settings 2 tab.

## Settings

### Actor to watch for

Enter the NPC name the bot should detect and respond to when it spawns.

### Code to execute

A single line of code to run when the monitored NPC spawns. This supports basic code and OgreBotAPI commands.

### [OC] On success - Send message to Ogre Console

When enabled, the bot notifies you through the Ogre Console upon detecting the watched NPC spawn.

### [Ding] On success

When enabled, produces an audible alert sound when the target NPC spawns.

## Example

| Field | Value |
|-------|-------|
| **Actor to watch for** | `an iksar child` |
| **Code to execute** | `OgreBotAPI:Jump[all]` |
| **[OC] On success** | Checked |
| **[Ding] On success** | Checked |

**Result:** The bot monitors for "an iksar child" to spawn. Upon detection, it executes `OgreBotAPI:Jump[all]`, causing the entire group to jump. You also receive a console message and audible notification.

<!-- Source: wiki.ogregaming.com - This page may need updating -->
