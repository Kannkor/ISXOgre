# No Ogre windows

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../index.md).
</div>

OgreBot loads and runs, but no Ogre windows appear in the game. If the InnerSpace console says **Windows is blocking EverQuest2.exe from starting other programs**, this page is the fix.

## What is wrong

Ogre's windows run in a small program of their own, `OgreUltralight.exe`, which the game starts. A Windows security setting called Exploit Protection has a rule on `EverQuest2.exe` that stops it starting any other program, so the windows never start.

You may not have set this rule yourself. Other software can add it.

## Turn the rule off

Close the game first.

1. Open **Windows Security**.
2. Open **App & browser control**, then **Exploit protection settings**.
3. Open the **Program settings** tab.
4. Find `EverQuest2.exe`. There can be more than one, one for each copy of the game. Do these steps for each one.
5. Choose **Edit**, then find **Do not allow child processes**. Turn off **Override system settings** for it, then choose **Apply**.
6. Start the game and load OgreBot.

Windows may show slightly different names on your version.

## If you cannot turn it off

On a work PC or a shared PC you may not be allowed to change this. Ogre can have the InnerSpace uplink start its windows instead of the game. In the InnerSpace console, type:

```
ogre ui uplinkstart on
```

Then restart the game. Use this only if you cannot remove the rule. To go back, type `ogre ui uplinkstart off` and restart the game. On its own, `ogre ui uplinkstart` shows whether this is on.

## Still no windows?

Send this file to Kannkor, from your InnerSpace folder:

```
x64\Extensions\ISXDK35\OgreUIRuntime\ISXOgreUIHost.log
```
