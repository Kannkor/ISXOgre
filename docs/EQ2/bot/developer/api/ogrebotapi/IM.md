# OgreBotAPI.IM

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Members

### `EndWhenFinished`

`${OgreBotAPI.IM.EndWhenFinished}`

Whether -end is armed, so the Inventory Manager window closes itself once the work has been idle for about 1.5 seconds. Only the console arms it (the -end flag of an `ogre im` line); there is no method for it, and closing the window clears it.

**Returns:** bool: TRUE while -end is armed; FALSE otherwise.

```text
echo ${OgreBotAPI.IM.EndWhenFinished}
```

### `IsOpen`

`${OgreBotAPI.IM.IsOpen}`

Whether the Inventory Manager window is up on this session - the window is the session, so this is what a script waits on after starting it with -end. It reads FALSE when the UI host is not available, even while modes run from the console.

**Returns:** bool: TRUE while the Inventory Manager window really exists; FALSE when it is closed or could not open.

```text
echo ${OgreBotAPI.IM.IsOpen}
```

### `IsRunning`

`${OgreBotAPI.IM.IsRunning}`

Whether the Inventory Manager is doing work right now - a mode (depot, sell, destroy, tse, restock, trade, quiver), a chain of them, or a depot withdraw started anywhere. It is FALSE while the window sits open and idle and can be FALSE just before a mode starts, so to wait for work to finish poll IsOpen with -end instead.

**Returns:** bool: TRUE while any Inventory Manager mode or chain is working; FALSE when idle.

```text
echo ${OgreBotAPI.IM.IsRunning}
```

### `Mode`

`${OgreBotAPI.IM.Mode}`

The Inventory Manager mode working right now: depot, sell, destroy, tse, restock, trade, quiver or withdraw (a depot withdraw from anywhere). It reads chain when only a chain is busy between modes, and empty when idle.

**Returns:** string: the busy mode's name, "chain", or "" when nothing is running.

```text
echo ${OgreBotAPI.IM.Mode}
```

### `Status`

`${OgreBotAPI.IM.Status}`

One line saying what the Inventory Manager is doing, the same line `echo ${OgreBotAPI.IM}` prints. It reads "closed", "open, idle", "open, running sell", "open, running withdraw" or "closed (running headless), running restock", with "; will close when finished (-end)" added while -end is armed.

**Returns:** string: the status line, such as "open, idle" or "closed".

```text
echo ${OgreBotAPI.IM.Status}
```

## Methods

### `Chain`

`OgreBotAPI.IM:Chain[fw, words...]`

Prints what each -&lt;mode> flag expands to. `reload` reads the chain defaults from disk again.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `words...` | string |  | reload. Optional. |

```text
OgreBotAPI.IM:Chain[all,reload]
```

### `Close`

`OgreBotAPI.IM:Close[fw]`

Closes the Inventory Manager window, clears a pending -end, and closes the merchant window unless a sell run is using it. It does not stop work that is running - use Stop for that.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.IM:Close[${Me.Name}]
```

### `Console`

`OgreBotAPI.IM:Console[fw, word]`

The window's activity log: always, running or never sets when the strip shows, and clear empties it. With no word it prints the setting and how many lines it holds.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `word` | string |  | always, running, never or clear. Optional. |

```text
OgreBotAPI.IM:Console[all,running]
```

### `Depot`

`OgreBotAPI.IM:Depot[fw, words...]`

Runs the depot mode, deposits into the nearest house or guild hall depots, and brings the window up; with no flags it runs the line saved on the Depot tab, or warns if nothing is saved. The words after it are read as one `ogre im` line, so `ogre im depot status` is `ogre im status`.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `words...` | string |  | The depot flags, one argument each, such as -harvest all -nearestdepot. `ogre im help` lists them. Optional. |

```text
OgreBotAPI.IM:Depot[all,-harvest,all,-nearestdepot]
```

### `Destroy`

`OgreBotAPI.IM:Destroy[fw, words...]`

The destroy mode: with no words, or flags first, it brings the window up and destroys what is on the destroy list; a name or an item id destroys that one item. The other first words are in the param.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `words...` | string |  | stop, status, reload, preview (or plan), list [all], add &lt;name> or remove &lt;name>; or flags; or an item. One argument each. Optional. |

```text
OgreBotAPI.IM:Destroy[all,preview]
```

### `End`

`OgreBotAPI.IM:End[fw]`

Stops whatever the Inventory Manager is running and closes the window, the same as `ogre end im` and the window's X. It stops first, so a script polling IsOpen never reads FALSE while work is still going.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.IM:End[all]
```

### `Examine`

`OgreBotAPI.IM:Examine[fw, box]`

Fills the named box of the window with the item in the open item examine window; you still pick the quantity and add it. It warns when no item examine window is open.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `box` | string |  | restock or trade: the tab whose box it fills. |

```text
OgreBotAPI.IM:Examine[all,restock]
```

### `Flags`

`OgreBotAPI.IM:Flags[fw, words...]`

Takes the words no other method spells: a line wholly of mode flags is a chain, run in that order, with -end to close the window when it finishes. Any other line goes to the depot parser, which says what it cannot read.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `words...` | string |  | The line, one argument each. |

```text
OgreBotAPI.IM:Flags[all,-destroy,-tse,-end]
```

