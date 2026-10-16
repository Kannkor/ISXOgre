# Auto-Login

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../index.md).
</div>

> **:bulb: In game - the ? button on this window says**
>
> Builds auto-login profiles: which character goes into which session. Start makes your sessions match the profile and loads OgreBot on each character once it is in the world.
>
> **What you can do here**
>
> - **Profiles** - click one to open it. **+ New** starts a blank one; **Import** copies your old OgreBot profiles.
> - **Character rows** - pick the PC (ThisUplink), the session (is1, is2, or any) and the character.
> - **Settings** - the game to launch and the pauses between launches and logins (in tenths of a second).
> - **Save** the profile, **Delete** the one selected in the list, or make a **Desktop shortcut** that runs it.
> - **Start** runs the selected saved profile. Tick **Dry run** to only list what it would do.
>
> **Good to know**
>
> - Saving over an existing profile needs **Overwrite** ticked.
> - Start runs the saved profile, so Save first.
> - No passwords are stored; characters must be in your saved account list.

**Open it:** Type `ogre autologin`. `ogre end autologin` closes it.

[![Auto-Login](../assets/autologin/window.png)](../assets/autologin/window.png "Click for full size")

## What it is for

Auto-Login builds **profiles**: a named list of which character goes into which InnerSpace session. Press **Start** and InnerSpace itself (the uplink, not the game window) makes your sessions match the profile: characters already in the right place are left alone, a wrong character is camped out, missing sessions are launched, and each character is logged in with a pause between logins. Once a character is in the world, OgreBot is loaded for it. Profiles hold no account names or passwords; those come from your saved account list when the profile runs, so a profile is safe to share.

## Profiles list

Your saved profiles, in name order. The number after a name is how many characters it has. A red name with a warning sign is a profile file that could not be read.

[![Profiles list](../assets/autologin/list.png)](../assets/autologin/list.png "Click for full size")

| Control | What it does | Default |
|---|---|---|
| **Click a profile** | Opens that profile on the right so you can check it, change it, start it or delete it.<br>*Clicking a red (broken) profile only shows why it could not be read, in the log at the bottom.* |  |
| **+ New** | Clears the right side for a brand new profile: no name, one character row (ThisUplink, any), and the default settings.<br>*Nothing is saved until you click Save.* |  |
| **Import** | Copies your auto-login profiles from the old OgreBot into this window. It reads the old bot's AutoLoginProfiles.xml and AutoLoginSettings.xml (in Scripts\EQ2OgreCommon\OgreAutoLogin) and writes one new profile per old one. The log shows how many were written, skipped or failed.<br>*The old bot's timing settings are copied into every imported profile. Characters not in your saved account list are counted as warnings but still imported.* |  |
| **Overwrite on import** | When ticked, Import replaces a profile you already have with the same name. When not ticked, those are skipped and your existing profile is kept. | off |

## Profile name

[![Profile name](../assets/autologin/name.png)](../assets/autologin/name.png "Click for full size")

| Control | What it does | Default |
|---|---|---|
| **Profile name** | The name of the profile. Save uses it. The file on disk is named after it, with anything that is not a letter or number turned into an underscore.<br>*Spaces are fine. Renaming a saved profile and clicking Save moves it to the new name.* | empty |

## Character assignments

One row per character. Each field is pick-or-type: click it for a list, or type anything. Typing narrows the list.

[![Character assignments](../assets/autologin/rows.png)](../assets/autologin/rows.png "Click for full size")

| Control | What it does | Default |
|---|---|---|
| **Uplink** | Which PC this character belongs to. ThisUplink means "whichever PC runs the profile". Otherwise type that PC's InnerSpace uplink name. A run only handles rows for its own PC; other rows are skipped.<br>*The list offers ThisUplink plus any PC names used in your other profiles.* | ThisUplink |
| **Session** | Which InnerSpace session the character must be in: is1, is2 and so on. "any" means any session is fine: if the character is already in the world somewhere it is left alone, otherwise a free session is used or a new one is launched.<br>*The list offers any and is1 to is24. Left empty, it saves as any.* | any |
| **Character** | The character to log in. The list shows the characters in your saved account list.<br>*A character that is not in your saved account list gets a warning when the profile runs, because its account cannot be looked up.* | empty |
| **x (remove row)** | Removes that character row. If it was the last row, a fresh empty row takes its place.<br>*Not saved until you click Save.* |  |
| **+ Add row** | Adds another character row (Uplink ThisUplink, Session any, Character empty). |  |

## Settings

Times are in tenths of a second: 150 means 15 seconds. The editor scrolls; these are below the character rows.

[![Settings](../assets/autologin/settings.png)](../assets/autologin/settings.png "Click for full size")

