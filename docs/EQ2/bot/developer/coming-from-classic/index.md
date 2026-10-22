# Coming from Classic

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../index.md).
</div>

These pages are for people who wrote their own Classic scripts, raid modules, instance files or console lines, and want them to work with the new bot. Look a name up on the page where Classic's own developer docs described it.

> **:no_entry: Read this first: an old spelling does not give an error - it silently does nothing**
>
> The new bot does not keep Classic's names as aliases. When a script calls a name that no longer
> exists, LavishScript does **not** stop with an error: a method call does nothing, and a member read
> gives `NULL`. Nothing is written to any log. A console line with the wrong arguments still runs -
> with the arguments in the wrong places. So a script that "still runs" after the switch may be doing
> far less than you think.
>
> That is why every row on these pages says **what the old spelling does today** before it says what
> to write instead.

## The four changes that touch almost everything

1. **The for-who comes first.** Every new call that acts on some sessions takes the for-who as its
   first argument: `OgreBotAPI.CampSpot:SetLoc[igw:${Me.Name},10,20,30]`. Old calls that had no for-who
   (most `Ogre_CampSpot:` calls acted only on the session that ran them) now need one - use `all`. A script's
   own call only ever runs on the session running it, so `all` there means "this session", exactly as
   before. A name / `igw:${Me.Name}` works as before when you want to narrow it.
2. **Calls live in groups.** The flat `OgreBotAPI:Xxx` list became groups: `OgreBotAPI.CampSpot`,
   `OgreBotAPI.Movement`, `OgreBotAPI.Cures`, ... The old flat names were removed, not kept as aliases.
3. **Ability and item names are fine.** Pass the bot's calls a name or an id, whichever you have - the
   bot looks names up in its own ability export, not by asking the game server. What to avoid in your own
   code is the game's name lookup (`${Me.Ability["name"]}`, `.ToAbilityInfo`): that one asks the server and
   can come back empty.
4. **Many scripts became data files.** Fights (raid modules) and instance files are written as JSON
   now, and the bot runs them itself. A helper call from an instance file often has no script
   replacement because the step is a line in the instance's JSON file instead.

## What the "What changed" column means

| | Means | What you do |
|---|---|---|
| ✅ Works as is | the same spelling works | nothing |
| ➡️ Moved | same name, now inside a group | write the new call |
| ✏️ Renamed | new name, same job, same arguments | write the new call |
| ⚠️ Arguments changed | the arguments are different (usually a for-who added) | write the new call **and** fix the arguments |
| ⚠️ Argument order changed | same arguments, new order | reorder them |
| ➡️ Lives somewhere else | the job is done somewhere else (a window, an `ogre` command, another object) | use that instead |
| 📄 In a data file now | the job is a line in a fight or instance JSON file | move it to the data file |
| ⛔ Not ported yet | the new bot has nothing for it yet | leave it out for now - and tell us you need it |
| ⛔ Exists, does nothing yet | the new name is there but does nothing | same as not ported |
| ⛔ Removed | taken out on purpose | leave it out |
| ❔ Not checked yet | nobody has compared this name with the new bot yet | ask before relying on it |

## The pages

- [Camp spot](campspot.md) - Ogre_CampSpot, the movement locks, the camp-spot calls and commands, the jump helper
- [Console commands](console.md) - every OgreConsole command: what changed, and the ones that work as typed
- [OgreBotAPI](ogrebotapi.md) - every flat OgreBotAPI call, by the group it lives in now
- [Ask query system](ask.md) - OgreBotAPI.Ask and the Ask calls
- [Preferred group members](preferred.md) - the ...Preferred group and raid calls
- [Detrimentals](detrimentals.md) - the ISXOgre detrimental members and events, and AskDetrimentals
- [ISXOgre (old extension)](isxogre.md) - everything else on the old ISXOgre extension
- [OgreEvents](events.md) - which Classic events still fire
- [OgreCraft](ogrecraft.md) - OgreCraftAPI and the crafting bot object
- [Instance files](instance.md) - the instance-file helpers - mostly data-file lines now
- [Other Classic objects](objects.md) - GetInfoOb, ClassInfo, TabConfig, Ob_AutoTarget and the rest
- [OgreBot option ids](options.md) - the option ids buttons and scripts set, that the new bot does not have

## Everything at a glance

Every Classic name these pages cover so far, by what happened to it:

| What happened | Names |
|---|---|
| ⚠️ Arguments changed | 201 |
| ⚠️ Argument order changed | 20 |
| ✏️ Renamed | 502 |
| ➡️ Moved | 178 |
| ➡️ Lives somewhere else | 272 |
| 📄 In a data file now | 210 |
| ⛔ Exists, does nothing yet | 45 |
| ⛔ Not ported yet | 328 |
| ⛔ Removed | 203 |
| ✅ Works as is | 492 |
| **Total** | **2451** |

Can't find a name? Use the search box at the top - every old name is on one of these pages.
