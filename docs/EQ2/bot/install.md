# Installing and first start

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../index.md).
</div>

This page takes you from nothing to a running bot: download one file, sign in, and let the bot fetch the rest. It
takes a few minutes. After that, the bot keeps itself up to date every time it loads.

## Before you start

- **InnerSpace** and **ISXEQ2**, installed and working. InnerSpace must run as 64-bit, which is its default. You do
  not load ISXEQ2 yourself: the bot loads it.
- **Your OgreBot username and password.** They are the same as for OgreBot Classic. You got them in the
  **Welcome to ISXOgre** email when you subscribed. No subscription yet? See
  [How to Subscribe](../about/pricing.md#how-to-subscribe).
- **Your PC's clock set right.** Sign-in is refused when the clock is off by more than 10 minutes.
- **InnerSpace in a folder Windows lets you write to.** The bot saves its settings and downloads inside the
  InnerSpace folder (the folder InnerSpace itself is in). A folder under `Program Files` can stop it from saving.
- **About 15 GB free** on that drive. The maps the bot downloads after its first start are about 14 GB.

## Step 1: Start one game session

Close every EverQuest 2 session first. Then start **one**, with an InnerSpace profile that loads nothing by itself,
such as InnerSpace's own **EverQuest 2 Client** profile.

> **:bulb: Why only one?**
>
> When the bot updates itself it reloads in every session on the PC. A profile that loads OgreBot Classic by itself
> also gets in the way of the first install.

## Step 2: Download ISXOgreX

Open the InnerSpace console (the **`~`** key) and paste this line:

```
httpget -file "${LavishScript.HomeDirectory}/x64/Extensions/ISXDK35/ISXOgreX.dll" https://cluster1.ogregaming.com/eq2/download_isxogrex.php
```

Wait until the console says it succeeded.

> **:bulb: Or download it in your browser**
>
> [Download ISXOgreX.dll](https://cluster1.ogregaming.com/eq2/download_isxogrex.php) and save it into your
> InnerSpace folder, in `x64\Extensions\ISXDK35\`. The file must be named exactly `ISXOgreX.dll`.

This one file is all you download by hand. It fetches everything else itself.

## Step 3: Load it and sign in

In the console, type:

```
ext isxogrex
```

A window called **OgreX - Login** opens. Enter your OgreBot **Username** and **Password** and click **Login**. They
are in the **Welcome to ISXOgre** email you got when you subscribed, and they are the same as for OgreBot Classic.
Copy and paste them: they are case-sensitive. They are saved on this PC, so you only do this once. The console then says `authenticated`.

If sign-in fails, the console says why: see [If something goes wrong](#if-something-goes-wrong).

## Step 4: The first download

The bot now downloads the rest of itself: about 1,500 files, a little over 100 MB. The console counts them off as
they arrive: first how many files there are to get, then a line every few files saying how far it has got, for
example `patch: downloading 300 of 1544`. You do not have to watch it, and you can close the console while it works:
the welcome window below opens by itself when everything is in. When the new files are in, the extension reloads itself once. That is
normal. It signs in again by itself, and then the welcome window opens (step 5).

**The maps download afterwards.** The maps the bot uses to move and fly around zones are large, about 14 GB in all.
They download in the background after the bot has loaded, and the console says so:
`navmesh: downloading ... in the background - the bot is ready to use`. You can play while they download.

## Step 5: The welcome tour

When the download is done, the **Welcome to OgreBot** window opens and plays a short animation of an ogre smashing
its way in. It ends on **Start the tour**. Click it for a short tour of how every Ogre window works: resizing, the
right-click menu on the title bar, saving a window's place, and the settings. Click **Got it** at the end. You can
skip both: press and hold **Hold to skip** for 3 seconds during the animation, or close the tour.

Right after the tour, the **Migration Assistant** opens for a moment and closes itself. It adds an InnerSpace profile
called **Everquest 2 ISXOgreX** that loads the bot by itself next time. If you used OgreBot Classic on this PC, it also
copies your Classic settings into the new bot: see [Migration Assistant](windows/migrate.md).

## Step 6: Log in and open the bot

Log your character in to the world the usual way. Then, in the InnerSpace console, type:

```
ogre
```

OgreBot starts, and its small window appears: see [OgreBot's small window](windows/ogremini.md). Click
**Show Main** for the big window.

**The first time on each character**, the bot asks to export your abilities: a box says there is no ability export and
offers **Run export now**. Click it. The bot needs the export to know what your character can cast, and it stays
paused until the export is done.

## Step 7: Save your characters

Open the **EQ2Chars** tab in the big OgreBot window and add each of your characters, with its game account and
password if you want the bot to log it in for you. See [EQ2Chars](ogrebot/eq2chars.md).

From then on, `ogre <name>` typed in the InnerSpace console logs that character in from character select and starts
the bot, for example `ogre Brutus`. Until a character is on the list, `ogre <name>` only says it is not a known character.

## Next time

Start your session with the **Everquest 2 ISXOgreX** profile. The bot loads, signs in and updates by itself. Then
type `ogre <name>` at character select, or `ogre` once you are in the world.

## If something goes wrong

| The console says | What to do |
|---|---|
| `login failed - invalid credentials. Re-enter them in the login box.` | Your username or password is wrong. Enter them again in the login window: copy and paste them from the **Welcome to ISXOgre** email. They are case-sensitive. |
| `your OgreBot subscription is not active - adapter not loaded.` | Your account has no active OgreBot subscription. To get one or renew it, see [How to Subscribe](../about/pricing.md#how-to-subscribe). |
| `login failed - ... Sync this machine's clock ...` | Set your PC's clock right (Windows Settings, Time & language, **Sync now**), then type `ext isxogrex` again. |
| `login failed - ... too many machines or IPs for your subscription.` | Your subscription has hit its PC/IP limit: it is in use on more PCs or internet addresses than it allows. Talk to Kannkor on [Discord](https://discord.gg/hnSTRQr). |
| Step 2's download line does not succeed | Download the file in your browser instead (the box under step 2) and save it in your InnerSpace folder as `x64\Extensions\ISXDK35\ISXOgreX.dll`. |
| `ext isxogrex` opens no login window | Check that the file is in your InnerSpace folder at `x64\Extensions\ISXDK35\ISXOgreX.dll`, named exactly that, and that InnerSpace runs as 64-bit. Then type `ext isxogrex` again. |
| `cannot reach the OgreGaming server. Retrying in ...` | The bot tries again by itself. If it keeps failing, check your internet connection and firewall. |
| The game closed during the first download | Start a session again and type `ext isxogrex`. The bot checks its files every time it loads and downloads what is missing. The maps pick up where they stopped. |
| No Ogre windows appear | See [No Ogre windows](no-ogre-windows.md). |

## Next steps

- [The basics](basics.md): the window buttons every Ogre window shares.
- [OgreBot](ogrebot/index.md): the main window, then its [Setup](ogrebot/setup.md) and
  [Cast Stack](ogrebot/cast-stack.md) tabs.
