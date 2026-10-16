# ISXOgre (the old extension)

<div class="ogre-beta" markdown>
**OgreBot is in beta testing.** Looking for OgreBot Classic? [Click here](../../../index.md).
</div>

Everything Classic's *ISXOgre API Reference* page described (except the detrimentals, which have [their own page](detrimentals.md)), and what each one is in the new bot.

> **:warning: The old extension is not loaded with the new bot**
>
> Every `${ISXOgre.…}` read gives `NULL` and every `ISXOgre:` call does nothing. Find your name below and write what the row says instead.

## At a glance

| What happened | Names |
|---|---|
| ⚠️ Arguments changed | 1 |
| ✏️ Renamed | 5 |
| ➡️ Moved | 2 |
| ➡️ Lives somewhere else | 10 |
| ⛔ Not ported yet | 29 |
| ⛔ Removed | 30 |
| **Total** | **77** |

## Worked examples

One real Classic line per kind of change, and the line that replaces it.

### ⚠️ Arguments changed: `ISXOgre.Username`

```
; before (Classic)
switch ${ISXOgre.Username[1,2,3]}
; after (new bot)
switch ${ISXOgreEQ2.Auth.Username}
```

### ✏️ Renamed: `ISXOgre.IsReady`

```
; before (Classic)
while !${ISXOgre.IsReady}
; after (new bot)
while !${ISXOgreEQ2.Auth.Authorized}
```

### ➡️ Moved: `ISXOgre.MD5`

```
; before (Classic)
return "${ISXOgre.MD5["${_Input}"]}"
; after (new bot)
return "${OgreBotAPI.Util.MD5["${_Input}"]}"
```

## ISXOgre

**Note A** (8 rows below): Nearest tier-0 reads: ${ISXOgreEQ2.Auth.Authorized} (signed in at all), ${ISXOgreEQ2.Auth.AccessLevel} (tier text), ${ISXOgreEQ2.Auth.AccessLevelNum} (number). No code maps those to client/tester/elite/all, so do not translate the flag to a threshold by guess.