### `Help`

`OgreBotAPI.IM:Help[fw]`

Prints the `ogre im` usage to the console: the depot flags, every other mode, chains, the queue and the settings.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.IM:Help[all]
```

### `Open`

`OgreBotAPI.IM:Open[fw]`

Opens the Inventory Manager window on the characters named; calling it while the window is up just refreshes it. If the UI host is not available it prints a warning and IsOpen stays FALSE.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.IM:Open[${Me.Name}]
```

### `Pane`

`OgreBotAPI.IM:Pane[fw, words...]`

Builds the editor list for a tab and prints how many rows it holds: sell or destroy, destroy when no name is given. `sell reopen` opens the merchant again first if its window is shut, as the Sell list tab's Refresh button does.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `words...` | string |  | The tab name, then reopen for sell. Optional. |

```text
OgreBotAPI.IM:Pane[all,destroy]
```

### `Probe`

`OgreBotAPI.IM:Probe[fw]`

Prints what the open depot's tier dropdown holds, for checking a depot window against the depot tables. It changes nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.IM:Probe[all]
```

### `Queue`

`OgreBotAPI.IM:Queue[fw, mode]`

Adds a mode to the run queue and brings the window up: it runs when the current work finishes. With no mode it prints what is waiting, and a word that is not a mode is refused.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `mode` | string |  | depot, sell, destroy, tse, restock, trade or quiver. Optional. |

```text
OgreBotAPI.IM:Queue[all,sell]
```

### `Reload`

`OgreBotAPI.IM:Reload[fw]`

Reloads the depot tables from disk: the depot kinds, the ammo rows and the shared resource table.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.IM:Reload[all]
```

### `Restock`

`OgreBotAPI.IM:Restock[fw, words...]`

The restock mode: with no words, or a profile name, it brings the window up and tops up from the depots, and -forwho &lt;expr> runs it only on the characters named. A word short of its arguments is read as a profile name.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `words...` | string |  | A profile, or one of stop, status, reload, list (or profiles), show &lt;profile>, preview (or plan) [profile], set &lt;profile> &lt;qty> &lt;item>, forwho &lt;profile> &lt;who> &lt;item>, drop &lt;profile> &lt;item>. Optional. |

```text
OgreBotAPI.IM:Restock[all,"Raid night",-forwho,${Me.Name}]
```

### `Sell`

`OgreBotAPI.IM:Sell[fw, words...]`

The sell mode: with no words it brings the window up and sells what is on the sell list, opening a nearby merchant if none is open. The other first words are in the param; any other words go to the run.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `words...` | string |  | stop, status, reload, preview (or plan), list [all], add &lt;name> or remove &lt;name>, then its arguments. Optional. |

```text
OgreBotAPI.IM:Sell[all,preview]
```

### `Settings`

`OgreBotAPI.IM:Settings[fw, words...]`

With no words, prints the saved settings; too few words prints the usage and changes nothing. Otherwise it changes one setting, as the param says.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `words...` | string |  | One of: bag &lt;tse\|destroy> &lt;1-6\|overseer\|harvest\|sharedtradeskill> &lt;on\|off>; tse &lt;option> &lt;on\|off\|number>; quiver &lt;arrow\|bolt\|throwing> &lt;name\|clear\|examine>; depot &lt;flags>; reload. One argument each. Optional. |

```text
OgreBotAPI.IM:Settings[all,tse,minlevel,120]
```

### `Status`

`OgreBotAPI.IM:Status[fw]`

Prints the session line to the console, then the chain if one runs and one summary line each for depot, sell, destroy, restock and trade. For one line a script can read, use ${OgreBotAPI.IM.Status}.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.IM:Status[all]
```

### `Stop`

`OgreBotAPI.IM:Stop[fw]`

Stops whatever the Inventory Manager is running (the chain, every busy mode, or a depot withdraw still in flight) and leaves the window open. When nothing is running it prints "im: nothing is running." to the console.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |

```text
OgreBotAPI.IM:Stop[igw:${Me.Name}]
```

### `Trade`

`OgreBotAPI.IM:Trade[fw, words...]`

The trade mode: with no words it brings the window up and runs the queue. The other first words are in the param.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `words...` | string |  | add &lt;player> &lt;qty\|all> &lt;item>, remove &lt;n> (or delete), list, clear, preview (or plan), status or stop, then its arguments. Optional. |

```text
OgreBotAPI.IM:Trade[all,add,Tobbin,5,"Rare Ore"]
```

### `Transmute`

`OgreBotAPI.IM:Transmute[fw, words...]`

Brings the window up and transmutes one named item, or an item by id.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `words...` | string |  | The item name or id. A name may be several arguments; they are joined with spaces. |

```text
OgreBotAPI.IM:Transmute[all,"Rusted Greatsword"]
```

### `Tse`

`OgreBotAPI.IM:Tse[fw, words...]`

The transmute, salvage and extract mode: `stop` stops it, and anything else brings the window up and runs. It starts from the options saved on the TSE tab, and flags such as -salvage or -stopafter 5 change that run.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | [for-who](ForWho.md): this runs only when this character is one it names |
| `words...` | string |  | stop, or the run's flags, one argument each. Optional. |

```text
OgreBotAPI.IM:Tse[all,-stopafter,5]
```
