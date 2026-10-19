<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../index.md).
</div>

# Add your own commands (command packs)

A **command pack** adds your own commands to OgreConsole and to the MCP command builder. Once a pack is
installed, your commands work everywhere ours do: typed in the console, sent to the group, and put on MCP
buttons with the builder, For Who and all.

A pack is a folder of its own, laid out like Ogre's own `Scripts\Ogre` folder. You do not need to build anything
or touch any Ogre file.

> **No promises.** Use this at your own risk, and expect it to change. That said, Kannkor works hard to keep
> things backwards compatible.

## Quick start

1. An example pack ships with Ogre: the folder `Scripts\Ogre\EQ2\Examples\CommandPack\`. Copy the whole
   folder into `Scripts\OgreExternal\` and rename it `Example`. The folder's name is your pack's name.
2. In the InnerSpace console, type `ogre commandpacks`. OgreConsole's **Commands** tab says
   `Command packs loaded: Example (2)`.
3. Try it: `oc !c -Example.HelloPack all Hi there` prints `Hello from a command pack: Hi there` in the
   InnerSpace console of every character.

To start your own pack, rename the folder, then change the file in it.

## The example

`Example\EQ2\Commands\commands.json`:


```json
{
  "author": "Your name here",
  "description": "An example command pack. Copy the whole CommandPack folder into Scripts\\OgreExternal\\ and rename it Example to try it.",
  "commands": [
    {
      "name": "-HelloPack",
      "label": "Hello from a pack",
      "description": "Prints a line in the InnerSpace console of every character the For Who picks.",
      "params": [
        { "name": "who",  "type": "forwho", "description": "Who runs it - leave blank to use the For Who window.", "default": "auto" },
        { "name": "text", "type": "rest",   "description": "What to say.", "default": "" }
      ],
      "execute": [
        { "command": "echo", "args": [ "Hello from a command pack: ${text}" ] }
      ]
    },
    {
      "name": "-RunMyScript",
      "aliases": [ "-rms" ],
      "label": "Run my script",
      "description": "Runs a script, with its arguments, on every character the For Who picks.",
      "params": [
        { "name": "who",    "type": "forwho", "description": "Who runs it - leave blank to use the For Who window.", "default": "auto" },
        { "name": "script", "type": "string", "description": "The script to run, like MyFolder/myscript.", "default": "" },
        { "name": "args",   "type": "rest",   "description": "Anything after the script name is passed to it, one argument each.", "default": "" }
      ],
      "execute": [
        { "command": "runscript", "args": [ "${script}", "${args}" ] }
      ]
    }
  ]
}
```

`oc !c -Example.rms all MyFolder/myscript 12 "two words"` runs `runscript "MyFolder/myscript" "12" "two words"`
on every character.

## Where a pack goes

A pack is a folder in `Scripts\OgreExternal\`, laid out the same way as Ogre's own `Scripts\Ogre\`: a folder
for what works in every game (`Common`), a folder per game (`EQ2`), and inside those, one folder per kind of
thing. Today a pack can carry console commands; keeping to this layout leaves room for more later.

```
Scripts\OgreExternal\
  BJTools\                              your pack - the folder's name is the pack's name
    Common\Commands\commands.json       commands for every game
    EQ2\Commands\commands.json          commands for EverQuest 2