| Control | What it does | Default |
|---|---|---|
| **Game** | The InnerSpace game entry used when a new session has to be launched. The list comes from the games set up in InnerSpace.<br>*Left empty, it saves as Everquest 2.* | Everquest 2 |
| **Game profile** | The InnerSpace game profile used when a new session has to be launched. The list shows the profiles of the game chosen above. | everquest 2 default profile |
| **Wait after load** | After new sessions are launched, how long to wait for them to load before logging anyone in. Only used when a session had to be launched. | 150 (15 seconds) |
| **Wait between launches** | The pause after each new session is launched, before the next one. | 50 (5 seconds) |
| **Login stagger - base** | The pause between one character's login and the next, so the server is not hit with every login at once. | 300 (30 seconds) |
| **Login stagger - random** | A random extra pause, up to this much, added to the base pause for each login. 0 turns the random part off. | 150 (up to 15 seconds) |

## Save, Delete, Shortcut and Start

At the opening window size these buttons are below the fold: scroll the right side down to reach Start.

[![Save, Delete, Shortcut and Start](../assets/autologin/actions.png)](../assets/autologin/actions.png "Click for full size")

| Control | What it does | Default |
|---|---|---|
| **Overwrite** | Must be ticked to save over a profile that is already saved. Without it, Save refuses and says a profile with that name already exists.<br>*This includes saving changes to the profile you just opened. It is not remembered: it is off each time the window opens.* | off |
| **Save** | Saves the profile. The log says whether it worked, and the list on the left updates.<br>*A profile needs a name. A row with no character is dropped when saving; a blank Uplink saves as ThisUplink and a blank Session as any. Settings this window does not show (such as loginOnly or sessionAppearMaxDs, set by hand in the file) are kept.* |  |
| **Delete** | Asks for confirmation, then deletes the profile you selected in the list.<br>*It deletes the selected saved profile, even if you have typed a different name in the box. A new profile that was never saved cannot be deleted.* |  |
| **Delete (in the confirm box)** | Deletes the profile file and clears the right side to a new blank profile. This cannot be undone. |  |
| **Cancel (in the confirm box)** | Closes the confirm box without deleting anything. |  |
| **Desktop shortcut** | Puts a shortcut on your Windows desktop that runs this saved profile through InnerSpace, the same as pressing Start. The log shows where it was made.<br>*Save the profile first. A shortcut with the same name is replaced; if something else already has that name, a numbered copy like "Raid_Night (1)" is made instead.* |  |
| **Dry run** | When ticked, Start only works out and lists what it would do (who stays, who gets camped, which sessions it would launch, who it would log in). Nothing is actually done.<br>*Off means Start really does it. Tick it the first time you try a new profile.* | off |
| **Start** | Runs the selected profile, as it is saved, in InnerSpace. Characters already where they belong are left alone; a wrong character in a session is camped first; missing sessions are launched; then each character logs in, with the stagger pause between logins. Each character gets OgreBot loaded as soon as it is in the world. Progress appears in the log below as it happens.<br>*Start runs the profile as last SAVED, not what is on screen. Click Save first if you changed anything, or if the profile is new.* |  |

## Window

[![Window](../assets/autologin/status.png)](../assets/autologin/status.png "Click for full size")

| Control | What it does |
|---|---|
| **Title bar close (X)** | Closes the window. A run that has already started keeps going in InnerSpace.<br>*Unsaved changes are lost.* |

## What the window shows

- Profiles (left): every saved profile, in name order. The number in brackets is how many characters it has. Green outline = the one open on the right. Red with a warning sign = a profile file that could not be read.
- The note under the name is a reminder that profiles hold no usernames or passwords.
- The log (bottom): green lines are things that worked, red lines are problems. During a Start it shows the run as it happens, between "run output" and "run complete" lines.
- The log stops following a run if nothing new appears for 90 seconds, or after 10 minutes.

## Good to know

- Saving changes to an existing profile needs Overwrite ticked, even if it is the profile you just opened.
- Start runs the SAVED profile. Save first if you changed anything.
- A run only handles rows for the PC it runs on (ThisUplink rows and rows naming this PC). Rows for another PC are skipped; to run them, copy the profile to that PC and start it there.
- Profiles are saved as files in Scripts\OgreSave\EQ2\AutoLogin\Profiles. You can copy them to another PC; they hold no passwords.
- Characters must be in your saved account list so their account can be found when the profile runs.
- Opening the window again while it is open does nothing, so the profile you are editing stays.

## Scrolled down

![The settings and the Start button](../assets/autologin/window-lower.png)

The right side scrolls. At the size the window opens at, **Start** is below the fold.

## Pick-or-type lists

![Character list](../assets/autologin/dropdown.png)

![Session list](../assets/autologin/dropdown-session.png)

Click a field for its list, or type: typing narrows the list, and you may type a value that is not in it.

## Deleting

![Confirm delete](../assets/autologin/delete-confirm.png)

## First open

![No profiles yet](../assets/autologin/empty.png)

With nothing saved yet, build a profile on the right and click **Save**, or click **Import** to bring over the profiles from the old OgreBot.

