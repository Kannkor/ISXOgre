# IRC Remote Commands (AutoLogin / Session Management)

**Added: 2026-04-19**

> **:warning: Untested**
>
> These commands have been written but **not yet tested live**. Treat this as a reference-in-progress. If you try them and something misbehaves, report back and the docs will be updated.

---

## What This Is

Five new IRC commands let you drive AutoLogin and session management on a remote computer from your IRC client. You send `!c <targetclient> -<switch> <args>` in the shared IRC channel; the target machine runs the action locally and echoes responses back through the usual OgreConsole reply path.

They run on the receiving machine (the IRC client you addressed), not on the sender. They are gated by whatever auth your OgreConsoleIRC client already enforces — no new auth scheme was added.

---

## The Commands

| Switch | Purpose |
|---|---|
| `-List_AutoLoginProfiles [-profile <name>] [-details]` | Read and list AutoLogin profiles configured on the target machine. |
| `-LaunchAutoLogin <profile>` | Run a named AutoLogin profile locally. |
| `-OSExecute <command line...>` | Run an arbitrary OS command. |
| `-KillSession <name\|all>` | Kill one named InnerSpace session, or all sessions except the uplink. |
| `-LoadCharacter <toon>[:<session>]` | Log a character into an existing session, or open a new one. Stackable. |

Responses come back through the same OgreConsole reply path as the rest of the `oc` command set — you will see them wherever you normally see OgreConsole output for cross-session commands.

---

## Command Reference

### `-List_AutoLoginProfiles`

Lists AutoLogin profiles configured on the target machine.

| Form | Output |
|---|---|
| `-List_AutoLoginProfiles` | One-line comma-separated list of profile names. |
| `-List_AutoLoginProfiles -details` | Every profile with all of its entries. |
| `-List_AutoLoginProfiles -profile <name>` | Entries of that one profile only. |

**Examples**

```
!c PC1 -List_AutoLoginProfiles
!c PC1 -List_AutoLoginProfiles -details
!c PC1 -List_AutoLoginProfiles -profile RaidGroupA
```

---

### `-LaunchAutoLogin`

Runs the AutoLogin script locally with the given profile name, the same as starting AutoLogin by hand on the target machine.

**Example**

```
!c PC1 -LaunchAutoLogin RaidGroupA
```

If the profile name is missing or invalid, the target replies with an error.

---

### `-OSExecute`

Consumes the entire rest of the message and runs it as an OS command via `OSExecute`. Useful for launching helper scripts, notification scripts, or anything else you would type at a Windows command prompt on the target machine.

> **:warning: No sandboxing**
>
> Whatever you send, the target machine runs. Make sure your IRC auth is tight and you trust everyone on the auth list.

**Examples**

```
!c PC1 -OSExecute notepad.exe
!c PC1 -OSExecute powershell -WindowStyle Hidden -File <path-to-your-script.ps1>
```

---

### `-KillSession`

Kills InnerSpace sessions on the target machine.

**Behavior**

1. Graceful close first.
2. Waits about two seconds.
3. If the session is still alive, force-kills it.

`all` iterates every session and skips the uplink itself, so you will not nuke the machine that is running your IRC client.

**Examples**

```
!c PC1 -KillSession is1
!c PC1 -KillSession all
```

---

### `-LoadCharacter`

Logs a character in. Two modes:

| Syntax | Behavior |
|---|---|
| `-LoadCharacter <toon>` | Opens a brand new InnerSpace session on the target machine and logs that toon in. |
| `-LoadCharacter <toon>:<session>` | If the named session already exists, reuses it and logs the toon in. If the session does **not** exist, falls back to opening a new session. |

The switch is **stackable** — you can pass multiple `-LoadCharacter` tokens in one message to log in multiple characters in one shot.

**Examples**

```
!c PC1 -LoadCharacter Mytank
!c PC1 -LoadCharacter Mytank:is1
!c PC1 -LoadCharacter Mytank:is1 -LoadCharacter Mydps:is2 -LoadCharacter Myheal:is3
```

---

## End-to-End Walkthrough

Scenario: you are away from home, logged into IRC, and want to spin up a raid on your home PC called `PC1`.

```
!c PC1 -List_AutoLoginProfiles
[PC1] AutoLogin Profiles: RaidGroupA, RaidGroupB, Harvesters

!c PC1 -LaunchAutoLogin RaidGroupA
[PC1] LaunchAutoLogin: Launching profile 'RaidGroupA'.
```

Later, you want to swap one character out:

```
!c PC1 -KillSession is3
[PC1] KillSession: Killing session 'is3' (PID 12345).

!c PC1 -LoadCharacter Backupheal:is3
[PC1] LoadCharacter: Opening new session for Backupheal.
```

Or tear everything down at end of night:

```
!c PC1 -KillSession all
[PC1] KillSession: Killing session 'is1' (PID 11111).
[PC1] KillSession: Killing session 'is2' (PID 22222).
[PC1] KillSession: Killing session 'is3' (PID 33333).
```

---

## Known Limitations

- Not tested live yet (see banner at the top).
- `-OSExecute` has no output capture — you see only a "dispatched" confirmation, not the command's stdout.
- Auth is enforced by your IRC client layer. These commands do not add their own auth check, so keep your IRC auth list tight.
