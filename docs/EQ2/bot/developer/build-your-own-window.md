# Build your own window

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../index.md).
</div>

Ogre's in-game windows are HTML pages drawn over the game. Your own script, or your own extension, can put a
window of its own up there, read and change what is in it, react when the player clicks a button, and hear
when any window opens or closes.

All you need loaded is the core, `ext ISXOgreX`. You do not need OgreBot, a profile, or a toon in the world:
it works at the login screen.

> **No promises.** Use this at your own risk, and expect it to change. That said, Kannkor works hard to keep
> things backwards compatible, and the new bot is the first big break in a very long time.

## Quick start

A working example ships with Ogre. In the InnerSpace console, type:

```
run Ogre/Common/OgreUI/examples/hello/hello
```

A small **Hello** window opens. Type a name, tick **Shout it**, and press **Say hello**: the greeting
appears in the console and in the window's status line. Close the window with its **X**, and the script ends.

The example is three files in `Scripts\Ogre\Common\OgreUI\examples\hello\`:

| File | What it is |
|---|---|
| `hello.html` | The window: its options, its style, its markup, and its script, all in one file. |
| `hello.iss` | The script that opens the window, reacts to it, and closes it. |
| `hello.md` | The text the window's **?** button shows. |

To start your own window, copy that folder next to your script and rename things.

### The window: `hello.html`

```html

<script type="ogre/window">{"title":"Hello","w":280,"h":0}</script>

<style>
  #hello-root { padding: 10px; display: flex; flex-direction: column; gap: 8px; }
  #hello-root .row { display: flex; gap: 8px; align-items: center; }
  #hello-status { opacity: 0.8; }
</style>

<div id="hello-root">
  <div class="row">Name <input type="text" id="hello-name" value="Brutus"></div>
  <label class="row"><input type="checkbox" id="hello-shout"> Shout it</label>
  <button id="hello-say">Say hello</button>
  <span id="hello-status">Ready.</span>
</div>

<script>
  // The button tells the script. ogreCall('cmd', ...) runs one LavishScript command line on the next frame;
  // here it fires an event the script attached an atom to.
  document.getElementById('hello-say').addEventListener('click', function () {
    window.ogreCall('cmd', 'Event[Hello_Say]:Execute');
  });
</script>
```

### The script: `hello.iss`

```
; hello.iss - opens hello.html, reacts to its button, follows its checkbox, re-opens it after a UI reload, and
; ends when you close the window.
;   run Ogre/Common/OgreUI/examples/hello/hello
variable string Dir="${Script.CurrentDirectory}"
variable bool Shout=FALSE

; The window's button fires this (hello.html: Event[Hello_Say]:Execute).
atom(script) OnSay()
{
    variable string Greeting="Hello, ${ISXOgreX.UI.Value[hello,hello-name]}!"
    if ${ISXOgreX.UI.Value[hello,hello-shout]}
        Greeting:Set["${Greeting.Upper}"]
    echo "${Greeting}"
    ISXOgreX.UI:Set[hello,hello-status,"Said: ${Greeting}"]
}

; Every window's close comes here. A reload takes every window away - open ours again. Closed by the user: stop.
atom(script) OnClosed(string name, string reason)
{
    if !${name.Equal[hello]}
        return
    if ${reason.Equal[reload]}
        OpenWindow
    else
        Script:End
}

; The window is one file; its ? help is the .md beside it. Already open: nothing happens.
atom(script) OpenWindow()
{
    ISXOgreX.UI:Open[hello,"${Dir}/hello.html","${Dir}/hello.md"]
}

function main()
{
    LavishScript:RegisterEvent[Hello_Say]
    Event[Hello_Say]:AttachAtom[OnSay]
    Event[OgreUI_Closed]:AttachAtom[OnClosed]
    OpenWindow

    ; Follow the checkbox. Value is NULL until the window is open, so only compare once it answers.
    while TRUE
    {
        if ${ISXOgreX.UI.Value[hello,hello-shout](exists)} && !${ISXOgreX.UI.Value[hello,hello-shout].Equal[${Shout}]}
        {
            Shout:Set[${ISXOgreX.UI.Value[hello,hello-shout]}]
            echo "Shout is now ${Shout}"
        }
        wait 10
    }
}

