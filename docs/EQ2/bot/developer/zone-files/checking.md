# Check your file

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../index.md).
</div>

## Checking your file

Press **Reload** after every change. A file with a problem is **not valid**: it still shows in the IC window's zone
list, but in **red** with a *not valid* chip, and it cannot be queued or run. Click it, and the bar under the list
gives every problem at once; hovering the row shows them too. `ogre ic reload` in the console prints the same, one
line per problem, like this:

```
custom/My Zone.json: steps[3]: path: `using` must be "campspot" or "nav"
```

The most common one on a file written before October 2026 is the missing way out - add a `zoneOut` step
([The way out](how-it-runs.md#the-way-out)). A file that is not even valid JSON is listed by its file name, as "not valid JSON".

`steps[3]` is the third step in `steps`; a step inside a loop shows as `steps[5].steps[1]`.

Some things only **warn**: the file still loads, but read the warning. The most common is a key nothing reads, which
is usually a typo:

```
custom/My Zone.json: steps[3]: path: 'spotLimitMS' is not a field of this action - nothing reads it, so as written it does nothing - did you mean 'spotLimitMs'?
```

Two mistakes are not caught when the file loads: a misspelt condition (in `when`, `wait` or `until`), and two
steps with the same `stepId`. So watch the log the first time a new file runs.

## Checklist

- [ ] `zone` and `variants` match what the game shows for the zone.
- [ ] Every named step has a `stepId` (`named1`, `named2`, ...), and the steps that go with it are named after it
      (`named1.walk`, `named1.chest`).
- [ ] The last boss has `"boss": true`.
- [ ] The file has an `entrance`.
- [ ] The file has a `zoneOut` step: `auto`, or `door` with the exit's name.
- [ ] **Reload** says `0 skipped, 0 warning(s)`.