| Old call | Today | Write instead | What changed | Notes |
|---|---|---|---|---|
| `command:OgreA` | does nothing | — | ⛔ Removed | Old: registered /; its handler already returned at once in Classic - "With 64 bit this is retired unless people want it again". Nothing to port. Public doc: NOT in. |
| `command:OgreBotAtom` | does nothing | — | ⛔ Removed | Each atom has its own replacement - usually the matching `oc !c -<Verb>` console row or OgreBotAPI method. Where each Classic atom user was routed: section 7.2. |
| `ISXOgre.Base64Decode` | does nothing | — | ⛔ Not ported yet | Old: returns the decoded text of a jsonvalue's scalar (outer quotes stripped) or of the literal argument. Public doc: YES - (Base64Decode - Member). |
| `ISXOgre.Base64DecodeString` | does nothing | — | ⛔ Not ported yet | Old: returns the base64-decoded argv[0] taken by value. Public doc: NOT in. |
| `ISXOgre.Base64Encode` | does nothing | — | ⛔ Not ported yet | Old: returns base64 of a jsonvalue's JSON (jsonvalue arg) or of the literal argument text. Public doc: YES - (Base64Encode - Member). |
| `ISXOgre.Base64EncodeString` | does nothing | — | ⛔ Not ported yet | Old: returns base64 of argv[0] taken by value. Public doc: NOT in. |
| `ISXOgre.CleanString` | does nothing | — | ⛔ Not ported yet | Old: returns a filename-safe token: space -&gt; _, strips, [ ]: ' ` and / \ * ? " &lt; &gt; \|. Classic uses it to build the server key for tradeskill exports. Public doc: NOT in. |
| `ISXOgre.DevBuild` | does nothing | — | ⛔ Not ported yet | Old: returns gISXOGRE_DEVELOPMENT_VERSION, a compile-time dev-build flag; Classic reads it in to pick the dev or live revision. Public doc: NOT in. |
| `ISXOgre.HasOgreBotAccessAll` | does nothing | — | ⛔ Removed | Note A |
| `ISXOgre.HasOgreBotAccessClient` | does nothing | — | ⛔ Removed | Note A |
| `ISXOgre.HasOgreBotAccessElite` | does nothing | — | ⛔ Removed | Note A |
| `ISXOgre.HasOgreBotAccessTester` | does nothing | — | ⛔ Removed | Note A |
| `ISXOgre.HasOgreCraftAccessAll` | does nothing | — | ⛔ Removed | Note A |
| `ISXOgre.HasOgreCraftAccessClient` | does nothing | — | ⛔ Removed | Note A |
| `ISXOgre.HasOgreCraftAccessElite` | does nothing | — | ⛔ Removed | Note A |
| `ISXOgre.HasOgreCraftAccessTester` | does nothing | — | ⛔ Removed | Note A |
| `ISXOgre.HttpLastSubmitError` | does nothing | — | ⛔ Not ported yet |  |
| `ISXOgre.HttpRequest` | does nothing | — | ⛔ Not ported yet |  |
| `ISXOgre.HttpRequestSubmit` | does nothing | — | ⛔ Not ported yet |  |
| `ISXOgre.IsCommand` | does nothing | — | ⛔ Not ported yet | Old: returns bool pISInterface-&gt;ResolveCommand(argv[0]) - is this a known command/alias. Classic site:. Public doc: NOT in. |
| `ISXOgre.IsPatching` | does nothing | `ogre patch status` | ➡️ Lives somewhere else | A script reads it as ${ISXOgreX.Patch.InProgress} (core TLO). |
| `ISXOgre.IsReady` | does nothing | `ISXOgreEQ2.Auth.Authorized` | ✏️ Renamed | Old answered NULL (no object) when not ready; new answers FALSE. `!${...}` and `wait N ${...}` behave the same; a `(exists)` test does not - it is always TRUE now. |
| `ISXOgre.MD5` | does nothing | `OgreBotAPI.Util.MD5` | ➡️ Moved |  |
| `ISXOgre.PatchVersion` | does nothing | `ogre patch status` | ➡️ Lives somewhere else | ReleaseId is a STRING, not an int - a numeric compare against it is meaningless. |
| `ISXOgre.ResolveCommand` | does nothing | — | ⛔ Not ported yet | Old: returns the text a command/alias resolves to (pISInterface-&gt;ResolveCommand), NULL if none. No Classic call sites. Public doc: NOT in. |
| `ISXOgre.SkinName` | does nothing | — | ⛔ Removed | Old: returns cISXConfig.SkinName, the LGUI skin every Classic window loads with `ui -reload -skin ${ISXOgre.SkinName}`. The new bot has no LGUI layer: "We do NOT use the ISUI (LGUI) layer in this extension"; its windows are Ultralight HTML through ${ISXOgreX.UI}. Public doc: NOT in. |
| `ISXOgre.TimeUTC` | does nothing | — | ⛔ Not ported yet | Old: returns float64 seconds since the Unix epoch (time(nullptr)). Classic's only site is commented out. Public doc: NOT in. |
| `ISXOgre.Username` | does nothing | `ISXOgreEQ2.Auth.Username` | ⚠️ Arguments changed | Drop the [1,2,3] - the new member needs no key (it does not read argc, so passing it is harmless but meaningless). Before auth it answers an empty string, not NULL. |
| `ISXOgre.Version` | does nothing | `ISXOgreEQ2.Version` | ➡️ Moved | The new bot is two extensions with two versions: ${ISXOgreEQ2.Version} is the EQ2 adapter, ${ISXOgreX.Version} the core. Treat the value as text. |
| `ISXOgre:Base64Decode` | does nothing | — | ⛔ Not ported yet | Old: decodes into a destination jsonvalue, restoring JSON shape when the payload is JSON. Public doc: YES - (Base64Decode - Method). |
| `ISXOgre:Base64Encode` | does nothing | — | ⛔ Not ported yet | Old: encodes into a destination jsonvalue: [jsonref] in place, [jsonref, jsonref2], or [string, jsonref]. Public doc: YES - (Base64Encode - Method). |
| `ISXOgre:DebugInfo` | does nothing | — | ⛔ Not ported yet | Old: calls outputDebugInfo: prints the InnerSpace install path, CWD, executable, IS build, session, virtual-input flag and extension hashes. Public doc: NOT in. |
| `ISXOgre:DITW` | does nothing | — | ⛔ Removed | Old: registered at but GetMethod has no case for it, so the call already did nothing in Classic. Public doc: NOT in. |
| `ISXOgre:FullScreen` | does nothing | — | ⛔ Not ported yet | Old: calls cISXOgreEQ2Config.Force_Full_Screen. Public doc: NOT in. |
| `ISXOgre:Generate` | does nothing | — | ⛔ Removed | Old: runs the embedded Generate script with the caller's args, used to fill LGUI combo boxes. The new bot has no LGUI layer: "We do NOT use the ISUI (LGUI) layer in this extension"; its windows are Ultralight HTML through ${ISXOgreX.UI}. Public doc: NOT in. |
| `ISXOgre:GenerateSessionNames` | does nothing | — | ⛔ Removed | Old: runs an embedded script that fills an LGUI listbox/combobox (argv[0] = its ID) with session names. The new bot has no LGUI layer: "We do NOT use the ISUI (LGUI) layer in this extension"; its windows are Ultralight HTML through ${ISXOgreX.UI}. Public doc: NOT in. |
| `ISXOgre:GenerateToonNames` | does nothing | — | ⛔ Removed | Old: runs an embedded script that fills an LGUI listbox/combobox (argv[0] = its ID) with toon names. The new bot has no LGUI layer: "We do NOT use the ISUI (LGUI) layer in this extension"; its windows are Ultralight HTML through ${ISXOgreX.UI}. Public doc: NOT in. |
| `ISXOgre:GenerateUplinkNames` | does nothing | — | ⛔ Removed | Old: runs an embedded script that fills an LGUI listbox/combobox (argv[0] = its ID) with uplink names. The new bot has no LGUI layer: "We do NOT use the ISUI (LGUI) layer in this extension"; its windows are Ultralight HTML through ${ISXOgreX.UI}. Public doc: NOT in. |
| `ISXOgre:OgreConsole` | does nothing | — | ⛔ Removed | Sending a console line in the new bot is `oc` / ISXOgreX.Console:Send. |
| `ISXOgre:OgreIRC` | does nothing | — | ⛔ Removed | The new IRC door is `ogre irc`. |
| `ISXOgre:OgreIRCTest` | does nothing | — | ⛔ Removed | Old: is marked "OLD DOES NOT WORK NO LONGER USED" and returns false before executing. Public doc: NOT in. |
| `ISXOgre:Patch` | does nothing | `ogre patch` | ➡️ Lives somewhere else | Inside a script the same door is ISXOgreX.Patch:Run. |
| `ISXOgre:PatchDev` | does nothing | — | ⛔ Removed | Old: already did nothing in Classic - it prints "Development build is no longer being used" and returns before the patch code. Nothing to port. Public doc: NOT in. |
| `ISXOgre:PatchLive` | does nothing | `ogre patch` | ➡️ Lives somewhere else |  |
| `ISXOgre:ReportPing` | does nothing | `ogre sessions` | ➡️ Lives somewhere else | No call to make: every session's core now reports to the uplink on its own, every 5 s. See the uplink's table with `ogre sessions`. |
| `ISXOgre:ResetSkin` | does nothing | — | ⛔ Removed | Old: re-applies the LGUI2 skin (pExtension-&gt;SetLGUI2Skin). The new bot has no LGUI layer: "We do NOT use the ISUI (LGUI) layer in this extension"; its windows are Ultralight HTML through ${ISXOgreX.UI}. Public doc: NOT in. |
| `ISXOgre:SetFormBodyB64` | does nothing | — | ⛔ Not ported yet |  |
| `ISXOgre:SetSkinFile` | does nothing | — | ⛔ Removed | Old: loads an LGUI skin file (cISXConfig.SetSkin). The new bot has no LGUI layer: "We do NOT use the ISUI (LGUI) layer in this extension"; its windows are Ultralight HTML through ${ISXOgreX.UI}. Public doc: NOT in. |
| `ISXOgre:SetSkinName` | does nothing | — | ⛔ Removed | Old: sets cISXConfig.SkinName (what ${ISXOgre.SkinName} answers). The new bot has no LGUI layer: "We do NOT use the ISUI (LGUI) layer in this extension"; its windows are Ultralight HTML through ${ISXOgreX.UI}. Public doc: NOT in. |
| `ISXOgre:Test` | does nothing | — | ⛔ Removed | Old: - the whole body is commented out; it returns false and does nothing. Public doc: NOT in. |
| `ISXOgre:TestIndex` | does nothing | — | ⛔ Removed | Old: is a developer sample of writing into a caller's index variable, "kept as a working sample". Not a feature; nothing in the new bot. Public doc: NOT in. |
| `ISXOgre:TestJSON` | does nothing | — | ⛔ Removed | Not a feature; nothing in the new bot. Public doc: NOT in. |
| `ogrehttpjob.Body` | does nothing | — | ⛔ Not ported yet | Old: returns the response body for the handle's job id. Public doc: YES - (ogrehttpjob Members). |
| `ogrehttpjob.Complete` | does nothing | — | ⛔ Not ported yet | Old: returns TRUE iff Completed or Failed for the handle's job id. Public doc: YES - (ogrehttpjob Members). |
| `ogrehttpjob.Error` | does nothing | — | ⛔ Not ported yet | Old: returns the libcurl error text for the handle's job id. Public doc: YES - (ogrehttpjob Members). |
| `ogrehttpjob.Exists` | does nothing | — | ⛔ Not ported yet | Old: returns TRUE iff a job record exists for the handle's job id. Public doc: YES - (ogrehttpjob Members). |
| `ogrehttpjob.ID` | does nothing | — | ⛔ Not ported yet | Old: returns the job id for the handle's job id. Public doc: YES - (ogrehttpjob Members). |
| `ogrehttpjob.Ok` | does nothing | — | ⛔ Not ported yet | Old: returns TRUE iff Completed and 2xx for the handle's job id. Public doc: YES - (ogrehttpjob Members). |
| `ogrehttpjob.State` | does nothing | — | ⛔ Not ported yet | Old: returns "Pending"/"Completed"/"Failed"/"None" for the handle's job id. Public doc: YES - (ogrehttpjob Members). |
| `ogrehttpjob.Status` | does nothing | — | ⛔ Not ported yet | Old: returns the HTTP status code for the handle's job id. Public doc: YES - (ogrehttpjob Members). |
| `ogrehttpjob:Release` | does nothing | — | ⛔ Not ported yet | Old: frees the job slot (OgreHttp::Release). Public doc: YES - (ogrehttpjob Methods). |
| `OgreOSA.Debug` | does nothing | — | ⛔ Not ported yet | Old: returns the OSA debug-log flag. New OSA: ${ISXOgreEQ2.OSA} registers only Open / Close / Target and has no members. Its settings are read from the OgreBot option store every pulse while the OSA is wanted. Public doc: no. |
| `OgreOSA.Enabled` | does nothing | `OgreBotAPI.Options.Value` | ➡️ Lives somewhere else | There is no read of the OSA window's own open state; ${OgreBotAPI.Options.Value[checkbox_settings_enableonscreenassistant]} is the setting it follows. A window opened by hand with `ogre osa` while the box is unticked does not show up in it. |
| `OgreOSA.ScanRadius` | does nothing | `OgreBotAPI.Options.Value` | ➡️ Lives somewhere else | The option is stored as text; the OSA clamps it to 200 and keeps its default of 50 when the option is missing. |
| `OgreOSA.TargetsOnly` | does nothing | `OgreBotAPI.Options.Value` | ➡️ Lives somewhere else | Read ${OgreBotAPI.Options.Value[checkbox_osa_targetsonly]}. |
| `OgreOSA:ClickingDone` | does nothing | `ISXOgreEQ2.OSA:Target` | ✏️ Renamed | See OgreOSA:DoTarget for the timing difference. |
| `OgreOSA:ClickingStart` | does nothing | — | ⛔ Removed | Old: is the LGUI listbox OnLeftDown hook (EQ2OgreCommon/OgreOnScreenAssistant/EQ2OgreOnScreenAssistantXML.xml:52) that holds the scan so the listbox does not rebuild under a click. The new bot has no LGUI layer: "We do NOT use the ISUI (LGUI) layer in this extension"; the Ultralight OSA window's click calls ISXOgreEQ2.OSA:Target directly, so there is no listbox to hold. Public doc: no. |
| `OgreOSA:DoTarget` | does nothing | `ISXOgreEQ2.OSA:Target` | ✏️ Renamed | Not deferred any more: do not call it from inside a UI event callback. |
| `OgreOSA:LoadConfig` | does nothing | — | ⛔ Removed | Old: re-pulls the OSA filters from OgreBot; Classic calls it after every OSA option change. New: nothing to call - the new OgreBot pushes the OSA config every pulse while the OSA is wanted, so a changed option applies on its own. Public doc: no. |
| `OgreOSA:NoUpdate` | does nothing | — | ⛔ Removed | Old: - an isolation toggle: when TRUE a click targets WITHOUT arming the OgreBotAPI:UpdateNPCTarget nudge. New: OSA::Target only runs `target <id>` and logs it - there is no nudge to switch off. Public doc: no. |
| `OgreOSA:Set_ScanRadius` | does nothing | `OgreBotAPI.Options:Set` | ➡️ Lives somewhere else | OgreBotAPI.Options:Set[&lt;forwho&gt;,textentry_osa_radius,&lt;n&gt;] - for-who first. It changes the saved option; the OSA clamps to 200. |
| `OgreOSA:Set_TargetsOnly` | does nothing | `OgreBotAPI.Options:Set` | ➡️ Lives somewhere else | OgreBotAPI.Options:Set[&lt;forwho&gt;,checkbox_osa_targetsonly,TRUE] - for-who first, then the option id and value. It changes the saved option, not just the running OSA. |
| `OgreOSA:SetDebug` | does nothing | — | ⛔ Not ported yet | Old: [true\|false] turns OSA debug logging to a file on/off. Public doc: no. |
| `OgreOSA:Start` | does nothing | `ISXOgreEQ2.OSA:Open` | ✏️ Renamed |  |
| `OgreOSA:Stop` | does nothing | `ISXOgreEQ2.OSA:Close` | ✏️ Renamed |  |
| `OgreOSA:TargetMode` | does nothing | — | ⛔ Removed | Old: picks how a click targets (command/actor/timed/getmethod) - an A/B switch for isolating the LGUI click-&gt;target crash. New: one path, `target <id>` run from the command-queue drain. Public doc: no. |
| `OgreOSA:Update` | does nothing | — | ⛔ Not ported yet | Old: forces one scan now (OSA_RunScan). New: OSA::Pulse self-throttles to one scan per 200 ms; no registered method forces one. Public doc: no. |

