# EQ2 Chars

<!-- TODO: Add screenshot -->

The EQ2 Chars tab is a character management interface for storing and managing your EverQuest 2 character information.

## Fields

| Field | Required | Description |
|-------|----------|-------------|
| **Character Name** | Yes | The name of the character |
| **Account Name** | No | The account associated with the character |
| **Password** | No | The account password (for auto-login) |
| **Comments** | No | Optional notes about the character |

## Data Storage

Character information is stored in `/EQ2OgreCommon/DoNotShareWithOthers/EQ2Chars.xml`. These settings are saved globally and are **not** part of your OgreBot profile, allowing a single setup for all characters.

## Adding and Removing Entries

- **Left-click** to select an entry
- **Right-click** to remove an entry
- When adding a new entry matching an existing character name, the system removes any entry with the same character name first

## Editing Behavior

When selecting a list item, all fields repopulate except passwords, which remain blank. This protects saved passwords from accidental overwriting during edits.

## Group/Raid Feature

The **Add Current Group/Raid** button adds all current raid or group members to the character list if they do not already exist.

## Auto-Login

Using OgreAutoLogin requires all of the following fields to be filled in:

- Account Name
- Password
- Server

## Display

Account name, character name, and server are displayed in the interface. Passwords remain hidden for security.

<!-- Source: wiki.ogregaming.com - This page may need updating -->
