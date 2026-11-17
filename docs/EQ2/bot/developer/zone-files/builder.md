<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../index.md).
</div>

# Build one in the Content Builder

The **Content Builder** is a window that draws a zone file as boxes, one per step. You add steps from a list, fill in
their options in a form, and the game checks the file after every change. You do not have to write JSON, and you can
still see and edit the JSON whenever you want to.

It does the same for fight files, on its **Encounters** tab: see [Fight files](#fight-files-the-encounters-tab) below.

Type `ogre contentbuilder` to open it. It works at the login screen too; only **Run** and the **here** buttons need a
character in the world.

> **No promises.** Use this at your own risk, and expect it to change.

## A first file, start to finish

This builds a small file you can run in your guild hall: walk to a spot, say so, wait for any fight to end, loot,
say you are done.

1. Press **New**. The card on the left of the graph is the top of the file, and it is selected: type the zone's name
   in **zone** on the right, exactly as the game shows it. The file already ends with a **Leave the zone** step,
   because every zone file must say how it leaves.
2. Click the **Walk a path** chip at the bottom. A box appears, outlined red: a walk needs at least one spot. Stand
   where the group should walk to and press **+ where I stand**. The red outline goes away.
3. Click **Show a message** and type the `message`.
4. Click **Wait for the fight to end**, then **Loot**. Loot starts as `chest`; the `op` dropdown has `shinies` and
   `corpses` too.
5. Drag **Show a message** from the bottom onto the **+** under the Loot box, and type its message.
6. The verdict in the bar should say **loads clean**. Press **Save** and give the file a name.
7. Press **Run**. The Instance Controller runs the file where your character stands, and its window and the console
   show each step.

For a file that only runs in place, like this one, set the last step's `op` to `none`: it then stays in the zone
instead of looking for an exit.

## The window

| Part | What it is |
|---|---|
| The tabs at the top left | **Instances** for zone files, **Encounters** for fight files. Each keeps its own file. |
| The bar | The file's name, **New**, **Open**, **Save**, **Save as**, **Undo**, **Redo**, **Run**, **Add to IC list**, and the verdict. |
| The lists | **Before**, **Steps**, **After**, **On a wipe**, **Zone given up**: the file's `enter`, `steps`, `exit`, `onWipe` and `afterWipe`. Click one to see its boxes. Most files only use **Steps**. |
| The graph | The boxes of the list you picked, top to bottom, then the next column. Steps whose names start the same (`named1`, `named1.walk`, `named1.chest`) share a column. **Fit** and **All** zoom out; click the percent for normal size. |
| The pane on the right | **Box**: the selected box's options. **Box JSON** and **File JSON**: the same as text. **Problems**: what the game's check found. |
| The chips at the bottom | The steps you can add, grouped. **Every step...** opens the full list, with a search. |

### The colours

| Colour | Kind | Examples |
|---|---|---|
| Green | Moves the group | Walk a path, Use a teleporter, Leave the zone |
| Blue | Does something | Kill a named, Loot, Show a message |
| Yellow | Waits | Wait, Wait for the fight to end |
| Teal | Loops | Repeat, For each |
| Purple | Keeps a value | Ask the group, Mark a step done, Set a variable |
| Red | Stops and wipes | Recover from a wipe |
| Grey | A step this window does not know | It stays in the file as it is. You can move or delete it, not edit it. |

## Adding, moving and changing steps

- **Add**: click a chip (the step goes after the selected box, or at the end), drag a chip onto a **+**, or click a
  **+** to pick from the full list.
- **Move**: drag a box onto a **+**, or select it and use the arrows.
- **Duplicate** and **Delete** are on the right when a box is selected. **Undo** takes back any change, one at a time.
- **Loops**: a **Repeat** or **For each** box holds steps of its own. Drop a chip or a box on a **+** inside it.

## The options of a step

Click a box. The form on the right is made from the same list of steps and options the game itself uses, so it
always shows every option the step has.

- A red star marks an option the step cannot do without.
- **More options** holds the rest. Each shows what it does and its default. An option you leave alone is not written
  to the file.
- A dropdown lists the words an option takes. Yes / no options are two buttons.
- A spot has three boxes, x, y and z. **here** fills them from where your character stands; **+ where I stand** adds
  a spot to a list of spots.
- The **x** beside an option takes it out of the file again, back to its default.
- Conditions (a step's `when`, a wait) are a list: press **+ a condition**, pick one, and fill in its settings. Every
  condition in the list must be true. **Not**, **Any of** and **All of** hold conditions of their own.

What each step and option does is on [The steps, one by one](steps.md) and [Other actions](other-actions.md).

## The game checks it

After every change the whole file goes to the game, which checks it by the same rules it uses when it loads a zone
file. Nothing is saved to do that.

- The verdict in the bar says **loads clean**, **loads** with a number of notes, or how many problems there are.
- A box with a problem is outlined red. Hover it to read the problem.
- The **Problems** tab lists everything, in the game's own words. Click one to go to its box.

The messages are the ones on [Check your file](checking.md).

## Saving and running

- **Save** writes to your own folder, `Scripts\OgreSave\EQ2\IC\custom\`. You can put a folder in front of the name
  (`mine/My_Zone.json`).
- A zone file that ships with Ogre can be opened, but it is never changed. **Save** on one asks for a name and keeps
  your own copy.
- A file with problems can still be saved, so you can stop and come back. It shows red in the Instance Controller
  and cannot run until it is fixed.
- **Run** puts the saved file on the Instance Controller's list, starts the list at its row and ticks **Stop after this zone**, so only this file runs. It runs as any zone on your list does: your Instance Controller options apply, the after-zone ones too.
- **Add to IC list** adds the saved file to the Instance Controller's list, the same as its **Add** button.
- Changes you have not saved are kept if the window closes or the UI reloads, and are offered back the next time
  the window opens.

## Fight files: the Encounters tab

The **Encounters** tab at the top left is the same window for the other kind of file: a fight file, which says what the
group does in one fight. Each tab keeps its own file, so you can switch back and forth.

A fight file has six lists, shown as tabs above the graph:

| Tab | What it holds |
|---|---|
| **Setup** | Steps that run once when the fight starts. |
| **When something happens** | Rules set off by something: a line of text, an announcement, a mob appearing, a detriment landing, a cast ending. |
| **All the time** | Rules checked over and over while the fight lasts. |
| **Teardown** | Steps that run once when the fight is over. |
| **On a kill** | Steps that run when a mob dies, one column per mob. |
| **Routines** | Named lists of steps that a **Run a routine** step runs. |

### Rules

A rule is drawn as a column: its head on top, a yellow **Only when** box with its conditions, then its steps.

- Click the **head** for the rule's settings. Under **When something happens**, **on** says what sets it off and **match**
  shows the fields for that kind: a `needle` for text, a `name` for a mob, `main` and `back` for a detriment.
- Click the **yellow box** for its conditions. Press **+ a condition**, pick one from the list, and fill in its settings.
  Every condition in the list must be true. **Not**, **Any of** and **All of** hold conditions of their own.
- With a rule selected, a chip you click goes to the end of that rule's steps. You can also drag a chip onto any **+**.

### Quick starts

Three buttons beside the rules make a common rule from a few questions. What they make is an ordinary rule you can change.

| Quick start | What it makes |
|---|---|
| **Run out on a detriment** | While a character has the detriment it stands on a spot you choose, and comes back when the detriment is gone. |
| **When I get a detriment…** | A rule set off by a detriment: once when it lands, or again and again while it lasts. |
| **From what happened in a fight…** | A rule set off by a line of text, an announcement, a mob appearing or a cast ending. |

### The top of the file

The card on the left holds **named**, the mob or mobs the fight is for, and the zone. A new fight starts with one empty
name: target the mob and press **target**, or type it. **+ a mob** and **+ my target** add another. The fight starts when
one of the named is engaged. Click the card, and **named** and **zone** are the first two rows on the right.

### Saving a fight

Your fight files go in `Scripts\OgreSave\EQ2\Encounters\custom`. The game reads its fight files again after each save.

To change a fight that ships with Ogre, open it and save it under the same name. Your copy then replaces the shipped fight
for you: it is saved with `noMerge`, so what you see in the window is the whole fight. Under another name the game sees
two files for the same mob in the same zone and skips yours; the window tells you so.

A file with no `named`, saved under a shipped fight's name, holds only what it changes. The game lays it over the shipped
fight: what you leave out comes from that fight, and a list you write replaces the shipped list whole. The card then says
**Laid over the shipped fight**. Type a name and it becomes a whole fight of its own.
[Run your own fight files](fight-files.md) has more on how your file and the shipped one meet.

**Set up now** asks the game to run the saved fight's setup, as the Set Up For button does. The named must be here.

### What the game says about a fight file

- A problem with the file itself (no `named`, a mob another file already has) stops it from loading.
- A broken rule or step does not: the game keeps the file and that part does not do what it says. The bar reads
  "loads, but … broken".
- A yellow note is not an error. It often points at a mistake all the same, such as an option nothing reads.

## Checking a file from the console or a script

`ogre ic validate custom My_Zone.json` checks a zone file on disk by the same rules and prints each problem; `ogre encounter validate custom "My Zone/My Mob.json"` does the same for a fight file. It
changes nothing.

```
ogre ic validate custom My_Zone.json
```

A script calls `ISXOgreEQ2.IC:Validate[custom,"My_Zone.json"]` and reads the answer from `${ISXOgreEQ2.IC.Validation}`.
The answer is JSON: `ok` (true when the file would load), `errors` and `warnings` (how many), and `issues`, one for
each line the console printed.

## The schema

The list of steps and options the window draws from is a file that ships with Ogre:
`Scripts\Ogre\EQ2\IC\ic.schema.json`. It is a JSON Schema, so an editor that understands those can use it to check
a zone file and to complete as you type. Ogre makes that file from the game's own tables; do not edit it.

Fight files have one too: `Scripts\Ogre\EQ2\Encounters\fight.schema.json`.
