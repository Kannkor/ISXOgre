# Converting your scripts

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../index.md).
</div>

This page is for moving your own OgreBot Classic scripts over to the new OgreBot: side scripts, helper
scripts, console lines and MCP buttons. It has a small tool that checks a script, fixes what it safely
can, and tells you what is left. The second half is a step-by-step procedure you can hand to Claude
(or do yourself).

> **:no_entry: An old spelling does not give an error - it silently does nothing**
>
> When a script calls a Classic name that no longer exists, LavishScript does not stop: a method call
> does nothing, and a member read gives `NULL`. Nothing is written to any log. A console line with its
> arguments in the wrong order still runs, with the wrong values. So "it loads without errors" proves
> nothing. A script is converted when the tool's **sweep** says `CLEAN`.

## Download

Two files. Put them **in the same folder** - the tool looks for the map next to itself.

- [ogre_convert.py](converter/ogre_convert.py) - the tool (open source)
- [conversion-map.json](converter/conversion-map.json) - the map: one row for every Classic name, saying
  what it does now and what to write instead

You need **Python 3** and nothing else. The tool does not read any bot files and does not talk to the
game, so it runs on any PC. To use a map somewhere else, add `--map <path to conversion-map.json>`.

> **:bulb: Download them again after an update**
>
> The map is generated from the bot itself, so a newer bot can have names an older copy does not know.
> Get both files fresh before you start a conversion.

## What the tool does

Run it from a command prompt in the folder that holds the two files (on Windows, `py` works in place
of `python`). Each command takes a script, several scripts, or a whole folder.

| Command | What it does | Changes files? |
|---|---|---|
| `coverage` | Does the map know every Classic name the script uses? | No |
| `fix` | Makes the safe rewrites, and lists everything else as a to-do | Only with `-o` or `--in-place` |
| `lookup` | Shows what happened to one name, and what to write instead | No |
| `sweep` | Checks a converted script: is any old spelling left? | No |
| `sites` | Lists lines you should keep as they are and mention in your notes | No |

### coverage - does the map know this script?

```
python ogre_convert.py coverage <file.iss>
```

