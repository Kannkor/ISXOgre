# No Ogre windows

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../index.md).
</div>

OgreBot loads and runs, but no Ogre windows appear in the game. Ogre's windows are drawn inside each game, unless you chose to have one separate program, `OgreUltralight.exe`, draw them for every game to save memory. When they cannot start, the InnerSpace console says why, and a window opens (at most once a day) with two choices: the steps on this page, or the other way of drawing them.

## Two ways of drawing Ogre's windows

- **Inside each game** (the default). Nothing extra runs.
- **In `OgreUltralight.exe`**, one program for every game on the PC. It uses about 150 MB less memory per game, but with many games running it can become the slow part. Tick **Draw Ogre windows in OgreUltralight.exe** in `ogre config` (Ogre tab), or type `ogre ui exe on` in the InnerSpace console. `ogre ui exe off`, or unticking it, goes back.

Either change takes effect when you restart the game, each box. Find what the console said below.

## "Windows Exploit Protection does not let EverQuest2.exe start other programs"

You chose `OgreUltralight.exe`, and a Windows security setting called Exploit Protection has a rule on `EverQuest2.exe` that stops it starting any other program. You may not have set this rule yourself. Other software can add it.

- **Draw the windows inside the game instead:** choose **Draw them in the game** in the window that opened, or type `ogre ui exe off`, then restart the game.
- **Or change the rule.** Close the game first.
  1. Open **Windows Security**.
  2. Open **App & browser control**, then **Exploit protection settings**.
  3. Open the **Program settings** tab.
  4. Find `EverQuest2.exe`. There can be more than one, one for each copy of the game. Do these steps for each one.
  5. Choose **Edit**, then find **Do not allow child processes**. Turn off **Override system settings** for it, then choose **Apply**.
  6. Start the game and load OgreBot.

  Windows may show slightly different names on your version.
- **Or let InnerSpace start it:** `ogre ui uplinkstart on` has the InnerSpace uplink start `OgreUltralight.exe` instead of the game. Restart the game after it; `ogre ui uplinkstart off` goes back.

## "Windows Smart App Control blocked OgreUltralight.exe" or "blocked Ogre's window files"

Smart App Control is a Windows 11 security setting that blocks programs and files that are not signed. Ogre's are not signed.

- **If it blocked `OgreUltralight.exe`:** draw the windows inside the game instead. Choose **Draw them in the game** in the window that opened, or type `ogre ui exe off`, then restart the game.
- **If it blocked Ogre's window files:** drawing them in `OgreUltralight.exe` will most likely be blocked too. Turning Smart App Control off is the fix: open **Windows Security**, then **App & browser control**, then **Smart App Control settings**, and choose **Off**. On some versions of Windows, Smart App Control cannot be turned back on without resetting Windows, so read what Windows says before you choose.

## "Windows would not load Ogre's window files into the game" or "did not start inside the game"

Try the other way of drawing them: choose **Use OgreUltralight.exe** in the window that opened, or type `ogre ui exe on`, then restart the game. If that does not help either, send the files below.

## Still no windows?

Send these files to Kannkor, from your InnerSpace folder:

```
x64\Extensions\ISXDK35\OgreUIRuntime\ISXOgreUIHost.log
x64\Extensions\ISXDK35\OgreUIRuntime\OgreUltralight\OgreUltralight.log
```
