# Chat Commands

OgreBot can be controlled through in-game chat channels. These commands let you and your group members issue instructions to the bot without opening the UI.

> **:warning: Authorization Required**
>
> Chat commands only work when sent by a character on your **EQ2Chars authorized list**. Unauthorized characters are ignored for security.

---

## Essence and Shard Requests

These commands request summoned items from Conjurors and Necromancers:

| Command | What It Does |
|---------|-------------|
| `need essence` | Asks a Conjuror to summon a shard |
| `heart please` / `shard please` | Summons from a Conjuror or Necromancer |
| `raid essence please` | Casts a raid-wide shard (if mana and spell are available) |

---

## Movement Control

These commands control follow and movement behavior:

| Command | What It Does |
|---------|-------------|
| `do not move` | Stops follow and disables auto-follow |
| `hold up` / `place here` | Disables auto-follow |
| `lets go` / `lets move` / `move up` | Re-enables auto-follow |

---

## Follow Commands

Tell specific characters or groups to follow you:

| Command | What It Does |
|---------|-------------|
| `follow me` | All characters follow you |
| `mages follow me` | Only mages follow you |
| `G1 follow me` | Only Group 1 follows you |
| `come to me` | Characters move to your location |
| `melee come to me` | Only melee characters come to you |
| `mages come to me` / `casters come to me` | Only casters come to you |
| `priests come to me` / `healers come to me` | Only healers come to you |

---

## Group Management

These commands work via **tell** channel only:

| Command | What It Does |
|---------|-------------|
| `group invite: CharacterName` | Invites a character to your group |
| `group invite me` | Requests a group invite for yourself |
| `make me leader` | Transfers group leadership to you |
| `kick CharacterName from group` | Removes a character from the group |

> **:memo: Tell Only**
>
> Group management commands must be sent as a **tell** (private message) to the character running OgreBot. They do not work in group or raid chat.

---

## Buffing

| Command | What It Does |
|---------|-------------|
| `full rebuff` | Removes all maintained buffs and reapplies them from scratch |

> **:bulb: When to Use Full Rebuff**
>
> Use this when buffs get out of sync, after a zone-wide buff wipe, or when you want to make sure all buffs are freshly applied.

---

## Utility Commands

| Command | What It Does |
|---------|-------------|
| `repair gear` | Targets the nearest mender (e.g., in a guild hall) and repairs |
| `revive` | Resurrects dead group/raid members |
| `mentor me` | Mentors the character who sent the command |
| `mentor:CharacterName` | Mentors a specific character by name |

---

## Command Channels

Most commands can be sent through multiple channels:

| Channel | Usage |
|---------|-------|
| **Tell** | Send a private message to the character running OgreBot |
| **Group** | Send in group chat (all group members with OgreBot will respond) |
| **Raid** | Send in raid chat (all raid members with OgreBot will respond) |

Some commands (like group management) are restricted to tells only, as noted above.

---

## Console Commands

In addition to chat commands, you can type commands directly in the InnerSpace console (`~`):

| Command | What It Does |
|---------|-------------|
| `ogre` | Loads or reloads OgreBot |
| `ogre export` | Exports all abilities for the current character |
| `ogre export SpellName` | Exports a single ability by name |

<!-- Source: wiki.ogregaming.com/eq2/index.php/OgreBotChatCommands - This page may need updating -->
