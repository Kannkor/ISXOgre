# 2026 March 24th Patch - EverQuest2.exe Mismatch Fix

## Are you getting this error?

**"The version of ISXEQ2 you have does not match the version of EverQuest 2 that you are running."**

Then you're in the right place.

## What happened?

On **Tuesday, March 24th**, EverQuest 2 was patched, requiring everyone to update.
Then on **Wednesday, March 25th**, there was another patch that was **NOT** required.

ISXEQ2 works for the one on Tuesday, **NOT** the one on Wednesday.

If you run the EQ2 launchpad, it will patch the file and you will have a mismatch.

**Good news** - there is a way to fix it.

---

## Step 1: Find your EverQuest 2 install directory

Do you know where your EverQuest 2 is installed? Let's pretend you don't, because if you're wrong, none of this will work.

When you get the mismatch message, in the console type:

```
ISXOgre:DebugInfo
```

It will output a whole bunch of information. The thing you are looking for looks like this:

```
Your executable is: C:/Sony/EverQuest II/EverQuest2.exe
```

It will specifically start with **"Your executable"** and end with **"EverQuest2.exe"**. That is the path to your EverQuest 2 directory. Copy/paste it into notepad, or open explorer to that location.

---

## Step 2: STOP - Do NOT run the EQ2 launchpad

!!! warning "This is very important"
    At this time, you are **NOT** allowed to run the EverQuest 2 launchpad (their patcher) again. If you do run it, it will overwrite the file and give you a mismatch, and you will have to start this entire process over again.

Make sure **all** EverQuest 2 is completely closed. It doesn't matter if it is with or without InnerSpace, etc. Close them all down. If you're not sure, restart your computer.

---

## Step 3: Download and replace EverQuest2.exe

!!! note "A quick warning"
    Generally speaking, you should never download .EXE files, .DLL files (and a bunch of other types of files) because that's how viruses are generally shared. Since you're already using Ogre, which is a .DLL file, that means you should already trust me. That is why I am providing the file directly. You should never download these kinds of files from anyone, unless you have absolute trust in them.

**[Download EverQuest2.exe](EverQuest2.exe)**

Save it to your EverQuest 2 directory (the one we got/saved earlier, in this example: `C:/Sony/EverQuest II/`). Make sure it saves as **EXACTLY** `EverQuest2.exe`. Make sure it doesn't try to save as `EverQuest2 (1).exe` or something similar.

---

## Troubleshooting

### I got a permission denied error!

- If you get a pop up from **UAC** (User Account Control) asking if you want to continue/give access, give it access to copy it.
- If it simply tells you "no", it means you have some Windows options locked down. You can try to save it to your desktop, then from your desktop, move/copy it into the correct directory (again, in our example, it is `C:/Sony/EverQuest II/`).
- If you have an **anti-virus**, it may not allow you to download .exe files. If this is the case, you will have to tell it you are allowed to. (It shouldn't give you a false negative about a virus, it just may not allow .exe files).
- Much like the above, some **web browsers** won't allow you to download .exe files without approving of them first.

If you failed to get it copied to the correct location, it will not work. Go back and try again, or copy/paste your error and hope someone can assist.

---

## Step 4: Launch EverQuest 2

If you got it copied over, excellent! But first, one important reminder...

!!! danger "Do NOT run the EQ2 launchpad"
    **IF YOU RUN the EverQuest 2 launchpad (the patcher), you will overwrite this file**, and get a mismatch, having to start this entire process over again. Don't do that.

Go ahead and load an EverQuest 2 session via InnerSpace/ISBoxer, however you normally do. It should work.

---

## Additional Notes

- If you play on a server (e.g. PvP) that **requires** you to use the launchpad, I do not have any recommendations for you at this time. You may have to wait until ISXEQ2 is updated for the latest EverQuest2.exe. The next patch is scheduled for **April 14th**.
- To be clear, I am the Ogre guy. ISXEQ2 is run by Amadeus.
