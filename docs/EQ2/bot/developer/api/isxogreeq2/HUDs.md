<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

# ISXOgreEQ2.HUDs

## Members

### `Diag`

`${ISXOgreEQ2.HUDs.Diag}`

One diagnostic line about the on-screen HUD overlay: whether it is open, which HUD parts are switched on, whether you are in a raid, whether the group or raid part is the one showing, how many updates it has sent and whether the UI host is up. Reading it does one game read and changes nothing.

**Returns:** string: space-separated key=value pairs describing the HUD overlay's state.

```text
echo ${ISXOgreEQ2.HUDs.Diag}
```

## Methods

### `Authorized`

`ISXOgreEQ2.HUDs:Authorized[names]`

Replaces the list of character names the HUD's nearest-player alert ignores with one comma-separated list; names match in any case. No argument, or an empty one, clears the list (your group and raid never set the alert off anyway).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `names` | string | `""` | character names separated by commas, no spaces |

```text
ISXOgreEQ2.HUDs:Authorized["Bob,Alice"]
```

### `Close`

`ISXOgreEQ2.HUDs:Close`

Closes the on-screen HUD overlay and leaves the switched-on parts as they are. Setting a raid message line or switching a HUD part on later opens it again.

```text
ISXOgreEQ2.HUDs:Close
```

### `Open`

`ISXOgreEQ2.HUDs:Open`

Opens the on-screen HUD overlay - a click-through layer that shows the nearest NPC, group or raid member distances and the raid message lines, for the parts that are switched on. If its files cannot be read or the UI host is not up it stays closed and only the log says why.

```text
ISXOgreEQ2.HUDs:Open
```

### `Set`

`ISXOgreEQ2.HUDs:Set[key,value]`

Sets one HUD overlay setting by key: a part on or off, a display option, or a position. Switching the npc, group, raid or raidopts part on opens the overlay if it is closed, switching one off never closes it, and an unknown key is ignored.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `key` | string |  | parts (on/off): npc, group, raid, raidopts; options (on/off): hidename, hidecasting, grouphidename, grouphidecasting, raidonly; positions and spacing (numbers): npcx, npcy, groupx, groupy, groupinc, raidx, raidy, raidinc, raidspacer, raidgap, raidoptx, raidopty, raidoptinc; namewidth and groupnamewidth (1-40, the raid and group name column width). Case does not matter |
| `value` | string |  | 1, TRUE or on to switch on (anything else is off), or the number for a position key |

```text
ISXOgreEQ2.HUDs:Set[group,TRUE]
```

### `SetOption`

`ISXOgreEQ2.HUDs:SetOption[slot,text,displaySecs,removeSecs,minUpdateSecs]`

Writes one raid message line on the HUD overlay, with an optional countdown after the text, and removes it after removeSecs; minUpdateSecs then makes the line ignore further writes for that long. A non-empty text opens the overlay if it is closed and empty text blanks the line; a slot outside 1-10 is ignored, and a call without a slot and text prints one usage line.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `slot` | int |  | which raid message line, 1 to 10 |
| `text` | string |  | the text to show; empty blanks the line |
| `displaySecs` | int | `0` | seconds of countdown shown after the text; 0 shows no countdown |
| `removeSecs` | int | `30` | seconds until the line is removed; 0 or less means 30 |
| `minUpdateSecs` | int | `0` | seconds the line ignores further writes (an empty write still clears it); 0 or less means no lock |

```text
ISXOgreEQ2.HUDs:SetOption[1,"Next add in:",20,25]
```

### `Test`

`ISXOgreEQ2.HUDs:Test[on]`

TRUE loads five demo raid message lines (10 s countdown, gone after 15 s) at once, opening the overlay if it is closed; FALSE, or no argument, clears all ten lines if the demo was loaded. A second TRUE does nothing until a FALSE in between.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `on` | bool | `FALSE` | 1, TRUE or on loads the demo lines; anything else clears them |

```text
ISXOgreEQ2.HUDs:Test[TRUE]
```
