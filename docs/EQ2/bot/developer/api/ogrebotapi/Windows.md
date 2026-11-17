# OgreBotAPI.Windows

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Members

### `CastingWindowVisible`

`${OgreBotAPI.Windows.CastingWindowVisible}`

Whether the game's casting bar is on screen. Always FALSE while you are not in the world.

**Returns:** bool: TRUE when the casting bar is visible; FALSE when it is hidden or you are not in the world.

```text
echo ${OgreBotAPI.Windows.CastingWindowVisible}
```

*Was (OldBot):* `OgreBotAPI.IsCastingWindowVisible`

### `ReplyExists`

`${OgreBotAPI.Windows.ReplyExists[text]}`

Which reply of the open reply dialog (the window a clicked item or object opens) contains the text, in any case. It answers a number, not TRUE/FALSE, so test it with > 0; it does not look at the NPC conversation window.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `text` | string |  | Text to look for inside each reply. Matches anywhere in the reply, any case. |

**Returns:** int: the 1-based number of the first reply that contains the text; 0 when no reply dialog is open, nothing matches, or the text is empty.

```text
echo ${OgreBotAPI.Windows.ReplyExists[Yes]}
```

*Was (OldBot):* `OgreBotAPI.ReplyDialog_ReplyExists`

### `RewardID`

`${OgreBotAPI.Windows.RewardID[num|name,windowId]}`

The number of one reward on a reward window, picked by number or by item name the same way AcceptReward picks it. A number past the window's reward count, a name that matches no row, an empty selection, or no reward window all answer 0.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `num\|name` | number or text |  | The reward to pick: its number on the window (1 = the first), or its item name (trimmed, any case, first match). Empty or 0 picks nothing. |
| `windowId` | int | `0` | The reward window id to read. Empty or 0 = the active reward window (the oldest one the bot saw open that is still up). |

**Returns:** int: the 1-based reward number; 0 when there is no reward window or nothing matches.

```text
echo ${OgreBotAPI.Windows.RewardID[2,0]}
```

*Was (OldBot):* `OgreBotAPI.Get_RewardID`

### `RewardLinkID`

`${OgreBotAPI.Windows.RewardLinkID[num|name,windowId]}`

The LinkID of one reward on a reward window, picked by number or by item name the same way AcceptReward picks it. Empty when there is no reward window, nothing matches, or the game has no LinkID for that row.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `num\|name` | number or text |  | The reward to pick: its number on the window (1 = the first), or its item name (trimmed, any case, first match). Empty or 0 picks nothing. |
| `windowId` | int | `0` | The reward window id to read. Empty or 0 = the active reward window (the oldest one the bot saw open that is still up). |

**Returns:** string: that reward's LinkID; empty when there is no window or no match.

```text
echo ${OgreBotAPI.Windows.RewardLinkID[1,0]}
```

*Was (OldBot):* `OgreBotAPI.Get_RewardLinkID`

### `RewardName`

`${OgreBotAPI.Windows.RewardName[num|name,windowId]}`

The item name of one reward on a reward window, picked by number or by item name. Empty when there is no reward window, nothing matches, or the row does not read.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `num\|name` | number or text |  | The reward to pick: its number on the window (1 = the first), or its item name (trimmed, any case, first match). Empty or 0 picks nothing. |
| `windowId` | int | `0` | The reward window id to read. Empty or 0 = the active reward window (the oldest one the bot saw open that is still up). |

**Returns:** string: that reward's item name; empty when there is no window or no match.

```text
echo ${OgreBotAPI.Windows.RewardName[1,0]}
```

*Was (OldBot):* `OgreBotAPI.Get_RewardName`

### `RewardWindowID`

`${OgreBotAPI.Windows.RewardWindowID}`

The id of the active reward window: the oldest reward window the bot saw open that is still up, or with none held, the one open now. It reads 0 when no reward window is up.

**Returns:** int64: the active reward window's id; 0 when none is open or you are not in the world.

```text
echo ${OgreBotAPI.Windows.RewardWindowID}
```

*Was (OldBot):* `OgreBotAPI.RewardWindow_Get_WindowID`

### `SelectOption`

`${OgreBotAPI.Windows.SelectOption[n]}`

