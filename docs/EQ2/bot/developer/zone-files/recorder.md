# Record a fight with the Encounter Recorder

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../index.md).
</div>

The **Encounter Recorder** writes down everything the game shows during a fight: who is there, where they stand, what
lands on whom, what the game says, what the named casts and spawns. Afterwards you can work the fight out from the
recording alone, and write or fix its [fight file](fight-files.md). It only reads the game; it never acts, and it
never records what players say in chat.

Type `ogre er` (or `ogre encounterrecorder`) to open it. The **?** on its title bar lists every switch and button.

> **No promises.** This is a tool for people who write fight files. Use it at your own risk, and expect it to change.

## 1. Before the pull

1. `ogre er on` starts recording on this box. It is never on by itself: switch it on after every login. For the
   whole group or raid, press the window's second **On** (For Who), or type `ogre er onforwho`.
2. Choose what is written. These are saved for the PC:
    - **Record trash pulls**: only when the boss is not marked as a named by the game.
    - **Examine every det**: only when two different dets share their icons. Off, each new pair of icons is examined
      once.
    - **Pets**: only when pets matter to the fight.
    - **Read the names of effects on NPCs**: one session of a PC is enough (`is1`, unless you tick it elsewhere).
3. An event that never puts anyone in combat: **Start a file** and **End the file** by hand (`ogre er start` and
   `ogre er stop`).
4. During the fight, **Mark** (or `ogre er mark <text>`) drops a note on the timeline: "wipe here", "the add came".

## 2. After the pull

1. The recording is under `OgreSave\EQ2\EncounterRecorder\<Zone>\<Named>\<date and time>\`, one file per box.
2. A fight of several nameds is filed under the named a fight file of the zone is written for, or else the one with
   the lowest id: rename the folder if that is not the boss. A boss whose adds come first: add its name to the
   `named` list in the folder's `encounter.json`. A folder is found by its `encounter.json`, never by its name.
3. **Build pages** (or `ogre er pages [zone] [rebuild]`) makes the pages you read. Open the named's `report.html` in
   a browser: all its pulls together, its health over time, what landed on whom, what the game said.

**Build pages needs Node.js.** It is a free program the page script runs in. Install the LTS version from
[nodejs.org](https://nodejs.org), close the game and InnerSpace, start them again (they only see a program
installed before they started), then press **Build pages** again. Nothing else needs it: recording and uploading
work without it.

## 3. Working the fight out

1. Read the named's page first, then a pull's page for the detail.
2. Where the zone has a fight file, the page checks every condition of it against the pull: **seen**, **not seen**,
   **not from the game**, **not recorded**, **not judged**. "Not seen" is not proof the file is wrong: the mechanic
   may not have happened in that pull.
3. A new mechanic: find its det (its pair of icons and its name), the line the game says (and on which channel), or
   the actor that spawns, and the time. A fight file keys on exactly those.
4. What a recording does NOT hold yet: the Heroic Opportunity wheel, what a toon itself does with an item or a click
   on an object, and the bot's own choices (spots, timers, who is assigned what).

What a recording holds, row by row: [The recording format](recording-format.md).

**Hiding the lines every fight has.** A page can leave out the lines your group prints in every fight (your own
heals, procs, buffs). Run the page script once with `--standard` after a few nights of recording, in a command
window:

```bash
node "<your Scripts folder>/Ogre/EQ2/EncounterRecorder/builder/encounter-recorder-report.js" --standard
```

It writes `standard-lines.json` beside your recordings, made from your own fights only. A line seen in 4 zones or
more is then left out of every page, and the page says how many it left out.

## 4. Sharing it with your raid (the codex site)

1. You need your EQ2Codex API token (in OgreBot, the **Codex Inspect** or **Codex Toons** tab, **Setup API
   Token**), and a raid on the codex site that you own or are an accepted member of.
2. Tick **Upload each finished fight**, and choose the **Raid** with **Refresh** (the list of raids you may send to).
   Each box sends its own file a few seconds after its fight ends.
3. Only fights recorded since the recorder was switched on go by themselves; older recordings go only by **Upload
   now**. Trash
   pulls and folders whose name begins with `_` are never sent.
4. Only your raid's members can read what you send, on the raid's **Encounters** tab. Publishing a fight with every
   name taken out is a separate step on the site, approved by its admins.

## Commands

`ogre er help` lists them all in the console: `on`, `off`, `status`, `start`, `stop`, `mark <text>`, `pets`,
`npceffects`, `everydet`, `trash`, `onforwho`, `offforwho`, `pages [zone] [rebuild]`, `upload [on|off|now]`,
`raid <slug>|none`, `raids`. `ogre end er` stops everything and closes the window.
