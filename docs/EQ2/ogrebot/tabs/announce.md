# Announce

<!-- TODO: Add screenshot -->

The Announce tab controls when the bot communicates with others using chat macros similar to player communication.

!!! warning
    Exercise caution when using this feature with actual players. The bot may attempt to cast spells in situations beyond its control. For instance, if a target cannot be acquired, the bot lacks the ability to detect this limitation and will still attempt the spell cast.

## Target Replacement

The `*Target*` placeholder automatically substitutes the ability's target name. This placeholder can be used multiple times within the text.

**Example:** A message stating `*Target* I am casting an ability on you *Target*` directed at character Kannkor would announce: `Kannkor I am casting an ability on you Kannkor`

## Announce Target Settings

You configure three elements for each announcement: the **ability**, the **target**, and the **message text**.

### Communication Methods

| Method | Description |
|--------|-------------|
| **Group** | Broadcasts via `/gsay` command |
| **Raid** | Broadcasts via `/raid` command |
| **Tell To Target** | Sends a private message to the ability's target using `/tell` |

## Text Execution

The **Included in text** option executes commands as written. For example, `/gc blah blah *Target*` becomes `/gc blah blah Kannkor`.

## NULL Fragment Restriction

Messages containing "NULL" will not be announced, as the system interprets this as indicating an error. This limitation prevents announcing abilities or character names containing "null" (such as Warlock's Null Caress).

<!-- Source: wiki.ogregaming.com - This page may need updating -->