Lists every Classic name in the file that the map has **no row for** (`UNKNOWN`), and ends with a count.
Each unknown is a question to ask before you convert - see [Stop and ask](#7-stop-and-ask). It never says
`CLEAN`: it only checks that the map knows the names, not that anything is converted yet.

It also catches Classic **idioms** - expressions that read differently now even though no Classic name
is in them. The common one is a check that OgreBot is running by its script name,
`${Script["Buffer:OgreBot"](exists)}`. The new bot is not a LavishScript script, so that reads `NULL`.
`fix` rewrites it to `${ISXOgreEQ2.OgreBot.IsReady}`.

### fix - the safe rewrites

```
python ogre_convert.py fix <file.iss>                       (a dry run: writes nothing, prints the list)
python ogre_convert.py fix <file.iss> -o <output.iss>       (writes the result to a new file)
python ogre_convert.py fix <file.iss> --in-place            (keeps the name - see below)
```

`fix` only rewrites what it can prove is right:

- a call that **moved** or was **renamed** and takes the same arguments;
- a Classic call that had no for-who, where the only change is "the for-who is now the first argument":
  it puts `all` first. A script's own call only ever runs on the session running it, so `all` there means
  "this session" - exactly what the old call did;
- a console command that was renamed and takes the same arguments.

Everything else stays as it was and is printed as a to-do, with the map's how-to-fix text. Each line of
the list says `DONE` (rewritten) or what is left (`signature`, `argOrder`, `notPorted`, `UNKNOWN`, ...).
**Keep that list** - it is the work list for the rest of the conversion.

`--in-place` keeps the file's name, so `run <your script>` and anything that `#include`s it keep working
on the new bot. It first copies the original to a backup beside it (the tool prints the backup's name),
then converts the file. If that backup already exists, it stops and writes nothing - the file may
already be converted.

### lookup - one name

```
python ogre_convert.py lookup Ogre_CampSpot:Set_CampSpot
python ogre_convert.py lookup OgreBotAPI:ChangeCampSpotWho
python ogre_convert.py lookup -ChangeCampSpotWho
```

Object calls are written `Object:Name` or `Object.Name`; console commands keep their dash. `lookup`
prints the map's row:

| Field | Means |
|---|---|
| `status` | what happened to the name (see the table in [Pass 2](#5-pass-2-the-work-list-one-row-at-a-time)) |
| `oldSignature` | Classic's arguments |
| `newForm` | what to write instead |
| `newSignature` | the new arguments - `fw` is the for-who, which comes first |
| `oldSpellingToday` | what the old spelling does under the new bot right now |
| `howToFix` | what to do |
| `note` | **the traps - read it** |
| `newParams` | (console commands) the new command and its parameters, in order |
| `example` | a real Classic line and its new form, when there is one |

`lookup` also answers for a **new** name ("a new-bot name - it exists", and which old names become it),
so you can check every name you write. A name that is not Classic's at all - `oc`, `!ci`, `Script`, `Me`,
`echo` - says so and is unchanged. Only `NOT IN THE MAP` is a question.

### sweep - is it clean?

```
python ogre_convert.py sweep <converted file>
```

`CLEAN` means: no Classic spelling is left that changed, no Classic name the map does not know, no
new-bot call that does not exist, no console command that does not exist, and no console command
wrapped in quotes. Anything else is `NOT CLEAN`, with one line per problem:

| Tag | Means |
|---|---|
| `OLD` | a Classic spelling that changed is still there |
| `UNKNOWN` | a name the map has no row for - a question |
| `BROKEN` | a new-bot call that does not exist, or a console command in quotes |
| `WARN` | a console command whose arguments changed - the sweep cannot tell whether you already fixed them; check each one against its `note` |
| `NOTE` | (button files) a button with a label and no command |

The sweep checks **names** only - not the logic around them. Lines that start with `;` are comments and
are skipped, so `; TODO(Classic): ...` notes are fine.

### sites - lines to keep and list

```
python ogre_convert.py sites <file.iss>
```

Lists lines that should **not** be rewritten, but that you should know about:

| Tag | Means |
|---|---|
| `R10` | the game's own name lookup - `${Me.Ability["..."]}`, `.ToAbilityInfo`, `.ToItemInfo` and the other `.To*Info`. These ask the game server and can come back empty. |
| `R12` | an actor scan or search - `EQ2:QueryActors`, `EQ2:GetActors`, `CustomActorArray`, or `Actor[...]` by name or query instead of by id. These are slow. |
| `INDEX` | a loop guarded by `${Something[${i}](exists)}`. Reading past the end of an ISXEQ2 list **crashes the game client**, and the `(exists)` check is that read. It needs a bound by the list's count. |

The tool finds candidates; look at each one yourself.

## Which files to convert

- **Your own scripts** - yes. That is what the tool and the procedure below are for.
- **Instance files** - not line by line. An instance in the new bot is an IC JSON zone file that the bot
  runs itself, so almost every line of an old instance file becomes a line in that JSON file instead. A
  line-by-line conversion would sweep `CLEAN` and do nothing. Run `coverage` and a dry `fix`: its list
  says what each line becomes, and is the plan for the zone's JSON file.
- **Raid modules** (a file that `inherits Object_ZoneParentInherit` or `Object_ZoneModuleInherit`) - no.
  In the new bot a fight is an encounter JSON file.
- **MCP buttons** - not by hand. The new bot copies your Classic buttons itself when it loads, and puts
  the arguments of every command whose order changed in the new order. `ogre migrate` shows the progress.
  Afterwards, check them with
  `python ogre_convert.py sweep <your Scripts folder>\OgreSave\EQ2\OgreMCP.json`.

## Converting with Claude

You can hand a conversion to Claude (or another AI assistant). Give it the two files above (or their
links), the script, and this instruction:

> Convert this OgreBot Classic script to the new OgreBot. Follow the procedure in the section
> "Converting with Claude" on the "Converting your scripts" page, using ogre_convert.py and
> conversion-map.json.

The rest of this page is that procedure. It is written for Claude, but it works the same for a person.

### 1. The one fact that shapes everything

A Classic spelling does not fail in the new bot - it silently does nothing. A call to a method that no
longer exists does nothing; a read of a member that no longer exists gives `NULL`; nothing is logged. So
"it loads without errors" proves nothing. You are done only when the **sweep** (step 6) says `CLEAN`,
or every line it still names is a question you have listed.

### 2. Rules you must not break

1. **Ask before you write, and never lose the original.**
    - **A file that ships with Classic** (anything in Classic's own folders, such as `EQ2OgreBot`,
      `EQ2OgreCommon`, `OgreConsole`): never edit it. Write the result to a new file (`fix -o`).
    - **The person's own script** (the usual case): ask once, before step 4, which they want:
        - **Keep the name (recommended):** `fix --in-place`. The original is backed up beside it and the
          script keeps its name, so `run` and `#include` lines elsewhere keep working. It refuses if the
          backup already exists - then ask, the file may already be converted.
        - **A new file beside it:** `fix <file.iss> -o <new name>`. The original is untouched.

    Never write over a file the person did not choose, and never without the backup.

2. **Never invent a name.** Every new name you write comes from a map row (`newForm`), or from the map's
   lists of new names (`newApi`, `newConsole`). `lookup` confirms any name. If the map has no row for an
   old name, stop and ask (step 7).
3. **No compatibility shims.** Never write a wrapper, alias or variable that makes an old name keep
   working. Convert the call.
4. **No game name lookups in what you add.** Never write `${Me.Ability["..."]}`, `Me.Ability[name,...]`,
   `.ToAbilityInfo`, `.ToItemInfo` or any `.To*Info` - they ask the game server. Passing an ability or item
   **name** to a bot call (`OgreBotAPI...`, a console command) is fine: the bot looks names up in its own
   ability export. If the Classic line already has a game name lookup, keep it as it is and list it
   (`R10` in `sites`).
5. **No actor scans in what you add.** Never add `EQ2:QueryActors`, `EQ2:GetActors`, `CustomActorArray`
   or an `Actor[...]` that finds an actor by anything but its id (`Actor[query,...]`,
   `Actor[exactname,...]`, `Actor["name"]`). Existing ones: keep, and list (`R12` in `sites`).
   Loops guarded by `${Something[${i}](exists)}` (`INDEX` in `sites`): do not rewrite them (that changes
   the logic) - list them, and say they can crash the game client and need a bound by the list's count.
6. **A name the map does not know is a question.** Leave the line exactly as it was and ask. Do not
   guess what it became.
7. **The for-who comes first** on every new call that takes one (its `newSignature` starts with `fw`).
   When the Classic call had none, the word you insert depends on the line:
    - a **script call** (`OgreBotAPI.<Group>:Name[...]`): `all` - a script's own call only runs on the
      session running it, so `all` is that session;
    - a **console line** (`oc !c -Command ...`): `auto` - the For Who window decides, as it did in Classic.

    A console line that starts `oc !c -cfw <who> -Command ...` already says who: leave it as it is.

### 3. Pass 0 - does the map know this file?

```
python ogre_convert.py coverage <file.iss>
```

Every `UNKNOWN` it lists is a question for step 7. Then decide what kind of file it is:

- It `inherits Object_ZoneParentInherit` or `Object_ZoneModuleInherit`: a **raid module**. Stop. Report
  "raid module - not converted" and nothing else.
- It `#include`s `Ogre_Instance_Include.iss`, calls `function_Handle_Startup_Process`, or lives under
  `InstanceController\Instance_Files`: an **instance file**. Do not convert it as a script. Run a dry
  `fix` (no `-o`, no `--in-place`): its list says what each line becomes. Hand that list back as the plan
  for the zone's IC JSON file, with your questions, and say plainly "instance file - its job moves to an
  IC JSON file; the script is not converted". Writing the IC JSON file is a separate job - ask the person
  before starting it.
- An MCP button file (`OgreMCP.json`): see [MCP buttons](#mcp-buttons) below.
- Anything else: carry on.

### 4. Pass 1 - the mechanical pass

```
python ogre_convert.py fix <file.iss> --in-place          (keep the name - the person's choice in rule 1 of step 2)
python ogre_convert.py fix <file.iss> -o <output.iss>     (a new file, or a file that ships with Classic)
```

It prints every `DONE` line and every line it left for you, with the map's how-to-fix text. **Keep that
list - it is your work list for pass 2.**

### 5. Pass 2 - the work list, one row at a time

For each line the tool left, `lookup` the name, read the row - **the `note` carries the traps** - and do
what its status says:

| status | do this |
|---|---|
| `unchanged` | nothing |
| `moved`, `renamed` | write `newForm`. The tool left it only because it could not prove the arguments line up: compare `oldSignature` with `newSignature` and match each argument by its MEANING, not its position |
| `signature` | write `newForm` and rebuild the arguments from `newSignature` and `note`. "The for-who is now argument 0" on a call that had none: put `all` first. A call that already had a for-who keeps it, moved to the front |
| `argOrder` | write `newForm` (or keep the command) and reorder the arguments exactly as `note` says (console notes give `Old:` and `New:`) |
| `portedElsewhere` | write what `newForm` / `howToFix` names (often a `${ISXOgreEQ2...}` read, a window, or an `ogre` command). If it is a window or command a person uses, it is not script work: comment the line out, `; TODO(Classic) done elsewhere: <newForm> - <old line>`, and list it |
| `dataFile` | the job is now a line in an encounter or IC JSON file. Do not convert it in the script: comment it out, `; TODO(Classic) data file: <newForm> - <old line>`, and list it |
| `notPorted`, `stub`, `removed` | if `howToFix` names a replacement, write it. Otherwise there is no working replacement: comment the line out, `; TODO(Classic) <status>: <old line>`, and list it with what the script loses (`oldSpellingToday`, `note`). Never substitute something "close" |
| `unexamined` | nobody has checked this name yet. Comment it out the same way, list it, and say it needs an answer |

**What depended on a line you commented out goes with it.** An `if !${Return}` (or any read of
`${Return}`) right after a call you commented out would read a stale value, and an `if` or `while` whose
condition you commented out leaves its `{ ... }` body orphaned. Comment those out too, and list each one
with the line it depended on. The same goes for a line the tool rewrote (`DONE`) inside a block whose job
moved to a data file.

**Member reads inside expressions.** `${Ogre_CampSpot.Get_CampSpot}` becomes
`${OgreBotAPI.CampSpot.EffectiveLoc}`: replace only the `Object.Name` part, and keep `${`, `}`, the rest
of the expression, and any `[arguments]` the new member takes. If the new member's empty value differs
(the `note` says so), check that the code using the value still makes sense.

**Commented-out code in the original stays commented**, and is not converted.

**`call` and functions.** A Classic `call OgreBotAPI.X` or `call <Object>.X` is a function call. If the
row's `newForm` is a method (it has a `:`), write a method call, `OgreBotAPI.Group:Name[...]`. If the row
is `unchanged`, keep the `call`.

**Events.** `lookup event:<Name>` says whether a Classic event still fires. An atom attached to an event
whose row is not `unchanged` will never run - list it.

**Console quoting is the same as Classic.** Keep a quoted argument quoted
(`oc !c -ZoneDoor all "${UserInput}"` - without the quotes a value with a space splits in two), and never
wrap a whole command in quotes.

### 6. Pass 3 - prove it

```
python ogre_convert.py sweep <converted file>
python ogre_convert.py sites <converted file>
```

You are not done until the sweep prints `CLEAN` - or until every line it still names is an `UNKNOWN`
you have listed as a question. **Never edit, comment out or "convert" an `UNKNOWN` line to make the sweep
pass**: leave it exactly as Classic wrote it, so the sweep keeps saying `NOT CLEAN` until someone answers
the question. A `NOT CLEAN` result with every unknown listed is an honest result; a `CLEAN` result that
hides them is not. Check every `WARN` line against its row's `note`, and say in the report that you did.

### 7. Stop and ask

Do not decide these yourself:

- A name the map does not have (`UNKNOWN` in `coverage`, `fix` or `sweep`; `NOT IN THE MAP` in `lookup`).
  Leave the line untouched and list it - one question per name, with how often the file uses it.
- An OgreBot **option id** the new bot does not have (`option id the new bot does not have`), in
  `-ChangeOgreBotUIOption`, `Options:Set`, `Options.Value`, `OgreBot.Value` or `TabConfig.<Tab>.<id>`.
  Never swap in an id with a similar name: Classic has several options whose ids differ by one word.
  Proven renames are in the map, and `fix` applies them itself.
- A `notPorted`, `stub`, `unexamined` or `UNKNOWN` call the script cannot work without (its main job).
  Commenting it out makes the script run but not do its job - say so plainly, at the top of the questions.
- A for-who you cannot work out: the old call took it from a variable whose meaning you cannot see, or the
  same line mixes "everyone" and "only me".
- A `signature` row whose `note` and `newSignature` do not tell you how an old argument maps.

In a conversation, ask the person in ONE message with every question together. In a batch run, finish
everything else, then put the questions at the top of the report.

### 8. The report

```
Converted: <in> -> <out>   (kept the name: the original is backed up as <the backup's name>)
Sweep: CLEAN | NOT CLEAN - U unknown names, all in Questions   (N calls checked - the sweep's count; W warnings checked by hand)
Mechanical rewrites: N   (the DONE lines - not repeated below)
Hand conversions:   line  old -> new   (what YOU changed; say WHY for every signature / argOrder one)
Commented out: N   (not ported + done elsewhere + data-file moves + the lines that depended on them)
Not ported (commented out):   line  old  [status]  - what the script loses
Done elsewhere (commented out):   line  old -> <window / ogre command / setting>
Data-file moves:   line  old -> <what>  - belongs in <encounter / IC file>
Game lookups and actor scans kept as they were:   line  text   (R10 / R12 from sites)
Index loops (can crash the client):   line  text   (INDEX from sites)
Questions:   (step 7)
```

### MCP buttons

The new bot copies Classic's buttons itself when it loads - do not rewrite button commands by hand. Your
job is the check afterwards:

```
python ogre_convert.py sweep <Scripts folder>\OgreSave\EQ2\OgreMCP.json
```

In a button file the sweep checks every button's `command` (labels are not code), and names each finding
by its place in the file, with the page and button names, for example
`pages[0]{Combat}.btns.13_0{Intercept}.command`. It reads every command on a line the way the new console
does, including chains. A `WARN` appears only on a button the copy did NOT rewrite - check those against
the row's `note`. A console or `irc !c` button that needs a for-who gets `auto`; a button that calls a
method directly (`OgreBotAPI.<Group>:Name[...]`) is a script call and gets `all`.

You change nothing yourself - the person changes buttons in the MCP window. Report per button:

```
Questions:   button - what is unknown or unclear
Change to:   button - now: <command> - change to: <command> - why (the row's how-to-fix)
No replacement:   button - <command> - [status] - what it loses
Runs, but does less:   button - what changed
Empty buttons:   button   (the NOTE lines)
Checked by hand (WARNs that are fine):   button
Actor scans kept:   button - text   (from sites)
```

Scripts a button starts (`-RunScriptOB`, `runscript ...`) are separate files - each needs its own
conversion; list them.

### The four changes behind most rows

These explain most of what the notes say. [Coming from Classic](coming-from-classic/index.md) has the
longer version, and a page per Classic object with every name on it.

1. **The for-who comes first.** Every new call that acts on some sessions takes the for-who as its
   first argument. A call that had none gets `all` in a script (that session) or `auto` on a console line.
   A name or `igw:${Me.Name}` narrows it, as before.
2. **Calls live in groups.** The flat `OgreBotAPI:Xxx` calls became `OgreBotAPI.<Group>:Xxx` (`CampSpot`,
   `Movement`, `Cures`, `Roster`, `Abilities`, ...). Classic's global objects (`Ogre_CampSpot`,
   `GetInfoOb`, `Obj_CureCurseCalled`, `ClassInfo`, `Ob_AutoTarget`, ...) do not exist in the new bot -
   every call on them is a conversion.
3. **Ability and item names are fine in bot calls.** The bot looks names up in its own ability export.
   Only the game's own name lookups (`${Me.Ability["..."]}`, `.To*Info`) are out.
4. **Data files replace scripts.** Fights are encounter JSON files, and instances are IC JSON files. The
   script calls that drove them (`dataFile` rows) move there instead of being converted.

### Scripts that watched for frozen sessions (OgrePing)

`fix` rewrites the three OgrePing spellings itself. What it cannot do is change the handler's shape, and
the new events mean something different:

| Classic (OgrePing) | New bot (the uplink's session watch) | So the script must... |
|---|---|---|
| `PingTimeOut` fired every round (about 10 seconds) while a session stayed silent | `OgreEvent_SessionFrozen` fires **once** per freeze, after 30 seconds of silence (90 while loading) | act on the first event, and drop any timeout counter |
| a closed or crashed session was never reported, so scripts polled `${Session["is1"](exists)}` | `OgreEvent_SessionGone` fires once for any disappearance (closed, crashed, killed) | attach to it, and drop the polling loop |
| nothing when a session came back | `OgreEvent_SessionRecovered` | (optional) cancel a pending recovery |
| one shared "ignore pings" flag | each event names its session | keep "being recovered" per session |
| `${OgreConsole.bUplink}` | `${LavishScript.Executable.Right[14].Equal["EverQuest2.exe"]}` is TRUE inside the game | test the executable |
| the script had to start OgrePing | the watch is off by default: the ogre config checkbox keeps it on, and `OgreConsoleHub.Sessions:On` turns it on until the uplink restarts | turn it on if `${OgreConsoleHub.Sessions.Watching}` is FALSE |

To bring a session back, let the auto-login do it: it already knows which toon goes in which slot, logs
the toon in and loads OgreBot. Keep every wait bounded, and never test a kill on a session with a toon in
the world without asking first.
