# Run your own fight files

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../index.md).
</div>

A **fight file** (an encounter file) tells the bot what to do in one named fight: where to stand, what to cast,
and what to do when the mob does something. A zone file walks the group through the zone; the fight files do the
fighting. The ones that ship are in `Scripts\Ogre\EQ2\Encounters\default\`, one file per named, in
`<Expansion>\<Zone>\<Named>.json`.

## You never run a fight file by its name

No command, button or zone file step takes a fight file's name or path. The bot picks the file itself, from
**the zone you are in** and **the named mob's name**. So to have your own file used, three things must be true:

1. The file is in the custom folder (below), at the right place.
2. Its `zone` and `named` match the zone you are in and the mob you are fighting.
3. A setup starts for that mob: by itself when the fight starts, or when you ask for one (from a button or a
   zone file, below).

## Where your fight files go

Put them in `Scripts\OgreSave\EQ2\Encounters\custom\`. Make the folder if it is not there: nothing makes it for
you. Folders inside it are fine, at any depth. The folder and file names decide nothing; the `zone` and `named`
inside the file do.

### Changing a fight that ships

Copy the shipped file into `custom` **at the same place**: `custom\<Expansion>\<Zone>\<Named>.json`, with the
same folder and file names as in `default`. Then:

- Yours is laid over the shipped one, key by key. Anything you leave out comes from the shipped file, so a file
  that only holds the part you changed works. A list or a single value you give replaces the shipped one whole.
- To have your file replace the shipped one completely instead, add `"noMerge": true` at the top of yours.

> **Same mob, different place = ignored.** A custom file at any other path that names the same mob in the same
> zone is skipped, and the load says so: `mob '<name>' in zone '<zone>' is already claimed by <file> - skipping
> duplicate`. The shipped file keeps the fight. Put yours at the shipped file's path.

### A fight that has no file yet

Any path in `custom` works, as long as no other file already claims that mob in that zone. Copying a shipped file
from a similar fight is the easiest start.

### What decides the match

| Key | What it does |
|---|---|
| `zone` | The zone's name as the game shows it, difficulty included: `"Gerion: Realm of Conquest [Untold Heroic]"`. Case does not matter, and the instance number is left off. A list covers several zones. Leave it out and the file is for any zone. |
| `named` | The mobs this fight is for, each `{ "name": "...", "aliases": ["..."], "distance": 50 }`. A setup starts when one of them is in range (`distance`). |
| `enabled` | `false` turns the file off without deleting it. |

## Loading your changes

The bot reads the fight files when it starts, and again on zone-in when a file has changed. To load them at once,
type `ogre encounter reload`.

On zone-in the console lists the fights this zone has a file for (unless **No Available Setups** is ticked on the
Settings tab). The `-ShowAvailableSetups` command prints that list any time: if your fight is not on it, the bot
did not match your file to this zone.

## When a setup starts

**By itself:** when one of the file's named is in this zone, in a fight (it has a target), and within its
`distance`. That needs:

- **Enable Raid Setups** (raid zones) or **Enable Heroic Setups** (every other zone) ticked on the Settings tab.
  With it off, no setup starts at all, by itself or by hand.
- **Disable Auto Setups** unticked, and the bot not paused. These two stop only the setups that start by
  themselves.

**By hand:** from a button, a zone file or a script, below. This works while paused and with Disable Auto Setups
ticked, but the named must still be up in this zone, and either in range or in a fight.

## From an MCP button

Either of these:

- **The `-SetUpFor` command.** Pick `-SetUpFor` in the button builder and set:
    - **who**: the characters to set up (the For Who, as on any button);
    - **chat**: the named's name, for example `Dagrin`. Leave it blank and each character sets up for the nearest
      or engaged named;
    - **restart**: TRUE starts the setup over if one is already running.
- **Raw mode** with `ISXOgreEQ2.Encounter:Fire["Dagrin"]`. Raw runs only on the character that clicks the
  button.

A name no fight file claims in this zone prints `Fire: no encounter owns mob '<name>'` in the console.

## From a zone file

You usually need nothing. A [named](steps.md#named) step already sets up for the fight: when the named engages, IC
tells every character in the group to set up for its engaged named, and each one finds its fight file by matching.

To set up for one mob by name at another point, run the command with a `raw` step (see
[Other actions](other-actions.md)):

```json
{ "stepId": "setup.dagrin", "do": "raw", "command": "oc !ci -SetUpFor igw:{{me}} \"Dagrin\"" }
```

The quotes around the name are escaped (`\"`) because they sit inside the JSON string.
