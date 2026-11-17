# ISXOgreEQ2.Perf

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../../index.md).
</div>

## Methods

### `Measure`

`ISXOgreEQ2.Perf:Measure[seconds,nothreads]`

Measures the frame rate and what uses each frame for a number of seconds, then prints a report to the console and the log file - the same as ogre perf. The capture starts on the next frame; if one is already running, or a word other than a number or nothreads is given, it prints a line and measures nothing.

| Parameter | Type | Default | Meaning |
|---|---|---|---|
| `seconds` | int | `10` | how long to measure, 3 to 120 (values outside are clamped) |
| `nothreads` | string | `""` | the word nothreads turns off the per-thread breakdown; it may come before or after the seconds |

```text
ISXOgreEQ2.Perf:Measure[30]
```

### `Status`

`ISXOgreEQ2.Perf:Status`

Prints one console line saying whether a measurement is idle, about to start, or running with the seconds done and left - the same as ogre perf status.

```text
ISXOgreEQ2.Perf:Status
```

### `Stop`

`ISXOgreEQ2.Perf:Stop`

Ends a running measurement early and prints the report for what was measured, or cancels one that has not started yet - the same as ogre perf stop. With nothing running it prints that nothing is being measured.

```text
ISXOgreEQ2.Perf:Stop
```