Which option of the open select window matches, without clicking anything and without printing anything, so a script may read it as often as it likes. Options count from 1 (OldBot's numbers were one higher).

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `search...` | number or text |  | The option to find: a number is that option's position; text must match the option name exactly (any case). Add -substring as another argument to match text anywhere in the name. |

**Returns:** int: the 1-based option position; 0 when no select window is open, nothing matches, or no argument is given.

```text
echo ${OgreBotAPI.Windows.SelectOption[1]}
```

*Was (OldBot):* `OgreBotAPI.Select_Window_GetOption`

## Methods

### `AcceptNoChoiceReward`

`OgreBotAPI.Windows:AcceptNoChoiceReward[fw, windowId=0]`

Presses Receive on a reward window that offers no choice. It refuses, with a console line, a window that offers a choice, a 'New Quest!' offer, or a window whose reward pack is not shown.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `windowId` | int | `0` | The reward window id. Empty or 0 = the active reward window (the oldest one the bot saw open that is still up). |

```text
OgreBotAPI.Windows:AcceptNoChoiceReward[${Me.Name},0]
```

*Was (OldBot):* `OgreBotAPI:AcceptNoChoiceReward`

### `AcceptReward`

`OgreBotAPI.Windows:AcceptReward[fw, num|name=0, windowId=0]`

Takes a reward from a reward window: on a choice window it accepts the reward you name, and on a single or no-choice window it presses Receive whatever you pass, but never on a 'New Quest!' offer. Each outcome, including no window or no match, prints a line to the console.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `num\|name` | number or text | `0` | The reward to take on a choice window: its number (1 = the first) or its item name (any case). Ignored on a single-reward window. |
| `windowId` | int | `0` | The reward window id. 0 = the active reward window (the oldest one the bot saw open that is still up). |

```text
OgreBotAPI.Windows:AcceptReward[${Me.Name},1,0]
```

*Was (OldBot):* `OgreBotAPI:AcceptReward`, `Obj_OgreIH:AcceptReward`

### `Choice`

`OgreBotAPI.Windows:Choice[fw, option=1]`

Clicks one of the choice window's buttons: 1 is the first button, 2 the second. Another number is clamped to the nearer of the two, with a console line saying which it chose; does nothing when no choice window is open.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `option` | int | `1` | Which button to click: 1 or 2 (below 1 is 1, above 2 is 2). |

```text
OgreBotAPI.Windows:Choice[${Me.Name},1]
```

*Was (OldBot):* `OgreBotAPI:ChoiceWindow`

### `Close`

`OgreBotAPI.Windows:Close[fw]`

Closes the top-most game window, exactly as the /close_top_window command does. Does nothing when you are not in the world.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.Windows:Close[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:CloseWindow`

### `CloseExamine`

`OgreBotAPI.Windows:CloseExamine[fw]`

Clicks the close button of the item examine window once. It closes one examine window per call, and it clicks even when none is open.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.Windows:CloseExamine[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:CloseAllExamine`, `OgreBotAPI:CloseExamineWindow`, `OgreBotAPI:CloseExamine`

### `DungeonMakerCancel`

`OgreBotAPI.Windows:DungeonMakerCancel[fw]`

Clicks Cancel on the Dungeon Maker save-rating window. It clicks only when that button is there and visible; with the window closed it does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.Windows:DungeonMakerCancel[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:DungeonMakerCancel`

### `F2PWindowCheck`

`OgreBotAPI.Windows:F2PWindowCheck[fw]`

Closes the game's All-Access membership offer window by clicking its Cancel button, and prints a line to the console when it does. Does nothing when that window is not up; it runs only when called, nothing watches for the window.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.Windows:F2PWindowCheck[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:F2PWindow_Check`

### `InputTextAccept`

`OgreBotAPI.Windows:InputTextAccept[fw]`

Clicks the first button of the choice window when that window is showing a text box (for example a password prompt). Does nothing when the text box is not visible.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.Windows:InputTextAccept[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:InputTextWindow_Accept`

### `InputTextAdd`

`OgreBotAPI.Windows:InputTextAdd[fw, text]`

Adds text to the end of the choice window's text box, after whatever is already there; use InputTextClear first to replace it. Does nothing when the text box is not visible or the text is empty.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `text` | string |  | The text to add to the box. Quote it if it contains a comma. |

```text
OgreBotAPI.Windows:InputTextAdd[${Me.Name},"open sesame"]
```

*Was (OldBot):* `OgreBotAPI:InputTextWindow_AddText`

### `InputTextClear`

`OgreBotAPI.Windows:InputTextClear[fw]`

Empties the choice window's text box. Does nothing when the text box is not visible.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.Windows:InputTextClear[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:InputTextWindow_ClearText`

### `OK`

`OgreBotAPI.Windows:OK[fw]`

Clicks the first button of the game's choice window (the pop-up with two buttons), but only when that button is visible. It does not touch any other window, and it does nothing when no choice window is up.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.Windows:OK[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:OK_Button`

### `ProvingGroundsExit`

`OgreBotAPI.Windows:ProvingGroundsExit[fw]`

Clicks Exit on the Proving Grounds score window. It clicks only when that button is there and visible; with the window closed it does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.Windows:ProvingGroundsExit[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:ProvingGrounds_Exit`

### `ProvingGroundsScoreboardClose`

`OgreBotAPI.Windows:ProvingGroundsScoreboardClose[fw]`

Clicks the close button of the Proving Grounds leaderboard window. It clicks only when that button is there and visible; with the window closed it does nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.Windows:ProvingGroundsScoreboardClose[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:ProvingGrounds_Scoreboard_Close`

### `Reply`

`OgreBotAPI.Windows:Reply[fw, number|text=1]`

Picks a reply in the open reply dialog (the window a clicked item or object opens): a number picks that reply, text picks the first reply that contains it in any case. When no dialog is open or nothing matches, nothing is clicked and a warning listing the replies goes to the console.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `number\|text` | number or text | `1` | A reply number (1 = the first), or text to find inside a reply (any case). |

```text
OgreBotAPI.Windows:Reply[${Me.Name},1]
```

*Was (OldBot):* `OgreBotAPI:ReplyDialog`, `ReplyDialog`

### `ReplyClose`

`OgreBotAPI.Windows:ReplyClose[fw]`

Closes the open reply dialog. Does nothing, silently, when no reply dialog is open.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.Windows:ReplyClose[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:ReplyDialogClose`

### `Select`

`OgreBotAPI.Windows:Select[fw, search...]`

Picks an option in the open select window and then presses its OK. The match happens at once but the clicks are queued: the option first, then OK about 0.3 seconds later; each pick and each miss prints a line to the console.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `search...` | number or text |  | The option to pick: a number is its position (1 = the first real option); text must match the option name exactly, any case. Flags may come before or after it as their own arguments: -substring (match text anywhere in the name), -test (click the option but not OK), -reportonly (say which option matches, click nothing) and -spew (list the options). |

```text
OgreBotAPI.Windows:Select[${Me.Name},1]
```

*Was (OldBot):* `OgreBotAPI:Select_Window`

### `SelectCancel`

`OgreBotAPI.Windows:SelectCancel[fw]`

Clicks Cancel on the open select window. Does nothing, silently, when the Cancel button is not visible.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.Windows:SelectCancel[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Select_Window_Cancel`

### `SelectSpew`

`OgreBotAPI.Windows:SelectSpew[fw]`

Prints every option of the open select window to the console, numbered from 1, with the row template it found. Prints a 'no select window open' line instead when there is none.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.Windows:SelectSpew[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:Select_Window_Spew`

### `ShowConsole`

`OgreBotAPI.Windows:ShowConsole[fw, on=TRUE]`

Opens the OgreConsole window, or closes it for a no word (FALSE, 0, no or off). Empty, a yes word, or any other word opens it, so a typo never closes the console.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `on` | bool | `TRUE` | FALSE, 0, no or off closes the console; anything else, empty included, opens it. |

```text
OgreBotAPI.Windows:ShowConsole[${Me.Name},TRUE]
```

*Was (OldBot):* `OgreBotAPI:ShowOgreConsole`

### `SpewRewardWindowIDs`

`OgreBotAPI.Windows:SpewRewardWindowIDs[fw]`

Prints every reward window id the bot has seen open, oldest first, and whether each is still up. It keeps at most the last 16 windows.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.Windows:SpewRewardWindowIDs[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:RewardWindow_Spew_WindowIDs`

### `ToggleConsole`

`OgreBotAPI.Windows:ToggleConsole[fw, value=toggle]`

Flips the OgreConsole window between open and closed. A yes word (TRUE, 1, yes, on) always opens it and a no word (FALSE, 0, no, off) always closes it.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |
| `value` | string | `toggle` | TRUE opens, FALSE closes, anything else (or nothing) flips. |

```text
OgreBotAPI.Windows:ToggleConsole[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:ToggleConsoleWindow`

### `ToggleMain`

`OgreBotAPI.Windows:ToggleMain[fw]`

Hides the main OgreBot window if it is shown, or shows it if it is hidden. It does not close OgreBot, and it does nothing when OgreBot is not open.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `fw` | for-who |  | for-who: which characters this runs on |

```text
OgreBotAPI.Windows:ToggleMain[${Me.Name}]
```

*Was (OldBot):* `OgreBotAPI:ToggleMainWindow`
