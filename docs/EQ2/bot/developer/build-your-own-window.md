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
| `minimizable` | `true` | `false`: no minimize button, and a double-click on the title bar does nothing. See [Minimizing](#minimizing). |

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
| `ISXOgreX.UI:Close[name]` | Closes the window. The player can also close it with its **X**. Like a `Set`, it lands on a later frame: on the very next line `Window` still exists and `Value` still answers; the `OgreUI_Closed` event marks the moment it is gone. |
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
(a `<div>` around your form, say) have no value: `Value` answers `NULL` for them, as for an id that is not there.

## Changing elements

`ISXOgreX.UI:Set[name,id,value]` changes one element, the right way for its kind:

| Element | What `Set` does |
|---|---|
| Checkbox, radio button | Ticks it for `TRUE`, `1`, `on` or `yes` (any case); unticks it for anything else. From a script the bare tokens are fine: `ISXOgreX.UI:Set[hello,hello-shout,TRUE]`. Ticking a radio button unticks the others in its group, and their `Value`s follow. |
| Text box, text area, slider, hidden input | Sets its value. For a dropdown's hidden input, the dropdown shows the new choice too. |
| Anything else | Sets its text. |

`Set` fires the element's `change` (and, for text, `input`) event, so your window's own script reacts just
as it would if the player had done it. Setting a checkbox to the state it is already in fires nothing.

**You can read your own change straight back**, even inside an event handler:

```
ISXOgreX.UI:Set[hello,hello-name,"Mirelle"]
echo ${ISXOgreX.UI.Value[hello,hello-name]}      ; Mirelle
```

The window applies a `Set` a moment after it is made. A `Value` read of an element you have just changed
waits for that, which takes well under a millisecond. Anything your window's own script changes in its
`change` or `input` handler, with `ogreUISet`, is in by then too. Reads of elements you have not just
changed never wait.

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
- **The command line may be at most 8,191 bytes.** One of 8,192 bytes or more is dropped whole, and nothing tells
  your window or your script; the only trace is one line in the UI log. Send a short command and let the script
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
- An `ogreCall` that your window's own script sends while the page is still loading reaches your script
  BEFORE `OgreUI_Opened` fires: at that moment `Window` does not exist yet and every `Value` is `NULL`. A `Set`
  you issue from there is still applied. Do your reads after the event, not from a load-time command.
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
InnerSpace console covers. A hidden window keeps the position it last had on screen. While the player
drags or resizes a window, the position can be a frame behind.

## Moving and sizing a window

`ISXOgreX.UI:Move[name,x,y]` puts window `name`'s top-left corner at `x`, `y`. `ISXOgreX.UI:Size[name,width,height]`
sets its size. Both take the same screen pixels `Window` reads back, at any window scale, so a number you read
can go straight back in. They work on any open window, by its name: yours, or one of OgreBot's - the Master
Control Panel is `mcp`, the OSA is `osa`, and `OgreUI_Opened` hands you every window's name as it opens.

```
ISXOgreX.UI:Move[mcp,100,200]
ISXOgreX.UI:Size[mcp,520,340]
echo MCP at ${ISXOgreX.UI.Window[mcp].X},${ISXOgreX.UI.Window[mcp].Y} size ${ISXOgreX.UI.Window[mcp].Width}x${ISXOgreX.UI.Window[mcp].Height}
```

- **It is not saved.** When the player moves or sizes a window, Ogre remembers it; a script's `Move` and `Size`
  last until the window closes, and it opens at the player's spot next time. To place a window every time, move
  it after it opens (on `OgreUI_Opened`).
- It changes the window in this session only. Each session has its own windows.
- A window that is not open: nothing happens. `x` and `y` must be whole numbers, `width` and `height` whole
  numbers above 0; anything else prints a line in the console and changes nothing.
- A window is always drawn where its title bar can be grabbed, and no smaller than Ogre's minimum or larger
  than the screen. Ask for a spot or a size outside that and it is drawn at the nearest one it can be; `Window`
  reads back what is drawn.
- Like a `Set`, the change lands on the next frame: read `Window` a moment later, not on the very next line.

## Minimizing

Every framed window, yours included, has a **▼** minimize button in its title bar: it rolls the window up to its
title bar where it sits, and **▲** restores it to exactly the size it had. A double-click on the title bar and the
right-click menu do the same, and the right-click menu's **Minimize all windows** / **Restore all windows** acts on
every open Ogre window at once. You do not write any of this.

- **The size is never lost.** The width does not change while minimized, and Save Position saves the full size.
- **It is not remembered.** A window always opens at its normal size, and opening it again while it is minimized
  restores it.
- **The button never makes your window wider.** In a very narrow window the title is cut short ("...") instead.

### Choosing what stays on screen

By default nothing but the title bar shows while minimized. Mark the parts that should stay:

| You mark | It shows |
|---|---|
| `data-ogmini` | As always, AND while minimized - a status line, a Start / Stop row, an error banner. |
| `data-ogmini="only"` | ONLY while minimized - a one-line summary the full window does not need. |

Mark as many elements as you like, at any depth. Everything else is hidden while minimized, and the containers
around what you marked shrink to fit them, even if your stylesheet gives them a fixed height.

### Knowing when it happens

Your window hears it: an `ogreminimize` event on the window's body (the `.ogbody` that holds your markup), with
`detail.minimized` `true` or `false`. Use it to stop redrawing a list nobody can see while minimized, and to redraw
it when the window is restored.

### Example: a window that minimizes well

`mytool.html` keeps its status line at the top in both states, shows a short summary with a **Stop** button only
while it is minimized, and does not redraw its list while nobody can see it:

```html

<script type="ogre/window">{"title":"My Tool","w":360,"h":320}</script>

<style>
  #mytool-root   { padding: 6px; display: flex; flex-direction: column; gap: 6px; height: 280px; }
  #mytool-status { font-weight: 600; }
  #mytool-mini   { display: flex; gap: 8px; align-items: center; }
  #mytool-list   { flex: 1 1 auto; overflow: auto; }
</style>

<div id="mytool-root">
  <div id="mytool-status" data-ogmini>Idle</div>                     
  <div id="mytool-mini" data-ogmini="only">                          
    <span id="mytool-count">0 items</span>
    <button id="mytool-stop">Stop</button>
  </div>
  <div id="mytool-list"></div>                                       
</div>

<script>
  var mytoolMinimized = false;
  var mytoolItems = ['Apple', 'Banana', 'Cherry'];

  window.mytoolDraw = function () {
    document.getElementById('mytool-count').textContent = mytoolItems.length + ' items';
    if (mytoolMinimized) return;                 // nobody can see the list - draw it on restore
    document.getElementById('mytool-list').innerHTML =
      mytoolItems.map(function (t) { return '<div>' + t + '</div>'; }).join('');
  };

  document.getElementById('mytool-root').closest('.ogbody')
    .addEventListener('ogreminimize', function (e) {
      mytoolMinimized = e.detail.minimized;
      if (!mytoolMinimized) window.mytoolDraw();  // restored: bring the list up to date
    });

  document.getElementById('mytool-stop').addEventListener('click', function () {
    document.getElementById('mytool-status').textContent = 'Stopped';
  });

  window.mytoolDraw();
</script>
```

Minimized, it is the title bar, `Idle`, and `3 items  [Stop]`. Restored, it is the window exactly as it was.

### Opting out

A window that should not minimize - a small toolbar, or a window that already shrinks its own way - says so in its
options. It gets no button, a double-click on its title does nothing, and Minimize all windows leaves it alone:

```html
<script type="ogre/window">{"title":"My Toolbar","w":160,"h":90,"minimizable":false}</script>
```

A window with no title bar (`"chrome": "none"`) never minimizes.

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

Each of these was checked in game on 2026-10-17 or 2026-10-18.

| You try | What happens |
|---|---|
| `confirm('...')` | No dialog appears. It returns `false`. |
| `prompt('...')` | No dialog appears. It returns `null`. |
| `alert('...')` | No dialog appears. |
| `localStorage` or `sessionStorage` | Throws `SecurityError: The operation is insecure.` Keep state in your script instead. |
| `<script src="...">`, `<link rel="stylesheet" href="...">`, `<img src="...">` | Nothing loads, whether the path is a full `file:///` path or a relative one; the UI log says `Not allowed to load local resource: file:///...`. The window has no web address (`about:blank`). Put styles and scripts inline in your file, and images in as inline SVG or `data:` URIs. |
| `console.log('...')` | Goes to `<InnerSpace folder>\x64\Extensions\ISXDK35\OgreUIRuntime\ISXOgreUIHost.log`, as a line ending `CONSOLE: ...`, not to the InnerSpace console. Every session on the PC writes to that one file. |
| A command of 8,192 bytes or more through `ogreCall('cmd', ...)` (the cap is 8,191) | Dropped, with only a line in that same log. |
| `<select>` | Drawn as a small empty box that cannot be clicked or opened. Use the gallery's dropdown. |
| `<input type="number">` | No up/down arrows. Only digits can be typed: a letter empties the box. Use a text box, or the gallery's number field or stepper. |
| `<input type="color">` | Drawn as a text box showing the color code; clicking it opens nothing. Use the gallery's color picker. |
| `<datalist>` | No suggestions ever appear. Use the gallery's combobox. |
| `</script>` written inside your script's text | Ends the block there, as in any HTML page. None of that block runs, the UI log says `UI:Open <name>: script error - SyntaxError: Unexpected EOF`, and the rest of it shows as text in your window. Split it: `'</scr' + 'ipt>'`. |
| A popup, menu or tooltip with `position: fixed`, placed at `getBoundingClientRect()` or mouse (`clientX`) numbers | Fine at normal size, but in a window the player has scaled up it opens far down and to the right of where it should. A scaled window becomes the frame `fixed` positions are measured in, in its own unscaled pixels. Place it with `ogrePlaceFixed(el, x, y)` instead, and turn a size taken off the screen into the element's own pixels with `/ ogreFixedScale(el)`. |
| An error in your window's script | Nothing in the console. The UI log gets `UI:Open <name>: script error - <the error>`, and that block stops; the other blocks still run. |

A `title="..."` on any element shows as a tooltip when the mouse rests on it: Ogre draws it for you.

**Typing in your window.** While a text box in your window has the cursor, the keyboard types into it and
the game does not see the keys. Your InnerSpace console key still opens the console.

- **Escape** clears the box's text and keeps the cursor; a second Escape gives the keyboard back to the game.
- **Enter** in a one-line text box runs your window's own Enter handling first, then gives the keyboard back
  to the game. In a text area, Enter starts a new line.

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
| `ISXOgreX.UI:Set` | method | `name`, `id`, `value` | Changes element `id` in window `name`; a `Value` read of it right after answers the new value. |
| `ISXOgreX.UI.Value` | member | `name`, `id` | string: the element's value; `NULL` if the window is not open or there is no such element. |
| `ISXOgreX.UI.Window` | member | `name` | The open window, or `NULL`. |
| `.Name` | member of `Window` | - | string |
| `.Visible` | member of `Window` | - | bool |
| `.X` | member of `Window` | - | int: screen pixels |
| `.Y` | member of `Window` | - | int: screen pixels |
| `.Width` | member of `Window` | - | int: screen pixels |
| `.Height` | member of `Window` | - | int: screen pixels |
| `ISXOgreX.UI:Move` | method | `name`, `x`, `y` | Puts window `name`'s top-left corner at `x`, `y` (screen pixels). Not saved. |
| `ISXOgreX.UI:Size` | method | `name`, `width`, `height` | Sets window `name`'s size (screen pixels, above 0). Not saved. |
| `OgreUI_Opened` | event | `name` | A window opened. |
| `OgreUI_Closed` | event | `name`, `reason` | A window closed; `reason` is `closed` or `reload`. |
| `ogreUISet` | function in your window | `name`, `id`, `value` | Same as `ISXOgreX.UI:Set`, from the window's own script. |
| `ogreCall` | function in your window | `'cmd'`, command line | Runs one LavishScript command line on the next frame. |
| `ogrePlaceFixed` | function in your window | element, `x`, `y`, optional margin | Puts a `position: fixed` element's top-left at screen position `x`, `y` (the numbers `getBoundingClientRect()` and mouse events give), kept on screen, at any window scale. The element must be showing. |
| `ogreFixedScale` | function in your window | element | number: the scale the element is drawn at (1 in an unscaled window). A size measured on screen divided by it is the size in the element's own pixels. |
| `OgreBotAPI.Options.Value` | member | setting id | string: an OgreBot setting; `""` if unknown. |
| `data-ogmini` | attribute in your markup | - | The element stays shown while the window is minimized (it shows as usual too). See [Minimizing](#minimizing). |
| `data-ogmini="only"` | attribute in your markup | - | The element shows ONLY while the window is minimized. |
| `ogreminimize` | event on your window's body | `detail.minimized` | Fired when the window is minimized (`true`) or restored (`false`). |

### In the EverQuest 2 bot

`ogre ui reload` reloads the UI from disk. Every window closes with reason `reload`. OgreBot re-opens its own
two windows, and your script re-opens yours.
