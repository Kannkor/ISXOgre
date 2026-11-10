# Write your own zone files

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../index.md).
</div>

A **zone file** tells the Instance Controller (IC) how to run one instanced zone: where the group walks, which
nameds it kills, what it loots, and how it leaves. It is a JSON file. IC reads it from the top, one step at a
time, on the character that runs IC, and that character leads the group through it.

The zone files that ship with Ogre are written the same way, so the best way to learn is to open one beside this
page. The examples below are cut from `_01_Oogothl_Sprawl_VerBohten_Atoll.json` and `_05_Gerion_Dominion_of_Pain.json`,
both in `Scripts\Ogre\EQ2\IC\default\Rage of Cthurath\`.

> **No promises.** Use this at your own risk, and expect it to change. That said, Kannkor works hard to keep
> things backwards compatible.

## Quick start

1. Make the folder `Scripts\OgreSave\EQ2\IC\custom\` if it is not there. Folders inside it are fine; the IC window
   shows them as folders.
2. Copy a shipped zone file into it to start from, and give it a name of your own.
3. Edit it. Every file must say how it leaves the zone, with a `zoneOut` step (see [The way out](how-it-runs.md#the-way-out)). Then
   press **Reload** in the IC window. It prints `N zone(s) from M file(s) - X skipped, Y warning(s)`.
4. Pick **custom** in the IC window's root list. A file with a problem shows there in **red**, marked *not valid*:
   click it, and the bar under the list says what is wrong (see [Checking your file](checking.md#checking-your-file)).
5. When your zone shows normally, queue it and press **Run**.

## The pages

- [Where zone files go](where-they-go.md): the custom folder, your own folders in it, file names, and queueing a zone by name.
- [A zone file, start to finish](example.md): a whole file from a shipped zone, read top to bottom.
- [How a zone file runs](how-it-runs.md): the top of the file, how a run goes, steps, waiting, loops, the values you can use in text, and the way out.
- [The steps, one by one](steps.md): every step - path, named, loot, zoneOut, teleporter, hunt, the waits, trash, reward, groupQuery, progress and recover.
- [Other actions](other-actions.md): the actions a step can run besides moving.
- [Run your own fight files](fight-files.md): where your own fight (encounter) files go, how one is picked, and starting a setup from a button or a zone file.
- [Check your file](checking.md): how to find what is wrong with a file, and a checklist before you share it.