```

| What | Rule |
|---|---|
| Pack folder | `Scripts\OgreExternal\<PackName>\`. One folder per pack. |
| Pack name | The folder's name: letters, digits and `_`, up to 40 characters. No spaces, no dots. |
| Command files | `Common\Commands\commands.json`, `EQ2\Commands\commands.json`, or both. Both are one pack. |
| Patching | Ogre's patcher never touches `Scripts\OgreExternal`. Your pack is safe across updates. |

Every PC that should run a pack's commands needs the pack installed. Each character reads its own command
list, so a character without the pack says `Unknown command entered: -BJTools.YourCommand` when the command
reaches it, and does nothing else.

## The file

The file is JSON. Text goes in double quotes, and a backslash in text is written `\\`.

| Field | Required | What it is |
|---|---|---|
| `author` | yes | Your name. Shown with your pack. |
| `description` | no | One line about the pack. |
| `commands` | yes | The list of commands, below. |

### A command

| Field | Required | What it is |
|---|---|---|
| `name` | yes | The command, like `-BuffMe`: a dash, then letters, digits or `_`. It is typed with your pack's name in front: `-BJTools.BuffMe`. Any case works. |
| `aliases` | no | Other names for it, like `[ "-bm" ]`, typed `-BJTools.bm`. Same rules as `name`. |
| `label` | yes | The name the MCP builder lists it under. |
| `description` | yes | What it does. The builder shows it. |
| `params` | yes | Its parameters, in the order they are typed. **At least one must be a `forwho`.** |
| `execute` | yes | What it runs: one or more steps, run in order. |

### A parameter

| Field | Required | What it is |
|---|---|---|
| `name` | yes | Letters, digits or `_`. Used as `${name}` in the steps. |
| `type` | yes | One of the types below. |
| `description` | yes | What to put there. The builder shows it. |
| `default` | no | The value when it is left out, as text: `"auto"`, `"30"`, `"TRUE"`. |
| `allParams` | no | For a `rest` parameter: `true` takes everything to the end of the line, other commands' names included. Without it, `rest` stops at the next command. |

| Type | Takes |
|---|---|
| `forwho` | Who the command is for: `all`, a name, `igw:Name`, `@Healer1` and every other For Who. Left out, or `auto`, it uses the For Who window. |
| `string`, `int`, `int64`, `float`, `bool` | One word. Put quotes around text with spaces: `"two words"`. |
| `point3f` | A location: `x,y,z` as one word, or three numbers. |
| `rest` | Everything after it, each word as its own argument. |

### An execute step

| Field | Required | What it is |
|---|---|---|
| `command` | yes | What to run. Any InnerSpace command or LavishScript method. |
| `args` | no | Its arguments. `${name}` is replaced by that parameter's value. |

How a step becomes the line that runs:

| `command` | `args` | Runs |
|---|---|---|
| `runscript` (no `:`) | `[ "${script}", "${args}" ]` | `runscript "MyFolder/myscript" "12" "two words"` - each argument quoted, separated by spaces. |
| `Script[MyScript]:QueueCommand` (has a `:`) | `[ "${what}" ]` | `Script[MyScript]:QueueCommand["hello"]` - in brackets, separated by commas. |

An argument that is exactly `${a rest parameter}` becomes one argument per word. Empty arguments at the end are
left off.

## For Who

Every command needs a `forwho` parameter. Ogre checks it **before** your steps run, on every character: a
character the For Who does not pick runs nothing and says nothing. Your script never has to check it.

When a command has more than one `forwho`, the first one decides who runs it. The others are just values you
can pass on.

## Names

Every pack command is typed with its pack's name: **`-<PackName>.<command>`**, like `-Example.HelloPack`, and
its aliases the same way, like `-Example.rms`. There is no short form.

- **Anyone can see it is not one of OgreBot's own.** `-BJTools.Buff` says where it came from.
- **A pack can never replace one of ours.** Ours have no pack name in front.
- **Two packs never clash.** Two packs can both have a `-Buff`; they are `-BJTools.Buff` and `-Other.Buff`.
  Installing a new pack never breaks a command that already works.

## Loading and reloading

- Packs load with the console's own commands when Ogre starts.
- After you change a pack, type `ogre commandpacks` (or `ogre packs`). It re-reads every pack.
- The MCP command builder shows the new list the next time the MCP opens.
- What loaded, and anything that did not, is in OgreConsole's **Commands** tab: `Command packs loaded: ...`,
  then one line for each problem.

A command with a mistake is skipped with the reason, and the rest of its pack still loads. A file with a
mistake in its JSON, or with no `author`, is not loaded at all.

## In the MCP

Pack commands are in the command builder's list, under their `label`, with every other command. Build a
button with them the same way: pick the command, fill in its parameters, save.

## Checklist

For a person or an AI writing a pack:

- [ ] Folder `Scripts\OgreExternal\<PackName>\`, name made of letters, digits or `_`.
- [ ] File `EQ2\Commands\commands.json` (and/or `Common\Commands\commands.json`), valid JSON, with `author` and `commands`.
- [ ] Commands are typed `-<PackName>.<name>` - in buttons, scripts and anything you hand out.
- [ ] Each command has `name` (`-Word`), `label`, `description`, `params` and at least one `execute` step.
- [ ] Each command has a `forwho` parameter.
- [ ] Each parameter has `name`, a `type` from the table, and a `description`. Each `default` is text.
- [ ] Every `${name}` in a step matches a parameter's `name`.
- [ ] `ogre commandpacks` reports your pack with the number of commands you expect, and no problem lines.