## Not in the new bot yet

If your script needs one of these, leave it out for now and tell us - this list is what still needs work.

- `ISXOgre.Base64Decode` - not ported yet
- `ISXOgre.Base64DecodeString` - not ported yet
- `ISXOgre.Base64Encode` - not ported yet
- `ISXOgre.Base64EncodeString` - not ported yet
- `ISXOgre.CleanString` - not ported yet
- `ISXOgre.DevBuild` - not ported yet
- `ISXOgre.HttpLastSubmitError` - not ported yet
- `ISXOgre.HttpRequest` - not ported yet
- `ISXOgre.HttpRequestSubmit` - not ported yet
- `ISXOgre.IsCommand` - not ported yet
- `ISXOgre.ResolveCommand` - not ported yet
- `ISXOgre.TimeUTC` - not ported yet
- `ISXOgre:Base64Decode` - not ported yet
- `ISXOgre:Base64Encode` - not ported yet
- `ISXOgre:DebugInfo` - not ported yet
- `ISXOgre:FullScreen` - not ported yet
- `ISXOgre:SetFormBodyB64` - not ported yet
- `ogrehttpjob.Body` - not ported yet
- `ogrehttpjob.Complete` - not ported yet
- `ogrehttpjob.Error` - not ported yet
- `ogrehttpjob.Exists` - not ported yet
- `ogrehttpjob.ID` - not ported yet
- `ogrehttpjob.Ok` - not ported yet
- `ogrehttpjob.State` - not ported yet
- `ogrehttpjob.Status` - not ported yet
- `ogrehttpjob:Release` - not ported yet
- `OgreOSA.Debug` - not ported yet
- `OgreOSA:SetDebug` - not ported yet
- `OgreOSA:Update` - not ported yet
