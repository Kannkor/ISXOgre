# Your first script

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../index.md).
</div>

This page is for you if you have never written a script. It shows one small script, explains each piece,
and then shows how a script reads the bot and makes your group act. After this, the
[API reference](api/index.md) tells you what each bot call does.

Scripts are written in LavishScript, the InnerSpace script language.

## Where a script goes and how to run it

A script is a plain text file that ends in `.iss`. Put it in InnerSpace's `Scripts` folder, for example
`Scripts\waitforgroup.iss`.

To run it, type this in the InnerSpace console:

```
run waitforgroup
```

- Leave off the `.iss`.
- The path starts at the `Scripts` folder. A script in a folder of its own is run as
  `run MyScripts/waitforgroup`, with forward slashes.

To stop a script that is still running, type `end` and its name:

```
end waitforgroup
```

## A whole script

This script waits until you are out of combat and your whole group is in the zone with you. Then it tells
the bots of everyone in your group to resume. If that has not happened after one minute, it gives up.

```
; waitforgroup.iss
; Wait until the fight is over and the group is here, then resume the group's bots.
function main()
{
    variable int Tries=0
    variable bool Ready=FALSE
    variable string Who="igw:${Me.Name}"

    ; Check once a second, 60 times: give up after one minute.
    while ${Tries}<60
    {
        if !${OgreBotAPI.Combat.InCombat} && ${OgreBotAPI.Roster.InZone}
        {
            Ready:Set[TRUE]
            break
        }
        Tries:Inc
        wait 10
    }

    if !${Ready}
    {
        echo "Gave up: still fighting, or the group is not all here."
        return
    }

    echo "All ${OgreBotAPI.Roster.GroupSize} of us are here. Resuming."
    oc !c -resume ${Who}
}
```

## Each piece

**`function main()` and braces.** `main` is where the script starts. Its lines go between `{` and `}`.
The `{` and the `}` each go on a line of their own, for `function`, `if`, `else` and `while` alike. Writing
`function main() {` on one line is wrong.

**Comments.** A line that starts with `;` is a comment, and the script skips it. The `;` must be the first
thing on the line (spaces before it are fine). There is no comment at the end of a line, so keep each
comment on a line of its own.

**Variables.** `variable <type> <name>=<value>` makes a variable. The common types are:

| Type | Holds | Example |
|---|---|---|
| `int` | a whole number | `variable int Tries=0` |
| `string` | text | `variable string Name="Bob"` |
| `bool` | `TRUE` or `FALSE` | `variable bool Ready=FALSE` |

A variable made inside `main` lasts until `main` ends.

**`${...}` reads a value.** `${Tries}` is put in its place by the value of `Tries` before the line runs. So
`echo "Try ${Tries}"` prints `Try 3`. The same goes for the game and the bot: `${Me.Name}` is your
character's name.

**Changing a variable.** A variable is changed with a method, written with a `:`, on a line of its own:

```
Tries:Inc
Tries:Inc[5]
Tries:Set[0]
Ready:Set[TRUE]
Name:Set["Bob"]
```

`Inc` adds 1 (or the number you give it). `Set` gives the variable a new value.

**`echo`** writes a line in the InnerSpace console. It is the easiest way to see what your script is doing.

**`if` and `else`.** `if` runs the lines under it only when its test is true. `else` runs when it is not.
A test is true when it is not `0`, `NULL` or `FALSE`.

- Compare numbers with `<`, `>`, `<=`, `>=`, `==` and `!=`, as in `${Tries}<60`.
- `&&` means and, `||` means or, and `!` in front means not: `!${Ready}` is true when `Ready` is `FALSE`.
- With only one line under it, an `if` needs no braces. With more, put them in `{` and `}`.

**`while`** runs the lines in its braces again and again, as long as its test is true. `break` leaves the
loop at once.

**`wait`** pauses the script. Its number is in **tenths of a second**: `wait 10` is one second, `wait 50` is
five. Every loop needs a `wait` in it. A loop without one uses up all the time the game has to draw a frame,
and the game looks frozen.

**A loop that gives up.** The `while` above stops after 60 tries, one second apart. Without that limit, a
group member who never zones in would keep the script waiting forever.

**`return`** leaves the function at once. Here it stops `main` early, so nothing after it runs.

**Quoting.** A space splits a line into separate words. Text with a space in it goes in double quotes:
`echo "Gave up: still fighting"`. A `"` inside quoted text is written `\"`. When you pass a variable's text
to another command or method inside quotes, write a `~` before the `}`, as in `"${Name~}"`, so a quote or a
`}` in the text cannot break the line.

## Reading the bot

A **member** is read with `${...}` and a `.` between the parts:

```
echo ${OgreBotAPI.Roster.GroupSize}
```

That prints how many people are in your group, counting you. Some members take arguments in `[ ]`:
`${OgreBotAPI.Roster.InZone[50]}` is TRUE only when the rest of your group is in this zone and no farther
than 50 from you. Each member's row in the API reference says what it returns.

`${Me}`, `${Target}`, `${Zone}` and the like are not the bot's. They are ISXEQ2's own objects, so they are
not in the bot's API reference. `${Me.Name}` is your character's name.

A **method** makes something happen. It is a line of its own, with a `:` before the method's name:

```
OgreBotAPI.Bot:Resume[igw:${Me.Name}]
```

To read a result, use a member.

## Making the group act

Most bot methods take a [for-who](api/ogrebotapi/ForWho.md) as their first argument. In a script, the
for-who only decides whether **this** character acts. `OgreBotAPI.Bot:Resume[igw:${Me.Name}]` resumes
your own bot, because you are in your group. It never reaches the other characters.

To make other characters act, send a console command with `oc !c`, as the script above does:

```
oc !c -resume igw:${Me.Name}
```

The command goes to the sessions on this PC, this one included. The for-who after the command picks which
of them act:

- `igw:${Me.Name}` is your whole group.
- `igwbn:${Me.Name}` is your group without you.
- Left out, or `auto`, it uses the For Who window.

`oc !ci` does the same as `oc !c`. The [Commands](api/commands/index.md) pages list every console command
and what it takes.

## Where next

- [API reference](api/index.md) - every member, method and command a script can use, with an example.
- [For-who](api/ogrebotapi/ForWho.md) - every word a for-who can use.
- [Converting your scripts](converting.md) - moving an OgreBot Classic script over to the new bot.
