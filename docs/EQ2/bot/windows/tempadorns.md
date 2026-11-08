<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../index.md).
</div>

# Temp Adornments

> **:bulb: In game - the ? button on this window says**
>
> Choose which temporary adornment goes on each gear piece and save it as a profile. Apply a profile here, on other toons, or with `ogre tempadorns <profile>`.
>
> **What you can do here**
>
> - **Pick a profile** on the left to edit it, or **+ New profile** to start an empty one.
> - **Type an adornment** next to a gear piece, or tick pieces and click an adornment under the table to set it on all of them. A blank piece is skipped.
> - **Save** stores the profile under its name. **Delete** removes it (click twice).
> - **Apply** runs the selected profile on this toon. Put `igw:Name`, a group or `all` in **to** to run it on those toons instead.
>
> **Good to know**
>
> - Apply always puts the adornment on, even on a piece that already has it with time left.
> - **Primary (two-handed)** is used instead of **Primary** when your primary weapon is a two-hander.
> - Make as many profiles as you like (for example one per fight), each under its own name.
> - Every toon on this PC shares the same profiles.

**Open it:** Type `ogre tempadorns`. If the window is already open, this does nothing. `ogre end tempadorns` (or the window's X) closes it. `ogre tempadorns <profile>` applies a saved profile without opening the window, and `ogre tempadorns list` prints your profiles.


## What it is for

A temporary adornment is a short-lived rune you put on a piece of gear. This window lets you say which one goes on which gear piece and save that as a profile, the way the classic bot's Temp Adorns window did. Applying a profile puts each listed adornment on its gear piece, one after another. You can apply it on this toon, on other toons (`igw:Name`, a group, `all`), from the console with `ogre tempadorns <profile>`, or from any box with `-TempAdorns <who> <profile>`. Three profiles come ready-made: CBOC, Pot and HP, the lists the old PoP button used. The first time the window opens it also copies in your profiles from the classic bot's Saved_Temp_Adorns.xml.

## Profiles

The list on the left is every profile you have saved. The number beside each name is how many gear pieces it sets.


| Control | What it does |
|---|---|
| **a profile name** | Opens that profile in the table to edit, and makes it the one Apply runs. |
| **+ New profile** | Clears the table and the name so you can build a new profile. |
| **Reload** | Reads the profiles file again, for after you have edited it by hand. |



## The gear table

One row per gear piece. Type the adornment's full name, exactly as the item is called in your bags. Leave a piece blank to skip it.


| Control | What it does |
|---|---|
| **Name** | The profile's name. One word: letters, digits, _ . and - (no spaces), up to 32 characters. It cannot be panel, end, list or apply, because `ogre tempadorns` uses those words itself. |
| **x** | Empties that gear piece (nothing goes on it). |
| **an adornment under the table** | Sets that adornment on every gear piece whose box is ticked. The list is every adornment your saved profiles use.<br>*Nothing happens if no box is ticked; the footer says so.* |
| **Save** | Saves the profile under its name. A profile with the same name (any capitals) is replaced. The footer says what was saved, or why it was not. |
| **Delete** | Deletes the profile. Click it twice: the first click turns it into 'Sure? click again'. |



## Apply

Runs the selected saved profile.


| Control | What it does |
|---|---|
| **Apply** | With the 'to' box empty, applies the profile on this toon. With a for-who in it (`igw:Name`, a group, `all`), sends `-TempAdorns <who> <profile>` so those toons apply it.<br>*Save first: Apply runs the profile as it is saved, not what is typed in the table.* |



## What the window shows

- The header shows your toon's name ('not in world' at character select).
- The footer shows what the last button did, or where the profiles are saved.

## Good to know

- Every toon on this PC shares the same profiles (OgreSave/EQ2/TempAdorns/profiles.json).
- Apply always puts the adornment on, even on a gear piece that already has it with time left.
- Primary (two-handed) is used instead of Primary when your primary weapon is a two-hander. To know that, Apply asks the game for your weapon's details once.
- Make as many profiles as you like, each under its own name (for example one per fight), and apply whichever one you need.
- A gear piece with nothing equipped, or an adornment that is not in your bags, is skipped with one line in the console.
- Applying waits its turn behind other queued bot work (it is one entry in the action queue).
- The ready-made CBOC, Pot and HP profiles are the old PoP button's lists. You can change or delete them; they are not put back.