atom atexit()
{
    Event[Hello_Say]:DetachAtom[OnSay]
    Event[OgreUI_Closed]:DetachAtom[OnClosed]
    ISXOgreX.UI:Close[hello]
}
```

The rest of this page explains each piece.

## The window file

A window is **one HTML file**. It is not a whole web page, so there is no `<html>`, `<head>` or `<body>`: just
the parts below, in this order.

1. **Options** (optional): one `<script type="ogre/window">` block holding JSON.
2. **Style**: a `<style>` block.
3. **Markup**: what the window shows.
4. **Script**: one or more `<script>` blocks. They run once, after the markup is in place, in file order.

The file can sit anywhere on disk; you pass its full path when you open it. `${Script.CurrentDirectory}` is
the folder your script is in, with forward slashes, so `"${Script.CurrentDirectory}/mywindow.html"` finds a
file next to your script.

### Window options

| Option | Default | What it does |
|---|---|---|
| `title` | the window name | The text in the title bar. |
| `w`, `h` | `0` (fit the content) | Width and height in pixels. |
| `x`, `y` | `60`, `60` | Where the window first opens. |
| `resizable` | `true` | The player can resize it from the corner. |
| `draggable` | `true` | The player can move it by its title bar. |
| `chrome` | `"full"` | `"none"` draws no title bar or frame - just your content. |
| `capture` | `true` | `false` lets clicks fall through the window to the game. |
| `scale` | `0` (the player's UI scale) | A size multiplier for this window only, from 0.5 to 2. |
| `noPersist` | `false` | `true`: never remember where the player put it. |
| `noHelp` | `false` | `true`: no **?** button in the title bar. |

Ogre remembers where the player moves and sizes each window, by its name. `x`, `y`, `w` and `h` are only
where it starts the very first time; after that, the player's position wins.

### Names: keep yours your own

Every window shares one page, and your scripts run in that page's global scope.

- **Give your window a name that is clearly yours**, for example `mytool` rather than `options`. Opening a name
  that is already open does nothing, so a clash with another window means yours never appears.
- **Prefix your element ids, CSS selectors and global functions** with your window's name: `mytool-status`,
  `#mytool-root .row`, `window.mytoolRefresh`. Two windows with the same id, class or global function name
  will fight.

## Loading and unloading the window

| You write | What happens |
|---|---|
| `ISXOgreX.UI:Open[name,path]` | Reads the file at `path` now; the window opens a moment later, once the UI is up. |
| `ISXOgreX.UI:Open[name,path,helpPath]` | The same, and the **?** button shows the markdown file at `helpPath`. |
| `ISXOgreX.UI:Close[name]` | Closes the window. The player can also close it with its **X**. |
| `${ISXOgreX.UI.Window[name](exists)}` | `TRUE` while the window is open, `NULL` when it is not. |

- **`Open` does not wait.** Straight after it, the window is not there yet. To act once it is, attach to
  `OgreUI_Opened` and wait for your window's name; by the time that fires, every `Value` in the window
  answers. Or check `${ISXOgreX.UI.Window[name](exists)}` in a loop, with a limit on how long you wait. With
  the UI up it takes a few frames; at game start, the UI comes up after the core signs in.
- If the file cannot be read, `Open` prints a warning in the console and opens nothing.
- **Opening a window that is already open does nothing**: no second copy, no reset, no event.
- `Close` on a window that is not open does nothing.
- **Closing does not end your script.** The hello example ends itself when it hears its window close; see
  [Knowing when windows open and close](#knowing-when-windows-open-and-close).

## Reading elements

`${ISXOgreX.UI.Value[name,id]}` is the current value of the element with id `id` in window `name`.

| Element | Value |
|---|---|
| Checkbox, radio button | `TRUE` or `FALSE` |
| Text box, password box, text area | The text. An empty box is `""`, not `NULL`. |
| Slider (`type="range"`) | The number, as text. |
| Hidden input | Its value. Ogre's dropdowns keep their choice in one (see the gallery). |
| Any other element with an id and no child elements (a `<span>`, a `<label>`, a `<button>`) | Its text. |

`Value` is `NULL` when the window is not open, or when there is no such element. Use `(exists)` to tell
those cases apart from an empty text box.

The value is kept up to date as the player types, clicks and picks. Elements that contain other elements
(a `<div>` around your form, say) have no value.

## Changing elements

`ISXOgreX.UI:Set[name,id,value]` changes one element, the right way for its kind:

| Element | What `Set` does |
|---|---|
| Checkbox, radio button | Ticks it for `TRUE`, `1`, `on` or `yes` (any case); unticks it for anything else. Ticking a radio button unticks the others in its group, and their `Value`s follow. |
| Text box, text area, slider, hidden input | Sets its value. For a dropdown's hidden input, the dropdown shows the new choice too. |
| Anything else | Sets its text. |

`Set` fires the element's `change` (and, for text, `input`) event, so your window's own script reacts just
as it would if the player had done it. Setting a checkbox to the state it is already in fires nothing.

**`Set` takes effect on the next frame.** Read the value straight after a `Set` and you get the old one;
after a `waitframe` you get the new one:

```
ISXOgreX.UI:Set[hello,hello-name,"Mirelle"]
echo ${ISXOgreX.UI.Value[hello,hello-name]}      ; still the old name
waitframe
echo ${ISXOgreX.UI.Value[hello,hello-name]}      ; Mirelle
```

`waitframe` (like `wait`) works in a `function`, not in an `atom`: an event handler cannot wait. If you set
something from an event handler and need to read it back, do the reading in your `main` loop.

Put the value in double quotes when it has spaces or commas in it: `ISXOgreX.UI:Set[hello,hello-name,"Mirelle Dawn"]`.

### From the window's own script

When your window's script changes an element itself, change it with `ogreUISet` so scripts see the new value:

```js
ogreUISet('hello', 'hello-status', 'Working...');
```

It takes the same three things as `ISXOgreX.UI:Set` and behaves the same way. If you change an element some
other way (`el.textContent = ...`, `el.checked = true`), `Value` keeps answering the old value until the
player next touches that element.

## Reacting to clicks

The window talks to your script with one call:

```js
window.ogreCall('cmd', 'Event[Hello_Say]:Execute');
```

It runs one LavishScript command line, exactly as if typed in the console. The usual pattern is to fire an
event your script has attached an atom to, as hello does. Your script registers the event with
`LavishScript:RegisterEvent[Hello_Say]` and attaches with `Event[Hello_Say]:AttachAtom[OnSay]`.

- The command runs on the **next frame**, not inside the click.
- **Nothing comes back.** `ogreCall('cmd', ...)` returns nothing useful. To answer the window, the script
  uses `ISXOgreX.UI:Set`.
- **Keep the command line fixed.** Do not build it from what the player typed: a `]` or a `"` in their text
  changes the command. Send a fixed command and let the script read the text with `Value`.
- **The command line must be under 8,191 bytes.** A longer one is dropped whole, and nothing tells your
  window or your script; the only trace is one line in the UI log. Send a short command and let the script
  read what it needs with `Value`.

## Knowing when windows open and close

Two events fire for **every** window - yours, OgreBot's, and the help windows the **?** button opens:

| Event | Arguments |
|---|---|
| `OgreUI_Opened` | `name` |
| `OgreUI_Closed` | `name`, `reason`: `closed` (its **X**, or `ISXOgreX.UI:Close`) or `reload` |

- ISXOgreX registers both events when it loads, so your script attaches with
  `Event[OgreUI_Closed]:AttachAtom[...]` and needs no `RegisterEvent`. Load ISXOgreX before your script
  attaches.
- `OgreUI_Opened` fires every time a window is created, including your own re-open after a reload. It does
  not fire for an `Open` of a window that is already open, and it does not say why the window opened: keep
  your own note if you need to tell a first open from a re-open.
- The help window that the **?** button opens is named `help:` followed by the window's name, for example
  `help:hello`.
- Hiding or showing a window does not fire them; only opening and closing does.

### Surviving a UI reload

A reload of the UI closes **every** window at once. That happens when a patch lands, when the player types
`ogre ui reload`, and it can happen while the game is starting up. Each window gets `OgreUI_Closed` with reason
`reload`. **Nothing re-opens your window for you**: re-open it when you see your own name with that reason.

```
atom(script) OnClosed(string name, string reason)
{
    if ${name.Equal[mytool]} && ${reason.Equal[reload]}
        ISXOgreX.UI:Open[mytool,"${Dir}/mytool.html"]
}
```

- Your window counts as closed from the moment the reload starts: `Window` and `Value` answer `NULL` until it
  is open again.
- Calling `Open` from inside your `OgreUI_Closed` handler is fine; the new window opens as soon as the new UI
  is up.
- The new window is a fresh copy of your file: everything in it is back to what the file says.

## Where a window is

`${ISXOgreX.UI.Window[name]}` is the window, while it is open:

| Member | Type | What it is |
|---|---|---|
| `Name` | string | The window's name. |
| `Visible` | bool | `FALSE` while the window is hidden. |
| `X`, `Y` | int | Its top-left corner on the screen, in pixels. |
| `Width`, `Height` | int | Its size on the screen, in pixels, after its scale. |

Ogre can hide a window without closing it: for example, when the player has Ogre hide the windows that the
InnerSpace console covers. A hidden window keeps the position it last had on screen. Like `Value`, the
position is a frame behind a move.

## The ? button

Pass a help file as the third argument of `Open` and the **?** in your window's title bar shows it. The help
is plain markdown, kept small on purpose:

```
---
title: Hello
---
The smallest example window: type a name and press **Say hello**.

### What you can do here
- **Name** - who to greet.
- **Shout it** - greet in capitals.
```

It understands `### headings`, paragraphs, `- ` list items, `**bold**` and `` `code` ``. Anything else shows
as plain text. The block between the `---` lines at the top is optional and is not shown.

Open a window without a help file and its **?** says "No help written for this window yet." To have no **?** at
all, put `"noHelp": true` in the window's options.

## Every element, working

Ogre's windows use about thirty kinds of element: tabs, dropdowns, drag-to-reorder lists, a color picker,
and more, many of them built by hand. The **gallery** example has a working sample of each, with the code
next to it:

```
run Ogre/Common/OgreUI/examples/gallery/gallery
```

Copy what you need from `Scripts\Ogre\Common\OgreUI\examples\gallery\gallery.html`. For a dropdown, a number
field or a color picker, use the gallery's versions: they are the ones Ogre's own windows are built with.

## Reading OgreBot's own settings

When OgreBot is running, a script can read any setting from the bot's own window:

```
echo ${OgreBotAPI.Options.Value[checkbox_settings_loot]}
```

The id is the setting's name, matched without regard to case. Checkboxes read `TRUE` or `FALSE`; other
settings read as the text or number they hold. An unknown id, or no profile loaded (at the login screen,
say), reads `""` rather than `NULL`. The ids are listed on
[OgreBot option ids](coming-from-classic/options.md).

## From a C++ extension

There is no separate C++ API. An extension uses the same names through InnerSpace:

```cpp
// open, change, read  (myDir = the folder your files are in, with forward slashes)
std::string open = "ISXOgreX.UI:Open[mytool,\"" + myDir + "/mytool.html\"]";
pISInterface->ExecuteCommand(open.c_str());
pISInterface->ExecuteCommand("ISXOgreX.UI:Set[mytool,mytool-status,\"Ready\"]");

char buf[256];
pISInterface->DataParse("${ISXOgreX.UI.Value[mytool,mytool-name]}", buf, sizeof(buf));

// hear every window open and close
static void __cdecl OnUIClosed(int argc, char *argv[], PLSOBJECT)
{
    // argv[0] = window name, argv[1] = "closed" or "reload"
}

unsigned int ev = pISInterface->RegisterEvent("OgreUI_Closed");
pISInterface->AttachEventTarget(ev, OnUIClosed);
// ... and in your Shutdown:
pISInterface->DetachEventTarget(ev, OnUIClosed);
```

- `RegisterEvent` finds the event if it already exists and creates it if not, so it does not matter whether
  your extension or ISXOgreX loads first.
- Events fire on the game's frame, the same thread your extension's pulse runs on.
- Keep the callback short: it runs inside every window open and close.

## Pitfalls

Each of these was checked in game on 2026-10-17.

| You try | What happens |
|---|---|
| `confirm('...')` | No dialog appears. It returns `false`. |
| `prompt('...')` | No dialog appears. It returns `null`. |
| `alert('...')` | No dialog appears. |
| `localStorage` or `sessionStorage` | Throws `SecurityError: The operation is insecure.` Keep state in your script instead. |
| `<script src="...">`, `<link rel="stylesheet" href="...">`, `<img src="...">` | Nothing loads, whether the path is a full `file:///` path or a relative one; the UI log says `Not allowed to load local resource: file:///...`. The window has no web address (`about:blank`). Put styles and scripts inline in your file, and images in as inline SVG or `data:` URIs. |
| `console.log('...')` | Goes to `<InnerSpace folder>\x64\Extensions\ISXDK35\OgreUIRuntime\ISXOgreUIHost.log`, as a line ending `CONSOLE: ...`, not to the InnerSpace console. Every session on the PC writes to that one file. |
| A command over 8,191 bytes through `ogreCall('cmd', ...)` | Dropped, with only a line in that same log. |
| Reading `Value` straight after `Set` | The old value. Wait one frame (`waitframe`). |
| `</script>` written inside your script's text | Ends the block there, as in any HTML page. None of that block runs, the UI log says `UI:Open <name>: script error - SyntaxError: Unexpected EOF`, and the rest of it shows as text in your window. Split it: `'</scr' + 'ipt>'`. |
| An error in your window's script | Nothing in the console. The UI log gets `UI:Open <name>: script error - <the error>`, and that block stops; the other blocks still run. |

Modern JavaScript (arrow functions, `const`, template strings) works. Ogre's own windows are written in plain
older JavaScript, which works too.

## What not to rely on

Only the names on this page are meant for your scripts. Everything else on `ISXOgreX.UI`, and every `ogreWM...`
function in the page, is Ogre's own plumbing and may change or vanish without notice. That includes `Load`,
which replaces Ogre's entire UI and does not bring it back.

## Reference

| Name | Kind | Arguments | Returns / does |
|---|---|---|---|
| `ISXOgreX.UI:Open` | method | `name`, `path`, optional `helpPath` | Opens window `name` from the file at `path`; nothing if it is already open. |
| `ISXOgreX.UI:Close` | method | `name` | Closes window `name`. |
| `ISXOgreX.UI:Set` | method | `name`, `id`, `value` | Changes element `id` in window `name` (next frame). |
| `ISXOgreX.UI.Value` | member | `name`, `id` | string: the element's value; `NULL` if the window is not open or there is no such element. |
| `ISXOgreX.UI.Window` | member | `name` | The open window, or `NULL`. |
| `.Name` | member of `Window` | - | string |
| `.Visible` | member of `Window` | - | bool |
| `.X` | member of `Window` | - | int: screen pixels |
| `.Y` | member of `Window` | - | int: screen pixels |
| `.Width` | member of `Window` | - | int: screen pixels |
| `.Height` | member of `Window` | - | int: screen pixels |
| `OgreUI_Opened` | event | `name` | A window opened. |
| `OgreUI_Closed` | event | `name`, `reason` | A window closed; `reason` is `closed` or `reload`. |
| `ogreUISet` | function in your window | `name`, `id`, `value` | Same as `ISXOgreX.UI:Set`, from the window's own script. |
| `ogreCall` | function in your window | `'cmd'`, command line | Runs one LavishScript command line on the next frame. |
| `OgreBotAPI.Options.Value` | member | setting id | string: an OgreBot setting; `""` if unknown. |

### In the EverQuest 2 bot

`ogre ui reload` reloads the UI from disk. Every window closes with reason `reload`. OgreBot re-opens its own
two windows, and your script re-opens yours.
